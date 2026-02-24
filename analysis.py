import json
from yandexgpt_api import ask_yandexgpt
from analysis_file import load_analysis, save_results
from prompts import analysis_prompt 

file_path = "result/Отзывы-Оценка.json"
reviews = load_analysis(file_path)
output_path = 'analysis/Отзывы-Анализ.xlsx'

prompt = analysis_prompt(reviews)

response = ask_yandexgpt(prompt)

cleaned_response = response.strip()
if cleaned_response.startswith("```") and cleaned_response.endswith("```"):
    cleaned_response = cleaned_response[3:-3].strip()

try:
    result = json.loads(cleaned_response)
except json.JSONDecodeError:
    print("Ошибка JSON в ответе:", cleaned_response)
    result = None

if result:
    save_results(result, output_path)
    print(f"Готово. Результаты сохранены в {output_path}")