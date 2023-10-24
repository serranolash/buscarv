import tkinter as tk
from tkinter import filedialog
import pandas as pd

# Función para cargar el primer archivo Excel
def cargar_primer_archivo():
    archivo = filedialog.askopenfilename()
    primer_archivo_entry.delete(0, tk.END)
    primer_archivo_entry.insert(0, archivo)

# Función para cargar el segundo archivo Excel
def cargar_segundo_archivo():
    archivo = filedialog.askopenfilename()
    segundo_archivo_entry.delete(0, tk.END)
    segundo_archivo_entry.insert(0, archivo)

# Función para comparar los archivos de forma flexible
def comparar_archivos():
    primer_archivo = primer_archivo_entry.get()
    segundo_archivo = segundo_archivo_entry.get()
    
    if primer_archivo and segundo_archivo:
        df1 = pd.read_excel(primer_archivo)
        df2 = pd.read_excel(segundo_archivo)
        
        nombres_posibles = ['codigo', 'ARTCOD', 'Articulo', 'CODIGO', 'ArtCod']  # Lista de nombres posibles
        
        # Función para renombrar las columnas en df1
        def renombrar_columnas(dataframe, nombres_posibles):
            for nombre in nombres_posibles:
                if nombre in dataframe.columns:
                    dataframe.rename(columns={nombre: 'codigo_comun'}, inplace=True)
                    return True
            return False
        
        # Buscar y renombrar columnas en df1
        if not renombrar_columnas(df1, nombres_posibles):
            resultado_label.config(text='No se encontraron columnas con nombres posibles en el primer archivo.')
            return
        
        # Buscar y renombrar columnas en df2
        if not renombrar_columnas(df2, nombres_posibles):
            resultado_label.config(text='No se encontraron columnas con nombres posibles en el segundo archivo.')
            return

        # Realizar la comparación utilizando el nombre de columna común
        resultados = pd.merge(df1, df2, how='inner', on='codigo_comun')
        print(resultados)  # Imprimir los resultados en la consola

        
        # Guardar los resultados en un archivo Excel
        resultados.to_excel('resultados.xlsx', index=False)
        resultado_label.config(text='Comparación completada. Resultados guardados en resultados.xlsx')
    else:
        resultado_label.config(text='Cargue ambos archivos antes de comparar.')


# Configuración de la ventana de la aplicación
app = tk.Tk()
app.title('Comparación de Archivos Excel')
# Establece el tamaño de la ventana en píxeles
app.geometry("600x600")  # Ajusta el ancho y alto según tus preferencias

# Cargar una imagen de fondo
background_image = tk.PhotoImage(file="logo.png")

# Configurar el fondo de la ventana con la imagen
background_label = tk.Label(app, image=background_image)
background_label.place(relwidth=1, relheight=1)

primer_archivo_label = tk.Label(app, text='Primer Archivo Excel:')
primer_archivo_label.pack()
primer_archivo_entry = tk.Entry(app)
primer_archivo_entry.pack()
cargar_primer_archivo_button = tk.Button(app, text='Cargar Primer Archivo', command=cargar_primer_archivo)
cargar_primer_archivo_button.pack()

segundo_archivo_label = tk.Label(app, text='Segundo Archivo Excel:')
segundo_archivo_label.pack()
segundo_archivo_entry = tk.Entry(app)
segundo_archivo_entry.pack()
cargar_segundo_archivo_button = tk.Button(app, text='Cargar Segundo Archivo', command=cargar_segundo_archivo)
cargar_segundo_archivo_button.pack()

comparar_button = tk.Button(app, text='Comparar Archivos', command=comparar_archivos)
comparar_button.pack()

resultado_label = tk.Label(app, text='')
resultado_label.pack()

app.mainloop()
