from openai import OpenAI
from news import news_cr

client = OpenAI(
  api_key='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImUyYzA2ZTY5LTYyNjItNGRlMi1iZjA3LTI0MGUyZDlmZGYxOSIsImlzRGV2ZWxvcGVyIjp0cnVlLCJpYXQiOjE3Mjk1ODQwODksImV4cCI6MjA0NTE2MDA4OX0.3Ut16apK8uMfSS-WkpinVI4VTFcuK6j8wcIUEiiqnnI',
  base_url='https://bothub.chat/api/v2/openai/v1'
)
def generate_blog_text(news_article):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                'role': 'user',
                'content': f"Создай краткий текст на русском языке для блога на основе этой новостной статьи: {news_article}. Напиши его в короткой и понятной для матерей форме. Не используй # и эмодзи"
            }
        ],
        model='gpt-3.5-turbo',
    )

    for choice in chat_completion.choices:
        return choice.message.content

def slog():
    return(generate_blog_text(news_cr()))

