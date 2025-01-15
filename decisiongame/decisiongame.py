from colorama import Fore, init, Style

init()

def jogo_decisoes():
    init()
    print(Fore.BLUE + '--------- A JORNADA DO AVENTUREIRO --------- \n' + Style.RESET_ALL )

    print(Fore.BLUE + 'Seja Bem-Vindo a terra de Eldoria \n' + Style.RESET_ALL)

    print(Fore.BLUE + 'Você é um aventureiro chamado Ludof e está em busca do lendário tesouro de Eldoria, escondido em uma floresta mágica cheia de desafios e perigos. Ao longo da jornada, suas decisões determinarão seu destino. \n -------------------------------------------' + Style.RESET_ALL)
    
    print('Ludof está no meio da floresta com dois caminhos diferentes. Um sombrio e misterioso à esquerda e outro iluminado e tranquilo à direita. \n')

    caminho = str (input(Fore.YELLOW + 'Ludof deve seguir qual caminho? Esquerda ou Direita? \n' + Style.RESET_ALL)).lower()
    
    if caminho == 'esquerda':
        print(Fore.RED + '\nOh, não! Ludof entrou em uma trilha escura e começou a ouvir rugidos assustadores. \n' + Style.RESET_ALL)
        decisao = str (input(Fore.YELLOW + 'UM MONSTRO APARECEU NO MEIO DO CAMINHO! E agora o que Ludof deve fazer? Lutar ou Fugir? \n' + Style.RESET_ALL)).lower()
        if decisao == 'lutar':
            print(Fore.GREEN + 'Ludof derrotou o monstro! O monstro protegia um BAÚ DO TESOURO! O tesouro agora é de Ludof!' + Style.RESET_ALL)
        elif decisao == 'fugir':
            print(Fore.RED + 'Ludof escapa correndo e se perde na floresta e nunca encontrou o tesouro perdido.' + Style.RESET_ALL)

    
    elif caminho == 'direita':
        print(Fore.GREEN + 'Uau! Ludof seguiu por um caminho tranquilo que o levou para um lindo lago. \n' + Style.RESET_ALL)

        print(Fore.YELLOW + 'Ludof encontrou um lago mágico lindo e ao longe avista uma linda ilha brilhando.\n')

        decisao_direita = str (input('O que Ludof deve fazer? Atravessar o Lago ou Seguir pela Margem? ' + Style.RESET_ALL)).lower()
        if decisao_direita == 'atravessar o lago':
            print(Fore.GREEN + 'Ludof encontrou o tesouro escondido na ilha!')
        elif decisao_direita == 'seguir pela margem':
            print('Ludof encontrou uma vila pacífica e decide abandonar a aventura e viver entre os moradores.')


        
    

jogo_decisoes()
