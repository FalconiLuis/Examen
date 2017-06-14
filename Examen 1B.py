# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 11:17:57 2017

@author: 22B
"""

import turtle
from  tkinter import *

tk = Tk()


def figura_3_lados(altura):
    
    t = turtle.Pen()
    
    
    t.left(60)
    t.forward(altura)
    t.left(-120)
    t.forward(altura)
    t.left(-120)
    t.forward(altura)

def figura_4_lados(lados):
    
    t = turtle.Pen()
    
    t.left(90)
    t.forward(lados)
    t.left(90)
    t.forward(lados)
    t.left(90)
    t.forward(lados)
    t.left(90)
    t.forward(lados)
    
def figura_5_lados(largo): 
    
    t = turtle.Pen()
    
    t.forward (largo)
    t.right(60)
    t.forward(largo)
    t.right(60)
    t.forward(largo)
    t.right (60)
    t.forward(largo)
    t.right(60)
    t.forward(largo)
    t.right(60)
    t.forward(largo)
    

def area_figuras():
    
    print("AREAS DE FIGURAS GEOMÉTRICAS")
    n = int (input("Cuantos lados tiene la figura?: "))
    
    while((n == 3) or (n == 5) or (n == 4)):
    
        if (n == 3):
        
            b = int(input("Indique la Base del triangulo: "))
            h = int(input("Indique la altura del triangulo: "))
            print("Area del Triangulo: " , b*h/2) 
            if(h>=300):
                print("El altura del triangulo debe ser menor para poderlo dibujar")  
            else:
                figura_3_lados(h)
        
        
        elif(n == 4):
            a = int(input("Indique la altura del cuadrado: "))
            print("Area del Cuadrado: " , a**2 )
            if(a>=300):
                print("El altura del cuadrado debe ser menor para poderlo dibujar")  
            else:
                figura_4_lados(a)
            
        
        elif(n == 5):
            p = int(input("Indique el perimetro del pentagono: "))
            a = int(input("Indique la Apotema del pentagono: "))
            print("Area del Pentagono: " ,(p*a)/2)
            if(p>=300):
                print("El altura del pentagono debe ser menor para poderlo dibujar")  
            else:
                figura_5_lados(p)
            
        elif(n <=3 or n>=5):
            break
            print("La figura debe ser de 3,4 o 5 lados minimo")
            n = int (input("Cuantos lados tiene la figura?: ")) 
    
    
    
            
        
def perimetro_figuras():
    
    print("PERIMETRO DE FIGURAS GEOMÉTRICAS")
    
    n = int(input("Cuantos lados tiene la figura?: "))
    if (n == 3):
        
        l = int(input("Indique el lado 1 : "))
        l2 = int(input("Indique el lado 2 : "))
        l3 = int(input("Indique el lado 3 : "))
        
        print("Perimetro del Triangulo: " , l*l2*l3)
        if(l>=300):
                print("El altura del triangulo debe ser menor para poderlo dibujar")  
        else:
                figura_3_lados(l)
        
        
    elif(n == 4):
        lc = int(input("Indique el lado del cuadrado: "))
        print("Perimetro del Cuadrado: " , 4*lc ) 
        if(lc>=300):
                print("El altura del cuadrado debe ser menor para poderlo dibujar")  
        else:
                figura_4_lados(lc)
        
        
             
    elif(n == 5):
        
        lp = int(input("Indique el lado del pentagono: "))
        print("Area del Pentagono: ", 5*lp)
        if(lp>=300):
                print("El altura del pentagono debe ser menor para poderlo dibujar")  
        else:
                figura_5_lados(lp)
        
        
    elif(n <=3 or n>=5):
        print("La figura debe ser de 3,4 o 5 lados minimo")
        
    
tk.title("Examen primer Bimestre ")
tk.geometry("640x480")

ms1 = "Examen de Programación"
ms2 = "Elija una opcion: "

msg = Message(tk, text = ms1)
msg.config(font=('Andalus', 20, 'italic'))
msg.pack( )

msg2 = Message(tk, text = ms2)
msg2.config(font=('Andalus', 20, 'italic'))
msg2.pack( )


btn= Button(tk, text = "1",command = area_figuras, width = 10, height = 5, anchor = "nw")
btn2= Button(tk, text = "2",command = perimetro_figuras , width = 10, height = 5, anchor = "w")

btn.pack()
btn2.pack()

tk.mainloop()


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    

    

 
    