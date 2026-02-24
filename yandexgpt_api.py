from yandex_cloud_ml_sdk import YCloudML
import os
from dotenv import load_dotenv

load_dotenv()

sdk = YCloudML(
    folder_id= os.getenv("YC_FOLDER_ID"),
    auth= os.getenv("YC_IAM_TOKEN"),
)

def ask_yandexgpt(prompt: str):
    
    model = sdk.models.completions("yandexgpt-lite").configure(temperature=0)
    result = model.run(prompt)
    return result.alternatives[0].text
