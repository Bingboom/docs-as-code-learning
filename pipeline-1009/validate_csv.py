
import pandas as pd, json

def validate_csv(csv_path):
    df = pd.read_csv(csv_path)
    errors = []

    for i, row in df.iterrows():
        try:
            json.loads(row["参数JSON"])
        except Exception as e:
            errors.append(f"[第{i+1}行] 参数JSON格式错误: {e}")

        for col in ["命令", "命令标题", "命令格式", "功能描述"]:
            if pd.isna(row[col]) or str(row[col]).strip() == "":
                errors.append(f"[第{i+1}行] 缺少必要字段: {col}")

        if "|" in row["示例命令"] and row["示例命令"].count("|") != row["示例响应"].count("|"):
            errors.append(f"[第{i+1}行] 示例命令与响应数量不匹配")

    if errors:
        print("❌ 校验未通过，共发现以下问题：")
        for err in errors:
            print(" -", err)
    else:
        print("✅ CSV 校验通过！")

if __name__ == "__main__":
    validate_csv("commands_template.csv")
