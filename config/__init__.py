import os, dotenv


dotenv.load_dotenv()


TG_TOKEN: str = os.getenv('TG_TOKEN')

if not TG_TOKEN:
    raise ValueError('Telegram token missed!')