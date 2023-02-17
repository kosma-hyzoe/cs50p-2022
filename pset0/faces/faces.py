FACES = {":)": "🙂", ":(": "🙁"}

text = input()

for face, unicode_face in FACES.items():
    if face in text:
        text = text.replace(face, unicode_face)

print(text)