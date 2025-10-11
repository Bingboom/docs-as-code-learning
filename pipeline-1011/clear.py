import shutil, os

DOCS_DIR = "docs"

# 💥 若目录存在则清空重建
if os.path.exists(DOCS_DIR):
    print("⚠️ 检测到旧的 docs/ 目录，正在清理...")
    shutil.rmtree(DOCS_DIR)
    print("✅ 已删除旧目录。")