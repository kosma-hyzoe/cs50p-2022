CORRECT_ANSWERS = ["42", "forty-two", "forty two"]
answer = input("What is the meaning of life?")
print("yes") if answer.strip().lower() in CORRECT_ANSWERS else print("no")

