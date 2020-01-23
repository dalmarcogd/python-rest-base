from decouple import config

DEBUG = config("DEBUG", default=False, cast=bool)
BASE_PATH = config("BASE_PATH", default="/my-app")
