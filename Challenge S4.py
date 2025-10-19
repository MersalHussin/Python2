import re
my_String = "almdrasa is your way to learn programming the right way, almdrasa badges motivate students to do more, almdrasa quizes help students practice on what they have learned through the course. almdrasa courses are one of a kind because they were made by professionals. almdrasa look and feel is one of a kind. almdrasa wishes you a good learning. thanks"
repeatTimes = re.findall(r"almdrasa\s\w{3,}",my_String)
result = re.sub(r"almdrasa\s\w{3,}","Almadrasa",my_String,3)
print(f"'almdrasa' repeated {len(repeatTimes)} times followed by a 3+ character word")
print("-------------------------------------------------")
print(result)