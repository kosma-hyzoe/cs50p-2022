greeting = input("Greeting: ").lower().strip()

if greeting.startswith("hello"):
    print("$0", end="")
elif greeting.startswith("h"):
    print("$20", end="")
else:
    print("$100", end="")