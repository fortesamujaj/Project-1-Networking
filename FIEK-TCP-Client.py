import socket

commands = ['ASTRO', 'DUPLIKAT','IP', 'NRPORTIT', 'NUMERO', 'ANASJELLTAS', 'PALINDROM', 'KOHA', 'LOJA', 'GCF', 'KONVERTO']
convertions = ['cmneinch', 'inchnecm', 'kmnemiles', 'milenekm']

def isValid(message):
    if message.split(' ')[0] not in commands:
        return False
    else:
        return True

def concat(text, message):
    if len(text) <= 0:
        return 'Provo Prape!'
    else:
        message = message + ' ' + text
        return message

def operation(message):
    cmd_message = message.split(' ')[0].lower().strip()

    if cmd_message == 'ip':
        return message

    elif cmd_message == 'nrportit':
        return message

    elif cmd_message == 'numero':
        if len(message.split(' ')) == 1:
            text = input("Teksti? ")
            text = concat(text, cmd_message)
        else:
            text = 'Provo Prape!'
        return text

    elif cmd_message == 'anasjelltas' and  len(message.split(' ')) == 1:
        text = input("Teksti? ")
        return concat(text, cmd_message)

    elif cmd_message == 'palindrom' and  len(message.split(' ')) == 1:
        text = input("Teksti? ")
        return concat(text, cmd_message)

    elif cmd_message == 'koha':
        return message

    elif cmd_message == 'loja':
        return message

    elif cmd_message == 'konverto':
        message_arr = message.split(' ')
        if not len(message_arr) == 3:
            return 'Provo Prape!'
        else:
            if message_arr[1] not in convertions:
                return 'Provo Prape!'
            elif not message_arr[2].isnumeric():
                return 'Provo Prape!'
            else:
                return message

    elif cmd_message == 'gcf':
        message_arr = message.split(' ')
        if not len(message_arr) == 3:
            return 'Provo Prape!'
        elif message_arr[1].isnumeric() and message_arr[2].isnumeric():
            return message
        else:
            return 'Provo Prape!'

    elif cmd_message == 'astro':
        if len(message.split(' ')) == 1:
            text = int(input(" Dita e lindjes? "))
            if text < 1 or text > 32:
                print("Dita duhet te shkruhet si numer ndermjet vlerave 1 dhe 32")
                return 'Provo Prape!'
            else:
                text_concat = concat(str(text), cmd_message)
            text = int(input("Muaji i lindjes? "))
            if text < 1 or text > 12:
                print("Muaji duhet te shkruhet si numer ndermjet vlerave 1 dhe 12")
                return 'Provo Prape!'
            else:
                text_concat =  concat(str(text), text_concat)    
            return text_concat
        else:
            return 'Provo Prape!'

    elif cmd_message == 'duplikat':
        if len(message.split(' ')) == 1:
            text = input("Teksti? ")
            return concat(text, cmd_message)
        else:
            return 'Provo Prape!'
    else:
        return 'Provo Prape!'
     

def client_program():
    print("FIEK-TCP Protocol - Client \n")
    print(
      "--------------------------------------------------------------\n"
      "1. IP\n"
      "2. NRPORTIT\n"
      "3. NUMERO\n"
      "4. ANASJELLTAS\n"
      "5. PALINDROM\n"
      "6. KOHA\n"
      "7. LOJA\n"
      "8. GCF numri1 numri2\n"
      "9. KONVERTO cmneinch/inchnecm/kmnemiles/milenekm numri\n"
      "10. ASTRO\n"
      "11. DUPLIKAT\n")
    
    host = socket.gethostname()
    port = 14000
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    ndrr = int(input("Shtypni 1 nese deshironi te nderroni adresen dhe portin: ").strip())

    while ndrr == 1:
        host_changed = input("IP adresa: ")
        port_changed = int(input("Porti: "))
        while port > 14000:
            port = int(input("Shkruaj nje numrer porti tjeter:"))
        try:
            client_socket.connect((host_changed, port_changed))
            break
        except (socket.error, OverflowError, ValueError) as error:
            print("Gabime gjate krijimit te socket-it: " + str(error))
            ndrr = int(input("Shtypni 1 nese deshironi te nderroni adresen dhe portin: ").strip())

    message = input("Operacioni: ")

    while message.lower().strip() != 'exit':
        if not isValid(message.upper()):
            message = input(" Komanda nuk eshte valide. Provoni operacionin perseri: ")
            continue
        else:
            op = operation(message.lower())
            if op == 'Provo Prape!':
                message = input(" Komanda nuk eshte shkruar si duhet! Provoni operacionin perseri: ")
                continue
            client_socket.send(op.encode())
            data = client_socket.recv(128).decode()
            print('Pergjigja nga serveri: ' + data + "\n\n")
        message = input("Operacioni: ")
          
    client_socket.close()


if __name__ == '__main__':
    client_program()
