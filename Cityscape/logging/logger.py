import logging 
import os
from datetime import datetime


class DualLogger:
    def __init__(self, log_dir="logs", log_level=logging.DEBUG):
        log_file=f"{datetime.now().strftime('%Y-%m-%d')}.log"
        self.log_dir=os.path.join(os.getcwd(),log_dir, log_file)
        os.makedirs(self.log_dir, exist_ok=True)
        log_file_path=os.path.join(self.log_dir, log_file)
        self.logger=logging.getLogger("dual_logger")
        self.logger.setLevel(log_level)
        formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        #file handler
        file_handler=logging.FileHandler(log_file_path)
        file_handler.setLevel(log_level)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        #stream handler/comsole handler
        stream_handler=logging.StreamHandler()
        stream_handler.setLevel(log_level)  
        stream_handler.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))
        self.logger.addHandler(stream_handler)


    def get_logger(self):
        return self.logger