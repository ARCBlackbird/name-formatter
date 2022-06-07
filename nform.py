def ftingName (a, itsAname=True, noNumbers=False, parmin=0, parmax=0):
    try:
        from time import sleep

        # Init Bloco de Range (BR)
        if parmin == 0:
            parmin = 3
        if parmax == 0:
            parmax = 12
        # Fim BR

        while True:
            keyrepeatnonumber = False
            primput = input (a).strip()

            # Correções ortográficas
            namemin = parmin - len(primput)
            namemax = len(primput) - parmax

            if namemin > 1 or namemax > 1:
                charn = 'caracteres'
            else:
                charn = 'caracter'

            # Fim das correções ortográficas

            # Init Bloco do Vazio (BV)
            if primput == '':
                print ('\033[3;2;6m Insira um nome...\033[m')
                continue
            # FimBV

            # Init Bloco de Verificação de Capitalização (BVC)
            if itsAname:
                primput = primput.capitalize()
            # Fim BVC

            # Init Bloco de Verificação de Números (BVM)
            if noNumbers == True:
                for l in primput:
                    if l.isnumeric():
                        keyrepeatnonumber = True
                if keyrepeatnonumber:
                    print ("\033[3;2;6m O nome inserido não pode conter números, tente novamente...\033[m")
                    continue
            # Fim BVM

            # Init Bloco de Verificação de Tamanho (BVT)
            if len(primput) < parmin:
                print (f'\033[3;2;6m O nome inserido é muito curto, tente novamente... (+{namemin} {charn})\033[m')
                continue
            if len(primput) > parmax:
                print (f'\033[3;2;6m O nome inserido é muito longo, tente novamente... (-{namemax} {charn})\033[m')
                continue
            
            return primput
    except KeyboardInterrupt:
        print ('\n\033[3;1;2;31m O programa foi interrompido pelo usuário, encerrando...\033[m')
        exit
