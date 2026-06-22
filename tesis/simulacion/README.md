# Simulacion MuseIQ MVP

Museo virtual top-down para demostrar el flujo conjunto entre:

- `Tesis`: desplazamiento fisico del visitante.
- `iot-museiq`: ubicacion BLE simulada mediante comandos.
- `museApp`: respuesta contextual del guia virtual.

## Espacios del MVP

- `SALA_1`: una sala normal dividida en seis sectores.
- Cada sector contiene una obra y dos QR reales compatibles con `museApp`.
- `SALA_VR`: espacio separado que activa el modo inmersivo mediante `vr`.
- El visitante comienza en un vestibulo de entrada y debe cruzar la puerta
  principal antes de acercarse a la primera obra.

| Comando | Zona | Obra |
| --- | --- | --- |
| `1` | `Z1` | Musico Moche |
| `2` | `Z2` | Botella Chimu-Lambayeque |
| `3` | `Z3` | Aribalo inca |
| `4` | `Z4` | Asiento del Inca |
| `5` | `Z5` | Botella Chavin 204002 |
| `6` | `Z6` | Obelisco Tello |
| `vr` | `S4` | Sala VR |

## Ejecutar

```bash
cd /home/eduardo/proyectos/MuseIQ/Tesis/tesis/simulacion
python3 -m http.server 5500
```

Abre:

```text
http://localhost:5500
```

## Controles

- `WASD` o flechas: mover al visitante.
- `Espacio` o `Enter`: registrar la visita a la obra cercana.
- `R`: reiniciar el recorrido.
- Los botones inferiores permiten saltar entre zonas durante un ensayo.

## Demostracion integrada

En otra terminal:

```bash
cd /home/eduardo/proyectos/MuseIQ/iot-museiq
source .venv/bin/activate
python dev_location_bridge.py --host 0.0.0.0 --port 8787
```

Cuando el visitante entre en una zona de la simulacion, escribe el comando indicado
en `iot-museiq`. El panel de sincronizacion compara la posicion fisica con el estado
del bridge y confirma cuando ambos coinciden.

La URL predeterminada del bridge se calcula usando el mismo host de la simulacion y
el puerto `8787`. Puede cambiarse desde el panel lateral.

## QR

Los doce QR contienen exactamente los codigos consumidos por `museApp`:

```text
SALA_1-01-A / SALA_1-01-B
...
SALA_1-06-A / SALA_1-06-B
```
