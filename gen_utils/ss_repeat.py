import pyautogui
import time
import os

region = (1100, 100, 2160, 2000)

c = 0
while True:
  img = pyautogui.screenshot(region=region)
  img.save(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', f'screenshot{c}.png'))

  print(f"took ss {c}")
  c += 1

  time.sleep(2)

