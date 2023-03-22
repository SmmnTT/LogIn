
from tkinter import *
from PIL import ImageTk,Image


#Ventana
raiz= Tk()
raiz.title("Log In")
raiz.geometry("800x600")


#Variables
nameEntry=StringVar()
GEN=StringVar()
Terminos=IntVar()

contrasenaUsuario=StringVar()
confirmarcontrasenaUsuario=StringVar()

#Frame
frame=Frame(raiz,bg="#707070")
frame.pack(fill="both",expand=1)


#imagen
im=Image.open("gato.jpg")
imRe=im.resize((200,150))
imagen=ImageTk.PhotoImage(imRe)

imlabel=Label(frame,image=imagen)
imlabel.place(relx=0.4,rely=0.025)










def iniciarSesion():
    
    if confirmarcontrasenaUsuario.get() == contrasenaUsuario.get()and Terminos.get()==1:
        print(f'''Iniciaste sesión correctamente {nameEntry.get()} 
               Sexo: {GEN.get()}
               
              ''')
        frame.config(bg="#008f39")
    elif Terminos.get()!=1:
        print(f'Acepta los términos y condiciones')
    else:
        print('Sigue intentando')


#Etiqueta nombre
etiquetanombre=Label(frame,text="Ingresa tu nombre: ",
                     font=("Roboto",20,"bold"),
                     bg="#707070",
                     fg="#f7f7f7").place(relx=.1 ,rely=.3)
#Entry nombre
nombreEntry=Entry(frame,
                  font=("Roboto",18,"bold"),
                  textvariable=nameEntry).place(relx=0.6,rely=0.3)

#Etiqueta contra
etiquetacontra=Label(frame,text="Ingresa tu contraseña: ",
                     font=("Roboto",20,"bold"),
                     bg="#707070",
                     fg="#f7f7f7").place(relx=.1 ,rely=.4)
#Entry contra
contraEntry=Entry(frame,
                  font=("Roboto",18,"bold"),
                  textvariable=contrasenaUsuario).place(relx=0.6,rely=0.4)

#Etiqueta confirmar contra
etiquetaconfirmar=Label(frame,text="Confirmar contraseña: ",
                     font=("Roboto",20,"bold"),
                     bg="#707070",
                     fg="#f7f7f7").place(relx=.1 ,rely=.5)
#Entry confirmar contra
confirmarEntry=Entry(frame,
                  font=("Roboto",18,"bold"),
                  textvariable=confirmarcontrasenaUsuario).place(relx=0.6,rely=0.5)





#Boton Opcion Hombre
btnH=Radiobutton(frame,text="Hombre",
                  font=("Roboto",20,"bold"),
                  bg="#707070",
                  value="Hombre",
                  variable=GEN)
btnH.place(relx=.25,rely=.6)

#Boton Opcion Mujer
btnM=Radiobutton(frame,text="Mujer",
                  font=("Roboto",20,"bold"),
                  bg="#707070",
                  value="Mujer",
                  variable=GEN)
btnM.place(relx=.5,rely=.6)

#Boton Opcion Aceptar terminos y condiciones
btnTerminos=Radiobutton(frame,text="Aceptar términos y condiciones",
                  font=("Roboto",20,"bold"),
                  bg="#707070",
                  value=1,
                  variable=Terminos)
btnTerminos.place(relx=.2,rely=.7)



#Boton
boton=Button(frame,text="Iniciar",
             font=("Roboto",20,"bold"),
             width=15,
             height=1,
             command=iniciarSesion,
             ).place(relx=.3,rely=.8)



raiz.mainloop()


