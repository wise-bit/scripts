import pyautogui
import time


def main():
    move_amount = 20
    x, y = pyautogui.position()
    while True:
        pyautogui.moveTo(x - move_amount, y - move_amount, duration=0.25)
        time.sleep(1)
        pyautogui.moveTo(x + move_amount, y + move_amount, duration=0.25)
        time.sleep(1)
        pyautogui.keyDown("w")
        pyautogui.keyUp("w")
        time.sleep(7.5)


if __name__ == "__main__":
    main()
