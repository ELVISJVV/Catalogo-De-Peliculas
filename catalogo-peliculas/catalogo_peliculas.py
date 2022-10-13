import tkinter as tk
from client.gui_app import Frame, barra_menu

def main():
    root = tk.Tk()
    root.title('Catalogo de Peliculas')
    root.iconbitmap('A:\Programas de Python\Cursos Udemy\Escuela de Programación y Desarrollo Web desde cero a Master\catalogo-peliculas\catalogo-peliculas\img\cp-logo.ico')
    #root.geometry('900x500')
    root.resizable(0,0)
    barra_menu(root)
    
    app = Frame(root = root)
    
    app.mainloop()

if __name__ == '__main__':
    main()  