import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import pickle

startups = [['Prodsmart', 'James', 'Talkdesk', 'Codacy', 'Veniam',
              'Sensei', 'DefinedCrowd', 'Heptasense', 'Probe.ly',
              'Aptoide'], [1300000, 2500000, 13400000, 5900000,
                           24000000, 500000, 11800000, 5000000,
                           620000, 3700000],["www.prodsmart.com", "www.observador.pt", "www.observado .pt", "www.codacy.com","veniam.com","senseitech.com","definedcrowded.com","www.fido.com","aptoide.com","probely.com"]]

opc = 0

while opc != 7:
    print("_" * 80)
    print(""" \n    [1]MOSTRAR AS STARTUPS
    [2]ADICIONAR MAIS STARTUP
    [3]MOSTRAR O GRÁFICO CIRCULAR (PIE CHART)
    [4]MOSTRAR O GRÁFICO HORIZONTAL 
    [5]GRAVAR EM FICHEIRO TEXTO
    [6]GRAVAR EM FICHEIRO BINÁRIO 
    [7]SAIR DO PROGRAMA""")
    print("_" * 80)

    opc = int(input("\n >>>> QUAL É A SUA OPÇÃO? "))

    if opc == 1:
        print(startups)

    elif opc == 2:
        novastar = str(input("Nome da Startup: "))
        invest = int(input("Valor investido: "))
        sitee = str(input("Site da Startup: "))
        startups[0].append(novastar)
        startups[1].append(invest)
        startups[2].append(sitee)

    elif opc == 3:

        for linha in startups:
            for elemento in linha:
                print(elemento, end='|')

        labels = startups[0]
        sizes = startups[1]
        colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple',
                  'brown', 'grey', 'beige']
        explode = [0.9, 0.2, 0, 0, 0, 0.8, 0, 0, 0.8, 0]
        plt.pie(sizes, explode=None, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=220 ,labeldistance=1.1,
                pctdistance=0.8)
        plt.legend(loc='best')
        plt.axis('equal')
        plt.show()

    elif opc == 5:
        arquivo = open("arq01.txt", "w")
        arquivo.write("STARTUPs 2018 – 10 melhores em Lisboa e outras\n")
        arquivo.write("Abaixo podemos encontrar as 10 melhores Startups em Lisboa\n")
        arquivo.write("Prodsmart - 1300000\nJames - 2500000\nTalkdesk - 13400000\nCodacy - 5900000\nVeniam - 24000000\nSensei - 500000\nDefinedCrowd - 11800000\nHeptasense - 5000000\nProbe.ly - 620000\nAptoide - 3700000")
        arquivo.close()

        arquivo = open("arq01.txt", "r")
        for linha in arquivo:
            linha = linha.rstrip()
            print(linha)
        arquivo.close()

    elif opc == 4:

        for linha in startups:
            for elemento in linha:
                print(elemento, end='|')

        fig, ax = plt.subplots(figsize=(8, 4))
        ax.barh(startups[0], startups[1])
        labels = ax.get_xticklabels()
        print(plt.style.use('bmh'))
        plt.setp(labels, rotation=35)
        ax.set(xlim=[-1000000, 26000000], xlabel='Montante Investido',
               ylabel='Startups', title='STARTLIS-Startups-Lisboa')


        def currency(x, group_data):
            if x >= 1000000:
                s = '€{:1.1f}M'.format(x * 1e-6)
            else:
                s = '€{:1.0f}K'.format(x * 1e-3)
            return s


        formatter = FuncFormatter(currency)
        ax.xaxis.set_major_formatter(formatter)
        plt.show()

    elif opc == 6:
        with open('fichExt.pkl', 'wb') as f:
            pickle.dump(startups, f)

        with open('fichExt.pkl', 'rb') as f:
            startups = pickle.load(f)
            f.close()

    elif opc == 7:
        print("Finalizando....")

    else:
        print("Opção invalida, Tente novamente")
print("Fim do programa.")

