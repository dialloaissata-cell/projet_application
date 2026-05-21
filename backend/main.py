from fastapi import FastAPI
import json
app=FastAPI()
#on doit creer une fonction qui s'excecute quand on va sur cette route 
def load_data():
    with open ("etudiants.json","r") as file:
        return json.load(file)

#on cree une route pour l'acceuil (non obligatoire)
#get c'est pour récupérer 
@app.get("/")
def acceuil ():
    return{"message": "API fonctionne"}

@app.get("/etudiants")
def get_etudiants():
    return load_data()

#pour acceder au swagger et acceuil on ecrit fastapi dev 