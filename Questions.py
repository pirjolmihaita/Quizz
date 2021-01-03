import json
import random
class Questions():


    def details(self):
        j = 0  # una dintre posibilele barinate(A,B,C,D,F....)
        for i in range(3): # nr de intrebari pe care il vreau introdus
            self.text = input("Introduceti intrebarea: ")

            self.optiuni = [] # optiunile intrebarii

            self.nrVariante = int(input("Cate variante vrei sa aiba intrebarea ? "))

            for varianta in range(self.nrVariante):
                varianta = input()
                print("Varianta ", lista[j], ":", varianta)
                self.optiuni.append(varianta)
                j += 1
            j = 0


            self.varianta_corecta = input("Introduceti varianta corecte ") # introduc varianta corecta
            lista_intrebari.append(self.create_dictionary())

            print("\n")

            with open('istorie.json', mode='r', encoding='utf-8') as outfile: # instorie - numele domeniului unde introduc intrebarile
                intrebari = json.load(outfile)

            with open('istorie.json', 'w', encoding='utf-8') as outfile:
                intrebari.append(self.create_dictionary())
                json.dump(intrebari, outfile)





    def create_dictionary(self):
        dict ={
            "Intrebare: " : self.text,
            "Variante: "  : self.optiuni,
            "Varianta corecta: " : self.varianta_corecta,
        }
        return dict

lista = ["A","B","C","D","E"]
lista_intrebari = []
