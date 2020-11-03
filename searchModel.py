import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize
import os,sys,re,copy,time
import operator
import pickle
from math import *
import numpy
import codecs


position = os.path.dirname(os.path.abspath(__file__))
baseFilePath="C:\\Users\\PC\\Desktop\\TPRI\\ProjetRI\\cacm\\"
tableFrequences = {}
tableFichierInverse = {}
tableFrequencesPondere={}
tableInversePondere = {}
maxFreqTable = {}
stopWordsIndex = {}
matriceAppariment=None
tempsDeConstruction={}
tempsExecution={}

def ExtraireInformations(NomF):
    TabContenuDocs = nltk.defaultdict(str)
    fichier = open(NomF, 'r')
    Lignes = fichier.readlines()
    i = 0
    NumDoc = 0

    while(i < len(Lignes)):
        Ligne = Lignes[i]
        if Ligne.startswith('.I'):
            NumDoc = int(Ligne.split()[1])

        if Ligne.startswith('.T'):
            i += 1
            contenuDoc = ""
            while(((nltk.re.findall('\.([TWBANX]\n|I [0-9]+\n)', Lignes[i]) == [])) and (i < len(Lignes))):
                mots = Lignes[i].split()  # word_tokenize(Lignes[i])
                for mot in mots:
                    if len(mot) > 1 and acess(mot) is None:
                        contenuDoc = contenuDoc+" "+mot.lower()

                i += 1
            #contenuDoc = contenuDoc[1:]
            TabContenuDocs[NumDoc] = contenuDoc
            i -= 1

        if Ligne.startswith('.W'):
            i += 1
            contenuDoc = ""
            while(((nltk.re.findall('\.([TWBANX]\n|I [0-9]+\n)', Lignes[i]) == [])) and (i < len(Lignes))):
                mots = Lignes[i].split()  # word_tokenize(Lignes[i])
                for mot in mots:
                    if len(mot) > 1 and acess(mot) == None:
                        contenuDoc = contenuDoc+" "+mot.lower()


                i += 1
            #contenuDoc = contenuDoc[1:]
            TabContenuDocs[NumDoc] = TabContenuDocs[NumDoc]+contenuDoc

            i -= 1

        i += 1
       
    return TabContenuDocs


def construireTableFreq(nomF):
    debut=time.time()
    tableContenu = ExtraireInformations(nomF)
    global tableFrequences
    global tempsDeConstruction
    for doc, listeMots in tableContenu.items():
        frequences = {}
        tab = nltk.tokenize.word_tokenize(listeMots)
        tab=[el for el in tab if el not in '[ ( ) ! \ ? . ; , - - : / \' \ * \ + \ - ]'.split(' ')  ]
        tab=[re.sub("[\"'\.,:\)\(\?!<>-]+$","",el) for el in tab]
        tab=[re.sub("^[\"'\.,:\)\(\?!<>-]+","",el) for el in tab]
        for mot in tab:
            if len(mot)>1 and not acess(mot):
                if not mot in frequences:
                    frequences[mot] = 0
                frequences[mot] += 1

        tableFrequences[int(doc)] = frequences
    fin=time.time()
    tempsDeConstruction["TableFreq"]=fin-debut
    sauvegarder_obj(tableFrequences,"tableFrequences")
    sauvegarder_json(tableFrequences,"tableFrequences")
    
    print("Temps de la constructionde l'index des fréquences : ",(fin-debut)," seconds.")

    return tableFrequences    


def construireFichierInverse():
    global tableFichierInverse
    global tableFrequences
    global baseFilePath
    global tempsDeConstruction
    debut=time.time()
    if not os.path.exists('objets\\tableFrequences.txt'):
        print("ConstruireFichierInverse : table fréquence non trouvée sur disque. Reconstruction . . .")
        tableFrequences=construireTableFreq(baseFilePath+"cacm.all")
        
    if not bool(tableFrequences):
        tableFrequences=charger_obj("tableFrequences")  
    
    for doc in tableFrequences:
        for mot, freq in tableFrequences[doc].items():
            if not mot.lower() in tableFichierInverse:
                tableFichierInverse[mot.lower()] = []
            tableFichierInverse[mot.lower()].append([doc, freq])
    fin=time.time()
    tempsDeConstruction["FichierInverse"]=fin-debut
    sauvegarder_obj(tableFichierInverse,"fichierInverse")
    sauvegarder_json(tableFichierInverse,"fichierInverse")
    print("Temps de la constructionde du Ficher inverse : ",(fin-debut)," seconds.")
    return tableFichierInverse        


def getFrequences(doc):
    global tableFrequences
    doc=str(doc)
    doc=doc.lower()
    if not os.path.exists('objets\\tableFrequences.txt'):
        print("GetFrequences : table fichier inversé non trouvée sur disque. Reconstruction . . .")
        tableFrequences=construireTableFreq()
    if not bool(tableFrequences):
        tableFrequences=charger_obj("tableFrequences")

    if type(next(iter(tableFrequences)))==type(2):
        doc=int(doc)
    if doc not in tableFrequences:
        print("None value")
        return None
        
    frequences = {}
   
    for term,freq in tableFrequences[doc].items():
            frequences[term] = freq

    return frequences


def getOccurences(term):

    if term not in tableFichierInverse:
        return None
    occurences = {}
    for occurence in tableFichierInverse[term]:
        occurences[occurence[0]] = occurence[1]

    return occurences


def getMaxFrequence(doc):
    global tableFrequences
    max = 0
    for term, freq in tableFrequences[doc].items():
        if freq > max:
            max = freq

    return max

def calculerTousMaxes(maxesDict):
    global tableFrequences
    
    for doc in tableFrequences.keys():
        maxesDict[int(doc)]=getMaxFrequence(doc)

    return maxesDict  


def calculerNi(term):
    global tableFichierInverse
    if not os.path.exists('objets\\fichierInverse.txt'):
        print("Calcul Ni : table fichier inversé non trouvée sur disque. Reconstruction . . .")
        tableFichierInverse=construireFichierInverse()
    if not bool(tableFichierInverse):
        tableFichierInverse=charger_obj("fichierInverse")
    ni = 0
    
    for liste in tableFichierInverse[term.lower()]:
        ni += liste[1]

    return ni


def construireTableFrequencesPondere():
    global tableFrequences
    global tableFrequencesPondere
    global tempsDeConstruction
    if not os.path.exists('objets\\tableFrequences.txt'):
        print("ConstruireTFreqPondéré : table fréquence non trouvée sur disque. Reconstruction . . .")
        tableFrequences=construireTableFreq(baseFilePath+"cacm.all")
        
    if not bool(tableFrequences):
        tableFrequences=charger_obj("tableFrequences")
        
    debut=time.time()
    tableFrequencesPondere = tableFrequences.copy()
    maxes = {}
    N=len(tableFrequencesPondere)
    for doc,frequences in tableFrequencesPondere.items():
        maxes[doc] = getMaxFrequence(doc)
        for term,freq in frequences.items():
                
            ni = calculerNi(term)
           

            tableFrequencesPondere[doc][term] = float(
                (freq/maxes[doc]) * numpy.log10((float(N)/ni)+1))
    fin=time.time()
    tempsDeConstruction["IndexPondere"]=fin-debut            
    sauvegarder_json(tableFrequencesPondere,"tableFrequencesPondere")
    sauvegarder_obj(tableFrequencesPondere,"tableFrequencesPondere")
    
    print("Temps de la constructionde de l'index pondéré : ",(fin-debut)," seconds.")
    return tableFrequencesPondere

def construireFichierInversePondere():
    global tableFichierInverse
    global tableFrequences
    global tableInversePondere
    global tempsDeConstruction
    debut=time.time()
    if not os.path.exists('objets\\fichierInverse.txt'):
        print("ConstruireFIPondéré : table fichier inversé non trouvée sur disque. Reconstruction . . .")
        tableFichierInverse=construireFichierInverse()

    if not bool(tableFichierInverse):
        tableFichierInverse=charger_obj("fichierInverse")

    if not bool(tableFrequences):
        tableFrequences=charger_obj("tableFrequences")  

    
    tableInversePondere = copy.deepcopy(tableFichierInverse)
    maxes = {}
    maxes=calculerTousMaxes(maxes)
    
    N=len(tableFrequences)
    for term, listeOccurences in tableFichierInverse.items():
        i=0
        listeNi={} # si un terme apparait K fois avec la même fréquence, pas la peinde de la recalculer
        for liste in listeOccurences:
           
            doc = liste[0]
            if not liste[1] in listeNi:
                ni = calculerNi(term)
                listeNi[liste[1]]=ni 
            else:
                ni=listeNi[liste[1]]

            tableInversePondere[term][i][1] = float(
                (liste[1]/maxes[doc]) * numpy.log10((float(N)/ni)+1))
            i+=1    
    fin=time.time()
    tempsDeConstruction["fichierInversePondere"]=fin-debut
    sauvegarder_json(tableInversePondere,"fichierInversePondere")
    sauvegarder_obj(tableInversePondere,"fichierInversePondere")
    print("Temps de la constructionde du Ficher inverse  pondéré: ",(fin-debut)," seconds.")
    return tableInversePondere


def construireIndexMotsVides():
    global stopWordsIndex
    global tempsDeConstruction
    debut=time.time()
    listMotsVides = stopwords.words('english')  # text.split('\n')
    for ligne in listMotsVides:
        if str(ligne.lower()[0]) not in stopWordsIndex:
            stopWordsIndex[str(ligne.lower()[0])] = []

        stopWordsIndex[str(ligne.lower()[0])].append(ligne)
    fin=time.time()
    tempsDeConstruction["indexStopWords"]=fin-debut
    # fichierMotsVides.close()

    return stopWordsIndex

def acess(motVide):
    global stopWordsIndex
    if not bool(stopWordsIndex):
        stopWordsIndex=construireIndexMotsVides()
    if not str(motVide.lower()[0]) in stopWordsIndex:
        return None
    for element in stopWordsIndex[str(motVide.lower()[0])]:
        if element.lower() == motVide.lower():
            return True
    return None

def sauvegarderTableFrequences():
    global tableFrequences
    # print(tableFrequences)
    buffer = ""
    for doc in tableFrequences.keys():
        ligne = ""+str(doc)+"--> {"
        for term, freq in tableFrequences[doc].items():
            ligne += "<"+term+", "+str(freq)+">,"

        ligne = ligne[:len(ligne)-1]
        ligne += "}"
        # print(ligne)
        buffer += ligne+"\n"

    f = open(os.path.join(position, "objets/tableFrequences.txt"), "w")
    f.write(buffer)
    f.close()




def sauvegarder_obj(obj, name):
    with open(os.path.join(position+"\\objets", name) + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def charger_obj(name):
    with open(os.path.join(position+"\\objets", name) + '.pkl', 'rb') as f:
        return pickle.load(f)


def sauvegarder_json(dictionary, name):
    import json
    with open(os.path.join(position+"\\objets", name) + '.txt', 'w') as f:
        f.write(json.dumps(dictionary))


def charger_json(name):
    import json
    return json.loads(open(os.path.join(position+"\\objets", name)+'.txt', 'r').read())


def Recherche_modelBooleen(Requete):
    global tableFrequences
    global tableFichierInverse
    if not bool(tableFrequences):
        tableFrequences = charger_obj("tableFrequences")
    if not bool(tableFichierInverse):
        tableFichierInverse = charger_obj("fichierInverse")

    docsPertinants = []
    ReqTokens = re.split(r'([ \(\)])', Requete.lower())
    ReqTokens = [el for el in ReqTokens if not re.match(
        r'\s+', el) and el != '']
    
    ReqTerms = []
    for token in ReqTokens:
        if token not in ['(', ')', 'not', 'or', 'and']:
            ReqTerms.append(token)

    matriceAppariment = numpy.empty(
        shape=(len(tableFrequences)+1, len(ReqTerms)), dtype=str)
    for key in tableFichierInverse.keys():
        if recherche(key, ReqTerms) >= 0:
            liste = tableFichierInverse[key]
            for el in liste:
                matriceAppariment[el[0]][recherche(key, ReqTerms)] = "1"

    for i in range(1, len(tableFrequences)):
        docEtTerm = ReqTokens.copy()
        for j in range(len(ReqTokens)):
            if ReqTokens[j] in ['(', ')', 'not', 'or', 'and']:
                docEtTerm[j] = ReqTokens[j]
            else:
                docEtTerm[j] = "1" if matriceAppariment[i,ReqTerms.index(ReqTokens[j])] == "1"else "0"        
        try:
            if(eval(' '.join(docEtTerm)) == 1):
                docsPertinants.append(i)

        except Exception:
            return -1


    return docsPertinants


def Recherche_ModelVectoriel(tableInversePoids, requete, methode,seuil):
    global tableFrequences
    global tableInversePondere
    global tableFrequencesPondere
    global matriceAppariment
    if os.path.exists('RSV_'+methode+'.txt'):
        resultat=charger_json("RSV_"+methode)
        if resultat["Requete"]==requete:
            return resultat["Resultat"]

    debut=time.time()
    if not os.path.exists('objets\\tableFrequences.txt'):
        tableFrequences=construireTableFreq(baseFilePath+"cacm.all")
    if not bool(tableFrequences):
        tableFrequences = charger_obj("tableFrequences")

    if not os.path.exists('objets\\fichierInversePondere.txt'):
        
        tableInversePondere=construireFichierInversePondere()

    if not bool(tableInversePondere):
        tableInversePondere = charger_obj("fichierInversePondere")

    if not os.path.exists('objets\\tableFrequencesPondere.txt'):
        tableFrequencesPondere=construireTableFrequencesPondere()

    if not bool(tableFrequencesPondere):
        tableFrequencesPondere = charger_obj("tableFrequencesPondere")    

    
    
    ensembleTermes = [term for term in list(tableInversePondere)]
    
    # if matriceAppariment is None:
    #     if not os.path.exists('objets\\matriceCollection.pkl'):
    #         matriceAppariment = numpy.empty(shape=(len(tableFrequences)+1, len(tableInversePondere)), dtype=int)

    #         for doc in tableFrequences.keys():
            
    #             for i in range(len(ensembleTermes)):
    #                 if(ensembleTermes[i] in tableFrequences[doc]):
    #                     matriceAppariment[int(doc),i] = tableFrequences[doc][ensembleTermes[i]]
    #                 else:
    #                     matriceAppariment[int(doc), i] = 0


    #         sauvegarder_obj(matriceAppariment,"matriceCollection")  

    #     else:
    #         matriceAppariment=charger_obj("matriceCollection")              
                 

    Requete = [term for term in nltk.tokenize.word_tokenize(requete) if not acess(term) and not term in '[ ( ) ! \ ? . ; , - - : / \' \ * \ + \ - ]'.split(' ') ]
    vecteurRequete = numpy.empty(len(tableInversePondere.keys()), dtype=int)
    
    for i in range(len(vecteurRequete)):
        vecteurRequete[i] = 1 if recherche(
            ensembleTermes[i], Requete) >= 0 else 0
    tableRSV={}
    for doc in range(1, len(tableFrequences)):
        sommex=0.0
        sommexy=0.0
        sommey=0.0
        # Effectuer les calculs
        if(methode.lower() == "Inner Product".lower()):
            for indice in range(len(Requete)):
                sommexy = sommexy+float((tableFrequencesPondere[doc][Requete[indice]] if Requete[indice] in tableFrequencesPondere[doc] else 0))
            if sommexy>seuil:
                tableRSV[doc]=sommexy

        if(methode.lower() == "Coef. de Dice".lower()):
            vecteurAppariement=[]
            
            for mot,poids in tableFrequencesPondere[doc].items():
                vecteurAppariement.append(mot)
                sommey+=pow(poids,2)
           
            
            for indice in range(len(Requete)):
                sommex +=1 #sommex+ pow( vecteurRequete[indice],2)
                
                if( recherche( Requete[indice] , vecteurAppariement)>=0):
                    y=tableFrequencesPondere[doc][Requete[indice].lower()]
                else :
                    y=0.0
                
                sommexy = sommexy+y
                sommey = sommey+pow(y,2)
            if(sommex+sommey) != 0:
                rsv = (2*sommexy)/(sommex+sommey)
            else :
                rsv=0    
            if rsv>seuil:
                tableRSV[doc]=rsv

        if(methode.lower() == "Mesure de Cosinus".lower()):
                # somme des x^2, y^2, x*y
            vecteurAppariement=[]
            
            for mot,poids in tableFrequencesPondere[doc].items():
                vecteurAppariement.append(mot)
                sommey+=pow(poids,2)
           
            
            for indice in range(len(Requete)):
                sommex +=1 #sommex+ pow( vecteurRequete[indice],2)
                
                if( recherche( Requete[indice] , vecteurAppariement)>=0):
                    y=tableFrequencesPondere[doc][Requete[indice].lower()]
                else :
                    y=0.0
                
                sommexy = sommexy+y
                sommey = sommey+pow(y,2)

            if(sqrt(sommex*sommey) != 0):
                rsv = sommexy/sqrt(sommex*sommey)
            else :
                rsv=0
            if rsv>seuil:
                tableRSV[doc]=rsv

        if(methode.lower() == "Mesure de Jacard".lower()):
            # somme des x^2; y^2 et x*y
            vecteurAppariement=[]
            
            for mot,poids in tableFrequencesPondere[doc].items():
                vecteurAppariement.append(mot)
                sommey+=pow(poids,2)
           
            
            for indice in range(len(Requete)):
                sommex +=1 #sommex+ pow( vecteurRequete[indice],2)
                
                if( recherche( Requete[indice] , vecteurAppariement)>=0):
                    y=tableFrequencesPondere[doc][Requete[indice].lower()]
                else :
                    y=0.0
                
                sommexy = sommexy+y
                sommey = sommey+pow(y,2)
            # mesure pour le doc i
            if((sommex+sommey-sommexy) != 0):
                rsv = sommexy/(sommex+sommey-sommexy)
            else :
                rsv=0    
            if rsv>seuil:
                tableRSV[doc]=rsv

    tableRSV=dict(sorted(tableRSV.items(),key=operator.itemgetter(1),reverse=True))
    fin=time.time()
    print("Temps d'execution :"+str(fin-debut)+" seconds.")
    tempsExecution["temps_modeleVectoriel"]=fin-debut
    result={}
    result["Requete"]=requete
    result['Resultat']=tableRSV
    sauvegarder_json(result,"RSV_"+methode)
    return tableRSV 

def chargerRequetes(nomF):
    global stopWordsIndex

    stopWordsIndex=construireIndexMotsVides()

    tabContenu=ExtraireInformations(nomF)

    dictionnaireRequetes=nltk.defaultdict(list)

    for doc,contenu in tabContenu.items():
        listeTokens = set()
        tab = nltk.tokenize.word_tokenize(contenu)
        for mot in tab:
            if not mot in '[ ( ) ! \ ? . ; , - - : / \' \ * \ + \ - ]'.split(' ') and not acess(mot):
                listeTokens.add(mot)

        dictionnaireRequetes[int(doc)] = list(listeTokens)

    return dictionnaireRequetes    


def chargerResultatsRequetes(nomF):
    f=open(nomF,'r')
    text=f.readlines()
    Resultat=nltk.defaultdict(list)
    for line in text:
        Tab=line.split()        
        Resultat[int(Tab[0])].append(int(Tab[1]))
    return Resultat


def evaluerModelVectoriel(resultats,numRequete,methode):
    
   
    resultatAttendus=chargerResultatsRequetes(baseFilePath+"qrels.text")[numRequete]
    #print("Expected : "+str(resultatAttendus))

    #print("returned : "+str(resultats))
    intersect=list(set(resultats) & set(resultatAttendus))
    rappel=len(intersect)/len(resultatAttendus) if len(resultatAttendus)!=0 else 0

    precision=len(intersect)/len(resultats) if len(resultats)!=0 else 0
    return [rappel,precision]


def recherche(term, liste):
    for i in range(len(liste)):
        if liste[i].lower() == term.lower():
            return i

    return -1

def getTableFrequences():
    global tableFrequences
    global baseFilePath
    if not os.path.exists('objets\\tableFrequences.txt'):
        tableFrequences=construireTableFreq(baseFilePath+"cacm.all")
        
    if not bool(tableFrequences):
        tableFrequences=charger_obj("tableFrequences")#charger_json("tableFrequences")

    return tableFrequences    

def getTableFichierInverse():
    global tableFichierInverse

    if not os.path.exists('objets\\fichierInverse.txt'):
        tableFichierInverse=construireFichierInverse()

    if not bool(tableFichierInverse):
        tableFichierInverse = charger_obj("fichierInverse")

    return tableFichierInverse    
        
         


# ***************************************************************************************************************



def evaluation(vectResult, docsUser):
    docsSys = []
    docsPerti = []
    for element in vectResult:
        if (element != 0.0):
            docsSys.append(element[0])
    for element in docsSys:
        if element in docsUser:
            docsPerti.append(element)
    # calcul du rappel et de la precision
    nbDocsSys = len(docsSys)
    nbDocsUser = len(docsUser)
    nbDocsPerti = len(docsPerti)
    print(nbDocsSys, nbDocsUser, nbDocsPerti)
    # nb docs pertinants de sys  / nb docs pertinants de user
    rappel = nbDocsPerti/nbDocsUser
    # nb docs pertinants de sys / nb total docs retournés par sys
    précision = nbDocsPerti/nbDocsSys

    result = []
    result.append(rappel)
    result.append(précision)

    return result


