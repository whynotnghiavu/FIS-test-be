import os
import subprocess
from time import sleep
# prettier --write  file_path
# pip install pyautogui
import pyautogui


def format(directory):
    exclude_dirs = [".git", "node_modules", "__pycache__"]
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]

        for file in files:
            # Nếu file có đuôi là ".code-workspace" thì bỏ qua continue

            if file.endswith(".code-workspace"):
                continue

            # file_path = os.path.join(root, file)
            # print(f"Processing file: {file_path}")
            # subprocess.run(["code", file_path], check=True, shell=True)
            # sleep(1)

            # if os.name == 'nt':
            #     pyautogui.hotkey('alt', 'shift', 'f')
            # elif os.name == 'posix':
            #     pyautogui.hotkey('ctrl', 'shift', 'i')
            # sleep(1)

            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                print(f"Processing file: {file_path}")
                subprocess.run(["code", file_path], check=True, shell=True)
                sleep(1)

                if os.name == 'nt':
                    pyautogui.hotkey('alt', 'shift', 'f')
                elif os.name == 'posix':
                    pyautogui.hotkey('ctrl', 'shift', 'i')
                sleep(1)


if __name__ == "__main__":
    paths = [
           r"C:\Users\vvn20206205\Downloads\Nghia\Git\whynotnghiavu\FIS-test-be\contents\code\python",
    ]
    for path in paths:
        format(path)
