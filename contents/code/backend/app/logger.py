import logging

# Kiến thức về LOG


def setup_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_formatter)

    file_handler = logging.handlers.TimedRotatingFileHandler(
        "history/log.log",
        when="m",
        # 'when' có thể là 's' (giây), 'm' (phút), 'h' (giờ), 'd' (ngày), 'midnight' hoặc 'w0'-'w6' (ngày trong tuần)
        interval=5,
        backupCount=7,
        delay=True
    )

    file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_formatter)

    if not logger.hasHandlers():
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger
