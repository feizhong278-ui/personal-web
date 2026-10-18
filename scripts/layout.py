# -*- coding: utf-8 -*-
import json
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = json.loads((ROOT / "assets/img-manifest.json").read_text())
SITE_URL = "https://feizhong278-ui.github.io/personal-web/"

NAV_ITEMS = [
    ("index.html", "首页", "home"),
    ("operations.html", "运营案例", "operations"),
    ("design.html", "设计作品", "design"),
    ("about.html", "关于我", "about"),
]


def dims(src):
    if src not in MANIFEST:
        raise KeyError(f"Missing image in manifest: {src}")
    data = MANIFEST[src]
    inline = {k: v for k, v in data.items() if k in ("w", "h", "bytes")}
    return inline


def image(src, alt, base="", cls="", loading="lazy", fetchpriority=None, sizes=None,
          width=None, height=None, extra=""):
    d = dims(src)
    w = width or d.get("w")
    h = height or d.get("h")
    attrs = [
        f'src="{base}{escape(src)}"',
        f'alt="{escape(alt, quote=True)}"',
        f'width="{w}"', f'height="{h}"',
    ]
    if cls:
        attrs.append(f'class="{cls}"')
    if loading:
        attrs.append(f'loading="{loading}"')
    if fetchpriority:
        attrs.append(f'fetchpriority="{fetchpriority}"')
    if sizes:
        attrs.append(f'sizes="{escape(sizes, quote=True)}"')
    attrs.append('decoding="async"')
    if extra:
        attrs.append(extra)
    return f'<img {" ".join(attrs)}>'


def design_picture(project, n, alt, base="", sizes="(max-width: 900px) 100vw, 1400px",
                   loading="lazy", cls="", fetchpriority=None):
    board = next(b for b in project["_board_data"] if b["n"] == n)
    variants = board["variants"]
    widths = sorted(int(w) for w in variants)
    default_w = 1600 if 1600 in widths else max(widths)
    src = base + variants[str(default_w)]
    srcset = ", ".join(f'{base}{variants[str(w)]} {w}w' for w in widths)
    d = dims(variants[str(default_w)])
    attrs = [
        f'src="{src}"', f'srcset="{srcset}"', f'sizes="{escape(sizes, quote=True)}"',
        f'alt="{escape(alt, quote=True)}"', f'width="{d["w"]}"', f'height="{d["h"]}"',
        'decoding="async"',
    ]
    if cls:
        attrs.append(f'class="{cls}"')
    if loading:
        attrs.append(f'loading="{loading}"')
    if fetchpriority:
        attrs.append(f'fetchpriority="{fetchpriority}"')
    return f'<img {" ".join(attrs)}>'


def lightbox_button(inner, group, full, caption, alt, base="", cls="media-open", w=None, h=None,
                    open_group=None, open_index=None, extra=""):
    attrs = [
        f'data-lightbox-group="{group}"',
        f'data-full="{base}{full}"',
        f'data-caption="{escape(caption, quote=True)}"',
        f'data-alt="{escape(alt, quote=True)}"',
    ]
    if w:
        attrs.append(f'data-w="{w}"')
    if h:
        attrs.append(f'data-h="{h}"')
    if open_group:
        attrs.append(f'data-open-group="{open_group}"')
    if open_index is not None:
        attrs.append(f'data-open-index="{open_index}"')
    if extra:
        attrs.append(extra)
    return f'<button class="{cls}" type="button" {" ".join(attrs)}>{inner}</button>'


def header(active, base=""):
    nav = []
    for href, label, key in NAV_ITEMS:
        current = ' aria-current="page"' if key == active else ""
        nav.append(f'<a href="{base}{href}"{current}>{label}</a>')
    nav_html = "\n          ".join(nav)
    return f'''
  <header class="site-header" data-header>
    <div class="container header-inner">
      <a class="brand" href="{base}index.html" aria-label="钟菲作品集首页">
        <span class="brand-mark">ZF</span>
        <span class="brand-type"><strong>钟菲</strong><small>ZHONG FEI / PORTFOLIO</small></span>
      </a>
      <nav class="desktop-nav" aria-label="主导航">
          {nav_html}
      </nav>
      <div class="header-tools">
        <span class="availability"><i aria-hidden="true"></i> OPEN TO WORK</span>
        <a class="resume-link" href="{base}assets/docs/zhongfei-resume.pdf" download>简历 <span aria-hidden="true">↓</span></a>
        <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="mobile-menu" data-menu-toggle>
          <span class="menu-toggle__label">菜单</span>
          <span class="menu-toggle__lines" aria-hidden="true"><i></i><i></i></span>
        </button>
      </div>
    </div>
    <div class="scroll-progress" data-scroll-progress aria-hidden="true"></div>
  </header>
  <div class="mobile-menu" id="mobile-menu" data-mobile-menu aria-hidden="true">
    <div class="mobile-menu__inner">
      <p class="mobile-menu__kicker">INDEX / 2027</p>
      <nav class="mobile-nav" aria-label="移动端主导航">
        <a href="{base}index.html"><span>01</span>首页</a>
        <a href="{base}operations.html"><span>02</span>运营案例</a>
        <a href="{base}design.html"><span>03</span>设计作品</a>
        <a href="{base}about.html"><span>04</span>关于我</a>
      </nav>
      <div class="mobile-menu__foot">
        <a href="mailto:Aria.zhong@outlook.com">Aria.zhong@outlook.com</a>
        <a href="{base}assets/docs/zhongfei-resume.pdf" download>下载简历 PDF ↓</a>
        <p>杭州 · 2027 届 · 可接受江浙沪机会</p>
      </div>
    </div>
  </div>'''


def footer(base=""):
    return f'''
  <footer class="site-footer">
    <div class="container">
      <div class="footer-main">
        <a class="footer-brand" href="{base}index.html" aria-label="回到首页">
          <span class="brand-mark">ZF</span>
          <span>钟菲 / ZHONG FEI</span>
        </a>
        <p class="footer-statement">让内容被看见，<br>也让结果被验证。</p>
        <div class="footer-links">
          <a href="{base}operations.html">运营案例</a>
          <a href="{base}design.html">设计作品</a>
          <a href="{base}about.html">关于我</a>
          <a href="mailto:Aria.zhong@outlook.com">Email ↗</a>
        </div>
      </div>
      <div class="footer-bottom">
        <p>© <span data-year>2026</span> 钟菲. 保留所有权利。</p>
        <p>杭州，中国 <span class="footer-time" data-local-time>14:23</span></p>
        <p>数据来自个人工作复盘 · 截图已做必要脱敏</p>
        <a class="back-top" href="#top">回到顶部 ↑</a>
      </div>
    </div>
  </footer>'''


def page(title, description, content, active="home", base="", body_class="", canonical_path="",
         og_image="assets/img/og-cover.jpg", extra_head="", jsonld="", base_href=""):
    canonical = SITE_URL + canonical_path
    og_abs = SITE_URL + og_image.lstrip("/")
    return f'''<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  {f'<base href="{base_href}">' if base_href else ''}
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#f3efe5">
  <meta name="author" content="钟菲">
  <title>{escape(title)}</title>
  <meta name="description" content="{escape(description, quote=True)}">
  <link rel="canonical" href="{canonical}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="钟菲作品集">
  <meta property="og:title" content="{escape(title, quote=True)}">
  <meta property="og:description" content="{escape(description, quote=True)}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{og_abs}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:locale" content="zh_CN">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{escape(title, quote=True)}">
  <meta name="twitter:description" content="{escape(description, quote=True)}">
  <meta name="twitter:image" content="{og_abs}">
  <link rel="icon" href="{base}assets/favicon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="{base}assets/img/apple-touch-icon.png">
  <link rel="preload" href="{base}assets/fonts/source-han-serif-sc-light.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="{base}assets/fonts/source-han-sans-sc-regular.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="{base}assets/css/site.css">
  <script>document.documentElement.classList.add('js');</script>
  <script src="{base}assets/js/site.js" defer></script>
  {extra_head}
  {jsonld}
</head>
<body id="top" class="{body_class}">
  <a class="skip-link" href="#main">跳到主要内容</a>
  {header(active, base)}
  <main id="main">
{content}
  </main>
  {footer(base)}
  <dialog class="lightbox" data-lightbox-dialog aria-label="图片查看器">
    <div class="lightbox__bar">
      <span class="lightbox__count" data-lightbox-count>01 / 01</span>
      <div class="lightbox__tools">
        <a class="lightbox__raw" data-lightbox-raw href="#" target="_blank" rel="noopener">原图 ↗</a>
        <button class="lightbox__close" type="button" data-lightbox-close aria-label="关闭图片查看器">关闭 ×</button>
      </div>
    </div>
    <div class="lightbox__stage" data-lightbox-stage>
      <button class="lightbox__nav lightbox__nav--prev" type="button" data-lightbox-prev aria-label="上一张">←</button>
      <figure class="lightbox__figure">
        <img data-lightbox-img src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" alt="" width="1" height="1">
        <figcaption data-lightbox-caption></figcaption>
      </figure>
      <button class="lightbox__nav lightbox__nav--next" type="button" data-lightbox-next aria-label="下一张">→</button>
    </div>
  </dialog>
  <div class="cursor" data-cursor aria-hidden="true"><span data-cursor-label></span></div>
  <div class="toast" data-toast role="status" aria-live="polite"></div>
</body>
</html>'''


def section_head(index, label, title, copy="", extra_class=""):
    copy_html = f'<p class="section-head__copy">{copy}</p>' if copy else ""
    return f'''<div class="section-head {extra_class}">
        <div class="section-head__meta"><span>{index}</span><p>{label}</p></div>
        <div class="section-head__main">
          <h2>{title}</h2>
          {copy_html}
        </div>
      </div>'''


def stat(value, suffix, label, note=""):
    note_html = f'<span class="stat__note">{note}</span>' if note else ""
    return f'''<div class="stat">
          <p class="stat__value"><span class="count-value" data-count="{value}">{value}</span><sup>{suffix}</sup></p>
          <p class="stat__label">{label}</p>
          {note_html}
        </div>'''


def cta_link(href, label, cls="btn btn--dark", arrow="↗", extra=""):
    return f'<a class="{cls}" href="{href}" {extra}><span>{label}</span><span class="btn__arrow" aria-hidden="true">{arrow}</span></a>'
