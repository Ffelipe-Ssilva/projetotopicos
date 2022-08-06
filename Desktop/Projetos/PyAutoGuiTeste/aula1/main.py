import pyautogui
import pyperclip
import time
import pandas
pyautogui.PAUSE=1

pyautogui.hotkey("win")
pyautogui.write("edge")
pyautogui.hotkey("enter")
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga")
pyautogui.hotkey("ctrl","v")
pyautogui.press("enter")
time.sleep(5)
pyautogui.click(x=2275, y=146)
pyautogui.press("enter")
pyautogui.press("enter")
pyautogui.click(x=2278, y=206)
pyautogui.click(x=3247, y=26)
pyautogui.click(x=3028, y=430)
time.sleep(10)
#arq baixado agr é excel
tabela=pandas.read_excel(r"C:\Users\felipe.silva\Downloads\Vendas - Dez.xlsx")
#trocar por display
print(tabela)
quantidade=tabela["Quantidade"].sum()
faturamento=tabela["Valor Final"].sum()
print(quantidade)
print(faturamento)

pyautogui.hotkey("ctrl","t")
pyperclip.copy("https://mail.google.com/mail/u/1/#inbox")
pyautogui.hotkey("ctrl","v")
pyautogui.press("enter")
time.sleep(5)
pyautogui.click(x=2018, y=46)
pyautogui.write("ffelipe.ssilva02@gmail.com")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.write("Resultados de Vendas")
pyautogui.press("tab")

texto= f"""
Prezados, bom dia.
Segue resultados de Vendas
Quantidade: {quantidade} unidades
Faturamento: R${faturamento}

Atenciosamente, Carteiro.
"""
pyperclip.copy(texto)
pyautogui.hotkey("ctrl","v")
pyautogui.click(x=2891, y=640)










