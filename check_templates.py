import os

print("🔍 Проверяем шаблоны...")
print(f"📁 Текущая папка: {os.getcwd()}")

# Проверяем папку templates
if not os.path.exists("templates"):
    print("❌ Папка 'templates' не существует!")
    print("Создаю папку...")
    os.makedirs("templates")
else:
    print("✅ Папка 'templates' существует")

# Проверяем файлы шаблонов
templates = {
    "history.docx": "📋 История болезни",
    "extract.docx": "📄 Выписка", 
    "prescription.docx": "💊 Назначения"
}

for filename, description in templates.items():
    path = f"templates/{filename}"
    if os.path.exists(path):
        print(f"✅ {description}: {filename} - найден")
    else:
        print(f"❌ {description}: {filename} - НЕ НАЙДЕН!")

print("\n📝 Если файлы не найдены, создай их в папке templates/")