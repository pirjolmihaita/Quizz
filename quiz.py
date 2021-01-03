from Questions import Questions
import json

from datetime import date
import datetime
import random

today = date.today()

class Quiz():

    nr_puncte = 0 # nr de puncte care va fi obtinut per intrebare
    puntaj_maxim = 0 # punctajul amxim care poate fi obtinut

    def TakeQuizz(self):
        domeniu = input("Ce domeniu alegeti? ") # unul dintre domeniile unde vrem sa raspundem
        nrIntrebari = int(input("La cate intrebari vrei sa raspunzi: "))

        Quiz.puntaj_maxim = 2 * nrIntrebari
        print("Punctajul maxim care poate fi obtinut este: ", Quiz.puntaj_maxim)
        print("\n")

        with open(domeniu + '.json') as json_file:
            self.index  = 0
            data = json.load(json_file)
            contor  = 0
            i = 0
            j = 0
            while contor < nrIntrebari:
                        dictionar  = random.choice(data)
                        data.remove(dictionar)
                        i += 1
                        print("Intrebare: ",dictionar["Intrebare: "])
                        for varianta in dictionar["Variante: "]:
                            print("Varinata",lista[j],":",varianta)
                            j += 1
                        j  = 0

                        raspuns = input("Introduceti indexul raspunsul dvs ")
                        if raspuns == dictionar["Varianta corecta: "]:
                            Quiz.nr_puncte += 2
                            print("Raspuns corect ")
                            print("\n")
                        else:
                            Quiz.nr_puncte -= 1
                            print("Raspuns incorect")
                            print("\n")
                            self.index = 0

                        contor += 1 # nu depasesc nu depasesc nr de intrebari la care vreau sa raspund



        print("Punctajul obtinut de dvs este: ",Quiz.nr_puncte)
        input("Press enter to exit ;)")
        self.dateTime()

    def dateTime(self):
        dictionar = {
            "data " : today,
            "puncte" : Quiz.nr_puncte
        }

        def default(obj):
            if isinstance(obj, (datetime.date, datetime.datetime)):
                return obj.isoformat()


        with open('punctaj.json', mode='r', encoding='utf-8') as outfile:
            feeds = json.load(outfile)

        with open('punctaj.json', 'w', encoding='utf-8') as outfile:
            feeds.append(dictionar)
            json.dump(feeds, outfile,default=default)

        # input("Press enter to exit ;)")

lista = ["A","B","C","D","E"]

# q = Questions()
# q.details()
x  = Quiz()
x.TakeQuizz()

#q.update1()