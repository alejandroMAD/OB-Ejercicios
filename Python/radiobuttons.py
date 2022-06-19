import tkinter
from tkinter import ttk


def main():
    window = tkinter.Tk()
    window.title('Elige tu lenguaje favorito')  # Nombre de la ventana
    window.resizable(True, True)  # Usuario puede redimensionar
    window.geometry("300x400")  # Tamaño inicial de la ventana

    diccionario_lenguajes = {
        'java': 'Lenguaje orientado a objetos, de propósito general, tipado y de sintaxis clara',
        'python': 'Lenguaje POO de muy alto nivel y sintaxis muy concisa, fuerte en Data Science',
        'javascript': 'Lenguaje orientado a dinamizar páginas web directamente interpretable por browsers',
        'c++': 'Lenguaje multiparadigma que extendió el lenguaje C permitiendo manipular objetos',
        'ruby': 'Lenguaje de programación orientado a objetos con una sintaxis muy atractiva',
        'php': 'Lenguaje especialmente utilizado en el desarrollo web y de servidores back-end'
    }

    seleccion = tkinter.StringVar()

    def set_descripcion():
        area_descripcion.delete(1.0, "end")
        area_descripcion.insert(1.0, diccionario_lenguajes[seleccion.get()])

    def clear_descripcion():
        area_descripcion.delete(1.0, "end")
        seleccion.set(None)  # Resetea el StringVar

    def salir():
        window.quit()

    label_pregunta = ttk.Label(text='¿Cuál es tu lenguaje de programación favorito?')
    radiobutton1 = ttk.Radiobutton(
        window, text='Java', value='java', variable=seleccion, command=set_descripcion)
    radiobutton2 = ttk.Radiobutton(
        window, text='Python', value='python', variable=seleccion, command=set_descripcion)
    radiobutton3 = ttk.Radiobutton(
        window, text='JavaScript', value='javascript', variable=seleccion, command=set_descripcion)
    radiobutton4 = ttk.Radiobutton(
        window, text='C++', value='c++', variable=seleccion, command=set_descripcion)
    radiobutton5 = ttk.Radiobutton(
        window, text='Ruby', value='ruby', variable=seleccion, command=set_descripcion)
    radiobutton6 = ttk.Radiobutton(
        window, text='PHP', value='php', variable=seleccion, command=set_descripcion)
    area_descripcion = tkinter.Text(
        window, height=4, width=34, wrap='word')
    boton_reinicio = tkinter.Button(
        window, text='Reiniciar', width=18, command=clear_descripcion)
    boton_salir = tkinter.Button(
        window, text='Salir', width=18, command=salir)

    label_pregunta.pack(pady=10)
    radiobutton1.pack(fill='x', padx=30, pady=6)
    radiobutton2.pack(fill='x', padx=30, pady=6)
    radiobutton3.pack(fill='x', padx=30, pady=6)
    radiobutton4.pack(fill='x', padx=30, pady=6)
    radiobutton5.pack(fill='x', padx=30, pady=6)
    radiobutton6.pack(fill='x', padx=30, pady=6)
    area_descripcion.pack(padx=10, pady=6)
    boton_reinicio.pack(padx=10, pady=6)
    boton_salir.pack(padx=10, pady=6)

    window.mainloop()


if __name__ == "__main__":
    main()
