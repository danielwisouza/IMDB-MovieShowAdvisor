#37.593 total 75.186
# Criar duas pastas de XMLConsumidos e XMLNovos e fazer o programa
# Verificar se a pasta XMLNovos contem novos arquivos
# Caso tenha, ira pegar o XML, abrir e inserir os novos dados no banco de dados
# finalizando o processo, enviara ou deletara o XML para a pasta XMLConsumidos
# deixando pronto para o programa pesquisar os dados necessarios
def listarAnosXML():
    ##VERIFICAR ARMAZENAR TODOS OS DADOS NO BANCO DE DADOS!!!!!
    #POIS E MUITA INFORMACAO PARA ABRIR ARQUIVO POR ARQUIVO
    from xml.dom import minidom
    #   ABRINDO ARQUIVO XML UNICO
    xmldoc = minidom.parse('0000301510136952_2016_estendido.xml')
    print (xmldoc)
    #itemlist = xmldoc.getElementsByTagName('PESQUISADORES')

    #LOCALIZANDO CAMPO COM AS INFORMACOES NO XML
    itemList = xmldoc.getElementsByTagName('TOTAL-PRODUCAO')
    print (itemList)
    #Faz verificacao interna para percorrer os anos sem repeticao
    anoVer=[]
    anoVer.append(int(itemList[0].attributes['ANO-PRODUCAO'].value))
    
    #Faz a conta de quantidade de anos
    qtdAno = 0
    for s in itemList:
        #print("Ano percorrendo XML: ",int(s.attributes['ANO-PRODUCAO'].value))
        i = 0
        while i != len(anoVer):
            #print("Ano comparando com o XML do Array: ",anoVer[i])
            #print("Listando anos inseridos: ",anoVer)
            if (int(s.attributes['ANO-PRODUCAO'].value)) not in anoVer:
                anoVer.append(int(s.attributes['ANO-PRODUCAO'].value))
                #print("ADICIONOU!! ",int(s.attributes['ANO-PRODUCAO'].value))
            i += 1
        qtdAno += 1

    print("Quantidade projetos: ", qtdAno)
    print ("Anos disponiveis: ", anoVer)

def capturaValoresAno(dataAno):
    from xml.dom import minidom
    #   ABRINDO ARQUIVO XML UNICO
    xmldoc = minidom.parse('0000301510136952_2016_estendido.xml')
    #itemlist = xmldoc.getElementsByTagName('PESQUISADORES')

    #LOCALIZANDO CAMPO COM AS INFORMACOES NO XML
    itemList = xmldoc.getElementsByTagName('TOTAL-PRODUCAO')

    #INICIANDO LISTA E VARIAVEIS
    arrValores = []
    totalValores = 0
    qtdAnoPesquisa = 0

    print ("Ano a ser processado: ", dataAno)
    for s in itemList:
        if int(s.attributes['ANO-PRODUCAO'].value) == dataAno:
            #print ("Deu serto")
            arrValores.append(int(s.attributes['TOT-BIBL'].value))

            #Faz a soma de todos os valores encontrados do campo atraves do cast
            totalValores += (int(s.attributes['TOT-BIBL'].value))
            qtdAnoPesquisa += 1
    print ("Quantidade de pesquisa deste ano: ",qtdAnoPesquisa)
    print("Total :", totalValores)
    print("Valores da Lista: ",arrValores)

def capturaValoresGeral():
    from xml.dom import minidom
    #   ABRINDO ARQUIVO XML UNICO
    xmldoc = minidom.parse('0000301510136952_2016_estendido.xml')
    #itemlist = xmldoc.getElementsByTagName('PESQUISADORES')

    #LOCALIZANDO CAMPO COM AS INFORMACOES NO XML
    itemList = xmldoc.getElementsByTagName('TOTAL-PRODUCAO')

    #INICIANDO LISTA E VARIAVEIS
    arrValores = []
    totalValores = 0
    #anoPesquisa = 2014
    qtdAnoPesquisa = 0
    print("Total de itens encontrados no unico XML: ",len(itemList))
    #print(itemlist[0].attributes['TOT-BIBL'].value)

    for s in itemList:
        #Printa valores separados de cada TOTAL-PRODUCAO
        #print(s.attributes['TOT-BIBL'].value)

        #Adiciona do array os valores sem usar o cast para INT
        #arrValores.append(s.attributes['TOT-BIBL'].value)

        #Armazena os valores formatados para INT
        arrValores.append(int(s.attributes['TOT-BIBL'].value))

        #Faz a soma de todos os valores encontrados do campo atraves do cast
        totalValores += (int(s.attributes['TOT-BIBL'].value))

    print("Total :", totalValores)
    print("Valores da Lista: ",arrValores)

