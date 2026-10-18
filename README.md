# 钟菲｜内容增长与设计作品集

一个为内容运营 / GEO / AI 内容岗位制作的作品集网站。没有框架与第三方脚本，纯静态 HTML、CSS 与 JavaScript，部署在 GitHub Pages。

**线上地址：** <https://feizhong278-ui.github.io/personal-web/>

## 页面结构

```text
index.html              首页：岗位定位、关键成绩、精选案例、设计档案、方法与联系
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
- `scripts/layout.py`：共享 head、导航、页脚与 SEO。
- `scripts/build_site.py`：各页面结构与生成逻辑。
- `scripts/resume-source.html`：两页简历的打印源文件，`assets/docs/zhongfei-resume.pdf` 由它生成。

图片位于 `assets/img/`，尺寸记录在 `assets/img-manifest.json`。新增图片后，需要同步更新 manifest 与对应的内容引用。

## 部署

推送到 `main` 后，`.github/workflows/deploy.yml` 会通过 GitHub Actions 发布到 GitHub Pages。站点本身不需要构建步骤：生成后的 HTML、CSS、JS 与图片直接发布。

首次启用 Pages 时，在仓库 **Settings → Pages** 将 Source 设为 **GitHub Actions**。

## 设计与技术说明

- 字体：思源宋体 / 思源黑体（SIL Open Font License）按站内字符子集化，Instrument Serif（SIL OFL）用于拉丁文展示。
- 图片：设计项目板与截图已转为 WebP；首屏只加载少量图片，其余使用懒加载，灯箱按需加载大图。
- 交互：滚动显现、数字滚动、GEO 数据视图切换、拖拽/横向滚动画廊、键盘可用的图片灯箱与移动端菜单。
- 无障碍：跳转链接、键盘焦点、语义化标签、图片替代文本、`prefers-reduced-motion` 支持。
- 数据：所有数字来自项目复盘；页面中已注明统计口径。设计项目图片与文字版权归钟菲所有。

## 内容边界

网站公开邮箱与简历 PDF；电话仅出现在简历中。若后续不再希望公开，删除 `assets/docs/zhongfei-resume.pdf`、修改 `about.html` 与 `index.html` 中的下载链接即可。

原始素材（约 480 MB）不进入仓库；仓库只保留面向网站的压缩版本。

## 字体许可

本站使用并子集化以下 SIL Open Font License 1.1 字体：

- Source Han Sans / 思源黑体，Copyright 2014-2025 Adobe。
- Source Han Serif / 思源宋体，Copyright 2014-2021 Adobe。
- Instrument Serif，Copyright 2022 The Instrument Serif Project Authors。

完整许可见 [`assets/fonts/OFL.txt`](assets/fonts/OFL.txt)。字体已按站内字符裁剪为 WOFF2 子集，若新增大量中文内容，建议重新生成子集或回退到系统字体。
