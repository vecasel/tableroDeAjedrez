import tkinter as tk

# Crear una ventana de tkinter
root = tk.Tk()

# Crear un lienzo en la ventana con las dimensiones deseadas
canvas = tk.Canvas(root, width=400, height=400)

# Dibujar las casillas del tablero con un bucle for anidado
# El rango de la variable 'i' es de 0 a 8 para cubrir 8 filas
# El rango de la variable 'j' es de 0 a 8 para cubrir 8 columnas
for i in range(8):
    for j in range(8):
        # Calcular las coordenadas del rectángulo actual basándose en la fila y la columna
        x1 = j * 50
        y1 = i * 50
        x2 = x1 + 50
        y2 = y1 + 50
        # Si la suma de i y j es impar, el rectángulo es negro, de lo contrario, es blanco
        if (i + j) % 2 == 0:
            canvas.create_rectangle(x1, y1, x2, y2, fill="white")
        else:
            canvas.create_rectangle(x1, y1, x2, y2, fill="black")

# Agregar el lienzo a la ventana
canvas.pack()

# Iniciar el bucle de eventos de tkinter
root.mainloop()


