import pywhatkit
from datetime import datetime, timedelta

def send_messages(content):
    # idea to send a message to the person who fill the form passing some instructions
    try:
        message = 'Hello, I am sick today \nName: {0}\nRoom: {1} \nHouse: {2}\nAppointment: {3}, Help: {4}'.format(content['name'], content['room'], content['house'], content['appointment_situation'], content['help'])
        waiting_time_to_send = 10
        close_tab = True
        waiting_time_to_close = 10

        with open('contacts.txt', 'r') as arquivo:    
            contacts = [linha.strip() for linha in arquivo.readlines()]

        for contact in contacts:
            current_time = datetime.now()
            new_time = current_time + timedelta(minutes=1)
            time_hour = new_time.hour
            time_minute = new_time.minute
            pywhatkit.sendwhatmsg(contact, message, time_hour, time_minute, waiting_time_to_send, close_tab, waiting_time_to_close)
        
        return 'Messages delivered succefully'
    except:
        return 'An error occured while sending messages.'        