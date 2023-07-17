# import pyautogui
# from time import sleep

# for i in range(43):
#     pyautogui.click(2800, 1500, button="right")  # image
#     pyautogui.click(2850, 1560)  # save image as
#     sleep(1)
#     pyautogui.click(2950, 750)  # save dialog
#     pyautogui.click(2950, 1790)  # next page
#     sleep(1)


import os

def main():
    folder = "C:/Users/satra/Pictures/book"

    files = os.listdir(folder)
    files.sort(key=lambda x: os.path.getctime(f"{folder}/{x}"))

    for count, filename in enumerate(files):
        dst = f"{1001 + count}.jpg"
        src = f"{folder}/{filename}"  # foldername/filename, if .jpg file is outside folder
        dst = f"{folder}/{dst}"

        os.rename(src, dst)


# Driver Code
if __name__ == '__main__':
    main()
