# reqres

import json
import requests

# ---------- d 1
test_url = "https://reqres.in/api/users/"
method = "GET"
# method = "POST"
# method = "PUT"
# method = "DELETE"
# 
def request(method, url, payload=""):
    payload = {}
    headers= {}
    response = requests.request(method, url, headers=headers, data = payload)
    results = response.text
    if method != "DELETE":
        results = json.loads(response.text) #si, no es gran cosa, cambia las comillas, import json decoder requiere de un valor     
    print("codigo de respuesta:",response)
#   print(results)
    print(type(results))
    return results

results = request(method, test_url)

# request(method,url,payload)

# ---------- d 2
def show_users(dictionary_users):
    for i in range(0,3):
        print(dictionary_users["data"][i]["id"], dictionary_users["data"][i]["first_name"], dictionary_users["data"][i]["last_name"])

show_users(results)

# ---------- d 3

def create_user():
    print("jajajaja, ya quisiera yo saber hacer eso")

create_user()
# ---------- d 4
# ---------- d 5


# API algo que se consulta, es una url a la que uno le pide cosas y te retorna una respuesta, es una forma de comunicarse con otro computador 