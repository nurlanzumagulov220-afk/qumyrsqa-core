import os
import json
import queue
import sys
import requests
import sounddevice as sd
from vosk import Model, KaldiRecognizer
from datetime import datetime  # <-- Вот та самая недостающая деталь!

# --- НАСТРОЙКИ ---
MODEL_PATH = "model_kz"
TELEGRAM_TOKEN = "8673217255:AAHm_wWr-PoaK3AwTpa4trzzlzmVF5RRf1M"
CHAT_ID = "6885842409"

def send_to_tg(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    try: 
        requests.post(url, json={"chat_id": CHAT_ID, "text": message})
    except Exception as e: 
        print(f"Ошибка отправки в TG: {e}")

# --- ИНИЦИАЛИЗАЦИЯ VOSK ---
print("⏳ Загрузка акустической модели Роя (Vosk)...")
model = Model(MODEL_PATH)
rec = KaldiRecognizer(model, 16000)
q = queue.Queue()

def callback(indata, frames, time, status):
    if status: 
        print(status, file=sys.stderr)
    q.put(bytes(indata))

# --- ЗАПУСК ПРОСЛУШКИ ---
print("🎤 Рой слушает... Скажи 'Тоқта' для остановки!")

try:
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result.get("text", "").lower()
                
                if text:
                    print(f"✅ Принято: {text}")
                    
                    # 1. Записываем в файл для Streamlit (теперь со временем!)
                    with open("voice_alerts.txt", "a", encoding="utf-8") as f:
                        f.write(f"{datetime.now().strftime('%H:%M:%S')} - {text}\n")
                    
                    # 2. Если команда критическая - шлем в ТГ
                    if "тоқта" in text or "стоп" in text:
                        print("🚨 Отправляю SOS в Telegram...")
                        send_to_tg(f"🚨 КРИТИЧЕСКАЯ ОСТАНОВКА: Голосовая команда '{text.upper()}'!")

except KeyboardInterrupt:
    print("\n🛑 Голосовой модуль выключен.")