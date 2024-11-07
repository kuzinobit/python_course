text = input("Введите слово или фразу: ")
cleaned_text = text.replace(" ", "").lower()
if cleaned_text == cleaned_text[::-1]:
    print("Это палиндром.")
else:
    print("Это не палиндром.")