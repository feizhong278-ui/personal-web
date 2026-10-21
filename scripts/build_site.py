# -*- coding: utf-8 -*-
import json
import sys
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from content import SITE, PROJECTS, SELFIE_ACCOUNTS, SELFIE_NOTE_COUNT, SELFIE_PRODUCT_COUNT, \
    SELFIE_DETAIL_COUNT, LAZY_POSTS, SLIDE_FEATURES, CASE_NAV
from layout import page, section_head, stat, cta_link, image, design_picture, lightbox_button, \
    MANIFEST, SITE_URL

# Display order for the four design cards and project reader navigation.
DISPLAY_ORDER = ["gengong", "lingyin", "liangzhu", "harbin"]
PROJECTS.sort(key=lambda project: DISPLAY_ORDER.index(project["slug"]))
for _i, _project in enumerate(PROJECTS, 1):
    _project["index"] = f"{_i:02d}"

# Attach board metadata
for project in PROJECTS:
    boards = MANIFEST[f"project:{project['slug']}"]["boards"]
    project["_board_data"] = []
    for i, entry in enumerate(boards, 1):
        variants = entry["variants"]
        p = {"n": i, "variants": variants, "w": entry["w"], "h": entry["h"]}
        project["_board_data"].append(p)

PROJECT_BY_SLUG = {p["slug"]: p for p in PROJECTS}


def board_path(project, n, width=640):
    board = next(b for b in project["_board_data"] if b["n"] == n)
    variants = board["variants"]
    widths = sorted(int(x) for x in variants)
    chosen = width if str(width) in variants else max(widths)
    return variants[str(chosen)]


def board_srcset(project, n, base=""):
    board = next(b for b in project["_board_data"] if b["n"] == n)
    widths = sorted(int(x) for x in board["variants"])
    return ", ".join(f'{base}{board["variants"][str(w)]} {w}w' for w in widths)


def card_cover_picture(project, alt, sizes, base="", loading="lazy"):
    """Use a dedicated overview cover when provided, otherwise the first board."""
    cover = project.get("card_cover")
    if not cover:
        return design_picture(project, project["cover"], alt, base=base, sizes=sizes, loading=loading)
    srcset = ", ".join(f'{base}{url} {w}w' for url, w in cover["srcset"])
    return (f'<img src="{base}{cover["src"]}" srcset="{srcset}" '
            f'sizes="{escape(sizes, quote=True)}" alt="{escape(alt, quote=True)}" '
            f'width="{cover["w"]}" height="{cover["h"]}" '
            f'loading="{loading}" decoding="async">')


def home_deck(project):
    return f'''
      <div class="hero-deck" data-tilt aria-hidden="true">
        <div class="deck-card deck-console">
          <div class="deck-console__top"><span><i></i> GEO / VISIBILITY</span><span>01—03</span></div>
          <p class="deck-console__kicker">AI SEARCH / CONTENT MATRIX</p>
          <p class="deck-console__title">让品牌<br>被 AI 推荐。</p>
          <div class="deck-meter">
            <div><span>品牌提及率</span><b>63.46<small>%</small></b></div>
            <div class="deck-meter__bar"><i style="--w:63.46%"></i><em>44.53 → 63.46</em></div>
          </div>
          <div class="deck-meter">
            <div><span>品牌推荐率</span><b>46.15<small>%</small></b></div>
            <div class="deck-meter__bar deck-meter__bar--lime"><i style="--w:46.15%"></i><em>25.36 → 46.15</em></div>
          </div>
          <div class="deck-console__foot"><span>50+ ACCOUNTS</span><span>800+ POSTS</span><span>90% COVERAGE</span></div>
        </div>

        <figure class="deck-card deck-note">
          <img src="assets/img/ops/selfie/note-04-600.webp" alt="" width="600" height="465" decoding="async">
          <figcaption><span>XIAOHONGSHU / 01</span><span>爆款笔记</span></figcaption>
        </figure>

        <figure class="deck-card deck-design">
          <img src="{board_path(project, 14, 640)}" alt="" width="640" height="360" decoding="async">
          <figcaption><span>IP / CULTURAL CREATIVE</span><span>根宫佛国</span></figcaption>
        </figure>

        <div class="deck-sticker">
          <svg viewBox="0 0 120 120" role="presentation">
            <defs><path id="deckCircle" d="M60,60 m-41,0 a41,41 0 1,1 82,0 a41,41 0 1,1 -82,0"/></defs>
            <circle cx="60" cy="60" r="57" fill="none" stroke="currentColor" stroke-width="1"/>
            <text><textPath href="#deckCircle" startOffset="0">OPEN TO WORK · CONTENT OPERATIONS · 2027 · </textPath></text>
          </svg>
          <span class="deck-sticker__star">✳</span>
        </div>
      </div>'''


# -*- coding: utf-8 -*-
HOME_EDUCATION = [
    {
        "tone": "peach",
        "badge": "硕士",
        "label": "MDes / 2024—2027",
        "period": "2024.09 — 2027.06",
        "school": "中国计量大学",
        "degree": "设计学 · 硕士（全日制）",
        "gpa": "GPA 3.93 / 4.0 · 专业前 3%",
        "desc": "从视觉传达走到设计学，继续研究文化、视觉与内容之间的关系。",
        "image": "assets/img/education/cjlu-campus-stone.webp",
        "image_alt": "中国计量大学校园",
        "image_h": 581,
        "tags": ["ICCC 全国二等奖", "两岸青年非遗一等奖", "优秀班干部"],
    },
    {
        "tone": "mint",
        "badge": "本科",
        "label": "BA / 2020—2024",
        "period": "2020.09 — 2024.06",
        "school": "中国计量大学",
        "degree": "视觉传达 · 本科（全日制）",
        "gpa": "GPA 3.9 / 4.0 · 专业前 3%",
        "desc": "设计训练、摄影与校园媒体实践，让我开始习惯观察和记录。",
        "image": "assets/img/education/cjlu-campus-lake.webp",
        "image_alt": "中国计量大学校园",
        "image_h": 576,
        "tags": ["澳门文创全国一等奖", "互联网+ 铜奖", "摄影社社长"],
    },
]

HOME_EXPERIENCE = [
    {
        "num": "01",
        "tone": "mint",
        "period": "2026.07 — 至今",
        "company": "海康威视",
        "company_note": "",
        "role": "AI 搜索内容运营（GEO）",
        "now": True,
        "bullets": [
            "负责豆包、千问、DeepSeek、元宝等 AI 平台的 GEO 内容策略与执行，跟踪内容抓取、引用与推荐表现。",
            "搭建并运营覆盖 50+ 个账号的内容矩阵，沉淀 GEO 素材库、问答库、选题库、Prompt 模板及内容生产 SOP。",
            "围绕 36 个核心提示词产出 800+ 篇结构化内容；按项目统计口径，260+ 篇被 AI 平台召回，累计召回 2,000+ 次，核心提示词覆盖率达 90%。",
            "豆包平台品牌提及率由 44.53% 提升至 63.46%，品牌推荐率由 25.36% 提升至 46.15%。",
        ],
        "tags": ["50+ 矩阵账号", "800+ 结构化内容", "2,000+ 次召回", "90% 提示词覆盖"],
    },
    {
        "num": "02",
        "tone": "peach",
        "period": "2024.12 — 2026.06",
        "company": "杭州红商电子商务有限公司",
        "company_note": "",
        "role": "内容与店铺运营",
        "now": False,
        "bullets": [
            "独立搭建并运营小红书矩阵及抖音账号「自拍杆小圆子」，负责账号定位、选题策划、图文制作、视频拍摄剪辑与日常维护。",
            "负责 4 家 3C 数码类店铺的商品上架、主图与详情页维护，参与笔记加热及付费推广，跟踪曝光、点击、进店与成交表现。",
            "累计产出 30+ 篇爆文笔记，平均单篇获赞 1,000+，单篇最高阅读量 10 万+、赞藏 6,000+。",
            "任职期间累计成交 3 万+ 单，其中 3 个月成交 5,000+ 单；最高月成交 GMV 27 万+。",
        ],
        "tags": ["30+ 爆文", "4 家店铺", "3万+ 订单", "最高月 GMV 27.4万"],
    },
]
HOME_SKILLS = [
    {
        "icon": "🚀",
        "tone": "peach",
        "title": "核心内容运营",
        "desc": "从账号定位到内容复盘，建立可持续运转的内容系统。",
        "tags": ["小红书", "抖音", "账号定位", "选题策划", "内容矩阵", "内容 SOP"],
    },
    {
        "icon": "✦",
        "tone": "mint",
        "title": "AI & GEO",
        "desc": "理解生成式搜索的抓取、引用与推荐逻辑，让品牌成为 AI 愿意调用的知识。",
        "tags": ["GEO 策略", "Prompt", "结构化内容", "AI 搜索", "豆包 / 千问 / DeepSeek / 元宝"],
    },
    {
        "icon": "📊",
        "tone": "blue",
        "title": "数据复盘",
        "desc": "用曝光、点击、进店、成交与 AI 引用，判断内容是否真的有效。",
        "tags": ["曝光 / 阅读", "点击率", "进店 / 成交", "AI 引用", "复盘文档"],
    },
    {
        "icon": "🎨",
        "tone": "lilac",
        "title": "视觉创作",
        "desc": "把信息整理成有秩序、也有辨识度的画面。",
        "tags": ["Photoshop", "Illustrator", "剪映", "Midjourney", "Stable Diffusion", "图文排版"],
    },
]

HOME_INTERESTS = [
    {
        "icon": "📷",
        "tone": "peach",
        "title": "摄影",
        "desc": "当过摄影社社长，也做过校荣媒体记者。喜欢观察光线、构图和人在场景里的状态。",
        "tag": "记录生活",
    },
    {
        "icon": "🎨",
        "tone": "mint",
        "title": "设计收藏",
        "desc": "收集排版、包装、IP 与品牌视觉案例。做「懒羊羊素材库」时，把喜欢的东西变成了内容。",
        "tag": "保持输入",
    },
    {
        "icon": "🔎",
        "tone": "lilac",
        "title": "内容观察",
        "desc": "长期观察小红书、抖音与 AI 搜索里的表达方式。刷到的内容，最后都会变成选题库。",
        "tag": "研究表达",
    },
]

HOME_HONORS = [
    {
        "rank": 1,
        "title": "澳门文创设计大赛",
        "award": "全国一等奖",
        "year": "2024",
        "work": "灵隐万象集",
        "slug": "macau-2024-first",
    },
    {
        "rank": 2,
        "title": "国文奖 · 两岸青年非遗文创大赛",
        "award": "一等奖",
        "year": "2024",
        "work": "灵隐万象集",
        "slug": "cross-strait-2024-first",
    },
    {
        "rank": 3,
        "title": "第三届中国研究生「美丽中国」创新设计大赛",
        "award": "全国二等奖",
        "year": "2025",
        "work": "哈尔滨夏日文化使者",
        "slug": None,
    },
    {
        "rank": 4,
        "title": "ICCC 国际学生设计大赛",
        "award": "二等奖",
        "year": "2024",
        "work": "仙灵所隐",
        "slug": "iccc-2024-second",
    },
    {
        "rank": 5,
        "title": "国际金创意华人设计奖",
        "award": "银华奖",
        "year": "2024",
        "work": "舞动中华情",
        "slug": "igc-2024-silver",
    },
    {
        "rank": 6,
        "title": "澳门文创设计大赛",
        "award": "全国二等奖",
        "year": "2024",
        "work": "舞动中华情",
        "slug": "macau-2024-second",
    },
    {
        "rank": 7,
        "title": "全国会展策划创意大赛",
        "award": "全国三等奖",
        "year": "2024",
        "work": "根宫佛国「无念熊」",
        "slug": "expo-2024-national-third",
    },
    {
        "rank": 8,
        "title": "澳门文创设计大赛",
        "award": "全国三等奖",
        "year": "2025",
        "work": "三晋之旅",
        "slug": "macau-2025-third",
    },
    {
        "rank": 9,
        "title": "国文奖 · 两岸青年非遗文创大赛",
        "award": "二等奖",
        "year": "2024",
        "work": "舞动中华情",
        "slug": "cross-strait-2024-second",
    },
    {
        "rank": 10,
        "title": "国文奖 · 两岸青年非遗文创大赛",
        "award": "优秀奖",
        "year": "2025",
        "work": "出发！台州非遗之旅",
        "slug": "cross-strait-2025-merit",
    },
    {
        "rank": 11,
        "title": "浙江省会展策划创意大赛",
        "award": "一等奖",
        "year": "2024",
        "work": "根宫佛国「无念熊」",
        "slug": "expo-2024-provincial-first",
    },
    {
        "rank": 12,
        "title": "浙江省国际「互联网+」大学生创新创业大赛",
        "award": "铜奖",
        "year": "2022",
        "work": "慧知",
        "slug": "internet-plus-2022-bronze",
    },
    {
        "rank": 13,
        "title": "米兰设计周中国高校设计学科师生优秀作品展",
        "award": "浙江赛区三等奖",
        "year": "2025",
        "work": "赶海去！",
        "slug": "milan-2025-third",
    },
    {
        "rank": 14,
        "title": "大运河文化转化设计大赛",
        "award": "入围奖",
        "year": "2025",
        "work": "专业组",
        "slug": "canal-2025-finalist",
    },
    {
        "rank": 15,
        "title": "中国计量大学研究生校区联动羽毛球友谊赛",
        "award": "亚军",
        "year": "2024",
        "work": "团体赛",
        "slug": "badminton-2024-runner-up",
        "tag": "校园",
    },

]

P_STICKER = '''
<svg class="p-sticker" viewBox="0 0 160 160" aria-hidden="true">
  <defs>
    <linearGradient id="pStickerGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#d8f3ff"></stop>
      <stop offset=".52" stop-color="#d8d1ff"></stop>
      <stop offset="1" stop-color="#ffd8e6"></stop>
    </linearGradient>
    <filter id="pStickerShadow" x="-30%" y="-30%" width="160%" height="160%">
      <feDropShadow dx="0" dy="8" stdDeviation="8" flood-color="#6b5a7a" flood-opacity=".18"></feDropShadow>
    </filter>
  </defs>
  <g filter="url(#pStickerShadow)" transform="rotate(-8 80 80)">
    <ellipse cx="80" cy="40" rx="23" ry="30" fill="url(#pStickerGrad)" stroke="#fff" stroke-width="3"></ellipse>
    <ellipse cx="80" cy="40" rx="23" ry="30" fill="url(#pStickerGrad)" stroke="#fff" stroke-width="3" transform="rotate(60 80 80)"></ellipse>
    <ellipse cx="80" cy="40" rx="23" ry="30" fill="url(#pStickerGrad)" stroke="#fff" stroke-width="3" transform="rotate(120 80 80)"></ellipse>
    <ellipse cx="80" cy="40" rx="23" ry="30" fill="url(#pStickerGrad)" stroke="#fff" stroke-width="3" transform="rotate(180 80 80)"></ellipse>
    <ellipse cx="80" cy="40" rx="23" ry="30" fill="url(#pStickerGrad)" stroke="#fff" stroke-width="3" transform="rotate(240 80 80)"></ellipse>
    <ellipse cx="80" cy="40" rx="23" ry="30" fill="url(#pStickerGrad)" stroke="#fff" stroke-width="3" transform="rotate(300 80 80)"></ellipse>
    <circle cx="80" cy="80" r="31" fill="#fff9fd" stroke="#fff" stroke-width="3"></circle>
    <circle cx="70" cy="76" r="3.4" fill="#39332f"></circle>
    <circle cx="90" cy="76" r="3.4" fill="#39332f"></circle>
    <path d="M70 88 Q80 96 90 88" fill="none" stroke="#39332f" stroke-width="3" stroke-linecap="round"></path>
    <ellipse cx="63" cy="86" rx="6" ry="3" fill="#ffafc4" opacity=".55"></ellipse>
    <ellipse cx="97" cy="86" rx="6" ry="3" fill="#ffafc4" opacity=".55"></ellipse>
  </g>
  <path d="M31 28 l3 8 8 3 -8 3 -3 8 -3 -8 -8 -3 8 -3Z" fill="#fff" opacity=".9"></path>
  <path d="M132 118 l2 6 6 2 -6 2 -2 6 -2 -6 -6 -2 6 -2Z" fill="#fff" opacity=".8"></path>
</svg>'''


def _chips(tags, tone=""):
    return "".join(f'<span class="p-chip{(" p-chip--" + tone) if tone else ""}">{tag}</span>' for tag in tags)


def _p_stat(value, suffix, label, note, tone):
    return f'''
      <div class="p-stat p-stat--{tone}">
        <div class="p-stat__value"><span class="count-value" data-count="{value}">{value}</span><sup>{suffix}</sup></div>
        <p>{label}</p>
        <small>{note}</small>
      </div>'''


def _project_visual_geo():
    return '''
      <div class="p-geo-visual">
        <div class="p-geo-visual__head"><span><i></i> GEO / VISIBILITY</span><span>2026.10</span></div>
        <p class="p-geo-visual__title">让品牌<br>被 AI 推荐。</p>
        <div class="p-geo-metric">
          <div><span>品牌提及率</span><b>63.46<small>%</small></b></div>
          <div class="p-bar"><i style="--w:63.46%"></i></div>
          <small>44.53 → 63.46</small>
        </div>
        <div class="p-geo-metric">
          <div><span>品牌推荐率</span><b>46.15<small>%</small></b></div>
          <div class="p-bar p-bar--coral"><i style="--w:46.15%"></i></div>
          <small>25.36 → 46.15</small>
        </div>
        <div class="p-geo-visual__foot"><span>50+ 账号</span><span>800+ 内容</span><span>90% 覆盖</span></div>
      </div>'''


def _project_row(project, tone, number, label, title, desc, tags, metrics, visual, href, cta):
    chips = _chips(tags)
    metric_html = "".join(f'<span><b>{v}</b>{k}</span>' for v, k in metrics)
    return f'''
      <a class="p-project-row p-project-row--{tone}" href="{href}" data-cursor="OPEN">
        <div class="p-project-row__aside">
          <span class="p-project-row__num">{number}</span>
          <span class="p-project-row__label">{label}</span>
        </div>
        <div class="p-project-row__body">
          <div class="p-chip-row">{chips}</div>
          <h3>{title}</h3>
          <p>{desc}</p>
          <div class="p-project-row__metrics">{metric_html}</div>
          <span class="p-project-row__cta">{cta} <b>↗</b></span>
        </div>
        <div class="p-project-row__visual">{visual}</div>
      </a>'''


def new_index_page():
    g = PROJECT_BY_SLUG["gengong"]
    l = PROJECT_BY_SLUG["liangzhu"]

    # Selfie collage
    selfie_visual = '''
      <div class="p-note-stack" aria-hidden="true">
        <img src="assets/img/ops/selfie/note-09-600.webp" alt="" width="600" height="460" loading="lazy" decoding="async">
        <img src="assets/img/ops/selfie/note-04-600.webp" alt="" width="600" height="459" loading="lazy" decoding="async">
        <img src="assets/img/ops/selfie/note-10-600.webp" alt="" width="600" height="448" loading="lazy" decoding="async">
        <span>14 NOTES / 4 ACCOUNTS</span>
      </div>'''

    lazy_visual = f'''
      <div class="p-board-visual">
        <img src="assets/img/ops/lazy/case-board-1000.webp" alt="懒羊羊素材库内容案例板" width="1000" height="562" loading="lazy" decoding="async">
        <span>CASE BOARD / 6 POSTS</span>
      </div>'''

    project_rows = "".join([
        _project_row(
            "geo", "mint", "01", "GEO / AI SEARCH", "让品牌，<br>进入 AI 的答案。",
            "从 36 个核心提示词出发，搭建 50+ 账号内容矩阵，让品牌在生成式搜索中被看见、被引用、被推荐。",
            ["GEO 策略", "内容矩阵", "AI 搜索"],
            [("50+", "账号"), ("800+", "内容"), ("2,000+", "召回"), ("90%", "覆盖")],
            _project_visual_geo(), "case-geo.html", "查看完整案例"
        ),
        _project_row(
            "selfie", "peach", "02", "COMMERCE CONTENT", "把种草，<br>做成生意。",
            "从账号定位、拍剪、标题封面，到商品页与成交复盘，跑通一条内容到生意的完整链路。",
            ["小红书", "抖音", "电商转化"],
            [("30+", "爆文"), ("3万+", "订单"), ("27.4万", "最高月 GMV")],
            selfie_visual, "case-selfie.html", "查看完整案例"
        ),
        _project_row(
            "lazy", "lilac", "03", "DESIGN CONTENT", "让审美，<br>成为流量。",
            "从 0 到 1 搭建「懒羊羊素材库」，用设计案例内容连接审美、收藏与店铺转化。",
            ["设计内容", "0 → 1", "内容账号"],
            [("3万+", "赞藏"), ("6", "篇爆款"), ("3,645", "单篇最高赞")],
            lazy_visual, "case-lazy.html", "查看完整案例"
        ),
    ])

    design_cards = ""
    for p in PROJECTS:
        design_cards += f'''
        <a class="p-design-card" href="design/{p['slug']}.html" data-cursor="OPEN">
          <div class="p-design-card__img">
            {card_cover_picture(p, p['title'] + "项目封面", sizes="(max-width: 700px) 100vw, 28vw", loading="lazy")}
            <span>{p['index']} / 04</span>
          </div>
          <div class="p-design-card__body">
            <div class="p-chip-row"><span class="p-chip p-chip--soft">{p['discipline'].split(" / ")[0]}</span><span class="p-chip p-chip--soft">{p['year']}</span>{f'<span class="p-chip p-chip--soft">{p["award_short"]}</span>' if p['award_short'] and p['award_short'] != p['discipline'].split(" / ")[0] else ''}</div>
            <h3>{p['title']}</h3>
            <p>{p['summary']}</p>
            <span class="p-design-card__cta">查看项目 <b>↗</b></span>
          </div>
        </a>'''

    school_cards = ""
    for item in HOME_EDUCATION:
        tags = _chips(item["tags"], "soft")
        school_cards += f'''
        <article class="p-school p-school--{item['tone']}">
          <div class="p-school__art">
            <img class="p-school__art-img" src="{item['image']}" alt="{item['image_alt']}" width="1200" height="{item['image_h']}" loading="lazy" decoding="async">
            <span class="p-school__shade" aria-hidden="true"></span>
            <span class="p-school__badge">{item['badge']}</span>
            <span class="p-school__label">{item['label']}</span>
            <span class="p-school__emoji" aria-hidden="true">🎓</span>
          </div>
          <div class="p-school__body">
            <p class="p-date">{item['period']}</p>
            <h3>{item['school']}</h3>
            <p class="p-school__degree">{item['degree']}</p>
            <p class="p-school__gpa">{item['gpa']}</p>
            <p class="p-school__desc">{item['desc']}</p>
            <div class="p-chip-row">{tags}</div>
          </div>
        </article>'''

    honor_chips = "".join(
        f'<span class="p-award">{item["title"]} · {item["award"]}</span>' for item in HOME_HONORS
    )

    experience_cards = ""
    for item in HOME_EXPERIENCE:
        now = '<span class="p-now-badge"><i></i>NOW</span>' if item["now"] else ""
        bullets = "".join(f'<li>{b}</li>' for b in item["bullets"])
        tags = _chips(item["tags"], "soft")
        experience_cards += f'''
        <article class="p-exp-item p-exp-item--{item['tone']}">
          <div class="p-exp-marker">{item['num']}</div>
          <div class="p-exp-card">
            <div class="p-exp-card__top"><span class="p-date">{item['period']}</span>{now}</div>
            <h3>{item['company']}{f' <small>{item["company_note"]}</small>' if item["company_note"] else ""}</h3>
            <p class="p-role">{item['role']}</p>
            <ul>{bullets}</ul>
            <div class="p-chip-row">{tags}</div>
          </div>
        </article>'''

    skill_cards = ""
    for s in HOME_SKILLS:
        skill_cards += f'''
        <article class="p-skill-card p-skill-card--{s['tone']}">
          <span class="p-skill-icon" aria-hidden="true">{s['icon']}</span>
          <h3>{s['title']}</h3>
          <p>{s['desc']}</p>
          <div class="p-chip-row">{_chips(s['tags'], "soft")}</div>
        </article>'''

    interest_cards = ""
    for item in HOME_INTERESTS:
        interest_cards += f'''
        <article class="p-interest p-interest--{item['tone']}">
          <span class="p-interest__icon" aria-hidden="true">{item['icon']}</span>
          <span class="p-interest__tag">{item['tag']}</span>
          <h3>{item['title']}</h3>
          <p>{item['desc']}</p>
        </article>'''

    content = f'''
    <section class="p-hero" id="about" aria-labelledby="hero-title">
      <div class="container p-hero__grid">
        <div class="p-hero__copy">
          <p class="hello-pill"><i aria-hidden="true"></i> HELLO / 你好</p>
          <div class="p-hero__title-wrap">
            <h1 id="hero-title">Hi,<br><span>我是钟菲</span></h1>
            {P_STICKER}
          </div>
          <p class="p-hero__role">内容运营 / GEO 内容运营 / 视觉设计</p>
          <div class="p-philosophy">
            <span>个人理念 /</span>
            <p>让内容有审美的形状，<br>也有可被验证的结果。</p>
          </div>
          <p class="p-hero__bio">设计学硕士，7 年设计训练。做过 AI 搜索内容矩阵、电商内容与店铺运营、设计内容账号；擅长把洞察拆成内容结构，用数据复盘，也具备视觉与拍剪能力。</p>
          <div class="p-chip-row">
            <span class="p-chip">GEO 内容</span><span class="p-chip">小红书 / 抖音</span><span class="p-chip">电商运营</span><span class="p-chip">数据分析</span><span class="p-chip">视觉表达</span>
          </div>
          <div class="p-hero__actions">
            <a class="p-btn p-btn--dark" href="assets/docs/zhongfei-resume.pdf?v=20261021f" download>下载简历 <span>↗</span></a>
            <a class="p-btn p-btn--ghost" href="#contact">联系我 <span>↓</span></a>
          </div>
        </div>
        <div class="p-hero__visual">
          <div class="p-hero__halo" aria-hidden="true"></div>
          <figure class="p-portrait" data-tilt-portrait>
            <div class="p-portrait__img">
              <img src="assets/img/portrait-900.webp" srcset="assets/img/portrait-480.webp 480w, assets/img/portrait-720.webp 720w, assets/img/portrait-900.webp 900w" sizes="(max-width: 700px) 92vw, 440px" alt="钟菲的职业肖像" width="900" height="1199" loading="eager" fetchpriority="high" decoding="async">
            </div>
            <figcaption><span>ZHONG FEI / PORTRAIT 2026</span></figcaption>
          </figure>
          <div class="p-now">
            <span class="p-now__label"><i aria-hidden="true"></i> NOW</span>
            <strong>2027 届 · 求职中</strong>
            <small>杭州 / 可接受江浙沪</small>
          </div>
          <span class="p-floating p-floating--a">OPEN TO WORK</span>
        </div>
      </div>
      <a class="p-scroll-hint" href="#projects">继续下滑，探索更多 <span>↓</span></a>
    </section>

    <section class="p-section p-about" aria-labelledby="about-title">
      <div class="container">
        <div class="p-about-card">
          <div class="p-about-card__copy">
            <p class="p-kicker">01 / ABOUT ME</p>
            <h2 id="about-title">把审美变成方法，<br>把内容做成结果。</h2>
            <p>我在中国计量大学读了七年设计，从视觉传达走到设计学。设计训练给我的不只是审美，更是一套观察、拆解、表达、验证问题的方法。</p>
            <p>现在，我把这套方法用在内容增长上：既关心一条内容有没有被看见，也关心它有没有带来下一步行动。</p>
            <div class="p-chip-row"><span class="p-chip">设计学硕士</span><span class="p-chip">GPA 3.93 / 4.0</span><span class="p-chip">专业前 3%</span></div>
            <a class="p-inline-link" href="about.html">更多关于我 <span>↗</span></a>
          </div>
          <div class="p-stat-grid">
            {_p_stat(50, "+", "GEO 内容矩阵账号", "AI SEARCH / 2026", "mint")}
            {_p_stat(800, "+", "结构化内容", "围绕 36 个核心提示词", "peach")}
            {_p_stat(2000, "+", "AI 平台累计召回", "260+ 篇内容被召回", "lilac")}
            {_p_stat(3, "万+", "累计成交订单", "最高月 GMV 27.4万", "blue")}
          </div>
        </div>
      </div>
    </section>

    <section class="p-section p-projects" id="projects" aria-labelledby="projects-title">
      <div class="container">
        <div class="p-section-head">
          <p class="p-kicker">02 / SELECTED WORK</p>
          <h2 id="projects-title">我把内容，<br>做成了什么。</h2>
          <p>三个运营项目，四组设计作品。每一个都从真实问题出发，也都有可以被查看的过程与结果。</p>
        </div>
        <div class="p-project-list">{project_rows}</div>
        <div class="p-project-more"><a class="p-btn p-btn--ghost" href="operations.html">查看全部运营案例 <span>↗</span></a></div>

        <div class="p-design-head">
          <div><p class="p-kicker">DESIGN ARCHIVE / 04</p><h2>设计，是另一种表达。</h2></div>
          <p>45 张项目板，从城市 IP、景区文创、寺院视觉到博物馆角色设计。</p>
        </div>
        <div class="p-design-grid">{design_cards}</div>
        <div class="p-project-more"><a class="p-btn p-btn--ghost" href="design.html">打开完整设计档案 <span>↗</span></a></div>
      </div>
    </section>

    <section class="p-section p-experience" id="experience" aria-labelledby="experience-title">
      <div class="container">
        <div class="p-section-head">
          <p class="p-kicker">03 / THE PRACTITIONER</p>
          <h2 id="experience-title">我在过往职场<br>做过什么。</h2>
          <p>从 AI 搜索到电商内容。两段实习经历，都同时包含策略、执行与复盘。</p>
        </div>
        <div class="p-timeline">{experience_cards}</div>
        <div class="p-center-link"><a class="p-inline-link" href="assets/docs/zhongfei-resume.pdf?v=20261021f" download>下载完整简历 PDF <span>↓</span></a></div>
      </div>
    </section>

    <section class="p-section p-education" id="education" aria-labelledby="education-title">
      <div class="container">
        <div class="p-section-head">
          <p class="p-kicker">04 / EDUCATION</p>
          <h2 id="education-title">我的学习轨迹</h2>
          <p>从视觉传达到设计学，从本科到硕士。设计训练一直是我理解内容的方式。</p>
        </div>
        <div class="p-school-grid">
          {school_cards}
          <span class="p-school-path" aria-hidden="true">成长路径 →</span>
        </div>
        <div class="p-awards-card">
          <div><p class="p-kicker">HONORS / 荣誉</p><h3>一些被看见的时刻</h3></div>
          <div class="p-awards">{honor_chips}</div>
        </div>
      </div>
    </section>

    <section class="p-section p-skills" id="skills" aria-labelledby="skills-title">
      <div class="container">
        <div class="p-section-head">
          <p class="p-kicker">05 / SKILLS</p>
          <h2 id="skills-title">技能图谱</h2>
          <p>跨领域的复合能力：从品牌全链路内容，到电商多维运营，再到 AI 搜索与视觉表达。</p>
        </div>
        <div class="p-skill-grid">{skill_cards}</div>
        <div class="p-soft-skills">
          <span>SOFT SKILLS /</span>
          <span class="p-chip">项目管理</span><span class="p-chip">跨部门协作</span><span class="p-chip">沟通表达</span><span class="p-chip">快速学习</span><span class="p-chip">抗压能力</span>
        </div>
      </div>
    </section>

    <section class="p-section p-interests" id="interests" aria-labelledby="interests-title">
      <div class="container">
        <div class="p-section-head">
          <p class="p-kicker">06 / OFF DUTY</p>
          <h2 id="interests-title">工作之外的我</h2>
          <p>关于审美、观察与记录。它们不一定直接写进 KPI，但一直在影响我怎么做内容。</p>
        </div>
        <div class="p-interest-grid">{interest_cards}</div>
        <div class="p-interest-note"><span>摄影社社长</span><i></i><span>校荣媒体记者</span><i></i><span>设计素材账号主理人</span></div>
      </div>
    </section>

    <section class="p-contact" id="contact" aria-labelledby="contact-title">
      <div class="container">
        <div class="p-contact-card">
          <span class="p-contact-sticker" aria-hidden="true">✳</span>
          <p class="p-kicker">LET'S TALK / 联系我</p>
          <h2 id="contact-title">一起做点<br>有回声的内容。</h2>
          <p class="p-contact-copy">如果你正在找一位懂内容、也懂视觉的内容运营，欢迎直接把机会发给我。2027 届，杭州，可接受江浙沪机会。</p>
          <div class="p-contact-actions">
            <a class="p-btn p-btn--dark" href="mailto:Aria.zhong@outlook.com">Aria.zhong@outlook.com <span>↗</span></a>
            <button class="p-btn p-btn--ghost" type="button" data-copy-email="Aria.zhong@outlook.com"><span class="email-copy__action">复制邮箱</span></button>
            <a class="p-inline-link" href="assets/docs/zhongfei-resume.pdf?v=20261021f" download>下载简历 PDF <span>↓</span></a>
          </div>
          <div class="p-contact-meta"><span><i></i> OPEN TO WORK</span><span>HANGZHOU / CN</span><span>2027</span></div>
        </div>
      </div>
    </section>
'''
    return page(
        "钟菲｜内容运营 · GEO 内容增长 · 设计作品集",
        SITE["description"],
        content,
        active="home",
        body_class="page-home",
        canonical_path="",
    )


def ops_stat(value, suffix, label, note="", decimals=0):
    note_html = f'<span>{note}</span>' if note else ""
    decimals_attr = f' data-decimals="{decimals}"' if decimals else ""
    return f'''<div class="ops-stat">
      <p class="ops-stat__value"><span class="count-value" data-count="{value}"{decimals_attr}>{value}</span><sup>{suffix}</sup></p>
      <p class="ops-stat__label">{label}</p>
      {note_html}
    </div>'''


def operations_page():
    dots = []
    for i in range(1, 51):
        cls = " is-lit" if i in {3, 7, 11, 16, 21, 28, 32, 37, 41, 46, 50} else ""
        dots.append(f'<i class="{cls.strip()}" style="--d:{i}"></i>')
    dots_html = "".join(dots)

    slide_triggers = ""
    for n in range(1, 31):
        slide_triggers += lightbox_button(
            f'<span class="visually-hidden">第 {n} 页</span>',
            "slides",
            f"assets/img/slides/slide-{n:02d}-1600.webp",
            f"拆解小红书爆款笔记 / 第 {n:02d} 页",
            f"拆解小红书爆款笔记手册第 {n} 页",
            cls="visually-hidden",
        )

    slide_features = ""
    for feature in SLIDE_FEATURES:
        n = feature["n"]
        inner = f'''
          <span class="slide-card__img"><img src="assets/img/slides/slide-{n:02d}-480.webp" alt="拆解小红书爆款笔记第 {n} 页：{feature['label']}" width="480" height="270" loading="lazy" decoding="async"></span>
          <span class="slide-card__meta"><span>P.{n:02d} / {feature['label']}</span><b>查看 ↗</b></span>
          <span class="slide-card__caption">{feature['caption']}</span>'''
        slide_features += f'<button class="slide-card" type="button" data-open-group="slides" data-open-index="{n - 1}" data-cursor="OPEN">{inner}</button>'

    accounts = ""
    for i, account in enumerate(SELFIE_ACCOUNTS, 1):
        accounts += lightbox_button(
            f'''<span class="account-phone__frame"><img src="{account['img']}" alt="{account['name']}小红书账号主页截图" width="760" height="1651" loading="lazy" decoding="async"></span>
            <span class="account-phone__meta"><span>{i:02d} / {account['name']}</span><span>{account['label']}</span></span>''',
            "accounts",
            account["img"],
            f"{account['name']} / 小红书账号主页",
            f"{account['name']}小红书账号主页截图",
            cls="account-phone",
            extra='data-cursor="OPEN"',
        )

    notes = ""
    for i in range(1, SELFIE_NOTE_COUNT + 1):
        note_key = f"assets/img/ops/selfie/note-{i:02d}-600.webp"
        note_dims = MANIFEST[note_key]
        notes += lightbox_button(
            f'''<img src="{note_key}" srcset="{note_key} 600w, assets/img/ops/selfie/note-{i:02d}-1200.webp 1200w" sizes="(max-width: 650px) 80vw, (max-width: 1000px) 42vw, 22vw" alt="自拍杆小圆子爆款笔记截图 {i:02d}" width="{note_dims['w']}" height="{note_dims['h']}" loading="lazy" decoding="async">
            <span class="note-card__overlay"><span>NOTE {i:02d}</span><b>打开截图 ↗</b></span>''',
            "selfie-notes",
            f"assets/img/ops/selfie/note-{i:02d}-1200.webp",
            f"自拍杆小圆子爆款笔记截图 / {i:02d}",
            f"自拍杆小圆子爆款笔记截图 {i:02d}",
            cls="note-card",
            extra='data-cursor="OPEN"',
        )

    products = ""
    for i in range(1, SELFIE_PRODUCT_COUNT + 1):
        products += lightbox_button(
            f'<img src="assets/img/ops/selfie/product-{i:02d}-700.webp" alt="自拍杆商品主图 {i:02d}" width="700" height="933" loading="lazy" decoding="async"><span>主图 {i:02d}</span>',
            "products",
            f"assets/img/ops/selfie/product-{i:02d}-700.webp",
            f"3C 店铺商品主图 / {i:02d}",
            f"自拍杆商品主图 {i:02d}",
            cls="product-card",
        )
    details = ""
    for i in range(1, SELFIE_DETAIL_COUNT + 1):
        details += lightbox_button(
            f'<img src="assets/img/ops/selfie/detail-{i:02d}-620.webp" alt="自拍杆商品详情页设计 {i:02d}" width="620" height="4133" loading="lazy" decoding="async"><span>DETAIL {i:02d} <b>↗</b></span>',
            "details",
            f"assets/img/ops/selfie/detail-{i:02d}-620.webp",
            f"自拍杆商品详情页 / {i:02d}",
            f"自拍杆商品详情页设计 {i:02d}",
            cls="detail-card",
        )

    lazy_posts = ""
    for i, post in enumerate(LAZY_POSTS, 1):
        post_dims = MANIFEST[post["img"]]
        lazy_posts += lightbox_button(
            f'''<span class="lazy-post__img"><img src="{post['img']}" alt="{post['title']} 笔记截图" width="{post_dims['w']}" height="{post_dims['h']}" loading="lazy" decoding="async"></span>
            <span class="lazy-post__body">
              <span class="lazy-post__index">POST {i:02d}</span>
              <strong>{post['title']}</strong>
              <span class="lazy-post__metrics"><span><b>{post['likes']:,}</b> 赞</span><span><b>{post['saves']:,}</b> 藏</span><span><b>{post['comments']}</b> 评</span></span>
            </span>''',
            "lazy-notes",
            post["img"],
            f"懒羊羊素材库 / {post['title']}（{post['likes']:,} 赞 · {post['saves']:,} 藏）",
            f"{post['title']} 笔记截图",
            cls="lazy-post",
            w=post_dims["w"],
            h=post_dims["h"],
        )

    content = f'''
    <section class="page-intro ops-intro" aria-labelledby="ops-title">
      <div class="container">
        <div class="intro-topline">
          <p class="micro-label">OPERATIONS / 2024—NOW</p>
          <p class="micro-label">03 CASES / 01 METHOD</p>
        </div>
        <h1 id="ops-title">把注意力，<br><span class="accent">变成结果。</span></h1>
        <div class="intro-bottom">
          <p>三个项目，三种内容能力：在 AI 搜索里建立品牌可见度，在电商场景里完成内容到成交，在设计分享里从 0 到 1 建立账号。</p>
          <div class="ops-index">
            <a href="case-geo.html"><span>01</span><strong>GEO 内容增长</strong><small>AI 搜索 / 50+ 内容矩阵</small><b>↗</b></a>
            <a href="case-selfie.html"><span>02</span><strong>自拍杆小圆子</strong><small>小红书 × 抖音 / 店铺转化</small><b>↗</b></a>
            <a href="case-lazy.html"><span>03</span><strong>懒羊羊素材库</strong><small>设计内容 / 0 到 1</small><b>↗</b></a>
          </div>
        </div>
      </div>
    </section>

    <nav class="case-nav" aria-label="运营案例目录">
      <div class="container case-nav__inner">
        <span class="case-nav__label">CASE INDEX</span>
        <div class="case-nav__links">
          <a href="#geo" data-case-link><span>01</span> GEO 内容增长</a>
          <a href="#selfie" data-case-link><span>02</span> 自拍杆小圆子</a>
          <a href="#lazy" data-case-link><span>03</span> 懒羊羊素材库</a>
        </div>
        <a class="case-nav__top" href="#top">TOP ↑</a>
      </div>
    </nav>

    <section class="case case--geo" id="geo" aria-labelledby="geo-title">
      <div class="container">
        <div class="case-label"><span>CASE 01 / GEO CONTENT</span><span>2026.07—至今</span></div>
        <div class="case-intro">
          <div>
            <p class="eyebrow">AI SEARCH / CONTENT MATRIX</p>
            <h2 id="geo-title">让品牌，<br>进入 AI 的答案。</h2>
          </div>
          <div class="case-intro__side">
            <p>当用户把问题交给 AI，品牌竞争的对象不再只是搜索结果页，而是答案里的那一句话。</p>
            <dl class="role-list">
              <div><dt>公司</dt><dd>海康威视</dd></div>
              <div><dt>角色</dt><dd>AI 搜索内容运营（GEO）</dd></div>
              <div><dt>范围</dt><dd>策略 / 矩阵 / 生产 / 复盘</dd></div>
            </dl>
          </div>
        </div>

        <div class="ops-stats">
          {ops_stat(50, '+', '内容矩阵账号', 'ACCOUNTS')}
          {ops_stat(800, '+', '结构化内容', '36 个核心提示词')}
          {ops_stat(2000, '+', 'AI 平台累计召回', '260+ 篇被召回')}
          {ops_stat(90, '%', '核心提示词覆盖率', '2026.08—10')}
        </div>

        <div class="geo-console" data-tabs>
          <div class="geo-console__bar">
            <span class="console-brand"><i aria-hidden="true"></i> GEO / CONTENT SYSTEM</span>
            <span>VISUALIZATION / 2026.10</span>
          </div>
          <div class="geo-console__body">
            <div class="geo-console__intro">
              <p class="micro-label">INSIDE THE SYSTEM</p>
              <p class="geo-console__statement">把品牌信息，<br>做成可被 AI 调用的<br>内容资产。</p>
              <div class="console-tabs" role="tablist" aria-label="GEO 内容系统视图">
                <button class="console-tab is-active" type="button" role="tab" id="geo-tab-results" aria-controls="geo-panel-results" aria-selected="true">结果 / RESULTS</button>
                <button class="console-tab" type="button" role="tab" id="geo-tab-matrix" aria-controls="geo-panel-matrix" aria-selected="false" tabindex="-1">矩阵 / MATRIX</button>
                <button class="console-tab" type="button" role="tab" id="geo-tab-content" aria-controls="geo-panel-content" aria-selected="false" tabindex="-1">内容 / CONTENT</button>
              </div>
              <p class="console-hint">点击切换，查看这套系统如何运转。</p>
            </div>
            <div class="geo-console__panels">
              <div class="console-panel" id="geo-panel-results" role="tabpanel" aria-labelledby="geo-tab-results">
                <div class="result-row">
                  <div class="result-row__head"><span>品牌提及率</span><span>DOUBAO / 优化前后</span></div>
                  <div class="result-row__values"><span>44.53<small>%</small></span><i>→</i><strong>63.46<small>%</small></strong></div>
                  <div class="result-bars"><i class="result-bars__before" style="--w:44.53%"></i><i class="result-bars__after" style="--w:63.46%"></i></div>
                </div>
                <div class="result-row">
                  <div class="result-row__head"><span>品牌推荐率</span><span>DOUBAO / 优化前后</span></div>
                  <div class="result-row__values"><span>25.36<small>%</small></span><i>→</i><strong>46.15<small>%</small></strong></div>
                  <div class="result-bars result-bars--lime"><i class="result-bars__before" style="--w:25.36%"></i><i class="result-bars__after" style="--w:46.15%"></i></div>
                </div>
                <div class="result-bottom">
                  <div class="coverage-ring" style="--p:90"><span>90<small>%</small></span></div>
                  <div><p>核心提示词覆盖率</p><span>围绕 36 个核心提示词建立稳定、可复用的内容供给。</span></div>
                  <div class="platform-chips"><span>豆包</span><span>千问</span><span>DeepSeek</span><span>元宝</span></div>
                </div>
              </div>
              <div class="console-panel" id="geo-panel-matrix" role="tabpanel" aria-labelledby="geo-tab-matrix" hidden>
                <div class="matrix-panel">
                  <div class="matrix-panel__head"><span>50+ ACCOUNTS / CONTENT MATRIX</span><span>ACTIVE NODES</span></div>
                  <div class="matrix-grid">{dots_html}</div>
                  <div class="matrix-panel__foot">
                    <span>素材库</span><span>问答库</span><span>选题库</span><span>Prompt</span><span>SOP</span>
                  </div>
                  <p>不是 50 个账号各说各话，而是围绕同一套品牌知识，用不同内容形态持续供给。</p>
                </div>
              </div>
              <div class="console-panel" id="geo-panel-content" role="tabpanel" aria-labelledby="geo-tab-content" hidden>
                <div class="content-panel">
                  <div class="content-panel__hero"><span>800<sup>+</sup></span><p>篇结构化内容<br>围绕 36 个核心提示词</p></div>
                  <div class="content-panel__grid">
                    <div><strong>260<sup>+</sup></strong><span>篇内容被 AI 召回</span></div>
                    <div><strong>2,000<sup>+</sup></strong><span>次累计召回</span></div>
                    <div><strong>90<sup>%</sup></strong><span>核心提示词覆盖率</span></div>
                  </div>
                  <div class="content-panel__list"><span>素材库</span><span>问答库</span><span>选题库</span><span>Prompt 模板</span><span>内容生产 SOP</span></div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="case-process">
          <article><span>01</span><h3>识别问题</h3><p>把用户在 AI 里的真实提问，拆成 36 个核心提示词。先理解问题如何被问出来，再决定内容怎么回答。</p></article>
          <article><span>02</span><h3>建立系统</h3><p>搭建 50+ 账号的内容矩阵，沉淀素材库、问答库、选题库、Prompt 模板与内容 SOP，让生产不依赖单次灵感。</p></article>
          <article><span>03</span><h3>持续生产</h3><p>围绕核心问题持续产出 800+ 篇结构化内容，用问答、清单、场景与测评等不同形态覆盖用户决策路径。</p></article>
          <article><span>04</span><h3>追踪迭代</h3><p>跟踪豆包、千问、DeepSeek、元宝的抓取、引用与推荐表现，根据数据反馈调整选题与内容结构。</p></article>
        </div>

        <blockquote class="case-quote">
          <p>“GEO 不是把 SEO 换个名字，而是为 AI 准备一套可信、清晰、可复用的品牌知识。”</p>
          <span>MY WORKING DEFINITION</span>
        </blockquote>
        <p class="source-note">数据口径：2026.08—2026.10 项目统计；提及率与推荐率为豆包平台优化前后对比。页面为数据可视化，并非真实 AI 对话截图。</p>
      </div>
    </section>

    <section class="case case--selfie" id="selfie" aria-labelledby="selfie-title">
      <div class="container">
        <div class="case-label"><span>CASE 02 / COMMERCE CONTENT</span><span>2024.12—2026.06</span></div>
        <div class="case-intro">
          <div>
            <p class="eyebrow">XIAOHONGSHU × DOUYIN / 3C</p>
            <h2 id="selfie-title">把种草，<br>做成生意。</h2>
          </div>
          <div class="case-intro__side">
            <p>从选题、拍摄、剪辑，到店铺页面与成交复盘，跑通内容到生意的完整链路。</p>
            <dl class="role-list">
              <div><dt>公司</dt><dd>杭州红商电子商务有限公司</dd></div>
              <div><dt>角色</dt><dd>账号矩阵主理人 / 独立拍剪写与运营</dd></div>
              <div><dt>范围</dt><dd>小红书 / 抖音</dd></div>
            </dl>
          </div>
        </div>

        <div class="ops-stats ops-stats--selfie">
          {ops_stat(30, '+', '高互动爆文笔记', 'AVG. 1,000+ LIKES')}
          {ops_stat(10, 'W+', '单篇最高阅读量', 'XIAOHONGSHU')}
          {ops_stat(3, '万+', '任职期间累计成交订单', '3 个月 5,000+ 单')}
          {ops_stat(27.4, '万', '最高月成交 GMV', '2025.12 / 店铺后台', 1)}
        </div>

        <div class="subsection">
          <div class="subsection__head">
            <div><p class="micro-label">01 / ACCOUNT MATRIX</p><h3>四个账号，<br>一套内容测试场。</h3></div>
            <p>围绕同一品类建立多个账号，测试不同选题与表达，再把有效经验复制到主账号与店铺。点击查看账号主页截图。</p>
          </div>
          <div class="account-row">{accounts}</div>
          <div class="account-extra">
            <span>ALSO ON DOUYIN / 账号与店铺</span>
            <button type="button" data-lightbox-group="douyin" data-full="assets/img/ops/selfie/douyin-home-760.webp" data-caption="自拍杆小圆子 / 抖音账号主页" data-alt="自拍杆小圆子抖音账号主页截图" data-w="760" data-h="1651">账号主页 ↗</button>
            <button type="button" data-lightbox-group="douyin" data-full="assets/img/ops/selfie/douyin-store-760.webp" data-caption="自拍杆小圆子 / 抖音店铺页面" data-alt="自拍杆小圆子抖音店铺页面截图" data-w="760" data-h="1651">店铺页面 ↗</button>
            <p>抖音账号与店铺截图 / 已做必要脱敏</p>
          </div>
        </div>

        <div class="subsection">
          <div class="subsection__head">
            <div><p class="micro-label">02 / CONTENT PLAYBOOK</p><h3>爆款不是运气，<br>是可以拆解的。</h3></div>
            <p>把标题、封面、素材、正文、Tag 与平台推流机制，拆成一套 30 页的方法手册。先理解规则，再持续做实验。</p>
          </div>
          <div class="playbook-layout">
            <div class="slide-feature-grid">{slide_features}</div>
            <aside class="playbook-aside">
              <p class="micro-label">FIELD MANUAL / 30 PAGES</p>
              <h4>拆解小红书<br>爆款笔记</h4>
              <p>从「标题公式」到「阶梯式推流」，一份面向自拍杆项目的完整内容复盘。</p>
              <button class="btn btn--dark" type="button" data-open-group="slides" data-open-index="0"><span>翻开完整手册</span><span class="btn__arrow" aria-hidden="true">↗</span></button>
              <a class="text-link" href="assets/docs/selfie-stick-playbook.pdf" download>下载 PDF（7.1 MB） <span>↓</span></a>
            </aside>
          </div>
        </div>

        <div class="subsection">
          <div class="subsection__head">
            <div><p class="micro-label">03 / CONTENT WALL</p><h3>把每一条内容，<br>当成一次实验。</h3></div>
            <p>14 张可公开的爆款笔记截图，覆盖演唱会、旅行、咖啡店、机场、桌搭等真实使用场景。</p>
          </div>
          <div class="note-wall">{notes}</div>
        </div>

        <div class="subsection">
          <div class="subsection__head">
            <div><p class="micro-label">04 / CONTENT TO COMMERCE</p><h3>内容和生意之间，<br>不能靠感觉。</h3></div>
            <p>跟踪曝光、点击、进店与成交表现，用数据判断哪一类选题、封面与场景值得继续投入。</p>
          </div>
          <div class="commerce-grid">
            <div class="commerce-panel">
              <div class="commerce-panel__head"><span>2025.12 / 经营数据概览</span><span class="data-live"><i></i> SHOP DATA</span></div>
              <div class="commerce-number"><span>¥</span>273,932.50</div>
              <p class="commerce-date">2025 年 12 月支付金额 · 4,397 笔订单</p>
              <div class="commerce-mini-grid">
                <div><strong>4,397</strong><span>支付订单</span></div>
                <div><strong>36,439</strong><span>商品访客</span></div>
                <div><strong>11.48%</strong><span>支付转化率</span></div>
                <div><strong>69.41%</strong><span>笔记支付占比</span></div>
              </div>
              <div class="account-bars">
                <div class="account-bar"><span>自拍杆小圆子</span><div><i style="--w:73.13%"></i></div><b>73.13%</b></div>
                <div class="account-bar"><span>自拍杆小小圆子</span><div><i style="--w:12.32%"></i></div><b>12.32%</b></div>
                <div class="account-bar"><span>自拍杆大圆子</span><div><i style="--w:7.38%"></i></div><b>7.38%</b></div>
                <div class="account-bar"><span>自拍杆中圆子</span><div><i style="--w:7.17%"></i></div><b>7.17%</b></div>
              </div>
              <span class="chart-note">2025.12 各账号支付金额占比</span>
            </div>
            <div class="data-side">
              <button class="data-shot" type="button" data-lightbox-group="selfie-data" data-full="assets/img/ops/selfie/data-02-1800.webp" data-caption="2025 年 12 月店铺经营数据概览 / 后台截图" data-alt="2025 年 12 月店铺经营数据后台截图" data-w="1800" data-h="1080" data-cursor="OPEN">
                <img src="assets/img/ops/selfie/data-02-1800.webp" alt="2025 年 12 月店铺经营数据后台截图" width="1800" height="1080" loading="lazy" decoding="async">
                <span class="data-shot__caption"><span>SHOP DASHBOARD / 2025.12</span><b>打开原图 ↗</b></span>
              </button>
              <div class="data-extra">
                <span>DATA / 2025.12</span>
                <button type="button" data-lightbox-group="selfie-data" data-full="assets/img/ops/selfie/data-01-1800.webp" data-caption="2025 年 12 月账号成交拆分 / 后台截图" data-alt="2025 年 12 月各账号成交金额拆分后台截图" data-w="1800" data-h="1042">查看账号成交拆分 ↗</button>
              </div>
            </div>
          </div>
        </div>

        <div class="subsection">
          <div class="subsection__head">
            <div><p class="micro-label">05 / STORE &amp; DETAIL PAGES</p><h3>内容之外，<br>也在做货架。</h3></div>
            <p>负责 4 家 3C 数码店铺的商品上架、主图与详情页维护，参与笔记加热与推广素材优化。点击查看大图。</p>
          </div>
          <div class="product-grid">{products}</div>
          <div class="detail-row">{details}</div>
        </div>

        <blockquote class="case-quote">
          <p>“先让内容被看见，再让看见发生行动。”</p>
          <span>COMMERCE CONTENT / 2026</span>
        </blockquote>
        <p class="source-note">数据口径：项目任职期间为 2024.12—2026.06；店铺数据截图为 2025 年 12 月。笔记与店铺截图已做必要脱敏。</p>
      </div>
    </section>

    <section class="case case--lazy" id="lazy" aria-labelledby="lazy-title">
      <div class="container">
        <div class="case-label"><span>CASE 03 / DESIGN CONTENT</span><span>2023.05—2024.05</span></div>
        <div class="case-intro">
          <div>
            <p class="eyebrow">XIAOHONGSHU / 0 TO 1</p>
            <h2 id="lazy-title">从 0 到 1，<br>把审美变成流量。</h2>
          </div>
          <div class="case-intro__side">
            <p>围绕平面设计、IP 设计、包装设计与品牌视觉，独立搭建「懒羊羊素材库」，用设计案例内容连接店铺。</p>
            <dl class="role-list">
              <div><dt>角色</dt><dd>主理人 / 选题、排版、发布、复盘</dd></div>
              <div><dt>内容</dt><dd>平面 / IP / 包装 / 品牌视觉</dd></div>
              <div><dt>路径</dt><dd>内容种草 → 店铺引流</dd></div>
            </dl>
          </div>
        </div>

        <div class="ops-stats ops-stats--lazy">
          {ops_stat(3, '万+', '账号累计获赞与收藏', 'LIKES + SAVES')}
          {ops_stat(6, '', '高互动爆款笔记', 'SELECTED POSTS')}
          {ops_stat(1.7, '万+', '6 篇爆款合计赞藏', '17,476 TOTAL', 1)}
          {ops_stat(3645, '', '单篇最高获赞', 'TOP POST')}
        </div>

        <div class="lazy-intro-grid">
          <div class="lazy-copy">
            <p class="micro-label">THE START</p>
            <h3>先有审美判断，<br>再有内容方法。</h3>
            <p>从 0 到 1 独立搭建账号，聚焦平面设计、IP 设计、包装设计和品牌视觉四大方向。选题、图文排版、封面标题、发布与数据复盘，全链路自己完成。</p>
            <p>账号累计获赞与收藏 3 万+，其中 6 篇高互动笔记合计赞藏 1.7 万+，单篇最高获赞 3,645。</p>
          </div>
          <button class="lazy-account" type="button" data-lightbox-group="lazy-account" data-full="assets/img/ops/lazy/account-home-760.webp" data-caption="懒羊羊素材库 / 小红书主页" data-alt="懒羊羊素材库小红书账号主页截图" data-w="760" data-h="1651" data-cursor="OPEN">
            <img src="assets/img/ops/lazy/account-home-760.webp" alt="懒羊羊素材库小红书账号主页截图" width="760" height="1651" loading="lazy" decoding="async">
            <span>ACCOUNT HOME / 2024</span>
          </button>
        </div>

        <button class="lazy-board" type="button" data-lightbox-group="lazy-board" data-full="assets/img/ops/lazy/case-board-2000.webp" data-caption="懒羊羊素材库 / 内容案例板：6 篇高互动笔记与账号数据" data-alt="懒羊羊素材库内容案例板" data-w="2000" data-h="1125" data-cursor="OPEN">
          <img src="assets/img/ops/lazy/case-board-1000.webp" alt="懒羊羊素材库内容案例板，展示 6 篇高互动笔记与数据" width="2000" height="1125" loading="lazy" decoding="async">
          <span class="lazy-board__caption"><span>CASE BOARD / 6 POSTS</span><b>打开完整案例板 ↗</b></span>
        </button>

        <div class="lazy-feature-head">
          <p class="micro-label">SELECTED POSTS / REAL NUMBERS</p>
          <h3>六篇内容，<br>六种被收藏的理由。</h3>
          <p>以下是可公开的 6 篇高互动笔记。数据来自账号后台截图，赞藏合计 1.7 万+。</p>
        </div>
        <div class="lazy-post-grid">{lazy_posts}</div>

        <div class="case-process case-process--three">
          <article><span>01</span><h3>选题</h3><p>把设计作业、素材与案例，转译成用户想收藏的「灵感卡」。围绕毕业设计、海报、品牌、画册等具体需求策划内容。</p></article>
          <article><span>02</span><h3>表达</h3><p>用统一的排版、封面、标题与信息层级，让复杂设计内容更容易被扫读、保存和二次传播。</p></article>
          <article><span>03</span><h3>闭环</h3><p>在内容价值之外探索店铺入口，让「内容种草」不只停在点赞，也为后续转化建立自然路径。</p></article>
        </div>

        <blockquote class="case-quote">
          <p>“设计背景给我的，不只是审美，而是知道一张内容为什么值得被保存。”</p>
          <span>DESIGN CONTENT / 2024</span>
        </blockquote>
      </div>
    </section>

    <div class="ops-next">
      <div class="container">
        <p class="micro-label">NEXT / DESIGN ARCHIVE</p>
        <a href="design.html">去看设计作品 <span>↗</span></a>
        <p>四组 IP 与文创项目，45 张完整项目板。</p>
      </div>
    </div>
    <div hidden>{slide_triggers}</div>
'''
    return page(
        "运营案例｜钟菲 · 内容运营 / GEO",
        "钟菲的运营案例：GEO 内容增长、小红书 × 抖音电商内容、设计素材账号从 0 到 1。包含数据、方法与完整素材。",
        content,
        active="operations",
        body_class="page-operations",
        canonical_path="operations.html",
    )


# ---------------------------------------------------------------------------
# Design overview + project pages
# ---------------------------------------------------------------------------

def design_page():
    cards = ""
    for project in PROJECTS:
        cards += f'''
        <a class="design-card" href="design/{project['slug']}.html" data-cursor="OPEN">
          <div class="design-card__media">
            {card_cover_picture(project, project['title'] + "项目封面", sizes="(max-width: 800px) 90vw, 48vw", loading="lazy")}
            <span class="design-card__index">{project['index']} / 04</span>
            <span class="design-card__open">打开项目档案 <b>↗</b></span>
          </div>
          <div class="design-card__body">
            <div class="design-card__meta"><span>{project['year']} / {project['discipline']}</span><span>{project['award_short']}</span></div>
            <h2>{project['title']}</h2>
            <p>{project['summary']}</p>
            <span class="design-card__cta">查看项目板 <b>→</b></span>
          </div>
        </a>'''

    frames_spec = [
        ("gengong", 14, "无念熊 / IP 形象"),
        ("liangzhu", 12, "良渚 / 表情系统"),
        ("lingyin", 3, "灵隐 / 角色设计"),
        ("harbin", 2, "哈尔滨 / 角色设定"),
        ("gengong", 4, "根宫佛国 / 市场分析"),
        ("liangzhu", 14, "良渚 / 文创包装"),
        ("lingyin", 4, "灵隐 / 文创延展"),
        ("liangzhu", 3, "良渚 / 海报设计"),
    ]
    frames = ""
    for slug, n, label in frames_spec:
        project = PROJECT_BY_SLUG[slug]
        board = next(b for b in project["_board_data"] if b["n"] == n)
        frames += f'''<a class="frame-card" href="design/{slug}.html#board-{n:02d}" data-cursor="OPEN">
          <img src="{board_path(project, n, 640)}" srcset="{board_srcset(project, n)}" sizes="(max-width: 700px) 48vw, 24vw" alt="{project['title']}项目板 {n:02d}" width="{board['w']}" height="{board['h']}" loading="lazy" decoding="async">
          <span><b>{label}</b><i>BOARD {n:02d} ↗</i></span>
        </a>'''

    content = f'''
    <section class="design-intro" aria-labelledby="design-page-title">
      <div class="container">
        <div class="intro-topline">
          <p class="micro-label">DESIGN / SELECTED WORKS</p>
          <p class="micro-label">2024—2025 / 04 PROJECTS</p>
        </div>
        <h1 id="design-page-title">文化，<br><span class="accent">可以被带走。</span></h1>
        <div class="design-intro__bottom">
          <p>四组 IP 与文创项目，从城市文化、景区、寺院到博物馆。用调研找到文化母题，用视觉把它变成角色、产品和场景。</p>
          <div class="design-counts">
            <div><strong>04</strong><span>组项目</span></div>
            <div><strong>45</strong><span>张项目板</span></div>
            <div><strong>02</strong><span>项全国奖项</span></div>
          </div>
        </div>
      </div>
    </section>

    <section class="design-grid-section" aria-label="设计项目列表">
      <div class="container">
        <div class="design-grid">{cards}</div>
      </div>
    </section>

    <section class="frames-section" aria-labelledby="frames-title">
      <div class="container">
        <div class="frames-head">
          <div><p class="micro-label">SELECTED FRAMES / 08</p><h2 id="frames-title">从调研到落地，<br>每一张都有来处。</h2></div>
          <p>项目板里不只有成品，也有市场分析、问卷、设计推演、三视图与场景应用。点击任意一张，进入它所在的项目档案。</p>
        </div>
        <div class="frames-grid">{frames}</div>
      </div>
    </section>

    <section class="design-note" aria-labelledby="design-note-title">
      <div class="container design-note__grid">
        <p class="micro-label">DESIGN NOTE / 2026</p>
        <div>
          <h2 id="design-note-title">设计不是给内容加装饰，<br>而是给信息建立秩序。</h2>
          <div class="design-principles">
            <div><span>01</span><h3>先理解文化</h3><p>不从符号开始，而从场域、人群与使用场景开始。角色要能解释文化，而不只是像某种文化。</p></div>
            <div><span>02</span><h3>再建立系统</h3><p>一个角色需要三视图、表情、色彩与应用规则。能延展，才算真正成立。</p></div>
            <div><span>03</span><h3>最后回到人</h3><p>文创不是把图案印在物件上，而是让人愿意带走、使用、分享。</p></div>
          </div>
        </div>
      </div>
    </section>

    <div class="cross-next">
      <div class="container">
        <p class="micro-label">NEXT / OPERATIONS</p>
        <a href="operations.html"><span class="cross-next__text">看完设计，<br>再看我如何把内容做成增长</span><span class="cross-next__arrow" aria-hidden="true">↗</span></a>
      </div>
    </div>
'''
    return page(
        "设计作品｜钟菲 · IP 文创与视觉设计",
        "钟菲的设计作品：哈尔滨城市 IP、根宫佛国文创、灵隐万象集、良渚博物院 IP。45 张完整项目板。",
        content,
        active="design",
        body_class="page-design",
        canonical_path="design.html",
    )


def project_page(project):
    idx = PROJECTS.index(project)
    next_project = PROJECTS[(idx + 1) % len(PROJECTS)]
    total = len(project["_board_data"])

    pages_html = ""
    for n in range(1, total + 1):
        board = next(b for b in project["_board_data"] if b["n"] == n)
        is_cover = n == project["cover"]
        is_portrait = board["h"] > board["w"]
        page_cls = " pdf-page--portrait" if is_portrait else ""
        sizes = "(max-width: 900px) 100vw, 715px" if is_portrait else "(max-width: 900px) 100vw, 1080px"
        pic = design_picture(
            project, n, f"{project['title']}项目板 {n:02d}", base="../",
            sizes=sizes, loading="eager" if n == 1 else "lazy",
            cls="pdf-page__img", fetchpriority="high" if n == 1 else None,
        )
        full = "../" + board["variants"][str(max(int(w) for w in board["variants"]))]
        page_button = lightbox_button(
            f'<span class="pdf-page__frame">{pic}</span>',
            f"project-{project['slug']}",
            full,
            f"{project['title']} / 项目板 {n:02d}",
            f"{project['title']}项目板 {n:02d}",
            cls="pdf-page__open",
        )
        page_label = "COVER / 封面" if is_cover else "BOARD / 项目板"
        pages_html += f'''
        <article class="pdf-page{page_cls}" id="board-{n:02d}">
          <h2 class="visually-hidden">PAGE {n:02d} / {total:02d} · {page_label}</h2>
          <div class="pdf-page__bar"><span>PAGE {n:02d} / {total:02d}</span><span>{page_label}</span></div>
          {page_button}
        </article>'''

    if next_project.get("card_cover"):
        next_card = next_project["card_cover"]
        next_cover = next_card["src"]
        next_srcset = ", ".join(f'../{url} {w}w' for url, w in next_card["srcset"])
        next_w, next_h = next_card["w"], next_card["h"]
    else:
        next_cover = board_path(next_project, next_project["cover"], 640)
        next_srcset = board_srcset(next_project, next_project["cover"], base="../")
        next_board = next_project["_board_data"][next_project["cover"] - 1]
        next_w, next_h = next_board["w"], next_board["h"]
    if project["award"]:
        award_label = "AWARD / 奖项"
        award_value = f'<span class="project-award">{project["award"]}</span>'
    else:
        award_label = "PROJECT / 类型"
        award_value = f'<span class="project-award project-award--type">{project["type"]}</span>'

    content = f'''
    <article class="project-page">
      <header class="project-hero">
        <div class="container">
          <div class="project-topline">
            <a href="../design.html">← 设计档案</a>
            <span>PROJECT {project['index']} / 04</span>
            <span>{project['year']}</span>
          </div>
          <div class="project-heading">
            <p class="eyebrow">{project['title_en']}</p>
            <h1>{project['title']}</h1>
            <p class="project-summary">{project['summary']}</p>
            <p class="project-intro-text">{project['intro']}</p>
            <div class="project-tags"><span>{project['discipline']}</span><span>{project['type']}</span><span>{project['award_short']}</span></div>
          </div>
          <div class="project-meta">
            <div class="project-meta__award"><span class="micro-label">{award_label}</span>{award_value}</div>
            <dl>
              <div><dt>年份</dt><dd>{project['year']}</dd></div>
              <div><dt>角色</dt><dd>{project['role']}</dd></div>
              <div><dt>类型</dt><dd>{project['type']}</dd></div>
              <div><dt>页数</dt><dd>{total} 页</dd></div>
            </dl>
          </div>
        </div>
      </header>

      <section class="project-reader" aria-label="完整项目板">
        <div class="container">
          <div class="project-reader__head">
            <p class="micro-label">PROJECT DOCUMENT / {total:02d} PAGES</p>
            <p>按原始顺序浏览 · 点击任意页放大</p>
          </div>
          <div class="pdf-stack">{pages_html}</div>
        </div>
      </section>

      <nav class="project-next" aria-label="下一个项目">
        <a href="{next_project['slug']}.html" data-cursor="NEXT">
          <div class="project-next__copy">
            <p class="micro-label">NEXT PROJECT / {next_project['index']}</p>
            <span class="project-next__title">{next_project['title']}</span>
            <span class="project-next__cta">继续浏览 <b>↗</b></span>
          </div>
          <div class="project-next__media"><img src="../{next_cover}" srcset="{next_srcset}" sizes="34vw" alt="{next_project['title']}项目封面" width="{next_w}" height="{next_h}" loading="lazy" decoding="async"></div>
        </a>
      </nav>
    </article>
'''
    return page(
        f"{project['title']}｜钟菲设计作品",
        project["summary"] + " " + project["intro"],
        content,
        active="design",
        base="../",
        body_class="page-design-detail",
        canonical_path=f"design/{project['slug']}.html",
    )


# ---------------------------------------------------------------------------
# About page
# ---------------------------------------------------------------------------

def about_page():
    experience = [
        ("2026.07—至今", "海康威视", "AI 搜索内容运营（GEO）",
         "负责豆包、千问、DeepSeek、元宝等 AI 平台的 GEO 内容策略与执行；搭建并运营 50+ 账号矩阵，沉淀 GEO 素材库、问答库、选题库、Prompt 模板与生产 SOP；围绕 36 个核心提示词产出 800+ 篇结构化内容，按项目统计口径 260+ 篇被 AI 平台召回、累计召回 2,000+ 次，核心提示词覆盖率达 90%。",
         ["50+ 矩阵账号", "800+ 结构化内容", "2,000+ 次 AI 召回"]),
        ("2024.12—2026.06", "杭州红商电子商务有限公司", "内容与店铺运营",
         "独立搭建并运营小红书矩阵及抖音账号「自拍杆小圆子」，负责账号定位、选题、图文、视频拍剪与日常维护；负责 4 家 3C 数码店铺商品上架、主图与详情页维护、笔记加热及推广优化，跟踪曝光、点击、进店与成交表现。",
         ["30+ 篇爆文", "3万+ 累计订单", "最高月 GMV 27.4万"]),
    ]
    exp_html = "".join(f'''
        <article class="timeline-item">
          <div class="timeline-item__date">{date}</div>
          <div class="timeline-item__body">
            <p class="timeline-item__company">{company}</p>
            <h3>{role}</h3>
            <p>{desc}</p>
            <ul>{"".join(f"<li>{tag}</li>" for tag in tags)}</ul>
          </div>
        </article>''' for date, company, role, desc, tags in experience)

    capabilities = [
        ("内容策略", "选题策划 / 关键词布局 / 内容矩阵 / 内容 SOP", "从用户问题出发，建立可复用的内容结构。"),
        ("平台运营", "小红书 / 抖音 / 账号定位 / 内容复盘", "理解平台语境，也理解内容如何被消费。"),
        ("GEO & AI", "AI 搜索引用 / Prompt / 结构化内容", "让品牌信息成为 AI 可以理解、调用和推荐的知识。"),
        ("视觉表达", "Photoshop / Illustrator / 剪映 / Midjourney / Stable Diffusion", "设计学训练带来的审美判断与执行能力。"),
        ("数据复盘", "曝光 / CTR / 互动 / 进店 / 成交 / AI 引用", "用数据验证判断，再决定下一轮做什么。"),
    ]
    caps_html = "".join(f'''
        <article class="capability">
          <span class="capability__index">{i:02d}</span>
          <div><h3>{title}</h3><p>{desc}</p><span>{tools}</span></div>
        </article>''' for i, (title, tools, desc) in enumerate(capabilities, 1))

    awards = [
        ("2025", "第三届中国研究生「美丽中国」创新设计大赛", "全国二等奖"),
        ("2024", "第五届全国会展策划创意大赛", "全国三等奖"),
        ("2024", "浙江省第十四届会展策划创意大赛", "省级一等奖"),
        ("2024", "ICCC 国际学生设计大赛", "全国二等奖"),
        ("2024", "两岸青年非遗文创设计大赛", "一等奖"),
        ("2023", "澳门文创设计大赛", "全国一等奖"),
    ]
    awards_html = "".join(f'''<li><span>{year}</span><p>{name}</p><b>{award}</b></li>''' for year, name, award in awards)

    jsonld = '''<script type="application/ld+json">{"@context":"https://schema.org","@type":"Person","name":"钟菲","alternateName":"ZHONG FEI","jobTitle":"内容运营 / GEO 内容运营","email":"mailto:Aria.zhong@outlook.com","url":"https://feizhong278-ui.github.io/personal-web/","alumniOf":{"@type":"CollegeOrUniversity","name":"中国计量大学"},"knowsAbout":["内容运营","GEO","AI 搜索","小红书","抖音","视觉设计","IP 设计"]}</script>'''

    content = f'''
    <section class="about-hero-page" aria-labelledby="about-page-title">
      <div class="container about-hero-page__grid">
        <div class="about-hero-page__copy">
          <div class="intro-topline">
            <p class="micro-label">ABOUT / ZHONG FEI</p>
            <p class="micro-label">HANGZHOU / 2027</p>
          </div>
          <h1 id="about-page-title">用设计的眼睛，<br>看内容的问题。</h1>
          <p class="about-hero-page__lead">我是钟菲，设计学硕士，2027 届。正在寻找内容运营、GEO 内容运营与 AI 内容运营的机会。</p>
          <div class="about-hero-page__actions">
            {cta_link('mailto:Aria.zhong@outlook.com', '发一封邮件', 'btn btn--dark', '↗')}
            <a class="text-link" href="assets/docs/zhongfei-resume.pdf?v=20261021f" download>下载简历 PDF <span>↓</span></a>
          </div>
          <div class="about-now">
            <p class="micro-label">NOW / 现在</p>
            <dl>
              <div><dt>状态</dt><dd><i></i> 2027 届 · 求职中</dd></div>
              <div><dt>地点</dt><dd>杭州 · 可接受江浙沪机会</dd></div>
              <div><dt>方向</dt><dd>内容运营 / GEO / AI 内容</dd></div>
            </dl>
          </div>
        </div>
        <figure class="about-page-photo">
          <div class="about-page-photo__frame">
            <img src="assets/img/portrait-900.webp" srcset="assets/img/portrait-480.webp 480w, assets/img/portrait-720.webp 720w, assets/img/portrait-900.webp 900w" sizes="(max-width: 700px) 92vw, 520px" alt="钟菲的职业肖像" width="900" height="1199" loading="eager" fetchpriority="high" decoding="async">
          </div>
          <span class="about-page-photo__stamp">OPEN<br>TO<br>WORK</span>
          <figcaption><span>ZHONG FEI / 钟菲</span><span>PORTRAIT 2026</span></figcaption>
        </figure>
      </div>
    </section>

    <section class="about-statement">
      <div class="container about-statement__grid">
        <h2 class="visually-hidden">关于我</h2>
        <p class="micro-label">01 / THE SHORT VERSION</p>
        <div>
          <p class="about-statement__lead">我在中国计量大学读了七年设计，从视觉传达走到设计学。设计训练给我的，不只是软件和审美，更是一套观察、拆解、表达、验证问题的方法。</p>
          <div class="about-statement__cols">
            <p>真正进入内容运营后，我发现这套方法同样适用：看用户的问题、拆内容的变量、做可复用的系统、用数据验证判断。设计让我对细节敏感，运营让我对结果负责。</p>
            <p>我喜欢把模糊的问题变成清晰的结构，也喜欢把结构做得好看。比起「发更多」，我更在意每一次发布是否留下了可复用的资产。</p>
          </div>
        </div>
      </div>
    </section>

    <section class="experience-section" aria-labelledby="experience-title">
      <div class="container">
        {section_head('02', 'EXPERIENCE', '做过的事，<br>都留下了数字。', '从 AI 搜索到电商内容，两段实习经历都同时包含策略、执行与复盘。')}
        <div class="timeline">{exp_html}</div>
      </div>
    </section>

    <section class="education-section" aria-labelledby="education-title">
      <div class="container education-grid">
        <div>
          <p class="micro-label">03 / EDUCATION</p>
          <h2 id="education-title">设计学硕士，<br>视觉传达本科。</h2>
          <div class="edu-list">
            <article><span>2024.09—2027.06</span><h3>中国计量大学 · 设计学硕士</h3><p>全日制 / GPA 3.93 / 4.0 / 专业前 3%</p></article>
            <article><span>2020.09—2024.06</span><h3>中国计量大学 · 视觉传达本科</h3><p>全日制 / GPA 3.9 / 4.0 / 专业前 3%</p></article>
          </div>
        </div>
        <div class="awards-block">
          <p class="micro-label">AWARDS / 奖项</p>
          <ul>{awards_html}</ul>
        </div>
      </div>
    </section>

    <section class="capabilities-section" aria-labelledby="capabilities-title">
      <div class="container">
        {section_head('04', 'CAPABILITIES', '内容、AI 与设计，<br>交叉的地方。', '不是工具清单，而是我能把一件事从想法推进到结果的能力范围。')}
        <div class="capability-grid">{caps_html}</div>
      </div>
    </section>

    <section class="principles" aria-labelledby="principles-title">
      <div class="container">
        <p class="micro-label">05 / PRINCIPLES</p>
        <h2 id="principles-title">我带着这三句话<br>做内容。</h2>
        <div class="principle-grid">
          <div><span>01</span><p>先问对问题，<br>再开始生产。</p><small>洞察先于执行</small></div>
          <div><span>02</span><p>审美不是装饰，<br>是信息的秩序。</p><small>设计先于美化</small></div>
          <div><span>03</span><p>数据不是终点，<br>是下一轮的起点。</p><small>复盘先于结论</small></div>
        </div>
      </div>
    </section>

    <section class="contact contact--about" id="contact" aria-labelledby="contact-title">
      <div class="container contact__inner">
        <div class="contact__meta"><p class="micro-label">06 / CONTACT</p><p>OPEN FOR CONVERSATION</p></div>
        <h2 id="contact-title">下一段好内容，<br><em>一起做。</em></h2>
        <div class="contact__bottom">
          <p>如果你正在找一位懂内容、也懂视觉的内容运营，欢迎直接把机会发给我。</p>
          <div class="contact__actions">
            <button class="email-copy" type="button" data-copy-email="Aria.zhong@outlook.com"><span>Aria.zhong@outlook.com</span><span class="email-copy__action">复制邮箱</span></button>
            <a class="contact__mailto" href="mailto:Aria.zhong@outlook.com">或直接写信 ↗</a>
            <a class="contact__resume" href="assets/docs/zhongfei-resume.pdf?v=20261021f" download>下载简历 PDF <span>↓</span></a>
          </div>
        </div>
        <div class="contact__stamp" aria-hidden="true"><span>AVAILABLE FOR WORK</span><b>2027</b><span>HANGZHOU · CN</span></div>
      </div>
    </section>
'''
    return page(
        "关于我｜钟菲 · 内容运营 / GEO",
        "钟菲，设计学硕士，2027 届。内容运营 / GEO 内容运营 / AI 内容运营求职者，具备小红书、抖音、AI 搜索与视觉设计经验。",
        content,
        active="about",
        body_class="page-about",
        canonical_path="about.html",
        jsonld=jsonld,
    )


def not_found_page():
    import base64
    site = "https://feizhong278-ui.github.io/personal-web/"
    avatar = base64.b64encode((ROOT / "assets/img/portrait-160.webp").read_bytes()).decode("ascii")
    css = '''
    @font-face { font-family: "PH"; src: url("__SITE__assets/fonts/alibaba-puhuiti-heavy.woff2") format("woff2"); font-weight: 700 900; font-style: normal; font-display: swap; }
    * { box-sizing: border-box; }
    html, body { margin: 0; min-height: 100%; }
    body {
      min-height: 100svh;
      color: #27231f;
      background:
        radial-gradient(circle at 7% 4%, rgba(255, 211, 193, .88), transparent 27%),
        radial-gradient(circle at 94% 3%, rgba(209, 241, 230, .92), transparent 31%),
        radial-gradient(circle at 90% 72%, rgba(226, 215, 247, .7), transparent 33%),
        linear-gradient(118deg, #fdf4ef, #fbfaf6 46%, #f6f7fb 74%, #f1faf5);
      font-family: "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
      -webkit-font-smoothing: antialiased;
    }
    a { color: inherit; }
    .wrap { display: flex; width: min(calc(100% - 32px), 1220px); min-height: 100svh; flex-direction: column; margin: auto; padding: 14px 0 22px; }
    .nav { display: flex; align-items: center; justify-content: space-between; gap: 14px; padding: 8px 10px 8px 12px; border: 1px solid rgba(255,255,255,.94); border-radius: 999px; background: rgba(255,255,255,.7); box-shadow: 0 12px 36px rgba(102,79,60,.08); backdrop-filter: blur(20px); }
    .brand { display: inline-flex; align-items: center; gap: 10px; color: #27231f; text-decoration: none; }
    .brand img { width: 37px; height: 37px; border: 2px solid #fff; border-radius: 50%; object-fit: cover; object-position: center 23%; box-shadow: 0 4px 12px rgba(93,69,52,.14); }
    .brand span { display: flex; flex-direction: column; font-family: "PH", sans-serif; font-size: 12px; font-weight: 900; letter-spacing: .08em; line-height: 1; }
    .brand small { margin-top: 5px; color: #6f665d; font-family: "PingFang SC", sans-serif; font-size: 7px; font-weight: 400; letter-spacing: .04em; }
    .back { padding: 9px 14px; border: 1px solid rgba(60,48,38,.16); border-radius: 999px; color: #27231f; background: rgba(255,255,255,.5); font-size: 10px; text-decoration: none; }
    .back:hover { color: #fff; background: #27231f; }
    main { display: flex; flex: 1; align-items: center; padding: 24px 0; }
    .card { position: relative; width: 100%; overflow: hidden; padding: clamp(25px, 5.4vw, 68px); border: 1px solid rgba(255,255,255,.84); border-radius: 42px; background: rgba(255,255,255,.55); box-shadow: 0 28px 70px rgba(105,82,61,.09); backdrop-filter: blur(18px); }
    .kicker { margin: 0 0 16px; color: #8b6047; font-family: "SFMono-Regular", Menlo, Consolas, monospace; font-size: 9px; letter-spacing: .12em; }
    h1 { position: relative; z-index: 2; margin: 0; font-family: "PH", "PingFang SC", sans-serif; font-size: clamp(4.4rem, 11.5vw, 10.8rem); font-weight: 900; letter-spacing: -.075em; line-height: .93; }
    .copy { position: relative; z-index: 2; max-width: 430px; margin: 26px 0 0; color: #5e554c; font-size: 12px; line-height: 1.9; }
    .actions { position: relative; z-index: 2; display: flex; flex-wrap: wrap; gap: 12px 20px; align-items: center; margin-top: 28px; }
    .btn { display: inline-flex; align-items: center; gap: 15px; min-height: 45px; padding: 10px 17px; border: 1px solid #27231f; border-radius: 999px; color: #fff; background: #27231f; font-size: 10px; text-decoration: none; }
    .btn b { color: #ffd2c1; font-size: 12px; font-weight: 400; }
    .link { padding-bottom: 3px; border-bottom: 1px solid rgba(69,56,43,.3); color: #5e554c; font-size: 10px; text-decoration: none; }
    .link:hover { color: #a94f39; border-color: #a94f39; }
    .note { position: relative; z-index: 2; margin: 44px 0 0; color: #6f665d; font-family: "SFMono-Regular", Menlo, Consolas, monospace; font-size: 7px; letter-spacing: .03em; }
    .ghost { position: absolute; right: -2%; bottom: -16%; z-index: 0; color: rgba(255,255,255,.6); font-family: "PH", sans-serif; font-size: clamp(14rem, 38vw, 35rem); font-weight: 900; letter-spacing: -.1em; line-height: .7; pointer-events: none; }
    .flower { position: absolute; top: 44px; right: 6%; z-index: 1; width: clamp(80px, 10vw, 130px); filter: drop-shadow(0 8px 12px rgba(107,90,122,.16)); transform: rotate(9deg); }
    footer { display: flex; flex-wrap: wrap; justify-content: space-between; gap: 7px 18px; padding: 15px 7px 0; border-top: 1px solid rgba(69,56,43,.14); color: #6f665d; font-family: "SFMono-Regular", Menlo, Consolas, monospace; font-size: 6px; }
    footer a { text-decoration: none; }
    footer b { color: #8a5f47; font-weight: 400; }
    @media (max-width: 600px) {
      .wrap { width: min(calc(100% - 20px), 1220px); padding-top: 9px; }
      .nav { padding: 6px 7px 6px 8px; }
      .brand img { width: 34px; height: 34px; }
      .back { padding: 8px 10px; font-size: 8px; }
      main { padding: 15px 0; }
      .card { padding: 24px 18px 26px; border-radius: 29px; }
      .copy { font-size: 11px; }
      h1 { font-size: clamp(4rem, 21vw, 6rem); }
      .flower { top: 25px; right: 6%; width: 78px; }
      .ghost { right: -15%; bottom: -4%; font-size: 18rem; }
      .note { margin-top: 31px; }
      footer { flex-direction: column; font-size: 5.5px; }
    }
    '''
    css = css.replace("__SITE__", site)
    return f'''<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#fbf8f4">
  <title>页面不存在｜钟菲作品集</title>
  <meta name="description" content="这个页面不存在。回到钟菲的作品集首页，浏览内容运营、GEO 与设计作品。">
  <meta name="robots" content="noindex">
  <link rel="canonical" href="{site}404.html">
  <link rel="icon" href="{site}assets/favicon.png" type="image/png" sizes="64x64">
  <link rel="apple-touch-icon" href="{site}assets/img/apple-touch-icon.png">
  <style>{css}</style>
</head>
<body>
  <div class="wrap">
    <header class="nav">
      <a class="brand" href="{site}" aria-label="钟菲作品集首页">
        <img src="data:image/webp;base64,{avatar}" alt="" width="160" height="213">
        <span>PORTFOLIO<small>钟菲 / 2027</small></span>
      </a>
      <a class="back" href="{site}">返回首页 ↗</a>
    </header>
    <main>
      <div class="card">
        <p class="kicker">ERROR / 404 / PAGE NOT FOUND</p>
        <h1>走丢了。</h1>
        <p class="copy">这个页面不存在，或者已经被移走。但好内容和好机会，都不该在这里停下。</p>
        <div class="actions">
          <a class="btn" href="{site}">回到首页 <b>↗</b></a>
          <a class="link" href="{site}operations.html">浏览运营案例 →</a>
          <a class="link" href="{site}design.html">浏览设计作品 →</a>
        </div>
        <p class="note">页面走丢了，机会没有。 · Aria.zhong@outlook.com</p>
        <span class="ghost" aria-hidden="true">404</span>
        <svg class="flower" viewBox="0 0 160 160" aria-hidden="true">
          <defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#d8f3ff"></stop><stop offset=".52" stop-color="#d8d1ff"></stop><stop offset="1" stop-color="#ffd8e6"></stop></linearGradient></defs>
          <g transform="rotate(-8 80 80)">
            <ellipse cx="80" cy="40" rx="23" ry="30" fill="url(#g)" stroke="#fff" stroke-width="3"></ellipse>
            <ellipse cx="80" cy="40" rx="23" ry="30" fill="url(#g)" stroke="#fff" stroke-width="3" transform="rotate(60 80 80)"></ellipse>
            <ellipse cx="80" cy="40" rx="23" ry="30" fill="url(#g)" stroke="#fff" stroke-width="3" transform="rotate(120 80 80)"></ellipse>
            <ellipse cx="80" cy="40" rx="23" ry="30" fill="url(#g)" stroke="#fff" stroke-width="3" transform="rotate(180 80 80)"></ellipse>
            <ellipse cx="80" cy="40" rx="23" ry="30" fill="url(#g)" stroke="#fff" stroke-width="3" transform="rotate(240 80 80)"></ellipse>
            <ellipse cx="80" cy="40" rx="23" ry="30" fill="url(#g)" stroke="#fff" stroke-width="3" transform="rotate(300 80 80)"></ellipse>
            <circle cx="80" cy="80" r="31" fill="#fff9fd" stroke="#fff" stroke-width="3"></circle>
            <circle cx="70" cy="76" r="3.4" fill="#39332f"></circle><circle cx="90" cy="76" r="3.4" fill="#39332f"></circle>
            <path d="M70 88 Q80 96 90 88" fill="none" stroke="#39332f" stroke-width="3" stroke-linecap="round"></path>
            <ellipse cx="63" cy="86" rx="6" ry="3" fill="#ffafc4" opacity=".55"></ellipse><ellipse cx="97" cy="86" rx="6" ry="3" fill="#ffafc4" opacity=".55"></ellipse>
          </g>
        </svg>
      </div>
    </main>
    <footer>
      <span>© 2026 钟菲 / CONTENT OPERATIONS</span>
      <span>杭州 · 中国 <b>HANGZHOU / CN</b></span>
    </footer>
  </div>
</body>
</html>'''


# ---------------------------------------------------------------------------
# Operations index + standalone case pages
# ---------------------------------------------------------------------------

CASE_META = {
    "geo": {"num": "01", "title": "GEO 内容增长", "date": "2026.07—至今", "next": "selfie"},
    "selfie": {"num": "02", "title": "自拍杆小圆子", "date": "2024.12—2026.06", "next": "lazy"},
    "lazy": {"num": "03", "title": "懒羊羊素材库", "date": "2023.05—2024.05", "next": "geo"},
}


def ops_case_nav(active):
    links = []
    for key, meta in CASE_META.items():
        cls = ' class="is-active"' if key == active else ""
        current = ' aria-current="page"' if key == active else ""
        links.append(f'<a href="case-{key}.html"{cls}{current}><span>{meta["num"]}</span> {meta["title"]}</a>')
    return f'''
    <nav class="case-nav case-nav--pages" aria-label="案例切换">
      <div class="container case-nav__inner">
        <span class="case-nav__label">OPERATIONS / 03 CASES</span>
        <div class="case-nav__links">{"".join(links)}</div>
        <a class="case-nav__top" href="operations.html">全部案例 ↗</a>
      </div>
    </nav>'''


def extract_case_section(full_html, key):
    marker = f'<section class="case case--{key}"'
    start = full_html.index(marker)
    end = full_html.index("</section>", start) + len("</section>")
    return full_html[start:end]


def extract_slide_triggers(full_html):
    import re
    match = re.search(r"<div hidden>(.*?)</div>", full_html, re.S)
    return match.group(1) if match else ""


def case_page(key, full_html):
    meta = CASE_META[key]
    section = extract_case_section(full_html, key)
    hidden = ""
    if key == "selfie":
        hidden = f'<div hidden>{extract_slide_triggers(full_html)}</div>'
    nxt = CASE_META[meta["next"]]
    next_block = f'''
    <nav class="case-next-case" aria-label="下一个案例">
      <div class="container">
        <p class="micro-label">NEXT CASE / {nxt['num']}</p>
        <a href="case-{meta['next']}.html"><span>{nxt['title']}</span><b>继续浏览 ↗</b></a>
        <a class="case-next-case__all" href="operations.html">← 返回全部运营案例</a>
      </div>
    </nav>'''
    content = f'''
    <h1 class="visually-hidden">{meta["title"]}｜运营案例</h1>
    {ops_case_nav(key)}
    {section}
    {hidden}
    {next_block}
'''
    return page(
        f"{meta['title']}｜钟菲运营案例",
        f"钟菲的运营案例：{meta['title']}。包含项目背景、方法、数据与完整素材。",
        content,
        active="operations",
        body_class="page-case",
        canonical_path=f"case-{key}.html",
    )


def operations_overview_page():
    geo_card = '''
      <a class="ops-teaser ops-teaser--geo" href="case-geo.html" data-cursor="OPEN CASE">
        <div class="ops-teaser__copy">
          <div class="ops-teaser__top"><span>CASE 01 / GEO</span><span>2026.07—至今</span></div>
          <h2>让品牌，<br>进入 AI 的答案。</h2>
          <p>从 36 个核心提示词出发，搭建 50+ 账号内容矩阵，让品牌在生成式搜索中被看见、被引用、被推荐。</p>
          <div class="ops-teaser__stats">
            <div><strong>50<sup>+</sup></strong><span>矩阵账号</span></div>
            <div><strong>800<sup>+</sup></strong><span>结构化内容</span></div>
            <div><strong>2,000<sup>+</sup></strong><span>AI 召回</span></div>
          </div>
          <span class="ops-teaser__cta">查看完整案例 <b>↗</b></span>
        </div>
        <div class="ops-teaser__visual">
          <div class="mini-console mini-console--teaser">
            <div class="mini-console__head"><span><i></i> GEO / VISIBILITY</span><span>2026.10</span></div>
            <div class="mini-console__row">
              <div><span>品牌提及率</span><b>44.53 <em>→</em> 63.46<small>%</small></b></div>
              <div class="mini-bars"><i style="--w:44.53%"></i><i style="--w:63.46%"></i></div>
            </div>
            <div class="mini-console__row">
              <div><span>品牌推荐率</span><b>25.36 <em>→</em> 46.15<small>%</small></b></div>
              <div class="mini-bars mini-bars--lime"><i style="--w:25.36%"></i><i style="--w:46.15%"></i></div>
            </div>
            <div class="mini-console__foot"><span>90% COVERAGE</span><span>260+ RECALLED</span></div>
          </div>
        </div>
      </a>'''

    selfie_card = '''
      <a class="ops-teaser ops-teaser--selfie" href="case-selfie.html" data-cursor="OPEN CASE">
        <div class="ops-teaser__collage" aria-hidden="true">
          <img src="assets/img/ops/selfie/note-09-600.webp" alt="" width="600" height="460" loading="lazy" decoding="async">
          <img src="assets/img/ops/selfie/note-04-600.webp" alt="" width="600" height="465" loading="lazy" decoding="async">
          <img src="assets/img/ops/selfie/note-10-600.webp" alt="" width="600" height="460" loading="lazy" decoding="async">
          <span>14 NOTES / 4 ACCOUNTS</span>
        </div>
        <div class="ops-teaser__copy">
          <div class="ops-teaser__top"><span>CASE 02 / COMMERCE</span><span>2024.12—2026.06</span></div>
          <h2>把种草，<br>做成生意。</h2>
          <p>从账号定位、拍剪、标题封面，到商品页与成交复盘，跑通一条内容到生意的完整链路。</p>
          <div class="ops-teaser__stats">
            <div><strong>30<sup>+</sup></strong><span>爆文笔记</span></div>
            <div><strong>3<sup>万+</sup></strong><span>累计订单</span></div>
            <div><strong>27.4<sup>万</sup></strong><span>最高月 GMV</span></div>
          </div>
          <span class="ops-teaser__cta">查看完整案例 <b>↗</b></span>
        </div>
      </a>'''

    lazy_card = '''
      <a class="ops-teaser ops-teaser--lazy" href="case-lazy.html" data-cursor="OPEN CASE">
        <div class="ops-teaser__copy">
          <div class="ops-teaser__top"><span>CASE 03 / DESIGN CONTENT</span><span>2023.05—2024.05</span></div>
          <h2>让审美，<br>成为流量。</h2>
          <p>围绕平面设计、IP、包装与品牌视觉，从 0 到 1 搭建「懒羊羊素材库」，用设计内容连接店铺。</p>
          <div class="ops-teaser__stats">
            <div><strong>3<sup>万+</sup></strong><span>累计赞藏</span></div>
            <div><strong>6</strong><span>篇爆款</span></div>
            <div><strong>1.7<sup>万+</sup></strong><span>爆款赞藏</span></div>
          </div>
          <span class="ops-teaser__cta">查看完整案例 <b>↗</b></span>
        </div>
        <div class="ops-teaser__visual ops-teaser__visual--board">
          <img src="assets/img/ops/lazy/case-board-1000.webp" alt="懒羊羊素材库内容案例板" width="1000" height="562" loading="lazy" decoding="async">
        </div>
      </a>'''

    content = f'''
    <section class="page-intro ops-intro" aria-labelledby="ops-title">
      <div class="container">
        <div class="intro-topline">
          <p class="micro-label">OPERATIONS / 2024—NOW</p>
          <p class="micro-label">03 CASES / 01 METHOD</p>
        </div>
        <h1 id="ops-title">把注意力，<br><span class="accent">变成结果。</span></h1>
        <div class="intro-bottom">
          <p>三个项目，三种内容能力：在 AI 搜索里建立品牌可见度，在电商场景里完成内容到成交，在设计分享里从 0 到 1 建立账号。</p>
          <div class="ops-index">
            <a href="case-geo.html"><span>01</span><strong>GEO 内容增长</strong><small>AI 搜索 / 50+ 内容矩阵</small><b>↗</b></a>
            <a href="case-selfie.html"><span>02</span><strong>自拍杆小圆子</strong><small>小红书 × 抖音 / 店铺转化</small><b>↗</b></a>
            <a href="case-lazy.html"><span>03</span><strong>懒羊羊素材库</strong><small>设计内容 / 0 到 1</small><b>↗</b></a>
          </div>
        </div>
      </div>
    </section>
    <section class="case-files" aria-labelledby="case-files-title">
      <div class="container">
        <div class="case-files__head">
          <p class="micro-label">CASE FILES / 03</p>
          <h2 id="case-files-title">每一页，<br>都是一条增长路径。</h2>
          <p>点开任意案例，查看背景、方法、数据与完整素材。长内容在独立页面展开，建议先看结果，再进入过程。</p>
        </div>
        <div class="ops-teasers">{geo_card}{selfie_card}{lazy_card}</div>
      </div>
    </section>
    <section class="case-method" aria-labelledby="case-method-title">
      <div class="container">
        <p class="micro-label">WHAT STAYS CONSTANT / 我的工作方式</p>
        <h2 id="case-method-title">问题不同，<br>方法可以复用。</h2>
        <div class="case-method__grid">
          <article><span>01</span><h3>先理解人</h3><p>搜索词、评论、使用场景与购买犹豫，先找到真实的问题。</p></article>
          <article><span>02</span><h3>再做结构</h3><p>把问题拆成选题、内容、账号与转化路径，让每一环有明确任务。</p></article>
          <article><span>03</span><h3>最后复盘</h3><p>用曝光、互动、进店、成交和 AI 引用，决定下一轮把资源放在哪里。</p></article>
        </div>
      </div>
    </section>
    <div class="ops-next">
      <div class="container">
        <p class="micro-label">NEXT / DESIGN ARCHIVE</p>
        <a href="design.html">去看设计作品 <span>↗</span></a>
        <p>四组 IP 与文创项目，45 张完整项目板。</p>
      </div>
    </div>
'''
    return page(
        "运营案例｜钟菲 · 内容运营 / GEO",
        "钟菲的运营案例：GEO 内容增长、小红书 × 抖音电商内容、设计素材账号从 0 到 1。包含数据、方法与完整素材。",
        content,
        active="operations",
        body_class="page-operations",
        canonical_path="operations.html",
    )


def write_site():
    (ROOT / "index.html").write_text(new_index_page(), encoding="utf-8")
    full_ops = operations_page()
    (ROOT / "case-geo.html").write_text(case_page("geo", full_ops), encoding="utf-8")
    (ROOT / "case-selfie.html").write_text(case_page("selfie", full_ops), encoding="utf-8")
    (ROOT / "case-lazy.html").write_text(case_page("lazy", full_ops), encoding="utf-8")
    (ROOT / "operations.html").write_text(operations_overview_page(), encoding="utf-8")
    (ROOT / "design.html").write_text(design_page(), encoding="utf-8")
    (ROOT / "about.html").write_text(about_page(), encoding="utf-8")
    (ROOT / "404.html").write_text(not_found_page(), encoding="utf-8")
    design_dir = ROOT / "design"
    design_dir.mkdir(exist_ok=True)
    for project in PROJECTS:
        (design_dir / f"{project['slug']}.html").write_text(project_page(project), encoding="utf-8")

    urls = [
        "", "operations.html", "case-geo.html", "case-selfie.html", "case-lazy.html",
        "design.html", "about.html", "design/harbin.html", "design/gengong.html", "design/lingyin.html", "design/liangzhu.html",
    ]
    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for url in urls:
        sitemap.append(f"  <url><loc>{SITE_URL}{url}</loc><changefreq>monthly</changefreq><priority>{'1.0' if not url else '0.8'}</priority></url>")
    sitemap.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(sitemap), encoding="utf-8")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}sitemap.xml\n", encoding="utf-8")

    # Keep generated HTML tidy (no trailing whitespace in the committed output).
    for path in list(ROOT.glob("*.html")) + list(design_dir.glob("*.html")):
        cleaned = "\n".join(line.rstrip() for line in path.read_text(encoding="utf-8").splitlines()).rstrip() + "\n"
        path.write_text(cleaned, encoding="utf-8")

    print("Built:", ", ".join(["index.html", "operations.html", "case-geo.html", "case-selfie.html", "case-lazy.html", "design.html", "about.html", "404.html"] + [f"design/{p['slug']}.html" for p in PROJECTS]))


if __name__ == "__main__":
    write_site()
