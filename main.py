from tkinter import *
from tkinter import messagebox
from proces import buscador, actualizar, leerID, insertRow, eliminar_desql
from assets import fonts
#procesos de ejecucion


class InterfazTierPregunta:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry('450x500')
        self.ventana.title("namesCuentas")
        self.widget_login_o()

        self.ventana.mainloop()

    def button_borrar(self):
        if self.entry_1.get() >= 0:
            lira = eliminar_desql(self.entry_1.get())
            messagebox.showinfo(message=f'Cuenta Borrada: {self.entry_1.get()}', title="Borrar")
        else:
            messagebox.showinfo(message=f'Insert un numero: en la entrada', title="Recordatorio")

    def button_añadir(self):
        self.valor = 1
        obtenido = leerID("cuentas")
        self.buttons_stdo(0)
        self.text_content.place_forget()
        self.widget_second_o()
        self.entry_id_.delete(0,END)
        self.entry_id_.insert(0,obtenido+1)
        self.entry_id_.config(state= "disabled")

    def button_aceptar(self):
        lista =[self.entry_id_.get(), self.entry_nombre.get(), self.entry_usuario_cuenta.get(), self.entry_contraseña.get(), self.entry_empresa.get(), self.entry_frase_secreta.get(), self.entry_descripcion.get()]
        lista1= ["id", "nombres", "usuario", "contraseña", "empresa", "frasescret", "descripcion"]
        if self.valor == 0:
            for i in range(0,len(lista1)):
                lira = actualizar(lista1[i], lista[i], lista[0])
            messagebox.showinfo(message="Cuenta Editado", title="Editar")
        elif self.valor == 1:
            liro = insertRow(lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6])
            messagebox.showinfo(message="Cuenta nueva Insertada", title="Insertar")
        self.button_atras()

    def button_editar(self):
        self.valor = 0
        self.buttons_stdo(0)
        self.text_content.place_forget()
        self.widget_second_o()
        self.change_editar()
        self.entry_id_.config(state= "disabled")

    def button_atras(self):
        self.buttons_stdo(1)
        self.text_content.place(relx=0.10, rely=0.20, relwidth=0.80, relheight=0.70)
        self.widget_second_c()

    def change_editar(self):
        iniciar = buscador()
        dato = iniciar.buscar_por_select(self.entry_1.get())
        self.entry_id_.delete(0,END)
        self.entry_nombre.delete(0,END)
        self.entry_usuario_cuenta.delete(0,END)
        self.entry_contraseña.delete(0,END)
        self.entry_empresa.delete(0,END)
        self.entry_frase_secreta.delete(0,END)
        self.entry_descripcion.delete(0,END)
        self.entry_id_.insert(0,dato[0])
        self.entry_nombre.insert(0,dato[1])
        self.entry_usuario_cuenta.insert(0,dato[2])
        self.entry_contraseña.insert(0,dato[3])
        self.entry_empresa.insert(0,dato[4])
        self.entry_frase_secreta.insert(0,dato[5])
        self.entry_descripcion.insert(0,dato[6])

    def buttons_stdo(self, inte):
        lista =[DISABLED, NORMAL]
        self.buton_buscar_empresa['state'] = lista[inte]
        self.buton_buscar_id['state'] = lista[inte]
        self.buton_question['state'] = lista[inte]
        self.buton_añadir['state'] = lista[inte]
        self.buton_editar['state'] = lista[inte]
        self.buton_borrar['state'] = lista[inte]

    def button_question(self):
        lista = ["facebook", "gmail", "hotmail", "metamask", "ronin", "binance", "axie infinity", "none"]
        self.text_content.delete('1.0', END)
        for palabra in lista:
            self.text_content.insert(END, f'{palabra}\n')

    def button_por_id(self):
        iniciar = buscador()
        dato = iniciar.buscar_por_id(self.entry_1.get())
        self.text_content.delete('1.0', END)
        for palabra in dato:
            self.text_content.insert(END, f'{palabra}\n')

    def imprimir_por_empresa(self):
        if type(self.entry_1.get()) == str:
            iniciar = buscador()
            datos_por_empresa=iniciar.buscar_empresa(self.entry_1.get())
            self.text_content.delete('1.0', END)
            for palabras in datos_por_empresa:
                self.text_content.insert(END, palabras)
            #self.label_content.config(text=datos_por_empresa)
        else:
            messagebox.showinfo(message=f'Inserte  la empresa a buscar', title="Recordatorio")

    def acceder_a_cuenta(self):
        self.widget_login_c()
        self.widget_principal_o()
        #self.widget_second_o()
        
    def widget_second_o(self):
        self.entry_id_=Entry(self.ventana)
        self.entry_nombre=Entry(self.ventana)
        self.entry_usuario_cuenta=Entry(self.ventana)
        self.entry_contraseña=Entry(self.ventana)
        self.entry_empresa=Entry(self.ventana, text="lola flores")
        self.entry_frase_secreta=Entry(self.ventana)
        self.entry_descripcion=Entry(self.ventana)
        self.label_id=Label(self.ventana, text="ID \t\t:", anchor="w")
        self.label_nombre=Label(self.ventana, text="Nombres \t:", anchor="w") 
        self.label_usuario_cuenta=Label(self.ventana,text="Usario cuenta\t:", anchor="w")
        self.label_contraseña=Label(self.ventana,text="Contraseña\t:", anchor="w")
        self.label_empresa=Label(self.ventana,text="Empresa o Red\t:", anchor="w")
        self.label_frase_secreta=Label(self.ventana,text="Frase Secreta\t:", anchor="w")
        self.label_descripcion=Label(self.ventana,text="Descripción\t:", anchor="w")
        self.buton_cambiar=Button(self.ventana, text="Hacer cometido", cursor="hand1", bg=fonts.BACKGROUND, fg=fonts.FOREGROUND, command=self.button_aceptar)
        self.buton_retro=Button(self.ventana, text="Atrás", cursor="hand1", bg=fonts.BACKGROUND, fg=fonts.FOREGROUND, command=self.button_atras)
        self.entry_id_.place(relx=0.40, rely=0.20, relwidth=0.50, relheight=0.04)
        self.entry_nombre.place(relx=0.40, rely=0.25, relwidth=0.50, relheight=0.04)
        self.entry_usuario_cuenta.place(relx=0.40, rely=0.30, relwidth=0.50, relheight=0.04)
        self.entry_contraseña.place(relx=0.40, rely=0.35, relwidth=0.50, relheight=0.04)
        self.entry_empresa.place(relx=0.40, rely=0.40, relwidth=0.50, relheight=0.04)
        self.entry_frase_secreta.place(relx=0.40, rely=0.45, relwidth=0.50, relheight=0.04)
        self.entry_descripcion.place(relx=0.40, rely=0.50, relwidth=0.50, relheight=0.04)
        self.label_id.place(relx=0.10, rely=0.20, relwidth=0.30, relheight=0.04)
        self.label_nombre.place(relx=0.10, rely=0.25, relwidth=0.30, relheight=0.04)
        self.label_usuario_cuenta.place(relx=0.10, rely=0.30, relwidth=0.30, relheight=0.04)
        self.label_contraseña.place(relx=0.10, rely=0.35, relwidth=0.30, relheight=0.04)
        self.label_empresa.place(relx=0.10, rely=0.40, relwidth=0.30, relheight=0.04)
        self.label_frase_secreta.place(relx=0.10, rely=0.45, relwidth=0.30, relheight=0.04)
        self.label_descripcion.place(relx=0.10, rely=0.50, relwidth=0.30, relheight=0.04)
        self.buton_cambiar.place(relx=0.40, rely=0.55, relwidth=0.50, relheight=0.04)
        self.buton_retro.place(relx=0.40, rely=0.60, relwidth=0.50, relheight=0.04)

    def widget_second_c(self):
        self.entry_id_.place_forget()
        self.entry_nombre.place_forget()
        self.entry_usuario_cuenta.place_forget()
        self.entry_contraseña.place_forget()
        self.entry_empresa.place_forget()
        self.entry_frase_secreta.place_forget()
        self.entry_descripcion.place_forget()
        self.label_id.place_forget()
        self.label_nombre.place_forget()
        self.label_usuario_cuenta.place_forget()
        self.label_contraseña.place_forget()
        self.label_empresa.place_forget()
        self.label_frase_secreta.place_forget()
        self.label_descripcion.place_forget()
        self.buton_cambiar.place_forget()
        self.buton_retro.place_forget()

    def widget_principal_o(self):
        self.entry_1 = Entry(self.ventana, fg=fonts.FOREGROUND)
        self.buton_buscar_empresa = Button(self.ventana, text="Buscar Empr", cursor="hand1", bg=fonts.BACKGROUND, fg=fonts.FOREGROUND, command=self.imprimir_por_empresa)
        self.buton_buscar_id = Button(self.ventana, text="Por Id", cursor="hand1", bg=fonts.BACKGROUND, fg=fonts.FOREGROUND, command=self.button_por_id)
        self.buton_question = Button(self.ventana, text="Question", cursor="hand1", bg=fonts.BACKGROUND, fg=fonts.FOREGROUND, command=self.button_question)
        self.buton_añadir = Button(self.ventana, text="Añadir", cursor="hand1", bg=fonts.BACKGROUND, fg=fonts.FOREGROUND, command=self.button_añadir)
        self.buton_editar = Button(self.ventana, text="Editar", cursor="hand1", bg=fonts.BACKGROUND, fg=fonts.FOREGROUND, command=self.button_editar)
        self.buton_borrar = Button(self.ventana, text="Borrar", cursor="hand1", bg=fonts.BACKGROUND, fg=fonts.FOREGROUND, command=self.button_borrar)
        #self.buton_history = Button(self.ventana, text="History", cursor="hand1", bg=fonts.BACKGROUND, fg=fonts.FOREGROUND)
        #self.label_content = Label(self.ventana, text="El Contenido", bg=fonts.BACKGROUND, fg=fonts.FOREGROUND, anchor="nw")
        self.text_content = Text(self.ventana, height=2, width=40)
        self.entry_1.place(relx=0.10, rely=0.05, relwidth=0.30, relheight=0.04)
        self.buton_buscar_empresa.place(relx=0.45, rely=0.05, relwidth=0.20, relheight=0.04)
        self.buton_buscar_id.place(relx=0.45, rely=0.10, relwidth=0.20, relheight=0.04)
        self.buton_question.place(relx=0.70, rely=0.05, relwidth=0.20, relheight=0.04)
        self.buton_añadir.place(relx=0.70, rely=0.10, relwidth=0.20, relheight=0.04)
        self.buton_editar.place(relx=0.45, rely=0.15, relwidth=0.20, relheight=0.04)
        self.buton_borrar.place(relx=0.70, rely=0.15, relwidth=0.20, relheight=0.04)
        #self.buton_history.place(relx=0.45, rely=0.10, relwidth=0.20, relheight=0.04)
        #self.label_content.place(relx=0.10, rely=0.20, relwidth=0.80, relheight=0.70)
        self.text_content.place(relx=0.10, rely=0.20, relwidth=0.80, relheight=0.70)

    def widget_principal_c(self):
        self.entry_1.place_forget()
        self.buton_buscar_empresa.place_forget()
        self.buton_buscar_id.place_forget()
        self.buton_question.place_forget()
        self.buton_añadir.place_forget()
        self.buton_editar.place_forget()
        self.buton_borrar.place_forget()
        self.buton_history.place_forget()
        self.label_content.place_forget()

    def widget_login_o(self):
        self.label_usuario = Label(self.ventana, text="Cuentas Admisibles", anchor="w", fg=fonts.FOREGROUND)
        self.entry_usuario = Entry(self.ventana, bg=fonts.BACKGROUND, fg=fonts.FOREGROUND)
        self.entry_contraseña = Entry(self.ventana, bg=fonts.BACKGROUND, fg=fonts.FOREGROUND)
        self.label_nocuenta = Label(self.ventana, text="Olvidó su contraseña?", anchor="e", fg=fonts.FOREGROUND)
        self.login = Button(self.ventana, text="Accerder", cursor="hand1", bg=fonts.BACKGROUND, fg=fonts.FOREGROUND, command=self.acceder_a_cuenta)
        self.label_usuario.place(relx=0.30, rely=0.52, relwidth=0.4, relheight=0.05)
        self.entry_usuario.place(relx=0.30, rely=0.58, relwidth=0.4, relheight=0.05)
        self.entry_contraseña.place(relx=0.30, rely=0.65, relwidth=0.4, relheight=0.05)
        self.label_nocuenta.place(relx=0.30, rely=0.70, relwidth=0.4, relheight=0.05)
        self.login.place(relx=0.40, rely=0.76, relwidth=0.2, relheight=0.05)
    
    def widget_login_c(self):
        self.label_usuario.place_forget()
        self.entry_usuario.place_forget()
        self.entry_contraseña.place_forget()
        self.label_nocuenta.place_forget()
        self.login.place_forget()

def main():
    interfaz = InterfazTierPregunta()
    #interfaz.geometry('600x300')
    
if __name__ == "__main__":
    main()