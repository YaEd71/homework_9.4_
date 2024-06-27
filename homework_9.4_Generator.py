def all_variants(text):
    length = len(text)
    # Перебираем все возможные длины подстрок
    for start in range(length):
        for end in range(start + 1, length + 1):
            yield text[start:end]

# Пример использования
a = all_variants("abc")
for i in a:
    print(i)
