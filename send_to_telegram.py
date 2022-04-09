from pyrogram import Client


def send_me(filename):
    api_id = 8553553
    api_hash = "e41a7ae054a851e4e94b96dc31ffb28e"

    with Client("my_account", api_id, api_hash) as app:
        app.send_message("Suren_main", "Unknown people")
        app.send_photo("Suren_main", filename)

