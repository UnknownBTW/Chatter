from Chat import main
from pyupdater.client import Client
from Client_config import APP_NAME, APP_VERSION, UPDATE_URLS, PUBLIC_KEY

class ClientConfig(object):
    APP_NAME = APP_NAME
    APP_VERSION = APP_VERSION
    UPDATE_URLS = UPDATE_URLS
    PUBLIC_KEY = PUBLIC_KEY


Client = Client(ClientConfig())
app_update = Client.update_check("Chatter", "0.1.0")

if __name__ == "__main__":

    if app_update:
        app_update.download()
        if app_update.is_downloaded():
            app_update.extract_restart()

    main()
