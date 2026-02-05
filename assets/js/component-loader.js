/**
 * Component Loader
 * Dynamically loads header, nav, and footer components into pages
 */

(function () {
  "use strict";

  async function loadComponent(containerId, componentPath) {
    try {
      const container = document.getElementById(containerId);
      if (!container) {
        console.warn(`Container #${containerId} not found`);
        return;
      }

      const response = await fetch(componentPath);
      if (!response.ok) {
        throw new Error(`Failed to load ${componentPath}: ${response.status}`);
      }

      const html = await response.text();
      container.innerHTML = html;

      // Apply custom data attributes after loading (for per-page customization)
      applyCustomAttributes(container);

      console.log(`✓ Loaded ${componentPath}`);
    } catch (error) {
      console.error(`Error loading component ${componentPath}:`, error);
    }
  }

  function applyCustomAttributes(container) {
    // Custom logo image (data-logo attribute)
    const logoPath = container.dataset.logo;
    if (logoPath) {
      const logoImg = container.querySelector(".navbar-brand img");
      if (logoImg) {
        logoImg.src = logoPath;
        console.log(`✓ Applied custom logo: ${logoPath}`);
      }
    }

    // Custom subtitle image (data-subtitle attribute)
    const subtitlePath = container.dataset.subtitle;
    if (subtitlePath) {
      const subtitleImg = container.querySelector(".navbar-header span img");
      if (subtitleImg) {
        subtitleImg.src = subtitlePath;
        console.log(`✓ Applied custom subtitle: ${subtitlePath}`);
      }
    }

    // Custom title text (data-title attribute)
    const customTitle = container.dataset.title;
    if (customTitle) {
      const titleElement = container.querySelector(".navbar-brand");
      if (titleElement) {
        titleElement.setAttribute("title", customTitle);
      }
    }
  }

  // Load all components when DOM is ready
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initComponents);
  } else {
    initComponents();
  }

  function initComponents() {
    loadComponent("header-container", "/components/header.html");
    loadComponent("nav-container", "/components/nav.html");
    loadComponent("footer-container", "/components/footer.html");
  }
})();
