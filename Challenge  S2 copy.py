fruits =[
        'apples',
        'bananas',
        'grapes',
        'mangoes',
        'nectarines',
        'pears',
]

print("Start Looping Fruits with for Loop")
for fruit in fruits:
    print(fruit)
print("End Looping Fruits with for Loop")

#-----------------------------------------------------------

indexFruit = 0
print("Start Looping Fruits with while Loop")
while fruits[indexFruit] != "nectarines":
        print(fruits[indexFruit])
        indexFruit += 1
print("End Looping Fruits with while Loop")