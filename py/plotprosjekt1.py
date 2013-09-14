from scitools.std import *
import numpy as np

def extract(filename):
    infile = open(filename,'r')
    column1=[]
    column2=[]
    column3=[]

    for line in infile:
        if len(line)<2:
            break
        values= line.split()
        
        column1.append(float(values[0]))
        column2.append(float(values[1]))
        column3.append(float(values[2]))
    infile.close()
    return array(column1), array(column2), array(column3)


fil='../data/prosjekt1data.txt'
x,u,v = extract(fil)
n=len(x)
plot(x,u,x,v,title=('n=%d'% n),legend=['u (eksakt)','v'],xlabel='x',ylabel='y',hardcopy= '../plot/plot%d'%n)

