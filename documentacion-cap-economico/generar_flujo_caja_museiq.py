from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import xlsxwriter
from xlsxwriter.utility import xl_rowcol_to_cell


OUT = Path(__file__).resolve().parent / "FLUJO_DE_CAJA_MUSEIQ.xlsx"

YEARS = list(range(1, 11))
YEAR_LABELS = [f"Año {year}" for year in YEARS]

PRICE_ADJUSTMENT = 1.00
ADDITIONAL_SERVICE_RATE = 0.05
ADDITIONAL_SERVICE_COST_RATE = 0.50
INCOME_TAX = 0.295
EXPECTED_INFLATION = 0.02
BCRP_REFERENCE_RATE = 0.0425
EQUITY_RISK_PREMIUM = 0.0575
EQUITY_COST = BCRP_REFERENCE_RATE + EQUITY_RISK_PREMIUM
PROJECT_RISK_PREMIUM = 0.02
LOAN_RATE = 0.1973
LOAN_RATE_STRESS = 0.24
LOAN_SHARE = 0.60
EQUITY_SHARE = 0.40
LOAN_GRACE_YEARS = 2
LOAN_TOTAL_YEARS = 8
INITIAL_INVESTMENT = 300_000.0
TANGIBLE_ASSETS = 118_000.0
INTANGIBLE_ASSETS = 132_000.0
INITIAL_CASH = INITIAL_INVESTMENT - TANGIBLE_ASSETS - INTANGIBLE_ASSETS
SALVAGE_VALUE = 35_000.0
INFLATION = [EXPECTED_INFLATION] * 10
FLOW_ESCALATION = [0.0] * 10
COLLECTION_CASH = 0.40
COLLECTION_CREDIT = 0.60
COLLECTION_CURRENT_CREDIT = 0.80
PURCHASE_CASH = 0.30
PURCHASE_CREDIT = 0.70
PAY_CURRENT_CREDIT = 0.85

# Commercial path aligned with Chapter 5: 35 museums and a 5/20/10 mix.
NEW_BASIC = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
NEW_STANDARD = [0, 0, 2, 2, 3, 1, 2, 3, 3, 4]
NEW_ADVANCED = [2, 2, 1, 1, 0, 2, 1, 0, 1, 0]


@dataclass(frozen=True)
class Package:
    code: str
    name: str
    base_implementation_price: float
    base_recurring_price: float
    implementation_cost: float
    recurring_cost: float
    coverage: str
    beacons: str


PACKAGES = {
    "B": Package("B", "Basico", 48_000, 14_000, 18_000, 6_000, "3 a 5 salas", "8 a 12"),
    "E": Package("E", "Estandar", 96_000, 29_000, 36_000, 11_500, "6 a 10 salas", "18 a 25"),
    "A": Package("A", "Avanzado", 185_000, 52_000, 68_000, 20_000, "12 a 18 salas", "35 a 45"),
}

SOURCES = {
    "bcrp": "https://www.bcrp.gob.pe/",
    "sbs": "https://www.sbs.gob.pe/app/pp/EstadisticasSAEEPortal/Paginas/TIActivaTipoCreditoEmpresa.aspx?tip=B",
    "sunat": "https://renta.sunat.gob.pe/empresas/tasas-de-impuesto",
    "openai": "https://openai.com/api/pricing/",
    "google_stt": "https://cloud.google.com/speech-to-text/pricing",
    "google_tts": "https://cloud.google.com/text-to-speech/pricing",
    "digitalocean": "https://www.digitalocean.com/pricing/droplets",
}


def money(value: float) -> float:
    return round(float(value), 2)


def cached_value(value: float, kind: str) -> float:
    if kind == "integer":
        return int(round(float(value)))
    if kind == "money":
        return money(value)
    return float(value)


def cell(row: int, col: int, *, abs_row: bool = False, abs_col: bool = False) -> str:
    return xl_rowcol_to_cell(row, col, row_abs=abs_row, col_abs=abs_col)


def sheet_cell(sheet: str, row: int, col: int, *, abs_row: bool = False, abs_col: bool = False) -> str:
    return f"'{sheet}'!{cell(row, col, abs_row=abs_row, abs_col=abs_col)}"


def same_row_formula(operator: str, rows: Iterable[int], col: int) -> str:
    refs = [cell(row, col) for row in rows]
    return f"={operator}({','.join(refs)})"


def safe_div(num: float, den: float) -> float:
    return 0.0 if abs(den) < 1e-9 else num / den


def npv(rate: float, flows: list[float]) -> float:
    return sum(flow / ((1 + rate) ** i) for i, flow in enumerate(flows))


def irr(flows: list[float]) -> float:
    low, high = -0.95, 5.0
    previous_rate = low
    previous_value = npv(previous_rate, flows)
    for i in range(1, 30000):
        rate = low + (high - low) * i / 30000
        value = npv(rate, flows)
        if previous_value == 0 or previous_value * value < 0:
            a, b = previous_rate, rate
            for _ in range(100):
                mid = (a + b) / 2
                if npv(a, flows) * npv(mid, flows) <= 0:
                    b = mid
                else:
                    a = mid
            return (a + b) / 2
        previous_rate, previous_value = rate, value
    return float("nan")


def discounted_payback(flows: list[float], rate: float) -> float:
    cumulative = flows[0]
    for index in range(1, len(flows)):
        discounted = flows[index] / ((1 + rate) ** index)
        previous = cumulative
        cumulative += discounted
        if cumulative >= 0:
            return (index - 1) + abs(previous) / discounted
    return float("nan")


def inflation_factors() -> list[float]:
    factors = [1.0]
    for i in range(1, len(YEARS)):
        factors.append(factors[-1] * (1 + FLOW_ESCALATION[i - 1]))
    return factors


def labor_total(monthly_salary: float) -> dict[str, float]:
    annual_salary = monthly_salary * 12
    gratification = monthly_salary * 2
    essalud = annual_salary * 0.09
    cts = (annual_salary + gratification) * 0.0833
    vacations = monthly_salary * 0.50
    severance = monthly_salary * 14 / 12
    social = gratification + essalud + cts + vacations + severance
    return {
        "monthly": monthly_salary,
        "annual": annual_salary,
        "gratification": gratification,
        "essalud": essalud,
        "cts": cts,
        "vacations": vacations,
        "notice": 0.0,
        "severance": severance,
        "social": social,
        "total": annual_salary + social,
    }


def staff_plan(year_index: int) -> dict[str, list[tuple[str, float]]]:
    growth = 1.04**year_index
    admin = [
        ("Gerente general - financiero", 1800 * growth),
        ("Asistente contable administrativo", 900 * growth),
    ]
    if year_index >= 4:
        admin.append(("Coordinador administrativo y contratos", 1200 * (1.04 ** (year_index - 4))))

    production = [
        ("Lider backend, RAG y plataforma", 2500 * growth),
        ("Especialista curatorial y datos", 1300 * growth),
    ]
    if year_index >= 1:
        production.append(("Ingeniero mobile e IoT BLE", 1800 * (1.04 ** (year_index - 1))))
    if year_index >= 2:
        production.append(("Soporte tecnico y QA", 1200 * (1.04 ** (year_index - 2))))
    if year_index >= 5:
        production.append(("Implementador de campo", 1300 * (1.04 ** (year_index - 5))))
    if year_index >= 7:
        production.append(("Analista de datos y soporte IA", 1500 * (1.04 ** (year_index - 7))))

    sales = [("Ejecutivo comercial institucional", 1700 * growth)]
    if year_index >= 3:
        sales.append(("Gestor de relaciones institucionales", 1500 * (1.04 ** (year_index - 3))))
    if year_index >= 7:
        sales.append(("Coordinador postventa y alianzas", 1300 * (1.04 ** (year_index - 7))))

    return {"admin": admin, "production": production, "sales": sales}


def staff_totals(admin_factor: float = 1.0, cost_factor: float = 1.0) -> dict[str, list[float]]:
    totals = {"admin": [], "production": [], "sales": []}
    for i in range(10):
        plan = staff_plan(i)
        totals["admin"].append(sum(labor_total(salary)["total"] for _, salary in plan["admin"]) * admin_factor * cost_factor)
        totals["production"].append(sum(labor_total(salary)["total"] for _, salary in plan["production"]) * cost_factor)
        totals["sales"].append(sum(labor_total(salary)["total"] for _, salary in plan["sales"]) * cost_factor)
    return totals


def debt_schedule(loan: float, annual_rate: float) -> dict[str, list[float]]:
    balance = loan
    amort_years = LOAN_TOTAL_YEARS - LOAN_GRACE_YEARS
    payment = loan * annual_rate / (1 - (1 + annual_rate) ** (-amort_years))
    interest, principal, installment, final_balance, initial_balance = [], [], [], [], []
    for i in range(10):
        initial_balance.append(balance)
        if i < LOAN_GRACE_YEARS:
            year_interest = balance * annual_rate
            year_principal = 0.0
        elif i < LOAN_TOTAL_YEARS:
            year_interest = balance * annual_rate
            year_principal = min(payment - year_interest, balance)
            balance -= year_principal
            if balance < 1e-6:
                balance = 0.0
        else:
            year_interest = 0.0
            year_principal = 0.0
        interest.append(year_interest)
        principal.append(year_principal)
        installment.append(year_interest + year_principal)
        final_balance.append(balance)
    return {
        "initial_balance": initial_balance,
        "interest": interest,
        "principal": principal,
        "installment": installment,
        "final_balance": final_balance,
    }


def asset_schedules() -> dict[str, list[float] | float]:
    fixed_assets = [
        ("Laptops y equipos de prueba", 48_000.0, 4),
        ("Servidor/NAS y red local", 32_000.0, 5),
        ("Herramientas de instalacion y medicion", 20_000.0, 5),
        ("Mobiliario y oficina", 18_000.0, 10),
    ]
    intangibles = [
        ("Constitucion y formalizacion", 8_000.0, 5),
        ("Desarrollo base app/API/RAG", 90_000.0, 5),
        ("Documentacion y manuales", 22_000.0, 5),
        ("Marca, preventa y dossier comercial", 12_000.0, 5),
    ]

    depreciation = [0.0] * 10
    amortization = [0.0] * 10
    fixed_net = []
    intangible_net = []
    fixed_accum = 0.0
    intangible_accum = 0.0
    for i in range(10):
        depreciation[i] = sum(value / life for _, value, life in fixed_assets if i < life)
        amortization[i] = sum(value / life for _, value, life in intangibles if i < life)
        fixed_accum += depreciation[i]
        intangible_accum += amortization[i]
        fixed_net.append(max(0.0, TANGIBLE_ASSETS - fixed_accum))
        intangible_net.append(max(0.0, INTANGIBLE_ASSETS - intangible_accum))
    return {
        "fixed_assets": fixed_assets,
        "intangibles": intangibles,
        "depreciation": depreciation,
        "amortization": amortization,
        "fixed_net": fixed_net,
        "intangible_net": intangible_net,
        "fixed_total": TANGIBLE_ASSETS,
        "intangible_total": INTANGIBLE_ASSETS,
    }


def build_model(
    *,
    name: str = "Base",
    revenue_factor: float = 1.0,
    cost_factor: float = 1.0,
    price_adjustment: float = PRICE_ADJUSTMENT,
    interest_rate: float = LOAN_RATE,
    admin_factor: float = 1.0,
    bad_debt_rate: float = 0.0,
) -> dict[str, object]:
    factors = inflation_factors()
    staff = staff_totals(admin_factor=admin_factor, cost_factor=cost_factor)
    assets = asset_schedules()
    loan = INITIAL_INVESTMENT * LOAN_SHARE
    equity = INITIAL_INVESTMENT * EQUITY_SHARE
    debt = debt_schedule(loan, interest_rate)

    new = {"B": NEW_BASIC[:], "E": NEW_STANDARD[:], "A": NEW_ADVANCED[:]}
    cumulative = {"B": 0, "E": 0, "A": 0}
    active_end = {key: [] for key in new}
    effective = {key: [] for key in new}
    total_new, total_active = [], []

    sales_impl, sales_rec, sales_extra, sales_total = [], [], [], []
    direct_impl_cost, direct_rec_cost, direct_extra_cost, direct_total = [], [], [], []
    cash_sales, credit_sales, current_credit_collection = [], [], []
    previous_cxc_collection, cxc_end, cash_income = [], [], []
    purchase_cash, purchase_credit, current_supplier_payment = [], [], []
    previous_supplier_payment, cxp_end, supplier_cash_payment = [], [], []
    production_labor, admin_labor, sales_labor = [], [], []
    admin_other, sales_other, sales_commission = [], [], []
    energy, platform_tools, supplies, maintenance, indirect_cash, indirect_total = [], [], [], [], [], []
    cost_of_production, cost_of_sales = [], []
    operating_expenses, ebit, ebt, income_tax = [], [], [], []
    cash_tax_paid, cash_egress, cash_budget_flow = [], [], []
    reserve_legal, reserve_accum, retained_profit = [], [], []
    current_debt = []

    previous_cxc = 0.0
    previous_cxp = 0.0
    reserve_limit = equity * 0.20
    reserve_acc = 0.0

    for i in range(10):
        year_new = 0
        year_active = 0
        for key in new:
            effective[key].append(cumulative[key] + 0.5 * new[key][i])
            cumulative[key] += new[key][i]
            active_end[key].append(cumulative[key])
            year_new += new[key][i]
            year_active += cumulative[key]
        total_new.append(year_new)
        total_active.append(year_active)

        impl = sum(
            new[key][i] * PACKAGES[key].base_implementation_price * price_adjustment * factors[i]
            for key in new
        ) * revenue_factor
        rec = sum(
            effective[key][i] * PACKAGES[key].base_recurring_price * price_adjustment * factors[i]
            for key in new
        ) * revenue_factor
        extra = impl * ADDITIONAL_SERVICE_RATE
        total_sales_year = impl + rec + extra
        sales_impl.append(impl)
        sales_rec.append(rec)
        sales_extra.append(extra)
        sales_total.append(total_sales_year)

        contado = total_sales_year * COLLECTION_CASH
        credito = total_sales_year * COLLECTION_CREDIT
        current_credit = credito * COLLECTION_CURRENT_CREDIT * (1 - bad_debt_rate)
        prior_collection = previous_cxc * (1 - bad_debt_rate)
        ending_cxc = credito * (1 - COLLECTION_CURRENT_CREDIT)
        cash_sales.append(contado)
        credit_sales.append(credito)
        current_credit_collection.append(current_credit)
        previous_cxc_collection.append(prior_collection)
        cxc_end.append(ending_cxc)
        cash_income.append(contado + current_credit + prior_collection)

        impl_cost = sum(new[key][i] * PACKAGES[key].implementation_cost * factors[i] for key in new) * cost_factor
        rec_cost = sum(effective[key][i] * PACKAGES[key].recurring_cost * factors[i] for key in new) * cost_factor
        extra_cost = extra * ADDITIONAL_SERVICE_COST_RATE * cost_factor
        direct_cost = impl_cost + rec_cost + extra_cost
        direct_impl_cost.append(impl_cost)
        direct_rec_cost.append(rec_cost)
        direct_extra_cost.append(extra_cost)
        direct_total.append(direct_cost)

        cash_purchase = direct_cost * PURCHASE_CASH
        credit_purchase = direct_cost * PURCHASE_CREDIT
        current_payment = credit_purchase * PAY_CURRENT_CREDIT
        ending_cxp = credit_purchase * (1 - PAY_CURRENT_CREDIT)
        purchase_cash.append(cash_purchase)
        purchase_credit.append(credit_purchase)
        current_supplier_payment.append(current_payment)
        previous_supplier_payment.append(previous_cxp)
        cxp_end.append(ending_cxp)
        supplier_cash_payment.append(cash_purchase + current_payment + previous_cxp)

        admin_labor.append(staff["admin"][i])
        production_labor.append(staff["production"][i])
        sales_labor.append(staff["sales"][i])
        admin_other.append(16_000 * (1.04**i) * cost_factor * admin_factor)
        commission = total_sales_year * 0.025 * cost_factor
        sales_commission.append(commission)
        sales_other.append((16_000 * (1.04**i) * cost_factor) + commission)

        energy.append(20_000 * (1.04**i) * cost_factor)
        platform_tools.append((0 if i == 0 else 9_000 * (1.04 ** (i - 1))) * cost_factor)
        supplies.append(3_800 * (1.04**i) * cost_factor)
        maintenance.append(4_500 * (1.04**i) * cost_factor)
        indirect_cash_year = energy[i] + platform_tools[i] + supplies[i] + maintenance[i]
        indirect_cash.append(indirect_cash_year)
        indirect_total.append(indirect_cash_year + assets["depreciation"][i] * 0.60)

        prod_cost = direct_cost + production_labor[i] + indirect_total[i]
        cost_of_production.append(prod_cost)
        cost_of_sales.append(prod_cost)
        op_exp = admin_labor[i] + admin_other[i] + sales_labor[i] + sales_other[i] + assets["depreciation"][i] * 0.40 + assets["amortization"][i]
        operating_expenses.append(op_exp)
        ebit_year = total_sales_year - cost_of_sales[i] - op_exp
        ebit.append(ebit_year)
        ebt_year = ebit_year - debt["interest"][i]
        ebt.append(ebt_year)
        tax_year = max(0.0, ebt_year * INCOME_TAX)
        income_tax.append(tax_year)
        cash_tax_paid.append(0.0 if i == 0 else income_tax[i - 1])
        current_debt.append(debt["principal"][i + 1] if i + 1 < LOAN_TOTAL_YEARS else 0.0)

        net_income = ebt_year - tax_year
        legal = min(max(0.0, net_income * 0.10), max(0.0, reserve_limit - reserve_acc))
        reserve_acc += legal
        reserve_legal.append(legal)
        reserve_accum.append(reserve_acc)
        retained_profit.append(net_income - legal)

        cash_out = (
            supplier_cash_payment[i]
            + production_labor[i]
            + indirect_cash[i]
            + admin_labor[i]
            + admin_other[i]
            + sales_labor[i]
            + sales_other[i]
            + debt["interest"][i]
            + debt["principal"][i]
            + cash_tax_paid[i]
        )
        cash_egress.append(cash_out)
        cash_budget_flow.append(cash_income[i] - cash_out)

        previous_cxc = ending_cxc
        previous_cxp = ending_cxp

    cash_balance = [INITIAL_CASH]
    for i in range(10):
        cash_balance.append(cash_balance[-1] + cash_budget_flow[i])

    final_current_liabilities = cxp_end[-1] + income_tax[-1]
    flow_net = []
    for i in range(10):
        terminal = cxc_end[i] + SALVAGE_VALUE - final_current_liabilities if i == 9 else 0.0
        flow_net.append(cash_income[i] - cash_egress[i] + terminal)
    flows_for_valuation = [-INITIAL_INVESTMENT] + flow_net

    nominal_wacc = (
        EQUITY_SHARE * EQUITY_COST
        + LOAN_SHARE * interest_rate * (1 - INCOME_TAX)
    )
    avg_inflation = sum(INFLATION) / len(INFLATION)
    real_wacc = (1 + nominal_wacc) / (1 + avg_inflation) - 1
    risk = PROJECT_RISK_PREMIUM
    cut_rate = (1 + real_wacc) * (1 + risk) - 1
    model_npv = npv(cut_rate, flows_for_valuation)
    model_irr = irr(flows_for_valuation)
    profitability_index = (model_npv + INITIAL_INVESTMENT) / INITIAL_INVESTMENT
    payback = discounted_payback(flows_for_valuation, cut_rate)

    net_income = [ebt[i] - income_tax[i] for i in range(10)]
    gross_profit = [sales_total[i] - cost_of_sales[i] for i in range(10)]
    current_assets = [cash_balance[i + 1] + cxc_end[i] for i in range(10)]
    current_liabilities = [cxp_end[i] + current_debt[i] + income_tax[i] for i in range(10)]
    fixed_net = assets["fixed_net"]
    intangible_net = assets["intangible_net"]
    total_assets = [current_assets[i] + fixed_net[i] + intangible_net[i] for i in range(10)]
    long_debt = [max(0.0, debt["final_balance"][i] - (debt["principal"][i + 1] if i + 1 < 10 else 0.0)) for i in range(10)]
    total_liabilities = [current_liabilities[i] + long_debt[i] for i in range(10)]
    accumulated_retained = []
    acc = 0.0
    for value in retained_profit:
        acc += value
        accumulated_retained.append(acc)
    equity_values = [equity + reserve_accum[i] + accumulated_retained[i] for i in range(10)]
    balance_gap = [total_assets[i] - total_liabilities[i] - equity_values[i] for i in range(10)]

    variable_costs = [direct_total[i] + production_labor[i] * 0.70 + indirect_cash[i] * 0.60 for i in range(10)]
    fixed_costs = [
        production_labor[i] * 0.30
        + indirect_cash[i] * 0.40
        + admin_labor[i]
        + admin_other[i]
        + sales_labor[i]
        + sales_other[i]
        + debt["interest"][i]
        for i in range(10)
    ]
    contribution_margin = [1 - safe_div(variable_costs[i], sales_total[i]) for i in range(10)]
    break_even_sales = [safe_div(fixed_costs[i], contribution_margin[i]) for i in range(10)]
    equivalent_museums = [safe_div(sales_total[i], max(1.0, total_new[i] + sum(effective[key][i] for key in new))) for i in range(10)]
    break_even_units = [safe_div(break_even_sales[i], equivalent_museums[i]) for i in range(10)]
    break_even_pct = [safe_div(break_even_sales[i], sales_total[i]) for i in range(10)]

    return {
        "name": name,
        "factors": factors,
        "new": new,
        "active_end": active_end,
        "effective": effective,
        "total_new": total_new,
        "total_active": total_active,
        "sales_impl": sales_impl,
        "sales_rec": sales_rec,
        "sales_extra": sales_extra,
        "sales_total": sales_total,
        "cash_sales": cash_sales,
        "credit_sales": credit_sales,
        "current_credit_collection": current_credit_collection,
        "previous_cxc_collection": previous_cxc_collection,
        "cxc_end": cxc_end,
        "cash_income": cash_income,
        "direct_impl_cost": direct_impl_cost,
        "direct_rec_cost": direct_rec_cost,
        "direct_extra_cost": direct_extra_cost,
        "direct_total": direct_total,
        "purchase_cash": purchase_cash,
        "purchase_credit": purchase_credit,
        "current_supplier_payment": current_supplier_payment,
        "previous_supplier_payment": previous_supplier_payment,
        "cxp_end": cxp_end,
        "supplier_cash_payment": supplier_cash_payment,
        "production_labor": production_labor,
        "admin_labor": admin_labor,
        "sales_labor": sales_labor,
        "admin_other": admin_other,
        "sales_other": sales_other,
        "sales_commission": sales_commission,
        "energy": energy,
        "platform_tools": platform_tools,
        "supplies": supplies,
        "maintenance": maintenance,
        "indirect_cash": indirect_cash,
        "indirect_total": indirect_total,
        "cost_of_production": cost_of_production,
        "cost_of_sales": cost_of_sales,
        "operating_expenses": operating_expenses,
        "gross_profit": gross_profit,
        "ebit": ebit,
        "ebt": ebt,
        "income_tax": income_tax,
        "cash_tax_paid": cash_tax_paid,
        "cash_egress": cash_egress,
        "cash_budget_flow": cash_budget_flow,
        "cash_balance": cash_balance,
        "reserve_legal": reserve_legal,
        "reserve_accum": reserve_accum,
        "retained_profit": retained_profit,
        "net_income": net_income,
        "debt": debt,
        "loan": loan,
        "equity": equity,
        "assets": assets,
        "flow_net": flow_net,
        "flows_for_valuation": flows_for_valuation,
        "cost_capital": nominal_wacc,
        "real_cost_capital": real_wacc,
        "avg_inflation": avg_inflation,
        "risk": risk,
        "cut_rate": cut_rate,
        "npv": model_npv,
        "irr": model_irr,
        "profitability_index": profitability_index,
        "payback": payback,
        "current_assets": current_assets,
        "current_liabilities": current_liabilities,
        "current_debt": current_debt,
        "fixed_net": fixed_net,
        "intangible_net": intangible_net,
        "total_assets": total_assets,
        "long_debt": long_debt,
        "total_liabilities": total_liabilities,
        "equity_values": equity_values,
        "balance_gap": balance_gap,
        "variable_costs": variable_costs,
        "fixed_costs": fixed_costs,
        "contribution_margin": contribution_margin,
        "break_even_sales": break_even_sales,
        "equivalent_museums": equivalent_museums,
        "break_even_units": break_even_units,
        "break_even_pct": break_even_pct,
        "price_adjustment": price_adjustment,
        "interest_rate": interest_rate,
        "bad_debt_rate": bad_debt_rate,
    }


def make_formats(workbook: xlsxwriter.Workbook) -> dict[str, object]:
    return {
        "title": workbook.add_format({"bold": True, "font_color": "white", "bg_color": "#006E9E", "align": "center", "valign": "vcenter", "border": 1}),
        "subtitle": workbook.add_format({"bold": True, "font_color": "white", "bg_color": "#008CC7", "align": "center", "border": 1}),
        "header": workbook.add_format({"bold": True, "font_color": "white", "bg_color": "#00A6CF", "align": "center", "border": 1}),
        "label": workbook.add_format({"border": 1, "bg_color": "#EAF8FC"}),
        "text": workbook.add_format({"border": 1, "text_wrap": True, "valign": "top"}),
        "money": workbook.add_format({"border": 1, "num_format": '"S/" #,##0;[Red]-"S/" #,##0'}),
        "money_blue": workbook.add_format({"border": 1, "bg_color": "#CDEFF8", "num_format": '"S/" #,##0;[Red]-"S/" #,##0'}),
        "number": workbook.add_format({"border": 1, "num_format": "#,##0.00"}),
        "integer": workbook.add_format({"border": 1, "num_format": "#,##0"}),
        "percent": workbook.add_format({"border": 1, "num_format": "0.00%"}),
        "total": workbook.add_format({"bold": True, "font_color": "white", "bg_color": "#008CC7", "border": 1, "num_format": '"S/" #,##0;[Red]-"S/" #,##0'}),
        "total_num": workbook.add_format({"bold": True, "font_color": "white", "bg_color": "#008CC7", "border": 1, "num_format": "#,##0.00"}),
        "total_pct": workbook.add_format({"bold": True, "font_color": "white", "bg_color": "#008CC7", "border": 1, "num_format": "0.00%"}),
        "note": workbook.add_format({"italic": True, "font_color": "#3D4B54", "text_wrap": True}),
        "input": workbook.add_format({"border": 1, "bg_color": "#FFF2CC", "num_format": "#,##0.00"}),
        "input_money": workbook.add_format({"border": 1, "bg_color": "#FFF2CC", "num_format": '"S/" #,##0;[Red]-"S/" #,##0'}),
        "input_pct": workbook.add_format({"border": 1, "bg_color": "#FFF2CC", "num_format": "0.00%"}),
        "formula": workbook.add_format({"border": 1, "bg_color": "#E2F0D9", "num_format": "#,##0.00"}),
        "formula_money": workbook.add_format({"border": 1, "bg_color": "#E2F0D9", "num_format": '"S/" #,##0;[Red]-"S/" #,##0'}),
        "formula_pct": workbook.add_format({"border": 1, "bg_color": "#E2F0D9", "num_format": "0.00%"}),
        "url": workbook.add_format({"font_color": "blue", "underline": True, "text_wrap": True, "valign": "top", "border": 1}),
    }


def setup(ws, title: str, formats: dict[str, object], last_col: int = 11) -> None:
    ws.set_zoom(90)
    ws.freeze_panes(3, 1)
    ws.set_column(0, 0, 36)
    ws.set_column(1, last_col, 13)
    ws.merge_range(0, 0, 0, last_col, title, formats["title"])


def write_year_header(ws, row: int, formats: dict[str, object], first_label: str = "Concepto", year0: bool = False) -> int:
    labels = [first_label] + (["Año 0"] if year0 else []) + YEAR_LABELS
    for col, label in enumerate(labels):
        ws.write(row, col, label, formats["header"])
    return row + 1


def write_series(
    ws,
    row: int,
    label: str,
    values: Iterable[float],
    formats: dict[str, object],
    *,
    kind: str = "money",
    total: bool = False,
    first_col: int = 1,
    formulas: Iterable[str] | None = None,
) -> int:
    ws.write(row, 0, label, formats["total"] if total and kind == "money" else formats["label"])
    fmt = formats["total"] if total and kind == "money" else formats["money"]
    if kind == "integer":
        fmt = formats["total_num"] if total else formats["integer"]
    elif kind == "number":
        fmt = formats["total_num"] if total else formats["number"]
    elif kind == "percent":
        fmt = formats["total_pct"] if total else formats["percent"]
    formula_values = list(formulas) if formulas is not None else None
    for index, value in enumerate(values):
        col = first_col + index
        cached = cached_value(value, kind)
        if formula_values is None:
            ws.write_number(row, col, cached, fmt)
        else:
            ws.write_formula(row, col, formula_values[index], fmt, cached)
    return row + 1


def write_section(ws, row: int, title: str, formats: dict[str, object], last_col: int = 10) -> int:
    ws.merge_range(row, 0, row, last_col, title, formats["subtitle"])
    return row + 1


def define_cell_name(workbook, name: str, row: int, col: int = 1) -> None:
    workbook.define_name(name, f"=SUPUESTOS!${xlsxwriter.utility.xl_col_to_name(col)}${row + 1}")


def write_assumptions(workbook, model, formats):
    ws = workbook.add_worksheet("SUPUESTOS")
    setup(ws, "Supuestos editables y fuentes del modelo MuseIQ", formats, 12)
    ws.freeze_panes(4, 1)
    ws.set_column(0, 0, 40)
    ws.set_column(1, 2, 18)
    ws.set_column(3, 3, 56)
    ws.set_column(4, 4, 70)
    ws.write(1, 0, "Celdas amarillas: entradas editables. Celdas verdes: resultados calculados por formula.", formats["note"])

    row = 3
    row = write_section(ws, row, "PARAMETROS COMERCIALES Y OPERATIVOS", formats, 4)
    for col, label in enumerate(["Concepto", "Valor", "Unidad", "Criterio", "Fuente"]):
        ws.write(row, col, label, formats["header"])
    row += 1

    commercial = [
        ("Factor aplicado a precios base", PRICE_ADJUSTMENT, "factor", "Se elimina el recargo adicional de 20% del libro anterior.", "Capitulo 5"),
        ("Servicios adicionales sobre implementacion", ADDITIONAL_SERVICE_RATE, "%", "Escenario prudente para ampliaciones y capacitacion.", "Supuesto de tesis"),
        ("Costo directo de servicios adicionales", ADDITIONAL_SERVICE_COST_RATE, "%", "Participacion de curaduria, capacitacion y despliegue.", "Supuesto operativo"),
        ("Ventas al contado", COLLECTION_CASH, "%", "Cobro inicial o contra hitos.", "Politica comercial"),
        ("Ventas al credito", COLLECTION_CREDIT, "%", "Saldo sujeto a conformidad institucional.", "Politica comercial"),
        ("Cobro del credito dentro del año", COLLECTION_CURRENT_CREDIT, "%", "El remanente queda como cuenta por cobrar.", "Politica comercial"),
        ("Compras y servicios pagados al contado", PURCHASE_CASH, "%", "Estructura de pagos a proveedores.", "Supuesto operativo"),
        ("Credito de proveedores pagado en el año", PAY_CURRENT_CREDIT, "%", "El remanente queda como cuenta por pagar.", "Supuesto operativo"),
        ("Escalamiento anual de flujos reales", FLOW_ESCALATION[0], "%", "Cero porque los flujos se expresan en soles constantes de 2026.", "Criterio metodologico"),
        ("Inflacion esperada de largo plazo", EXPECTED_INFLATION, "%", "Punto medio del rango meta de inflacion de 1% a 3%.", SOURCES["bcrp"]),
    ]
    commercial_names = [
        "factor_precio_base",
        "tasa_servicios_adicionales",
        "tasa_costo_servicios_adicionales",
        "porcentaje_ventas_contado",
        "porcentaje_ventas_credito",
        "porcentaje_cobro_credito_actual",
        "porcentaje_compras_contado",
        "porcentaje_pago_proveedor_actual",
        "escalamiento_flujos",
        "inflacion_esperada",
    ]
    for (label, value, unit, criterion, source), name in zip(commercial, commercial_names):
        ws.write(row, 0, label, formats["label"])
        value_format = formats["input_pct"] if unit == "%" else formats["input"]
        ws.write_number(row, 1, value, value_format)
        ws.write(row, 2, unit, formats["text"])
        ws.write(row, 3, criterion, formats["text"])
        if source.startswith("http"):
            ws.write_url(row, 4, source, formats["url"], string=source)
        else:
            ws.write(row, 4, source, formats["text"])
        define_cell_name(workbook, name, row)
        row += 1

    row += 1
    row = write_section(ws, row, "FINANCIAMIENTO, IMPUESTOS Y TASA DE CORTE", formats, 4)
    for col, label in enumerate(["Concepto", "Valor", "Unidad", "Formula o sustento", "Fuente"]):
        ws.write(row, col, label, formats["header"])
    row += 1

    financial_inputs = [
        ("Inversion inicial", INITIAL_INVESTMENT, "S/", "Activos tangibles + intangibles + caja inicial.", "Modelo MuseIQ"),
        ("Activos tangibles", TANGIBLE_ASSETS, "S/", "Equipos, servidor, herramientas y mobiliario.", "Modelo MuseIQ"),
        ("Activos intangibles", INTANGIBLE_ASSETS, "S/", "Desarrollo base, documentacion y formalizacion.", "Modelo MuseIQ"),
        ("Valor de salvamento", SALVAGE_VALUE, "S/", "Valor residual conservador al cierre del año 10.", "Modelo MuseIQ"),
        ("Participacion de fondos propios", EQUITY_SHARE, "%", "Estructura de financiamiento.", "Supuesto financiero"),
        ("Participacion de deuda", LOAN_SHARE, "%", "Estructura de financiamiento.", "Supuesto financiero"),
        ("Tasa de referencia BCRP", BCRP_REFERENCE_RATE, "%", "Referencia macroeconomica al 11/06/2026.", SOURCES["bcrp"]),
        ("Prima de riesgo del capital propio", EQUITY_RISK_PREMIUM, "%", "Riesgo comercial, tecnologico y de adopcion institucional.", "Criterio conservador"),
        ("Tasa bancaria para pequeña empresa", LOAN_RATE, "%", "Promedio SBS en moneda nacional al 17/06/2026.", SOURCES["sbs"]),
        ("Prima especifica del proyecto", PROJECT_RISK_PREMIUM, "%", "Riesgo residual adicional al WACC real.", "Criterio conservador"),
        ("Impuesto a la renta", INCOME_TAX, "%", "Regimen General empresarial.", SOURCES["sunat"]),
    ]
    financial_names = [
        "inversion_inicial",
        "activos_tangibles",
        "activos_intangibles",
        "valor_salvamento",
        "participacion_capital",
        "participacion_deuda",
        "tasa_referencia_bcrp",
        "prima_capital_propio",
        "tasa_deuda",
        "prima_riesgo_proyecto",
        "tasa_impuesto_renta",
    ]
    for (label, value, unit, criterion, source), name in zip(financial_inputs, financial_names):
        ws.write(row, 0, label, formats["label"])
        if unit == "%":
            value_format = formats["input_pct"]
        elif unit == "S/":
            value_format = formats["input_money"]
        else:
            value_format = formats["input"]
        ws.write_number(row, 1, value, value_format)
        ws.write(row, 2, unit, formats["text"])
        ws.write(row, 3, criterion, formats["text"])
        if source.startswith("http"):
            ws.write_url(row, 4, source, formats["url"], string=source)
        else:
            ws.write(row, 4, source, formats["text"])
        define_cell_name(workbook, name, row)
        row += 1

    ws.write(row, 0, "Capital de trabajo inicial", formats["label"])
    ws.write_formula(row, 1, "=inversion_inicial-activos_tangibles-activos_intangibles", formats["formula_money"], INITIAL_CASH)
    ws.write(row, 2, "S/", formats["text"])
    ws.write(row, 3, "Liquidez inicial obtenida por diferencia.", formats["text"])
    define_cell_name(workbook, "capital_trabajo_inicial", row)
    row += 1

    cost_equity_row = row
    ws.write(row, 0, "Costo de capital propio", formats["label"])
    ws.write_formula(row, 1, "=tasa_referencia_bcrp+prima_capital_propio", formats["formula_pct"], EQUITY_COST)
    ws.write(row, 2, "%", formats["text"])
    ws.write(row, 3, "Ke = tasa de referencia BCRP + prima de riesgo del capital propio.", formats["text"])
    define_cell_name(workbook, "costo_capital_propio", row)
    row += 1

    nominal_wacc_row = row
    ws.write(row, 0, "WACC nominal despues de impuestos", formats["label"])
    ws.write_formula(
        row,
        1,
        "=participacion_capital*costo_capital_propio+participacion_deuda*tasa_deuda*(1-tasa_impuesto_renta)",
        formats["formula_pct"],
        model["cost_capital"],
    )
    ws.write(row, 2, "%", formats["text"])
    ws.write(row, 3, "WACC = E/V x Ke + D/V x Kd x (1-IR).", formats["text"])
    define_cell_name(workbook, "wacc_nominal", row)
    row += 1

    real_wacc_row = row
    ws.write(row, 0, "WACC real", formats["label"])
    ws.write_formula(row, 1, "=(1+wacc_nominal)/(1+inflacion_esperada)-1", formats["formula_pct"], model["real_cost_capital"])
    ws.write(row, 2, "%", formats["text"])
    ws.write(row, 3, "Conversion de Fisher para flujos en soles constantes.", formats["text"])
    define_cell_name(workbook, "wacc_real", row)
    row += 1

    ws.write(row, 0, "Tasa de corte real", formats["total"])
    ws.write_formula(row, 1, "=(1+wacc_real)*(1+prima_riesgo_proyecto)-1", formats["total_pct"], model["cut_rate"])
    ws.write(row, 2, "%", formats["text"])
    ws.write(row, 3, "Tasa usada para descontar los flujos reales del proyecto.", formats["text"])
    define_cell_name(workbook, "tasa_corte", row)
    row += 2

    row = write_section(ws, row, "PAQUETES, PRECIOS Y COSTOS DIRECTOS", formats, 8)
    headers = ["Paquete", "Precio implementacion", "Costo directo implementacion", "Margen contribucion", "Precio recurrente", "Costo directo recurrente", "Margen recurrente", "Cobertura", "BLE"]
    for col, label in enumerate(headers):
        ws.write(row, col, label, formats["header"])
    row += 1
    package_rows = {}
    for key in ["B", "E", "A"]:
        pkg = PACKAGES[key]
        package_rows[key] = row
        ws.write(row, 0, pkg.name, formats["label"])
        ws.write_number(row, 1, pkg.base_implementation_price, formats["input_money"])
        ws.write_number(row, 2, pkg.implementation_cost, formats["input_money"])
        ws.write_formula(row, 3, f"=1-C{row + 1}/B{row + 1}", formats["formula_pct"], 1 - pkg.implementation_cost / pkg.base_implementation_price)
        ws.write_number(row, 4, pkg.base_recurring_price, formats["input_money"])
        ws.write_number(row, 5, pkg.recurring_cost, formats["input_money"])
        ws.write_formula(row, 6, f"=1-F{row + 1}/E{row + 1}", formats["formula_pct"], 1 - pkg.recurring_cost / pkg.base_recurring_price)
        ws.write(row, 7, pkg.coverage, formats["text"])
        ws.write(row, 8, pkg.beacons, formats["text"])
        define_cell_name(workbook, f"precio_impl_{key}", row, 1)
        define_cell_name(workbook, f"costo_impl_{key}", row, 2)
        define_cell_name(workbook, f"precio_rec_{key}", row, 4)
        define_cell_name(workbook, f"costo_rec_{key}", row, 5)
        row += 1

    row += 1
    row = write_section(ws, row, "CRONOGRAMA DE CAPTACION ALINEADO CON EL CAPITULO 5", formats, 10)
    ws.write(row, 0, "Paquete", formats["header"])
    for col, label in enumerate(YEAR_LABELS, start=1):
        ws.write(row, col, label, formats["header"])
    ws.write(row, 11, "Total", formats["header"])
    row += 1
    schedule_rows = {}
    for key, label in [("B", "Basico"), ("E", "Estandar"), ("A", "Avanzado")]:
        schedule_rows[key] = row
        ws.write(row, 0, label, formats["label"])
        for col, value in enumerate({"B": NEW_BASIC, "E": NEW_STANDARD, "A": NEW_ADVANCED}[key], start=1):
            ws.write_number(row, col, value, formats["input"])
        ws.write_formula(row, 11, f"=SUM(B{row + 1}:K{row + 1})", formats["total_num"], sum({"B": NEW_BASIC, "E": NEW_STANDARD, "A": NEW_ADVANCED}[key]))
        workbook.define_name(f"nuevos_{key}", f"=SUPUESTOS!$B${row + 1}:$K${row + 1}")
        row += 1
    ws.write(row, 0, "TOTAL MUSEOS", formats["total"])
    for col in range(1, 11):
        ws.write_formula(row, col, f"=SUM({cell(schedule_rows['B'], col)}:{cell(schedule_rows['A'], col)})", formats["total_num"], model["total_new"][col - 1])
    ws.write_formula(row, 11, f"=SUM(L{schedule_rows['B'] + 1}:L{schedule_rows['A'] + 1})", formats["total_num"], sum(model["total_new"]))

    row += 2
    row = write_section(ws, row, "REFERENCIAS DE COSTOS TECNOLOGICOS", formats, 4)
    ws.write(row, 0, "Componente", formats["header"])
    ws.write(row, 1, "Referencia verificable", formats["header"])
    ws.write(row, 2, "Dato usado para contrastar", formats["header"])
    ws.write(row, 3, "Uso en el modelo", formats["header"])
    row += 1
    references = [
        ("Speech-to-Text", SOURCES["google_stt"], "US$0.016 por minuto en reconocimiento estandar", "Parte del costo recurrente"),
        ("Text-to-Speech", SOURCES["google_tts"], "Desde US$4 por millon de caracteres en voces estandar", "Parte del costo recurrente"),
        ("API de modelos y embeddings", SOURCES["openai"], "Tarifas por tokens segun modelo", "Consultas RAG y embeddings"),
        ("Servidor cloud", SOURCES["digitalocean"], "Droplets basicos desde US$4 por mes", "Hosting, monitoreo y respaldo"),
    ]
    for component, source, datum, use in references:
        ws.write(row, 0, component, formats["label"])
        ws.write_url(row, 1, source, formats["url"], string=source)
        ws.write(row, 2, datum, formats["text"])
        ws.write(row, 3, use, formats["text"])
        row += 1

    ws.autofilter(4, 0, 4 + len(commercial), 4)


def write_ingresos(workbook, model, formats):
    ws = workbook.add_worksheet("INGRESOS")
    setup(ws, "Servicio de Implementacion MuseIQ - Soporte, IA y Analitica", formats, 11)
    row = 2
    row = write_section(ws, row, "PROYECCION DE INGRESOS - IMPLEMENTACION MUSEIQ", formats)
    row = write_year_header(ws, row, formats)
    new_basic_row = row
    row = write_series(
        ws,
        row,
        "Museos nuevos - Basico",
        model["new"]["B"],
        formats,
        kind="integer",
        formulas=[f"=INDEX(nuevos_B,1,{col})" for col in range(1, 11)],
    )
    new_standard_row = row
    row = write_series(
        ws,
        row,
        "Museos nuevos - Estandar",
        model["new"]["E"],
        formats,
        kind="integer",
        formulas=[f"=INDEX(nuevos_E,1,{col})" for col in range(1, 11)],
    )
    new_advanced_row = row
    row = write_series(
        ws,
        row,
        "Museos nuevos - Avanzado",
        model["new"]["A"],
        formats,
        kind="integer",
        formulas=[f"=INDEX(nuevos_A,1,{col})" for col in range(1, 11)],
    )
    total_new_row = row
    row = write_series(
        ws,
        row,
        "Total museos implementados por año",
        model["total_new"],
        formats,
        kind="integer",
        total=True,
        formulas=[same_row_formula("SUM", [new_basic_row, new_standard_row, new_advanced_row], col) for col in range(1, 11)],
    )
    sales_impl_row = row
    row = write_series(ws, row, "Ventas implementacion MuseIQ", model["sales_impl"], formats, total=True)
    sales_extra_row = row
    row = write_series(
        ws,
        row,
        "Servicios adicionales de despliegue",
        model["sales_extra"],
        formats,
        formulas=[f"={cell(sales_impl_row, col)}*tasa_servicios_adicionales" for col in range(1, 11)],
    )
    row += 1
    row = write_section(ws, row, "INGRESOS - SOPORTE, IA Y ANALITICA", formats)
    row = write_year_header(ws, row, formats)
    active_row = row
    row = write_series(
        ws,
        row,
        "Museos activos al cierre",
        model["total_active"],
        formats,
        kind="integer",
        formulas=[f"=SUM($B${total_new_row + 1}:{cell(total_new_row, col)})" for col in range(1, 11)],
    )
    effective_basic_row = row
    row = write_series(
        ws,
        row,
        "Museos equivalentes recurrentes - Basico",
        model["effective"]["B"],
        formats,
        kind="number",
        formulas=[
            f"={cell(new_basic_row, col)}*0.5" if col == 1 else f"=SUM($B${new_basic_row + 1}:{cell(new_basic_row, col - 1)})+{cell(new_basic_row, col)}*0.5"
            for col in range(1, 11)
        ],
    )
    effective_standard_row = row
    row = write_series(
        ws,
        row,
        "Museos equivalentes recurrentes - Estandar",
        model["effective"]["E"],
        formats,
        kind="number",
        formulas=[
            f"={cell(new_standard_row, col)}*0.5" if col == 1 else f"=SUM($B${new_standard_row + 1}:{cell(new_standard_row, col - 1)})+{cell(new_standard_row, col)}*0.5"
            for col in range(1, 11)
        ],
    )
    effective_advanced_row = row
    row = write_series(
        ws,
        row,
        "Museos equivalentes recurrentes - Avanzado",
        model["effective"]["A"],
        formats,
        kind="number",
        formulas=[
            f"={cell(new_advanced_row, col)}*0.5" if col == 1 else f"=SUM($B${new_advanced_row + 1}:{cell(new_advanced_row, col - 1)})+{cell(new_advanced_row, col)}*0.5"
            for col in range(1, 11)
        ],
    )
    sales_rec_row = row
    row = write_series(ws, row, "Ventas soporte, IA y analitica", model["sales_rec"], formats, total=True)
    sales_total_row = row
    row = write_series(
        ws,
        row,
        "VENTAS TOTALES",
        model["sales_total"],
        formats,
        total=True,
        formulas=[same_row_formula("SUM", [sales_impl_row, sales_extra_row, sales_rec_row], col) for col in range(1, 11)],
    )
    row += 1
    row = write_section(ws, row, "DETERMINACION DE INGRESOS DE EFECTIVO", formats)
    row = write_year_header(ws, row, formats)
    cash_sales_row = row
    row = write_series(
        ws,
        row,
        "Ventas al contado 40%",
        model["cash_sales"],
        formats,
        formulas=[f"={cell(sales_total_row, col)}*porcentaje_ventas_contado" for col in range(1, 11)],
    )
    credit_sales_row = row
    row = write_series(
        ws,
        row,
        "Ventas al credito 60%",
        model["credit_sales"],
        formats,
        formulas=[f"={cell(sales_total_row, col)}*porcentaje_ventas_credito" for col in range(1, 11)],
    )
    current_credit_row = row
    row = write_series(
        ws,
        row,
        "Recuperacion de cuentas por cobrar del año",
        model["current_credit_collection"],
        formats,
        formulas=[f"={cell(credit_sales_row, col)}*porcentaje_cobro_credito_actual*(1-{model['bad_debt_rate']})" for col in range(1, 11)],
    )
    previous_cxc_row = row
    row = write_series(
        ws,
        row,
        "Recuperacion de cuentas por cobrar año anterior",
        model["previous_cxc_collection"],
        formats,
    )
    cash_income_row = row
    row = write_series(
        ws,
        row,
        "TOTAL INGRESOS DE EFECTIVO",
        model["cash_income"],
        formats,
        total=True,
        formulas=[same_row_formula("SUM", [cash_sales_row, current_credit_row, previous_cxc_row], col) for col in range(1, 11)],
    )
    cxc_end_row = row
    row = write_series(
        ws,
        row,
        "Saldo de cuentas por cobrar al final del año",
        model["cxc_end"],
        formats,
        formulas=[f"={cell(credit_sales_row, col)}*(1-porcentaje_cobro_credito_actual)" for col in range(1, 11)],
    )
    workbook.define_name("cuentas_cobrar_finales", f"=INGRESOS!$B${cxc_end_row + 1}:$K${cxc_end_row + 1}")
    row += 1
    row = write_section(ws, row, "FLUJOS REALES, INFLACION DE REFERENCIA Y PRECIOS BASE", formats)
    row = write_year_header(ws, row, formats)
    inflation_row = row
    row = write_series(
        ws,
        row,
        "Inflacion esperada de referencia",
        INFLATION,
        formats,
        kind="percent",
        formulas=["=inflacion_esperada" for _ in range(10)],
    )
    escalation_row = row
    row = write_series(
        ws,
        row,
        "Escalamiento aplicado a flujos reales",
        FLOW_ESCALATION,
        formats,
        kind="percent",
        formulas=["=escalamiento_flujos" for _ in range(10)],
    )
    factor_row = row
    row = write_series(
        ws,
        row,
        "Factor acumulado aplicado a precios",
        model["factors"],
        formats,
        kind="number",
        formulas=[f"=1" if col == 1 else f"={cell(factor_row, col - 1)}*(1+{cell(escalation_row, col - 1)})" for col in range(1, 11)],
    )
    for col in range(1, 11):
        ws.write_formula(
            sales_impl_row,
            col,
            f"=({cell(new_basic_row, col)}*precio_impl_B+{cell(new_standard_row, col)}*precio_impl_E+{cell(new_advanced_row, col)}*precio_impl_A)*factor_precio_base*{cell(factor_row, col)}",
            formats["total"],
            money(model["sales_impl"][col - 1]),
        )
        ws.write_formula(
            sales_rec_row,
            col,
            f"=({cell(effective_basic_row, col)}*precio_rec_B+{cell(effective_standard_row, col)}*precio_rec_E+{cell(effective_advanced_row, col)}*precio_rec_A)*factor_precio_base*{cell(factor_row, col)}",
            formats["total"],
            money(model["sales_rec"][col - 1]),
        )
        ws.write_formula(
            previous_cxc_row,
            col,
            "=0" if col == 1 else f"={cell(cxc_end_row, col - 1)}*(1-{model['bad_debt_rate']})",
            formats["money"],
            money(model["previous_cxc_collection"][col - 1]),
        )
    row += 2
    ws.write(row, 0, "Paquete", formats["header"])
    ws.write(row, 1, "Precio base cap. 5", formats["header"])
    ws.write(row, 2, "Precio economico año 1", formats["header"])
    ws.write(row, 3, "Recurrente base cap. 5", formats["header"])
    ws.write(row, 4, "Recurrente economico año 1", formats["header"])
    ws.write(row, 5, "Cobertura", formats["header"])
    ws.write(row, 6, "BLE estimados", formats["header"])
    row += 1
    for key in ["B", "E", "A"]:
        pkg = PACKAGES[key]
        ws.write(row, 0, pkg.name, formats["label"])
        ws.write_formula(row, 1, f"=precio_impl_{key}", formats["money"], pkg.base_implementation_price)
        ws.write_formula(row, 2, f"=precio_impl_{key}*factor_precio_base", formats["money"], pkg.base_implementation_price * model["price_adjustment"])
        ws.write_formula(row, 3, f"=precio_rec_{key}", formats["money"], pkg.base_recurring_price)
        ws.write_formula(row, 4, f"=precio_rec_{key}*factor_precio_base", formats["money"], pkg.base_recurring_price * model["price_adjustment"])
        ws.write(row, 5, pkg.coverage, formats["text"])
        ws.write(row, 6, pkg.beacons, formats["text"])
        row += 1
    ws.write(row + 1, 0, "Nota: el precio economico parte de los valores del Capitulo 5 sin recargo adicional. Los flujos se expresan en soles constantes, por lo que la inflacion no se acumula sobre ventas ni costos.", formats["note"])


def write_costos(workbook, model, formats):
    ws = workbook.add_worksheet("COSTOS")
    setup(ws, "Cuadro de costos de insumos directos anuales", formats, 12)
    row = 2
    row = write_section(ws, row, "MATERIALES Y SERVICIOS DIRECTOS", formats)
    row = write_year_header(ws, row, formats)
    direct_impl_row = row
    row = write_series(
        ws,
        row,
        "Hardware BLE, señalizacion e instalacion",
        model["direct_impl_cost"],
        formats,
        formulas=[
            f"=(INDEX(nuevos_B,1,{col})*costo_impl_B+INDEX(nuevos_E,1,{col})*costo_impl_E+INDEX(nuevos_A,1,{col})*costo_impl_A)*(1+escalamiento_flujos)^{col - 1}"
            for col in range(1, 11)
        ],
    )
    direct_rec_row = row
    row = write_series(
        ws,
        row,
        "Nube, voz, IA y soporte variable",
        model["direct_rec_cost"],
        formats,
        formulas=[
            (
                f"=((SUM(INDEX(nuevos_B,1,1):INDEX(nuevos_B,1,{col}))-0.5*INDEX(nuevos_B,1,{col}))*costo_rec_B"
                f"+(SUM(INDEX(nuevos_E,1,1):INDEX(nuevos_E,1,{col}))-0.5*INDEX(nuevos_E,1,{col}))*costo_rec_E"
                f"+(SUM(INDEX(nuevos_A,1,1):INDEX(nuevos_A,1,{col}))-0.5*INDEX(nuevos_A,1,{col}))*costo_rec_A)"
                f"*(1+escalamiento_flujos)^{col - 1}"
            )
            for col in range(1, 11)
        ],
    )
    direct_extra_row = row
    row = write_series(
        ws,
        row,
        "Curaduria, capacitacion y servicios adicionales",
        model["direct_extra_cost"],
        formats,
        formulas=[
            f"={sheet_cell('INGRESOS', 9, col)}*tasa_costo_servicios_adicionales"
            for col in range(1, 11)
        ],
    )
    direct_total_row = row
    row = write_series(
        ws,
        row,
        "TOTAL COSTO DIRECTO ANUAL",
        model["direct_total"],
        formats,
        total=True,
        formulas=[same_row_formula("SUM", [direct_impl_row, direct_rec_row, direct_extra_row], col) for col in range(1, 11)],
    )
    row += 1
    row = write_section(ws, row, "CUADRO DE PRODUCCION - UNIDADES DE SERVICIO", formats)
    row = write_year_header(ws, row, formats)
    row = write_series(ws, row, "Museos implementados", model["total_new"], formats, kind="integer")
    row = write_series(ws, row, "Museos activos al cierre", model["total_active"], formats, kind="integer")
    row = write_series(ws, row, "Museos equivalentes recurrentes", [sum(model["effective"][key][i] for key in ["B", "E", "A"]) for i in range(10)], formats, kind="number")
    row += 1
    row = write_section(ws, row, "PRESUPUESTO COMPRA DE INSUMOS Y SERVICIOS DIRECTOS", formats)
    row = write_year_header(ws, row, formats)
    purchase_cash_row = row
    row = write_series(
        ws,
        row,
        "Compra de contado 30%",
        model["purchase_cash"],
        formats,
        formulas=[f"={cell(direct_total_row, col)}*porcentaje_compras_contado" for col in range(1, 11)],
    )
    purchase_credit_row = row
    row = write_series(
        ws,
        row,
        "Proveedores credito 70%",
        model["purchase_credit"],
        formats,
        formulas=[f"={cell(direct_total_row, col)}*(1-porcentaje_compras_contado)" for col in range(1, 11)],
    )
    current_payment_row = row
    row = write_series(
        ws,
        row,
        "Pago a proveedores en el año",
        model["current_supplier_payment"],
        formats,
        formulas=[f"={cell(purchase_credit_row, col)}*porcentaje_pago_proveedor_actual" for col in range(1, 11)],
    )
    previous_supplier_row = row
    row = write_series(ws, row, "Pago a proveedores año anterior", model["previous_supplier_payment"], formats)
    supplier_payment_row = row
    row = write_series(
        ws,
        row,
        "TOTAL PAGO A PROVEEDORES",
        model["supplier_cash_payment"],
        formats,
        total=True,
        formulas=[same_row_formula("SUM", [purchase_cash_row, current_payment_row, previous_supplier_row], col) for col in range(1, 11)],
    )
    cxp_row = row
    row = write_series(
        ws,
        row,
        "Saldo cuentas por pagar",
        model["cxp_end"],
        formats,
        formulas=[f"={cell(purchase_credit_row, col)}*(1-porcentaje_pago_proveedor_actual)" for col in range(1, 11)],
    )
    workbook.define_name("cuentas_pagar_finales", f"=COSTOS!$B${cxp_row + 1}:$K${cxp_row + 1}")
    for col in range(1, 11):
        ws.write_formula(
            previous_supplier_row,
            col,
            "=0" if col == 1 else f"={cell(cxp_row, col - 1)}",
            formats["money"],
            money(model["previous_supplier_payment"][col - 1]),
        )
    row += 1
    row = write_section(ws, row, "COSTO DE ENERGIA, HERRAMIENTAS Y COSTOS INDIRECTOS", formats)
    row = write_year_header(ws, row, formats)
    energy_row = row
    row = write_series(ws, row, "Energia, internet y comunicaciones", model["energy"], formats)
    tools_row = row
    row = write_series(ws, row, "Herramientas cloud, repositorios y monitoreo", model["platform_tools"], formats)
    supplies_row = row
    row = write_series(ws, row, "Papeleria, insumos de oficina y pruebas", model["supplies"], formats)
    maintenance_row = row
    row = write_series(ws, row, "Mantenimiento menor de equipos", model["maintenance"], formats)
    production_dep_row = row
    row = write_series(ws, row, "Depreciacion asignada a produccion", [v * 0.60 for v in model["assets"]["depreciation"]], formats)
    row = write_series(
        ws,
        row,
        "TOTAL COSTO INDIRECTO DE PRODUCCION",
        model["indirect_total"],
        formats,
        total=True,
        formulas=[same_row_formula("SUM", [energy_row, tools_row, supplies_row, maintenance_row, production_dep_row], col) for col in range(1, 11)],
    )
    row += 2
    ws.write(row, 0, "Descripcion de equipos de operacion anual", formats["subtitle"])
    ws.write(row, 1, "Potencia/uso", formats["header"])
    ws.write(row, 2, "% produccion", formats["header"])
    ws.write(row, 3, "% ventas", formats["header"])
    ws.write(row, 4, "% adm.", formats["header"])
    equipment = [
        ("Laptops de desarrollo y pruebas", "8 h/dia", 0.65, 0.10, 0.25),
        ("Servidor local/NAS para RAG y datos", "24 h/dia", 0.80, 0.00, 0.20),
        ("Smartphones/tablets de prueba", "4 h/dia", 0.70, 0.10, 0.20),
        ("Red WiFi, router y UPS", "24 h/dia", 0.60, 0.20, 0.20),
    ]
    row += 1
    for item in equipment:
        ws.write(row, 0, item[0], formats["label"])
        ws.write(row, 1, item[1], formats["text"])
        ws.write_number(row, 2, item[2], formats["percent"])
        ws.write_number(row, 3, item[3], formats["percent"])
        ws.write_number(row, 4, item[4], formats["percent"])
        row += 1


def write_unit_cost(workbook, model, formats):
    ws = workbook.add_worksheet("COSTO DE PRODUCCION UNITARIO")
    setup(ws, "Costo Total de Operacion - MuseIQ", formats, 11)
    row = 3
    row = write_year_header(ws, row, formats)
    direct_row = row
    row = write_series(ws, row, "Insumos y servicios directos", model["direct_total"], formats)
    labor_row = row
    row = write_series(ws, row, "Mano de obra directa", model["production_labor"], formats)
    indirect_row = row
    row = write_series(ws, row, "Costos indirectos de servicio", model["indirect_total"], formats)
    total_cost_row = row
    row = write_series(
        ws,
        row,
        "TOTAL COSTO DE PRODUCCION",
        model["cost_of_production"],
        formats,
        total=True,
        formulas=[same_row_formula("SUM", [direct_row, labor_row, indirect_row], col) for col in range(1, 11)],
    )
    unit = [safe_div(model["cost_of_production"][i], max(1, model["total_new"][i] + sum(model["effective"][key][i] for key in ["B", "E", "A"]))) for i in range(10)]
    row = write_series(
        ws,
        row,
        "Costo unitario por museo equivalente",
        unit,
        formats,
        formulas=[
            f"={cell(total_cost_row, col)}/MAX(1,{sheet_cell('COSTOS', 11, col)}+{sheet_cell('COSTOS', 13, col)})"
            for col in range(1, 11)
        ],
    )
    ws.write(row + 1, 0, "El costo unitario se expresa por museo equivalente: museos implementados en el año mas museos recurrentes ponderados.", formats["note"])


def write_planilla(workbook, model, formats, *, admin_factor: float = 1.0, cost_factor: float = 1.0, sheet_name: str = "PLANILLA"):
    ws = workbook.add_worksheet(sheet_name)
    setup(ws, "Prestacion de servicios por año - Planilla MuseIQ", formats, 11)
    row = 2
    for i, year in enumerate(YEARS):
        row = write_section(ws, row, f"PRESTACION DE SERVICIOS POR AÑO {year}", formats, 10)
        headers = ["CARGO", "SUELDO MENSUAL", "SUELDO ANUAL", "GRATIFICACION JULIO DICIEMBRE", "ESSALUD (9%)", "CTS (8.33%)", "VACACIONES", "PREAVISO", "CESANTIA", "TOTAL C. SOCIAL", "TOTAL"]
        for col, header in enumerate(headers):
            ws.write(row, col, header, formats["header"])
        row += 1
        plan = staff_plan(i)
        for section, label, factor in [("admin", "Administracion", admin_factor * cost_factor), ("production", "Produccion MuseIQ", cost_factor), ("sales", "Ventas", cost_factor)]:
            ws.write(row, 0, label, formats["subtitle"])
            row += 1
            section_total = 0.0
            section_start = row
            for role, monthly in plan[section]:
                labor = labor_total(monthly * factor)
                ws.write(row, 0, role, formats["label"])
                ws.write_number(row, 1, labor["monthly"], formats["money"])
                excel_row = row + 1
                labor_formulas = {
                    2: f"=B{excel_row}*12",
                    3: f"=B{excel_row}*2",
                    4: f"=C{excel_row}*9%",
                    5: f"=(C{excel_row}+D{excel_row})*8.33%",
                    6: f"=B{excel_row}*0.5",
                    7: "=0",
                    8: f"=B{excel_row}*14/12",
                    9: f"=SUM(D{excel_row}:I{excel_row})",
                    10: f"=C{excel_row}+J{excel_row}",
                }
                for col, key in enumerate(["annual", "gratification", "essalud", "cts", "vacations", "notice", "severance", "social", "total"], start=2):
                    ws.write_formula(row, col, labor_formulas[col], formats["money"], money(labor[key]))
                section_total += labor["total"]
                row += 1
            ws.write(row, 0, f"TOTAL PLANILLA {label.upper()}", formats["total"])
            ws.write_formula(row, 10, f"=SUM(K{section_start + 1}:K{row})", formats["total"], money(section_total))
            row += 1
        row += 2


def write_expenses_finance(workbook, model, formats):
    ws = workbook.add_worksheet("GASTOS_ADM_VTAS_FINANZAS")
    setup(ws, "Gastos de Venta, Administracion y Finanzas", formats, 12)
    row = 2
    row = write_section(ws, row, "GASTOS DE VENTA", formats)
    row = write_year_header(ws, row, formats)
    sales_labor_row = row
    row = write_series(ws, row, "Sueldo y carga social depto. venta", model["sales_labor"], formats)
    sales_commission_row = row
    row = write_series(
        ws,
        row,
        "Comisiones a vendedores 2.5% ventas",
        model["sales_commission"],
        formats,
        formulas=[f"={sheet_cell('INGRESOS', 18, col)}*2.5%" for col in range(1, 11)],
    )
    prospect_row = row
    row = write_series(
        ws,
        row,
        "Prospeccion, viajes y representacion",
        [16_000 * (1.04**i) for i in range(10)],
        formats,
        formulas=[f"=16000*(1.04^{col - 1})" for col in range(1, 11)],
    )
    sales_total_row = row
    row = write_series(
        ws,
        row,
        "TOTAL GASTOS DE VENTA",
        [model["sales_labor"][i] + model["sales_other"][i] for i in range(10)],
        formats,
        total=True,
        formulas=[same_row_formula("SUM", [sales_labor_row, sales_commission_row, prospect_row], col) for col in range(1, 11)],
    )
    row += 1
    row = write_section(ws, row, "GASTOS DE ADMINISTRACION", formats)
    row = write_year_header(ws, row, formats)
    admin_labor_row = row
    row = write_series(ws, row, "Sueldo y carga social administracion", model["admin_labor"], formats)
    admin_services_row = row
    row = write_series(ws, row, "Servicios contables, legales, oficina y comunicaciones", model["admin_other"], formats)
    admin_dep_row = row
    row = write_series(
        ws,
        row,
        "Depreciacion y amortizacion asignada",
        [model["assets"]["depreciation"][i] * 0.40 + model["assets"]["amortization"][i] for i in range(10)],
        formats,
        formulas=[f"={sheet_cell('DEPRECIACIONES AMORTIZACION', 10, col)}*40%+{sheet_cell('DEPRECIACIONES AMORTIZACION', 22, col)}" for col in range(1, 11)],
    )
    admin_total_row = row
    row = write_series(
        ws,
        row,
        "TOTAL GASTOS ADMINISTRATIVOS",
        [model["admin_labor"][i] + model["admin_other"][i] + model["assets"]["depreciation"][i] * 0.40 + model["assets"]["amortization"][i] for i in range(10)],
        formats,
        total=True,
        formulas=[same_row_formula("SUM", [admin_labor_row, admin_services_row, admin_dep_row], col) for col in range(1, 11)],
    )
    row += 1
    row = write_section(ws, row, "GASTOS FINANCIEROS - AMORTIZACION DEL PRESTAMO", formats)
    row = write_year_header(ws, row, formats)
    initial_debt_row = row
    row = write_series(ws, row, "Saldo inicial de deuda", model["debt"]["initial_balance"], formats)
    interest_row = row
    row = write_series(
        ws,
        row,
        "Intereses",
        model["debt"]["interest"],
        formats,
        formulas=[f"={cell(initial_debt_row, col)}*tasa_deuda" for col in range(1, 11)],
    )
    principal_row = row
    payment_formula = f"PMT(tasa_deuda,{LOAN_TOTAL_YEARS - LOAN_GRACE_YEARS},-inversion_inicial*participacion_deuda)"
    row = write_series(
        ws,
        row,
        "Abono a capital",
        model["debt"]["principal"],
        formats,
        formulas=[
            f"=IF(COLUMN({cell(0, col)})-COLUMN($B$1)+1<={LOAN_GRACE_YEARS},0,IF(COLUMN({cell(0, col)})-COLUMN($B$1)+1<={LOAN_TOTAL_YEARS},MIN({payment_formula}-{cell(interest_row, col)},{cell(initial_debt_row, col)}),0))"
            for col in range(1, 11)
        ],
    )
    installment_row = row
    row = write_series(
        ws,
        row,
        "Cuota anual",
        model["debt"]["installment"],
        formats,
        total=True,
        formulas=[same_row_formula("SUM", [interest_row, principal_row], col) for col in range(1, 11)],
    )
    final_debt_row = row
    row = write_series(
        ws,
        row,
        "Saldo final de deuda",
        model["debt"]["final_balance"],
        formats,
        formulas=[f"=MAX(0,{cell(initial_debt_row, col)}-{cell(principal_row, col)})" for col in range(1, 11)],
    )
    for col in range(1, 11):
        ws.write_formula(
            initial_debt_row,
            col,
            "=inversion_inicial*participacion_deuda" if col == 1 else f"={cell(final_debt_row, col - 1)}",
            formats["money"],
            money(model["debt"]["initial_balance"][col - 1]),
        )
    ws.write(row + 1, 0, "Condicion adoptada: 2 años de gracia de capital y amortizacion en 6 cuotas anuales; tasa base vinculada al promedio SBS para pequeñas empresas.", formats["note"])


def write_depreciation(workbook, model, formats):
    ws = workbook.add_worksheet("DEPRECIACIONES AMORTIZACION")
    setup(ws, "Depreciaciones y Amortizacion", formats, 11)
    row = 2
    row = write_section(ws, row, "ACTIVOS TANGIBLES", formats)
    ws.write(row, 0, "Activo", formats["header"])
    ws.write(row, 1, "Valor", formats["header"])
    ws.write(row, 2, "Vida util", formats["header"])
    row += 1
    fixed_start_row = row
    for name, value, life in model["assets"]["fixed_assets"]:
        ws.write(row, 0, name, formats["label"])
        ws.write_number(row, 1, value, formats["money"])
        ws.write_number(row, 2, life, formats["integer"])
        row += 1
    fixed_end_row = row - 1
    row += 1
    row = write_year_header(ws, row, formats)
    depreciation_row = row
    row = write_series(
        ws,
        row,
        "Depreciacion anual",
        model["assets"]["depreciation"],
        formats,
        formulas=[
            "="
            + "+".join(
                f"IF({year}<={cell(asset_row, 2, abs_row=True, abs_col=True)},{cell(asset_row, 1, abs_row=True, abs_col=True)}/{cell(asset_row, 2, abs_row=True, abs_col=True)},0)"
                for asset_row in range(fixed_start_row, fixed_end_row + 1)
            )
            for year in YEARS
        ],
    )
    row = write_series(
        ws,
        row,
        "Activo fijo neto",
        model["fixed_net"],
        formats,
        total=True,
        formulas=[
            f"=MAX(0,SUM({cell(fixed_start_row, 1, abs_row=True, abs_col=True)}:{cell(fixed_end_row, 1, abs_row=True, abs_col=True)})-SUM($B${depreciation_row + 1}:{cell(depreciation_row, col)}))"
            for col in range(1, 11)
        ],
    )
    row += 2
    row = write_section(ws, row, "ACTIVOS INTANGIBLES Y DIFERIDOS", formats)
    ws.write(row, 0, "Activo", formats["header"])
    ws.write(row, 1, "Valor", formats["header"])
    ws.write(row, 2, "Vida util", formats["header"])
    row += 1
    intangible_start_row = row
    for name, value, life in model["assets"]["intangibles"]:
        ws.write(row, 0, name, formats["label"])
        ws.write_number(row, 1, value, formats["money"])
        ws.write_number(row, 2, life, formats["integer"])
        row += 1
    intangible_end_row = row - 1
    row += 1
    row = write_year_header(ws, row, formats)
    amortization_row = row
    row = write_series(
        ws,
        row,
        "Amortizacion anual",
        model["assets"]["amortization"],
        formats,
        formulas=[
            "="
            + "+".join(
                f"IF({year}<={cell(asset_row, 2, abs_row=True, abs_col=True)},{cell(asset_row, 1, abs_row=True, abs_col=True)}/{cell(asset_row, 2, abs_row=True, abs_col=True)},0)"
                for asset_row in range(intangible_start_row, intangible_end_row + 1)
            )
            for year in YEARS
        ],
    )
    row = write_series(
        ws,
        row,
        "Activo intangible neto",
        model["intangible_net"],
        formats,
        total=True,
        formulas=[
            f"=MAX(0,SUM({cell(intangible_start_row, 1, abs_row=True, abs_col=True)}:{cell(intangible_end_row, 1, abs_row=True, abs_col=True)})-SUM($B${amortization_row + 1}:{cell(amortization_row, col)}))"
            for col in range(1, 11)
        ],
    )


def write_investment_plan(workbook, model, formats):
    ws = workbook.add_worksheet("PLAN DE INVERSION")
    setup(ws, "Plan de Inversion - MuseIQ", formats, 6)
    row = 3
    ws.write(row, 0, "Concepto", formats["header"])
    ws.write(row, 1, "Monto", formats["header"])
    ws.write(row, 2, "Criterio", formats["header"])
    rows = [
        ("Activos tangibles", TANGIBLE_ASSETS, "Equipos de prueba, servidor, herramientas y mobiliario"),
        ("Activos intangibles y diferidos", INTANGIBLE_ASSETS, "Desarrollo base, formalizacion, documentacion y preventa"),
        ("Capital de trabajo inicial", INITIAL_CASH, "Caja de arranque para cubrir descalce de cobros y pagos"),
        ("TOTAL INVERSION", INITIAL_INVESTMENT, "Base del flujo de efectivo"),
        ("Fondos propios", model["equity"], "40% de la inversion"),
        ("Financiamiento", model["loan"], "60% de la inversion"),
    ]
    row += 1
    row_by_label = {}
    for label, value, note in rows:
        row_by_label[label] = row
        ws.write(row, 0, label, formats["total"] if "TOTAL" in label else formats["label"])
        ws.write_number(row, 1, value, formats["total"] if "TOTAL" in label else formats["money"])
        ws.write(row, 2, note, formats["text"])
        row += 1
    ws.write_formula(
        row_by_label["TOTAL INVERSION"],
        1,
        f"=SUM(B{row_by_label['Activos tangibles'] + 1}:B{row_by_label['Capital de trabajo inicial'] + 1})",
        formats["total"],
        money(INITIAL_INVESTMENT),
    )
    ws.write_formula(row_by_label["Activos tangibles"], 1, "=activos_tangibles", formats["money"], money(TANGIBLE_ASSETS))
    ws.write_formula(row_by_label["Activos intangibles y diferidos"], 1, "=activos_intangibles", formats["money"], money(INTANGIBLE_ASSETS))
    ws.write_formula(row_by_label["Capital de trabajo inicial"], 1, "=capital_trabajo_inicial", formats["money"], money(INITIAL_CASH))
    ws.write_formula(row_by_label["Fondos propios"], 1, f"=B{row_by_label['TOTAL INVERSION'] + 1}*participacion_capital", formats["money"], money(model["equity"]))
    ws.write_formula(row_by_label["Financiamiento"], 1, f"=B{row_by_label['TOTAL INVERSION'] + 1}*participacion_deuda", formats["money"], money(model["loan"]))


def write_opening_balance(workbook, model, formats):
    ws = workbook.add_worksheet("BALANCE DE APERTURA")
    setup(ws, "Balance de Apertura", formats, 4)
    row = 3
    data = [
        ("Activos", "", ""),
        ("Caja y bancos", INITIAL_CASH, "Activo circulante"),
        ("Mobiliario, equipos y herramientas", TANGIBLE_ASSETS, "Activo fijo"),
        ("Activos intangibles y diferidos", INTANGIBLE_ASSETS, "Nominales"),
        ("TOTAL ACTIVOS", INITIAL_INVESTMENT, ""),
        ("Pasivos", "", ""),
        ("Prestamo bancario", model["loan"], "Pasivo largo plazo"),
        ("Patrimonio", "", ""),
        ("Capital social", model["equity"], "Fondos propios"),
        ("TOTAL PASIVO Y PATRIMONIO", INITIAL_INVESTMENT, ""),
    ]
    row_by_label = {}
    for label, value, note in data:
        if value == "":
            ws.merge_range(row, 0, row, 2, label, formats["subtitle"])
        else:
            row_by_label[label] = row
            total = label.startswith("TOTAL")
            ws.write(row, 0, label, formats["total"] if total else formats["label"])
            ws.write_number(row, 1, value, formats["total"] if total else formats["money"])
            ws.write(row, 2, note, formats["text"])
        row += 1
    ws.write_formula(
        row_by_label["TOTAL ACTIVOS"],
        1,
        f"=SUM(B{row_by_label['Caja y bancos'] + 1}:B{row_by_label['Activos intangibles y diferidos'] + 1})",
        formats["total"],
        money(INITIAL_INVESTMENT),
    )
    ws.write_formula(
        row_by_label["TOTAL PASIVO Y PATRIMONIO"],
        1,
        f"=B{row_by_label['Prestamo bancario'] + 1}+B{row_by_label['Capital social'] + 1}",
        formats["total"],
        money(INITIAL_INVESTMENT),
    )
    ws.write_formula(row_by_label["Caja y bancos"], 1, "=capital_trabajo_inicial", formats["money"], money(INITIAL_CASH))
    ws.write_formula(row_by_label["Mobiliario, equipos y herramientas"], 1, "=activos_tangibles", formats["money"], money(TANGIBLE_ASSETS))
    ws.write_formula(row_by_label["Activos intangibles y diferidos"], 1, "=activos_intangibles", formats["money"], money(INTANGIBLE_ASSETS))
    ws.write_formula(row_by_label["Prestamo bancario"], 1, "=inversion_inicial*participacion_deuda", formats["money"], money(model["loan"]))
    ws.write_formula(row_by_label["Capital social"], 1, "=inversion_inicial*participacion_capital", formats["money"], money(model["equity"]))


def write_cost_of_sales(workbook, model, formats):
    ws = workbook.add_worksheet("COSTO DE VENTA")
    setup(ws, "Costo de lo Vendido", formats, 11)
    row = 3
    row = write_year_header(ws, row, formats)
    zero = [0] * 10
    initial_inventory_row = row
    row = write_series(ws, row, "Inventario inicial", zero, formats)
    production_cost_row = row
    row = write_series(ws, row, "+ Costo de produccion", model["cost_of_production"], formats)
    available_product_row = row
    row = write_series(
        ws,
        row,
        "= Producto disponible para la venta",
        model["cost_of_production"],
        formats,
        formulas=[same_row_formula("SUM", [initial_inventory_row, production_cost_row], col) for col in range(1, 11)],
    )
    final_inventory_row = row
    row = write_series(ws, row, "- Inventario final", zero, formats)
    row = write_series(
        ws,
        row,
        "= Costo de venta",
        model["cost_of_sales"],
        formats,
        total=True,
        formulas=[f"={cell(available_product_row, col)}-{cell(final_inventory_row, col)}" for col in range(1, 11)],
    )
    for col in range(1, 11):
        ws.write_formula(production_cost_row, col, f"={sheet_cell('COSTO DE PRODUCCION UNITARIO', 7, col)}", formats["money"], money(model["cost_of_production"][col - 1]))


def write_income_statement(workbook, model, formats):
    ws = workbook.add_worksheet("ESTADO DE RESULTADOS")
    setup(ws, "Estado de Resultados - MuseIQ", formats, 11)
    row = 3
    row = write_year_header(ws, row, formats)
    sales_row = row
    row = write_series(ws, row, "Ventas totales", model["sales_total"], formats)
    cost_sales_row = row
    row = write_series(ws, row, "Costo de venta", model["cost_of_sales"], formats)
    gross_profit_row = row
    row = write_series(
        ws,
        row,
        "Utilidad bruta en ventas",
        model["gross_profit"],
        formats,
        total=True,
        formulas=[f"={cell(sales_row, col)}-{cell(cost_sales_row, col)}" for col in range(1, 11)],
    )
    operating_expenses_row = row
    row = write_series(ws, row, "Total gastos de operacion", model["operating_expenses"], formats)
    sales_expense_row = row
    row = write_series(ws, row, "Gastos de venta", [model["sales_labor"][i] + model["sales_other"][i] for i in range(10)], formats)
    admin_expense_row = row
    row = write_series(ws, row, "Gastos de administracion", [model["admin_labor"][i] + model["admin_other"][i] + model["assets"]["depreciation"][i] * 0.40 + model["assets"]["amortization"][i] for i in range(10)], formats)
    ebit_row = row
    row = write_series(
        ws,
        row,
        "Utilidad de operacion",
        model["ebit"],
        formats,
        total=True,
        formulas=[f"={cell(gross_profit_row, col)}-{cell(operating_expenses_row, col)}" for col in range(1, 11)],
    )
    interest_row = row
    row = write_series(ws, row, "Gastos financieros", model["debt"]["interest"], formats)
    ebt_row = row
    row = write_series(
        ws,
        row,
        "Utilidad antes del I.R.",
        model["ebt"],
        formats,
        formulas=[f"={cell(ebit_row, col)}-{cell(interest_row, col)}" for col in range(1, 11)],
    )
    tax_row = row
    row = write_series(
        ws,
        row,
        "Impuesto a la renta 29.5%",
        model["income_tax"],
        formats,
        formulas=[f"=MAX(0,{cell(ebt_row, col)}*tasa_impuesto_renta)" for col in range(1, 11)],
    )
    workbook.define_name("impuesto_renta_anual", f"='ESTADO DE RESULTADOS'!$B${tax_row + 1}:$K${tax_row + 1}")
    net_income_row = row
    row = write_series(
        ws,
        row,
        "Utilidad neta",
        model["net_income"],
        formats,
        total=True,
        formulas=[f"={cell(ebt_row, col)}-{cell(tax_row, col)}" for col in range(1, 11)],
    )
    reserve_row = row
    row = write_series(
        ws,
        row,
        "Reserva legal",
        model["reserve_legal"],
        formats,
        formulas=[
            f"=MIN(MAX(0,{cell(net_income_row, col)}*10%),MAX(0,inversion_inicial*participacion_capital*20%-SUM($B${reserve_row + 1}:{cell(reserve_row, col - 1) if col > 1 else '$A$1'})))"
            if col > 1
            else f"=MIN(MAX(0,{cell(net_income_row, col)}*10%),inversion_inicial*participacion_capital*20%)"
            for col in range(1, 11)
        ],
    )
    row = write_series(
        ws,
        row,
        "Utilidad a distribuir",
        model["retained_profit"],
        formats,
        total=True,
        formulas=[f"={cell(net_income_row, col)}-{cell(reserve_row, col)}" for col in range(1, 11)],
    )
    for col in range(1, 11):
        ws.write_formula(sales_row, col, f"={sheet_cell('INGRESOS', 18, col)}", formats["money"], money(model["sales_total"][col - 1]))
        ws.write_formula(cost_sales_row, col, f"={sheet_cell('COSTO DE VENTA', 8, col)}", formats["money"], money(model["cost_of_sales"][col - 1]))
        ws.write_formula(sales_expense_row, col, f"={sheet_cell('GASTOS_ADM_VTAS_FINANZAS', 7, col)}", formats["money"], money(model["sales_labor"][col - 1] + model["sales_other"][col - 1]))
        ws.write_formula(admin_expense_row, col, f"={sheet_cell('GASTOS_ADM_VTAS_FINANZAS', 14, col)}", formats["money"], money(model["admin_labor"][col - 1] + model["admin_other"][col - 1] + model["assets"]["depreciation"][col - 1] * 0.40 + model["assets"]["amortization"][col - 1]))
        ws.write_formula(interest_row, col, f"={sheet_cell('GASTOS_ADM_VTAS_FINANZAS', 19, col)}", formats["money"], money(model["debt"]["interest"][col - 1]))
        ws.write_formula(
            operating_expenses_row,
            col,
            f"={cell(sales_expense_row, col)}+{cell(admin_expense_row, col)}",
            formats["money"],
            money(model["operating_expenses"][col - 1]),
        )


def write_cash_budget(workbook, model, formats, *, sheet_name: str = "PRESUPUESTO CAJA"):
    ws = workbook.add_worksheet(sheet_name)
    setup(ws, "Presupuesto de Caja - MuseIQ", formats, 11)
    row = 3
    headers = ["Concepto", "Año 0"] + YEAR_LABELS
    for col, header in enumerate(headers):
        ws.write(row, col, header, formats["header"])
    row += 1
    ws.write(row, 0, "INGRESOS DE EFECTIVO", formats["subtitle"])
    row += 1
    rows = [
        ("Fondos propios", [model["equity"]] + [0] * 10),
        ("Financiamiento", [model["loan"]] + [0] * 10),
        ("Ingresos por venta de contado", [0] + model["cash_sales"]),
        ("Recuperacion cuentas por cobrar del año", [0] + model["current_credit_collection"]),
        ("Cuentas por cobrar año anterior", [0] + model["previous_cxc_collection"]),
        ("Total ingresos", [INITIAL_INVESTMENT] + model["cash_income"]),
    ]
    income_rows = {}
    for label, values in rows:
        income_rows[label] = row
        ws.write(row, 0, label, formats["total"] if label == "Total ingresos" else formats["label"])
        for col, value in enumerate(values, start=1):
            ws.write_number(row, col, value, formats["total"] if label == "Total ingresos" else formats["money"])
        row += 1
    ws.write_formula(income_rows["Fondos propios"], 1, "=inversion_inicial*participacion_capital", formats["money"], money(model["equity"]))
    ws.write_formula(income_rows["Financiamiento"], 1, "=inversion_inicial*participacion_deuda", formats["money"], money(model["loan"]))
    for col in range(2, 12):
        year_col = col - 1
        ws.write_formula(income_rows["Ingresos por venta de contado"], col, f"={sheet_cell('INGRESOS', 22, year_col)}", formats["money"], money(model["cash_sales"][year_col - 1]))
        ws.write_formula(income_rows["Recuperacion cuentas por cobrar del año"], col, f"={sheet_cell('INGRESOS', 24, year_col)}", formats["money"], money(model["current_credit_collection"][year_col - 1]))
        ws.write_formula(income_rows["Cuentas por cobrar año anterior"], col, f"={sheet_cell('INGRESOS', 25, year_col)}", formats["money"], money(model["previous_cxc_collection"][year_col - 1]))
    for col in range(1, 12):
        ws.write_formula(
            income_rows["Total ingresos"],
            col,
            f"=SUM({cell(income_rows['Fondos propios'], col)}:{cell(income_rows['Cuentas por cobrar año anterior'], col)})",
            formats["total"],
            money(([INITIAL_INVESTMENT] + model["cash_income"])[col - 1]),
        )
    row += 1
    ws.write(row, 0, "EGRESOS DE EFECTIVO", formats["subtitle"])
    row += 1
    egress_rows = [
        ("Compra de activos fijos", [TANGIBLE_ASSETS] + [0] * 10),
        ("Activos nominales", [INTANGIBLE_ASSETS] + [0] * 10),
        ("Planilla de produccion", [0] + model["production_labor"]),
        ("Costos indirectos de fabricacion", [0] + model["indirect_cash"]),
        ("Compra insumos y servicios directos", [0] + model["supplier_cash_payment"]),
        ("Gastos de administracion", [0] + [model["admin_labor"][i] + model["admin_other"][i] for i in range(10)]),
        ("Gastos de venta", [0] + [model["sales_labor"][i] + model["sales_other"][i] for i in range(10)]),
        ("Impuesto a la renta pagado", [0] + model["cash_tax_paid"]),
        ("Pago de intereses", [0] + model["debt"]["interest"]),
        ("Abono a capital", [0] + model["debt"]["principal"]),
    ]
    total_egress = [TANGIBLE_ASSETS + INTANGIBLE_ASSETS] + model["cash_egress"]
    egress_start_row = row
    for label, values in egress_rows:
        ws.write(row, 0, label, formats["label"])
        for col, value in enumerate(values, start=1):
            ws.write_number(row, col, value, formats["money"])
        row += 1
    egress_end_row = row - 1
    total_egress_row = row
    ws.write(row, 0, "Total egresos", formats["total"])
    for col, value in enumerate(total_egress, start=1):
        ws.write_formula(row, col, f"=SUM({cell(egress_start_row, col)}:{cell(egress_end_row, col)})", formats["total"], money(value))
    ws.write_formula(egress_start_row, 1, "=activos_tangibles", formats["money"], money(TANGIBLE_ASSETS))
    ws.write_formula(egress_start_row + 1, 1, "=activos_intangibles", formats["money"], money(INTANGIBLE_ASSETS))
    if sheet_name == "PRESUPUESTO CAJA":
        workbook.define_name(
            "ingresos_efectivo_base",
            f"='PRESUPUESTO CAJA'!$C${income_rows['Total ingresos'] + 1}:$L${income_rows['Total ingresos'] + 1}",
        )
        workbook.define_name(
            "egresos_efectivo_base",
            f"='PRESUPUESTO CAJA'!$C${total_egress_row + 1}:$L${total_egress_row + 1}",
        )
    row += 2
    flow = [INITIAL_CASH] + model["cash_budget_flow"]
    flow_row = row
    ws.write(row, 0, "Flujo de efectivo", formats["label"])
    for col, value in enumerate(flow, start=1):
        ws.write_formula(row, col, f"={cell(income_rows['Total ingresos'], col)}-{cell(total_egress_row, col)}", formats["money"], money(value))
    row += 1
    initial = [0] + model["cash_balance"][:-1]
    initial_row = row
    ws.write(row, 0, "Saldo inicial", formats["label"])
    for col, value in enumerate(initial, start=1):
        ws.write_number(row, col, value, formats["money"])
    row += 1
    final_row = row
    ws.write(row, 0, "Saldo final", formats["total"])
    for col, value in enumerate(model["cash_balance"], start=1):
        ws.write_formula(row, col, f"={cell(initial_row, col)}+{cell(flow_row, col)}", formats["total"], money(value))
    for col, value in enumerate(initial, start=1):
        ws.write_formula(initial_row, col, "=0" if col == 1 else f"={cell(final_row, col - 1)}", formats["money"], money(value))
    row += 2
    ws.write(row, 0, "Nota: si el saldo final es negativo, el proyecto requiere una linea temporal de capital de trabajo; se mantiene visible para no forzar caja perfecta.", formats["note"])


def write_balance(workbook, model, formats):
    ws = workbook.add_worksheet("BALANCE GENERAL PROYECTADO")
    setup(ws, "Balance General Proyectado - MuseIQ", formats, 12)
    row = 3
    row = write_year_header(ws, row, formats)
    row = write_section(ws, row, "ACTIVOS", formats)
    cash_row = row
    row = write_series(ws, row, "Caja y bancos", model["cash_balance"][1:], formats)
    cxc_row = row
    row = write_series(ws, row, "Cuentas por cobrar", model["cxc_end"], formats)
    current_assets_row = row
    row = write_series(
        ws,
        row,
        "Total activo circulante",
        model["current_assets"],
        formats,
        total=True,
        formulas=[same_row_formula("SUM", [cash_row, cxc_row], col) for col in range(1, 11)],
    )
    fixed_net_row = row
    row = write_series(ws, row, "Activo fijo neto", model["fixed_net"], formats)
    intangible_net_row = row
    row = write_series(ws, row, "Activo intangible neto", model["intangible_net"], formats)
    total_assets_row = row
    row = write_series(
        ws,
        row,
        "TOTAL ACTIVOS",
        model["total_assets"],
        formats,
        total=True,
        formulas=[same_row_formula("SUM", [current_assets_row, fixed_net_row, intangible_net_row], col) for col in range(1, 11)],
    )
    row += 1
    row = write_section(ws, row, "PASIVOS", formats)
    cxp_row = row
    row = write_series(ws, row, "Cuentas por pagar", model["cxp_end"], formats)
    short_debt_row = row
    row = write_series(ws, row, "Ptmo. corto plazo", [model["debt"]["principal"][i] for i in range(10)], formats)
    tax_row = row
    row = write_series(ws, row, "Impuesto a la renta por pagar", model["income_tax"], formats)
    current_liabilities_row = row
    row = write_series(
        ws,
        row,
        "Total pasivo circulante",
        model["current_liabilities"],
        formats,
        total=True,
        formulas=[same_row_formula("SUM", [cxp_row, short_debt_row, tax_row], col) for col in range(1, 11)],
    )
    long_debt_row = row
    row = write_series(ws, row, "Ptmo. largo plazo", model["long_debt"], formats)
    total_liabilities_row = row
    row = write_series(
        ws,
        row,
        "TOTAL PASIVOS",
        model["total_liabilities"],
        formats,
        total=True,
        formulas=[same_row_formula("SUM", [current_liabilities_row, long_debt_row], col) for col in range(1, 11)],
    )
    row += 1
    row = write_section(ws, row, "PATRIMONIO", formats)
    capital_row = row
    row = write_series(ws, row, "Capital social", [model["equity"]] * 10, formats)
    reserve_accum_row = row
    row = write_series(
        ws,
        row,
        "Reserva legal acumulada",
        model["reserve_accum"],
        formats,
        formulas=[f"=SUM('ESTADO DE RESULTADOS'!$B$16:{cell(15, col)})" for col in range(1, 11)],
    )
    accumulated = []
    acc = 0.0
    for value in model["retained_profit"]:
        acc += value
        accumulated.append(acc)
    retained_accum_row = row
    row = write_series(
        ws,
        row,
        "Utilidad acumulada",
        accumulated,
        formats,
        formulas=[f"=SUM('ESTADO DE RESULTADOS'!$B$17:{cell(16, col)})" for col in range(1, 11)],
    )
    equity_total_row = row
    row = write_series(
        ws,
        row,
        "TOTAL PATRIMONIO",
        model["equity_values"],
        formats,
        total=True,
        formulas=[same_row_formula("SUM", [capital_row, reserve_accum_row, retained_accum_row], col) for col in range(1, 11)],
    )
    row = write_series(
        ws,
        row,
        "Diferencia de cuadre referencial",
        model["balance_gap"],
        formats,
        formulas=[f"={cell(total_assets_row, col)}-{cell(total_liabilities_row, col)}-{cell(equity_total_row, col)}" for col in range(1, 11)],
    )
    for col in range(1, 11):
        ws.write_formula(cash_row, col, f"={sheet_cell('PRESUPUESTO CAJA', 27, col + 1)}", formats["money"], money(model["cash_balance"][col]))
        ws.write_formula(cxc_row, col, f"={sheet_cell('INGRESOS', 27, col)}", formats["money"], money(model["cxc_end"][col - 1]))
        ws.write_formula(fixed_net_row, col, f"={sheet_cell('DEPRECIACIONES AMORTIZACION', 11, col)}", formats["money"], money(model["fixed_net"][col - 1]))
        ws.write_formula(intangible_net_row, col, f"={sheet_cell('DEPRECIACIONES AMORTIZACION', 23, col)}", formats["money"], money(model["intangible_net"][col - 1]))
        ws.write_formula(cxp_row, col, f"={sheet_cell('COSTOS', 22, col)}", formats["money"], money(model["cxp_end"][col - 1]))
        next_principal = sheet_cell("GASTOS_ADM_VTAS_FINANZAS", 20, col + 1) if col < 10 else "0"
        ws.write_formula(short_debt_row, col, f"={next_principal}", formats["money"], money(model["current_debt"][col - 1]))
        ws.write_formula(tax_row, col, f"={sheet_cell('ESTADO DE RESULTADOS', 13, col)}", formats["money"], money(model["income_tax"][col - 1]))
        ws.write_formula(long_debt_row, col, f"=MAX(0,{sheet_cell('GASTOS_ADM_VTAS_FINANZAS', 22, col)}-{next_principal})", formats["money"], money(model["long_debt"][col - 1]))
        ws.write_formula(capital_row, col, f"={sheet_cell('PLAN DE INVERSION', 8, 1)}", formats["money"], money(model["equity"]))


def write_ratios(workbook, model, formats):
    ws = workbook.add_worksheet("RAZONES FINANCIERAS")
    setup(ws, "Razones Financieras - MuseIQ", formats, 11)
    row = 3
    row = write_year_header(ws, row, formats)
    def safe_formula(expr: str) -> str:
        return f"=IFERROR({expr},0)"

    ratios = [
        ("Indice de solvencia", [safe_div(model["current_assets"][i], model["current_liabilities"][i]) for i in range(10)], "number", [safe_formula(f"{sheet_cell('BALANCE GENERAL PROYECTADO', 7, col)}/{sheet_cell('BALANCE GENERAL PROYECTADO', 16, col)}") for col in range(1, 11)]),
        ("Capital de trabajo neto", [model["current_assets"][i] - model["current_liabilities"][i] for i in range(10)], "money", [f"={sheet_cell('BALANCE GENERAL PROYECTADO', 7, col)}-{sheet_cell('BALANCE GENERAL PROYECTADO', 16, col)}" for col in range(1, 11)]),
        ("Prueba del acido", [safe_div(model["current_assets"][i], model["current_liabilities"][i]) for i in range(10)], "number", [safe_formula(f"{sheet_cell('BALANCE GENERAL PROYECTADO', 7, col)}/{sheet_cell('BALANCE GENERAL PROYECTADO', 16, col)}") for col in range(1, 11)]),
        ("Rotacion de cuentas por cobrar", [safe_div(model["sales_total"][i], model["cxc_end"][i]) for i in range(10)], "number", [safe_formula(f"{sheet_cell('ESTADO DE RESULTADOS', 4, col)}/{sheet_cell('BALANCE GENERAL PROYECTADO', 6, col)}") for col in range(1, 11)]),
        ("Plazo promedio de cobro", [safe_div(360, safe_div(model["sales_total"][i], model["cxc_end"][i])) for i in range(10)], "number", [safe_formula(f"360/({sheet_cell('ESTADO DE RESULTADOS', 4, col)}/{sheet_cell('BALANCE GENERAL PROYECTADO', 6, col)})") for col in range(1, 11)]),
        ("Rotacion de cuentas por pagar", [safe_div(model["direct_total"][i], model["cxp_end"][i]) for i in range(10)], "number", [safe_formula(f"{sheet_cell('COSTOS', 7, col)}/{sheet_cell('BALANCE GENERAL PROYECTADO', 13, col)}") for col in range(1, 11)]),
        ("Plazo promedio de pago", [safe_div(360, safe_div(model["direct_total"][i], model["cxp_end"][i])) for i in range(10)], "number", [safe_formula(f"360/({sheet_cell('COSTOS', 7, col)}/{sheet_cell('BALANCE GENERAL PROYECTADO', 13, col)})") for col in range(1, 11)]),
        ("Razon de endeudamiento", [safe_div(model["total_liabilities"][i], model["total_assets"][i]) for i in range(10)], "percent", [safe_formula(f"{sheet_cell('BALANCE GENERAL PROYECTADO', 18, col)}/{sheet_cell('BALANCE GENERAL PROYECTADO', 10, col)}") for col in range(1, 11)]),
        ("Pasivo / Capital", [safe_div(model["total_liabilities"][i], model["equity_values"][i]) for i in range(10)], "number", [safe_formula(f"{sheet_cell('BALANCE GENERAL PROYECTADO', 18, col)}/{sheet_cell('BALANCE GENERAL PROYECTADO', 24, col)}") for col in range(1, 11)]),
        ("Margen bruto", [safe_div(model["gross_profit"][i], model["sales_total"][i]) for i in range(10)], "percent", [safe_formula(f"{sheet_cell('ESTADO DE RESULTADOS', 6, col)}/{sheet_cell('ESTADO DE RESULTADOS', 4, col)}") for col in range(1, 11)]),
        ("Margen operativo", [safe_div(model["ebit"][i], model["sales_total"][i]) for i in range(10)], "percent", [safe_formula(f"{sheet_cell('ESTADO DE RESULTADOS', 10, col)}/{sheet_cell('ESTADO DE RESULTADOS', 4, col)}") for col in range(1, 11)]),
        ("Margen neto", [safe_div(model["net_income"][i], model["sales_total"][i]) for i in range(10)], "percent", [safe_formula(f"{sheet_cell('ESTADO DE RESULTADOS', 14, col)}/{sheet_cell('ESTADO DE RESULTADOS', 4, col)}") for col in range(1, 11)]),
        ("Rotacion total del activo", [safe_div(model["sales_total"][i], model["total_assets"][i]) for i in range(10)], "number", [safe_formula(f"{sheet_cell('ESTADO DE RESULTADOS', 4, col)}/{sheet_cell('BALANCE GENERAL PROYECTADO', 10, col)}") for col in range(1, 11)]),
        ("ROA", [safe_div(model["net_income"][i], model["total_assets"][i]) for i in range(10)], "percent", [safe_formula(f"{sheet_cell('ESTADO DE RESULTADOS', 14, col)}/{sheet_cell('BALANCE GENERAL PROYECTADO', 10, col)}") for col in range(1, 11)]),
        ("Cobertura de intereses", [safe_div(model["ebit"][i], model["debt"]["interest"][i]) for i in range(10)], "number", [safe_formula(f"{sheet_cell('ESTADO DE RESULTADOS', 10, col)}/{sheet_cell('ESTADO DE RESULTADOS', 11, col)}") for col in range(1, 11)]),
    ]
    for label, values, kind, formulas in ratios:
        row = write_series(ws, row, label, values, formats, kind=kind, formulas=formulas)


def write_ratio_comments(workbook, model, formats):
    ws = workbook.add_worksheet("COMENTARIOS DE LAS RAZONES")
    setup(ws, "Comentarios de las Razones Financieras", formats, 9)
    comments = [
        ("INDICES DE LIQUIDEZ", "El escenario base conserva caja positiva, pero la holgura del primer año es reducida. MuseIQ debe gestionar anticipos, hitos facturables y seguimiento de cobranza."),
        ("CAPITAL DE TRABAJO", "El capital de trabajo inicial cubre el descalce del escenario base. Un retraso adicional de cobro o un sobrecosto de despliegue podria requerir una linea temporal de liquidez."),
        ("CUENTAS POR COBRAR", "La politica considerada combina anticipo, avance y retencion. Aun asi, queda un saldo por cobrar al cierre de cada año, por lo que la cobranza es un riesgo relevante."),
        ("ENDEUDAMIENTO", "El proyecto se modela con 60% de financiamiento y dos años de gracia de capital. Esta condicion reduce estrangulamiento inicial pero mantiene gasto financiero real."),
        ("RENTABILIDAD", "El margen mejora cuando la base recurrente crece; no se obtiene por venta aislada de beacons sino por implementacion, corpus, soporte, IA y analitica."),
        ("COBERTURA DE INTERESES", "Los primeros años son los mas debiles. La cobertura se fortalece despues de consolidar contratos recurrentes y cerrar nuevos museos estandar/avanzados."),
        ("RIESGO OPERATIVO", "El uso de IA, voz y soporte debe controlarse con bolsas de consumo y reglas de sobreconsumo; de lo contrario, el margen recurrente se deteriora."),
    ]
    row = 1
    for title, comment in comments:
        ws.write(row, 0, title, formats["subtitle"])
        ws.merge_range(row, 1, row + 2, 9, comment, formats["text"])
        row += 4


def write_break_even(workbook, model, formats):
    ws = workbook.add_worksheet("PUNTO DE EQUILIBRIO")
    setup(ws, "Punto de Equilibrio - MuseIQ", formats, 11)
    row = 3
    row = write_year_header(ws, row, formats)
    sales_row = row
    row = write_series(ws, row, "Ventas", model["sales_total"], formats)
    variable_costs_row = row
    row = write_series(ws, row, "Costos variables", model["variable_costs"], formats)
    direct_costs_row = row
    row = write_series(ws, row, "Costos directos", model["direct_total"], formats)
    variable_labor_row = row
    row = write_series(ws, row, "Mano de obra directa variable", [v * 0.70 for v in model["production_labor"]], formats)
    variable_indirect_row = row
    row = write_series(ws, row, "Costos indirectos variables", [v * 0.60 for v in model["indirect_cash"]], formats)
    fixed_costs_row = row
    row = write_series(ws, row, "Costos fijos", model["fixed_costs"], formats)
    break_even_sales_row = row
    row = write_series(
        ws,
        row,
        "Punto de equilibrio en soles",
        model["break_even_sales"],
        formats,
        total=True,
        formulas=[f"=IFERROR({cell(fixed_costs_row, col)}/(1-{cell(variable_costs_row, col)}/{cell(sales_row, col)}),0)" for col in range(1, 11)],
    )
    break_even_units_row = row
    row = write_series(
        ws,
        row,
        "Punto de equilibrio en museos equivalentes",
        model["break_even_units"],
        formats,
        kind="number",
        formulas=[
            f"=IFERROR({cell(break_even_sales_row, col)}/({cell(sales_row, col)}/MAX(1,{sheet_cell('COSTOS', 11, col)}+{sheet_cell('COSTOS', 13, col)})),0)"
            for col in range(1, 11)
        ],
    )
    row = write_series(
        ws,
        row,
        "Porcentaje de ventas",
        model["break_even_pct"],
        formats,
        kind="percent",
        formulas=[f"=IFERROR({cell(break_even_sales_row, col)}/{cell(sales_row, col)},0)" for col in range(1, 11)],
    )
    for col in range(1, 11):
        ws.write_formula(
            variable_costs_row,
            col,
            same_row_formula("SUM", [direct_costs_row, variable_labor_row, variable_indirect_row], col),
            formats["money"],
            money(model["variable_costs"][col - 1]),
        )
    row += 3
    row = write_section(ws, row, "APALANCAMIENTO OPERATIVO", formats)
    row = write_year_header(ws, row, formats)
    contribution = [model["sales_total"][i] - model["variable_costs"][i] for i in range(10)]
    operating_income = [model["sales_total"][i] - model["variable_costs"][i] - model["fixed_costs"][i] for i in range(10)]
    gao = [safe_div(contribution[i], operating_income[i]) for i in range(10)]
    contribution_row = row
    row = write_series(
        ws,
        row,
        "Ingresos menos costo variable",
        contribution,
        formats,
        formulas=[f"={cell(sales_row, col)}-{cell(variable_costs_row, col)}" for col in range(1, 11)],
    )
    operating_income_row = row
    row = write_series(
        ws,
        row,
        "Resultado antes de estructura fija",
        operating_income,
        formats,
        formulas=[f"={cell(contribution_row, col)}-{cell(fixed_costs_row, col)}" for col in range(1, 11)],
    )
    row = write_series(
        ws,
        row,
        "GAO",
        gao,
        formats,
        kind="number",
        formulas=[f"=IFERROR({cell(contribution_row, col)}/{cell(operating_income_row, col)},0)" for col in range(1, 11)],
    )


def write_flow_sheet(workbook, model, formats, sheet_name: str, title: str):
    ws = workbook.add_worksheet(sheet_name)
    setup(ws, title, formats, 11)
    row = 3
    headers = ["DESCRIPCION", "AÑO 0"] + YEAR_LABELS
    for col, header in enumerate(headers):
        ws.write(row, col, header, formats["header"])
    row += 1
    lines = [
        ("Inversion", [INITIAL_INVESTMENT] + [0] * 10),
        ("Flujo de ingresos", [0] + model["cash_income"]),
        ("Flujo de egresos", [0] + model["cash_egress"]),
        ("Flujo de efectivo", [0] + [model["cash_income"][i] - model["cash_egress"][i] for i in range(10)]),
        ("Mas liquidacion cuentas por cobrar", [0] * 10 + [model["cxc_end"][-1]]),
        ("Mas liquidacion inventarios finales", [0] * 11),
        ("Mas valor de salvamento", [0] * 10 + [SALVAGE_VALUE]),
        ("Menos pasivo circulante", [0] * 10 + [-(model["cxp_end"][-1] + model["income_tax"][-1])]),
        ("Flujo Neto de efectivo", [INITIAL_INVESTMENT] + model["flow_net"]),
    ]
    line_rows = {}
    for label, values in lines:
        line_rows[label] = row
        total = label == "Flujo Neto de efectivo"
        ws.write(row, 0, label, formats["total"] if total else formats["label"])
        for col, value in enumerate(values, start=1):
            ws.write_number(row, col, value, formats["total"] if total else formats["money"])
        row += 1
    if sheet_name == "FLUJO DE EFECTIVO":
        for col in range(1, 12):
            ws.write_formula(
                line_rows["Inversion"],
                col,
                "=inversion_inicial" if col == 1 else "=0",
                formats["money"],
                money(([INITIAL_INVESTMENT] + [0] * 10)[col - 1]),
            )
            ws.write_formula(
                line_rows["Flujo de ingresos"],
                col,
                "=0" if col == 1 else f"=INDEX(ingresos_efectivo_base,1,{col - 1})",
                formats["money"],
                money(([0] + model["cash_income"])[col - 1]),
            )
            ws.write_formula(
                line_rows["Flujo de egresos"],
                col,
                "=0" if col == 1 else f"=INDEX(egresos_efectivo_base,1,{col - 1})",
                formats["money"],
                money(([0] + model["cash_egress"])[col - 1]),
            )
        ws.write_formula(
            line_rows["Mas liquidacion cuentas por cobrar"],
            11,
            "=INDEX(cuentas_cobrar_finales,1,10)",
            formats["money"],
            money(model["cxc_end"][-1]),
        )
        ws.write_formula(
            line_rows["Mas valor de salvamento"],
            11,
            "=valor_salvamento",
            formats["money"],
            money(SALVAGE_VALUE),
        )
        ws.write_formula(
            line_rows["Menos pasivo circulante"],
            11,
            "=-(INDEX(cuentas_pagar_finales,1,10)+INDEX(impuesto_renta_anual,1,10))",
            formats["money"],
            money(-(model["cxp_end"][-1] + model["income_tax"][-1])),
        )
    for col in range(1, 12):
        ws.write_formula(
            line_rows["Flujo de efectivo"],
            col,
            f"={cell(line_rows['Flujo de ingresos'], col)}-{cell(line_rows['Flujo de egresos'], col)}",
            formats["money"],
            money(([0] + [model["cash_income"][i] - model["cash_egress"][i] for i in range(10)])[col - 1]),
        )
        ws.write_formula(
            line_rows["Flujo Neto de efectivo"],
            col,
            f"={cell(line_rows['Inversion'], col)}"
            if col == 1
            else f"=SUM({cell(line_rows['Flujo de efectivo'], col)}:{cell(line_rows['Menos pasivo circulante'], col)})",
            formats["total"],
            money(([INITIAL_INVESTMENT] + model["flow_net"])[col - 1]),
        )

    if sheet_name != "FLUJO DE EFECTIVO":
        row += 2
        ws.write(row, 0, "Flujo para evaluacion", formats["subtitle"])
        evaluation_row = row
        for col in range(1, 12):
            ws.write_formula(
                row,
                col,
                f"=-{cell(line_rows['Flujo Neto de efectivo'], col)}"
                if col == 1
                else f"={cell(line_rows['Flujo Neto de efectivo'], col)}",
                formats["money"],
                money(model["flows_for_valuation"][col - 1]),
            )
        row += 1
        ws.write(row, 0, "Tasa de corte", formats["label"])
        ws.write_number(row, 1, model["cut_rate"], formats["percent"])
        cut_rate_cell = cell(row, 1)
        row += 1
        ws.write(row, 0, "Valor actual neto", formats["total"])
        ws.write_formula(
            row,
            1,
            f"=NPV({cut_rate_cell},{cell(evaluation_row, 2)}:{cell(evaluation_row, 11)})+{cell(evaluation_row, 1)}",
            formats["total"],
            model["npv"],
        )
        van_excel_row = row + 1
        row += 1
        ws.write(row, 0, "Tasa interna de retorno", formats["total"])
        ws.write_formula(
            row,
            1,
            f"=IRR({cell(evaluation_row, 1)}:{cell(evaluation_row, 11)})",
            formats["total_pct"],
            model["irr"],
        )
        row += 1
        ws.write(row, 0, "Indice de rentabilidad", formats["total"])
        ws.write_formula(
            row,
            1,
            f"=(B{van_excel_row}+ABS({cell(evaluation_row, 1)}))/ABS({cell(evaluation_row, 1)})",
            formats["total_num"],
            model["profitability_index"],
        )
        row += 1
        decision = "PROYECTO SE ACEPTA" if model["npv"] > 0 and model["irr"] > model["cut_rate"] else "PROYECTO NO SE ACEPTA"
        ws.write(row, 0, "Comentario", formats["subtitle"])
        ws.write(row, 1, decision, formats["text"])


def write_cost_capital(workbook, model, formats):
    ws = workbook.add_worksheet("COSTO CAPITAL VAN TIR IR")
    setup(ws, "Costo de Capital, VAN, TIR e IR", formats, 15)
    row = 3
    ws.write(row, 0, "Concepto", formats["header"])
    ws.write(row, 1, "Monto de la inversion", formats["header"])
    ws.write(row, 2, "%", formats["header"])
    ws.write(row, 3, "Costo", formats["header"])
    ws.write(row, 4, "Costo promedio", formats["header"])
    for col, label in enumerate(YEAR_LABELS, start=6):
        ws.write(row, col, label, formats["header"])
    row += 1

    base_row = row
    capital_rows = [
        ("Fondos propios", model["equity"], EQUITY_COST),
        ("Financiamiento", model["loan"], model["interest_rate"]),
    ]
    for offset, (label, amount, cost) in enumerate(capital_rows):
        ws.write(row, 0, label, formats["label"])
        ws.write_formula(
            row,
            1,
            "=inversion_inicial*participacion_capital" if offset == 0 else "=inversion_inicial*participacion_deuda",
            formats["money"],
            amount,
        )
        excel_row = row + 1
        ws.write_formula(row, 2, f"=B{excel_row}/SUM($B${base_row + 1}:$B${base_row + 2})", formats["percent"], [EQUITY_SHARE, LOAN_SHARE][offset])
        ws.write_formula(
            row,
            3,
            "=costo_capital_propio" if offset == 0 else "=tasa_deuda*(1-tasa_impuesto_renta)",
            formats["percent"],
            cost if offset == 0 else cost * (1 - INCOME_TAX),
        )
        ws.write_formula(
            row,
            4,
            f"=C{excel_row}*D{excel_row}",
            formats["percent"],
            [EQUITY_SHARE * EQUITY_COST, LOAN_SHARE * model["interest_rate"] * (1 - INCOME_TAX)][offset],
        )
        row += 1

    ws.write(row, 0, "WACC nominal despues de impuestos", formats["label"])
    ws.write_formula(row, 4, f"=SUM(E{base_row + 1}:E{base_row + 2})", formats["percent"], model["cost_capital"])
    cost_capital_row = row + 1
    row += 1

    ws.write(row, 0, "Inflacion esperada anual", formats["label"])
    inflation_values_row = row + 1
    for col, value in enumerate(INFLATION, start=6):
        ws.write_formula(row, col, "=inflacion_esperada", formats["percent"], value)
    row += 1

    ws.write(row, 0, "Inflacion promedio", formats["label"])
    ws.write_formula(row, 4, f"=AVERAGE(G{inflation_values_row}:P{inflation_values_row})", formats["percent"], model["avg_inflation"])
    inflation_row = row + 1
    row += 1

    ws.write(row, 0, "WACC real", formats["label"])
    ws.write_formula(row, 4, f"=(1+E{cost_capital_row})/(1+E{inflation_row})-1", formats["percent"], model["real_cost_capital"])
    real_cost_capital_row = row + 1
    row += 1

    ws.write(row, 0, "Prima especifica del proyecto", formats["label"])
    ws.write_formula(row, 4, "=prima_riesgo_proyecto", formats["percent"], model["risk"])
    risk_row = row + 1
    row += 1

    ws.write(row, 0, "Tasa de corte", formats["total"])
    ws.write_formula(row, 4, f"=(1+E{real_cost_capital_row})*(1+E{risk_row})-1", formats["total_pct"], model["cut_rate"])
    cut_rate_row = row + 1
    row += 1

    row += 2
    ws.write(row, 0, "Valor Actual Neto", formats["subtitle"])
    row += 1
    ws.write(row, 0, "Flujos netos", formats["header"])
    ws.write(row, 1, "Flujos descontados", formats["header"])
    row += 1
    first_flow_row = row + 1
    for i, flow in enumerate(model["flows_for_valuation"]):
        label = "INVERSION INICIAL" if i == 0 else f"FLUJO AÑO {i}"
        ws.write(row, 0, label, formats["label"])
        source_col = i + 1
        source_formula = f"=-{sheet_cell('FLUJO DE EFECTIVO', 12, source_col)}" if i == 0 else f"={sheet_cell('FLUJO DE EFECTIVO', 12, source_col)}"
        ws.write_formula(row, 1, source_formula, formats["money"], money(flow))
        excel_row = row + 1
        ws.write_formula(row, 2, f"=B{excel_row}/((1+$E${cut_rate_row})^{i})", formats["money"], flow / ((1 + model["cut_rate"]) ** i))
        row += 1
    last_flow_row = row
    row += 1
    ws.write(row, 0, "VAN", formats["total"])
    ws.write_formula(row, 1, f"=SUM(C{first_flow_row}:C{last_flow_row})", formats["total"], model["npv"])
    workbook.define_name("van_base", f"='COSTO CAPITAL VAN TIR IR'!$B${row + 1}")
    van_row = row + 1
    row += 1
    ws.write(row, 0, "TIR", formats["total"])
    ws.write_formula(row, 1, f"=IRR(B{first_flow_row}:B{last_flow_row})", formats["total_pct"], model["irr"])
    workbook.define_name("tir_base", f"='COSTO CAPITAL VAN TIR IR'!$B${row + 1}")
    row += 1
    ws.write(row, 0, "Indice de rentabilidad", formats["total"])
    ws.write_formula(row, 1, f"=(B{van_row}+ABS(B{first_flow_row}))/ABS(B{first_flow_row})", formats["total_num"], model["profitability_index"])
    workbook.define_name("indice_rentabilidad_base", f"='COSTO CAPITAL VAN TIR IR'!$B${row + 1}")
    row += 1
    ws.write(row, 0, "Periodo recuperacion descontado", formats["total"])
    ws.write_number(row, 1, model["payback"], formats["total_num"])
    row += 1
    decision = "PROYECTO SE ACEPTA" if model["npv"] > 0 and model["irr"] > model["cut_rate"] and model["profitability_index"] > 1 else "PROYECTO CONDICIONADO"
    ws.write(row, 0, "Resultado", formats["subtitle"])
    ws.write(row, 1, decision, formats["text"])


def write_risk_admin(workbook, model, admin_model, formats):
    write_planilla(workbook, admin_model, formats, admin_factor=1.15, sheet_name="Riesgo Administrativo")
    ws = workbook.get_worksheet_by_name("Riesgo Administrativo")
    row = 392
    ws.write(row, 0, "RESUMEN DEL RIESGO ADMINISTRATIVO", formats["subtitle"])
    row += 1
    row = write_year_header(ws, row, formats)
    row = write_series(ws, row, "Flujo neto base", model["flow_net"], formats)
    row = write_series(ws, row, "Flujo neto con gastos administrativos +15%", admin_model["flow_net"], formats)
    row = write_series(ws, row, "Diferencia", [admin_model["flow_net"][i] - model["flow_net"][i] for i in range(10)], formats)
    ws.write(row + 1, 0, f"VAN escenario administrativo: S/ {admin_model['npv']:,.0f}", formats["note"])


def write_price_analysis(workbook, base_model, formats):
    ws = workbook.add_worksheet("Analisis Precio")
    setup(ws, "Analisis de Precio y contraste de supuestos - MuseIQ", formats, 11)
    row = 3
    row = write_section(ws, row, "COMPARACION ENTRE EL LIBRO ANTERIOR Y EL MODELO REVISADO", formats, 5)
    for col, label in enumerate(["Indicador", "Modelo anterior", "Modelo revisado", "Variacion", "Lectura"]):
        ws.write(row, col, label, formats["header"])
    row += 1
    comparisons = [
        ("Museos captados", 31, 35, "La cartera se alinea con el Capitulo 5."),
        ("Factor adicional sobre precios", 1.20, PRICE_ADJUSTMENT, "Se elimina el recargo duplicado de 20%."),
        ("Ventas acumuladas", 10_085_737.40, sum(base_model["sales_total"]), "El ingreso baja aun atendiendo cuatro museos adicionales."),
        ("Costos directos acumulados", 2_611_928.80, sum(base_model["direct_total"]), "Se reconocen mayores costos de despliegue y soporte."),
        ("VAN", 148_934.56, base_model["npv"], "La rentabilidad se mantiene positiva sin flujo inflado."),
    ]
    for label, previous, revised, note in comparisons:
        ws.write(row, 0, label, formats["label"])
        if "Factor" in label:
            ws.write_number(row, 1, previous, formats["number"])
            ws.write_formula(row, 2, "=factor_precio_base", formats["formula"], revised)
            ws.write_formula(row, 3, f"=C{row + 1}/B{row + 1}-1", formats["percent"], revised / previous - 1)
        elif label == "Museos captados":
            ws.write_number(row, 1, previous, formats["integer"])
            ws.write_formula(row, 2, "=SUM(nuevos_B)+SUM(nuevos_E)+SUM(nuevos_A)", formats["formula"], revised)
            ws.write_formula(row, 3, f"=C{row + 1}-B{row + 1}", formats["integer"], revised - previous)
        elif label == "Ventas acumuladas":
            ws.write_number(row, 1, previous, formats["money"])
            ws.write_formula(row, 2, "=SUM(INGRESOS!B19:K19)", formats["formula_money"], revised)
            ws.write_formula(row, 3, f"=C{row + 1}/B{row + 1}-1", formats["percent"], revised / previous - 1)
        elif label == "Costos directos acumulados":
            ws.write_number(row, 1, previous, formats["money"])
            ws.write_formula(row, 2, "=SUM(COSTOS!B8:K8)", formats["formula_money"], revised)
            ws.write_formula(row, 3, f"=C{row + 1}/B{row + 1}-1", formats["percent"], revised / previous - 1)
        else:
            ws.write_number(row, 1, previous, formats["money"])
            ws.write_formula(row, 2, "=van_base", formats["formula_money"], revised)
            ws.write_formula(row, 3, f"=C{row + 1}/B{row + 1}-1", formats["percent"], revised / previous - 1)
        ws.write(row, 4, note, formats["text"])
        row += 1

    row += 2
    row = write_section(ws, row, "SENSIBILIDAD DE PRECIOS", formats, 5)
    ws.write(row, 0, "Escenario", formats["header"])
    ws.write(row, 1, "Factor precio", formats["header"])
    ws.write(row, 2, "Ventas acumuladas", formats["header"])
    ws.write(row, 3, "VAN", formats["header"])
    ws.write(row, 4, "TIR", formats["header"])
    ws.write(row, 5, "IR", formats["header"])
    scenarios = [
        ("Precio -15%", 0.85),
        ("Precio -10%", 0.90),
        ("Precio base", 1.00),
        ("Precio +10%", 1.10),
        ("Precio +15%", 1.15),
    ]
    row += 1
    for label, factor in scenarios:
        model = build_model(name=label, revenue_factor=factor)
        ws.write(row, 0, label, formats["label"])
        ws.write_number(row, 1, factor, formats["percent"])
        ws.write_number(row, 2, sum(model["sales_total"]), formats["money"])
        ws.write_number(row, 3, model["npv"], formats["money"])
        ws.write_number(row, 4, model["irr"], formats["percent"])
        ws.write_number(row, 5, model["profitability_index"], formats["number"])
        row += 1
    row += 2
    row = write_year_header(ws, row, formats)
    row = write_series(ws, row, "Ventas escenario base", base_model["sales_total"], formats)
    reduced = build_model(name="Precio -10%", revenue_factor=0.90)
    row = write_series(ws, row, "Ventas precio -10%", reduced["sales_total"], formats)
    row = write_series(ws, row, "Diferencia", [reduced["sales_total"][i] - base_model["sales_total"][i] for i in range(10)], formats)


def write_all() -> None:
    base = build_model()
    low_income = build_model(name="Ingresos -20%", revenue_factor=0.80)
    high_cost = build_model(name="Gastos +10%", cost_factor=1.10)
    high_interest = build_model(name="Interes 24%", interest_rate=LOAN_RATE_STRESS)
    bad_debt = build_model(name="No recuperacion CxC 20%", bad_debt_rate=0.20)
    admin_risk = build_model(name="Admin +15%", admin_factor=1.15)
    optimistic = build_model(name="Optimista", revenue_factor=1.12, cost_factor=1.03)
    reduced_price = build_model(name="Precio -10%", revenue_factor=0.90)

    workbook = xlsxwriter.Workbook(OUT)
    workbook.set_calc_mode("auto")
    formats = make_formats(workbook)
    write_assumptions(workbook, base, formats)
    write_ingresos(workbook, base, formats)
    write_costos(workbook, base, formats)
    write_unit_cost(workbook, base, formats)
    write_planilla(workbook, base, formats)
    write_expenses_finance(workbook, base, formats)
    write_depreciation(workbook, base, formats)
    write_investment_plan(workbook, base, formats)
    write_opening_balance(workbook, base, formats)
    write_cost_of_sales(workbook, base, formats)
    write_income_statement(workbook, base, formats)
    write_cash_budget(workbook, base, formats)
    write_balance(workbook, base, formats)
    write_ratios(workbook, base, formats)
    write_ratio_comments(workbook, base, formats)
    write_break_even(workbook, base, formats)
    write_flow_sheet(workbook, base, formats, "FLUJO DE EFECTIVO", "Flujo Neto de Efectivo - Original")
    write_cost_capital(workbook, base, formats)
    write_flow_sheet(workbook, low_income, formats, "Sensibilidad Ingresos Bajos", "Flujo Neto Pesimista - Ingresos -20%")
    write_flow_sheet(workbook, high_cost, formats, "Sensibilidad Incremento Gastos", "Flujo Neto Pesimista - Gastos +10%")
    write_flow_sheet(workbook, high_interest, formats, "Sensibilidad Incremento Interes", "Flujo Neto Pesimista - Interes 24%")
    write_flow_sheet(workbook, bad_debt, formats, "Riesgo no recuperacion CxC", "Riesgo de no recuperacion de Cuentas por Cobrar")
    write_risk_admin(workbook, base, admin_risk, formats)
    write_flow_sheet(workbook, optimistic, formats, "Flujo Optimista", "Flujo Neto de Efectivo - Optimista")
    write_price_analysis(workbook, base, formats)
    write_cash_budget(workbook, reduced_price, formats, sheet_name="Presupuesto Caja Bajando Precio")
    write_flow_sheet(workbook, reduced_price, formats, "Flujo Efectivo Bajando Precio", "Flujo Neto - Bajando Precio 10%")
    workbook.close()

    print(f"Archivo generado: {OUT}")
    print(f"VAN base: S/ {base['npv']:,.2f}")
    print(f"TIR base: {base['irr']:.2%}")
    print(f"Tasa de corte: {base['cut_rate']:.2%}")
    print(f"Saldo minimo de caja: S/ {min(base['cash_balance']):,.2f}")


if __name__ == "__main__":
    write_all()
