// Formulario público de intenciones de oración (sección Intercesión).
// Envía directo a Firestore del Portal RCC Paterson (proyecto
// rcc-paterson-portal, colección "intercesion_intenciones") con
// origen:"publico" y estado:"pendiente" — el equipo de Intercesión lo
// revisa desde el portal antes de sumarlo a la cadena de oración. No
// requiere iniciar sesión ni tener cuenta en el portal.
//
// Nota: firestore.rules del portal exige que este documento traiga
// EXACTAMENTE estas claves (texto, porQuien, pedidoPor, origen, estado,
// creadoPorUid, createdAt) — si se agrega o quita un campo aquí, hay que
// actualizar también esIntencionPublicaValida() en ese archivo.
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.13.0/firebase-app.js";
import { getFirestore, collection, addDoc, serverTimestamp } from "https://www.gstatic.com/firebasejs/10.13.0/firebase-firestore.js";

const firebaseConfig = {
  apiKey: "AIzaSyAm94nr-0euL6N_zhQGVndY38nOPz_RG9g",
  authDomain: "rcc-paterson-portal.firebaseapp.com",
  projectId: "rcc-paterson-portal",
  storageBucket: "rcc-paterson-portal.firebasestorage.app",
  messagingSenderId: "43601775811",
  appId: "1:43601775811:web:abe2d9ed74baddb7bca676"
};

const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

const form = document.getElementById("intRequestForm");

if (form) {
  const msgEl = document.getElementById("reqMsg");
  const btn = document.getElementById("reqSubmitBtn");
  const successEl = document.getElementById("reqSuccess");
  const BTN_LABEL = btn.textContent;

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    msgEl.textContent = "";

    const texto = document.getElementById("reqTexto").value.trim();
    const porQuien = document.getElementById("reqPorQuien").value.trim();
    const pedidoPor = document.getElementById("reqPedidoPor").value.trim();

    if (!texto) {
      msgEl.textContent = "Escribe tu intención de oración antes de enviar.";
      return;
    }
    if (texto.length >= 1900) {
      msgEl.textContent = "Tu intención es muy larga — acórtala un poco, por favor.";
      return;
    }

    btn.disabled = true;
    btn.textContent = "Enviando…";

    try {
      await addDoc(collection(db, "intercesion_intenciones"), {
        texto,
        porQuien,
        pedidoPor,
        origen: "publico",
        estado: "pendiente",
        creadoPorUid: null,
        createdAt: serverTimestamp()
      });

      form.classList.add("hidden");
      successEl.classList.remove("hidden");
    } catch (err) {
      console.error(err);
      msgEl.textContent = "No se pudo enviar tu intención. Intenta de nuevo en un momento.";
      btn.disabled = false;
      btn.textContent = BTN_LABEL;
    }
  });
}
