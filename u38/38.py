def filter_string(input_string, text):
    # Удаляем символ из строки
    result_string = input_string.replace(text, "")
    
    # Удаляем начальные и концевые пробелы
    result_string = result_string.strip()
    
    return result_string

# Пример использования функции
input_string = "Привет, мир!"
text = "и"
output_string = filter_string(input_string, text)
print(output_string)