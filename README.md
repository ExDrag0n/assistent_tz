Данный ассистент создан для тестового задания 
В качестве чат бота был выбран сервис BotHub: https://bothub.chat/main

В качестве основных библиотек выступают:
1. requests - для работы с HTTPs запросами
2. datetime - для получения актуальных новостей
3. openai - для работы с выбранным чат ботом
4. io - стандартная бибилиотека для работы с потоками
5. docx - используется для сохранения результатов в docx формате

Для получения новостей использовался api хук https://newsapi.org/v2/everything.
После получения заголовка файл blog.py генерирует короткий блог по данному заголовку.
Далее файл txt4img.py выделяет из этого блога основной слоган, который передаётся в img.py 
в качестве промта для изображения. Файл res.py сохраняет все использованые промты и изображение как локальные файлы на устройстве
Файл main.py является скриптом для запуска приложения

Со всеми вопросами по поводу работы ассистента просьба связаться через телеграм: @Gr4num
