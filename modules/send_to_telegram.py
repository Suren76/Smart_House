api_id = 8553553
api_hash = "e41a7ae054a851e4e94b96dc31ffb28e"
bot_token = "5390678403:AAH4NvBfPrhT3o1mxyNjX35w8swTNcP0PYY"


def send_me(filename=None):
    import pyrogram
    from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InlineQuery
    from pyrogram.handlers import CallbackQueryHandler

    app = pyrogram.Client(session_name="my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

    btn1 = InlineKeyboardButton("Yes", callback_data="True")
    btn2 = InlineKeyboardButton("No", callback_data="False")
    markup = InlineKeyboardMarkup([[btn1, btn2]])

    with app:
        app.send_message('Suren_main', "Unknown people")
        app.send_photo("Suren_main", filename)
        app.send_message('Suren_main', "Open door?", reply_markup=markup)

    wait_answer()

    return "send_me end"

def wait_answer():
    import door_unlock
    import pyrogram
    import sys

    bot = pyrogram.Client(session_name="my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

    open_door = False

    @bot.on_callback_query()
    def answer(client, callback_query):
        # print(callback_query.data)
        if callback_query.data == "True":
            door_unlock.door_unlock()

        if callback_query:
            sys.exit()

        # callback_query.answer("Hello", show_alert=True, cache_time=0)
        # callback_query.answer(f"Button contains: '{callback_query.data}'", show_alert=True)
        # print('-inside')

    bot.run()