from datetime import datetime
from tkinter import N

def sample_resp(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello","hi","sup","wagwan"):
        return "Wagwann my G! What's good yeah?"
    
    elif user_message in ("who are you","who are you?"):
        return "I am a Bot bruv!"
    
    elif user_message in ("time","time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)
    
    return "I don't understand bruh!!"