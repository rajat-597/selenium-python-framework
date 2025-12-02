import configparser
import os

config = configparser.RawConfigParser()
# Correct cross-platform path
config_path = os.path.join(os.path.dirname(__file__), "config.ini")
config.read(config_path)
#config.read(".\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get("common info", "BASE_URL")
        return url
    
    @staticmethod
    def getUsername():
        userName = config.get('common info', "USERNAME")
        return userName

    @staticmethod
    def getPassword():
        password = config.get('common info', "PASSWORD")
        return password
    
