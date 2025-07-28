
import random
import telebot
import requests

TOKEN = "7985943305:AAFtN5o-lSA_JBPcghgL8y4JL4qAtGGQ0sM"
bot = telebot.TeleBot(TOKEN)

LIARA_API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySUQiOiI2ODg0ZWIwM2QyYmEwZGFhYWUyODk1MjMiLCJ0eXBlIjoiYXV0aCIsImlhdCI6MTc1MzU2ODkwMn0.joR3U8IVF1wlnRmLXgzdRbOoe_QGMko8wDcuVMsztsA"
LIARA_ENDPOINT = "https://api.liara.ai/v1/chat/completions"

ara_images = [
    "https://raw.githubusercontent.com/Djedihub/aradbot/refs/heads/main/images/ara1.png",
    "https://raw.githubusercontent.com/Djedihub/aradbot/refs/heads/main/images/ara2.png",
    "https://raw.githubusercontent.com/Djedihub/aradbot/refs/heads/main/images/ara3.png",
    "https://raw.githubusercontent.com/Djedihub/aradbot/refs/heads/main/images/ara4.png",
    "https://raw.githubusercontent.com/Djedihub/aradbot/refs/heads/main/images/ara5.png",
    "https://raw.githubusercontent.com/Djedihub/aradbot/refs/heads/main/images/ara6.png"
]

system_prompt = (
    "شما یک شخصیت هوشمند با نام آرا هستی که در نقش مشاور دکوراسیون داخلی شرکت آرادچوب فعالیت می‌کنی. "
    "با لحنی صمیمی و حرفه‌ای به کاربران پاسخ می‌دی. "
    "اطلاعات تخصصی محصولات آرادچوب را می‌دانی و فقط در زمینه دکوراسیون و محصولات پاسخ می‌دهی. "
    "اگر سوالی خارج از این موضوع پرسیده شد، کاربر را به شماره ۰۱۷۳۲۱۴۵۰۲۰ ارجاع بده. "
    "در پاسخ‌ها از اطلاعات دقیق مثل ابعاد محصولات، جنس، کاربرد و نکات نصب استفاده کن."
)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    img = random.choice(ara_images)
    caption = "سلام عزیز دل 😍 من آرا هستم، مشاور دکوراسیون داخلی برند آرادچوب. چه کمکی از دستم برمیاد؟"
    bot.send_photo(message.chat.id, img, caption=caption)

@bot.message_handler(func=lambda m: True)
def chat_with_ai(message):
    img = random.choice(ara_images)
    user_message = message.text

    headers = {
        "Authorization": f"Bearer {LIARA_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]
    }

    try:
        response = requests.post(LIARA_ENDPOINT, json=data, headers=headers)
        response_json = response.json()
        reply = response_json['choices'][0]['message']['content']
    except Exception as e:
        reply = "در حال حاضر نمی‌تونم پاسخ بدم، لطفاً بعداً تلاش کن یا با شماره ۰۱۷۳۲۱۴۵۰۲۰ تماس بگیر."

    bot.send_photo(message.chat.id, img, caption=reply)

bot.infinity_polling()
