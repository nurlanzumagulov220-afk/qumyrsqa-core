import telebot
import os

bot = telebot.TeleBot("8673217255:AAHm_wWr-PoaK3AwTpa4trzzlzmVF5RRf1M")

@bot.message_handler(commands=['stop'])
def handle_stop(message):
    # Пишем записку для Дашборда
    with open("web_control.txt", "w") as f:
        f.write("STOP")
    bot.reply_to(message, "🛑 СИГНАЛ ПЕРЕДАН НА ДАШБОРД!")

print("🤖 БОТ ЗАПУЩЕН! Напиши /stop в телеграм")
bot.polling()