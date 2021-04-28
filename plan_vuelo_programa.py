from tkinter import *
from tkinter import messagebox as ms 
import os.path

ventana = Tk()
ventana.geometry("700x700")
ventana.title("Plan de vuelo actividad 2") 
ventana.config(bg="green")  
#mensaje 
logo = Label(ventana,text="Alumno: Samuel Martinez") 
logo.grid(row=1,column=0,sticky=W,columnspan=2)
logo.configure(bg="white",fg="black") 
#etiqueta Distancia_focal 
logo2 = Label(ventana,text="Altura vuelo(m)")
logo2.grid(row=2,column=0,sticky=W) 
logo2.configure(bg="black",fg="white") 
#entrada Distancia_focal 
entrada1 = Entry(ventana)
entrada1.grid(row=3,column=0,sticky=W) 
entrada1.configure(bg="black",fg="white")  
#etiqueta Distancia_focal 
logo4 = Label(ventana,text="Distancia focal(mm)")
logo4.grid(row=2,column=1,sticky=NW)  
logo4.configure(bg="black",fg="white")  
#entrada ancho_sensor 
entrada2 = Entry(ventana)
entrada2.grid(row=3,column=1,sticky=W)
entrada2.configure(bg="black",fg="white")  
#etiqueta ancho_sensor
logo5 = Label(ventana,text="Ancho Sensor (mm)") 
logo5.grid(row=6,column=0,sticky=W)  
logo5.configure(bg="black",fg="white")  
#entrada Alto_sensor  
entrada3 = Entry(ventana) 
entrada3.grid(row=7,column=0,sticky=W) 
entrada3.configure(bg="black",fg="white")  
#etiqueta alto_imagen 
logo6 = Label(ventana,text="Alto imagen (pixel)")  
logo6.grid(row=6,column=1,sticky=W)  
logo6.configure(bg="black",fg="white")  
#entrada alto_imagen 
entrada4 = Entry(ventana) 
entrada4.grid(row=7,column=1,sticky=W)  
entrada4.configure(bg="black",fg="white")  
#etiqueta Alto_sensor  
logo7 = Label(ventana,text="Alto sensor (mm)")  
logo7.grid(row=10,column=0,sticky=W)  
logo7.configure(bg="black",fg="white")  
#entrada Alto_sensor 
entrada5 = Entry(ventana) 
entrada5.grid(row=11,column=0,sticky=W)  
entrada5.configure(bg="black",fg="white")  
#etiqueta altura_vuelo  
logo8 = Label(ventana,text="Ancho de la imagen (pixel)")  
logo8.grid(row=10,column=1,sticky=W)  
logo8.configure(bg="black",fg="white")  
#entrada altura_vuelo 
entrada6 = Entry(ventana) 
entrada6.grid(row=11,column=1,sticky=W)  
entrada6.configure(bg="black",fg="white")  
#etiqueta solape_longitudinal 
logo9 = Label(ventana,text="solape longitudinal  (%)")  
logo9.grid(row=12,column=0,sticky=W)  
logo9.configure(bg="black",fg="white")  
#entrada solape_longitudinal 
entrada7 = Entry(ventana) 
entrada7.grid(row=13,column=0,sticky=W)  
entrada7.configure(bg="black",fg="white")  
#etiqueta solpae_transversal 
logo10 = Label(ventana,text="solape transversal  (%)")  
logo10.grid(row=12,column=1,sticky=W) 
logo10.configure(bg="black",fg="white")  
#etiqueta solape_transversal 
entrada8 = Entry(ventana) 
entrada8.grid(row=13,column=1,sticky=W)  
entrada8.configure(bg="black",fg="white")  
#etiqueta largo_parcela 
logo11 = Label(ventana,text="Largo de parcela (m)")  
logo11.grid(row=14,column=0,sticky=W)  
logo11.configure(bg="black",fg="white")  
#entrada largo_parcela 
entrada9 = Entry(ventana) 
entrada9.grid(row=15,column=0,sticky=W)   
entrada9.configure(bg="black",fg="white")   
#etiqueta ancho_parcela
logo12 = Label(ventana,text="Ancho de parcela (m)")  
logo12.grid(row=14,column=1,sticky=W)    
logo12.configure(bg="black",fg="white")  
# entrada ancho_parcela
entrada10 = Entry(ventana) 
entrada10.grid(row=15,column=1,sticky=W)  
entrada10.configure(bg="black",fg="white")  
#velocidad_vuelo
logo13 = Label(ventana,text="velocidad de vuelo (m/s)")  
logo13.grid(row=16,column=0,sticky=W)   
logo13.configure(bg="black",fg="white")  
#entrada RSI
entrada11 = Entry(ventana) 
entrada11.grid(row=17,column=0,sticky=W) 
entrada11.configure(bg="black",fg="white")    
#RSI 
logo14 = Label(ventana,text="RSI diferencia de valor ")
logo14.grid(row=16,column=1,sticky=W) 
logo14.configure(bg="black",fg="white")  
#entrada RSI 
entrada12 = Entry(ventana)
entrada12.grid(row=17,column=1,sticky=W)
entrada12.configure(bg="black",fg="white")  
#funcion de calculo de datos 
def operaciones_generadas():
    global entrada1 , entrada2,entrada3,entrada4,entrada5,entrada6,entrada7,entrada8,entrada9,entrada10,entrada11,entrada12
    #GMS 
    texto.delete(1.0, END)
    altura_vuelo = int(entrada1.get()) 
    Distancia_focal = float(entrada2.get()) 
    RSI = entrada12 = float(entrada12.get())
    GMS_operacion = f"{round((altura_vuelo*100/Distancia_focal)*RSI,2)}"
    GMS = f"GMS resolución en terreno: {GMS_operacion} pixel" 
    texto.insert(END,GMS) 
    #Escala de vuelo  
    texto.delete(2.0,END)
    escala_vuelo = 1/((Distancia_focal/1000)/altura_vuelo)
    Escala_de_vuelo = f"{round(1/((Distancia_focal/1000)/altura_vuelo))} m" 
    Esv = f"\n La escala de vuelo es: {Escala_de_vuelo} "
    texto.insert(END,Esv)  
    #Ancho de la imagen sobre el terreno (m): 
    texto.delete(3.0,END) 
    ancho_sensor = float(entrada3.get())
    ancho_img_terreno = (ancho_sensor*escala_vuelo)/1000
    ancho_de_imagen_terreno = f"{(round(ancho_sensor*escala_vuelo)/1000)}" 
    ait = f"\n Ancho de la imagen sobre el terreno (m): {ancho_de_imagen_terreno} m" 
    texto.insert(END,ait)  
    #Alto de la imagen sobre el terreno (m):
    texto.delete(4.0,END)
    Alto_sensor = float(entrada5.get()) 
    alto_de_imagen = (Alto_sensor*escala_vuelo)/1000 
    alto_de_imagen_text = f"{round((Alto_sensor*escala_vuelo)/1000)}"
    adi = f"\n Alto de la imagen sobre el terreno (m) : {alto_de_imagen_text} m "
    texto.insert(END,adi)
    #Base aérea (m):
    texto.delete(5.0,END) 
    solape_longitudinal = int(entrada7.get())
    Base_area = ancho_img_terreno*(1-(solape_longitudinal/100)) 
    Base_area_text = f"{round(ancho_img_terreno*(1-(solape_longitudinal/100)))}"
    Ba = f"\n Base area (m): {Base_area_text} m"
    texto.insert(END,Ba) 
    # Distancia entre pasadas (m) 
    texto.delete(6.0, END)
    solape_transversal = int(entrada8.get()) 
    distancia_pasadas = alto_de_imagen * (1-(solape_transversal/100)) 
    distancia_pasadas_text = f"{round(alto_de_imagen * (1-(solape_transversal/100)))}"
    dpt = f"\n Distancia entre pasadas (m): {distancia_pasadas_text}" 
    texto.insert(END,dpt) 
    #Número de pasadas:  
    texto.delete(7.0,END)
    ancho_parcela = int(entrada10.get())
    numero_pasadas = ancho_parcela / distancia_pasadas 
    numero_pasadas_text = f"{round(ancho_parcela / distancia_pasadas)}"
    npt = f"\n Numero de pasadas del drone: {numero_pasadas_text}"
    texto.insert(END,npt)  
    #Número de fotos por pasada: 
    texto.delete(8.0,END)
    largo_parcela = int(entrada9.get())
    n_fotos_por_pasadas = (largo_parcela / Base_area) + 1 
    n_fotos_por_pasadas_text = f"{round(n_fotos_por_pasadas)}"
    nfpt = f"\n Numero de fotos por pasada: {n_fotos_por_pasadas_text}"
    texto.insert(END,nfpt) 
    #Número de fotos  
    texto.delete(9.0,END)
    numero_de_fotos_vuelo = n_fotos_por_pasadas * numero_pasadas 
    numero_de_fotos_vuelo_text = f"{round(numero_de_fotos_vuelo)}" 
    nfvt = f"\n Numero de fotos que tomara el drone: {numero_de_fotos_vuelo_text}"
    texto.insert(END,nfvt) 
    #Distancia de vuelo (m)  
    texto.delete(10.0,END)
    dv = (numero_pasadas*largo_parcela) + ancho_parcela 
    dvtext = f"{round(dv)}" 
    dvt = f"\n Distancia de vuelo del drone: {dvtext} m" 
    texto.insert(END,dvt)  
    #intervalo entre fotos  
    texto.delete(11.0,END)
    velocidad_vuelo = int(entrada11.get())
    intervalo_fotos = Base_area / velocidad_vuelo
    intervalo_fotos_text = f"{round(intervalo_fotos,2)}"
    ift = f"\n Intervalo entre fotos: {intervalo_fotos_text} segundos" 
    texto.insert(END,ift)
    # Duración del vuelo (min)  
    texto.delete(12.0,END)
    duracion = (numero_de_fotos_vuelo * intervalo_fotos)/60 
    duracion_text = f"{round(duracion,2)}"
    dt = f"\n Duracion del vuelo del drone: {duracion_text} min"
    texto.insert(END,dt)  
#comando calcular 
comando = Button(ventana,text="Calcular parametros",command=operaciones_generadas) 
comando.grid(row=24,column=0) 
#texto de dialogo 
texto = Text(ventana,width=50,height=18,font=("Arial",10))
texto.grid(row=25,column=0,sticky=N) 

ventana.mainloop()
filtro_poner = 1.57E-2
