from pyrogram import Client, types
from config import *


app = Client("a", API_ID, API_HASH)


@app.on_message()
def send_dice(client, message: types.Message):
    if message.from_user.id == user_id and message.text in ['.1', '.2', '.3', '.4', '.5', '.6']:
        app.send_dice(chat_id=chat_id)
        ev = [i for i in app.get_chat_history(chat_id=chat_id, limit=1)][0]
        if ev.dice.emoji == "🎲":
            while ev.dice.value != int(message.text[1]):
                app.delete_messages(chat_id=chat_id, message_ids=ev.id)
                app.send_dice(chat_id=chat_id)
                ev = [i for i in app.get_chat_history(chat_id=chat_id, limit=1)][0]
                print(ev.dice.value)


app.run()
