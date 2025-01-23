dic = {"name":"Mr Eagle", "planet":"Mars", "no.":3}
dic2 = {"name":"Mr Eagle", "planet":"Mars", "no.":3, "when":2025}

for key, value in dic2.items():
    if key in dic:
        dic[key] += dic2[key]
    else:
        dic[key] = value


print(dic)