phone1 = "+234-9003-39948"
print(phone1.startswith("+232"))

email = "josephabel540@gmail.com"
print(email.endswith("gmail.com"))

print("@" in email)  

url = "https://api.company/v1/data"
print("/api" in url)

file = "data_backup.csv"
print(file.endswith(".cvv"))

phone2 = "233-7658-6655"
print(phone2[4:])
print(phone1[5:])

print(phone1.find("-"))
print(phone2.find("-"))
