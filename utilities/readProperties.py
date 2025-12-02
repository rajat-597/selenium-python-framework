import configparser
import os

config = configparser.RawConfigParser()
# Get project root (two levels up from this file)
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Build correct absolute path: <PROJECT_ROOT>/Configurations/config.ini
config_path = os.path.join(project_root, "Configurations", "config.ini")
config.read(config_path)
#config.read(".\\Configurations\\config.ini") # for windows


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
    
