import pyautogui
import webbrowser
import time

# Passo1: Abrir o youtube com uma musica especifica
url = "https://youtu.be/fukGbiPuBjU?si=0d2NOrBURY2C8b72"
webbrowser.open(url)
# Passo2 aguardar o carregamento da página 
time.sleep(5) # Ajustar de acordor com a velocidade da internet utilizada

# Passo3: Garantir que o video comece(apertar o espaco para o play)
pyautogui.press("space")# toca ou pausa o video
