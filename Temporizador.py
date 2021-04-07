from tkinter import Tk, Frame, Label, Entry, Button
from playsound import playsound
import time
import tkinter
import threading


# Distribucion de ventana --------------------------

ventana = Tk()
ventana.config(bg="#2d3e52")
ventana.resizable(1,1)

fondo = Frame(ventana)
fondo.config(bg="#2d3e52")
fondo.pack(fill="both", expand="true", padx=20, pady=30)

Label(fondo, text="Temporizador de\nEjercicios", bg="#2d3e52", fg="white", font=("Arial", 36, "bold")).grid(row=0, column=0)

# Display donde se muestran iniciales y temporizador
display = Frame(fondo, bg="#1d2e42")
display.grid(row=1, column=0, ipady=10)


# temporizador de ronda y de descanso ---------------------

n_ronda = 2 #numero de rondas faltantes
t_ronda = 5 #tiempo de cada ronda
t_descanso = 5 #tiempo de descanso
t = t_ronda

# iniciar temporizador
def iniciar():
    global n_ronda, t_ronda, t_descanso, t

    if(entry_n_ronda.get().isdecimal() and entry_t_ronda.get().isdecimal() and entry_t_descanso.get().isdecimal()):
        n_ronda = int(entry_n_ronda.get()) #numero de rondas faltantes
        t_ronda = int(entry_t_ronda.get()) #tiempo de cada ronda
        t_descanso = int(entry_t_descanso.get()) #tiempo de descanso
        t = t_ronda

        run_btn.grid_remove()

        run_timer_ronda()
        
        
# Correr una ronda
def run_timer_ronda():
    global t, t_ronda, n_ronda
    for w in display.winfo_children():
        w.grid_remove()

    if(t>0 and t<4):
        sonar_suave()
        #print("sonidop suave") # Espacio para funcion que reproduce un sonido suave
    if(t == 0):
        sonar_fuerte()
        #print("sonido fuerte") # Espacio para funcion que reproduce un sonido fuerte
    
    Label(display, text="Ejercicio", bg="#1d2e42", fg="white", font=("Arial", 16, "bold")).grid(row=0, column=0)
    Label(display, text=time.strftime("%H:%M:%S", time.gmtime(t)), bg="#1d2e42", fg="white", font=("Arial", 36, "bold")).grid(row=1, column=0)

    if(t>0):
        t -= 1
        ventana.after(1000, run_timer_ronda)#ESTO DEBERIA SER UN HILO
    else:
        n_ronda -= 1
        t = t_descanso
        if(n_ronda > 0):
            ventana.after(1000, run_timer_descanso)
        else:
            ventana.after(1000, terminar)

# Correr un descanso
def run_timer_descanso():
    global t, t_ronda
    for w in display.winfo_children():
        w.grid_remove()

    if(t>0 and t<4):
        sonar_suave()
        print("sonido suave") # Espacio para funcion que reproduce un sonido suave

    if(t == 0):
        sonar_fuerte()
        print("sonido fuerte") # Espacio para funcion que reproduce un sonido fuerte

    Label(display, text="Descanso", bg="#1d2e42", fg="white", font=("Arial", 16, "bold")).grid(row=0, column=0)
    Label(display, text=time.strftime("%H:%M:%S", time.gmtime(t)), bg="#1d2e42", fg="white", font=("Arial", 36, "bold")).grid(row=1, column=0)
    
    if(t>0):
        t -= 1
        ventana.after(1000, run_timer_descanso)
    else:
        t = t_ronda
        ventana.after(1000, run_timer_ronda)

#Sonidos
def sonar_suave():
        pista_suave = "sounds/short.mp3"
        print("sonando suave")
        playsound(pista_suave)
        

def sonar_fuerte():
        pista_fuerte = "sounds/large.mp3"
        print("sonando fuerte")
        playsound(pista_fuerte)

# Ventana de terminacion --------------------------

def terminar():
    for w in display.winfo_children():
        w.grid_remove()
    
    Label(display, text="Felicitaciones!", bg="#1d2e42", fg="white", font=("Arial", 30, "bold")).grid(row=0, column=0)
    Label(display, text="Has terminado todas las rondas", bg="#1d2e42", fg="white", font=("Arial", 20, "bold")).grid(row=1, column=0)

    Button(fondo, text="Continuar", command=init, relief="flat", bg="#e67f22", fg="white", font=("Arial", 14, "bold")).grid(row=2, column=0)
    

# Ventana inicial ----------------------------------

# Entrada de numero de rondas
disp_n_rondas = Frame(display, bg="#1d2e42")
Label(disp_n_rondas, text="Numero de\nrondas", bg="#1d2e42", fg="white", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2)
entry_n_ronda = Entry(disp_n_rondas, font=("Arial", 12, "bold"), width=4)
entry_n_ronda.grid(row=1, column=0, sticky="e")
entry_n_ronda.insert(0, "5")
Label(disp_n_rondas, text="Rondas", bg="#1d2e42", fg="white", font=("Arial", 12, "bold")).grid(row=1, column=1, sticky="w")

# Entrada de tiempo de cada ronda
disp_t_ejercicio = Frame(display, bg="#1d2e42")
Label(disp_t_ejercicio, text="Duracion de\ncada ronda", bg="#1d2e42", fg="white", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2)
entry_t_ronda = Entry(disp_t_ejercicio, font=("Arial", 12, "bold"), width=4)
entry_t_ronda.grid(row=1, column=0, sticky="e")
entry_t_ronda.insert(0, "20")
Label(disp_t_ejercicio, text="Seg.", bg="#1d2e42", fg="white", font=("Arial", 12, "bold")).grid(row=1, column=1, sticky="w")

# Entrada de tiempo de cada descanso
disp_t_descanso = Frame(display, bg="#1d2e42")
Label(disp_t_descanso, text="Duracion del\ndescanso", bg="#1d2e42", fg="white", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2)
entry_t_descanso = Entry(disp_t_descanso, font=("Arial", 12, "bold"), width=4, justify=tkinter.RIGHT)
entry_t_descanso.grid(row=1, column=0, sticky="e")
entry_t_descanso.insert(0, "10")
Label(disp_t_descanso, text="Seg.", bg="#1d2e42", fg="white", font=("Arial", 12, "bold")).grid(row=1, column=1, sticky="w")

# Boton de inicio
run_btn = Button(fondo, text="Iniciar", command=iniciar, relief="flat", bg="#e67f22", fg="white", font=("Arial", 14, "bold"))

# inicializar ventana inicial -------------------------
def init():
    for w in display.winfo_children():
        w.grid_remove()
    disp_n_rondas.grid(row=1, column=0, padx=30, pady=30)
    disp_t_ejercicio.grid(row=1, column=1, padx=30, pady=30)
    disp_t_descanso.grid(row=1, column=2, padx=30, pady=30)
    run_btn.grid(row=2, column=0, columnspan=2)

# Ejecutar ------------------
init()
ventana.mainloop()