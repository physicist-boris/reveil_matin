from datetime import timedelta
import threading
from tkinter import Tk, Frame, Label, Entry, Button
import winsound


def reveil(frame_second, expected_time):
    frame_second.tkraise()
    list_expected_time = expected_time.get().split("/")
    expectime_time_interval = timedelta(hours=int(list_expected_time[0]),
                             minutes=int(list_expected_time[1]), seconds=int(list_expected_time[2]))

    def wake_up():
        winsound.PlaySound('731.wav', winsound.SND_FILENAME)

    increment = 1
    list_time_recall = time_recall.get().split("/")
    timestep_ofrecall = int(list_time_recall[1]) + 4
    timestep = expectime_time_interval.total_seconds()
    while increment <= int(list_time_recall[0]):
        threading.Timer(timestep, wake_up).start()
        increment += 1
        timestep += timestep_ofrecall


def back_principal_frame(frame_principal):
    frame_principal.tkraise()


root = Tk()
root.geometry("500x500")
labelfont = ('times', 20, 'bold')
container = Frame(root)
container.pack(side="top", fill="both", expand=True)
container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)
frame_principal = Frame(container, width=500, height=500)
welcome_word = Label(frame_principal, text="Bienvenue !", bg="black", fg='yellow', height=3, width=20)
welcome_word.config(font=labelfont)
welcome_word.pack()
frame_second = Frame(container, width=500, height=500)
waiting_word = Label(frame_second, text="En attente du réveil", bg="black", fg='yellow', height=3, width=20)
waiting_word.config(font=labelfont)
waiting_word.pack()
button = Button(frame_principal, text="commencer", width=10, command=lambda: reveil(frame_second, expected_time))
button.pack()
button = Button(frame_second, text="Retour menu", width=10, command=lambda: back_principal_frame(frame_principal))
button.pack()

question_1 = Label(frame_principal,
                   text="Dans combien de temps souhaitez-vous vous réveiller? Ex:hours/minutes/secondes")
question_1.pack()
expected_time = Entry(frame_principal, bg="yellow", bd=3, fg="blue")
expected_time.pack()
question_2 = Label(frame_principal,
                   text="Intervalles de rappel et nombres de fois(Ex: nombres de fois/intervalles de rappel(secondes)")
question_2.pack()
time_recall = Entry(frame_principal, bg="yellow", bd=3, fg="blue")
time_recall.pack()
frame_principal.grid(row=0, column=0, sticky="nsew")
frame_second.grid(row=0, column=0, sticky="nsew")
frame_principal.tkraise()
root.mainloop()
