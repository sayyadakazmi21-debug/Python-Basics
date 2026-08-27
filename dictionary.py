x={"name":"sayyada","class":11,"age":"16"}
x["gender"]="female"
print(x)


print(x["name"])


print(x.get("name"))

x["class"]=12
print(x)

x.pop("age")
print(x)

x.clear()
print(x)