# import
import array as ar


# Implementare l’algoritmo di Euclide (pag. 13)
def euclid(a, b):
    gcd = 0
    r = 0
    a = abs(a)
    b = abs(b)
    while b != 0:
        r = a % b
        a = b
        b = r
    gcd = a
    return gcd

# crea la classe di congruenza
class Congruence():
    def __init__(self, modulo):  # 84+19 = 62 = 19
        self.m = modulo

    # compie la riduzione di qualsiasi numero nella sua classe di numero inferiore al modulo m
    def redux(self, a):
        n = 0
        if a >= self.m:
            n = a % self.m  # riporta il resto in base al modulo

        return n

    # svolge l'operazione somma tra classi di congruenza e ne restituisce la congruenza appropriata
    def plusop(self, first, second):
        n = first + second
        return self.redux(n)

    # svolge l'operazione moltiplicazione tra classi di congruenza e ne restituisce la congruenza appropriata
    def moltop(self, first, second):
        n = first * second
        return self.redux(n)

    # trova il numero inverso rispetto alla somma
    def inverseopsum(self, a):
        inversesum = -1  # se non esiste l'inverso restituisce -1
        i = 0
        while i <= self.m:
            n = self.redux((a + i))
            if n == 0:  # se sommando l'insieme di numeri del modulo otteniamo zero abbiamo l'inverso
                inversesum = i
            i = i + 1
        return inversesum

    # trova il numero inverso rispetto alla moltiplicazione
    def inverseopmolt(self, a):
        inversemolt = -1  # se non esiste l'inverso restituisce -1
        i = 0
        while i < self.m:

            n = self.redux((a * i))

            if n == 1:  # se moltiplicando l'insieme di numeri del modulo otteniamo uno abbiamo l'inverso
                inversemolt = i

            i = i + 1

        return inversemolt

    # se abbiamo che il numero a ha un inverso restituisce true altrimenti false
    def existInverse(self, a):
        inversemolt = False
        i = 0
        while i <= self.m:

            n = self.redux((a * i))

            if n == 1:
                inversemolt = True

            i = i + 1

        return inversemolt

    def isgroup(self):

        flag = [None]
        n = flag

        i = 1
        while i < self.m:
            if self.existInverse(i):
                n.append(True)
            i = i + 1

        i = 1

        while i < len(n):

            if n[i] == False:
                return False
            i = i + 1
        return True

    def groupOrder(self):
        flag = [None]
        n = flag

        i = 1
        while i < self.m:
            if self.existInverse(i):
                n.append(True)
            i = i + 1

        j = 0
        i = 1
        while i < len(n):

            if n[i] == True:
                j = j + 1
            i = i + 1
        return j

    # Implementare l’algoritmo per calcolare la funzione di Eulero di un intero n, utilizzando il teorema 2.17.2. Questo programmino ci servira' per poter implementare i due programmi qui di seguito proposti.
    def fiEulero(self):
        count = 0
        i = 0
        while i < self.m:
            if euclid(i, self.m) == 1:
                count = count + 1
            i = i + 1
        return count

    # Implementare l’algoritmo per calcolare l’ordine di un elemento in un gruppo (teorema 2.14.1): il gruppo utilizzato sara’ il gruppo moltiplicativo degli interi modulo un primo p.
    def ordineElemG(self, elemento):
        i = 0
        while self.redux(elemento ** i) != 1:
            i = i + 1
        return i

congN = Congruence(13)
print("ordine 2 modulo 13 e':", congN.ordineElemG(4))

def binary_expansion(n, base):
    esponente_tra_n = 0  # trovo l'esponente che è minore del numero
    while base ** esponente_tra_n < n:  # finchè questa cosa vale, sostituisco e sommo di uno
        esponente_tra_n = esponente_tra_n + 1
    esponente_tra_n = esponente_tra_n - 1

    # print('base', base, 'esponente', esponente_tra_n)

    stringa_num_con_base = ""  # stringa di numeri
    i = esponente_tra_n  # partendo dalla fine
    # se il numero dispari prende uno, se pari prende zero.
    # divido per la base**esponente ed il risultato intero lo aggiungo alla stringa
    while i >= 0:
        aggiungo = int(n / base ** i)
        stringa_num_con_base = stringa_num_con_base + str(aggiungo)
        if base ** i <= n:
            n = n - base ** i
            # print('dentro', n, 'stringa', stringa_num_con_base, 'aggiungo', aggiungo, 'i', i)
        i = i - 1
        # print('numero fuori', n, 'stringa', stringa_num_con_base, 'aggiungo', aggiungo, 'i', i)

    return stringa_num_con_base

class Binar():

    def __init__(self, bs=2, lista=None):
        if lista is None:
            lista = []

        self.base = bs
        self.listaexp = lista

    def binary_expansion(self, n):
        esponente_tra_n = 0  # trovo l'esponente che è minore del numero
        while self.base ** esponente_tra_n < n:  # finchè questa cosa vale, sostituisco e sommo di uno
            esponente_tra_n = esponente_tra_n + 1
        esponente_tra_n = esponente_tra_n - 1

        # print('base', base, 'esponente', esponente_tra_n)

        stringa_num_con_base = ""  # stringa di numeri
        i = esponente_tra_n  # partendo dalla fine
        # se il numero dispari prende uno, se pari prende zero.
        # divido per la base**esponente ed il risultato intero lo aggiungo alla stringa
        while i >= 0:

            aggiungo = int(n / self.base ** i)

            stringa_num_con_base = stringa_num_con_base + str(aggiungo)
            if self.base ** i <= n:
                n = n - self.base ** i
                # print('dentro', n, 'stringa', stringa_num_con_base, 'aggiungo', aggiungo, 'i', i)
            i = i - 1
            # print('numero fuori', n, 'stringa', stringa_num_con_base, 'aggiungo', aggiungo, 'i', i)

        i = esponente_tra_n
        while i >= 0:
            if stringa_num_con_base == '1':
                self.listaexp.append(self.base ** i)
            i = i - 1

        return stringa_num_con_base

print(binary_expansion(105, 2))
print(len(binary_expansion(105, 2)))

def lista_valori_significativi(num):
    sa = binary_expansion(num, 2)
    i = len(sa) - 1
    lis = []

    # per ogni i trovo i sui valori e li inserisco in una lista.
    while i >= 0:
        if sa[i] == '1':
            print(2 ** i)
            lis.append((2 ** i))
            lis.sort()
        i = i - 1

    return lis

print(lista_valori_significativi(105))

def fermat_theorem(a, m):
    fer_val = 0
    if (euclid(a, m) == 1):
        congruenza = Congruence(m)
        fer_val = congruenza.redux(a ** (congruenza.fiEulero() - 1) * a)
    if (fer_val == 1):
        return 1
    else:
        return 0

nCong = Congruence(10) 
print("103, modulo 10:", nCong.redux(103))

# Implementare il Crivello di Eratostene (esercizio 1.12.24) per avere a disposizione la lista dei primi minori di un certo numero naturale n.
def completaArray(num):
    return list(range(0, num + 1))


def crivelloDiEratostene(n):
    array_n = completaArray(n)
    array_primi = []
    i = 2
    j = 2
    # aumento il valore del indice della moltiplicazione
    # devo mettere zero ai multipli del numero finoa nel arrnum
    while j <= len(array_n) - 1:
        if j <= (len(array_n) - 1):
            # array_primi.append(j)
            somma = j
            while i <= len(array_n) - 1:
                somma = i + somma

                if somma <= len(array_n) - 1:
                    if array_n[j] != -1:
                        array_n[j] = 0

                    array_n[somma] = -1
                if somma > len(array_n) - 1:
                    break
        j = j + 1
        i = j
    i = 2
    while i <= len(array_n) - 1:
        if array_n[i] == 0 or array_n[i] != -1:
            array_primi.append(i)

        i = i + 1
    return array_primi

#mostra 100000 numeri primi usando il crivello di eratostene
print(crivelloDiEratostene(100000))

import random

def cifrarioCesar(stringa):
    new_str = ''
    elem = range(1, len(stringa))
    salto = random.choice(elem)
    i = 0
    while i < len(stringa):
        n = ord(stringa[i])
        n = n + salto

        if n > 255:
            n = n % 256

        new_str = new_str + chr((n))

        i = i + 1
    return new_str


f = "teressi (per esempio, il contrasto tra Achille e Agamennone all inizio dell Iliade), oppure da una condizione di equilibrio, di tranquillit e di pace (per esempio la prima pagina de I Promessi Sposi).2. esordio ovvero lavvenimento che mette in moto l azione, modificando la situazione iniziale (l incontro di Don Abbondio con i Bravi per volere di Don Rodrigo).3. peripezie cio è l insieme degli avvenimenti che modificano di volta in volta la situazione in cui opera il protagonista. Nel corso delle peripezie entrano in azione altri personaggi che svolgono il ruolo di aiutanti o di oppositori, secondo che aiutino od ostacolino il protagonista nel conseguimento del suo obiettivo. L evoluzione della vicenda prosegue con un progressivo aumento di tensione (spannung) che raggiunge il culmine in prossimità dello scioglimento finale.4. scioglimento  è il momento conclusivo che determina il ritorno all equilibrio in positivo (lieto fine) o in negativo (morte dei personaggi principali).IL PUNTO DI VISTA O FOCALIZZAZIONE: Quando si analizza un testo narrativo  è molto importante stabilire da quale punto di vista sono presentati i fatti. Gli studiosi sono concordi nel distinguere tre tipi di focalizzazione:Focalizzazione zero: si verifica quando i fatti sono raccontati da un narratore onnisciente che  è a conoscenza di tutta la vicenda, legge nel pensiero e nell animo dei personaggi e sembra osservare dall alto lo svolgersi degli eventi (ad esempio àI Promessi Sposià).Focalizzazione interna: si verifica quando il narratore assume il punto di vista di un personaggio, sicchàE9 i fatti vengono giudicati e osservati dall interno dell ambiente rappresentato. La focalizzazione interna puàF2 essere fissa (un solo personaggio) o multipla (diversi punti di vista) (ad esempio i romanzi di Svevo).Focalizzazione esterna:  è il racconto assolutamente oggettivo. Il narratore, che osserva i fatti dall esterno,  è solo un testimone che ne sa meno di quanto sappia qualunque personaggio (ad esempio: il verismo, i romanzi gialli o d avventura).REGOLE GENERALI PER UNA CORRETTA ANALISI DI UN TESTO:Autore: specificare l autore dell opera.Opera: romanzo, racconto, novella, fiaba, mito, (racconto tratto dall operaà26).Spazio: luogo in cui si svolgono i fatti.Tempo: periodo in cui avvengono i fatti.Personaggi principali e secondariFabula o intreccio: specificare.Narratore: specificare se interno/esterno.Focalizzazione: specificare se zero/interna/esterna.TENERE PRESENTE LA STRUTTURA NARRATOLOGICA: 1. esposizione;2. esordio;3. Peripezie;4. Spannung;5. Scioglimento.Livelli del testo narrativo - versione di DavideàskriccoloTutti i testi narrativi presentano una struttura ricorrente, chiamata schema narrativo che si articola in 4 momenti fondamentali:>ESposizione:(o situazione iniziale): in questa fase viene descritta la situazione di partenza del racconto che  è di generale"
''' per visualizzare il cifrario di cesare rimuovi questo commento

visualizza = input("per visualizzare il cifrario di Cesare digita:\ns per visualizzarlo\nn per non visualizzarlo\n\n")

if visualizza == "s" :
    print(cifrarioCesar(f))
'''
#dico se 89 è un numero primo
n = 89
nroot = n ** (1 / 2)
nprime = crivelloDiEratostene(int(n ** (1 / 2)))
i = 0
flag = True
while flag and i < len(nprime):
    if n % nprime[i] == 0:
        flag = False
        print(n, 'is not prime')
    i = i + 1
if flag:
    print(n, 'is prime')

print(crivelloDiEratostene(100))
