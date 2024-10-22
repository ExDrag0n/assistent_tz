from openai import OpenAI
from txt4img import dlya_img
import json
import requests
import io


client = OpenAI(
  api_key='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImUyYzA2ZTY5LTYyNjItNGRlMi1iZjA3LTI0MGUyZDlmZGYxOSIsImlzRGV2ZWxvcGVyIjp0cnVlLCJpYXQiOjE3Mjk1ODQwODksImV4cCI6MjA0NTE2MDA4OX0.3Ut16apK8uMfSS-WkpinVI4VTFcuK6j8wcIUEiiqnnI',
  base_url='https://bothub.chat/api/v2/openai/v1'
)


def create_img(image_text):
    image_text = dlya_img()
    params = {
        'model': 'dall-e-3',
        'prompt': image_text,
        'n': 1,
        'size': '1024x1024',
    }


    req = client.images.generate(**params)
    image_data = json.loads(req.model_dump_json())['data'][0]['url']
    response = requests.get(image_data)


    if response.status_code == 200:
        with open("generated_image.jpg", "wb") as f:
            f.write(response.content)
        print("Изображение успешно сохранено как generated_image.jpg")
    else:
        print(f"Не удалось загрузить изображение. Статус код: {response.status_code}")

    print(f"URL сгенерированного изображения: {image_data}")
