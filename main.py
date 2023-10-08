
import requests
from time import sleep


def retornar_historico():
    return [i['color'] for i in requests.get('https://blaze-1.com/api/roulette_games/recent').json()][::-1]


def enviar_mensagem(mensagem):
    bot_token = '6519773070:AAGxFFV-0bPDWUx6snXUUoPsc_ESHmo6Zgw' #6492851585:AAEPJdOlP07oreESve-gOeA6cDFkw9nwNVM
    chat_id = '-1001882309167' #-4097953113 grupo
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={mensagem}&parse_mode=Markdown'
    requests.get(url)

padrao = []
gale = 0
apostando = 0
corApostando = 0
acertos = 0
erros = 0
historico = []

cor = ['Branco','Preto','Vermelho']
simbolo = ['⬜','⬛','🟥']


print('Bot Grupo de sinais iniciado ...')
enviar_mensagem('Iniciando...\n\n⬛🟩⬛🟩⬛🟩⬛🟩')

while True:  
    try:

        sleep(2)
        novoHistorico = retornar_historico()
        if novoHistorico != historico:
            historico = retornar_historico()
            novoPadrao = historico[-3:]
            if apostando == 0:
                if novoPadrao == [1,1,1] or novoPadrao == [1,2,1]:
                    corApostando = 2
                    apostando = 1
                    enviar_mensagem('Aposta recomendada: ⬛\n\nSegurança no branco ⬜')
                elif novoPadrao == [2,2,2] or novoPadrao == [2,1,2]:
                    corApostando = 1
                    apostando = 1
                    enviar_mensagem('Aposta recomendada: 🟥\n\nSegurança no branco ⬜')
            else:
                ultimo = historico[-1:]
                if ultimo == [0]:
                    apostando = 0
                    acertos += 1
                    enviar_mensagem('Branco!!\n\n⬜⬜⬜⬜⬜')
                    sleep(3)
                    enviar_mensagem(f'Saldo:\n\nAcertos: {acertos}\nErros: {erros}')
                elif ultimo == [corApostando]:
                    apostando = 0
                    acertos += 1
                    if gale != 0:
                        gale = 0
                    enviar_mensagem('Acertamos!\n\n🟩🟩🟩🟩🟩')
                    sleep(3)
                    enviar_mensagem(f'Saldo:\n\nAcertos: {acertos}\nErros: {erros}')
                else:
                    if gale == 0:
                        gale = 1
                        if corApostando == 2:
                            enviar_mensagem('Gale 1!\nAposta recomendada: ⬛\n\nSegurança no branco ⬜')
                        if corApostando == 1:
                            enviar_mensagem('Gale 1!\nAposta recomendada: 🟥\n\nSegurança no branco ⬜')
                    elif gale == 1:
                        gale = 2
                        if corApostando == 2:
                            enviar_mensagem('Gale 2!\nAposta recomendada: ⬛\n\nSegurança no branco ⬜')
                        if corApostando == 1:
                            enviar_mensagem('Gale 2!\nAposta recomendada: 🟥\n\nSegurança no branco ⬜')
                    elif gale == 2:
                        apostando = 0
                        gale = 0
                        erros += 1
                        enviar_mensagem('Essa não deu...\n\n🟥🟥🟥🟥🟥')
                        sleep(3)
                        enviar_mensagem(f'Saldo:\n\nAcertos: {acertos}\nErros: {erros}')


            padrao = historico[-3:]

    except Exception as e:
        print(e)
        

        sleep(5)
        pass