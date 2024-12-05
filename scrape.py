import csv
import re
from bs4 import BeautifulSoup
import requests

# Вказуємо шлях до папки Documents
file_path = '/Users/user/Documents/results.csv'

url = 'https://rozetka.com.ua/ua/promo/stmykday/?gad_source=1&section_id=80003'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

# Створюємо список для збереження результатів
results = []

# Знаходимо всі блоки з товарами
blocks = soup.find_all('div', class_='goods-tile__content')

# Функція, щоб прибрати символ валюти "₴" з ціни
def clean_price(price_text):
    return re.sub(r'\D', '', price_text)

# Обробка кожного блоку
for i, block in enumerate(blocks, start=1):
    title = block.find('span', class_='goods-tile__title')
    title_text = title.text.strip() if title else None  

    # Якщо знайдено, видаляємо "Мобільний телефон " із назви
    if title_text:
        title_text = title_text.replace("Мобільний телефон ", "").strip()

    # Перевірка на наявність старої ціни
    old_price = block.find('div', class_='goods-tile__price--old price--gray ng-star-inserted')
    old_price_text = old_price.text.strip() if old_price else None  

    # Перевірка на наявність нової ціни
    new_price = block.find('p', class_='ng-star-inserted')
    new_price_text = new_price.text.strip() if new_price else None

    old_price_clean = clean_price(old_price_text) if old_price_text else None
    new_price_clean = clean_price(new_price_text) if new_price_text else None

    # Додаємо дані до списку
    results.append([title_text, old_price_clean, new_price_clean])

# Записуємо дані у CSV файл
with open(file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Product name', 'Old price', 'New price'])  
    writer.writerows(results)

print(f"Your file is ready {file_path}!")
