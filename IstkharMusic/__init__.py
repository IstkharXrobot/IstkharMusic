from IstkharMusic.core.bot import Istkhar
from IstkharMusic.core.dir import dirr
from IstkharMusic.core.git import git
from IstkharMusic.core.userbot import Userbot
from IstkharMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Istkhar()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
