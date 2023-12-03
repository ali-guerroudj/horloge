# horloge analogique
# -*- coding: utf_8 -*-
from Tkinter import *
from math import *
from time import *
from winsound import *

global  hala , mala, heuala, iala, ichro, t0, dessala, iafd
hala, mala, heuala, iala, ichro, t0, dessala, iafd = 0, 0, 0, 0, 0, 0, 0, 0

def dessine_horloge() :
    can1.create_oval(25, 25, 175, 175, fill='', width=8,outline='gold')
    can1.create_oval(20, 20, 180, 180, fill='', width=1)    
    can1.create_oval(92,92,108,108, fill='gold',outline='black',width=1,tag="axe")
    can1.tag_bind("axe","<ButtonRelease>",affich_digit)
    can1.tag_bind("axe","<Enter>",curseur_main)
    can1.tag_bind("axe","<Leave>",curseur_fleche)
    i = 1
    while i < 61 :
        j = i*((2*pi)/60)
        # diametre horloge = 75  centre canvas =100,100
        x=(cos(j)*75)+100
        y=(sin(j)*75)+100
        can1.create_oval(x-1, y-1, x+1, y+1, fill='blue')
        if i in (15,30,45,60):
            can1.create_oval(x-4, y-4, x+4, y+4, fill='black')
        if i in (5,10,20,25,35,40,50,55):
            can1.create_oval(x-2, y-2, x+2, y+2, fill='blue')
        i = i+1

def affich_digit(e) :
    global iafd
    if iafd == 0 :
        iafd=1
    else : iafd=0    
    
def aff_heure() :
    global  hala, mala, heuala, indala, iafd
    dateheure=localtime()
    heur=dateheure[3]
    minu=dateheure[4]
    seco=dateheure[5]
    heurd=heur
    minud=minu
    if str(heur) == str(hala) and str(minu) == str(mala) and iala == 1 :
        Beep(800,100)
    if heur >12 :
        heur = heur -12        
    if ichro == 1 :
        t1=(dateheure[3]*3600)+(dateheure[4]*60)+dateheure[5]
        tchro = t1 - t0
        hchro = int(tchro/3600)
        mchro = int((tchro-(hchro*3600))/60)
        schro=tchro-(hchro*3600)-(mchro*60)
        affchro.configure(text = '%d' %hchro+'.%02d' %mchro+'.%02d'%schro, bg='white')
    # affich heures
    heur=heur+(minu/60.00)
    j=(heur+9)*((2*pi)/12)
    x=(cos(j)*55)+100
    y=(sin(j)*55)+100
    can1.coords(aigheu, 100, 100, x, y)
    # affich minutes
    minu=minu+(seco/60.0)
    j=(minu+45)*((2*pi)/60)
    x=(cos(j)*65)+100
    y=(sin(j)*65)+100
    can1.coords(aigmin, 100, 100, x, y)
    # affich secondes
    j=(seco+45)*((2*pi)/60)
    x=(cos(j)*70)+100
    y=(sin(j)*70)+100
    can1.coords(aigsec, 100, 100, x, y)
    if ichro == 1 and tchro < 60 :
        x=(cos(j)*84)+100
        y=(sin(j)*84)+100
        can1.create_oval(x-1, y-1, x+1, y+1, fill='green', outline='darkgreen')
    #afficher heure digitale
    if iafd == 1 :
        afdigi.configure(text = '%d' %heurd +" h " +'%02d' %minud)
    else : afdigi.configure(text ='',bg='lightgrey')
    can1.after(999,aff_heure)

def dessine_alarme() :
    global can2 , choixala, iala, dessala
    if dessala == 0 :
        can2 = Canvas(fen1, width=200, height=50, bg='lightgrey')
        can2.pack()
        choixala = Label(can2,font=('Arial', 7),fg='darkgreen')
        choixala.pack(side=BOTTOM)
        curs= Scale(can2, from_=0.0, to=12.00, length=150, sliderlength=7,
                    resolution=0.01, showvalue=0, orient=HORIZONTAL,
                    label="Réglage de l'alarme :",command=choix_alarme,font=('Arial', 8),fg='blue')
        curs.pack(side=LEFT)
        bouon=Button(can2, text="On", command=set_alarme,font=('Arial', 7),bg='grey')
        bouon.pack(side=BOTTOM)
        dessala = 1
        bouoff=Button(can2, text="Off", command=setoff_alarme,font=('Arial', 7),bg='grey')
        bouoff.pack(side=BOTTOM)
    
def choix_alarme(valcurs) :
    global  hala, mala, heuala
    heuala=float(valcurs)
    j=(heuala+9)*((2*pi)/12)
    x=(cos(j)*70)+100
    y=(sin(j)*70)+100
    can1.coords(aigala, 100, 100, x, y)
    can1.itemconfigure(aigala,fill="red")
    hala=int(heuala)
    mala=int((heuala - hala) * 60)
    dateheure=localtime()
    heur=dateheure[3]
    if heur > 11 :
        hala = hala + 12
    choixala.configure(text = "Déclencher l'alarme à " +'% d' %hala +" h. " +'%02d' %mala)

def set_alarme() :
    global indala, iala, dessala
    dessala = 0
    if iala ==1 :
        can1.delete(indala)
    bouala.config(bg='red')
    j=(heuala+9)*((2*pi)/12)
    x=(cos(j)*75)+100
    y=(sin(j)*75)+100
    indala=can1.create_oval(x-2, y-2, x+2, y+2, fill='red')
    iala =1
    affala.configure(text = '%d' %hala +" h." +'%02d' %mala,bg='white')
    can2.destroy()
    Beep(1000,20)

def setoff_alarme() :
    global indala, iala, dessala
    if dessala == 1 :
        can2.destroy()
        dessala = 0
    bouala.config(bg='grey')
    can1.itemconfigure(aigala,fill="lightgrey")
    if iala ==1 :
        can1.delete(indala)
    iala =0
    affala.configure(text = '',bg='lightgrey')
    Beep(100,50)

def chrono() :
    global ichro, t0
    if ichro == 0 :
        ichro = 1
        dateheure=localtime()
        t0=(dateheure[3]*3600)+(dateheure[4]*60)+dateheure[5]
        bouchro.config(bg='green')
    elif ichro == 1 :
        ichro = 2
        bouchro.config(bg='lightblue')
    else :
        ichro = 0
        bouchro.config(bg='grey')
        can1.create_oval(16, 16, 184, 184, fill='', outline='lightgrey', width=6)
        affchro.configure(text='',bg='lightgrey')

def aff_infos(e) :
    feninf = Toplevel()
    feninf.config(bg='lightblue')
    geo1=fen1.winfo_geometry()
    geox=fen1.winfo_rootx()
    geoy=fen1.winfo_rooty() 
    feninf.geometry("270x260+"+str(geox-50)+"+"+str(geoy-22))
    feninf.title("À propos de Horloge")
    labinf=Label(feninf, bg='lightblue',fg='black',width=50,font=('Arial', 9),
        text= "\nHorloge v.1.3\n\n"
                "Programme écrit en Python / Tkinter\n"
                 "et distribué sous licence GNU GPL.\n\n"
                "© 2007  Yves Le Chevalier\n"
                 "( yveslechevalier@free.fr )\n\n"
                "Ce programme affiche une horloge      \n"
                "avec une alarme, un chronomètre et    \n"
                 "un affichage digital losque l'on clique  \n"
                 "sur l'axe des aiguilles.                            ")
    labinf.pack(pady=5)
    bouf3=Button(feninf, text="Fermer", command=feninf.destroy,bg="orange", fg='brown')
    bouf3.pack(side=BOTTOM,pady=10)
    #feninf.transient()
    feninf.grab_set()
    feninf.wait_window()
    
def curseur_main(e) :
    fen1.config(cursor='hand2')

def curseur_fleche(e) :
    fen1.config(cursor='arrow')
     
# main
fen1 = Tk(className='Horloge')
fen1.geometry("+500+400")
fen1.resizable(width=False, height=False)
can1 = Canvas(fen1, width=200, height=200, bg='lightgrey')
aigala = can1.create_line(100, 100, 100, 35, fill='', width=1,arrow=LAST)
aigheu = can1.create_line(100, 100, 100, 50, fill='blue', width=3)
aigmin = can1.create_line(100, 100, 100, 40, fill='blue', width=2)
aigsec = can1.create_line(100, 100, 100, 27, fill='yellow', width=1)
bouala=Button(can1, text="Alarme", command=dessine_alarme, font=('Arial', 7),bg='grey')
bouala.place(x=2,y=2)
affala = Label(can1, font=('Arial', 7))
affala.place(x=4,y=22)
bouchro=Button(can1, text="Chrono", command=chrono, font=('Arial', 7),bg='grey')
bouchro.place(x=163,y=2)
affchro = Label(can1, font=('Arial', 7))
affchro.place(x=164,y=22)
bquit=Button(can1, text="Quitter", command=fen1.destroy, font=('Arial', 6),bg='pink',fg='black')
bquit.place(x=2,y=183)
afdigi = Label(can1, font=('Arial',9,'bold'),fg="blue")
afdigi.place(x=78,y=188)
signature='YLC.gif'
signat=PhotoImage(file=signature)
sign=can1.create_image(192,195, image=signat,tag="ylc")
can1.tag_bind("ylc","<ButtonRelease>",aff_infos)
can1.tag_bind("ylc","<Enter>",curseur_main)
can1.tag_bind("ylc","<Leave>",curseur_fleche)
can1.pack()

dessine_horloge()
aff_heure()

fen1.mainloop()