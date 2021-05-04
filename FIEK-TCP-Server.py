import socket
import time
from datetime import datetime
import random
import math
import threading

zanore = ['a', 'e', 'o', 'u', 'y' 'i']

def numero(data):
    print(data[1])
    shuma_zanore = 0
    shuma_bashktng = 0
    for shkronja in data[1]:
        if shkronja not in zanore:
            shuma_bashktng += 1
        else:
            shuma_zanore += 1
    return "Teksti i pranuar permban " + str(shuma_zanore) + " zanore dhe " + str(shuma_bashktng) + " bashketingellore"


def anasjelltas(data):
    rev_text = ""
    text = data[1]
    data_len = len(text)
    for letter in range(data_len):
        rev_text += text[data_len - 1]
        data_len -= 1
    return rev_text.strip()


def palindrom(data):
    rev_text = ""
    text = data[1]
    data_len = len(text)
    for letter in range(data_len):
        rev_text += text[data_len - 1]
        data_len -= 1
    if text == rev_text:
        return "Teksti i dhene eshte palindrom"
    else:
        return "Teksti i dhene nuk eshte palindrom"


def koha(data):
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")


def loja(data):
    arr = []
    while len(arr) != 5:
        y = random.randint(1, 36)
        if y not in arr:
            arr.append(y)  
    arr.sort()
    arrToStr = ', '.join([str(elem) for elem in arr])
    return arrToStr


def gcf(data):
    return str(math.gcd(int(data[1]), int(data[2])))


def konverto(data):
    if data[1].lower() == "cmneinch":
        return str(round((float(data[2]) * 0.393701), 2)) + "in"
    elif data[1].lower() == "inchnecm":
        return str(round((float(data[2]) / 0.393701), 2)) + "cm"
    elif data[1].lower() == "kmnemiles":
        return str(round((float(data[2]) * 0.621371), 2)) + "miles"
    elif data[1].lower() == "milenekm":
        return str(round((float(data[2]) / 0.621371), 2)) + "km"
    else:
        return "Nuk mund te konvertohet"
    return True


def astro(data):
    day = int(data[1])
    month = int(data[2])

    if month == 12:
        if day < 22:
            return "Shigjetari"
        else:
            return "Bricjapi"
    elif month == 1:
        if day < 20:
            return "Bricjapi"
        else:
            return "Ujori"
    elif month == 2:
        if day < 19:
            return "Ujori"
        else:
            return "Peshqit"
    elif month == 3:
        if day < 21:
            return "Peshqit"
        else:
            return "Dashi"
    elif month == 4:
        if day < 20:
            return "Dashi"
        else:
            return "Demi"
    elif month == 5:
        if day < 21:
            return "Demi"
        else:
            return "Binjaket"
    elif month == 6:
        if day < 21:
            return "Binjaket"
        else:
            return "Gaforrja"
    elif month == 7:
        if day < 23:
            return "Gaforrja"
        else:
            return "Luani"
    elif month == 8:
        if day < 23:
            return "Luani"
        else:
            return "Virgjeresha"
    elif month == 9:
        if day < 23:
            return "Virgjeresha"
        else:
            return "Peshorja"
    elif month == 10:
        if day < 23:
            return "Peshorja"
        else:
            return "Akrepi"
    elif month == 11:
        if day < 22:
            return "Akrepi"
        else:
            return "Shigjetari"
    else:
        return "Nuk ka shenje"


def duplikat(data):
    chars = "abcdefghijklmnopqrstuvwxyz"
    string = data[1]

    for char in chars:
        count = string.count(char)
        if count > 1:
            return "Teksti ka duplikate"
        else:
            continue
    return "Teksti nuk ka duplikate"


def send(conn, data):
     conn.send(data.encode())


def server_threaded(conn, address):
    while True:

        data = conn.recv(128).decode()
        if not data:
            break

        data = data.split(' ')

        if data[0].upper() == 'IP':
            text = "IP address is: " + address[0]
            send(conn, str(text))
        elif data[0].upper() == 'NRPORTIT':
            text = "Port number is: " + str(address[1])
            send(conn, str(text))
        elif data[0].upper() == 'NUMERO':
            send(conn, numero(data))
        elif data[0].upper() == 'ANASJELLTAS':
            send(conn, anasjelltas(data))
        elif data[0].upper() == 'PALINDROM':
            send(conn, palindrom(data))
        elif data[0].upper() == 'KOHA':
            send(conn, str(koha(data)))
        elif data[0].upper() == 'LOJA':
            send(conn, loja(data))
        elif data[0].upper() == 'GCF':
            send(conn, gcf(data))
        elif data[0].upper() == 'KONVERTO':
            send(conn, konverto(data))
        elif data[0].upper() == 'ASTRO':
            send(conn, astro(data))
        elif data[0].upper() == 'DUPLIKAT':
            send(conn, duplikat(data))
        else:
            send(conn, "E dhena eshte gabim! ")
        print("Kerkesa nga klienti: " + str(data[0]))

def server_program():
    print("FIEK-TCP Protocol - Server \n")

    host = socket.gethostname()
    port = 14000

    print(
        "--------------------------------------------------------------\n")

    server_socket = socket.socket()
    server_socket.bind((host, port))

    print("Serveri eshte startuar me portin: " + str(port))
    
    server_socket.listen(2)

    while True:
        conn, address = server_socket.accept()
        print("Lidhja nga: " + str(address))
        thread = threading.Thread(target=server_threaded, args=(conn, address))
        thread.start()
        print("Lidhjet aktive: ",  threading.activeCount() - 1)
    conn.close()

if __name__ == '__main__':
    server_program()
