import logging
from logging.handlers import TimedRotatingFileHandler


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


console_handler = logging.StreamHandler()
console_formatter = logging.Formatter('%(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)


file_handler = TimedRotatingFileHandler(
    filename="history/log.",
    when="s",
    # 'when' có thể là 's' (giây), 'm' (phút), 'h' (giờ), 'd' (ngày), 'midnight' hoặc 'w0'-'w6' (ngày trong tuần)
    interval=5,
    backupCount=7
)
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_handler)
logger.addHandler(file_handler)
