"""
Implementacion del Algoritmo de Daniel Nieto v3

Salida para el ejemplo:
Escherichia coli is able to use trehalose [O-U-D-glucosyl-a-D-glucoside] as a
carbon source when grown in high-osmolarity medium.

Escherichia coli is able to can also synthesize trehalose as an osmoprotectant when
grown in high-osmolarity medium.

Escherichia coli is able to can also accumulate trehalose as an osmoprotectant when
grown in high-osmolarity medium.
"""

import copy
import sys


class Simp(object):
  TYPE=""
  TEXT=""
  COMP=["","",""]


class Frase(object):
  TYPE=""
  TEXT=""
  POS=""
  TREE=""
#  SIMP=[Simp(),Simp()]
  SIMP=[]

class Sentence(object):
  TEXT=""
  TREE=""
  SIMP=[]
  
MEMORIAB=[]



#-----------parte para poner los datos desde archivo


#Frase 1: TYPE: sentence[0..199]
frase=Frase()
frase.TYPE='sentence[0..199]'
frase.TEXT='Escherichia coli is able to use trehalose [O-U-D-glucosyl-a-D-glucoside] as a carbon source but can also synthesize and accumulate trehalose as an osmoprotectant when grown in high-osmolarity medium.'
frase.POS='Escherichia_FW coli_FW is_VBZ able_JJ to_TO use_VB trehalose_NN -LSB-_-LRB- O-U-D-glucosyl-a-D-glucoside_NN -RSB-_-RRB- as_IN a_DT carbon_NN source_NN but_CC can_MD also_RB synthesize_VB and_CC accumulate_VB trehalose_NN as_IN an_DT osmoprotectant_NN when_WRB grown_VBN in_IN high-osmolarity_JJ medium_NN ._.'
frase.TREE='(ROOT (SINV (ADVP (FW Escherichia) (FW coli)) (VP (VBZ is) (ADJP (JJ able) (S (VP (TO to) (VP (VP (VB use) (NP (NN trehalose) (PRN (-LRB- -LSB-) (NN O-U-D-glucosyl-a-D-glucoside) (-RRB- -RSB-))) (PP (IN as) (NP (DT a) (NN carbon) (NN source)))) (CC but) (VP (MD can) (ADVP (RB also)) (VP (VP (VB synthesize) (CC and) (VB accumulate)) (NP (NN trehalose)) (PP (IN as) (NP (DT an) (NN osmoprotectant)))))))))) (SBAR (WHADVP (WRB when)) (S (VP (VBN grown) (PP (IN in) (NP (JJ high-osmolarity) (NN medium)))))) (. .)))'
#-SIMP1
frase.SIMP.append(Simp())#Simp1
frase.SIMP[0].TYPE='verb or verb phrase coordination[28..161]'
frase.SIMP[0].TEXT='use trehalose [O-U-D-glucosyl-a-D-glucoside] as a carbon source but can also synthesize and accumulate trehalose as an osmoprotectant'
#-COMP
frase.SIMP[0].COMP[0]='conjunct[28..91]'
frase.SIMP[0].COMP[1]='conjunction[92..95]'
frase.SIMP[0].COMP[2]='conjunct[96..161]'
#-SIMP2
frase.SIMP.append(Simp())#Simp2
frase.SIMP[1].TYPE='verb or verb phrase coordination[105..130]'
frase.SIMP[1].TEXT='synthesize and accumulate'
#-COMP
#frase.SIMP[1].COMP1='conjunct[105..115]'
#frase.SIMP[1].COMP2='conjunction[116..119]'
#frase.SIMP[1].COMP3='conjunct[120..130]'

frase.SIMP[1].COMP[0]='conjunct[105..115]'
frase.SIMP[1].COMP[1]='conjunction[116..119]'
frase.SIMP[1].COMP[2]='conjunct[120..130]'



"""
#Frase 2 TYPE: sentence[329..452]
frase=Frase()
frase.TYPE='sentence[329..452]'
frase.TEXT='rpoS is identical to katF, which was identified as a positive regulator for catalaseHPII (katE) and exonuclease III (xthA).'
frase.POS='rpoS_NN is_VBZ identical_JJ to_TO katF_NN ,_, which_WDT was_VBD identified_VBN as_IN a_DT positive_JJ regulator_NN for_IN catalaseHPII_NN -LRB-_-LRB- katE_NN -RRB-_-RRB- and_CC exonuclease_NN III_CD -LRB-_-LRB- xthA_NN -RRB-_-RRB- ._.'
frase.TREE='(ROOT (S (NP (NN rpoS)) (VP (VBZ is) (ADJP (JJ identical) (PP (TO to) (NP (NP (NN katF)) (, ,) (SBAR (WHNP (WDT which)) (S (VP (VBD was) (VP (VBN identified) (PP (IN as) (NP (NP (DT a) (JJ positive) (NN regulator)) (PP (IN for) (NP (NP (NP (NN catalaseHPII)) (PRN (-LRB- -LRB-) (NP (NN katE)) (-RRB- -RRB-))) (CC and) (NP (NN exonuclease) (CD III)) (PRN (-LRB- -LRB-) (NP (NN xthA)) (-RRB- -RRB-)))))))))))))) (. .)))'
#-SIMP1
frase.SIMP.append(Simp())#Simp1
frase.SIMP[0].TYPE='parenthesis[405..423]'
frase.SIMP[0].TEXT='catalaseHPII (katE'
#-COMP
frase.SIMP[0].COMP[0]='referred noun phrase[405..417]'
frase.SIMP[0].COMP[1]='parenthesized elements[419..423]'
frase.SIMP[0].COMP[2]=''
#-SIMP2
frase.SIMP.append(Simp())#Simp2
frase.SIMP[1].TYPE='full relative clause[350..451]'
frase.SIMP[1].TEXT='katF, which was identified as a positive regulator for catalaseHPII (katE) and exonuclease III (xthA)'
#-COMP
frase.SIMP[1].COMP[0]='referred noun phrase[350..354]'
frase.SIMP[1].COMP[1]='clause[356..451]'
frase.SIMP[1].COMP[2]=''
"""
#------------



#-------Programa principal

#Algoritmo v3


if ((frase.TYPE.find('sentence')) !=- 1) and (frase.SIMP[0].TYPE != ''):
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
  for i in range(len(frase.SIMP)):
    ordenSIMP[i].append(i)
    ordenSIMP[i].append((int)(Sentence1.SIMP[i].TYPE[Sentence1.SIMP[i].TYPE.find('[')+1:Sentence1.SIMP[i].TYPE.find('..')]))
    ordenSIMP[i].append((int)(Sentence1.SIMP[i].TYPE[Sentence1.SIMP[i].TYPE.find('..')+2:Sentence1.SIMP[i].TYPE.find(']')]))
  i=1
  a=0
  tmpOrden=Simp()
  while i:
    for j in range(len(frase.SIMP)):
      for k in range(len(frase.SIMP)-1):
        if (ordenSIMP[j][1]>ordenSIMP[k+1][1]):
          tmpOrden=Sentence1.SIMP.pop(j)
          Sentence1.SIMP.insert(k+1,tmpOrden)
          a=1
          break
        elif (ordenSIMP[j][1]==ordenSIMP[k+1][1]):
          if (ordenSIMP[j][2]<ordenSIMP[k+1][2]):
            tmpOrden=Sentence1.SIMP.pop(j)
            Sentence.SIMP.insert(k+1,tmpOrden)
            a=1
            break
      if a==1:
        a=0
        break
    i=0

  y=len(Sentence1.SIMP)
  while y>0:
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
              TEMPORAL[r-1]=copy.deepcopy(Sentence1)
              cad1=TEMPORAL[r-1].SIMP[y-1].TEXT
              indice1= (int)(TEMPORAL[r-1].SIMP[y-1].COMP[q-1][TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find('[')+1:TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find('..')])
              indice2= (int)(TEMPORAL[r-1].SIMP[y-1].COMP[q-1][TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find('..')+2:TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find(']')])
              cad2=TEMPORAL[r-1].TEXT[indice1:indice2]
              TEMPORAL[r-1].TEXT=TEMPORAL[r-1].TEXT.replace(cad1,cad2)
              p=p-1
              r=r+1
            q=q+1
          for i in range(len(TEMPORAL)):
            MEMORIAB.append(TEMPORAL[i].TEXT)
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
              TEMPORAL[r-1]=copy.deepcopy(Sentence1)
              cad1=TEMPORAL[r-1].SIMP[y-1].TEXT
              indice1= (int)(TEMPORAL[r-1].SIMP[y-1].COMP[q-1][TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find('[')+1:TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find('..')])
              indice2= (int)(TEMPORAL[r-1].SIMP[y-1].COMP[q-1][TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find('..')+2:TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find(']')])
              cad2=TEMPORAL[r-1].TEXT[indice1:indice2]
              TEMPORAL[r-1].TEXT=TEMPORAL[r-1].TEXT.replace(cad1,cad2)
              p=p-1
              r=r+1
            q=q+1
          for i in range(len(TEMPORAL)):
            MEMORIAB.append(TEMPORAL[i].TEXT) 
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
              TEMPORAL[r-1]=copy.deepcopy(Sentence1)
              indice1= (int)(TEMPORAL[r-1].SIMP[y-1].COMP[q-1][TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find('[')+1:TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find('..')])
              indice2= (int)(TEMPORAL[r-1].SIMP[y-1].COMP[q-1][TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find('..')+2:TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find(']')])
              cad2=TEMPORAL[r-1].TEXT[indice1:indice2]
              TEMPORAL[r-1].TEXT=copy.deepcopy(cad2)
              p=p-1
              r=r+1
            q=q+1
          for i in range(len(TEMPORAL)):
            MEMORIAB.append(TEMPORAL[i].TEXT)
        #5.4
        if 'parenthesis' in Sentence1.SIMP[y-1].TYPE:
          TEMPORAL.append(Sentence())
          TEMPORAL.append(Sentence())
          p=2
          q=1
          r=1
          while p>0:
            TEMPORAL[r-1]=copy.deepcopy(Sentence1)
            indice1= (int)(TEMPORAL[r-1].SIMP[y-1].COMP[q-1][TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find('[')+1:TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find('..')])
            indice2= (int)(TEMPORAL[r-1].SIMP[y-1].COMP[q-1][TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find('..')+2:TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find(']')])
            cad2=TEMPORAL[r-1].TEXT[indice1:indice2]
            TEMPORAL[r-1].TEXT=copy.deepcopy(cad2)
            p=p-1
            r=r+1
          for i in range(len(TEMPORAL)):
            MEMORIAB.append(TEMPORAL[i].TEXT)
        #5.5
        if 'full relative clause' in Sentence1.SIMP[y-1].TYPE:
          TEMPORAL.append(Sentence())
          TEMPORAL.append(Sentence())
          p=2
          q=1
          r=1
          while p>0:
            if 'referred noun frase' in Sentence1.SIMP[y-1].COMP[q-1]:
              TEMPORAL[r-1]=copy.deepcopy(Sentence1)
              cad1=TEMPORAL[r-1].SIMP[y-1].TEXT
              indice1= (int)(TEMPORAL[r-1].SIMP[y-1].COMP[q-1][TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find('[')+1:TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find('..')])
              indice2= (int)(TEMPORAL[r-1].SIMP[y-1].COMP[q-1][TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find('..')+2:TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find(']')])
              cad2=TEMPORAL[r-1].TEXT[indice1:indice2]
              TEMPORAL[r-1].TEXT=TEMPORAL[r-1].TEXT.replace(cad1,cad2)
            if 'clause' in Sentence1.SIMP[y-1].COMP[q-1]:
              TEMPORAL[r-1]=copy.deepcopy(Sentence1)
              indice1= (int)(TEMPORAL[r-1].SIMP[y-1].COMP[q-1][TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find('[')+1:TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find('..')])
              indice2= (int)(TEMPORAL[r-1].SIMP[y-1].COMP[q-1][TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find('..')+2:TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find(']')])
              cad2=TEMPORAL[r-1].TEXT[indice1:indice2]
              TEMPORAL[r-1].TEXT=copy.deepcopy(cad2)
            p=p-1
            r=r+1
            q=q+1
          for i in range(len(TEMPORAL)):
            MEMORIAB.append(TEMPORAL[i].TEXT)
        #5.6
        if 'reduced relatived clause' in Sentence1.SIMP[y-1].TYPE:
          TEMPORAL.append(Sentence())
          TEMPORAL.append(Sentence())
          p=2
          q=1
          r=1
          while p>0:
            if 'referred noun frase' in Sentence1.SIMP[y-1].COMP[q-1]:
              TEMPORAL[r-1]=copy.deepcopy(Sentence1)
              cad1=TEMPORAL[r-1].SIMP[y-1].TEXT
              indice1= (int)(TEMPORAL[r-1].SIMP[y-1].COMP[q-1][TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find('[')+1:TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find('..')])
              indice2= (int)(TEMPORAL[r-1].SIMP[y-1].COMP[q-1][TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find('..')+2:TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find(']')])
              cad2=TEMPORAL[r-1].TEXT[indice1:indice2]
              TEMPORAL[r-1].TEXT=TEMPORAL[r-1].TEXT.replace(cad1,cad2)
            if 'clause' in Sentence1.SIMP[y-1].COMP[q-1]:
              TEMPORAL[r-1]=copy.deepcopy(Sentence1)
              indice1= (int)(TEMPORAL[r-1].SIMP[y-1].COMP[q-1][TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find('[')+1:TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find('..')])
              indice2= (int)(TEMPORAL[r-1].SIMP[y-1].COMP[q-1][TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find('..')+2:TEMPORAL[r-1].SIMP[y-1].COMP[q-1].find(']')])
              cad2=TEMPORAL[r-1].TEXT[indice1:indice2]
              TEMPORAL[r-1].TEXT=copy.deepcopy(cad2)
            p=p-1
            r=r+1
            q=q+1
          for i in range(len(TEMPORAL)):
            MEMORIAB.append(TEMPORAL[i].TEXT)

        y=y-1
  for i in range(len(MEMORIAB)):
    print i,MEMORIAB[i],"\n"
elif ((frase.TYPE.find('sentence')) !=- 1) and (frase.SIMP[0].TYPE == ''):
  print frase.TEXT #----Salida
#FIN



