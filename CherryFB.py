import os

RES_0402_E96 = [1,    1.1,    1.2,    1.3,    1.5,    1.6,    1.8,    2,      2.2,    2.49,   2.7,    3,      3.3,    \
                3.6,  3.9,    4.3,    4.75,   4.99,   5.1,    5.6,    6.2,    6.8,    7.5,    8.2,    9.1,            \
                10,   11,     12,     13,     15,     16,     18,     20,     22,     24.9,   27,     30,     33,     \
                36,   39,     43,     47,     49.9,   51,     56,     62,     68,     75,     82,     91,     100,    \
                110,  120,    130,    150,    160,    180,    200,    220,    249,    270,    300,    330,    360,    \
                390,  430,    470,    499,    510,    560,    620,    680,    750,    820,    910,    1000,   2000]

print("##  +---- Vout   ")
print("##  |            ")
print("##  | R1         ")
print("##  |            ")
print("##  +----FB      ")
print("##  |            ")
print("##  | R2         ")
print("##  +---- GND    ") 

#    +---- Vout
#    |     
#    | R1   
#    |
#    +----FB  
#    |   
#    | R2
#    +---- GND 

def Calc_Vout(Vfb, VR1, VR2):
    Vout = round(Vfb *(1 + (VR1/VR2)), 3)
    return float(Vout)

Vout = 0

# a = 57.2
# print(  min(RES_0402_E96, key=lambda x: abs(x - a)) )

print("fb res:")
if 1:
    Vfb    = float(input("?Vfb="))
    Vout   = float(input("?Vout="))
else:
    Vfb    = 0.8
    Vout   = 3.3 

R2_R1_p = float((Vout - Vfb) / Vfb)
rlen = len(RES_0402_E96)

for i in range(-1,-1*rlen-1,-1):
    # print(RES_0402_E96[i])
    def_R1 = RES_0402_E96[i]        #2000K
    if(def_R1 < 10):
        continue
    def_R2 = def_R1 / R2_R1_p       #400K

    def_min_R2 = min(RES_0402_E96, key=lambda x: abs(x - def_R2))#choose min res
    def_min_v  = Calc_Vout(Vfb, def_R1, def_min_R2)
    # print("min_v ", def_min_v)
    if(abs(Vout - def_min_v) <= 0.2):
        if(def_min_R2 > 10):
            print(f"min_v={def_min_v}V\tR1={def_R1}K\tR2={def_min_R2}K")
            # print("min_v ", def_min_v, "V\tR1:",def_R1, "\tR2:", def_min_R2)
            # print("check R1 R2=")

# print("Vout=", Vout)
# print("R2_R1_p=", R2_R1_p)
