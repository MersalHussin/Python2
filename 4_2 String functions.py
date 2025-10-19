fristName = "Mersal"
lasName = "Hussin"
title = "The Frontend Developer"
title = "The, Frontend, Developer"
print(fristName.capitalize()) #Mersal
print(fristName.lower()) #mersal
print (title.find("Developer"))#13
print (title.replace("Developer","Designer")) #The Frontend Designer
print (title[4:]) # Frontend, Developer
print (title.split(",")) #['The', ' Frontend', ' Developer']


parts = title.split(",")
for part in parts:
    print(part.strip().capitalize())