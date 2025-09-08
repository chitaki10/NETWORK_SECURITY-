import sys
from networksecurity.logging import logger

# Custom exception class
class NetworkSecurityException(Exception):
    def __init__(self, error_message):
        super().__init__(error_message)
        self.error_message = error_message
        # Extract traceback details
        _, _, exc_tb = sys.exc_info()
        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return f"Error occurred in script [{self.file_name}] at line [{self.lineno}]: {self.error_message}"


if __name__ == "__main__":
    try:
        logger.logging.info("Enter the try block")
        a = 1 / 0
        print("This will not be printed", a)
    except Exception as e:
        raise NetworkSecurityException(str(e))
