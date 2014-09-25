def normalizar(raw_docs):

    import nltk
    from nltk.tokenize import word_tokenize

    tokenized_docs = [nltk.tokenize.word_tokenize(doc) for doc in raw_docs]

    import re
    import string
    regex = re.compile('[%s]' % re.escape(string.punctuation))

    tokenized_docs_no_punctuation = []

    for review in tokenized_docs:
        
        new_review = []
        for token in review: 
            new_token = regex.sub(u'', token)
            if not new_token == u'':
                new_review.append(new_token)
        
        tokenized_docs_no_punctuation.append(new_review)
        
    from nltk.corpus import stopwords

    tokenized_docs_no_stopwords = []
    for doc in tokenized_docs_no_punctuation:
        new_term_vector = []
        for word in doc:
            if not word in stopwords.words('english'):
                new_term_vector.append(word)
        tokenized_docs_no_stopwords.append(new_term_vector)
                
    from nltk.stem.porter import PorterStemmer
    from nltk.stem.snowball import SnowballStemmer
    from nltk.stem.wordnet import WordNetLemmatizer

    porter = PorterStemmer()
    snowball = SnowballStemmer('english')
    wordnet = WordNetLemmatizer()

    preprocessed_docs = []

    for doc in tokenized_docs_no_stopwords:
        final_doc = []
        for word in doc:
            final_doc.append(porter.stem(word).lower())
        preprocessed_docs.append(final_doc)
    return preprocessed_docs

def indexar(diccionario,archivos,archivo,carpeta_archivos):
    news = open(carpeta_archivos+'/'+archivo,'r',encoding='UTF-8',errors='strict')
    raw_docs = news.readlines()
    for linea in normalizar(raw_docs):
        for palabra in linea:
            if (palabra in diccionario) == 0:
                diccionario.append(palabra)
                archivos.append([archivo])
            elif (archivo in archivos[diccionario.index(palabra)])==0:
                archivos[diccionario.index(palabra)].append(archivo)
    return diccionario,archivos

def crear_indice(carpeta_archivos,diccionario,archivos):
    import os
    textos = os.listdir(carpeta_archivos)
    for archivo in textos:
        if archivo != '.DS_Store':
            diccionario,archivos=indexar(diccionario,archivos,archivo,carpeta_archivos)
    return diccionario,archivos
