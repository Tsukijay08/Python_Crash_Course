from string import Template

tempStr = "My name is $name and my age is $age"
tempObj = Template(tempStr)
tempHandler = tempObj.substitute(name = "Jeff", age=29)

print(tempHandler)