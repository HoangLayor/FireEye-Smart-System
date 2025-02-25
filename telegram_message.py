import asyncio
import os
import telegram

def send_message( ):
    try:
        my_token = os.getenv("TELEGRAM_TOKEN")
        user_id = os.getenv("TELEGRAM_USER_ID")
        bot = telegram.Bot(token=my_token)
        asyncio.run(bot.sendMessage(chat_id= user_id, text="Xin lưu ý rằng sự an toàn của bạn là ưu tiên hàng đầu của chúng tôi. Hãy chủ động và thực hiện các biện pháp cần thiết để đảm bảo an toàn."))
    except Exception as ex:
        print("can't not send message to telegram " , ex )
def send_warning( img_path= "warning.png" ):
    try:
        my_token = os.getenv("TELEGRAM_TOKEN")
        user_id = os.getenv("TELEGRAM_USER_ID")
        bot = telegram.Bot(token=my_token)
        asyncio.run(bot.sendPhoto( chat_id= user_id, photo= img_path , caption="Cảnh báo có cháy!"))
        print( "send success!" )
    except Exception as ex:
        print("can't not send message to telegram " , ex )


