import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

f = open('C:\\Users\\dav\\statistik\\daten4pdPractice.txt', 'r')
messystuff = f.read()
isitcool = messystuff.replace('-', '')
messystuff = isitcool.replace('==', '')
messystuff = messystuff.replace('Tagesstatistik / Benutzung vom ', '')
messystuff = messystuff.replace('apnum Anz. Exe Anz. Benutzer ', '')
messystuff = messystuff.replace('Anzahl der Nutzenden bei AusleihvorgÃ¤ngen pro Serviceplatz', '')
messystuff = messystuff.replace(' ', 'x')
messystuff = messystuff.replace('xx', 'xz')
messystuff = messystuff.replace('xxx', 'xyz')
messystuff = messystuff.replace('xxxx', 'xyzo')
messystuff = messystuff.replace('xxxxx', 'xyzop')
messystuff = messystuff.replace('x', ',')
messystuff = messystuff.replace('z', ',')
messystuff = messystuff.replace(',,', ',')
messystuff = messystuff.replace(',,', ',')
messystuff = messystuff.replace(',,', ',')
messystuff = messystuff.replace(',,', ',')
justTable1 = list(messystuff[16:260])
df = []
for element in justTable1:
    try:
        df.append(int(element))
    except:
        df.append(element)
print(df)