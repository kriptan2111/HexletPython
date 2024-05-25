url = 'example.org'

def normalize_url(url):
    https = 'https://'
    if url[:8] == https:
        return url
    elif url[:7] == 'http://':
        return https + url[7:]
    else:
        return https + url
    
"""

##url = 'https://example.com'
url = 'example.org'

import re

def normalize_url(url):
    
    Нормализует адрес сайта, добавляя "https://" в начало, если он отсутствует.

    Параметры:
    url (str): Адрес сайта.

    Возвращает:
    str: Нормализованный адрес сайта.
    
    if not re.match(r'^https?://', url):
        url = 'https://' + url
    return url
"""

print(normalize_url(url))