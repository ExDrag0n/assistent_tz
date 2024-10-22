import docx


def save_res(blog_text, image_text):
    document = docx.Document()
    document.add_paragraph(blog_text)
    document.save('blog_post.docx')
    print('Данные для генерации успешно сохранены в файле blog_post.docx')
    with open('image_text.txt', 'w') as f:
        f.write(image_text)
