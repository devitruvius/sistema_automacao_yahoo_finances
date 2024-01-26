import yfinance
import pyautogui as py
import pyperclip as pc
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
py.PAUSE = .6

py.hotkey("alt","tab")

# abrir uma nova aba
py.hotkey("ctrl", "t")

# copiar o endereço do gmail para o clipboard
pc.copy("www.gmail.com")


# colar o endereço do gmail e dar um ENTER
py.hotkey("ctrl", "v")
py.press("enter")

time.sleep(7)
# clicando no botão Escrever
py.press("tab", presses=14)
py.press("enter")

time.sleep(2)

# Preenchendo o destinatário
pc.copy(destinatario)
py.hotkey("ctrl", "v")
py.press("tab")

# Preenchendo o assunto
pc.copy(assunto)
py.hotkey("ctrl", "v")
py.press("tab")

# Preenchendo a mensagem
pc.copy(mensagem)
py.hotkey("ctrl", "v")

# Clicar no botão Enviar
py.hotkey("ctrl","enter")

# fechar a aba do gmail
py.hotkey("ctrl", "f4")

# Imprimir mensagem de enviado com sucesso
print('E-mail enviado com sucesso!')

#Código para descobrir as coordenadas do mouse
time.sleep(5)
py.position()