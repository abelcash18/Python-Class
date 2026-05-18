text = "Uniben UNIVERSITY"
print(text.lower())
print(text.upper())


search = "Email"
data = "email"
print(search == data)


search = "Email ".lower().strip()
data = " emAil".lower().strip()
print(search == data)

#classwork
messy = "968-Maria, ( D@t@ Engineer, ) ;; 27y,  "
print(messy[4:9], "-", )


Name = "968-Maria"
Role = "( D@t@ Engineer )"
Age = 27

print(Name[4:9])
print(Role.replace("(","").replace(")","").replace("@","a").strip().upper())
print(messy.replace("(","").replace(")","").replace("@","a").replace(";;","")[4:].upper().split())