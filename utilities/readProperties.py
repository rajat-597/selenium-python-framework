import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

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
    
