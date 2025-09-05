import sys

# Custom exception class
class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_details: sys):
        """
        Constructor (__init__) is called automatically when creating the object.
        It captures the error message, file name, and line number.
        """
        super().__init__(error_message)              # Pass message to base Exception class
        self.error_message = error_message

        # Extract traceback details from sys.exc_info()
        _, _, exc_tb = error_details.exc_info() #details.exc_info() returns a tuple (type, value, traceback)
        self.lineno = exc_tb.tb_lineno#gives the line number where the exception occurred
        self.file_name = exc_tb.tb_frame.f_code.co_filename# gives the file name where the exception occurred

    def __str__(self):
        """
        This method defines what should be printed when the exception is converted to a string.
        """
        return f"Error occurred in script [{self.file_name}] at line [{self.lineno}]: {self.error_message}"


if __name__ == "__main__":
    try:
        a = 1 / 0                       # Force an error
        print("This will not be printed", a)
    except Exception as e:
        # Raise the custom exception with the original error details
        raise NetworkSecurityException(str(e), sys)
