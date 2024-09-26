import random
import string


def generate_random_string():
    # Tạo ra một chuỗi gồm các chữ cái và số
    chars = string.ascii_lowercase + string.digits
    # Tạo một chuỗi 5 ký tự, thêm dấu '-' và 4 ký tự nữa
    random_string = ''.join(random.choices(chars, k=5)) + '-' + ''.join(random.choices(chars, k=4))
    return random_string
