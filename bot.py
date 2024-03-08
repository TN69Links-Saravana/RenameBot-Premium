import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6524778568:AAHJCr-nm6dUhhiR8G1zwVTOt81pxRKEETg")

API_ID = int(os.environ.get("API_ID", "24482734"))

API_HASH = os.environ.get("API_HASH", "5ccf6a58166cc047a7eba01c5dbc930c")

STRING = os.environ.get("STRING", "1BVtsOJwBu6WG3tnODLTIBAD7YeT6xcRp3I0ruJOGjhR5SU4pgoz1JFo6UUMjwKOo5C8dck11QH45bAx4lipz6ySFv2EhY2aKC7eTrcMbxv5u9CbkjaSsUf0WD4P9SuoKXa8_qLh04Rwtq9iwA0N-DNsL7qMRIaAMmKRfBvSheNSHwu6rsJVB6p3wLHAXmgHqnW8Z7K5tHU9-1dzilfUFRnMQqZk3VilBv_dJEukuGBcJOq10Sq71-n0LKqj8LCOrjppIe6MEbAn0ZfnzeE0PKGPT5BrCTzqfqUxOnI_DULBaas-1aeJrifgh94XcmytjMihbA1FPST0IgNrBpPy9Yo9F-BQwq5g=")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
