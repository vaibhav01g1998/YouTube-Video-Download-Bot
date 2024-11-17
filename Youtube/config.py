import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7563516045:AAE9TqsnWELah_w6TSm0TxIz5LphB4pY5Hw")
    API_ID = int(os.environ.get("API_ID", 29231699))
    API_HASH = os.environ.get("API_HASH", "11b7123fed095735b0961ec3c151be44")
    #Add your channel id. For force Subscribe.
    CHANNEL = os.environ.get("CHANNEL", "")
    #Skip or add your proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ''
