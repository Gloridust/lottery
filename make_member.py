import json

# 定义成员列表
members = []

# 生成成员数据
for i in range(1, 901):
    member = {
        "phone": f"中奖号码",
        "name": f"No.{str(i).zfill(3)}"
    }
    members.append(member)

# 将成员数据转换为 JSON 格式的字符串
member_json = json.dumps(members, indent=2, ensure_ascii=False)

# 生成 member.js 文件
with open("member.js", "w", encoding="utf-8") as f:
    f.write("var member = ")
    f.write(member_json)
    f.write(";")

print("member.js 文件生成完毕。")
