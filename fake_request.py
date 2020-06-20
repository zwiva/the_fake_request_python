# reqres

import json
import requests

test_url = "https://reqres.in/api/users/"

opcion = int(input("""Bienvenido. Escoja una opción: 
1 para mostrar el tiṕo de respuesta por defecto del programa,
2 para ver 3 usuarios,
3 para crear un usuario, 
4 para actualizar un usuario, 
5 para eliminar un usuario,
6 para salir \n"""))

def request(method, url, payload=""):
    payload = {}
    headers = {}
    response = requests.request(method, url, headers=headers, data = payload)
    results = response.text
    if method != "DELETE":
        results = json.loads(response.text) #si, no es gran cosa, cambia las comillas, import json decoder requiere de un valor     
    print(response)
#   print(results)
    # print(type(results))
    return results

while opcion != 6:
    if opcion == 1: # mostrar tipo de respuesta
        print("Por defecto el programa usa GET")
        method = "GET"
        results = request(method, test_url)
        opcion = int(input("Escoge otra opcion o 6 para salir\n"))
    
    elif opcion == 2:
        method = "GET"
        results = request(method, test_url)
        def show_users(dictionary_users):
            for i in range(0,3):
                print(dictionary_users["data"][i]["id"], dictionary_users["data"][i]["first_name"], dictionary_users["data"][i]["last_name"])
        show_users(results)
        opcion = int(input("Escoge otra opcion o 6 para salir\n"))

    elif opcion == 3:
        print("Escogiste crear un usuario")
        method = "POST"
        payload = "{\r\n    \"id\":483,\r\n    \"createdAt\": \"2020-06-19T23:08:50.551Z\"\r\n}"
        results = request(method, test_url, payload)
        def create_user():
            print(payload)
        create_user()    
        opcion = int(input("Escoge otra opcion o 6 para salir\n"))        
    
    elif opcion == 4:
        print("Escogiste actualizar un usuario")
        method = "PUT"
        payload = "{\r\n    \"id\":483,\r\n    \"createdAt\": \"2020-07-19T23:08:50.551Z\"\r\n}"
        test_url = "https://reqres.in/api/users/483"
        results = request(method, test_url, payload)
        def update_user():
            print("Modifica mes a 2020-07-19")
            print(payload)
            print(test_url)
        update_user()    
        opcion = int(input("Escoge otra opcion o 6 para salir"))
    
    elif opcion == 5:
        print("Escogiste eliminar un usuario:")

        def delete_user():
            print("...")

        method = "DELETE"
        print("")

    
    
    
    
    
    
    
    
    
    
        opcion = int(input("Escoge otra opcion o 6 para salir"))    
    elif opcion == 6: 
        print("Salir") 
    else:
        print("Opción inválida, adiós!")
        opcion = 6


# API algo que se consulta, es una url a la que uno le pide cosas y te retorna una respuesta, es una forma de comunicarse con otro computador 