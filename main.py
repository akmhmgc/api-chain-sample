from fastapi import FastAPI

app = FastAPI()

greetings = {
    "ja": {
        "morning": "おはようございます",
        "noon": "こんにちは",
        "night": "こんばんは"
    },
    "en": {
        "morning": "Good morning",
        "noon": "Good afternoon",
        "night": "Good evening"
    },
    "fr": {
        "morning": "Bonjour",
        "noon": "Bon après-midi",
        "night": "Bonsoir"
    },
    "de": {
        "morning": "Guten Morgen",
        "noon": "Guten Tag",
        "night": "Guten Abend"
    },
    "es": {
        "morning": "Buenos días",
        "noon": "Buenas tardes",
        "night": "Buenas noches"
    },
    "it": {
        "morning": "Buongiorno",
        "noon": "Buon pomeriggio",
        "night": "Buona sera"
    },
    "pt": {
        "morning": "Bom dia",
        "noon": "Boa tarde",
        "night": "Boa noite"
    },
    "ru": {
        "morning": "Доброе утро",
        "noon": "Добрый день",
        "night": "Добрый вечер"
    },
    "zh": {
        "morning": "早上好",
        "noon": "下午好",
        "night": "晚上好"
    },
    "ar": {
        "morning": "صباح الخير",
        "noon": "مساء الخير",
        "night": "مساء الخير"
    },
    "ko": {
        "morning": "안녕하세요",
        "noon": "안녕하세요",
        "night": "안녕하세요"
    },
}

@app.get("/")
def read_root(time: str = 'morning', country: str = "ja"):
    if country in greetings and time in greetings[country]:
        return {"greeting": greetings[country][time]}
    else:
        return {"error": "Invalid time or country"}
