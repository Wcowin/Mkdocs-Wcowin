#!/bin/bash
# ==========================================
# 将 site 文件夹打包为 site.zip
# 如果 site.zip 已存在则自动替换
# ==========================================

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SITE_DIR="$SCRIPT_DIR/site"
ZIP_FILE="$SCRIPT_DIR/site.zip"

# 检查 site 目录是否存在
if [ ! -d "$SITE_DIR" ]; then
    echo "[错误] site 目录不存在: $SITE_DIR"
    exit 1
fi

# 删除旧的 zip（如果存在）
if [ -f "$ZIP_FILE" ]; then
    echo "[信息] 检测到旧的 site.zip，正在删除..."
    rm -f "$ZIP_FILE"
fi

# 进入项目根目录后打包（这样 zip 内路径为 site/ 开头）
echo "[信息] 正在打包 site 目录..."
cd "$SCRIPT_DIR"
zip -r site.zip site/

echo "[完成] site.zip 已生成: $ZIP_FILE"
ls -lh "$ZIP_FILE"
