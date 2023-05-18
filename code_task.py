# код по задаче
original_list = ["Hello", "2", "world", ":-)"] 
new_list = []

for word in original_list:
    if len(word) <= 3:
        new_list.append(word)

print(new_list)