name = input("what's your name?")
age = input("how old are you?")
country = input("where are you from?")
job = input("what's your job?")
# result = "Welcome " + name + ", your age is " + age + ", you are from " + country + " and your job is " + job
result = f"Welcome {name}. Your age is {age}. Yout are from {country} and your job is {job}.".format(name=name, age=age, country=country, job=job)
print(result)
