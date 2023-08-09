import tkinter
import customtkinter
import pywhatkit
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pyjokes
import yagmail
import mediapipe as mp
import cv2
import numpy as np
import time
from langdetect import detect
import webbrowser
from googletrans import Translator
from gtts import gTTS
import playsound
import os
import pyautogui

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("700x780")
app.title("Eduza")



frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

# Create a scrollbar widget and pack it on the right side of the root window
scrollbar = tkinter.Scrollbar(app)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)



text_frame = customtkinter.CTkFrame(app,corner_radius=10)
text_frame.pack(pady=20, padx=60, fill="both", expand=True)

my_text = tkinter.Text(text_frame, height=20, width=70, wrap=tkinter.WORD, bd=0, bg="#292929", fg="silver",yscrollcommand=scrollbar.set)
my_text.pack(pady=20, padx=60, fill="both", expand=True,side=tkinter.LEFT)

def update_textbox(text):
    my_text.insert(tkinter.END, text + '\n')
    app.update() 


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

email_list = {
    'rishika': 'ucs19324@rmd.ac.in',
    'dad': 'jkenterprises@gmail.com',
    'nisha': 'nishakollacheri@gmail.com',
    'achu': 'rdrkailash@gmail.com',
    'richu': 'rishikarishi1001@gmail.com',
    'poonkuzhali':'ucs19311@rmd.ac.in',
    'reshma':'ucs19323@rmd.ac.in'
} 


#To get input in voice
def get_info():
    try:
        with sr.Microphone() as source:
            update_textbox('Listening...')
            print('Listening...') 
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            update_textbox(info)
            return info.lower()
    except:
        pass


def talk(text):
    engine.say(text)
    engine.runAndWait()

def greet_alexa():
    print('Hi, I am your Personal Assistant')
    talk('Hi, I am your Personal Assistant')
    update_textbox('Hi, I am your Personal Assistant')
    # my_text.insert(tkinter.END, "Hi, I am your Personal Assistant\n")

def button_callback():
    print("Button click")

def whatsapp_msg():
    individual_contact = {
    'rishika':'+919940215836',
    'dad':'+919176342800',
    'mom':'+919940215846',
        }


    print("Hello this is a Whatsapp Automation tool!") 
    update_textbox('Hello this is a Whatsapp Automation tool!')
    # my_text.insert(tkinter.END, 'Hello this is a Whatsapp Automation tool!\n')
    talk("Hello this is a Whatsapp Automation tool!")
    print("Do you like to send message?")
    update_textbox('Do you like to send message?')
    # my_text.insert(tkinter.END, 'Do you like to send message?\n')
    talk("Do you like to send message?")
    reply = get_info()
    if 'yes' in reply:
        print('Is it an individual message or group message?')
        update_textbox('Is it an individual message or group message?')
        # my_text.insert(tkinter.END, 'Is it an individual message or group message?\n')
        talk('Is it an individual message or group message?')
        reply2 = get_info()
        if 'individual' in reply2:
            print('Whom do you like to send message?')
            update_textbox('Whom do you like to send message?')
            talk('Whom do you like to send message?')
            receiver = get_info()
            print('Mention your message to be sent')
            update_textbox('Mention your message to be sent')
            talk('Mention your message to be sent')
            msg_content = get_info()
            pywhatkit.sendwhatmsg_instantly(phone_no = individual_contact[receiver],message = msg_content)
            print('Msg sent successfully!!')
            update_textbox("Msg sent successfully!!")
            talk('Msg sent successfully!!')
        elif 'group' in reply2:
            print('Which group do you like to send message?')
            update_textbox('Which group do you like to send message?')
            talk('Which group do you like to send message?')
            receiver = get_info()
            print('Enter the message to be sent')
            update_textbox('Enter the message to be sent')
            talk('Enter the message to be sent')
            msg_content = get_info()
            pywhatkit.sendwhatmsg_to_group(receiver, msg_content, 23,27)
            print('Msg sent successfully!!')
            update_textbox('Msg sent successfully!!')
            talk('Msg sent successfully!!')
    else:
        pass


def take_command():
        try:
            with sr.Microphone() as source:
                print('How can I help you?')
                update_textbox("How can I help you?")
                # my_text.insert(tkinter.END, 'How can I help you?\n')
                # my_text.insert(tkinter.END, 'Listening...\n')
                update_textbox("Listening...")
                talk('How can I help you?')
                print('Listening...')
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
                #print(command)
        except:
            pass
        return command

def screenshot():
    # take screenshot using pyautogui
    
    talk("Taking Screenshot")
    image = pyautogui.screenshot()
    
    # since the pyautogui takes as a 
    # PIL(pillow) and in RGB we need to 
    # convert it to numpy array and BGR 
    # so we can write it to the disk
    image = cv2.cvtColor(np.array(image),
                        cv2.COLOR_RGB2BGR)
    
    # writing it to the disk using opencv
    cv2.imwrite("image1.png", image)
    talk("Screenshot taken")

def send_email(receiver, subject, message):

    #Sender information
    user = 'rishikarishi1402@gmail.com'
     # a token for gmail
    app_password = 'lyllnxjhrcpmfuqn'
    

    #Yagmail function to send mail
    with yagmail.SMTP(user, app_password) as yag:
        yag.send(receiver, subject, message)
        print('Sent email successfully')
    
    #Confirmation message
    talk('Your email is successfully sent')
    update_textbox('Your email is successfully sent')
    print('Your email is successfully sent')
    talk('Do you want to send more email?')
    update_textbox('Do you want to send more email?')
    print('Do you want to send more email?')
    send_more = get_info()

    #To send extra mail
    if send_more == 'yes':
        get_email_info()

#To get information like receiver, subject, body of the mail

def get_email_info():

    #To get the name of the receiver
    print('To whom you want to send email')
    update_textbox('To whom you want to send email')
    talk('To whom you want to send email')
    name = get_info()

    #If receiver is whole class students!!
    if 'all' in name:
        receiver = ['ucs19324@rmd.ac.in','nishakollacheri@gmail.com','rdrkailash@gmail.com']
    else:
        receiver = email_list[name]
    print(receiver)
    update_textbox(receiver)

    #To get the suject of the mail
    talk('What is the subject of your email?')
    print('What is the subject of your email?')
    update_textbox('What is the subject of your email?')
    subject = get_info()

    #To get the body of the mail
    talk('Tell me the text in your email')
    print('Tell me the text in your email')
    update_textbox('What is the subject of your email?')
    message = get_info()
    send_email(receiver, subject, message)

def translator(target_language):
    # Initialize the speech recognizer
    r = sr.Recognizer()

    # Set the target language for translation
    # target_language = 'ml'

    # Use the microphone as the audio source
    with sr.Microphone() as source:
        talk('Speak now...')
        print('Speak now...')
        update_textbox('Speak now...')
        audio = r.listen(source)

    # Transcribe the speech using the SpeechRecognition library
    transcription = r.recognize_google(audio)

    # Detect the language of the transcription using the Googletrans library
    translator = Translator()
    language_code = translator.detect(transcription).lang

    # Translate the transcription to the target language using the Googletrans library
    translation = translator.translate(transcription, dest=target_language)

    # Print the original transcription, detected language, and the translated text
    print(f'Original transcription: {transcription}')

    print(f'Detected language: {language_code}')
    txt = translation.text
    update_textbox(txt)
    print(f'Translated text: {translation.text}')
 

    # Convert the translated text to speech using gTTS
    tts = gTTS(text=translation.text, lang=target_language)
    tts.save('translated_audio.mp3')

    # Play the translated audio file using the playsound library
    playsound.playsound('translated_audio.mp3', True)

    # Delete the translated audio file
    os.remove('translated_audio.mp3')


def virtual_painter():
    #contants
    ml = 150
    max_x, max_y = 250+ml, 50
    curr_tool = "select tool"
    time_init = True
    rad = 40
    var_inits = False
    thick = 4
    prevx, prevy = 0,0

    #get tools function
    def getTool(x):
        if x < 50 + ml:
            return "line"

        elif x<100 + ml:
            return "rectangle"

        elif x < 150 + ml:
            return"draw"

        elif x<200 + ml:
            return "circle"

        else:
            return "erase"

    def index_raised(yi, y9):
        if (y9 - yi) > 40:
            return True

        return False



    hands = mp.solutions.hands
    hand_landmark = hands.Hands(min_detection_confidence=0.6, min_tracking_confidence=0.6, max_num_hands=1)
    draw = mp.solutions.drawing_utils


    # drawing tools
    tools = cv2.imread("tools.png")
    tools = tools.astype('uint8')

    mask = np.ones((480, 640))*255
    mask = mask.astype('uint8')
    '''
    tools = np.zeros((max_y+5, max_x+5, 3), dtype="uint8")
    cv2.rectangle(tools, (0,0), (max_x, max_y), (0,0,255), 2)
    cv2.line(tools, (50,0), (50,50), (0,0,255), 2)
    cv2.line(tools, (100,0), (100,50), (0,0,255), 2)
    cv2.line(tools, (150,0), (150,50), (0,0,255), 2)
    cv2.line(tools, (200,0), (200,50), (0,0,255), 2)
    '''

    cap = cv2.VideoCapture(0)
    while True:
        _, frm = cap.read()
        frm = cv2.flip(frm, 1)

        rgb = cv2.cvtColor(frm, cv2.COLOR_BGR2RGB)

        op = hand_landmark.process(rgb)

        if op.multi_hand_landmarks:
            for i in op.multi_hand_landmarks:
                draw.draw_landmarks(frm, i, hands.HAND_CONNECTIONS)
                x, y = int(i.landmark[8].x*640), int(i.landmark[8].y*480)

                if x < max_x and y < max_y and x > ml:
                    if time_init:
                        ctime = time.time()
                        time_init = False
                    ptime = time.time()

                    cv2.circle(frm, (x, y), rad, (0,255,255), 2)
                    rad -= 1

                    if (ptime - ctime) > 0.8:
                        curr_tool = getTool(x)
                        print("your current tool set to : ", curr_tool)
                        time_init = True
                        rad = 40

                else:
                    time_init = True
                    rad = 40

                if curr_tool == "draw":
                    xi, yi = int(i.landmark[12].x*640), int(i.landmark[12].y*480)
                    y9  = int(i.landmark[9].y*480)

                    if index_raised(yi, y9):
                        cv2.line(mask, (prevx, prevy), (x, y), 0, thick)
                        prevx, prevy = x, y

                    else:
                        prevx = x
                        prevy = y



                elif curr_tool == "line":
                    xi, yi = int(i.landmark[12].x*640), int(i.landmark[12].y*480) 
                    y9  = int(i.landmark[9].y*480)

                    if index_raised(yi, y9):
                        if not(var_inits):
                            xii, yii = x, y
                            var_inits = True

                        cv2.line(frm, (xii, yii), (x, y), (50,152,255), thick)

                    else:
                        if var_inits:
                            cv2.line(mask, (xii, yii), (x, y), 0, thick)
                            var_inits = False

                elif curr_tool == "rectangle":
                    xi, yi = int(i.landmark[12].x*640), int(i.landmark[12].y*480)
                    y9  = int(i.landmark[9].y*480)

                    if index_raised(yi, y9):
                        if not(var_inits):
                            xii, yii = x, y
                            var_inits = True

                        cv2.rectangle(frm, (xii, yii), (x, y), (0,255,255), thick)

                    else:
                        if var_inits:
                            cv2.rectangle(mask, (xii, yii), (x, y), 0, thick)
                            var_inits = False

                elif curr_tool == "circle":
                    xi, yi = int(i.landmark[12].x*640), int(i.landmark[12].y*480)
                    y9  = int(i.landmark[9].y*480)

                    if index_raised(yi, y9):
                        if not(var_inits):
                            xii, yii = x, y
                            var_inits = True

                        cv2.circle(frm, (xii, yii), int(((xii-x)**2 + (yii-y)**2)**0.5), (255,255,0), thick)

                    else:
                        if var_inits:
                            cv2.circle(mask, (xii, yii), int(((xii-x)**2 + (yii-y)**2)**0.5), (0,255,0), thick)
                            var_inits = False

                elif curr_tool == "erase":
                    xi, yi = int(i.landmark[12].x*640), int(i.landmark[12].y*480)
                    y9  = int(i.landmark[9].y*480)

                    if index_raised(yi, y9):
                        cv2.circle(frm, (x, y), 30, (0,0,0), -1)
                        cv2.circle(mask, (x, y), 30, 255, -1)



        op = cv2.bitwise_and(frm, frm, mask=mask)
        frm[:, :, 1] = op[:, :, 1]
        frm[:, :, 2] = op[:, :, 2]

        frm[:max_y, ml:max_x] = cv2.addWeighted(tools, 0.7, frm[:max_y, ml:max_x], 0.3, 0)

        cv2.putText(frm, curr_tool, (270+ml,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
        cv2.imshow("paint app", frm)

        if cv2.waitKey(1) == 27:
            cv2.destroyAllWindows()
            cap.release()
            break

def translate():
    talk('Which language do you want to translate?')
    update_textbox('Which language do you want to translate?')
    command = get_info()
    if 'tamil' in command:
        translator('ta')
    elif 'malayalam' in command:
        translator('ml')
    elif 'hindi' in command:
        translator('hi')
    elif 'english' in command:
        translator('en')
    elif 'telugu' in command:
        translator('te')


label_1 = customtkinter.CTkLabel(master=frame_1, text ="Welcome" ,justify=tkinter.LEFT)
label_1.pack(pady=5, padx=5)

label_2 = customtkinter.CTkLabel(master=frame_1, text="This is an AI Powered Tool to make your work easier", justify=tkinter.LEFT)
label_2.pack(pady = 5, padx = 5)

label_3 = customtkinter.CTkLabel(master=frame_1, text="How can I help You?", justify=tkinter.LEFT)
label_3.pack(pady = 5, padx = 5)


def run_alexa():
    command = take_command()
    update_textbox(command)
    # my_text.insert(tkinter.END, command +'\n')
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        text = 'Playing...' + song
        update_textbox(text)
        # my_text.insert(tkinter.END, 'Playing...' + song+'\n')
        talk('Playing...' + song)
        pywhatkit.playonyt(song)

    elif 'whatsapp' in command:
        whatsapp_msg()

    elif 'how are you' in command:
        talk("I am fine, Thank you")
        update_textbox("I am fine, Thank you")
        print("I am fine, Thank you")
        talk("How are you, Sir")
        update_textbox("How are you, Sir")
        print("How are you, Sir")

    elif 'i am fine' in command or "i am good" in command:
        talk("It's good to know that your fine")
        update_textbox("It's good to know that your fine")
        print("It's good to know that your fine")

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        res = 'Correct time is:' + time
        update_textbox(res)
        talk(res)

    elif 'what' in command:
        subject = command.replace('what is','')
        info = wikipedia.summary(subject, 3)
        print(info)
        update_textbox(info)
        talk(info)

    elif 'who' in command:
        person = command.replace('who is','')
        info = wikipedia.summary(person,3)
        print(info)
        update_textbox(info)
        talk(info)

    elif 'explain' in command:
        subject = command.replace('explain','')
        info = wikipedia.summary(subject,3)
        print(info)
        update_textbox(info)
        talk(info)

    elif 'joke' in command:
        print(pyjokes.get_joke())
        update_textbox(info)
        talk(pyjokes.get_joke())

    elif 'email' in command:
        get_email_info()

    elif 'painter' in command:
        virtual_painter()

    elif 'open word document' in command:
        talk("Opening Microsoft Word")
        os.startfile("C:/Program Files (x86)/Microsoft Office/root/Office16/WINWORD.EXE")

    elif 'open powerpoint' in command:
        talk("Opening power point")
        os.startfile("C:/Program Files (x86)/Microsoft Office/root/Office16/POWERPNT.EXE")

    elif 'open one note' in command:
        talk("Opening one note")
        os.startfile("C:/Program Files (x86)/Microsoft Office/root/Office16/ONENOTE.EXE")

    elif 'open excel' in command:
        talk("Opening excel")
        os.startfile("C:/Program Files (x86)/Microsoft Office/root/Office16/EXCEL.EXE")

    elif 'open wikipedia' in command:
        talk("Here you go to Wikipedia\n")
        update_textbox('Here you go to Wikipedia')
        # webbrowser.open("https://wikipedia.org/")
        webbrowser.open("https://wikipedia.org/", new=2)

    elif 'open youtube' in command:
        talk("Here you go to Youtube\n")
        update_textbox('Here you go to Youtube')
        webbrowser.open("https://youtube.com")
        # time.sleep(9)

    elif 'open google' in command:
        talk("Here you go to Google\n")
        update_textbox('Here you go to Google')
        webbrowser.open("https://google.com")
        # time.sleep(9)

    elif "where is" in command:
        query = command.replace("where is", "")
        location = query
        talk("User asked to Locate")
        talk(location)
        res = "User asked to Locate" + location
        update_textbox(res)
        webbrowser.open("https://www.google.com/maps/place/" + location.strip().rstrip())

    elif 'open translator' in command:
        translate()

    elif "write a note" in command:
        talk("What should i write")
        note = get_info()
        file = open('notes.txt', 'w')
        file.write(note)

    elif "show note" in command:
        talk("Showing Notes")
        file = open("notes.txt", "r")
        os.startfile("C:/Users/DELL/Desktop/CTK Project/notes.txt")
    
    elif 'screenshot' in command:
        screenshot()

    elif 'exit' in command or 'bye' in command:
        talk("Thanks for giving me your time")
        update_textbox('Thanks for giving me your time')
        exit()
        
    elif '' in command:
        talk('Please say the command again!!')
        print('Please say the command again!!')
        update_textbox('Please say the command again!!')

    







# frame_1 = customtkinter.CTkFrame(master=app)
# frame_1.pack(pady=20, padx=60, fill="both", expand=True)



button_default = customtkinter.CTkButton(master=frame_1, text = "Enable audio", command=run_alexa)
button_default.pack(pady=10, padx=10)

button_1 = customtkinter.CTkButton(master=frame_1, text = "Virtual Painter", command=virtual_painter)
button_1.pack(pady=10, padx=10)

button_2 = customtkinter.CTkButton(master=frame_1, text = "Translation", command=translate)
button_2.pack(pady=10, padx=10)

button_3 = customtkinter.CTkButton(master=frame_1, text = "Email Automation", command=get_email_info)
button_3.pack(pady=10, padx=10)

button_4 = customtkinter.CTkButton(master=frame_1, text = "Whatsapp Messaging", command=whatsapp_msg)
button_4.pack(pady=10, padx=10)

# button_5 = customtkinter.CTkButton(master=frame_1, text = "Audio Book", command=button_callback)
# button_5.pack(pady=10, padx=10)

# text_frame = customtkinter.CTkFrame(app,corner_radius=10)
# text_frame.pack(pady=10)

# my_text = tkinter.Text(text_frame, height=20, width=67, wrap=tkinter.WORD, bd=0, bg="#292929", fg="silver")
# my_text.pack(pady=10)




entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Enter your command", width=520, height=30)
entry_1.pack(pady=10, padx=10)


          
def get_text_info():
    command = entry_1.get()
    return command


def text_alexa():
    command = get_text_info()
    update_textbox(command)
    command = command.lower()
    if 'play' in command:
        song = command.replace('play','')
        text = 'Playing...' + song
        update_textbox(text)
        # my_text.insert(tkinter.END, 'Playing...' + song+'\n')
        talk('Playing...' + song)
        pywhatkit.playonyt(song)

    elif 'whatsapp yes' in command:
        talk("Whom do you like to send message?")
        update_textbox("Whom do you like to send message?")
        print("Whom do you like to send message?")

    elif 'whatsapp rishika' in command:
        talk("Mention your message to be sent")
        update_textbox("Mention your message to be sent")
        print("Mention your message to be sent")

    elif 'whatsapp' in command:
        print("Hello this is a Whatsapp Automation tool!") 
        update_textbox('Hello this is a Whatsapp Automation tool!')
        # my_text.insert(tkinter.END, 'Hello this is a Whatsapp Automation tool!\n')
        talk("Hello this is a Whatsapp Automation tool!")
        print("Do you like to send message?")
        update_textbox('Do you like to send message?')
        # my_text.insert(tkinter.END, 'Do you like to send message?\n')
        talk("Do you like to send message?")
    
    
    
    

    elif 'how are you' in command:
        talk("I am fine, Thank you")
        update_textbox("I am fine, Thank you")
        print("I am fine, Thank you")
        talk("How are you, Sir")
        update_textbox("How are you, Sir")
        print("How are you, Sir")

    elif 'i am fine' in command or "i am good" in command:
        talk("It's good to know that your fine")
        update_textbox("It's good to know that your fine")
        print("It's good to know that your fine")

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        res = 'Correct time is:' + time
        update_textbox(res)
        talk(res)

    elif 'what' in command:
        subject = command.replace('what is','')
        info = wikipedia.summary(subject, 3)
        print(info)
        update_textbox(info)
        talk(info)

    elif 'who' in command:
        person = command.replace('who is','')
        info = wikipedia.summary(person,3)
        print(info)
        update_textbox(info)
        talk(info)

    elif 'explain' in command:
        subject = command.replace('explain','')
        info = wikipedia.summary(subject,3)
        print(info)
        update_textbox(info)
        talk(info)

    elif 'joke' in command:
        print(pyjokes.get_joke())
        update_textbox(info)
        talk(pyjokes.get_joke())

    elif 'email' in command:
        get_email_info()

    elif 'painter' in command:
        virtual_painter()

    elif 'open word document' in command:
        talk("Opening Microsoft Word")
        os.startfile("C:/Program Files (x86)/Microsoft Office/root/Office16/WINWORD.EXE")

    elif 'open powerpoint' in command:
        talk("Opening power point")
        os.startfile("C:/Program Files (x86)/Microsoft Office/root/Office16/POWERPNT.EXE")

    elif 'open one note' in command:
        talk("Opening one note")
        os.startfile("C:/Program Files (x86)/Microsoft Office/root/Office16/ONENOTE.EXE")

    elif 'open excel' in command:
        talk("Opening excel")
        os.startfile("C:/Program Files (x86)/Microsoft Office/root/Office16/EXCEL.EXE")

    elif 'open wikipedia' in command:
        talk("Here you go to Wikipedia\n")
        update_textbox('Here you go to Wikipedia')
        # webbrowser.open("https://wikipedia.org/")
        webbrowser.open("https://wikipedia.org/", new=2)

    elif 'open youtube' in command:
        talk("Here you go to Youtube\n")
        update_textbox('Here you go to Youtube')
        webbrowser.open("https://youtube.com")
        # time.sleep(9)

    elif 'open google' in command:
        talk("Here you go to Google\n")
        update_textbox('Here you go to Google')
        webbrowser.open("https://google.com")
        # time.sleep(9)

    elif "where is" in command:
        query = command.replace("where is", "")
        location = query
        talk("User asked to Locate")
        talk(location)
        res = "User asked to Locate" + location
        update_textbox(res)
        webbrowser.open("https://www.google.com/maps/place/" + location.strip().rstrip())

    elif 'open translator' in command:
        translate()

    elif "write a note" in command:
        talk("What should i write")
        note = get_text_info()
        file = open('notes.txt', 'w')
        file.write(note)

    elif "show note" in command:
        talk("Showing Notes")
        file = open("notes.txt", "r")
        os.startfile("C:/Users/DELL/Desktop/CTK Project/notes.txt")
    
    elif 'screenshot' in command:
        screenshot()

    elif 'exit' in command or 'bye' in command:
        talk("Thanks for giving me your time")
        update_textbox('Thanks for giving me your time')
        exit()
        
    

    else:
        pywhatkit.sendwhatmsg_instantly(phone_no = +919940215836,message = command)
        print('Msg sent successfully!!')
        update_textbox("Msg sent successfully!!")
        talk('Msg sent successfully!!')

   
# button_6 = customtkinter.CTkButton(master=frame_1, text = "Enter", command=get_text_info)
# button_6.pack(pady=10, padx=10)   

button_7 = customtkinter.CTkButton(master=frame_1, text = "Enable Text", command=text_alexa)
button_7.pack(pady=10, padx=10)

button_8 = customtkinter.CTkButton(master=frame_1, text = "Exit", command=app.destroy)
button_8.pack(pady=10, padx=10)

# text_frame = customtkinter.CTkFrame(master,corner_radius=)
# optionmenu_1 = customtkinter.CTkOptionMenu(frame_1, values=["Option 1", "Option 2", "Option 42 long long long..."])
# optionmenu_1.pack(pady=10, padx=10)
# optionmenu_1.set("CTkOptionMenu")





greet_alexa()    


app.mainloop()