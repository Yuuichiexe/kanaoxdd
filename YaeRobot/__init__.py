

import logging
import os
import sys
import time
import spamwatch
import aiohttp

from Python_ARQ import ARQ
import telegram.ext as tg
from redis import StrictRedis
from pyrogram import Client, errors
from telethon.sessions import MemorySession
from telethon import TelegramClient
from aiohttp import ClientSession
from YaeRobot.hacking_script import PM_START_TEXT
from redis import StrictRedis

StartTime = time.time()

# enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO)

LOGGER = logging.getLogger("[YaeRobot]")

# if version < 3.6, stop bot.
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    LOGGER.error(
        "You MUST have a python version of at least 3.6! Multiple features depend on this. Bot quitting."
    )
    quit(1)

ENV = bool(os.environ.get('ENV', True))

if ENV:
    TOKEN = os.environ.get('TOKEN', "")

    try:
        OWNER_ID = int(os.environ.get('OWNER_ID', 5531584953))
    except ValueError:
        raise Exception("Your OWNER_ID env variable is not a valid integer.")

    JOIN_LOGGER = os.environ.get('JOIN_LOGGER', -1001703672408)
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "XtheAnonymous")

    try:
        DRAGONS = set(int(x) for x in os.environ.get("DRAGONS", "").split())
        DEV_USERS = set(int(x) for x in os.environ.get("DEV_USERS", "").split())
    except ValueError:
        raise Exception(
            "Your sudo or dev users list does not contain valid integers.")

    try:
        DEMONS = set(int(x) for x in os.environ.get("DEMONS", "").split())
    except ValueError:
        raise Exception(
            "Your support users list does not contain valid integers.")

    try:
        WOLVES = set(int(x) for x in os.environ.get("WOLVES", "").split())
    except ValueError:
        raise Exception(
            "Your whitelisted users list does not contain valid integers.")

    try:
        TIGERS = set(int(x) for x in os.environ.get("TIGERS", "").split())
    except ValueError:
        raise Exception(
            "Your tiger users list does not contain valid integers.")

    INFOPIC = bool(os.environ.get('INFOPIC', True))
    EVENT_LOGS = os.environ.get('EVENT_LOGS', None)
    WEBHOOK = bool(os.environ.get('WEBHOOK', False))
    ARQ_API_URL = os.environ.get("ARQ_API_URL", None)
    ARQ_API_KEY = os.environ.get("ARQ_API_KEY", None)
    URL = os.environ.get('URL', "")  # Does not contain token
    PORT = int(os.environ.get('PORT', 5000))
    CERT_PATH = os.environ.get("CERT_PATH")
    API_ID = os.environ.get('API_ID', 4665778)
    API_HASH = os.environ.get('API_HASH', "10e3ed833b0d09699973420d45359409")
    DB_URI = os.environ.get('db_uri','postgres://griyemya:9Rok1yXyWcXMywkOTJx0w6Qei9qOKbvL@ziggy.db.elephantsql.com/griyemya')
    SQLALCHEMY_DATABASE_URI = os.environ.get('')
    DONATION_LINK = os.environ.get('DONATION_LINK')
    LOAD = os.environ.get("LOAD", "").split()
    NO_LOAD = os.environ.get("NO_LOAD", "rss").split()
    DEL_CMDS = bool(os.environ.get('DEL_CMDS', False))
    STRICT_GBAN = bool(os.environ.get('STRICT_GBAN', True))
    WORKERS = int(os.environ.get('WORKERS', 8))
    BAN_STICKER = os.environ.get('BAN_STICKER',
                                 'CAADAgADOwADPPEcAXkko5EB3YGYAg')
    ALLOW_EXCL = os.environ.get('ALLOW_EXCL', 'True')
    CASH_API_KEY = os.environ.get('CASH_API_KEY', None)
    TIME_API_KEY = os.environ.get('TIME_API_KEY', None)
    AI_API_KEY = os.environ.get('AI_API_KEY', None)
    WALL_API = os.environ.get('WALL_API', None)
    SUPPORT_CHAT = os.environ.get('SUPPORT_CHAT', "@Yae_Support")
    SPAMWATCH_SUPPORT_CHAT = os.environ.get('SPAMWATCH_SUPPORT_CHAT', None)
    SPAMWATCH_API = os.environ.get('SPAMWATCH_API', None)
    REPOSITORY = os.environ.get("REPOSITORY", "")
    REDIS_URL = os.environ.get("REDIS_URL")
    IBM_WATSON_CRED_URL = os.environ.get("IBM_WATSON_CRED_URL", None)
    IBM_WATSON_CRED_PASSWORD = os.environ.get("IBM_WATSON_CRED_PASSWORD", None)
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", "./")
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", "./")
    TELEGRAPH_SHORT_NAME = os.environ.get("TELEGRAPH_SHORT_NAME", "lightYagami")
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    STRING_SESSION = os.environ.get("STRING_SESSION", None)
    BOT_NAME = os.environ.get("BOT_NAME", 'YaeRobot') # Name Of your Bot.4
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "YaeRobot") # Bot Username
    OPENWEATHERMAP_ID = os.environ.get("OPENWEATHERMAP_ID", "") # From:- https://openweathermap.org/api
    LOG_GROUP_ID = os.environ.get('LOG_GROUP_ID', '-1001703672408')
    BOT_ID = 5434671964
    STRICT_GMUTE = bool(os.environ.get('STRICT_GMUTE', True))
    MONGO_DB_URI = os.environ.get("MONGO_DB_URI", 'mongodb+srv://ok:lol@cluster1.udhzs7r.mongodb.net/?retryWrites=true&w=majority')
    REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None) # From:- https://www.remove.bg/ 
    STRING_SEESSOIN = os.environ.get("STRING_SEESSOIN", None)

    try:
        BL_CHATS = set(int(x) for x in os.environ.get('BL_CHATS', "").split())
    except ValueError:
        raise Exception(
            "Your blacklisted chats list does not contain valid integers.")

else:
    from YaeRobot.config import Development as Config
    TOKEN = Config.TOKEN

    try:
        OWNER_ID = int(Config.OWNER_ID)
    except ValueError:
        raise Exception("Your OWNER_ID variable is not a valid integer.")

    JOIN_LOGGER = Config.JOIN_LOGGER
    OWNER_USERNAME = Config.OWNER_USERNAME

    try:
        DRAGONS = set(int(x) for x in Config.DRAGONS or [])
        DEV_USERS = set(int(x) for x in Config.DEV_USERS or [])
    except ValueError:
        raise Exception(
            "Your sudo or dev users list does not contain valid integers.")

    try:
        DEMONS = set(int(x) for x in Config.DEMONS or [])
    except ValueError:
        raise Exception(
            "Your support users list does not contain valid integers.")

    try:
        WOLVES = set(int(x) for x in Config.WOLVES or [])
    except ValueError:
        raise Exception(
            "Your whitelisted users list does not contain valid integers.")

    try:
        TIGERS = set(int(x) for x in Config.TIGERS or [])
    except ValueError:
        raise Exception(
            "Your tiger users list does not contain valid integers.")

    EVENT_LOGS = Config.EVENT_LOGS
    WEBHOOK = Config.WEBHOOK
    URL = Config.URL
    PORT = Config.PORT
    CERT_PATH = Config.CERT_PATH
    API_ID = Config.API_ID
    API_HASH = Config.API_HASH

    DB_URI = Config.SQLALCHEMY_DATABASE_URI
    REDIS_URL = Config.REDIS_URL
    DONATION_LINK = Config.DONATION_LINK
    LOAD = Config.LOAD
    NO_LOAD = Config.NO_LOAD
    DEL_CMDS = Config.DEL_CMDS
    STRICT_GBAN = Config.STRICT_GBAN
    WORKERS = Config.WORKERS
    BAN_STICKER = Config.BAN_STICKER
    ALLOW_EXCL = Config.ALLOW_EXCL
    CASH_API_KEY = Config.CASH_API_KEY
    TIME_API_KEY = Config.TIME_API_KEY
    AI_API_KEY = Config.AI_API_KEY
    WALL_API = Config.WALL_API
    SUPPORT_CHAT = Config.SUPPORT_CHAT
    SPAMWATCH_SUPPORT_CHAT = Config.SPAMWATCH_SUPPORT_CHAT
    SPAMWATCH_API = Config.SPAMWATCH_API
    INFOPIC = Config.INFOPIC
    ARQ_API_URL = Config.ARQ_API_URL
    ARQ_API_KEY = Config.ARQ_API_KEY

    BOT_USERNAME = Config.BOT_USERNAME
    OPENWEATHERMAP_ID = Config.OPENWEATHERMAP_ID

    REM_BG_API_KEY = Config.REM_BG_API_KEY

    try:
        BL_CHATS = set(int(x) for x in Config.BL_CHATS or [])
    except ValueError:
        raise Exception(
            "Your blacklisted chats list does not contain valid integers.")

DRAGONS.add(OWNER_ID)
DEV_USERS.add(OWNER_ID)


if not SPAMWATCH_API:
    sw = None
    LOGGER.warning("SpamWatch API key missing! recheck your config.")
else:
    sw = spamwatch.Client(SPAMWATCH_API)


session_name = TOKEN.split(":")[0]
pgram = Client(
    session_name,
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=TOKEN,
)

#install aiohttp session
print("[YaeRobot]: Initializing AIOHTTP Session")
aiohttpsession = ClientSession() 

#install arq
print("[YaeRobot]: Initializing ARQ Client")
arq = (ARQ_API_URL, ARQ_API_KEY, aiohttpsession)
updater = tg.Updater(TOKEN, workers=WORKERS, use_context=True)
telethn = TelegramClient(MemorySession(), API_ID, API_HASH)
pbot = Client("YaeRobotpbot", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)

dispatcher = updater.dispatcher

async def get_entity(client, entity):
    entity_client = client
    if not isinstance(entity, Chat):
        try:
            entity = int(entity)
        except ValueError:
            pass
        except TypeError:
            entity = entity.id
        try:
            entity = await client.get_chat(entity)
        except (PeerIdInvalid, ChannelInvalid):
            for pgram in apps:
                if pgram != client:
                    try:
                        entity = await pgram.get_chat(entity)
                    except (PeerIdInvalid, ChannelInvalid):
                        pass
                    else:
                        entity_client = pgram
                        break
            else:
                entity = await pgram.get_chat(entity)
                entity_client = pgram
    return entity, entity_client

apps = [pgram]

DRAGONS = list(DRAGONS) + list(DEV_USERS)
DEV_USERS = list(DEV_USERS)
WOLVES = list(WOLVES)
DEMONS = list(DEMONS)
TIGERS = list(TIGERS)

# Load at end to ensure all prev variables have been set
from YaeRobot.modules.helper_funcs.handlers import (CustomCommandHandler,
                                                        CustomMessageHandler,
                                                        CustomRegexHandler)

# make sure the regex handler can take extra kwargs
tg.RegexHandler = CustomRegexHandler
tg.CommandHandler = CustomCommandHandler
tg.MessageHandler = CustomMessageHandler

REDIS_URL = "redis://xelcius:Xelcius~97@redis-11612.c240.us-east-1-3.ec2.cloud.redislabs.com:11612"


REDIS = StrictRedis.from_url(REDIS_URL, decode_responses=True)

try:

    REDIS.ping()

    LOGGER.info("Connecting To Redis Database")

except BaseException:

    raise Exception("[ERROR]: Your Redis Database Is Not Alive, Please Check Again.")

finally:

   REDIS.ping()
