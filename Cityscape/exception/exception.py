import sys
from Cityscape.logging.logger import DualLogger

class CityscapeException(Exception):
    def __init__(self, err_message, error_details: sys):
        self.err_message = err_message
        _, _, exc_tb = error_details.exc_info()
        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(self.file_name, self.lineno, str(self.err_message))

if __name__ == '__main__':
    try:
        a = 1 / 0
        print("this will not be printed", a)
    except Exception as e:
        logger = DualLogger().get_logger()
        logger.error("An error occurred", exc_info=True)
        raise CityscapeException(e, sys)