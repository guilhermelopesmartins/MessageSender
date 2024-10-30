
import pywhatkit

def send_messages(content):
    try:
        message = 'Hello, I am sick today \nName: {0}\nRoom: {1} \nHouse: {2}\nAppointment: {3} \nHelp: {4}'.format(content['name'], content['room'], content['house'], content['appointment_situation'], content['help'])
        waiting_time_to_send = 15
        close_tab = True
        waiting_time_to_close = 3

        with open('contacts.txt', 'r') as arquivo:    
            contacts = [linha.strip() for linha in arquivo.readlines()]

        for contact in contacts:
            pywhatkit.sendwhatmsg_instantly(contact, message, waiting_time_to_send, close_tab, waiting_time_to_close)
        
        return 'Messages delivered succefully'
    except:
        return 'An error occured while sending messages.'        
    