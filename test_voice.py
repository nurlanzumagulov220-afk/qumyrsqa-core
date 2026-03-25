from vosk import Model
import os

# Проверяем, существует ли папка
if os.path.exists("model_kz"):
    print("✅ Папка model_kz найдена!")
    # Пытаемся загрузить модель
    model = Model("model_kz")
    print("🔥 Ура! Модель успешно загружена, ИИ готов слушать!")
else:
    print("❌ Ошибка: Папка model_kz не найдена в директории проекта.")