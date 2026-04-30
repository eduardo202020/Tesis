const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");

const visitedCounter = document.getElementById("visited-counter");
const roomName = document.getElementById("room-name");
const positionText = document.getElementById("position-text");
const directionText = document.getElementById("direction-text");
const hintText = document.getElementById("hint-text");
const artworkName = document.getElementById("artwork-name");
const artworkDescription = document.getElementById("artwork-description");
const scanRoom = document.getElementById("scan-room");
const scanNodes = document.getElementById("scan-nodes");
const scanRssi = document.getElementById("scan-rssi");
const occupancyStatus = document.getElementById("occupancy-status");
const lightingStatus = document.getElementById("lighting-status");
const brainStatus = document.getElementById("brain-status");
const docStatus = document.getElementById("doc-status");
const chatStatus = document.getElementById("chat-status");
const chatThread = document.getElementById("chat-thread");
const artImage = document.getElementById("art-image");
const artImageCaption = document.getElementById("art-image-caption");
const artImageRoom = document.getElementById("art-image-room");
const phonePrompt = document.getElementById("phone-prompt");
const voiceMode = document.getElementById("voice-mode");
const voiceState = document.getElementById("voice-state");
const voiceToggle = document.getElementById("voice-toggle");
const questionForm = document.getElementById("question-form");
const questionInput = document.getElementById("question-input");
const technicalToggle = document.getElementById("technical-toggle");
const compassNeedle = document.getElementById("compass-needle");
const museumCompassNeedle = document.getElementById("museum-compass-needle");
const headingText = document.getElementById("heading-text");
const museumHeadingText = document.getElementById("museum-heading-text");
const turnInstruction = document.getElementById("turn-instruction");

const tileSize = 48;
const cols = 20;
const rows = 12;
const wallHeight = 14;
const keys = new Set();

const museumMap = [
  "####################",
  "#........##........#",
  "#.A....A.##.A....A.#",
  "#........##........#",
  "#.A....A..D..A....A#",
  "#..................#",
  "#.A....A..D..A....A#",
  "#........##........#",
  "#.A....A.##.A....A.#",
  "#........##........#",
  "#........##........#",
  "####################",
];

const roomZones = [
  {
    name: "Sala 1 · Coleccion Moche",
    short: "Sala 1",
    x: 1,
    y: 1,
    w: 8,
    h: 10,
    summary: "Piezas funerarias y simbolicas vinculadas al universo Moche.",
    image: "src/imgs/sala-01-sipan.jpg",
  },
  {
    name: "Sala 2 · Coleccion Lambayeque",
    short: "Sala 2",
    x: 11,
    y: 1,
    w: 8,
    h: 10,
    summary: "Metalurgia, insignias y objetos ceremoniales del norte peruano.",
    image: "src/imgs/sala-02-naylamp.jpg",
  },
];

const decorativeTorches = [
  { x: 2, y: 2 },
  { x: 7, y: 2 },
  { x: 2, y: 8 },
  { x: 7, y: 8 },
  { x: 12, y: 2 },
  { x: 17, y: 2 },
  { x: 12, y: 8 },
  { x: 17, y: 8 },
];

const esp32Nodes = [
  { id: "ESP32-S1-A", room: "Sala 1", x: 2, y: 2 },
  { id: "ESP32-S1-B", room: "Sala 1", x: 7, y: 5 },
  { id: "ESP32-S1-C", room: "Sala 1", x: 3, y: 8 },
  { id: "ESP32-S2-A", room: "Sala 2", x: 12, y: 2 },
  { id: "ESP32-S2-B", room: "Sala 2", x: 17, y: 5 },
  { id: "ESP32-S2-C", room: "Sala 2", x: 13, y: 8 },
];

const raspberryPi = {
  id: "RPI-CORE-01",
  label: "Raspberry Pi 5",
  x: 10,
  y: 9,
  role: "Nodo central de consulta curatorial y orquestacion",
};

const artworkData = [
  {
    id: "S1-01",
    room: "Sala 1 · Coleccion Moche",
    title: "Huaco Ceremonial",
    description: "Pieza de ceramica asociada a rituales y memoria simbolica del valle.",
    narration: "Frente a ti tienes un huaco ceremonial. Observa su forma compacta y su lenguaje simbolico: resume creencias, jerarquia y practica ritual dentro del mundo Moche.",
    image: "src/imgs/sala-01-tumba.png",
  },
  {
    id: "S1-02",
    room: "Sala 1 · Coleccion Moche",
    title: "Mascara de Cobre",
    description: "Objeto funerario que resalta jerarquia, metalurgia y poder ritual.",
    narration: "Esta mascara de cobre dialoga con la idea de presencia y estatus. No solo protege o decora: construye una identidad visual asociada al poder funerario.",
    image: "src/imgs/sala-01-sipan.jpg",
  },
  {
    id: "S1-03",
    room: "Sala 1 · Coleccion Moche",
    title: "Orejeras del Senor",
    description: "Conjunto ornamental que comunica rango y refinamiento estetico.",
    narration: "Las orejeras amplifican la imagen del gobernante. Su tamaño y materialidad proyectan prestigio, autoridad y dominio tecnico sobre el metal.",
    image: "src/imgs/sala-01-arete.png",
  },
  {
    id: "S1-04",
    room: "Sala 1 · Coleccion Moche",
    title: "Textil de Aves",
    description: "Fragmento restaurado con iconografia zoomorfa y patrones repetitivos.",
    narration: "Este textil conserva ritmo visual e iconografia repetida. Funciona como soporte narrativo y como evidencia del trabajo especializado sobre fibras y color.",
    image: "src/imgs/sala-01-textil.jpg",
  },
  {
    id: "S1-05",
    room: "Sala 1 · Coleccion Moche",
    title: "Baston Ritual",
    description: "Elemento de autoridad utilizado en ceremonias de alto valor simbolico.",
    narration: "El baston ritual sintetiza mando y ceremonia. Es un objeto que ordena la escena politica, pero tambien transmite legitimidad frente a la comunidad.",
    image: "src/imgs/sala-01-baston.jpg",
  },
  {
    id: "S1-06",
    room: "Sala 1 · Coleccion Moche",
    title: "Pendiente Lunar",
    description: "Adorno de metal con referencias cosmologicas y estatus elite.",
    narration: "Este pendiente combina ornamentacion con cosmologia. La pieza sugiere que el cuerpo tambien era un soporte para expresar relacion con lo sagrado.",
    image: "src/imgs/sala-01-pendiente.webp",
  },
  {
    id: "S1-07",
    room: "Sala 1 · Coleccion Moche",
    title: "Escena de Caza",
    description: "Relieve narrativo que presenta accion, territorio y especializacion tecnica.",
    narration: "La escena de caza transforma un evento concreto en relato visual. Aqui se cruzan tecnica, territorio y una manera de representar el orden social.",
    image: "src/imgs/sala-01-caza.webp",
  },
  {
    id: "S1-08",
    room: "Sala 1 · Coleccion Moche",
    title: "Tumi de Exhibicion",
    description: "Pieza iconica que vincula practica ceremonial y representacion politica.",
    narration: "El tumi es una pieza de enorme carga iconica. Su presencia ayuda a entender como la forma ceremonial tambien comunica poder y centralidad politica.",
    image: "src/imgs/sala-01-joyas.png",
  },
  {
    id: "S2-01",
    room: "Sala 2 · Coleccion Lambayeque",
    title: "Corona Dorada",
    description: "Insignia ceremonial que enfatiza prestigio y refinamiento metalurgico.",
    narration: "Esta corona dorada concentra prestigio visual. El brillo, la escala y la composicion la convierten en un marcador directo de elite y ceremoniedad.",
    image: "src/imgs/sala-02-corona.webp",
  },
  {
    id: "S2-02",
    room: "Sala 2 · Coleccion Lambayeque",
    title: "Vaso de Ofrenda",
    description: "Recipiente asociado a contextos de ritual y redistribucion simbolica.",
    narration: "El vaso de ofrenda remite a practicas de intercambio ritual. Su valor esta tanto en lo que contiene como en la escena social que activa.",
    image: "src/imgs/sala-02-vaso.jpg",
  },
  {
    id: "S2-03",
    room: "Sala 2 · Coleccion Lambayeque",
    title: "Collar de Cuentas",
    description: "Pieza compuesta que sugiere redes de intercambio y valor suntuario.",
    narration: "El collar de cuentas hace visible una economia de materiales, desplazamientos y prestigio. Cada cuenta suma detalle y construye presencia.",
    image: "src/imgs/sala-02-collar.jpg",
  },
  {
    id: "S2-04",
    room: "Sala 2 · Coleccion Lambayeque",
    title: "Icono de Naylamp",
    description: "Representacion vinculada al relato fundacional y legitimidad cultural.",
    narration: "El icono de Naylamp no solo ilustra un personaje. Activa un relato fundacional y organiza una memoria politica dentro de la coleccion.",
    image: "src/imgs/sala-02-naylamp.jpg",
  },
  {
    id: "S2-05",
    room: "Sala 2 · Coleccion Lambayeque",
    title: "Placa de Tocado",
    description: "Elemento decorativo trabajado para acompanar vestimenta de elite.",
    narration: "Esta placa de tocado muestra como el vestido ceremonial era una arquitectura visual. Los detalles importan porque codifican jerarquia.",
    image: "src/imgs/sala-02-tocado.jpg",
  },
  {
    id: "S2-06",
    room: "Sala 2 · Coleccion Lambayeque",
    title: "Cuchillo Ornamental",
    description: "Objeto funcional y simbolico exhibido como muestra de maestria tecnica.",
    narration: "El cuchillo ornamental combina uso y simbolo. La precision del trabajo material transforma el objeto en una declaracion de maestria tecnica.",
    image: "src/imgs/sala-02-cuchillo.jpg",
  },
  {
    id: "S2-07",
    room: "Sala 2 · Coleccion Lambayeque",
    title: "Pectoral Solar",
    description: "Composicion metalica que destaca brillo, centralidad y visibilidad ritual.",
    narration: "El pectoral solar captura la relacion entre brillo, frontalidad y espectaculo ceremonial. Es una pieza pensada para ser vista y recordar autoridad.",
    image: "src/imgs/sala-02-pectoral.jpg",
  },
  {
    id: "S2-08",
    room: "Sala 2 · Coleccion Lambayeque",
    title: "Miniatura de Barca",
    description: "Interpretacion de movilidad, intercambio y cosmovision del litoral norte.",
    narration: "La miniatura de barca conecta movilidad y cosmovision costera. Aunque es una pieza pequena, abre una lectura amplia sobre intercambio y paisaje.",
    image: "src/imgs/sala-02-pectoral.jpg",
  },
];

const artworkSlots = [];
let artworkIndex = 0;

for (let y = 0; y < rows; y += 1) {
  for (let x = 0; x < cols; x += 1) {
    if (museumMap[y][x] === "A") {
      artworkSlots.push({
        ...artworkData[artworkIndex],
        tileX: x,
        tileY: y,
        visited: false,
      });
      artworkIndex += 1;
    }
  }
}

const player = {
  x: tileSize * 4,
  y: tileSize * 5.5,
  size: 17,
  speed: 2.55,
  facing: "down",
  heading: 180,
};

const routeWaypoints = [
  { x: 4, y: 2, label: "Inicio de Sala 1" },
  { x: 7, y: 2, label: "Primer corredor de Sala 1" },
  { x: 7, y: 8, label: "Cierre de Sala 1" },
  { x: 10, y: 5, label: "Paso al corredor central" },
  { x: 12, y: 2, label: "Ingreso a Sala 2" },
  { x: 17, y: 2, label: "Primer tramo de Sala 2" },
  { x: 17, y: 8, label: "Cierre de Sala 2" },
];

let lastGuideKey = "";
let activeArtworkId = null;
let voiceEnabled = true;
let currentUtterance = null;
let routeIndex = 0;
let pendingQuestion = null;
let signalAnimation = null;
let technicalViewEnabled = true;
let docQueryState = "inactivo";

const speechSupported = "speechSynthesis" in window && "SpeechSynthesisUtterance" in window;

function isWalkable(tileX, tileY) {
  if (tileX < 0 || tileY < 0 || tileX >= cols || tileY >= rows) {
    return false;
  }

  const tile = museumMap[tileY][tileX];
  return tile === "." || tile === "D";
}

function movePlayer(dx, dy) {
  const nextX = player.x + dx;
  const nextY = player.y + dy;
  const hitbox = player.size;

  const canMoveX = [
    [nextX - hitbox, player.y - hitbox],
    [nextX + hitbox, player.y - hitbox],
    [nextX - hitbox, player.y + hitbox],
    [nextX + hitbox, player.y + hitbox],
  ].every(([px, py]) => isWalkable(Math.floor(px / tileSize), Math.floor(py / tileSize)));

  if (canMoveX) {
    player.x = nextX;
  }

  const canMoveY = [
    [player.x - hitbox, nextY - hitbox],
    [player.x + hitbox, nextY - hitbox],
    [player.x - hitbox, nextY + hitbox],
    [player.x + hitbox, nextY + hitbox],
  ].every(([px, py]) => isWalkable(Math.floor(px / tileSize), Math.floor(py / tileSize)));

  if (canMoveY) {
    player.y = nextY;
  }
}

function updatePlayer() {
  let dx = 0;
  let dy = 0;

  if (keys.has("arrowleft") || keys.has("a")) {
    dx -= player.speed;
    player.heading = 270;
  }
  if (keys.has("arrowright") || keys.has("d")) {
    dx += player.speed;
    player.heading = 90;
  }
  if (keys.has("arrowup") || keys.has("w")) {
    dy -= player.speed;
    player.heading = 0;
  }
  if (keys.has("arrowdown") || keys.has("s")) {
    dy += player.speed;
    player.heading = 180;
  }

  if (dx !== 0 && dy !== 0) {
    const normalizer = Math.sqrt(2) / 2;
    dx *= normalizer;
    dy *= normalizer;
  }

  player.facing = getFacingFromHeading(player.heading);
  movePlayer(dx, dy);
  updateRouteProgress();
}

function getCurrentRoom() {
  const tileX = Math.floor(player.x / tileSize);
  const tileY = Math.floor(player.y / tileSize);

  return roomZones.find(
    (zone) =>
      tileX >= zone.x &&
      tileX < zone.x + zone.w &&
      tileY >= zone.y &&
      tileY < zone.y + zone.h
  ) || {
    name: "Pasillo de Conexion",
    short: "Pasillo",
    summary: "Zona de transicion entre las dos salas del museo.",
    image: "src/imgs/sala-01-sipan.jpg",
  };
}

function getNearbyArtwork() {
  return artworkSlots.find((art) => {
    const artX = art.tileX * tileSize + tileSize / 2;
    const artY = art.tileY * tileSize + tileSize / 2;
    return Math.hypot(player.x - artX, player.y - artY) < 64;
  }) || null;
}

function updateVisitedCount() {
  const visited = artworkSlots.filter((art) => art.visited).length;
  visitedCounter.textContent = `${visited}/16 obras vistas`;
}

function getScanReadings() {
  const readings = esp32Nodes.map((node) => {
    const nodeX = node.x * tileSize + tileSize / 2;
    const nodeY = node.y * tileSize + tileSize / 2;
    const distance = Math.hypot(player.x - nodeX, player.y - nodeY);
    const rssi = Math.max(-92, Math.round(-38 - distance / 5.8));
    return {
      ...node,
      distance,
      rssi,
      active: distance < 230,
    };
  }).sort((a, b) => a.distance - b.distance);

  return readings;
}

function getDetectedRoomFromNodes(readings) {
  const activeTop = readings.filter((node) => node.active).slice(0, 3);
  if (activeTop.length === 0) {
    return { room: "Sin deteccion estable", activeTop };
  }

  const counts = activeTop.reduce((acc, node) => {
    acc[node.room] = (acc[node.room] || 0) + 1;
    return acc;
  }, {});

  const room = Object.entries(counts).sort((a, b) => b[1] - a[1])[0][0];
  return { room, activeTop };
}

function getOccupancyState() {
  const room = getCurrentRoom();
  const occupiedRoom = room.short === "Sala 1" || room.short === "Sala 2" ? room.short : "Sin sala activa";
  const commandedNodes = esp32Nodes.filter((node) => node.room === occupiedRoom);
  return {
    occupiedRoom,
    commandedNodes,
    lightsOn: occupiedRoom !== "Sin sala activa",
  };
}

function normalizeAngle(angle) {
  const normalized = ((angle % 360) + 360) % 360;
  return normalized;
}

function getHeadingLabel(angle) {
  const normalized = normalizeAngle(angle);
  if (normalized >= 315 || normalized < 45) {
    return "Norte";
  }
  if (normalized >= 45 && normalized < 135) {
    return "Este";
  }
  if (normalized >= 135 && normalized < 225) {
    return "Sur";
  }
  return "Oeste";
}

function getFacingFromHeading(angle) {
  const normalized = normalizeAngle(angle);
  if (normalized >= 315 || normalized < 45) {
    return "up";
  }
  if (normalized >= 45 && normalized < 135) {
    return "right";
  }
  if (normalized >= 135 && normalized < 225) {
    return "down";
  }
  return "left";
}

function getCurrentWaypoint() {
  return routeWaypoints[Math.min(routeIndex, routeWaypoints.length - 1)];
}

function updateRouteProgress() {
  const waypoint = getCurrentWaypoint();
  const tileX = player.x / tileSize;
  const tileY = player.y / tileSize;
  const distance = Math.hypot(tileX - waypoint.x, tileY - waypoint.y);

  if (distance < 1.1 && routeIndex < routeWaypoints.length - 1) {
    routeIndex += 1;
  }
}

function getOrientationGuidance() {
  const waypoint = getCurrentWaypoint();
  const dx = waypoint.x * tileSize + tileSize / 2 - player.x;
  const dy = waypoint.y * tileSize + tileSize / 2 - player.y;
  const target = normalizeAngle((Math.atan2(dx, -dy) * 180) / Math.PI);
  const current = normalizeAngle(player.heading);
  let diff = normalizeAngle(target - current);
  if (diff > 180) {
    diff -= 360;
  }

  let action = "Sigue al frente";
  if (diff > 30 && diff < 150) {
    action = "Gira a la derecha";
  } else if (diff < -30 && diff > -150) {
    action = "Gira a la izquierda";
  } else if (Math.abs(diff) >= 150) {
    action = "Da media vuelta";
  }

  return {
    target,
    headingLabel: getHeadingLabel(current),
    targetLabel: getHeadingLabel(target),
    action,
    waypoint: waypoint.label,
  };
}

function updateCompass() {
  const guidance = getOrientationGuidance();
  compassNeedle.style.transform = `rotate(${player.heading}deg)`;
  museumCompassNeedle.style.transform = `rotate(${player.heading}deg)`;
  headingText.textContent = `Rumbo: ${guidance.headingLabel} ${Math.round(normalizeAngle(player.heading))}°`;
  museumHeadingText.textContent = `Museo orientado a ${guidance.targetLabel} · ${guidance.waypoint}`;
  turnInstruction.textContent = `${guidance.action} para seguir hacia ${guidance.waypoint}.`;
  directionText.textContent = `Orientacion: ${guidance.headingLabel} · Objetivo ${guidance.targetLabel}`;
  return guidance;
}

function updateTechnicalPanel() {
  if (!technicalViewEnabled) {
    scanRoom.textContent = "Sala detectada: oculto";
    scanNodes.textContent = "ESP32 activos: oculto";
    scanRssi.textContent = "Señal estimada: oculta";
    occupancyStatus.textContent = "Ocupacion: oculta";
    lightingStatus.textContent = "Iluminacion: oculta";
    brainStatus.textContent = "Raspberry Pi: oculto";
    docStatus.textContent = "Consulta documental: oculta";
    return;
  }

  const readings = getScanReadings();
  const detected = getDetectedRoomFromNodes(readings);
  const topNodes = detected.activeTop.length ? detected.activeTop : readings.slice(0, 3);
  const occupancy = getOccupancyState();

  scanRoom.textContent = `Sala detectada: ${detected.room}`;
  scanNodes.textContent = `ESP32 activos: ${topNodes.map((node) => node.id).join(", ")}`;
  scanRssi.textContent = `Señal estimada: ${topNodes.map((node) => `${node.id} ${node.rssi} dBm`).join(" · ")}`;
  occupancyStatus.textContent = `Ocupacion: celular reporta ${occupancy.occupiedRoom}`;
  lightingStatus.textContent = occupancy.lightsOn
    ? `Iluminacion: ${occupancy.occupiedRoom} encendida por orden del Raspberry Pi`
    : "Iluminacion: salas en espera, luces apagadas";
  brainStatus.textContent = occupancy.lightsOn
    ? `Raspberry Pi: recibe sala del celular y ordena encender ${occupancy.commandedNodes.map((node) => node.id).join(", ")}`
    : `Raspberry Pi: ${raspberryPi.label} en espera de ocupacion`;
  docStatus.textContent = `Consulta documental: ${docQueryState}`;
}

function stopSpeech() {
  if (!speechSupported) {
    return;
  }
  window.speechSynthesis.cancel();
  currentUtterance = null;
}

function speak(text) {
  if (!speechSupported || !voiceEnabled) {
    return;
  }

  stopSpeech();
  const utterance = new SpeechSynthesisUtterance(text);
  utterance.lang = "es-ES";
  utterance.rate = 1;
  utterance.pitch = 1.03;
  utterance.onstart = () => {
    voiceMode.textContent = "Narrando ahora";
    voiceState.textContent = "Voice live";
  };
  utterance.onend = () => {
    voiceMode.textContent = voiceEnabled ? "Narracion automatica" : "Voz silenciada";
    voiceState.textContent = voiceEnabled ? "Voice on" : "Voice off";
  };
  currentUtterance = utterance;
  window.speechSynthesis.speak(utterance);
}

function updatePhoneArtwork(image, title, room, subtitle) {
  artImage.src = image;
  artImage.alt = title;
  artImageCaption.textContent = title;
  artImageRoom.textContent = room;
}

function setGuideState(key, message, options = {}) {
  if (lastGuideKey === key) {
    return;
  }

  lastGuideKey = key;
  chatStatus.innerHTML = `
    <p class="chat-author">MuseIQ Voice</p>
    <p>${message}</p>
  `;
  phonePrompt.textContent = options.prompt || "Bot activo: escucha contextual y visual.";
  chatThread.scrollTop = chatThread.scrollHeight;

  if (options.image) {
    updatePhoneArtwork(options.image, options.title, options.room, options.subtitle);
  }

  if (options.speak) {
    speak(options.speak);
  }
}

function appendChatMessage(author, message, type) {
  const article = document.createElement("article");
  article.className = `chat-bubble ${type === "user" ? "chat-bubble-user" : "chat-bubble-bot"}`;
  article.innerHTML = `
    <p class="chat-author">${author}</p>
    <p>${message}</p>
  `;
  chatThread.appendChild(article);
  chatThread.scrollTop = chatThread.scrollHeight;
}

function getUserAnchor() {
  return { x: player.x, y: player.y - 10 };
}

function getRaspberryAnchor() {
  return {
    x: raspberryPi.x * tileSize + tileSize / 2,
    y: raspberryPi.y * tileSize + tileSize / 2,
  };
}

function startQuestionSignal(question, answer) {
  pendingQuestion = { question, answer };
  signalAnimation = {
    stage: "toPi",
    progress: 0,
    stageStartedAt: performance.now(),
  };
  phonePrompt.textContent = "Consulta enviada. Transmitiendo al Raspberry Pi...";
  voiceMode.textContent = "Enviando consulta";
  docQueryState = "esperando pregunta en el nodo central";
}

function finalizeQuestionSignal() {
  if (!pendingQuestion) {
    signalAnimation = null;
    return;
  }

  appendChatMessage("MuseIQ Voice", pendingQuestion.answer, "bot");
  phonePrompt.textContent = "Respuesta recibida desde el nodo curatorial.";
  if (voiceEnabled) {
    speak(pendingQuestion.answer);
  }
  docQueryState = "respuesta enviada al visitante";
  pendingQuestion = null;
  signalAnimation = null;
}

function updateSignalAnimation() {
  if (!signalAnimation) {
    return;
  }

  const now = performance.now();
  const elapsed = now - signalAnimation.stageStartedAt;

  if (signalAnimation.stage === "toPi") {
    signalAnimation.progress = Math.min(1, elapsed / 850);
    if (signalAnimation.progress >= 1) {
      signalAnimation.stage = "thinking";
      signalAnimation.progress = 0;
      signalAnimation.stageStartedAt = now;
      phonePrompt.textContent = "Raspberry Pi consultando documentos curatoriales...";
      voiceMode.textContent = "Buscando evidencia";
      docQueryState = "documentos de sala recuperados";
    }
    return;
  }

  if (signalAnimation.stage === "thinking") {
    signalAnimation.progress = Math.min(1, elapsed / 1500);
    if (signalAnimation.progress < 0.34) {
      docQueryState = "abriendo fichas curatoriales";
    } else if (signalAnimation.progress < 0.67) {
      docQueryState = "comparando coincidencias y contexto";
    } else {
      docQueryState = "seleccionando mejor respuesta";
    }
    if (signalAnimation.progress >= 1) {
      signalAnimation.stage = "toUser";
      signalAnimation.progress = 0;
      signalAnimation.stageStartedAt = now;
      phonePrompt.textContent = "Generando respuesta para el visitante...";
      voiceMode.textContent = "Devolviendo respuesta";
      docQueryState = "respuesta validada con material curatorial";
    }
    return;
  }

  if (signalAnimation.stage === "toUser") {
    signalAnimation.progress = Math.min(1, elapsed / 850);
    if (signalAnimation.progress >= 1) {
      finalizeQuestionSignal();
    }
  }
}

function answerQuestion(question) {
  const q = question.toLowerCase().trim();
  const room = getCurrentRoom();
  const nearby = getNearbyArtwork();
  const guidance = getOrientationGuidance();
  const readings = getScanReadings();
  const detected = getDetectedRoomFromNodes(readings);
  const visited = artworkSlots.filter((art) => art.visited).length;

  if (!q) {
    return "Puedes preguntarme por la sala actual, la obra cercana, el recorrido o la orientacion.";
  }

  if (q.includes("obra") || q.includes("pieza") || q.includes("cerca")) {
    if (nearby) {
      return `La obra mas cercana es ${nearby.title}. ${nearby.description} Si deseas una explicacion completa, presiona Espacio para activar la narracion.`;
    }
    return "En este momento no tienes una obra inmediatamente cerca. Avanza hacia un pedestal iluminado para consultar una pieza especifica.";
  }

  if (q.includes("sala") || q.includes("donde estoy") || q.includes("ubicacion")) {
    return `Estas en ${room.name}. ${room.summary}`;
  }

  if (q.includes("orient") || q.includes("brujula") || q.includes("rumbo")) {
    return `Tu orientacion actual es ${getHeadingLabel(player.heading)} con ${Math.round(normalizeAngle(player.heading))} grados. Para seguir el recorrido sugerido, ${guidance.action.toLowerCase()} hacia ${guidance.waypoint}.`;
  }

  if (q.includes("esp32") || q.includes("sensor") || q.includes("posicion") || q.includes("ubicando")) {
    const nodes = (detected.activeTop.length ? detected.activeTop : readings.slice(0, 3))
      .map((node) => `${node.id} (${node.rssi} dBm)`)
      .join(", ");
    return `La posicion se estima con tres ESP32 por sala. Ahora mismo el sistema detecta principalmente ${detected.room} usando ${nodes}. La app usa esta proximidad para inferir la sala y activar contenido contextual.`;
  }

  if (q.includes("raspberry") || q.includes("cerebro") || q.includes("curatorial") || q.includes("como respondes")) {
    return `El cerebro del sistema es una Raspberry Pi central. Recibe la pregunta del visitante, toma la sala estimada por los ESP32, consulta el material curatorial cargado para esa sala y devuelve una respuesta contextual mas precisa antes de que la app la narre.`;
  }

  if (q.includes("luz") || q.includes("luces") || q.includes("iluminacion") || q.includes("ocupacion")) {
    const occupancy = getOccupancyState();
    if (!occupancy.lightsOn) {
      return "En este momento no hay una sala activa. Cuando el celular reporta presencia dentro de una sala, el Raspberry Pi ordena a los tres ESP32 de esa sala que enciendan sus luces.";
    }
    return `Ahora mismo ${occupancy.occupiedRoom} esta ocupada. El celular comunica esa ubicacion al Raspberry Pi y este envia la orden a ${occupancy.commandedNodes.map((node) => node.id).join(", ")} para encender la iluminacion de la sala, mientras la otra sala permanece apagada.`;
  }

  if (q.includes("recorrido") || q.includes("seguir") || q.includes("ruta")) {
    return `Para mantener el recorrido en un solo sentido, ${guidance.action.toLowerCase()} y continua hacia ${guidance.waypoint}. Llevas ${visited} de 16 obras revisadas.`;
  }

  if (q.includes("cuantas") || q.includes("visitadas") || q.includes("vistas")) {
    return `Hasta ahora has revisado ${visited} de 16 obras del museo.`;
  }

  if (q.includes("museiq") || q.includes("app") || q.includes("bot")) {
    return "MuseIQ combina ubicacion por salas, orientacion asistida, apoyo visual en el celular y narracion contextual para mejorar la visita al museo.";
  }

  if (nearby) {
    return `Puedo ayudarte con la obra ${nearby.title}, con ${room.short} o con la orientacion del recorrido. Prueba preguntarme por la obra cercana o por donde seguir.`;
  }

  return `Puedo responder sobre la sala actual, la orientacion, el recorrido o la obra cercana. Ahora mismo estas en ${room.short}.`;
}

function submitQuestion(question) {
  const trimmed = question.trim();
  if (!trimmed) {
    return;
  }

  appendChatMessage("Visitante", trimmed, "user");
  const answer = answerQuestion(trimmed);
  startQuestionSignal(trimmed, answer);
}

function describeRoom(room) {
  if (room.short === "Sala 1") {
    return "Te encuentras en la Sala 1. Aqui predominan piezas asociadas al universo Moche, funerario y ceremonial.";
  }
  if (room.short === "Sala 2") {
    return "Has ingresado a la Sala 2. En esta zona destacan obras Lambayeque con fuerte presencia metalurgica y simbolica.";
  }
  return "Estas en el pasillo de conexion. Avanza hacia cualquiera de las salas para activar la narracion principal.";
}

function interact() {
  const nearby = getNearbyArtwork();
  if (!nearby) {
    hintText.textContent = "No hay una obra al alcance. Acercate un poco mas.";
    setGuideState("idle", "No detecto una obra cercana. Dirigete a un pedestal iluminado para activar la guia.", {
      prompt: "Sin obra en foco. Sigue explorando el museo.",
      image: getCurrentRoom().image,
      title: "Recorrido en curso",
      room: getCurrentRoom().short,
      subtitle: getCurrentRoom().summary,
      speak: "No detecto una obra cercana. Sigue avanzando hacia un pedestal para activar la guia.",
    });
    return;
  }

  nearby.visited = true;
  activeArtworkId = nearby.id;
  artworkName.textContent = `${nearby.id} · ${nearby.title}`;
  artworkDescription.textContent = nearby.description;
  hintText.textContent = `Narracion activada en ${nearby.room}. Continua el recorrido para explorar mas piezas.`;
  updateVisitedCount();

  setGuideState(`art-${nearby.id}`, nearby.narration, {
    prompt: `Narrando ${nearby.title}.`,
    image: nearby.image,
    title: nearby.title,
    room: nearby.room,
    subtitle: nearby.description,
    speak: nearby.narration,
  });
}

function updateHud() {
  const room = getCurrentRoom();
  const nearby = getNearbyArtwork();
  const guidance = updateCompass();
  updateTechnicalPanel();

  roomName.textContent = `Sala actual: ${room.name}`;
  positionText.textContent = `Posicion: (${Math.floor(player.x / tileSize)}, ${Math.floor(player.y / tileSize)})`;

  if (nearby) {
    artworkName.textContent = `${nearby.id} · ${nearby.title}`;
    artworkDescription.textContent = nearby.visited
      ? `${nearby.description} Ya fue narrada en la simulacion.`
      : `${nearby.description} Presiona Espacio para escuchar la narracion y ver la ficha visual.`;
    hintText.textContent = `Estas cerca de una obra. ${guidance.action} y luego activa la guia para mantener el recorrido en un solo sentido.`;

    if (activeArtworkId !== nearby.id) {
      setGuideState(`near-${nearby.id}`, `Estas frente a ${nearby.title}. ${guidance.action} si necesitas alinearte con el circuito; luego activa la guia para escuchar su relato y ver la obra en el dispositivo.`, {
        prompt: `Obra detectada: ${nearby.title}. Rumbo sugerido: ${guidance.action}.`,
        image: nearby.image,
        title: nearby.title,
        room: nearby.room,
        subtitle: nearby.description,
      });
    }
  } else {
    activeArtworkId = null;
    artworkName.textContent = "Ninguna";
    artworkDescription.textContent = "Explora las salas para activar fichas visuales y narradas.";
    hintText.textContent = `${guidance.action} para continuar el recorrido del museo en un mismo sentido.`;
    setGuideState(`room-${room.short}-${guidance.action}`, `${describeRoom(room)} ${guidance.action} para continuar hacia ${guidance.waypoint}.`, {
      prompt: `Recorrido actual en ${room.short}. ${guidance.action}.`,
      image: room.image,
      title: room.short,
      room: room.short,
      subtitle: room.summary,
    });
  }
}

function drawFloor(tileX, tileY) {
  const px = tileX * tileSize;
  const py = tileY * tileSize;
  const isCorridor = tileX === 9 || tileX === 10;
  const grad = ctx.createLinearGradient(px, py, px + tileSize, py + tileSize);

  grad.addColorStop(0, isCorridor ? "#5e4637" : "#6c4b36");
  grad.addColorStop(1, isCorridor ? "#35241b" : "#3c271c");
  ctx.fillStyle = grad;
  ctx.fillRect(px, py, tileSize, tileSize);

  ctx.strokeStyle = isCorridor ? "#7d5e4b" : "#8d6a51";
  ctx.strokeRect(px + 4, py + 4, tileSize - 8, tileSize - 8);

  ctx.strokeStyle = "rgba(255,232,182,0.08)";
  ctx.beginPath();
  ctx.moveTo(px + 6, py + 6);
  ctx.lineTo(px + tileSize - 6, py + tileSize - 6);
  ctx.stroke();

  ctx.fillStyle = "rgba(255, 188, 112, 0.06)";
  ctx.fillRect(px + 7, py + 7, tileSize - 14, 3);
}

function drawWall(tileX, tileY) {
  const px = tileX * tileSize;
  const py = tileY * tileSize;

  ctx.fillStyle = "#1b120f";
  ctx.fillRect(px, py, tileSize, tileSize);

  ctx.fillStyle = "#261815";
  ctx.fillRect(px + 4, py + 4, tileSize - 8, tileSize - 8);

  ctx.fillStyle = "#7a2f1d";
  ctx.fillRect(px + 5, py + 5, tileSize - 10, 5);

  ctx.fillStyle = "#0f0907";
  ctx.fillRect(px, py - wallHeight, tileSize, wallHeight);

  ctx.fillStyle = "#3d2017";
  ctx.fillRect(px + 4, py - wallHeight + 3, tileSize - 8, 4);

  ctx.fillStyle = "rgba(0, 0, 0, 0.28)";
  ctx.fillRect(px + tileSize - 5, py - wallHeight, 5, tileSize + wallHeight);
}

function drawDoor(tileX, tileY) {
  drawFloor(tileX, tileY);
  const px = tileX * tileSize;
  const py = tileY * tileSize;
  const grad = ctx.createLinearGradient(px, py, px + tileSize, py);

  grad.addColorStop(0, "#f0bb6f");
  grad.addColorStop(1, "#ffe8ae");
  ctx.fillStyle = grad;
  ctx.fillRect(px + 14, py + 4, 20, tileSize - 8);

  ctx.fillStyle = "rgba(255,245,220,0.5)";
  ctx.fillRect(px + 18, py + 8, 4, tileSize - 16);
}

function drawPedestal(art) {
  const px = art.tileX * tileSize + 7;
  const py = art.tileY * tileSize + 8;
  const w = tileSize - 14;
  const h = tileSize - 18;

  ctx.fillStyle = art.visited ? "rgba(255, 195, 103, 0.18)" : "rgba(255, 171, 74, 0.14)";
  ctx.beginPath();
  ctx.ellipse(px + w / 2, py + h - 2, 19, 11, 0, 0, Math.PI * 2);
  ctx.fill();

  ctx.fillStyle = "#4d3020";
  ctx.fillRect(px, py + 10, w, h - 14);
  ctx.fillStyle = "#7a5239";
  ctx.fillRect(px + 2, py + 7, w - 4, 8);
  ctx.fillStyle = "#332019";
  ctx.fillRect(px + 4, py + h - 10, w - 8, 8);

  const glass = ctx.createLinearGradient(px + 5, py + 2, px + w - 5, py + 12);
  glass.addColorStop(0, art.visited ? "rgba(255, 240, 210, 0.75)" : "rgba(255, 232, 192, 0.65)");
  glass.addColorStop(1, "rgba(255,255,255,0.18)");
  ctx.fillStyle = glass;
  ctx.fillRect(px + 5, py + 2, w - 10, 14);

  ctx.strokeStyle = art.visited ? "rgba(255, 210, 120, 0.85)" : "rgba(255, 196, 110, 0.7)";
  ctx.strokeRect(px + 5, py + 2, w - 10, 14);
  ctx.fillStyle = "rgba(255,255,255,0.35)";
  ctx.fillRect(px + 8, py + 4, w - 20, 3);
}

function drawTorch(torch) {
  const px = torch.x * tileSize + tileSize / 2;
  const py = torch.y * tileSize + tileSize / 2;
  const flicker = Math.sin(Date.now() / 130 + torch.x * 0.7 + torch.y * 0.4);

  ctx.fillStyle = "rgba(255, 155, 64, 0.12)";
  ctx.beginPath();
  ctx.ellipse(px, py + 5, 18 + flicker * 2, 10 + flicker * 1.2, 0, 0, Math.PI * 2);
  ctx.fill();

  ctx.fillStyle = "#3a2218";
  ctx.fillRect(px - 5, py + 6, 10, 8);

  ctx.fillStyle = "#ff9d2e";
  ctx.beginPath();
  ctx.moveTo(px, py - 10 - flicker * 2);
  ctx.quadraticCurveTo(px - 7, py - 1, px, py + 4);
  ctx.quadraticCurveTo(px + 7, py - 1, px, py - 10 - flicker * 2);
  ctx.fill();

  ctx.fillStyle = "#ffd86e";
  ctx.beginPath();
  ctx.moveTo(px, py - 6 - flicker);
  ctx.quadraticCurveTo(px - 4, py - 1, px, py + 2);
  ctx.quadraticCurveTo(px + 4, py - 1, px, py - 6 - flicker);
  ctx.fill();
}

function drawRaspberryPi() {
  if (!technicalViewEnabled) {
    return;
  }

  const x = raspberryPi.x * tileSize + tileSize / 2;
  const y = raspberryPi.y * tileSize + tileSize / 2;
  const pulse = 0.5 + (Math.sin(Date.now() / 240) + 1) / 2;

  ctx.fillStyle = `rgba(133, 255, 180, ${0.08 + pulse * 0.08})`;
  ctx.beginPath();
  ctx.ellipse(x, y + 6, 26, 14, 0, 0, Math.PI * 2);
  ctx.fill();

  ctx.fillStyle = "#2c8f51";
  ctx.fillRect(x - 20, y - 12, 40, 24);
  ctx.fillStyle = "#1f6038";
  ctx.fillRect(x - 16, y - 8, 32, 16);
  ctx.fillStyle = "#b9ffd1";
  ctx.fillRect(x - 10, y - 4, 8, 8);
  ctx.fillStyle = "#d2b06c";
  ctx.fillRect(x + 4, y - 6, 10, 4);
  ctx.fillRect(x + 4, y, 10, 4);

  ctx.strokeStyle = `rgba(133, 255, 180, ${0.2 + pulse * 0.3})`;
  ctx.lineWidth = 2;
  ctx.beginPath();
  ctx.arc(x, y, 34 + pulse * 4, 0, Math.PI * 2);
  ctx.stroke();
}

function drawRaspberryLinks() {
  if (!technicalViewEnabled) {
    return;
  }

  const occupancy = getOccupancyState();
  const nodes = occupancy.lightsOn ? occupancy.commandedNodes : [];
  const rx = raspberryPi.x * tileSize + tileSize / 2;
  const ry = raspberryPi.y * tileSize + tileSize / 2;

  nodes.forEach((node) => {
    const x = node.x * tileSize + tileSize / 2;
    const y = node.y * tileSize + tileSize / 2;
    ctx.strokeStyle = "rgba(255, 214, 122, 0.2)";
    ctx.lineWidth = 1.4;
    ctx.beginPath();
    ctx.moveTo(x, y);
    ctx.lineTo(rx, ry);
    ctx.stroke();
  });
}

function drawThinkingPulse() {
  if (!technicalViewEnabled || !signalAnimation || signalAnimation.stage !== "thinking") {
    return;
  }

  const { x, y } = getRaspberryAnchor();
  const pulse = 24 + Math.sin(performance.now() / 120) * 6;
  ctx.strokeStyle = "rgba(133, 255, 180, 0.28)";
  ctx.lineWidth = 3;
  ctx.beginPath();
  ctx.arc(x, y, pulse, 0, Math.PI * 2);
  ctx.stroke();

  ctx.strokeStyle = "rgba(255, 214, 122, 0.18)";
  ctx.beginPath();
  ctx.arc(x, y, pulse + 10, 0, Math.PI * 2);
  ctx.stroke();

  const docs = [
    { dx: -56, dy: -34, w: 22, h: 28 },
    { dx: 34, dy: -30, w: 20, h: 26 },
    { dx: -10, dy: 34, w: 24, h: 30 },
  ];

  docs.forEach((doc, index) => {
    const flicker = 0.4 + ((Math.sin(performance.now() / 180 + index) + 1) / 2) * 0.6;
    ctx.fillStyle = `rgba(226, 244, 255, ${0.45 * flicker})`;
    ctx.fillRect(x + doc.dx, y + doc.dy, doc.w, doc.h);
    ctx.strokeStyle = `rgba(133, 255, 180, ${0.25 * flicker})`;
    ctx.strokeRect(x + doc.dx, y + doc.dy, doc.w, doc.h);
    ctx.fillStyle = `rgba(133, 255, 180, ${0.35 * flicker})`;
    ctx.fillRect(x + doc.dx + 4, y + doc.dy + 6, doc.w - 8, 2);
    ctx.fillRect(x + doc.dx + 4, y + doc.dy + 12, doc.w - 8, 2);
    ctx.fillRect(x + doc.dx + 4, y + doc.dy + 18, doc.w - 12, 2);
  });
}

function drawSignalParticle(from, to, progress, color) {
  const x = from.x + (to.x - from.x) * progress;
  const y = from.y + (to.y - from.y) * progress;

  ctx.fillStyle = color;
  ctx.beginPath();
  ctx.arc(x, y, 7, 0, Math.PI * 2);
  ctx.fill();

  ctx.fillStyle = "rgba(255,255,255,0.65)";
  ctx.beginPath();
  ctx.arc(x, y, 3, 0, Math.PI * 2);
  ctx.fill();
}

function drawQuestionSignalFlow() {
  if (!technicalViewEnabled || !signalAnimation) {
    return;
  }

  const user = getUserAnchor();
  const pi = getRaspberryAnchor();

  ctx.setLineDash([8, 8]);
  ctx.lineWidth = 2;
  ctx.strokeStyle = "rgba(133, 255, 180, 0.18)";
  ctx.beginPath();
  ctx.moveTo(user.x, user.y);
  ctx.lineTo(pi.x, pi.y);
  ctx.stroke();
  ctx.setLineDash([]);

  if (signalAnimation.stage === "toPi") {
    drawSignalParticle(user, pi, signalAnimation.progress, "#7ff3ff");
    return;
  }

  if (signalAnimation.stage === "thinking") {
    drawThinkingPulse();
    return;
  }

  if (signalAnimation.stage === "toUser") {
    drawSignalParticle(pi, user, signalAnimation.progress, "#ffd87a");
  }
}

function drawEsp32Node(node) {
  if (!technicalViewEnabled) {
    return;
  }

  const x = node.x * tileSize + tileSize / 2;
  const y = node.y * tileSize + tileSize / 2;
  const pulse = (Date.now() / 16 + node.x * 15 + node.y * 10) % 120;
  const radius = 14 + pulse * 0.38;
  const readings = getScanReadings();
  const current = readings.find((entry) => entry.id === node.id);
  const active = current ? current.active : false;
  const occupancy = getOccupancyState();
  const powered = occupancy.occupiedRoom === node.room;

  if (active || powered) {
    ctx.strokeStyle = "rgba(112, 243, 255, 0.18)";
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.arc(x, y, radius, 0, Math.PI * 2);
    ctx.stroke();
  }

  ctx.fillStyle = powered ? "#ffd980" : active ? "#7ff3ff" : "#7a5d4d";
  ctx.fillRect(x - 8, y - 8, 16, 16);
  ctx.fillStyle = powered ? "#6f4b1f" : active ? "#1a4b55" : "#2a1913";
  ctx.fillRect(x - 5, y - 5, 10, 10);
  ctx.fillStyle = powered ? "#fff1b6" : active ? "#d7ffff" : "#cda889";
  ctx.fillRect(x - 2, y - 2, 4, 4);

  ctx.strokeStyle = powered
    ? "rgba(255, 214, 122, 0.52)"
    : active
      ? "rgba(127, 243, 255, 0.5)"
      : "rgba(180, 134, 95, 0.25)";
  ctx.beginPath();
  ctx.arc(x, y, 22, 0, Math.PI * 2);
  ctx.stroke();
}

function drawEsp32Links() {
  if (!technicalViewEnabled) {
    return;
  }

  const detected = getDetectedRoomFromNodes(getScanReadings());
  const nodes = detected.activeTop.length ? detected.activeTop : getScanReadings().slice(0, 3);

  nodes.forEach((node) => {
    const x = node.x * tileSize + tileSize / 2;
    const y = node.y * tileSize + tileSize / 2;
    ctx.strokeStyle = "rgba(127, 243, 255, 0.16)";
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.moveTo(x, y);
    ctx.lineTo(player.x, player.y);
    ctx.stroke();
  });
}

function drawWallShowcases() {
  const showcases = [
    { x: 2, y: 1 },
    { x: 5, y: 1 },
    { x: 12, y: 1 },
    { x: 15, y: 1 },
  ];

  showcases.forEach((item) => {
    const px = item.x * tileSize;
    const py = item.y * tileSize;

    ctx.fillStyle = "rgba(255, 208, 120, 0.18)";
    ctx.fillRect(px - 2, py + 4, tileSize * 2 + 4, 26);
    ctx.fillStyle = "#2d1a12";
    ctx.fillRect(px, py + 6, tileSize * 2, 22);
    ctx.strokeStyle = "rgba(255, 207, 122, 0.6)";
    ctx.strokeRect(px, py + 6, tileSize * 2, 22);
    ctx.fillStyle = "rgba(255,245,214,0.16)";
    ctx.fillRect(px + 4, py + 10, tileSize * 2 - 8, 5);
    });
  }

function drawRoomLighting() {
  const occupancy = getOccupancyState();

  ["Sala 1", "Sala 2"].forEach((roomShort) => {
    const zone = roomZones.find((room) => room.short === roomShort);
    if (!zone) {
      return;
    }

    const px = zone.x * tileSize;
    const py = zone.y * tileSize;
    const w = zone.w * tileSize;
    const h = zone.h * tileSize;

    if (occupancy.occupiedRoom === roomShort) {
      const glow = ctx.createRadialGradient(px + w / 2, py + h / 2, 40, px + w / 2, py + h / 2, Math.max(w, h) * 0.55);
      glow.addColorStop(0, "rgba(255, 214, 142, 0.22)");
      glow.addColorStop(1, "rgba(255, 214, 142, 0)");
      ctx.fillStyle = glow;
      ctx.fillRect(px, py, w, h);

      const edgeLight = ctx.createLinearGradient(px, py, px, py + 60);
      edgeLight.addColorStop(0, "rgba(255, 231, 178, 0.18)");
      edgeLight.addColorStop(1, "rgba(255, 231, 178, 0)");
      ctx.fillStyle = edgeLight;
      ctx.fillRect(px, py, w, h);
    } else {
      ctx.fillStyle = "rgba(0, 0, 0, 0.34)";
      ctx.fillRect(px, py, w, h);
    }
  });
}

function drawLabels() {
  ctx.fillStyle = "rgba(29, 15, 11, 0.76)";
  ctx.fillRect(52, 18, 250, 36);
  ctx.fillRect(604, 18, 250, 36);
  ctx.strokeStyle = "rgba(255, 196, 118, 0.38)";
  ctx.strokeRect(52, 18, 250, 36);
  ctx.strokeRect(604, 18, 250, 36);
  ctx.fillStyle = "#ffe8c6";
  ctx.font = '700 20px "Orbitron"';
  ctx.fillText("SALA 01", 86, 42);
  ctx.fillText("SALA 02", 638, 42);
}

function drawPlayer() {
  const isAdvancing = keys.has("arrowup") || keys.has("w") || keys.has("arrowdown") || keys.has("s");
  const bob = isAdvancing ? Math.sin(Date.now() / 180) * 1.6 : 0;
  const x = player.x;
  const y = player.y + bob;
  const radians = (player.heading * Math.PI) / 180;

  ctx.fillStyle = "rgba(72, 211, 255, 0.22)";
  ctx.beginPath();
  ctx.ellipse(x, y + 19, 18, 9, 0, 0, Math.PI * 2);
  ctx.fill();

  ctx.fillStyle = "rgba(255,255,255,0.18)";
  ctx.beginPath();
  ctx.arc(x, y + 2, 3, 0, Math.PI * 2);
  ctx.fill();

  ctx.save();
  ctx.translate(x, y);
  ctx.rotate(radians);

  ctx.fillStyle = "#0c1f33";
  ctx.fillRect(-2, -2, 4, 24);

  ctx.fillStyle = "#16263c";
  ctx.fillRect(-12, 6, 8, 12);
  ctx.fillRect(4, 6, 8, 12);

  ctx.fillStyle = "#1f3351";
  ctx.fillRect(-13, 3, 26, 14);

  ctx.fillStyle = "#2dd1ff";
  ctx.fillRect(-12, -4, 24, 15);

  ctx.fillStyle = "#7af3ff";
  ctx.fillRect(-8, -1, 16, 5);

  ctx.fillStyle = "#f0c8a2";
  ctx.fillRect(-7, -12, 14, 10);

  ctx.fillStyle = "#4a2f24";
  ctx.fillRect(-9, -17, 18, 7);

  ctx.fillStyle = "#a87dff";
  ctx.fillRect(-15, -1, 3, 12);
  ctx.fillRect(12, -1, 3, 12);

  ctx.fillStyle = "#e7f9ff";
  ctx.fillRect(-3, -8, 2, 2);
  ctx.fillRect(1, -8, 2, 2);

  ctx.fillStyle = "#0f6d87";
  ctx.fillRect(-4, -18, 8, 4);

  ctx.fillStyle = "#8effff";
  ctx.beginPath();
  ctx.moveTo(0, -23);
  ctx.lineTo(-4, -16);
  ctx.lineTo(4, -16);
  ctx.closePath();
  ctx.fill();

  ctx.fillStyle = "rgba(255,255,255,0.22)";
  ctx.beginPath();
  ctx.arc(0, 2, 2.2, 0, Math.PI * 2);
  ctx.fill();

  ctx.restore();
}

function drawAtmosphere() {
  const spotlight = ctx.createRadialGradient(player.x, player.y, 20, player.x, player.y, 210);
  spotlight.addColorStop(0, "rgba(255,225,180,0.12)");
  spotlight.addColorStop(1, "rgba(10,24,42,0)");
  ctx.fillStyle = spotlight;
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  const scan = ctx.createLinearGradient(0, 0, canvas.width, canvas.height);
  scan.addColorStop(0, "rgba(255,188,122,0.04)");
  scan.addColorStop(0.5, "rgba(255,255,255,0)");
  scan.addColorStop(1, "rgba(255,188,122,0.04)");
  ctx.fillStyle = scan;
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  ctx.fillStyle = "rgba(255,244,220,0.05)";
  for (let i = 0; i < 90; i += 1) {
    const x = (i * 67) % canvas.width;
    const y = (i * 43) % canvas.height;
    ctx.fillRect(x, y, 1, 1);
  }

  const vignette = ctx.createRadialGradient(canvas.width / 2, canvas.height / 2, 180, canvas.width / 2, canvas.height / 2, 520);
  vignette.addColorStop(0, "rgba(0,0,0,0)");
  vignette.addColorStop(1, "rgba(0,0,0,0.34)");
  ctx.fillStyle = vignette;
  ctx.fillRect(0, 0, canvas.width, canvas.height);
}

function drawMuseum() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  for (let y = 0; y < rows; y += 1) {
    for (let x = 0; x < cols; x += 1) {
      const tile = museumMap[y][x];
      if (tile === "#") {
        drawWall(x, y);
      } else if (tile === "D") {
        drawDoor(x, y);
      } else {
        drawFloor(x, y);
      }
    }
  }

  drawWallShowcases();
  drawRoomLighting();
  esp32Nodes.forEach(drawEsp32Node);
  drawEsp32Links();
  drawRaspberryLinks();
  drawRaspberryPi();
  drawQuestionSignalFlow();
  artworkSlots.forEach(drawPedestal);
  decorativeTorches.forEach(drawTorch);
  drawLabels();
  drawPlayer();
  drawAtmosphere();
}

function gameLoop() {
  updatePlayer();
  updateHud();
  updateSignalAnimation();
  drawMuseum();
  requestAnimationFrame(gameLoop);
}

voiceToggle.addEventListener("click", () => {
  voiceEnabled = !voiceEnabled;
  voiceToggle.textContent = voiceEnabled ? "Silenciar voz" : "Activar voz";
  voiceMode.textContent = voiceEnabled ? "Narracion automatica" : "Voz silenciada";
  voiceState.textContent = voiceEnabled ? "Voice on" : "Voice off";

  if (!voiceEnabled) {
    stopSpeech();
  } else {
    speak("Voz activada. MuseIQ puede narrar el recorrido nuevamente.");
  }
});

questionForm.addEventListener("submit", (event) => {
  event.preventDefault();
  submitQuestion(questionInput.value);
  questionInput.value = "";
  questionInput.focus();
});

technicalToggle.addEventListener("click", () => {
  technicalViewEnabled = !technicalViewEnabled;
  technicalToggle.textContent = technicalViewEnabled ? "Tecnico: visible" : "Tecnico: oculto";
  updateTechnicalPanel();
});

window.addEventListener("keydown", (event) => {
  const key = event.key.toLowerCase();
  const target = event.target;
  const isTypingField =
    target instanceof HTMLInputElement ||
    target instanceof HTMLTextAreaElement ||
    target instanceof HTMLSelectElement;

  if (isTypingField) {
    if (key === "enter" && target === questionInput) {
      return;
    }
    return;
  }

  keys.add(key);

  if (["arrowup", "arrowdown", "arrowleft", "arrowright", " "].includes(key)) {
    event.preventDefault();
  }

  if (key === " " || key === "enter") {
    interact();
  }
});

window.addEventListener("keyup", (event) => {
  keys.delete(event.key.toLowerCase());
});

window.addEventListener("beforeunload", stopSpeech);

if (!speechSupported) {
  voiceToggle.textContent = "Voz no disponible";
  voiceToggle.disabled = true;
  voiceMode.textContent = "Narracion en texto";
  voiceState.textContent = "No TTS";
}

updatePhoneArtwork("src/imgs/sala-01-sipan.jpg", "MuseIQ Tour", "Sala 1", "Recorre el museo y deja que el asistente te narre cada obra.");
updateVisitedCount();
updateHud();
gameLoop();
