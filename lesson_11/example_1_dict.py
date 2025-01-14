# Подсчет количества каждого слова в тексте
text = "python is great and python is dynamic"
words = text.split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)