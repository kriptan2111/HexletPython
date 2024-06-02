def my_substr(s, length):
    result = ""
    i = 0
    while i < length and i < len(s):
        result += s[i]
        i += 1
    return result

# Пример использования
s = "Пример строки"
length = 6
result = my_substr(s, length)
print(result)
