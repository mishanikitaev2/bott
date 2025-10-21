from docx import Document

def create_template(name, content):
    doc = Document()
    for line in content.split('\n'):
        doc.add_paragraph(line)
    doc.save(f'templates/{name}')

# Создаем шаблоны
templates = {
    'history.docx': """ИСТОРИЯ БОЛЕЗНИ

Пациент: {name}
Дата рождения: {birth_date}
Паспорт: {passport}
Диагноз: {diagnosis}
Дата поступления: {admission_date}

Особые отметки: {notes}""",

    'extract.docx': """ВЫПИСКА ИЗ ИСТОРИИ БОЛЕЗНИ

ФИО: {name}
Дата рождения: {birth_date}
Паспорт: {passport}
Диагноз: {diagnosis}
Дата выписки: {discharge_date}

Назначения: {notes}""",

    'prescription.docx': """НАЗНАЧЕНИЯ ВРАЧА

Пациент: {name}
Дата рождения: {birth_date}
Диагноз: {diagnosis}

Лечебные назначения: {notes}"""
}

for filename, content in templates.items():
    create_template(filename, content)

print("✅ Шаблоны созданы!")