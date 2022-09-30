import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION")

HNDLR = os.getenv("HNDLR", ".")

Meow = Client(name="STRING_SESSION", api_id = API_ID, api_hash = API_HASH, session_string=STRING_SESSION, plugins=dict(root="Meow.Modules"))
print("Your userbot is started")

hl = HNDLR[0]

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2068551800").split()))
aiohttpsession = aiohttp.ClientSession()