from ModulesChallenge import ModuleCH
import random2

print(random2.randint(10,12))
frist_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))
opertion = input("Enter operation (+, -, /, *,power,sqr,random): ")

if(opertion == "+"):
    print(ModuleCH.addition(frist_num,second_num))
elif(opertion == "-"):
    print(ModuleCH.subtraction(frist_num,second_num))
elif(opertion == "/"):
    print(ModuleCH.division(frist_num,second_num))
elif(opertion == "*"):
    print(ModuleCH.multiplication(frist_num,second_num))
elif(opertion == "sqr"):
    print(ModuleCH.sqr(frist_num,second_num))
elif(opertion == "power"):
    print(ModuleCH.power(frist_num,second_num))
elif(opertion == "random"):
    print(ModuleCH.random(frist_num,second_num))
else:
    print("Invalid opertion")

