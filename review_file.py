import pandas as pd
import json
import os

def load_reviews(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    
    if ext == ".csv":
        df = pd.read_csv(file_path)
        required_cols = ["Brand", "Specialization", "Adress", "Date", "Comment"]
        if not all(col in df.columns for col in required_cols):
            raise KeyError(f"CSV файл должен содержать столбцы: {', '.join(required_cols)}")
        
        return df[required_cols].rename(columns={"Comment": "review"}).to_dict(orient="records")
    
    elif ext == ".json":
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        df = pd.json_normalize(data, sep="_")

        required_cols = ["Brand", "Specialization", "Adress", "Date"]
        text_cols = ["text", "review_text", "review", "Comment"]

        review_col = next((col for col in text_cols if col in df.columns), None)
        if not review_col:
            raise KeyError("В JSON файле не найден столбец с текстом отзыва ('text', 'review_text', 'review', 'Comment')")

        if not all(col in df.columns for col in required_cols):
            raise KeyError(f"JSON должен содержать поля: {', '.join(required_cols)}")

        return df[required_cols + [review_col]].rename(columns={review_col: "review"}).to_dict(orient="records")
    
    elif ext == ".txt":
        with open(file_path, "r", encoding="utf-8") as f:
            reviews = [line.strip() for line in f if line.strip()]
        return reviews
    
    else:
        raise ValueError(f"Неподдерживаемый формат файла: {ext}")
    
def save_results(results, output_path):
    
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    return output_path
    