class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 29245477
    API_HASH = "0abc83883262245c90ca337b7a0375c4"

    CASH_API_KEY = "TN0MB8IYW9M1SZ5J"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgresql+asyncpg://neondb_owner:npg_XbwV4SzKFn7G@ep-steep-feather-a8wgninx-pooler.eastus2.azure.neon.tech/neondb"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1002456565415)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://phrolovaxrobot:p0SFEz825QuqzwTi@cluster0.sy26fqm.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/40eb1ed850cdea274693e.jpg"

    SUPPORT_CHAT = "ANTIKPOPSQUAD0000"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "7689010904:AAGl6l1k14WYV94ddbeVw3X6U2FDyFnaKRE"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "4F4M3PD40GD8"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 7654385403  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
