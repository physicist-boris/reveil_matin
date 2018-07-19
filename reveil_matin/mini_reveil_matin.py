from datetime import timedelta
import threading
from tkinter import *
import subprocess
import time


root = Tk()
root.geometry("500x500")
labelfont = ('times', 20, 'bold')
frame_principal =Frame(root, width=500, height=500)
frame_principal.pack()
welcome_word = Label(frame_principal, text="Bienvenue !",bg = "black", fg='yellow', height=3, width=20)
welcome_word.config(font = labelfont)
welcome_word.pack()
frame_second = Frame(root, width=500, height=500)

questions = Label(frame_principal, text = "Dans combien de temps souhaitez-vous vous réveiller? Ex:hours/minutes/secondes")
questions.pack()
time_wake = Entry(frame_principal, bg  ="yellow", bd = 3, fg = "blue")
time_wake.insert(0, "24/60/60")
time_wake.pack()
questions_2 = Label(frame_principal, text = "Intervalles de rappel et nombres de fois(Ex: nombres de fois/intervalles de rappel(secondes)")
questions_2.pack()
time_rappel = Entry(frame_principal, bg  ="yellow", bd = 3, fg ="blue")
time_rappel.insert(0, "nombres de fois/intervalles de temps")
time_rappel.pack()

def time_wake_callback(event):
    time_wake.delete(0, "end")
    return None

def time_rappel_callback(event):
    time_rappel.delete(0, "end")
    return None


def reveil():
    frame_principal.pack_forget()
    frame_second.pack()
    list_time_wake = time_wake.get().split("/")
    another_year = timedelta(hours=int(list_time_wake[0]),
                             minutes=int(list_time_wake[1]), seconds=int(list_time_wake[2]))

    time.sleep(another_year.total_seconds())

    def on_space(event):
        print("c fdjscjds cd")
        p.kill()

    def wake_up():
        global p
        p = subprocess.Popen(["python.exe", "son_pa.py"])

    wake_up()
    root.bind("<Key-space>", on_space)

    nbr = 1
    list_time_rappel = time_rappel.get().split("/")
    temps_interval = int(list_time_rappel[1]) + 4
    while nbr <= int(list_time_rappel[0]) - 1:
        t = threading.Timer(temps_interval, wake_up)
        t.start()
        nbr += 1
        temps_interval += (int(list_time_rappel[1]) + 4)


b = Button(frame_principal, text="commencer", width=10, command=reveil)
b.pack()

time_wake.bind("<Button-1>", time_wake_callback)
time_rappel.bind("<Button-1>", time_rappel_callback)

root.mainloop()
