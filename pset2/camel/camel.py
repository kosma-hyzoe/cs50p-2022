camel_case_name = input("CamelCase: ")
snake_case_name = ""
camel_case_copy = camel_case_name

for char in camel_case_name:
    camel_case_copy = camel_case_copy.replace(char, f"_{char.lower()}")if char.isupper() else camel_case_copy

snake_case_name = camel_case_copy
print(snake_case_name)
