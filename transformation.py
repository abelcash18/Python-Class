price = "1234,980"
print(price.replace(",",  ".").replace(".", "").replace("", "-")) 


phone ="234/905/642/4816"
print(phone.replace("/", "-").replace("-", ".").replace(".", ""))


#class work
tel = "+49 (176) 123-4567"
print(tel.replace("+", "00").replace("(","").replace(")", "").replace(" ","").replace("-", ""))

