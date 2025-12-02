import logging
import os

class LogGen:

    @staticmethod
    def loggen():

        # Ensure Logs folder exists
        os.makedirs("Logs", exist_ok=True)

        # Use a custom named logger
        logger = logging.getLogger("automation")
        logger.setLevel(logging.INFO)

        # Prevent adding multiple handlers in pytest
        if not logger.handlers:
            file_handler = logging.FileHandler(".\\Logs\\automation.log")
            formatter = logging.Formatter(
                '%(asctime)s: %(levelname)s: %(message)s',
                datefmt='%m/%d/%Y %I:%M:%S %p'
            )
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        return logger
