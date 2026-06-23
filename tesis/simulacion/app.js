const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");

const ui = {
  artworkImage: document.getElementById("artwork-image"),
  artworkKicker: document.getElementById("artwork-kicker"),
  artworkMeta: document.getElementById("artwork-meta"),
  artworkSummary: document.getElementById("artwork-summary"),
  artworkTitle: document.getElementById("artwork-title"),
  bridgeBadge: document.getElementById("bridge-badge"),
  bridgeForm: document.getElementById("bridge-form"),
  bridgeUrl: document.getElementById("bridge-url"),
  canvasHint: document.getElementById("canvas-hint"),
  commandReadout: document.getElementById("command-readout"),
  directionText: document.getElementById("direction-text"),
  expectedCommand: document.getElementById("expected-command"),
  lastAction: document.getElementById("last-action"),
  locationDot: document.getElementById("location-dot"),
  physicalLocation: document.getElementById("physical-location"),
  positionText: document.getElementById("position-text"),
  qrAImage: document.getElementById("qr-a-image"),
  qrATitle: document.getElementById("qr-a-title"),
  qrACode: document.getElementById("qr-a-code"),
  qrBImage: document.getElementById("qr-b-image"),
  qrBTitle: document.getElementById("qr-b-title"),
  qrBCode: document.getElementById("qr-b-code"),
  qrGrid: document.getElementById("qr-grid"),
  resetButton: document.getElementById("reset-button"),
  resourceCount: document.getElementById("resource-count"),
  resourceKicker: document.getElementById("resource-kicker"),
  resourceTitle: document.getElementById("resource-title"),
  roomStatus: document.getElementById("room-status"),
  syncDetail: document.getElementById("sync-detail"),
  syncState: document.getElementById("sync-state"),
  syncTitle: document.getElementById("sync-title"),
  visitedCounter: document.getElementById("visited-counter"),
  vrResources: document.getElementById("vr-resources"),
  zoneChip: document.getElementById("zone-chip"),
};

const tileSize = 48;
const cols = 24;
const rows = 16;
const keys = new Set();
const visitedZones = new Set();

const resourceData = [
  [
    ["SALA_1-01-A", "Músico Moche en 3D", "Explora la postura, la vestimenta y el instrumento del personaje."],
    ["SALA_1-01-B", "Botella Chimú-Lambayeque", "Compara dos tradiciones cerámicas de la costa norte."],
  ],
  [
    ["SALA_1-02-A", "Botella Chimú-Lambayeque en 3D", "Observa la figura animal, el asa y el acabado de la botella."],
    ["SALA_1-02-B", "Músico Moche", "Regresa al personaje Moche para comparar modelado y función."],
  ],
  [
    ["SALA_1-03-A", "Aríbalo inca en 3D", "Explora la forma, las asas laterales y la base cónica."],
    ["SALA_1-03-B", "Asiento del Inca", "Compara un recipiente móvil con una estructura ceremonial."],
  ],
  [
    ["SALA_1-04-A", "Asiento del Inca en 3D", "Recorre la superficie tallada y la relación con su base."],
    ["SALA_1-04-B", "Aríbalo inca", "Relaciona autoridad, espacio ceremonial y cultura material inca."],
  ],
  [
    ["SALA_1-05-A", "Botella Chavín 204002 en 3D", "Examina los felinos estilizados del asa, el gollete y el cuerpo."],
    ["SALA_1-05-B", "Obelisco Tello", "Compara la iconografía cerámica con un monolito monumental."],
  ],
  [
    ["SALA_1-06-A", "Obelisco Tello en 3D", "Gira el monolito para recorrer la composición de sus cuatro caras."],
    ["SALA_1-06-B", "Botella Chavín 204002", "Relaciona los felinos de la botella con el lenguaje del monolito."],
  ],
];

const artworks = [
  {
    id: "obra-1-1-L",
    zoneId: "Z1",
    command: "1",
    title: "Músico Moche",
    meta: "Cultura Moche · 200-850 d.C.",
    summary: "Botella escultórica que representa a un músico tocando una quena o flauta andina.",
    image: "src/imgs/mvp/01-musico-moche.png",
    x: 3.5 * tileSize,
    y: 3.5 * tileSize,
    color: "#e7b84c",
  },
  {
    id: "obra-1-1-C",
    zoneId: "Z2",
    command: "2",
    title: "Botella Chimú-Lambayeque",
    meta: "Estilo Chimú-Lambayeque · 1000-1470 d.C.",
    summary: "Botella escultórica de cerámica repatriada al Perú en 2023.",
    image: "src/imgs/mvp/02-botella-chimu-lambayeque.png",
    x: 9.5 * tileSize,
    y: 3.5 * tileSize,
    color: "#56a4e8",
  },
  {
    id: "obra-1-1-R",
    zoneId: "Z3",
    command: "3",
    title: "Aríbalo inca",
    meta: "Horizonte Tardío · 1470-1532 d.C.",
    summary: "Recipiente inca de cuello tubular, cuerpo amplio, asas laterales y base cónica.",
    image: "src/imgs/mvp/03-aribalo-inca.png",
    x: 15.5 * tileSize,
    y: 3.5 * tileSize,
    color: "#c989dc",
  },
  {
    id: "obra-1-2-L",
    zoneId: "Z4",
    command: "4",
    title: "Asiento del Inca",
    meta: "Tradición Inca · piedra tallada",
    summary: "Estructura lítica asociada a autoridad, presencia pública y espacio ceremonial.",
    image: "src/imgs/mvp/04-asiento-del-inca.png",
    x: 3.5 * tileSize,
    y: 9.5 * tileSize,
    color: "#ef806d",
  },
  {
    id: "obra-1-2-C",
    zoneId: "Z5",
    command: "5",
    title: "Botella Chavín 204002",
    meta: "Tradición Chavín · cerámica monocroma pulida",
    summary: "Botella escultórica de asa estribo con cabezas y rostros de felinos estilizados.",
    image: "src/imgs/mvp/05-botella-chavin-204002.png",
    x: 9.5 * tileSize,
    y: 9.5 * tileSize,
    color: "#4dc8a4",
  },
  {
    id: "obra-1-2-R",
    zoneId: "Z6",
    command: "6",
    title: "Obelisco Tello",
    meta: "Tradición Chavín · piedra tallada",
    summary: "Monolito de cuatro caras cubierto por seres, plantas y rasgos animales entrelazados.",
    image: "src/imgs/mvp/06-obelisco-tello.png",
    x: 15.5 * tileSize,
    y: 9.5 * tileSize,
    color: "#e19a52",
  },
].map((artwork, index) => ({
  ...artwork,
  resources: resourceData[index].map(([code, title, subtitle]) => ({
    code,
    title,
    subtitle,
    image: `src/qr/${code}.png`,
  })),
}));

const vrRoom = {
  id: "SALA_VR",
  zoneId: "S4",
  command: "vr",
  title: "Sala VR",
  meta: "Modo inmersivo · cuatro experiencias disponibles",
  summary: "Espacio sin obras físicas activas. El beacon S4 habilita en MuseIQ la selección de recorridos inmersivos preparados para headset.",
  image: "src/imgs/mvp/sala-vr.png",
  color: "#22c5c3",
};

const player = {
  x: 9.5 * tileSize,
  y: 14.45 * tileSize,
  radius: 14,
  heading: 0,
  speed: 245,
};

const initialPlayer = { x: player.x, y: player.y, heading: player.heading };
const imageCache = new Map();
let activeTarget = null;
let lastTargetKey = "";
let lastFrameAt = performance.now();
let bridgeSnapshot = null;
let bridgeConnected = false;
let bridgePollTimer = null;
let pendingBridgeCommand = null;
let bridgeCommandSyncPromise = null;

function preloadImage(src) {
  if (imageCache.has(src)) {
    return imageCache.get(src);
  }

  const image = new Image();
  image.src = src;
  imageCache.set(src, image);
  return image;
}

[...artworks.flatMap((artwork) => [artwork.image, ...artwork.resources.map((resource) => resource.image)]), vrRoom.image]
  .forEach(preloadImage);

function getTileType(tileX, tileY) {
  if (tileX < 0 || tileY < 0 || tileX >= cols || tileY >= rows) {
    return "wall";
  }

  if (tileX === 0 || tileX === cols - 1 || tileY === 0 || tileY === rows - 1) {
    return "wall";
  }

  if (tileY === 13) {
    return tileX === 9 || tileX === 10 ? "door" : "wall";
  }

  if (tileY === 14) {
    return tileX >= 7 && tileX <= 12 ? "floor" : "wall";
  }

  if (tileX === 19) {
    return tileY === 6 || tileY === 7 ? "door" : "wall";
  }

  if (tileX >= 20 && (tileY === 1 || tileY === 12)) {
    return "wall";
  }

  return "floor";
}

function isWalkablePixel(x, y) {
  return ["floor", "door"].includes(
    getTileType(Math.floor(x / tileSize), Math.floor(y / tileSize)),
  );
}

function movePlayer(dx, dy) {
  const nextX = player.x + dx;
  const nextY = player.y + dy;
  const radius = player.radius;

  const canMoveX = [
    [nextX - radius, player.y - radius],
    [nextX + radius, player.y - radius],
    [nextX - radius, player.y + radius],
    [nextX + radius, player.y + radius],
  ].every(([x, y]) => isWalkablePixel(x, y));

  if (canMoveX) {
    player.x = nextX;
  }

  const canMoveY = [
    [player.x - radius, nextY - radius],
    [player.x + radius, nextY - radius],
    [player.x - radius, nextY + radius],
    [player.x + radius, nextY + radius],
  ].every(([x, y]) => isWalkablePixel(x, y));

  if (canMoveY) {
    player.y = nextY;
  }
}

function updatePlayer(deltaSeconds) {
  let dx = 0;
  let dy = 0;

  if (keys.has("arrowleft") || keys.has("a")) {
    dx -= 1;
    player.heading = 270;
  }
  if (keys.has("arrowright") || keys.has("d")) {
    dx += 1;
    player.heading = 90;
  }
  if (keys.has("arrowup") || keys.has("w")) {
    dy -= 1;
    player.heading = 0;
  }
  if (keys.has("arrowdown") || keys.has("s")) {
    dy += 1;
    player.heading = 180;
  }

  if (dx !== 0 && dy !== 0) {
    const diagonal = Math.SQRT1_2;
    dx *= diagonal;
    dy *= diagonal;
  }

  movePlayer(dx * player.speed * deltaSeconds, dy * player.speed * deltaSeconds);
}

function getPhysicalTarget() {
  const tileX = player.x / tileSize;
  const tileY = player.y / tileSize;

  if (tileX >= 20 && tileY >= 2 && tileY <= 11) {
    return vrRoom;
  }

  let closest = null;
  let closestDistance = Infinity;

  artworks.forEach((artwork) => {
    const distance = Math.hypot(player.x - artwork.x, player.y - artwork.y);
    if (distance < closestDistance) {
      closest = artwork;
      closestDistance = distance;
    }
  });

  return closestDistance <= 112 ? closest : null;
}

function isInEntrance() {
  return player.y / tileSize >= 13.5;
}

function getHeadingLabel(heading) {
  if (heading >= 315 || heading < 45) {
    return "Norte";
  }
  if (heading < 135) {
    return "Este";
  }
  if (heading < 225) {
    return "Sur";
  }
  return "Oeste";
}

function setLastAction(message) {
  ui.lastAction.textContent = message;
}

function updateRouteStrip() {
  document.querySelectorAll(".route-step").forEach((button) => {
    const command = button.dataset.command;
    button.classList.toggle("active", activeTarget?.command === command);
    button.classList.toggle("visited", command !== "vr" && visitedZones.has(command));
  });
}

function renderRoomOverview() {
  ui.artworkImage.src = "src/imgs/mvp/01-musico-moche.png";
  ui.artworkImage.alt = "Sala 1";
  ui.artworkKicker.textContent = "Recorrido listo";
  ui.artworkTitle.textContent = "Sala 1";
  ui.artworkMeta.textContent = "6 sectores · 6 obras · 12 recursos QR";
  ui.artworkSummary.textContent =
    "Aproxímate a una pieza. La simulación enviará automáticamente la zona activa a iot-museiq para que MuseIQ responda al recorrido.";
  ui.zoneChip.textContent = "SALA_1";
  ui.qrGrid.hidden = true;
  ui.vrResources.hidden = true;
  ui.resourceCount.textContent = "Sin zona";
  ui.resourceKicker.textContent = "Recursos de la obra";
  ui.resourceTitle.textContent = "QR disponibles";
}

function renderEntrance() {
  ui.artworkImage.src = "src/imgs/mvp/01-musico-moche.png";
  ui.artworkImage.alt = "Entrada principal de MuseIQ";
  ui.artworkKicker.textContent = "Inicio del recorrido";
  ui.artworkTitle.textContent = "Entrada principal";
  ui.artworkMeta.textContent = "Acceso a Sala 1";
  ui.artworkSummary.textContent =
    "El visitante comienza aquí. Avanza hacia el norte, cruza la puerta y acércate a la primera obra para activar el recorrido contextual.";
  ui.zoneChip.textContent = "ENTRADA";
  ui.qrGrid.hidden = true;
  ui.vrResources.hidden = true;
  ui.resourceCount.textContent = "Inicio";
  ui.resourceKicker.textContent = "Recorrido MuseIQ";
  ui.resourceTitle.textContent = "Preparado para ingresar";
}

function renderArtwork(artwork) {
  ui.artworkImage.src = artwork.image;
  ui.artworkImage.alt = artwork.title;
  ui.artworkKicker.textContent = `${artwork.zoneId} · ${artwork.id}`;
  ui.artworkTitle.textContent = artwork.title;
  ui.artworkMeta.textContent = artwork.meta;
  ui.artworkSummary.textContent = artwork.summary;
  ui.zoneChip.textContent = `${artwork.zoneId} · comando ${artwork.command}`;
  ui.resourceCount.textContent = "2 QR";
  ui.resourceKicker.textContent = "Recursos de la obra";
  ui.resourceTitle.textContent = "QR disponibles";
  ui.qrGrid.hidden = false;
  ui.vrResources.hidden = true;

  const [resourceA, resourceB] = artwork.resources;
  ui.qrAImage.src = resourceA.image;
  ui.qrAImage.alt = `QR ${resourceA.code}`;
  ui.qrATitle.textContent = resourceA.title;
  ui.qrACode.textContent = resourceA.code;
  ui.qrBImage.src = resourceB.image;
  ui.qrBImage.alt = `QR ${resourceB.code}`;
  ui.qrBTitle.textContent = resourceB.title;
  ui.qrBCode.textContent = resourceB.code;
}

function renderVrRoom() {
  ui.artworkImage.src = vrRoom.image;
  ui.artworkImage.alt = "Sala VR";
  ui.artworkKicker.textContent = "S4 · SALA_VR";
  ui.artworkTitle.textContent = vrRoom.title;
  ui.artworkMeta.textContent = vrRoom.meta;
  ui.artworkSummary.textContent = vrRoom.summary;
  ui.zoneChip.textContent = "S4 · comando vr";
  ui.resourceCount.textContent = "4 experiencias";
  ui.resourceKicker.textContent = "Sala inmersiva";
  ui.resourceTitle.textContent = "Experiencias disponibles";
  ui.qrGrid.hidden = true;
  ui.vrResources.hidden = false;
}

function updatePhysicalState() {
  activeTarget = getPhysicalTarget();
  const entranceActive = isInEntrance();
  const targetKey = activeTarget?.id ?? (entranceActive ? "entrance" : "room");

  if (targetKey !== lastTargetKey) {
    lastTargetKey = targetKey;
    if (entranceActive) {
      renderEntrance();
      setLastAction("Visitante en la entrada");
    } else if (!activeTarget) {
      renderRoomOverview();
      setLastAction("Desplazamiento por Sala 1");
    } else if (activeTarget.id === "SALA_VR") {
      renderVrRoom();
      setLastAction("Ingreso a Sala VR");
    } else {
      renderArtwork(activeTarget);
      setLastAction(`Proximidad detectada: ${activeTarget.zoneId}`);
    }

    scheduleBridgeCommand(activeTarget?.command ?? "clear");
  }

  ui.roomStatus.textContent = entranceActive
    ? "ENTRADA"
    : activeTarget?.id === "SALA_VR"
      ? "SALA_VR"
      : "SALA_1";
  ui.physicalLocation.textContent = entranceActive
    ? "Entrada principal"
    : activeTarget
    ? activeTarget.id === "SALA_VR"
      ? "Sala VR · Beacon S4"
      : `${activeTarget.zoneId} · ${activeTarget.title}`
    : "Pasillo central de Sala 1";
  ui.expectedCommand.textContent = entranceActive ? "--" : activeTarget?.command ?? "--";
  ui.commandReadout.classList.toggle("vr", activeTarget?.id === "SALA_VR");
  ui.locationDot.classList.toggle("active", Boolean(activeTarget));
  ui.locationDot.classList.toggle("vr", activeTarget?.id === "SALA_VR");
  ui.positionText.textContent = `${(player.x / tileSize).toFixed(1)}, ${(player.y / tileSize).toFixed(1)}`;
  ui.directionText.textContent = getHeadingLabel(player.heading);
  ui.visitedCounter.textContent = `${visitedZones.size} / 6`;
  ui.canvasHint.textContent = entranceActive
    ? "Avanza hacia el norte para ingresar a Sala 1"
    : activeTarget
    ? activeTarget.id === "SALA_VR"
      ? "Sala VR sincronizada automáticamente con iot-museiq"
      : `Zona ${activeTarget.command} sincronizada con iot-museiq · Espacio para registrar visita`
    : "Acércate a una obra o cruza hacia la Sala VR";

  updateRouteStrip();
  updateSyncState();
}

function interact() {
  if (!activeTarget) {
    setLastAction("No hay una pieza al alcance");
    return;
  }

  if (activeTarget.id === "SALA_VR") {
    setLastAction("Sala VR registrada y sincronizada");
    return;
  }

  visitedZones.add(activeTarget.command);
  setLastAction(`Visita registrada: ${activeTarget.title}`);
  updateRouteStrip();
  ui.visitedCounter.textContent = `${visitedZones.size} / 6`;
}

function resetTour() {
  player.x = initialPlayer.x;
  player.y = initialPlayer.y;
  player.heading = initialPlayer.heading;
  visitedZones.clear();
  activeTarget = null;
  lastTargetKey = "";
  setLastAction("Recorrido reiniciado");
  updatePhysicalState();
  canvas.focus();
}

function teleportTo(command) {
  if (command === "vr") {
    player.x = 21.4 * tileSize;
    player.y = 7.2 * tileSize;
    player.heading = 0;
  } else {
    const artwork = artworks.find((item) => item.command === command);
    if (!artwork) {
      return;
    }
    player.x = artwork.x;
    player.y = artwork.y + 86;
    player.heading = 0;
  }

  setLastAction(`Ensayo rápido: comando ${command}`);
  updatePhysicalState();
  canvas.focus();
}

function getBridgeCommand(snapshot) {
  if (!snapshot?.enabled || !snapshot.beacon) {
    return null;
  }

  if (snapshot.beacon.roomId === "SALA_VR") {
    return "vr";
  }

  return String(snapshot.beacon.beaconNode ?? "");
}

function getNavigationCommand() {
  return activeTarget?.command ?? "clear";
}

async function sendBridgeCommand(command) {
  const baseUrl = ui.bridgeUrl.value.trim().replace(/\/$/, "");

  if (!baseUrl) {
    return;
  }

  try {
    const response = await fetch(`${baseUrl}/set?zone=${encodeURIComponent(command)}`, {
      cache: "no-store",
      headers: { Accept: "application/json" },
    });

    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }

    bridgeSnapshot = await response.json();
    bridgeConnected = true;
  } catch {
    bridgeSnapshot = null;
    bridgeConnected = false;
  }

  updateSyncState();
}

async function flushBridgeCommands() {
  while (pendingBridgeCommand !== null) {
    const command = pendingBridgeCommand;
    pendingBridgeCommand = null;
    await sendBridgeCommand(command);
  }
}

function scheduleBridgeCommand(command) {
  pendingBridgeCommand = command || "clear";

  if (bridgeCommandSyncPromise) {
    return;
  }

  bridgeCommandSyncPromise = flushBridgeCommands().finally(() => {
    bridgeCommandSyncPromise = null;
    if (pendingBridgeCommand !== null) {
      scheduleBridgeCommand(pendingBridgeCommand);
    }
  });
}

function updateSyncState() {
  ui.bridgeBadge.className = `bridge-badge ${bridgeConnected ? "bridge-online" : "bridge-offline"}`;
  ui.bridgeBadge.textContent = bridgeConnected ? "Conectado" : "Sin conexión";
  ui.syncState.classList.remove("synced", "mismatch");

  if (!bridgeConnected) {
    ui.syncTitle.textContent = "Esperando bridge";
    ui.syncDetail.textContent = "Inicia dev_location_bridge.py y comprueba la URL.";
    return;
  }

  const expected = activeTarget?.command ?? null;
  const actual = getBridgeCommand(bridgeSnapshot);

  if (!actual) {
    ui.syncTitle.textContent = "Bridge activo · simulación pausada";
    ui.syncDetail.textContent = expected
      ? `Enviando automáticamente la zona ${expected}.`
      : "Muévete hacia una obra para iniciar una zona.";
    return;
  }

  if (!expected) {
    ui.syncState.classList.add("mismatch");
    ui.syncTitle.textContent = `iot-museiq está en ${actual}`;
    ui.syncDetail.textContent = "El visitante físico se encuentra fuera de una zona activa.";
    return;
  }

  if (actual === expected) {
    ui.syncState.classList.add("synced");
    ui.syncTitle.textContent = "Recorrido sincronizado";
    ui.syncDetail.textContent = `${activeTarget.zoneId} y el comando ${actual} representan la misma ubicación.`;
    return;
  }

  ui.syncState.classList.add("mismatch");
  ui.syncTitle.textContent = `Desfase: museo ${expected} · iot ${actual}`;
  ui.syncDetail.textContent = `Actualizando iot-museiq automáticamente a la zona ${expected}.`;
}

function defaultBridgeUrl() {
  const hostname = window.location.hostname || "localhost";
  return `http://${hostname}:8787`;
}

async function pollBridge() {
  const baseUrl = ui.bridgeUrl.value.trim().replace(/\/$/, "");

  if (!baseUrl) {
    bridgeConnected = false;
    bridgeSnapshot = null;
    updateSyncState();
    return;
  }

  try {
    const response = await fetch(`${baseUrl}/state`, {
      cache: "no-store",
      headers: { Accept: "application/json" },
    });

    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }

    bridgeSnapshot = await response.json();
    bridgeConnected = true;

    const expected = getNavigationCommand();
    const actual = getBridgeCommand(bridgeSnapshot) ?? "clear";
    if (actual !== expected) {
      scheduleBridgeCommand(expected);
    }
  } catch {
    bridgeSnapshot = null;
    bridgeConnected = false;
  }

  updateSyncState();
}

function startBridgePolling() {
  window.clearInterval(bridgePollTimer);
  localStorage.setItem("museiqBridgeUrl", ui.bridgeUrl.value.trim());
  pollBridge();
  bridgePollTimer = window.setInterval(pollBridge, 800);
}

function drawFloor(tileX, tileY) {
  const x = tileX * tileSize;
  const y = tileY * tileSize;
  const inVr = tileX >= 20;
  const inEntrance = tileY >= 14;
  const column = tileX <= 6 ? 0 : tileX <= 12 ? 1 : 2;
  const row = tileY <= 6 ? 0 : 1;
  const artwork = artworks[row * 3 + column];

  ctx.fillStyle = inEntrance ? "#171c22" : inVr ? "#10272a" : "#24211d";
  ctx.fillRect(x, y, tileSize, tileSize);

  if (!inEntrance && !inVr && tileX <= 18 && artwork) {
    ctx.globalAlpha = 0.07;
    ctx.fillStyle = artwork.color;
    ctx.fillRect(x, y, tileSize, tileSize);
    ctx.globalAlpha = 1;
  }

  ctx.strokeStyle = inEntrance
    ? "rgba(77,163,255,0.16)"
    : inVr
      ? "rgba(34,197,195,0.14)"
      : "rgba(239,211,161,0.08)";
  ctx.strokeRect(x + 3, y + 3, tileSize - 6, tileSize - 6);
}

function drawWall(tileX, tileY) {
  const x = tileX * tileSize;
  const y = tileY * tileSize;
  ctx.fillStyle = "#0a0c0f";
  ctx.fillRect(x, y, tileSize, tileSize);
  ctx.fillStyle = "#171a1e";
  ctx.fillRect(x + 4, y + 4, tileSize - 8, tileSize - 8);
  ctx.strokeStyle = "#242a31";
  ctx.strokeRect(x + 4, y + 4, tileSize - 8, tileSize - 8);
}

function drawDoor(tileX, tileY) {
  drawFloor(tileX, tileY);
  const x = tileX * tileSize;
  const y = tileY * tileSize;
  ctx.fillStyle = "rgba(34,197,195,0.25)";
  ctx.fillRect(x + 10, y + 3, tileSize - 20, tileSize - 6);
  ctx.strokeStyle = "#22c5c3";
  ctx.strokeRect(x + 10, y + 3, tileSize - 20, tileSize - 6);
}

function drawSectorBoundaries() {
  ctx.save();
  ctx.setLineDash([8, 8]);
  ctx.lineWidth = 1;

  [6.5, 12.5].forEach((tileX) => {
    ctx.strokeStyle = "rgba(255,255,255,0.1)";
    ctx.beginPath();
    ctx.moveTo(tileX * tileSize, tileSize);
    ctx.lineTo(tileX * tileSize, 13 * tileSize);
    ctx.stroke();
  });

  ctx.beginPath();
  ctx.moveTo(tileSize, 6.5 * tileSize);
  ctx.lineTo(19 * tileSize, 6.5 * tileSize);
  ctx.stroke();
  ctx.restore();

  artworks.forEach((artwork, index) => {
    const startX = (index % 3) * 6 * tileSize + tileSize;
    const startY = Math.floor(index / 3) * 6 * tileSize + tileSize;
    const isActive = activeTarget?.id === artwork.id;

    ctx.fillStyle = isActive ? artwork.color : "rgba(255,255,255,0.66)";
    ctx.font = "800 15px system-ui";
    ctx.fillText(`${artwork.zoneId}  ·  ${artwork.command}`, startX + 14, startY + 25);
  });
}

function drawRoute() {
  const points = [...artworks.map(({ x, y }) => ({ x, y })), { x: 21 * tileSize, y: 7 * tileSize }];
  ctx.save();
  ctx.setLineDash([6, 8]);
  ctx.lineWidth = 2;
  ctx.strokeStyle = "rgba(242,189,66,0.24)";
  ctx.beginPath();
  points.forEach((point, index) => {
    if (index === 0) {
      ctx.moveTo(point.x, point.y);
    } else {
      ctx.lineTo(point.x, point.y);
    }
  });
  ctx.stroke();
  ctx.restore();
}

function drawQr(resource, x, y) {
  const image = preloadImage(resource.image);
  ctx.fillStyle = "#fff";
  ctx.fillRect(x - 2, y - 2, 30, 30);
  if (image.complete) {
    ctx.drawImage(image, x, y, 26, 26);
  }
}

function drawArtwork(artwork) {
  const image = preloadImage(artwork.image);
  const active = activeTarget?.id === artwork.id;
  const visited = visitedZones.has(artwork.command);
  const pulse = 1 + Math.sin(performance.now() / 190) * 0.08;

  if (active) {
    ctx.fillStyle = `${artwork.color}20`;
    ctx.beginPath();
    ctx.arc(artwork.x, artwork.y, 78 * pulse, 0, Math.PI * 2);
    ctx.fill();
    ctx.strokeStyle = artwork.color;
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.arc(artwork.x, artwork.y, 70 * pulse, 0, Math.PI * 2);
    ctx.stroke();
  }

  const frameX = artwork.x - 48;
  const frameY = artwork.y - 50;
  ctx.fillStyle = "#07090c";
  ctx.fillRect(frameX - 4, frameY - 4, 104, 73);
  ctx.strokeStyle = visited ? "#55d68b" : active ? artwork.color : "#59636f";
  ctx.lineWidth = active ? 3 : 2;
  ctx.strokeRect(frameX - 4, frameY - 4, 104, 73);

  if (image.complete) {
    ctx.save();
    ctx.beginPath();
    ctx.rect(frameX, frameY, 96, 65);
    ctx.clip();
    const scale = Math.max(96 / image.naturalWidth, 65 / image.naturalHeight);
    const width = image.naturalWidth * scale;
    const height = image.naturalHeight * scale;
    ctx.drawImage(image, frameX + (96 - width) / 2, frameY + (65 - height) / 2, width, height);
    ctx.restore();
  }

  ctx.fillStyle = "#11161b";
  ctx.fillRect(artwork.x - 31, artwork.y + 23, 62, 27);
  ctx.fillStyle = active ? artwork.color : "#75808c";
  ctx.fillRect(artwork.x - 35, artwork.y + 20, 70, 7);

  drawQr(artwork.resources[0], artwork.x - 45, artwork.y + 57);
  drawQr(artwork.resources[1], artwork.x + 19, artwork.y + 57);

  ctx.fillStyle = "#f5f7fa";
  ctx.font = "800 12px system-ui";
  ctx.textAlign = "center";
  ctx.fillText(artwork.title, artwork.x, artwork.y + 105);
  ctx.textAlign = "start";
}

function drawVrRoom() {
  const x = 20 * tileSize;
  const y = 2 * tileSize;
  const width = 3 * tileSize;
  const height = 10 * tileSize;
  const active = activeTarget?.id === "SALA_VR";

  ctx.fillStyle = active ? "rgba(34,197,195,0.14)" : "rgba(34,197,195,0.05)";
  ctx.fillRect(x, y, width, height);
  ctx.strokeStyle = active ? "#22c5c3" : "rgba(34,197,195,0.35)";
  ctx.lineWidth = active ? 3 : 1;
  ctx.strokeRect(x + 8, y + 8, width - 16, height - 16);

  const centerX = x + width / 2;
  const centerY = y + height / 2;
  const pulse = 1 + Math.sin(performance.now() / 220) * 0.08;
  ctx.strokeStyle = "rgba(34,197,195,0.7)";
  ctx.lineWidth = 4;
  ctx.beginPath();
  ctx.arc(centerX, centerY - 24, 34 * pulse, Math.PI, 0);
  ctx.stroke();
  ctx.fillStyle = "#102f32";
  ctx.fillRect(centerX - 40, centerY - 25, 80, 38);
  ctx.strokeStyle = "#22c5c3";
  ctx.strokeRect(centerX - 40, centerY - 25, 80, 38);
  ctx.fillStyle = "#22c5c3";
  ctx.fillRect(centerX - 27, centerY - 12, 18, 12);
  ctx.fillRect(centerX + 9, centerY - 12, 18, 12);

  ctx.fillStyle = "#dffcfb";
  ctx.textAlign = "center";
  ctx.font = "900 18px system-ui";
  ctx.fillText("SALA VR", centerX, centerY + 55);
  ctx.fillStyle = "#22c5c3";
  ctx.font = "800 13px system-ui";
  ctx.fillText("S4 · comando vr", centerX, centerY + 77);
  ctx.textAlign = "start";
}

function drawLabels() {
  ctx.fillStyle = "rgba(7,9,12,0.86)";
  ctx.fillRect(8 * tileSize, 8, 190, 32);
  ctx.strokeStyle = "rgba(242,189,66,0.35)";
  ctx.strokeRect(8 * tileSize, 8, 190, 32);
  ctx.fillStyle = "#f5f7fa";
  ctx.font = "900 16px system-ui";
  ctx.fillText("SALA 1 · 6 SECTORES", 8 * tileSize + 13, 30);

  ctx.fillStyle = "rgba(7,9,12,0.9)";
  ctx.fillRect(7.25 * tileSize, 14.08 * tileSize, 250, 28);
  ctx.strokeStyle = "rgba(77,163,255,0.45)";
  ctx.strokeRect(7.25 * tileSize, 14.08 * tileSize, 250, 28);
  ctx.fillStyle = "#f2bd42";
  ctx.font = "800 13px system-ui";
  ctx.fillText("ENTRADA PRINCIPAL · INICIO", 7.55 * tileSize, 14.48 * tileSize);
}

function drawPlayer() {
  const moving = keys.has("w") || keys.has("a") || keys.has("s") || keys.has("d") ||
    keys.has("arrowup") || keys.has("arrowdown") || keys.has("arrowleft") || keys.has("arrowright");
  const bob = moving ? Math.sin(performance.now() / 95) * 2 : 0;
  const angle = (player.heading * Math.PI) / 180;

  ctx.fillStyle = "rgba(77,163,255,0.18)";
  ctx.beginPath();
  ctx.arc(player.x, player.y + 10, 25, 0, Math.PI * 2);
  ctx.fill();

  ctx.save();
  ctx.translate(player.x, player.y + bob);
  ctx.rotate(angle);
  ctx.fillStyle = "#edf4fa";
  ctx.beginPath();
  ctx.arc(0, -10, 7, 0, Math.PI * 2);
  ctx.fill();
  ctx.fillStyle = "#207dbd";
  ctx.fillRect(-9, -2, 18, 22);
  ctx.fillStyle = "#64c9ff";
  ctx.fillRect(-6, 1, 12, 8);
  ctx.fillStyle = "#f2bd42";
  ctx.beginPath();
  ctx.moveTo(0, -27);
  ctx.lineTo(-7, -15);
  ctx.lineTo(7, -15);
  ctx.closePath();
  ctx.fill();
  ctx.restore();
}

function drawMuseum() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  for (let tileY = 0; tileY < rows; tileY += 1) {
    for (let tileX = 0; tileX < cols; tileX += 1) {
      const tileType = getTileType(tileX, tileY);
      if (tileType === "wall") {
        drawWall(tileX, tileY);
      } else if (tileType === "door") {
        drawDoor(tileX, tileY);
      } else {
        drawFloor(tileX, tileY);
      }
    }
  }

  drawSectorBoundaries();
  drawRoute();
  artworks.forEach(drawArtwork);
  drawVrRoom();
  drawLabels();
  drawPlayer();

  const vignette = ctx.createRadialGradient(
    canvas.width / 2,
    canvas.height / 2,
    220,
    canvas.width / 2,
    canvas.height / 2,
    760,
  );
  vignette.addColorStop(0, "rgba(0,0,0,0)");
  vignette.addColorStop(1, "rgba(0,0,0,0.36)");
  ctx.fillStyle = vignette;
  ctx.fillRect(0, 0, canvas.width, canvas.height);
}

function gameLoop(now) {
  const deltaSeconds = Math.min((now - lastFrameAt) / 1000, 0.035);
  lastFrameAt = now;
  updatePlayer(deltaSeconds);
  updatePhysicalState();
  drawMuseum();
  requestAnimationFrame(gameLoop);
}

window.addEventListener("keydown", (event) => {
  const target = event.target;
  const typing = target instanceof HTMLInputElement || target instanceof HTMLTextAreaElement;
  if (typing) {
    return;
  }

  const key = event.key.toLowerCase();
  keys.add(key);

  if (["arrowup", "arrowdown", "arrowleft", "arrowright", " "].includes(key)) {
    event.preventDefault();
  }

  if (!event.repeat && (key === " " || key === "enter")) {
    interact();
  }

  if (!event.repeat && key === "r") {
    resetTour();
  }
});

window.addEventListener("keyup", (event) => {
  keys.delete(event.key.toLowerCase());
});

canvas.addEventListener("pointerdown", () => canvas.focus());
ui.resetButton.addEventListener("click", resetTour);

document.querySelectorAll(".route-step").forEach((button) => {
  button.addEventListener("click", () => teleportTo(button.dataset.command));
});

ui.bridgeForm.addEventListener("submit", (event) => {
  event.preventDefault();
  startBridgePolling();
});

ui.bridgeUrl.value = localStorage.getItem("museiqBridgeUrl") || defaultBridgeUrl();
renderRoomOverview();
startBridgePolling();
canvas.focus();
const initialZone = new URLSearchParams(window.location.search).get("zone");
if (initialZone && ["1", "2", "3", "4", "5", "6", "vr"].includes(initialZone)) {
  teleportTo(initialZone);
}
requestAnimationFrame(gameLoop);
