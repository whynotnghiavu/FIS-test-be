import logging
from logging.handlers import TimedRotatingFileHandler


from colorama import Fore, Style, init
init(autoreset=True)


class ColoredFormatter(logging.Formatter):
    COLOR_MAP = {
        'DEBUG': Fore.BLUE,
        'INFO': Fore.GREEN,
        'WARNING': Fore.YELLOW,
        'ERROR': Fore.RED,
        'CRITICAL': Fore.RED + Style.BRIGHT
    }

    def format(self, record):
        color = self.COLOR_MAP.get(record.levelname, Fore.WHITE)
        message = super().format(record)
        return color + message + Style.RESET_ALL


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


console_handler = logging.StreamHandler()
console_formatter = ColoredFormatter('%(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)


file_handler = TimedRotatingFileHandler(
    "history/log.log",
    when="m",
    # 'when' có thể là 's' (giây), 'm' (phút), 'h' (giờ), 'd' (ngày), 'midnight' hoặc 'w0'-'w6' (ngày trong tuần)
    interval=5,
    backupCount=7
)
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
