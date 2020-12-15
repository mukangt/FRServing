'''
Author: mukangt
Date: 2020-12-09 10:57:32
LastEditors: mukangt
LastEditTime: 2020-12-15 14:32:38
Description: 
'''

import time
import logging
import logging.handlers

from conf.config import Config

start_time = time.localtime()

exec_day = time.strftime('%Y-%m-%d', start_time)  # Execution date
exec_hour = time.strftime('%H', start_time)
exec_minute = time.strftime('%M', start_time)

fmt_str = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=fmt_str)
log_file_handler = logging.handlers.TimedRotatingFileHandler(Config.LOG_PATH,
                                                             when='D',
                                                             interval=1,
                                                             backupCount=3)
log_file_handler.suffix = "%Y%m%d_%H%M%S.log"
log_file_handler.setLevel(logging.INFO)
formatter = logging.Formatter(fmt_str)
log_file_handler.setFormatter(formatter)
logging.getLogger('').addHandler(log_file_handler)
logging.info('exec_day :{}, exec_hour :{}, exec_minute :{}'.format(
    exec_day, exec_hour, exec_minute))
