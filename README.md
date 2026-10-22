# 钟菲｜内容增长与设计作品集

一个为内容运营 / GEO / AI 内容岗位制作的作品集网站。没有框架与第三方脚本，纯静态 HTML、CSS 与 JavaScript，部署在 GitHub Pages。

**线上地址：** <https://feizhong278-ui.github.io/personal-web/>

## 页面结构

```text
index.html              首页：关于我、项目展示、工作经历、教育背景、技能特长、兴趣爱好与联系
operations.html         运营案例总览：三个案例的快速索引
case-geo.html           GEO 内容增长完整案例
case-selfie.html        自拍杆小圆子 / 电商内容完整案例
case-lazy.html          懒羊羊素材库 / 设计内容账号完整案例
design.html             设计作品总览
design/harbin.html      哈尔滨夏日文化使者 IP
design/gengong.html     根宫佛国「无念熊」文创
design/lingyin.html     灵隐万象集
design/liangzhu.html    良渚博物院 IP 文创
about.html              经历、教育、能力、奖项与联系方式
404.html                404 页面
```

网站包含 3 个运营案例、4 个设计项目、45 张项目板、14 张笔记截图、30 页爆款拆解手册与 8 张商品主图 / 4 张详情页。长素材使用独立案例页与灯箱查看，避免在首页堆叠。

## 本地预览

```bash
python3 -m http.server 8000
```

打开 <http://localhost:8000>。所有资源都使用相对路径，可直接作为静态目录部署。

## 修改内容

`scripts/` 是生成源码，根目录 HTML 是已生成的发布文件：

```bash
python3 scripts/build_site.py
```

- `scripts/content.py`：项目文案、统计数字、图片引用与案例索引。
- `scripts/layout.py`：共享 head、浮动导航、页脚与 SEO。修改 CSS / JS 后请同步更新顶部的 `ASSET_VERSION`，避免浏览器继续使用旧缓存。
- `scripts/build_site.py`：各页面结构与生成逻辑。
- `scripts/resume-source.html`：旧版两页简历的打印源文件；当前对外下载 PDF 以 `assets/docs/zhongfei-resume.pdf` 为准。

图片位于 `assets/img/`，尺寸记录在 `assets/img-manifest.json`。新增图片后，需要同步更新 manifest 与对应的内容引用。

## 部署

推送到 `main` 后，`.github/workflows/deploy.yml` 会通过 GitHub Actions 发布到 GitHub Pages。站点本身不需要构建步骤：生成后的 HTML、CSS、JS 与图片直接发布。

首次启用 Pages 时，在仓库 **Settings → Pages** 将 Source 设为 **GitHub Actions**。

## 设计与技术说明

- 排版：正文 16px、卡片正文 14–15px、元信息 11–12px，标题使用 clamp 级差；正文近黑、次要信息深灰，保证长文可读性与对比度。
- 视觉：柔和桃 / 薄荷 / 薰衣草渐变背景、白色玻璃卡、浮动胶囊导航与阿里巴巴普惠体展示标题；首页以「关于我 → 项目 → 经历 → 教育 → 技能 → 兴趣」组织，深层案例页保留完整内容；4 个设计项目页按项目板原始顺序单列浏览，像翻 PDF 一样向下阅读。
- 字体：标题使用阿里巴巴普惠体 Heavy（覆盖 700–900 字重），正文使用思源黑体；均按站内字符裁剪为 WOFF2 子集。
- 图片：设计项目板与截图已转为 WebP；首屏只加载少量图片，其余使用懒加载，灯箱按需加载大图。
- 交互：滚动显现、滚动章节导航、数字滚动、GEO 数据视图切换、拖拽/横向滚动画廊、键盘可用的图片灯箱、移动端浮动菜单与肖像卡微倾斜。
- 无障碍：跳转链接、键盘焦点、语义化标签、图片替代文本、`prefers-reduced-motion` 支持。
- 数据：所有数字来自项目复盘；页面中已注明统计口径。设计项目图片与文字版权归钟菲所有。

## 内容边界

网站公开邮箱与简历 PDF；电话仅出现在简历中。若后续不再希望公开，删除 `assets/docs/zhongfei-resume.pdf`、修改 `about.html` 与 `index.html` 中的下载链接即可。

原始素材（约 480 MB）不进入仓库；仓库只保留面向网站的压缩版本。

## 字体许可

- **Alibaba PuHuiTi / 阿里巴巴普惠体**（Heavy）：由阿里巴巴集团发布，免费使用；来源与许可见 [`assets/fonts/ALIBABA-PUHUITI-NOTICE.md`](assets/fonts/ALIBABA-PUHUITI-NOTICE.md)。
- **Source Han Sans / 思源黑体**（Regular）：SIL Open Font License 1.1，Copyright 2014-2025 Adobe；完整许可见 [`assets/fonts/OFL.txt`](assets/fonts/OFL.txt)。

字体已按站内字符裁剪为 WOFF2 子集。若新增大量中文内容，建议重新生成子集或回退到系统字体。
