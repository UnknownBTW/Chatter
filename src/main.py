from Chat import main
from pyupdater.client import Client

Client = Client(ClientConfig())
app_update = Client.update_check("Chatter", "0.1.0")

if __name__ == "__main__":

    if app_update:
        app_update.download()
        if app_update.is_downloaded():
            app_update.extract_restart()

    main()
