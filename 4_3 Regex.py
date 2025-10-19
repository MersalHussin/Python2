import re
phrase = "ahmed 28 years old and mohamed 30 years old and mersal 21 years old"
print(re.sub(r"(mersal|ahmed) \d*","name",phrase))