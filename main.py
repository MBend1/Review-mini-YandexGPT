import json
from yandexgpt_api import ask_yandexgpt
from prompts import json_prompt
from review_file import load_reviews, save_results

file_path = "data/Отзывы-Еда.csv"
reviews = load_reviews(file_path)
output_path = 'result/Отзывы-Оценка.json'

results = []

for review in reviews:
    response = ask_yandexgpt(json_prompt(review))
    cleaned_response = response.strip()
    if cleaned_response.startswith("```") and cleaned_response.endswith("```"):
        cleaned_response = cleaned_response[3:-3].strip()
    try:
        parsed = json.loads(cleaned_response)
        results.append(parsed)
    except json.JSONDecodeError:
        print(f"Ошибка JSON: {review}")
    
        
saved_file = save_results(results, output_path)
print(f"Готово. Результаты сохранены в {saved_file}")