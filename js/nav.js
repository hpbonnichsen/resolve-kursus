/* Sidepanelets folde-tilstand.
   Tilstanden bor på <html data-nav>, så CSS kan style både panelet og
   indholdet ved siden af. Den læses tilbage inline i <head>, så et udfoldet
   panel ikke blinker sammenfoldet ved indlæsning. Uden JavaScript står
   panelet sammenfoldet og alle links virker stadig. */
(function () {
  "use strict";

  var root = document.documentElement;
  var btn = document.getElementById("nav-toggle");
  if (!btn) return;

  var KEY = "resolve-nav";
  var mqNarrow = matchMedia("(max-width: 900px)");

  function isOpen() {
    return root.dataset.nav === "open";
  }

  function set(open, remember) {
    root.dataset.nav = open ? "open" : "closed";
    btn.setAttribute("aria-expanded", String(open));
    if (remember) {
      try { localStorage.setItem(KEY, open ? "open" : "closed"); } catch (e) {}
    }
  }

  set(isOpen(), false);

  btn.addEventListener("click", function () {
    set(!isOpen(), true);
  });

  /* På smalle skærme lægger panelet sig over indholdet. Så skal et klik på et
     link lukke det igen, ellers dækker det målet man lige sprang til. */
  document.getElementById("side-body").addEventListener("click", function (e) {
    if (e.target.closest("a") && mqNarrow.matches) set(false, false);
  });

  /* Escape lukker et panel der ligger oven på indholdet. */
  addEventListener("keydown", function (e) {
    if (e.key === "Escape" && isOpen() && mqNarrow.matches) {
      set(false, false);
      btn.focus();
    }
  });
})();
