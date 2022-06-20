import tkinter
from tkinter import ANCHOR

window = tkinter.Tk()
window.title('Práctica GUIs')
window.resizable(True, True)
window.geometry("275x275")

lista = ['Litio', 'Sodio', 'Potasio', 'Rubidio', 'Cesio', 'Francio']


def eliminar():
    listbox.delete(ANCHOR)


label_titulo = tkinter.Label(window, text="Metales alcalinos:")
listbox = tkinter.Listbox(window)
boton_eliminar = tkinter.Button(window, text='Eliminar', command=eliminar)

for elemento in lista:
    listbox.insert(tkinter.END, elemento)

label_titulo.pack(pady=8)
listbox.pack(pady=8)
boton_eliminar.pack(pady=8)

window.mainloop()
