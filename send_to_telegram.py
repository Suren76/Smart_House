# from pyrogram import Client
# from pyrogram.types import InlineKeyboardButton
#
#
# def send_me(filename):
#     api_id = 8553553
#     api_hash = "e41a7ae054a851e4e94b96dc31ffb28e"
#
#     with Client("my_account", api_id, api_hash) as app:
#         app.send_message("Suren_main", "1")
#         # app.send_photo("Suren_main", filename)
#
#         btn1 = InlineKeyboardButton("btn1", 'btn1')
#         btn2 = InlineKeyboardButton("btn2", 'btn2')
#
#         @app.on_callback_query()
#         def answer(client, callback_query):
#             callback_query.answer(f"Button contains: '{callback_query.data}'", show_alert=True)
#
#         answer('me', "44")
#
#
#         # print(app.get_history("me", limit=2))
#
# send_me("tt")

from pyrogram import Client

app = Client("my_account", api_id=8553553, api_hash="e41a7ae054a851e4e94b96dc31ffb28e")


@app.on_callback_query()
def answer(client, callback_query):
    callback_query.answer(f"Button contains: '{callback_query.data}'", show_alert=True)


app.run()  # Automatically start() and idle()