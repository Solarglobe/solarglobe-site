document.documentElement.classList.add("js-enabled");

document.addEventListener("DOMContentLoaded", function () {
  (function loadSgPsReveal() {
    if (document.querySelector("script[data-sg-ps-reveal]")) return;
    var s = document.createElement("script");
    s.src = "/assets/js/sg-ps-reveal.js";
    s.async = true;
    s.setAttribute("data-sg-ps-reveal", "1");
    document.head.appendChild(s);
  })();

  const placeholder = document.getElementById("header-placeholder");
  if (!placeholder) return;

  const headerPath = window.location.origin + "/components/header.html";
  console.log("Solarglobe header loading:", headerPath);
  fetch(headerPath)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Header fetch failed: " + response.status);
      }
      return response.text();
    })
    .then((html) => {
      placeholder.innerHTML = html;
      console.log("Solarglobe header injected");
      initHeaderComponents();
      setActiveNav();
    })
    .catch((error) => {
      console.error("Header load error:", error);
    });
});

function initHeaderComponents() {
  const btn = document.getElementById("mobile-menu-button");
  const menu = document.getElementById("mobile-menu");
  const overlay = document.getElementById("mobile-overlay");

  console.log("Solarglobe header init", {
    btn: !!btn,
    menu: !!menu,
    overlay: !!overlay
  });

  if (!btn) {
    console.error("Solarglobe header error: mobile-menu-button missing");
    return;
  }
  if (!menu) {
    console.error("Solarglobe header error: mobile-menu missing");
    return;
  }
  if (!overlay) {
    console.error("Solarglobe header error: mobile-overlay missing");
    return;
  }

  const closeMenu = () => {
    menu.classList.remove("open");
    overlay.classList.remove("open");
    document.body.classList.remove("menu-open");
  };

  const openMenu = () => {
    menu.classList.add("open");
    overlay.classList.add("open");
    document.body.classList.add("menu-open");
  };

  const toggleMenu = () => {
    if (menu.classList.contains("open")) closeMenu();
    else openMenu();
  };

  btn.addEventListener("click", toggleMenu);
  overlay.addEventListener("click", closeMenu);

  // Accordions mobile
  const accordions = [
    { trigger: "mobile-solaire-trigger", content: "mobile-solaire-submenu" },
    { trigger: "mobile-methode-trigger", content: "mobile-methode-submenu" },
    { trigger: "mobile-produits-trigger", content: "mobile-produits-submenu" }
  ];
  accordions.forEach(function (item) {
    const trigger = document.getElementById(item.trigger);
    const content = document.getElementById(item.content);
    if (trigger && content) {
      trigger.addEventListener("click", function () {
        const isOpen = trigger.getAttribute("aria-expanded") === "true";
        trigger.setAttribute("aria-expanded", !isOpen);
        content.classList.toggle("open", !isOpen);
      });
    }
  });
}

function setActiveNav() {
  const path = window.location.pathname.replace(/\/$/, "") || "/";
  const pathNorm = path === "" ? "/" : path;

  const isActive = (href) => {
    const h = href.replace(/\/$/, "") || "/";
    if (h === "/") return pathNorm === "/" || pathNorm === "/index.html";
    return pathNorm === h || pathNorm.startsWith(h + "/");
  };

  const desktopLinks = document.querySelectorAll("#solarglobe-header .header-menu a");
  const mobileLinks = document.querySelectorAll("#solarglobe-header .mobile-menu a:not(.mobile-cta)");

  desktopLinks.forEach((a) => {
    const href = new URL(a.href).pathname;
    if (isActive(href)) a.classList.add("nav-active");
  });
  mobileLinks.forEach((a) => {
    const href = new URL(a.href).pathname;
    if (isActive(href)) a.classList.add("nav-active");
  });
}
