import yfinance
import pyautogui
import pyperclip
import time

#Buscando as cotações de uma Ação (ex: PETR4.SA)
ticker = input('Digite o código da ação: ')
dados = yfinance.Ticker(ticker)

dados.history()

#Configurando o período histórico
tabela = dados.history("6mo")

#Selecionando apenas a coluna de Fechamento (Close)
fechamento = tabela.Close

#Gerando um gráfico de linha
fechamento.plot()

#Gerando as estatísticas
maxima = fechamento.max()
minima = fechamento.min()
atual = fechamento[-1]

#Criando o e-mail que será enviado
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

#Automatizando o envio
# configurar uma pausa entre as ações do pyautogui
pyautogui.PAUSE = 3

# abrir uma nova aba
pyautogui.hotkey("ctrl", "t")

# copiar o endereço do gmail para o clipboard
pyperclip.copy("www.gmail.com")

# colar o endereço do gmail e dar um ENTER
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

# clicando no botão Escrever
pyautogui.click(x=2034, y=210)

# Preenchendo o destinatário
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")

# Preenchendo o assunto
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")

# Preenchendo a mensagem
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")

# Clicar no botão Enviar
pyautogui.click(x=3107, y=975)

# fechar a aba do gmail
pyautogui.hotkey("ctrl", "f4")

# Imprimir mensagem de enviado com sucesso
print('E-mail enviado com sucesso!')

#Código para descobrir as coordenadas do mouse
time.sleep(5)
pyautogui.position()