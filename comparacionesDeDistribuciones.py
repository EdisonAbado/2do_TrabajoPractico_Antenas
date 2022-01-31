# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 11:38:15 2022

@author: edyab
"""
import matplotlib.pyplot as graf

#G binómica para L/2
x1=[3   , 5   , 7   , 9   ]
y1=[7.43, 8.93, 9.93, 10.5]

#G triangular para L/2
x1=[3   , 5   , 7   , 9   ]
y2=[7.43, 9.65, 11.10, 8.99]

#G uniforme para L/2
x1=[3   , 5   , 7   , 9   ]
y3=[7.84, 10.20, 10.09, 12.90]

#G binómica para L/4
x1=[3   , 5   , 7   , 9   ]
y4=[4.11, 5.39, 6.39, 7.12]

#G triangular para L/4
x1=[3   , 5   , 7   , 9   ]
y5=[4.11, 6.29, 7.85, 11.90]

#G uniforme para L/4
x1=[3   , 5   , 7   , 9   ]
y6=[4.81, 7.52, 8.80, 10.00]

graf.plot(x1, y1, 'b', label='Distribución binómica para $d=\lambda/2$')
graf.plot(x1, y1, 'bo')
graf.plot(x1, y2, 'g', label='Distribución triangular para $d=\lambda/2$')
graf.plot(x1, y2, 'go')
graf.plot(x1, y3, 'r', label='Distribución uniforme para $d=\lambda/2$')
graf.plot(x1, y3, 'ro')
graf.plot(x1, y4, 'c', label='Distribución binómica para $d=\lambda/4$')
graf.plot(x1, y4, 'cs')
graf.plot(x1, y5, 'm', label='Distribución triangular para $d=\lambda/4$')
graf.plot(x1, y5, 'ms')
graf.plot(x1, y6, 'y', label='Distribución uniforme para $d=\lambda/4$')
graf.plot(x1, y6, 'ys')
graf.xlabel(r'Número de elementos del arreglo $N$')
graf.ylabel(r'Ganancia en $dBi$')
graf.title("Comparación de Ganancias para $H=\lambda /2$")
graf.legend(loc=2)
graf.grid(True)
graf.show()

