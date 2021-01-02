
#### DERIVATIVE SOLVER USING THE POWER RULE #####
def finda(n):
    a=""

    for x in range(len(n)):
            if n[x] == "x":
                for i in range(n.index('x')):
                    a += str(n[i])
                
    return a

def findb(n):

    b=""
    for x in range(len(n)):
            if n[x] == "x":
                b=n[x+1:len(n)]
    return b


def Diff(n):
    a = finda(n)
    b= findb(n)
    ders = ""
    #loop to keep differentiating
    while int(b) > 0:

        #####DIFFERENTIATE#######
        a=int(b)*int(a)
        b= int(b)-1
        n = str(a)+"x^"+ str(b)
        #####DIFFERENTIATE#######

        ders += (n + ", ")
    print(ders)

Diff("75x71")

    



