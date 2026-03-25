import json
import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer
import requests
from datetime import datetime  # <-- Это нужно для записи времени

# --- НАСТРОЙКИ ТЕЛЕГРАМА (Твои данные уже тут) ---
TELEGRAM_TOKEN = "" # Вставь свой токен снова
CHAT_ID = "" 

def send_to_telegram(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": f"📢 ГОЛОСОВОЙ АЛЕРТ: {text}"}
    try:
        requests.post(url, json=payload)
    except:
        print("❌ Ошибка сети")

# --- ЛОГИКА СЛУХА ---
q = queue.Queue()

def callback(indata, frames, time, status):
    q.put(bytes(indata))

# Загружаем модель (папка должна называться model_kz)
model = Model("model_kz")
rec = KaldiRecognizer(model, 16000)

print("🎤 РОЙ СЛУШАЕТ... Говори 'қауіп' или 'тоқта'")

with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                       channels=1, callback=callback):
    while True:
        data = q.get()
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            text = result.get("text", "")
            
            if text:
                print(f"🗣️ Распознано: {text}")
                
                # Если сказал "қауіп" (опасность)
                if "қауіп" in text:
                    msg = "⚠️ Обнаружена ОПАСНОСТЬ (Қауіп)!"
                    print(msg)
                    send_to_telegram(msg)
                    # ЗАПИСЬ В ФАЙЛ ДЛЯ ДАШБОРДА
                    with open("voice_alerts.txt", "a", encoding="utf-8") as f:
                        f.write(f"{datetime.now().strftime('%H:%M:%S')} - {msg}\n")
                    
                # Если сказал "тоқта" (стоп)
                if "тоқта" in text:
                    msg = "🛑 Требование ОСТАНОВКИ работ (Тоқта)!"
                    print(msg)
                    send_to_telegram(msg)
                    # ЗАПИСЬ В ФАЙЛ ДЛЯ ДАШБОРДА
                    with open("voice_alerts.txt", "a", encoding="utf-8") as f:
                        f.write(f"{datetime.now().strftime('%H:%M:%S')} - {msg}\n")
