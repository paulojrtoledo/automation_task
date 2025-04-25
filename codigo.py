import pyautogui
import time 

# pyautogui.click -> click somewhere
# pyautogui.press -> press a single key
# pyautogui.write -> type a text
# pyautogui.hotkey -> press a combination of keys

pyautogui.PAUSE = 0.5

# Step 1: Open the company's system - https://dlp.hashtagtreinamentos.com/python/intensivao/login
# open Chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# type the website
testsite = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(testsite)
pyautogui.press("enter")

print("Waiting 10 seconds for the page to load")
time.sleep(2)
print("Continuing the script...")

# Step 2: Log in
pyautogui.click(x=1021, y=411)
pyautogui.write("emaildeteste@gmail.com")
pyautogui.press("tab")
pyautogui.write("senhadeteste")
pyautogui.press("enter")

time.sleep(2)

# Step 3: Import the database
import pandas as pd
tabela = pd.read_csv("produtos.csv")

# Step 4: Register one product
# Step 5: Repeat for all products
for linha in tabela.index:
    pyautogui.click(x=1000, y=294)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)

    pyautogui.press("tab")
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)

    pyautogui.press("tab")
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)

    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)

    pyautogui.press("tab")
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)

    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)

    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])

    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(1000)

# pyautogui -> automate tasks with Python
