import json
import pandas as pd
def load_analysis(file_path):
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    required_cols = ["Brand", "Specialization", "Adress", "keywords"]
    text_cols = ["text", "review_text", "review", "Comment", "keywords"]

    review_col = next((col for col in text_cols if col in data[0]), None)
    if not review_col:
        raise KeyError("Нет колонки с отзывом")

    if not all(col in data[0] for col in required_cols):
        raise KeyError("Отсутствуют нужные поля")

    return [
        {**{col: row[col] for col in required_cols}, "review": row[review_col]}
        for row in data
    ]
        
def save_results(results, output_path):
    with pd.ExcelWriter(output_path) as writer:
        for category, data in results.items():
            df = pd.DataFrame(data)
            df.to_excel(writer, sheet_name=category[:31], index=False)
    
    return output_path