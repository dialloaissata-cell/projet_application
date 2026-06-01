from fastapi import FastAPI
import json
from math import ceil

#autoriser le frontend à accéder au backend
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

#autoriser le frontend à accéder au backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
#on doit creer une fonction qui s'excecute quand on va sur cette route 
def load_data():
    with open ("etudiants.json","r") as file:
        data= json.load(file)
    return data

#on cree une route pour l'acceuil (non obligatoire)
#get c'est pour récupérer 
@app.get("/")
def acceuil ():
    return{"message": "API fonctionne"}

@app.get("/etudiants")
def get_etudiants():
    return load_data()

@app.get("/etudiants/page/{page}")
def get_etudiants_paginated(page: int = 1):
    data = load_data()
    limit = 5
    start = (page - 1) * limit
    end = start + limit
    total_pages = ceil(len(data) / limit)
    
    return {
        "etudiants": data[start:end],
        "page": page,
        "total_pages": total_pages,
        "total_etudiants": len(data)
    }

#pour acceder au swagger et acceuil on ecrit fastapi dev 

# psycopg2 envoie la requête à PostgreSQL récupère les résultats transforme les données pour Python.Il permet la communication entre python et postgresql
#pour l'installer on fait pip install psycopg2-binary car version prête à utiliser plus simple pour les projets étudiants et développement.