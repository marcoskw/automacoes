import pyautogui
import time

# Quantidade de tempo para a troca de tela
time_duration = 10

while True:
    pyautogui.keyDown('alt')
    time.sleep(.2)
    pyautogui.press('tab')
    time.sleep(.2)
    pyautogui.keyUp('alt')
    time.sleep(time_duration)
