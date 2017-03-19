"""
Implementacion del Algoritmo de Daniel Nieto v4
Programado por Jose Contreras


"""

import copy
import sys

class Simp(object):
  def __init__(self):
    self.TYPE=""
    self.TEXT=""
    self.COMP=[]
  def agregarTYPE(self,Type):
    self.TYPE=Type
  def agregarTEXT(self,text):
    self.TEXT=text
  def agregarCOMP(self,comp):
    self.COMP.append(comp)

class Frase(object):
  def __init__(self):
    self.TYPE=""
    self.TEXT=""
    self.POS=""
    self.TREE=""
    self.SIMP=[]
  def agregarTYPE(self,Type):
    self.TYPE=Type
  def agregarTEXT(self,text):
    self.TEXT=text
  def agregarPOS(self,Pos):
    self.POS=Pos
  def agregarTREE(self,Tree):
    self.TREE=Tree
  def agregarSIMP(self):
    self.SIMP.append(Simp())

class Sentence(object):
  def __init__(self):
    self.TEXT=""
    self.TREE=""
    self.SIMP=[]
  def agregarTEXT(self,text):
    self.TEXT=text
  def agregarTREE(self,Tree):
    self.TREE=Tree
  def agregarSIMP(self):
    self.SIMP.append(Simp())


 
MEMORIAB=[]
MEMORIAA=[]


#----lectura de datos desde archivo
arch=(sys.argv[1])
f = open(arch)
dato = f.read().splitlines()
f.close

frase=Frase() 

for i in range(len(dato)):
  if 'TYPE: ' in dato[i][0:6]:
    frase.agregarTYPE(dato[i][6:])
  elif 'TEXT: ' in dato[i][0:6]:
    frase.agregarTEXT(dato[i][6:])
  elif 'POS : ' in dato[i][0:6]:
    frase.agregarPOS(dato[i][6:])
  elif 'TREE: ' in dato[i][0:6]:
    frase.agregarTREE(dato[i][6:])
  elif 'SIMP:' in dato[i]:
    frase.agregarSIMP()
  elif '  TYPE: ' in dato[i][0:8]:
    frase.SIMP[-1].agregarTYPE(dato[i][8:])
  elif '  TEXT: ' in dato[i][0:8]:
    frase.SIMP[-1].agregarTEXT(dato[i][8:])
  elif '  COMP: ' in dato[i]:
    frase.SIMP[-1].agregarCOMP(dato[i][8:])
#------------


#-------Programa principal

#Algoritmo v4


if ((frase.TYPE.find('sentence')) !=- 1) and (frase.SIMP!=[]) and (frase.SIMP[0].TYPE != ''):
  y=1
  w=1
  ordenSIMP=[]
  Sentence1=Sentence()
  Sentence1.TREE=copy.deepcopy(frase.TREE)
  Sentence1.TEXT=copy.deepcopy(frase.TEXT)
  for i in range(len(frase.SIMP)):
    Sentence1.SIMP.append(Simp())
    Sentence1.SIMP[i]=copy.deepcopy(frase.SIMP[i])
    ordenSIMP.append([])
  MEMORIAB.append(Sentence())
  for i in range(len(frase.SIMP)):
    ordenSIMP[i].append(i)
    ordenSIMP[i].append((int)(Sentence1.SIMP[i].TYPE[Sentence1.SIMP[i].TYPE.find('[')+1:Sentence1.SIMP[i].TYPE.find('..')]))
    ordenSIMP[i].append((int)(Sentence1.SIMP[i].TYPE[Sentence1.SIMP[i].TYPE.find('..')+2:Sentence1.SIMP[i].TYPE.find(']')]))
  tmpOrden=Simp()
  tmpOrdenSIMP=[]
#version anterior del orden en algV4_06.py
  b=len(Sentence1.SIMP)
  for j in range(len(Sentence1.SIMP)-1):
    for k in range(len(Sentence1.SIMP)-1-j):
      if (ordenSIMP[k+1+j][1]<ordenSIMP[j][1]):
          Sentence1.SIMP.insert(j,Sentence1.SIMP[k+1+j])
          ordenSIMP.insert(j,ordenSIMP[k+1+j])
          Sentence1.SIMP.pop(k+2+j)
          ordenSIMP.pop(k+2+j)        

#--cambio de orden de linea con respecto al algoritmo
  MEMORIAB.append(Sentence())
  MEMORIAB[0]=copy.deepcopy(Sentence1)
  numSimp=len(Sentence1.SIMP)

  DSIMP=0
  if 'noun or noun phrase coordination' in Sentence1.SIMP[0].TYPE and 'noun or noun phrase coordination' in Sentence1.SIMP[1].TYPE:
    DSIMP=1
#--
  while y<=numSimp:
    for x in range(len(MEMORIAB)):
      if Sentence1.SIMP[y-1].TEXT in MEMORIAB[x].TEXT:
        MEMORIAA.append(Sentence())
        MEMORIAA[-1]=copy.deepcopy(MEMORIAB[x])
        xTemp=Sentence()#----
        xTemp=copy.deepcopy(MEMORIAB[x])#----
        MEMORIAB.pop(x)
        #5.1
        if 'verb or verb phrase coordination' in Sentence1.SIMP[y-1].TYPE:
          ii=0 #ii equivale a i en el algoritmo
          for i in range(len(Sentence1.SIMP[y-1].COMP)):#y-1 -> python comienza indice en 0
            if ('conjunct' in Sentence1.SIMP[y-1].COMP[i]) and (not('conjunction' in Sentence1.SIMP[y-1].COMP[i])):
              ii=ii+1
          TEMPORAL=[]
          for i in range(ii):
            TEMPORAL.append(Sentence())
          p=ii
          q=1
          r=1
          while p>0:
            if ('conjunct' in Sentence1.SIMP[y-1].COMP[q-1]) and (not('conjunction' in Sentence1.SIMP[y-1].COMP[q-1])):#q-1 -> python comienza indice en 0
              TEMPORAL[r-1]=copy.deepcopy(xTemp)#----
              cad1=TEMPORAL[r-1].SIMP[y-1].TEXT
              indice1= (int)(TEMPORAL[r-1].SIMP[y-1].COMP[q-1][TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find('[')+1:TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find('..')])
              indice2= (int)(TEMPORAL[r-1].SIMP[y-1].COMP[q-1][TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find('..')+2:TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find(']')])
              cad2=Sentence1.TEXT[indice1:indice2]#----
              TEMPORAL[r-1].TEXT=TEMPORAL[r-1].TEXT.replace(cad1,cad2)
              p=p-1
              r=r+1
            q=q+1
          for i in range(len(TEMPORAL)):
            MEMORIAB.append(Sentence())
            MEMORIAB[-1]=copy.deepcopy(TEMPORAL[i])
        #5.2
        if 'noun or noun phrase coordination' in Sentence1.SIMP[y-1].TYPE:
          ii=0 #ii equivale a i en el algoritmo
          for i in range(len(Sentence1.SIMP[y-1].COMP)):#y-1 -> python comienza indice en 0
            if ('conjunct' in Sentence1.SIMP[y-1].COMP[i]) and (not('conjunction' in Sentence1.SIMP[y-1].COMP[i])):
              ii=ii+1
          TEMPORAL=[]
          for i in range(ii):
            TEMPORAL.append(Sentence())
          p=ii
          q=1
          r=1
          while p>0:
            if ('conjunct' in Sentence1.SIMP[y-1].COMP[q-1]) and (not('conjunction' in Sentence1.SIMP[y-1].COMP[q-1])):#q-1 -> python comienza indice en 0
              TEMPORAL[r-1]=copy.deepcopy(xTemp)#----
              cad1=TEMPORAL[r-1].SIMP[y-1].TEXT
              indice1= (int)(TEMPORAL[r-1].SIMP[y-1].COMP[q-1][TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find('[')+1:TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find('..')])
              indice2= (int)(TEMPORAL[r-1].SIMP[y-1].COMP[q-1][TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find('..')+2:TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find(']')])
              cad2=Sentence1.TEXT[indice1:indice2]#----
              TEMPORAL[r-1].TEXT=TEMPORAL[r-1].TEXT.replace(cad1,cad2)
              p=p-1
              r=r+1
            q=q+1
          for i in range(len(TEMPORAL)):
            MEMORIAB.append(Sentence())
            MEMORIAB[-1]=copy.deepcopy(TEMPORAL[i])
        #5.3
        if 'sentence coordination' in Sentence1.SIMP[y-1].TYPE:
          ii=0 #ii equivale a i en el algoritmo
          for i in range(len(Sentence1.SIMP[y-1].COMP)):#y-1 -> python comienza indice en 0
            if ('conjunct' in Sentence1.SIMP[y-1].COMP[i]) and (not('conjunction' in Sentence1.SIMP[y-1].COMP[i])):
              ii=ii+1
          TEMPORAL=[]
          for i in range(ii):
            TEMPORAL.append(Sentence())
          p=ii
          q=1
          r=1
          while p>0:
            if ('conjunct' in Sentence1.SIMP[y-1].COMP[q-1]) and (not('conjunction' in Sentence1.SIMP[y-1].COMP[q-1])):#q-1 -> python comienza indice en 0
              TEMPORAL[r-1]=copy.deepcopy(xTemp)#----

              cad1=TEMPORAL[r-1].SIMP[y-1].TEXT
              indice1= (int)(TEMPORAL[r-1].SIMP[y-1].COMP[q-1][TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find('[')+1:TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find('..')])
              indice2= (int)(TEMPORAL[r-1].SIMP[y-1].COMP[q-1][TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find('..')+2:TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find(']')])
              cad2=Sentence1.TEXT[indice1:indice2]#----           
              TEMPORAL[r-1].TEXT=TEMPORAL[r-1].TEXT.replace(cad1,cad2)

              p=p-1
              r=r+1
            q=q+1
          for i in range(len(TEMPORAL)):
            MEMORIAB.append(Sentence())
            MEMORIAB[-1]=copy.deepcopy(TEMPORAL[i])
        #5.4
        if 'parenthesis' in Sentence1.SIMP[y-1].TYPE:
          TEMPORAL=[]
          TEMPORAL.append(Sentence())
          TEMPORAL.append(Sentence())
          p=2
          q=1
          r=1
          while p>0:
            TEMPORAL[r-1]=copy.deepcopy(xTemp)#----
            cad1=TEMPORAL[r-1].SIMP[y-1].TEXT+')'
            indice1= (int)(TEMPORAL[r-1].SIMP[y-1].COMP[q-1][TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find('[')+1:TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find('..')])
            indice2= (int)(TEMPORAL[r-1].SIMP[y-1].COMP[q-1][TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find('..')+2:TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find(']')])
            cad2=Sentence1.TEXT[indice1:indice2]#----
            TEMPORAL[r-1].TEXT=TEMPORAL[r-1].TEXT.replace(cad1,cad2)
            q=q+1#falto poner este incremento en el algoritmo, se necesita agregar
            p=p-1
            r=r+1
          for i in range(len(TEMPORAL)):
            MEMORIAB.append(Sentence())
            MEMORIAB[-1]=copy.deepcopy(TEMPORAL[i])
        #5.5
        if 'full relative clause' in Sentence1.SIMP[y-1].TYPE:
          TEMPORAL=[]
          TEMPORAL.append(Sentence())
          TEMPORAL.append(Sentence())
          p=2
          q=1
          r=1
          while p>0:
            if 'referred noun phrase' in Sentence1.SIMP[y-1].COMP[q-1]:
              TEMPORAL[r-1]=copy.deepcopy(xTemp)

              if Sentence1.TEXT[Sentence1.TEXT.index(TEMPORAL[r-1].SIMP[y-1].TEXT)+len(TEMPORAL[r-1].SIMP[y-1].TEXT)-1]==',':
                cad1=TEMPORAL[r-1].SIMP[y-1].TEXT+','
              else:
                cad1=TEMPORAL[r-1].SIMP[y-1].TEXT

              indice1= (int)(TEMPORAL[r-1].SIMP[y-1].COMP[q-1][TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find('[')+1:TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find('..')])
              indice2= (int)(TEMPORAL[r-1].SIMP[y-1].COMP[q-1][TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find('..')+2:TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find(']')])


              cad2=Sentence1.TEXT[indice1:indice2]
              TEMPORAL[r-1].TEXT=TEMPORAL[r-1].TEXT.replace(cad1,cad2)
              indice3=indice1
              indice4=indice2
            if 'clause' in Sentence1.SIMP[y-1].COMP[q-1]:
              TEMPORAL[r-1]=copy.deepcopy(xTemp)

              indice1= (int)(TEMPORAL[r-1].SIMP[y-1].COMP[q-1][TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find('[')+1:TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find('..')])
              indice2= (int)(TEMPORAL[r-1].SIMP[y-1].COMP[q-1][TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find('..')+2:TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find(']')])

              TEMPORAL[r-1].TEXT=copy.deepcopy(Sentence1.TEXT[indice3:indice4]+' '+Sentence1.TEXT[indice1:indice2])
              cad3=Sentence1.TEXT[indice1:indice2]

              cad4=cad3.split()
              if (cad4[0]+'_WDT') in frase.POS:
                TEMPORAL[r-1].TEXT=TEMPORAL[r-1].TEXT.replace(' '+cad4[0],'')
            p=p-1
            r=r+1
            q=q+1
          for i in range(len(TEMPORAL)):
            MEMORIAB.append(Sentence())
            MEMORIAB[-1]=copy.deepcopy(TEMPORAL[i])
        #5.6
        if 'reduced relative clause' in Sentence1.SIMP[y-1].TYPE:
          TEMPORAL=[]
          TEMPORAL.append(Sentence())
          TEMPORAL.append(Sentence())
          p=2
          q=1
          r=1
          while p>0:
            if 'referred noun phrase' in Sentence1.SIMP[y-1].COMP[q-1]:
              TEMPORAL[r-1]=copy.deepcopy(xTemp)
              cad1=TEMPORAL[r-1].SIMP[y-1].TEXT
              indice1= (int)(TEMPORAL[r-1].SIMP[y-1].COMP[q-1][TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find('[')+1:TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find('..')])
              indice2= (int)(TEMPORAL[r-1].SIMP[y-1].COMP[q-1][TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find('..')+2:TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find(']')])
              cad2=Sentence1.TEXT[indice1:indice2]
              TEMPORAL[r-1].TEXT=TEMPORAL[r-1].TEXT.replace(cad1,cad2)
            if 'clause' in Sentence1.SIMP[y-1].COMP[q-1]:
              TEMPORAL[r-1]=copy.deepcopy(xTemp)
              cad2=Sentence1.SIMP[y-1].TEXT
              TEMPORAL[r-1].TEXT=copy.deepcopy(cad2)
            p=p-1
            r=r+1
            q=q+1
          for i in range(len(TEMPORAL)):
            MEMORIAB.append(Sentence())
            MEMORIAB[-1]=copy.deepcopy(TEMPORAL[i])
    y=y+1
  if DSIMP:
    y=2
    while y<=numSimp:
      for x in range(len(MEMORIAB)):
        if Sentence1.SIMP[y-1].TEXT in MEMORIAB[x].TEXT:
          MEMORIAA.append(Sentence())
          MEMORIAA[-1]=copy.deepcopy(MEMORIAB[x])
          xTemp=Sentence()#----
          xTemp=copy.deepcopy(MEMORIAB[x])#----
          MEMORIAB.pop(x)    
          if 'noun or noun phrase coordination' in Sentence1.SIMP[y-1].TYPE:
            ii=0 #ii equivale a i en el algoritmo
            for i in range(len(Sentence1.SIMP[y-1].COMP)):#y-1 -> python comienza indice en 0
              if ('conjunct' in Sentence1.SIMP[y-1].COMP[i]) and (not('conjunction' in Sentence1.SIMP[y-1].COMP[i])):
                ii=ii+1
            TEMPORAL=[]
            for i in range(ii):
              TEMPORAL.append(Sentence())
            p=ii
            q=1
            r=1
            while p>0:
              if ('conjunct' in Sentence1.SIMP[y-1].COMP[q-1]) and (not('conjunction' in Sentence1.SIMP[y-1].COMP[q-1])):#q-1 -> python comienza indice en 0
                TEMPORAL[r-1]=copy.deepcopy(xTemp)#----
                cad1=TEMPORAL[r-1].SIMP[y-1].TEXT
                indice1= (int)(TEMPORAL[r-1].SIMP[y-1].COMP[q-1][TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find('[')+1:TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find('..')])
                indice2= (int)(TEMPORAL[r-1].SIMP[y-1].COMP[q-1][TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find('..')+2:TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find(']')])
                cad2=Sentence1.TEXT[indice1:indice2]#----
                TEMPORAL[r-1].TEXT=TEMPORAL[r-1].TEXT.replace(cad1,cad2)
                p=p-1
                r=r+1
              q=q+1
            for i in range(len(TEMPORAL)):
              MEMORIAB.append(Sentence())
              MEMORIAB[-1]=copy.deepcopy(TEMPORAL[i])
      y=y+1


  for i in range(len(MEMORIAB)):
    if MEMORIAB[i].TEXT!='':
      print MEMORIAB[i].TEXT,"\n"#Salida
      archSalNombre=arch[:-4]+'_Salida'+'0'+(str)(i)+'.txt'
      archivoSalida=open(archSalNombre,"w")
      archivoSalida.write(MEMORIAB[i].TEXT)
      archivoSalida.close()
else:
  print frase.TEXT #----Salida
  archSalNombre=arch[:-4]+'_Salida'+'.txt'
  archivoSalida=open(archSalNombre,"w")
  archivoSalida.write(frase.TEXT)
  archivoSalida.close()
#FIN




