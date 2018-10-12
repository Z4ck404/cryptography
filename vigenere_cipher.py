def split(Text):
    return list(Text)
def numberletter(l):
    dict ={"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9,"K":10,"L":11,"M":12,"N":13,"O":14,"P":15,"Q":16,"R":17,"S":18,"T":19,"U":20,"V":21,"W":22,"X":23,"Y":24,"Z":25}
    return dict[l]
def letternumber(n):
    dict ={"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9,"K":10,"L":11,"M":12,"N":13,"O":14,"P":15,"Q":16,"R":17,"S":18,"T":19,"U":20,"V":21,"W":22,"X":23,"Y":24,"Z":25}
    for key,value in dict.items():
        if ( value == n) :
            return key            
def codeletter(text,key):
    cypher =[]
    T = split(text)
    K= split(key)
    k= len(K)
    stop = len(T)-1
    i = j =0
    while(stop > -1 ):
        s = len(K)+j
        number = (numberletter(T[i]) + numberletter(K[divmod(s,k)[1]]))
        r =  divmod(number,26)[1]
        ct = letternumber(r)
        cypher.append(ct)
        stop= stop -1
        j = j+1
        i = i+1
    return cypher
        
        
        
    
