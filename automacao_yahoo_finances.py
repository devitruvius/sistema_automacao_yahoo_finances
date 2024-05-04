import yfinance
import pyautogui as py
import pyperclip as pc
import time


# Seeking stock quotes (ex: PETR4.SA)
ticker = input('Digite o código da ação: ')
dados = yfinance.Ticker(ticker)

dados.history()

# Setting up the historical period
tabela = dados.history("6mo")

# Selecting only the Closing column (Close)
fechamento = tabela.Close

# Generating a line chart
fechamento.plot()

# Generating the statistics
maxima = fechamento.max()
minima = fechamento.min()
atual = fechamento[-1]

# Creating the email to be sent
destinatario = "seuemail@gmail.com"
assunto = "Análise diária"
mensagem = f"""
Bom dia,
Segue abaixo as análises da ação {ticker} dos últimos seis meses:
Cotação máxima: R${round(maxima,2)}
Cotação mínima: R${round(minima,2)}
Cotação atual: R${round(atual,2)}
Atenciosamente,
Seu nome.
"""

# Automating the sending process
# Configuring a pause between PyAutoGUI actions
py.PAUSE = .6

py.hotkey("alt","tab")

# Opening a new tab
py.hotkey("ctrl", "t")

# Copying the Gmail address to the clipboard
pc.copy("www.gmail.com")

# Pasting the Gmail address and hitting ENTER
py.hotkey("ctrl", "v")
py.press("enter")

time.sleep(7)

# Clicking the Compose button
py.press("tab", presses=14)
py.press("enter")

time.sleep(2)

# Filling in the recipient
pc.copy(destinatario)
py.hotkey("ctrl", "v")
py.press("tab")

# Filling in the subject
pc.copy(assunto)
py.hotkey("ctrl", "v")
py.press("tab")

# Filling in the message
pc.copy(mensagem)
py.hotkey("ctrl", "v")

# Clicking the Send button
py.hotkey("ctrl","enter")

# Closing the Gmail tab
py.hotkey("ctrl", "f4")

# Printing the message of successful sending
print('E-mail enviado com sucesso!')

# Code to discover mouse coordinates
time.sleep(5)
py.position()
