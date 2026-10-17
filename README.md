# 钟菲｜内容增长与设计作品集

一个无需构建步骤的静态作品集，适合部署在 GitHub Pages。

## 本地预览

在此目录运行：

```bash
python3 -m http.server 8000
```

然后访问 <http://localhost:8000>。

## 发布到 GitHub Pages

1. 将本目录内容推送到 `feizhong278-ui/personal-web` 的 `main` 分支。
2. 在仓库 **Settings → Pages → Build and deployment** 中，将 Source 选择为 **GitHub Actions** 并保存。这是 GitHub 首次创建 Pages 站点所要求的仓库级授权。
3. 打开 **Actions → Deploy GitHub Pages**，选择 **Run workflow** 重新运行部署；之后每次推送 `main` 都会自动部署。
4. 工作流完成后，站点将发布至：
   `https://feizhong278-ui.github.io/personal-web/`

所有网站图片均位于 `assets/images/`，为从本地素材导出的压缩发布版本；原始素材不应提交到仓库。
