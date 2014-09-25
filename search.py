import indexador

diccionario = []
archivos = []

diccionario,archivos = indexador.crear_indice('Noticias',diccionario,archivos)

indice = open('Indice','w')
for i in range(len(diccionario)):
    indice.write(diccionario[i]+' - '+','.join(archivos[i])+'\n')
    
while True:   
    semifinal = []        
    final = []
    resultado = []
    query= input('Query: ').split()
    if ('AND' in query)==1 and ('OR' in query)==1:
        print('Query no valida')
    elif ('AND' in query)==1:
        while ('AND' in query)==1:
            query.remove('AND')
        for palabra in query:
            n = indexador.normalizar([palabra])[0]
            if n:
                if (n[0] in diccionario)==1:
                    resultado.append(archivos[diccionario.index(n[0])])
        for parte in resultado:
            for archivo in parte:
                if (archivo in semifinal)==0:
                    semifinal.append(archivo)
        for archivo in semifinal:
            cont = 0
            for parte in resultado:
                if (archivo in parte)==0:
                    cont +=1
            if cont == 0:
                final.append(archivo)
                    
    elif ('OR' in query)==1:
        while ('OR' in query)==1:
            query.remove('OR')
        for palabra in query:
            n = indexador.normalizar([palabra])[0]
            if n:
                if (n[0] in diccionario)==1:
                    resultado.append(archivos[diccionario.index(n[0])])
        for parte in resultado:
            for archivo in parte:
                if (archivo in final)==0:
                    final.append(archivo)
    else:
        for palabra in query:
            n = indexador.normalizar([palabra])[0]
            if n:
                if (n[0] in diccionario)==1:
                    resultado.append(archivos[diccionario.index(n[0])])
        for parte in resultado:
            for archivo in parte:
                if (archivo in final)==0:
                    final.append(archivo)


    print('Archivos: '+', '.join(final))
    terminar = input('Desea hacer otro query? (Si/No): ')
    if terminar == 'No':
        break
