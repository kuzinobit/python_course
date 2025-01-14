# Сортировка словаря по значениям
import operator

scores = {'Иван': 90, 'Мария': 95, 'Олег': 85}
sorted_scores = dict(sorted(scores.items(), key=operator.itemgetter(1), reverse=True))
print(sorted_scores)