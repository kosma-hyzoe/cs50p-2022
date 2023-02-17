import sys

IMAGE_EXTENSIONS = ["gif", "jpg", "jpeg", "png"]
APPLICATION_EXTENSIONS = ["zip", "pdf"]

file_name = input("File name: ").lower()
if "." in file_name:
    extension = file_name[file_name.rindex(".") + 1:].rstrip()
else:
    print("application/octet-stream")
    sys.exit()

if extension in IMAGE_EXTENSIONS:
    extension = "jpeg" if extension == "jpg" else extension
    print(f"image/{extension}")
elif extension == "txt":
    print(f"text/plain")
elif extension in APPLICATION_EXTENSIONS:
    print(f"application/{extension}")
else:
    print("application/octet-stream")

