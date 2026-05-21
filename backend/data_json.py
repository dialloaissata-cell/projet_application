import pandas as pd 
data=pd.read_csv("donnees_propres.csv")
#pour passer du data frame (data) à json on fait:
data.to_json("etudiants.json",orient="records",force_ascii=False,indent=4)


#Avec FastAPI :Python devient un serveur web capable de :recevoir des requêtes (comme un site web) ,envoyer des données (JSON) ,communiquer avec un frontend
#Créer une API (le cœur du backend)Une API permet à une application de dire :“donne-moi les étudiants”“ajoute un étudiant”“filtre les données”FastAPI transforme tes fonctions Python en routes web :
#je dois cree Api car L’API est une porte d’entrée du backend.Elle sert à :recevoir les requêtes envoyer les réponses exposer les données.APi est dans le backend 
#pour installer fastAPI :pip install "fastapi[standard]"
#on va creer un API
