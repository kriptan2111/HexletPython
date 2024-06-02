def has_char(s, char):
    return char.lower() in s.lower()

# Пример использования
s = "Пример строки для проверки"
char = "р"
result = has_char(s, char)
print(result)
