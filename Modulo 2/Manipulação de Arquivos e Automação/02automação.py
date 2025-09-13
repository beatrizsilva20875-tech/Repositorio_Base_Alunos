# importar a biblioteca pyautogui
import pyautogui

# Criamos um loop de 10 repetições para mover
# o mouse na forma de quadrado que se move 
for i in range(10):
    pyautogui.moveTo(100 + 10 * 1, 100 + 10 * 1,duration=0.25)
    pyautogui.moveTo(200 + 10 * 1, 100 + 10 * 1,duration=0.25)
    pyautogui.moveTo(200 + 10 * 1, 200 + 10 * 1,duration=0.25)
    pyautogui.moveTo(100 + 10 * 1, 200 + 10 * 1,duration=0.25)