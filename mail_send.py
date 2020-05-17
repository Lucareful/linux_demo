import yagmail


# 163授权码：“Becareful333”

ya_obj = yagmail.SMTP(user="luencer@163.com", password="Becareful333", host="smtp.163.com")

content = "“我可以向你问路吗？”" \
          "“什么路？”" \
          "“通往你心里的路”"

ya_obj.send("@qq.com", "Luenci的来信", content)
