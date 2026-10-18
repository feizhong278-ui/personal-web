/* =========================================================
   TRACE ARCHIVE — interactions
   No dependencies. Progressive enhancement.
   ========================================================= */
(() => {
  "use strict";

  const $ = (selector, scope = document) => scope.querySelector(selector);
  const $$ = (selector, scope = document) => Array.from(scope.querySelectorAll(selector));
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const finePointer = window.matchMedia("(hover: hover) and (pointer: fine)").matches;

  /* ---------- header progress ---------- */
  const header = $("[data-header]");
  const progress = $("[data-scroll-progress]");
  let ticking = false;

  const updateScroll = () => {
    const max = document.documentElement.scrollHeight - window.innerHeight;
    const value = max > 0 ? Math.min(100, (window.scrollY / max) * 100) : 0;
    if (progress) progress.style.setProperty("--progress", `${value}%`);
    if (header) header.classList.toggle("is-scrolled", window.scrollY > 12);
    ticking = false;
  };

  window.addEventListener("scroll", () => {
    if (!ticking) {
      window.requestAnimationFrame(updateScroll);
      ticking = true;
    }
  }, { passive: true });
  updateScroll();

  /* ---------- mobile menu ---------- */
  const menuButton = $("[data-menu-toggle]");
  const mobileMenu = $("[data-mobile-menu]");
  let lastFocused = null;

  const setMenu = (open) => {
    if (!menuButton || !mobileMenu) return;
    menuButton.setAttribute("aria-expanded", String(open));
    mobileMenu.classList.toggle("is-open", open);
    mobileMenu.setAttribute("aria-hidden", String(!open));
    document.body.classList.toggle("is-locked", open);
    if (open) {
      lastFocused = document.activeElement;
      const first = $("a", mobileMenu);
      if (first) window.setTimeout(() => first.focus(), 220);
    } else if (lastFocused) {
      lastFocused.focus();
    }
  };

  if (menuButton && mobileMenu) {
    menuButton.addEventListener("click", () => {
      setMenu(menuButton.getAttribute("aria-expanded") !== "true");
    });
    $$("a", mobileMenu).forEach((link) => link.addEventListener("click", () => setMenu(false)));
    mobileMenu.addEventListener("click", (event) => {
      if (event.target === mobileMenu) setMenu(false);
    });
    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape" && mobileMenu.classList.contains("is-open")) setMenu(false);
      if (event.key !== "Tab" || !mobileMenu.classList.contains("is-open")) return;
      const focusables = $$('a, button, [tabindex]:not([tabindex="-1"])', mobileMenu);
      if (!focusables.length) return;
      const first = focusables[0];
      const last = focusables[focusables.length - 1];
      if (event.shiftKey && document.activeElement === first) {
        event.preventDefault();
        last.focus();
      } else if (!event.shiftKey && document.activeElement === last) {
        event.preventDefault();
        first.focus();
      }
    });
  }

  /* ---------- reveal ---------- */
  if (!reducedMotion) {
    const revealTargets = $$(".section-head, .proof-head, .stat, .archive-card, .method-step, .method-quote, .about-teaser__copy, .about-portrait, .contact__bottom, .work-foot, .design-band__foot");
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-inview");
        observer.unobserve(entry.target);
      });
    }, { threshold: 0.08, rootMargin: "0px 0px -7% 0px" });
    revealTargets.forEach((element, index) => {
      element.classList.add("reveal");
      element.style.transitionDelay = `${Math.min(index % 4, 3) * 55}ms`;
      observer.observe(element);
    });
  }

  /* ---------- count up ---------- */
  const formatNumber = (number, decimals = 0) =>
    new Intl.NumberFormat("zh-CN", { minimumFractionDigits: decimals, maximumFractionDigits: decimals }).format(number);

  const animateCount = (element) => {
    const target = Number(element.dataset.count || 0);
    const decimals = Number(element.dataset.decimals || 0);
    if (reducedMotion) {
      element.textContent = formatNumber(target, decimals);
      return;
    }
    const duration = 1250;
    const start = performance.now();
    const tick = (now) => {
      const t = Math.min(1, (now - start) / duration);
      const eased = 1 - Math.pow(1 - t, 3);
      element.textContent = formatNumber(target * eased, decimals);
      if (t < 1) window.requestAnimationFrame(tick);
      else element.textContent = formatNumber(target, decimals);
    };
    window.requestAnimationFrame(tick);
  };

  const counters = $$(".count-value[data-count]");
  if (counters.length) {
    const countObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        animateCount(entry.target);
        countObserver.unobserve(entry.target);
      });
    }, { threshold: 0.7 });
    counters.forEach((counter) => countObserver.observe(counter));
  }

  /* ---------- hero deck tilt ---------- */
  const deck = $("[data-tilt]");
  if (deck && finePointer && !reducedMotion) {
    let frame = null;
    deck.addEventListener("pointermove", (event) => {
      if (frame) return;
      frame = window.requestAnimationFrame(() => {
        const rect = deck.getBoundingClientRect();
        const x = (event.clientX - rect.left) / rect.width - 0.5;
        const y = (event.clientY - rect.top) / rect.height - 0.5;
        deck.style.transform = `perspective(1200px) rotateX(${(-y * 5).toFixed(2)}deg) rotateY(${(x * 7).toFixed(2)}deg)`;
        frame = null;
      });
    });
    deck.addEventListener("pointerleave", () => {
      if (frame) window.cancelAnimationFrame(frame);
      frame = null;
      deck.style.transform = "perspective(1200px) rotateX(0deg) rotateY(0deg)";
    });
  }

  /* ---------- horizontal rail ---------- */
  $$("[data-rail]").forEach((rail) => {
    const section = rail.closest("section") || document;
    const prev = $("[data-rail-prev]", section);
    const next = $("[data-rail-next]", section);
    const bar = $("[data-rail-progress]", section);
    const card = $(".archive-card", rail);
    const step = () => card ? card.getBoundingClientRect().width + 20 : rail.clientWidth * 0.8;

    const sync = () => {
      const max = rail.scrollWidth - rail.clientWidth;
      const progress = max > 0 ? (rail.scrollLeft / max) : 0;
      if (bar) bar.style.width = `${20 + progress * 80}%`;
      if (prev) prev.disabled = rail.scrollLeft < 4;
      if (next) next.disabled = rail.scrollLeft > max - 4;
    };

    const scrollBy = (direction) => {
      rail.scrollBy({ left: step() * direction, behavior: reducedMotion ? "auto" : "smooth" });
    };

    if (next) next.addEventListener("click", () => scrollBy(1));
    if (prev) prev.addEventListener("click", () => scrollBy(-1));
    rail.addEventListener("scroll", sync, { passive: true });
    window.addEventListener("resize", sync, { passive: true });
    sync();

    if (finePointer) {
      let isDown = false;
      let startX = 0;
      let startScroll = 0;
      let moved = false;
      rail.addEventListener("pointerdown", (event) => {
        if (event.pointerType !== "mouse") return;
        isDown = true;
        moved = false;
        startX = event.clientX;
        startScroll = rail.scrollLeft;
      });
      rail.addEventListener("pointermove", (event) => {
        if (!isDown || event.pointerType !== "mouse") return;
        const dx = event.clientX - startX;
        if (Math.abs(dx) > 6) {
          moved = true;
          rail.classList.add("is-dragging");
          rail.scrollLeft = startScroll - dx;
          event.preventDefault();
        }
      });
      const stop = () => {
        if (!isDown) return;
        isDown = false;
        rail.classList.remove("is-dragging");
      };
      rail.addEventListener("pointerup", stop);
      rail.addEventListener("pointercancel", stop);
      rail.addEventListener("pointerleave", stop);
      rail.addEventListener("click", (event) => {
        if (moved) {
          event.preventDefault();
          event.stopPropagation();
          moved = false;
        }
      }, true);
      rail.addEventListener("keydown", (event) => {
        if (event.key === "ArrowRight") { event.preventDefault(); scrollBy(1); }
        if (event.key === "ArrowLeft") { event.preventDefault(); scrollBy(-1); }
      });
    }
  });

  /* ---------- tabs ---------- */
  $$("[data-tabs]").forEach((tabGroup) => {
    const tabs = $$('[role="tab"]', tabGroup);
    const panels = $$('[role="tabpanel"]', tabGroup);
    tabs.forEach((tab, index) => {
      tab.addEventListener("click", () => {
        tabs.forEach((item) => {
          item.setAttribute("aria-selected", String(item === tab));
          item.tabIndex = item === tab ? 0 : -1;
        });
        panels.forEach((panel) => {
          panel.hidden = panel.id !== tab.getAttribute("aria-controls");
        });
      });
      tab.addEventListener("keydown", (event) => {
        let nextIndex = null;
        if (event.key === "ArrowRight") nextIndex = (index + 1) % tabs.length;
        if (event.key === "ArrowLeft") nextIndex = (index - 1 + tabs.length) % tabs.length;
        if (event.key === "Home") nextIndex = 0;
        if (event.key === "End") nextIndex = tabs.length - 1;
        if (nextIndex === null) return;
        event.preventDefault();
        tabs[nextIndex].focus();
        tabs[nextIndex].click();
      });
    });
  });

  /* ---------- active case subnav ---------- */
  const caseLinks = $$("[data-case-link]");
  if (caseLinks.length) {
    const sections = caseLinks.map((link) => $(link.getAttribute("href"))).filter(Boolean);
    const caseObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        caseLinks.forEach((link) => {
          const active = link.getAttribute("href") === `#${entry.target.id}`;
          link.classList.toggle("is-active", active);
          if (active) link.setAttribute("aria-current", "true");
          else link.removeAttribute("aria-current");
        });
      });
    }, { rootMargin: "-22% 0px -62% 0px", threshold: 0 });
    sections.forEach((section) => caseObserver.observe(section));
  }

  /* ---------- lightbox ---------- */
  const dialog = $("[data-lightbox-dialog]");
  if (dialog) {
    const image = $("[data-lightbox-img]", dialog);
    const caption = $("[data-lightbox-caption]", dialog);
    const count = $("[data-lightbox-count]", dialog);
    const raw = $("[data-lightbox-raw]", dialog);
    const prev = $("[data-lightbox-prev]", dialog);
    const next = $("[data-lightbox-next]", dialog);
    const close = $("[data-lightbox-close]", dialog);
    const groups = {};
    let currentGroup = "";
    let currentIndex = 0;
    let returnFocus = null;

    $$("[data-lightbox-group]").forEach((trigger) => {
      const group = trigger.dataset.lightboxGroup;
      if (!groups[group]) groups[group] = [];
      groups[group].push(trigger);
    });

    const currentList = () => groups[currentGroup] || [];

    const setImage = (index) => {
      const list = currentList();
      if (!list.length) return;
      currentIndex = (index + list.length) % list.length;
      const trigger = list[currentIndex];
      const src = trigger.dataset.full || $("img", trigger)?.src;
      image.src = src;
      image.alt = trigger.dataset.alt || "";
      if (trigger.dataset.w) image.width = trigger.dataset.w;
      else image.removeAttribute("width");
      if (trigger.dataset.h) image.height = trigger.dataset.h;
      else image.removeAttribute("height");
      caption.textContent = trigger.dataset.caption || "";
      count.textContent = `${String(currentIndex + 1).padStart(2, "0")} / ${String(list.length).padStart(2, "0")}`;
      if (raw) raw.href = src;
      const nextTrigger = list[(currentIndex + 1) % list.length];
      const nextSrc = nextTrigger?.dataset.full || $( "img", nextTrigger )?.src;
      if (nextSrc) {
        const preload = new Image();
        preload.src = nextSrc;
      }
    };

    const openLightbox = (group, index, trigger) => {
      if (!groups[group] || !groups[group].length) return;
      currentGroup = group;
      returnFocus = trigger || document.activeElement;
      setImage(index);
      document.body.classList.add("is-locked");
      if (typeof dialog.showModal === "function") dialog.showModal();
      else dialog.setAttribute("open", "");
      window.setTimeout(() => close?.focus(), 30);
    };

    const closeLightbox = () => {
      document.body.classList.remove("is-locked");
      if (typeof dialog.close === "function") dialog.close();
      else dialog.removeAttribute("open");
      if (returnFocus) returnFocus.focus();
    };

    $$("[data-lightbox-group], [data-open-group]").forEach((trigger) => {
      trigger.addEventListener("click", () => {
        if (trigger.dataset.openGroup) {
          openLightbox(trigger.dataset.openGroup, Number(trigger.dataset.openIndex || 0), trigger);
        } else if (trigger.dataset.lightboxGroup) {
          const group = trigger.dataset.lightboxGroup;
          const index = groups[group].indexOf(trigger);
          openLightbox(group, index, trigger);
        }
      });
    });

    if (close) close.addEventListener("click", closeLightbox);
    if (prev) prev.addEventListener("click", () => setImage(currentIndex - 1));
    if (next) next.addEventListener("click", () => setImage(currentIndex + 1));
    dialog.addEventListener("click", (event) => {
      if (event.target === dialog) closeLightbox();
    });
    dialog.addEventListener("keydown", (event) => {
      if (event.key === "ArrowLeft") { event.preventDefault(); setImage(currentIndex - 1); }
      if (event.key === "ArrowRight") { event.preventDefault(); setImage(currentIndex + 1); }
    });
    dialog.addEventListener("close", () => document.body.classList.remove("is-locked"));

    let touchStart = null;
    const stage = $("[data-lightbox-stage]", dialog);
    if (stage) {
      stage.addEventListener("pointerdown", (event) => {
        if (event.pointerType === "mouse") return;
        touchStart = { x: event.clientX, y: event.clientY };
      });
      stage.addEventListener("pointerup", (event) => {
        if (!touchStart || event.pointerType === "mouse") return;
        const dx = event.clientX - touchStart.x;
        const dy = event.clientY - touchStart.y;
        if (Math.abs(dx) > 45 && Math.abs(dx) > Math.abs(dy)) {
          if (dx > 0) setImage(currentIndex - 1);
          else setImage(currentIndex + 1);
        }
        touchStart = null;
      });
    }
  }

  /* ---------- copy email ---------- */
  const copyButtons = $$("[data-copy-email]");
  const toast = $("[data-toast]");
  let toastTimer = null;
  const showToast = (message) => {
    if (!toast) return;
    toast.textContent = message;
    toast.classList.add("is-visible");
    window.clearTimeout(toastTimer);
    toastTimer = window.setTimeout(() => toast.classList.remove("is-visible"), 2200);
  };

  copyButtons.forEach((button) => {
    button.addEventListener("click", async () => {
      const email = button.dataset.copyEmail;
      const original = button.querySelector(".email-copy__action");
      try {
        await navigator.clipboard.writeText(email);
      } catch {
        const input = document.createElement("textarea");
        input.value = email;
        input.style.position = "fixed";
        input.style.opacity = "0";
        document.body.appendChild(input);
        input.select();
        document.execCommand("copy");
        input.remove();
      }
      if (original) {
        const label = original.textContent;
        original.textContent = "已复制 ✓";
        window.setTimeout(() => { original.textContent = label; }, 1800);
      }
      showToast(`邮箱已复制：${email}`);
    });
  });

  /* ---------- custom cursor ---------- */
  const cursor = $("[data-cursor]");
  const cursorLabel = $("[data-cursor-label]");
  if (cursor && cursorLabel && finePointer && !reducedMotion) {
    let pointerX = 0;
    let pointerY = 0;
    let currentX = 0;
    let currentY = 0;
    let visible = false;
    let raf = null;

    const loop = () => {
      currentX += (pointerX - currentX) * 0.18;
      currentY += (pointerY - currentY) * 0.18;
      cursor.style.left = `${currentX}px`;
      cursor.style.top = `${currentY}px`;
      raf = window.requestAnimationFrame(loop);
    };

    window.addEventListener("pointermove", (event) => {
      pointerX = event.clientX;
      pointerY = event.clientY;
      if (!visible) {
        visible = true;
        cursor.classList.add("is-visible");
        currentX = pointerX;
        currentY = pointerY;
        if (!raf) loop();
      }
    }, { passive: true });
    document.addEventListener("mouseleave", () => {
      visible = false;
      cursor.classList.remove("is-visible");
      if (raf) window.cancelAnimationFrame(raf);
      raf = null;
    });
    document.addEventListener("mouseenter", () => {
      if (!raf) loop();
    });
    $$("[data-cursor]").forEach((target) => {
      target.addEventListener("mouseenter", () => {
        cursorLabel.textContent = target.dataset.cursor || "VIEW";
        cursor.classList.add("is-hover");
      });
      target.addEventListener("mouseleave", () => {
        cursor.classList.remove("is-hover");
        cursorLabel.textContent = "";
      });
    });
  }

  /* ---------- time + year ---------- */
  const time = $("[data-local-time]");
  if (time) {
    const renderTime = () => {
      const text = new Intl.DateTimeFormat("zh-CN", {
        timeZone: "Asia/Shanghai", hour: "2-digit", minute: "2-digit", hour12: false,
      }).format(new Date());
      time.textContent = text;
    };
    renderTime();
    window.setInterval(renderTime, 60000);
  }
  $$("[data-year]").forEach((element) => { element.textContent = String(new Date().getFullYear()); });
})();
