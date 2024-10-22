from blog import slog
from openai import OpenAI

client = OpenAI(
  api_key='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImUyYzA2ZTY5LTYyNjItNGRlMi1iZjA3LTI0MGUyZDlmZGYxOSIsImlzRGV2ZWxvcGVyIjp0cnVlLCJpYXQiOjE3Mjk1ODQwODksImV4cCI6MjA0NTE2MDA4OX0.3Ut16apK8uMfSS-WkpinVI4VTFcuK6j8wcIUEiiqnnI',
  base_url='https://bothub.chat/api/v2/openai/v1'
)

def generate_image_text(blog_post):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                'role': 'user',
                'content': f"Создай короткий запоминающийся слоган для данного текста блога: {blog_post}"
            }
        ],
        model='gpt-3.5-turbo',
    )

    for choice in chat_completion.choices:
        return choice.message.content


def dlya_img():
    return generate_image_text(slog())
