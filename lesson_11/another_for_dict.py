# Подсчет количества каждого символа в строке
text = "hello world"
char_count = {}

for char in text:
    if char != " ":
        char_count[char] = char_count.get(char, 0) + 1
print(char_count)