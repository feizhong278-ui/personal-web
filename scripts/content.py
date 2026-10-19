# -*- coding: utf-8 -*-
"""内容源：站点文案、项目数据与素材引用。"""

SITE = {
    "name": "钟菲",
    "name_en": "ZHONG FEI",
    "url": "https://feizhong278-ui.github.io/personal-web/",
    "email": "Aria.zhong@outlook.com",
    "role": "内容运营 / GEO 内容增长 / 视觉设计",
    "location": "杭州",
    "status": "2027 届 · 求职中",
    "description": "钟菲的作品集：内容运营、GEO 内容增长与视觉设计。用策略、数据与视觉，让内容留下痕迹。",
}

NAV = [
    ("index.html", "首页", "home"),
    ("operations.html", "运营案例", "operations"),
    ("design.html", "设计作品", "design"),
    ("about.html", "关于我", "about"),
]

PROJECTS = [
    {
        "slug": "harbin",
        "index": "01",
        "short": "哈尔滨 IP",
        "title": "哈尔滨夏日文化使者",
        "title_en": "HARBIN SUMMER CULTURAL AMBASSADOR",
        "discipline": "城市 IP / 角色设计 / 应用延展",
        "year": "2025.07—2025.10",
        "role": "项目负责人 / 文化提炼、IP 视觉与延展",
        "type": "团队项目",
        "award": "第三届中国研究生「美丽中国」创新设计大赛 · 全国二等奖",
        "award_short": "全国二等奖",
        "cover": 1,
        "card_cover": {
            "src": "assets/img/design/harbin/harbin-card-cover-800.webp",
            "srcset": [
                ("assets/img/design/harbin/harbin-card-cover-800.webp", 800),
                ("assets/img/design/harbin/harbin-card-cover-1600.webp", 1600),
            ],
            "w": 800,
            "h": 407,
        },
        "feature": 1,
        "summary": "把哈尔滨的夏日、冰雪记忆与城市性格，变成一个可以走进海报、文创与线下场景的角色。",
        "intro": "以哈尔滨夏日城市文化为起点，用 AIGC 辅助文化元素提炼与角色方向探索，再用 Photoshop、Illustrator 完成形象优化和应用延展。项目获得第三届中国研究生「美丽中国」创新设计大赛全国二等奖。",
        "theme": "yellow",
        "chapters": [
            {
                "title": "01 / 从城市气质，到一个角色",
                "desc": "从哈尔滨的建筑、冰雪与夏日生活里寻找视觉线索，建立角色设定、色彩与表情系统。",
                "boards": [1, 2, 3],
                "layout": "portrait",
            }
        ],
    },
    {
        "slug": "gengong",
        "index": "02",
        "short": "根宫佛国",
        "title": "根宫佛国「无念熊」",
        "title_en": "GEN GONG BUDDHA KINGDOM / WUNIAN BEAR",
        "discipline": "景区 IP / 文创产品 / 空间应用",
        "year": "2024.09—2024.12",
        "role": "项目负责人 / 团队统筹、实地调研、创意策划与视觉方案",
        "type": "团队项目",
        "award": "第五届全国会展策划创意大赛 · 全国三等奖 / 浙江省第十四届会展策划创意大赛 · 一等奖",
        "award_short": "全国三等奖 · 省级一等奖",
        "cover": 1,
        "feature": 14,
        "summary": "为开化根宫佛国景区做一个有亲和力的「无念熊」，让传统文化从展柜里走到日常物件上。",
        "intro": "围绕开化县根宫佛国景区，从市场分析、问卷调研、文化母题提炼到 IP 形象与文创落地，完成一套从策略到视觉的完整提案。项目获得全国会展策划创意大赛全国三等奖、浙江省一等奖。",
        "theme": "red",
        "chapters": [
            {
                "title": "01 / 先理解这座山",
                "desc": "从景区文化、游客画像与市场机会出发，找到「无念」这一可以转译为角色性格的精神内核。",
                "boards": [2, 3, 4, 5, 6],
                "layout": "wide",
            },
            {
                "title": "02 / 让角色成立",
                "desc": "从 AI 视觉探索到三视图、表情与动作，建立可延展的 IP 形象系统。",
                "boards": [7, 8, 9, 10, 11],
                "layout": "wide",
            },
            {
                "title": "03 / 让它被带走",
                "desc": "把角色转译为日用品、玩具、文具与线下空间，让文化成为可以被带走的体验。",
                "boards": [12, 13, 14, 15],
                "layout": "wide",
            },
        ],
    },
    {
        "slug": "lingyin",
        "index": "03",
        "short": "灵隐万象集",
        "title": "灵隐万象集",
        "title_en": "LINGYIN MYRIAD WORLDS",
        "discipline": "文化视觉 / 角色设计 / 文创延展",
        "year": "2024",
        "role": "视觉设计 / 角色设定与文创延展",
        "type": "文化主题视觉设计",
        "award": "",
        "award_short": "文化视觉",
        "cover": 1,
        "feature": 1,
        "summary": "把灵隐文化里的角色与符号，翻译成一套更年轻、更有亲近感的视觉语言。",
        "intro": "以灵隐文化为叙事母题，提炼角色、色彩与传统纹样，构建「灵隐万象集」的视觉系统，并延展至海报、徽章、钥匙扣与明信片等文创载体。",
        "theme": "gold",
        "chapters": [
            {
                "title": "01 / 传统符号的年轻转译",
                "desc": "从文化意象里提炼角色与色彩，用更轻盈的插画语言重新组织，让传统不只停留在庄重的一面。",
                "boards": [1, 2, 3, 4, 5],
                "layout": "wide",
            }
        ],
    },
    {
        "slug": "liangzhu",
        "index": "04",
        "short": "良渚博物院",
        "title": "良渚博物院 IP 文创",
        "title_en": "LIANGZHU MUSEUM / IP & CULTURAL CREATIVE",
        "discipline": "博物馆 IP / 角色设计 / 文创系统",
        "year": "2024",
        "role": "IP 形象与文创设计 / 视觉延展",
        "type": "博物馆文创项目",
        "award": "",
        "award_short": "博物馆 IP",
        "cover": 1,
        "feature": 12,
        "summary": "把玉琮、神人兽面纹与陶器，变成三个可以走进年轻人日常的良渚角色。",
        "intro": "从良渚玉琮、神人兽面纹与陶器造型中提取视觉基因，发展出「良良」「小琮」「陶陶」三个 IP 角色，并延展到海报、表情包、包装、服饰与线下展示，让博物馆文化以更轻的方式进入日常。",
        "theme": "orange",
        "chapters": [
            {
                "title": "01 / 建立角色宇宙",
                "desc": "从文物造型与纹样里提炼角色轮廓、配色和表情，让三个角色各有性格又共享同一套视觉基因。",
                "boards": [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                "layout": "wide",
            },
            {
                "title": "02 / 从展柜到日常",
                "desc": "把 IP 放进包装、手机壳、帆布袋、贴纸与线下打卡场景，验证这套视觉是否真的可以被使用。",
                "boards": [13, 14, 15],
                "layout": "wide",
            },
            {
                "title": "03 / 每个角色都要立得住",
                "desc": "用三视图、性格关键词和表情系统，把三个角色从概念推进到可生产的设定。",
                "boards": [16, 17, 18, 19, 20, 21, 22],
                "layout": "wide",
            },
        ],
    },
]

# 自拍杆项目：可公开的笔记截图（14 张）与账号矩阵截图
SELFIE_ACCOUNTS = [
    {"img": "assets/img/ops/selfie/account-01-760.webp", "name": "自拍杆小圆子", "label": "主账号 / 内容与成交"},
    {"img": "assets/img/ops/selfie/account-02-760.webp", "name": "自拍杆小小圆子", "label": "矩阵账号 / 场景测试"},
    {"img": "assets/img/ops/selfie/account-03-760.webp", "name": "自拍杆中圆子", "label": "矩阵账号 / 产品测试"},
    {"img": "assets/img/ops/selfie/account-04-760.webp", "name": "自拍杆大圆子", "label": "矩阵账号 / 内容测试"},
]

SELFIE_NOTE_COUNT = 14
SELFIE_PRODUCT_COUNT = 8
SELFIE_DETAIL_COUNT = 4

LAZY_POSTS = [
    {"title": "毕业设计物料只花了 400+｜店铺分享", "likes": 3645, "saves": 2370, "comments": 57, "img": "assets/img/ops/lazy/note-01-700.webp"},
    {"title": "海报设计｜民族舞蹈｜非遗传统", "likes": 2266, "saves": 1238, "comments": 2, "img": "assets/img/ops/lazy/note-02-700.webp"},
    {"title": "情绪咖啡品牌设计｜咖啡文化｜几何图案", "likes": 2149, "saves": 1503, "comments": 5, "img": "assets/img/ops/lazy/note-03-700.webp"},
    {"title": "大二版式结课大作业｜食品画册排版", "likes": 1315, "saves": 741, "comments": 16, "img": "assets/img/ops/lazy/note-04-700.webp"},
    {"title": "品牌视觉提案｜视传学生作业", "likes": 778, "saves": 459, "comments": 7, "img": "assets/img/ops/lazy/note-05-700.webp"},
    {"title": "画册排版设计｜汽车宣传册", "likes": 658, "saves": 354, "comments": 6, "img": "assets/img/ops/lazy/note-06-700.webp"},
]

# 30 页《拆解小红书爆款笔记》手册中，首页展示的三页
SLIDE_FEATURES = [
    {"n": 3, "label": "标题系统", "caption": "产品关键词 × 种草词 × 流量词，构成一条笔记的入口。"},
    {"n": 23, "label": "封面思维", "caption": "1 秒原则：在瀑布流里，先让用户愿意停下来。"},
    {"n": 30, "label": "推流机制", "caption": "理解阶梯式流量池，才知道发布之后该看什么、改什么。"},
]

# 用于页面上的项目导航
CASE_NAV = [
    ("geo", "01", "GEO 内容增长", "AI 搜索 / 内容矩阵"),
    ("selfie", "02", "自拍杆小圆子", "小红书 × 抖音 / 店铺转化"),
    ("lazy", "03", "懒羊羊素材库", "设计内容 / 0 到 1"),
]
