import random as rd
import time as tm

print('Jogo da advinhação')

tm.sleep(2)

print('Advinhe o número')
# valor = rd.randint(1,)
# resposta = int(input('Qual a sua resposta?'))
while resposta != valor:
    valor = rd.randint(1,10)
    resposta = int(input('Qual a sua resposta?'))
    if resposta == valor: 
        tm.sleep(1) 
        print('Parabéns! Você acertou')
    if resposta < valor:
            tm.sleep(1)
            print('O valor é mais alto')
    if resposta > valor:
            tm.sleep(1)
            print('O valor é menor')