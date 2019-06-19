import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math 
class par:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __lt__(self, other):
        if self.x == other.x:
            return self.y < other.y
        else:
            return self.x < other.x
def udaljenost(a,b):
                    sol=0
                    for i in range(27,56):
                        sol=sol+((K[b][i]-K[a][i])**2)
                    return sol**(1/float(2))


DATA_LOCATION = "data/main_players.csv"
FIRST_ATTRIBUTE = "LS"
SECOND_ATTRIBUTE = "ST"
treci="RS"
cetvrti="LW"
peti="LF"
sest="CF"
sedam="RF"
osam="RW"
devet="LAM"
deset="CAM"
jed="RAM"
dva="LM"
tri="CM"
cet="RCM"
pet="RM"
ses="LWB"
sed="LDM"
osa="CDM"
dev="RDM"
dvades="RWB"
djed="LB"
ddva="LCB"
dtri="CB"
dcet="RCB"
dpet="RB"
dses="LCM"
dsed="Crossing"
dosa="Finishing"
ddev="HeadingAccuracy"
trides="ShortPassing"
trijed="Volleys"
tridva="Dribbling"
tritri="Curve"
tricet="FKAccuracy"
tripet="LongPassing"
trises="BallControl"
trised="Acceleration"
triosa="SprintSpeed"
tridev="Agility"
cetdes="Reactions"
cetjed="Balance"
cetdva="ShotPower"
cettri="Jumping"
cetcet="Stamina"
cetpet="Strength"
cetses="LongShots"   
cetsed="Aggression"
cetosa="Interceptions"
cetdev="Positioning"
petdes="Vision"
petjed="Penalties"
petdva="Composure"
pettri="Marking"
petcet="StandingTackle"
petpet="SlidingTackle"
petses="Potential"
petsed="Overall"
petosa="Name"
petdev="pozicija"
datas = pd.read_csv(DATA_LOCATION)
data1 = datas[[FIRST_ATTRIBUTE, SECOND_ATTRIBUTE, treci,cetvrti,peti,peti,sest,sedam,osam,devet,deset,jed,dva,tri,cet,pet,ses,sed,osa,dev,dvades,djed,ddva,dtri,dcet,dpet,dses,dsed,dosa,ddev,trides,trijed,tridva,tritri,tricet,tripet,trises,trised,triosa,tridev,cetdes,cetjed,cetdva,cettri,cetcet,cetpet,cetses,cetsed,cetosa,cetdev,petdes,petjed,petdva,pettri,petcet,petpet,petses,petsed,petosa,petdev]]

K = data1.values
#plt.scatter(K[:,0], K[:,1], K[:,2],color = 'g')
#plt.show()
min=9999999
sol1=0
k=0
#broj = int(input())
polje = [];
#print("Njegova pozicija je", K[broj][59])
a=0;
b=0;
c=0;
x=0;
y=0;
z=0;
x1=0;
y1=0;
z1=0;
sol=0;
print(K[0][1]);
print(K[0][20]);
for i in range(0,12880):
    p=0;
    a=(K[i][1]+K[i][2]+K[i][3]+K[i][4]+K[i][5]+K[i][6]+K[i][7]+K[i][8])/8
    b=(K[i][9]+K[i][10]+K[i][11]+K[i][12]+K[i][13]+K[i][14]+K[i][15]+K[i][16]+K[i][17]+K[i][18]+K[i][19])/11
    c=(K[i][20]+K[i][21]+K[i][22]+K[i][23]+K[i][24]+K[i][25]+K[i][26])/7
    
    if(a>b and a>c and K[i][59]=="N"): 
                                        sol=sol+1;
                                        p=1;
    if(b>a and b>c and K[i][59]=="V"): 
                                        sol=sol+1;
                                        p=1;
    if(c>b and c>a and K[i][59]=="B"): 
                                        sol=sol+1;
                                        p=1;
    if(p==1 and K[i][59]=="N"): x=x+1;
    if(p==1 and K[i][59]=="V"): y=y+1;
    if(p==1 and K[i][59]=="B"): z=z+1;
    if(K[i][59]=="N"): x1=x1+1;
    if(K[i][59]=="V"): y1=y1+1;
    if(K[i][59]=="B"): z1=z1+1;
    if()     
print(sol)
print(x1)
print(x/x1)
print(y/y1)
print(z/z1)

