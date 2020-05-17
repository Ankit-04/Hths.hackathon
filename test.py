your_string = "directions from hollywood to disneyland"
removal_list = ["directions ","from ","to "]

for word in removal_list:
    your_string = your_string.replace(word, "")
print(your_string)