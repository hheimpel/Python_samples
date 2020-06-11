from itertools import permutations

#Given 4 numbers, can operations on them (including nested parenthesis)
#make them equal to 24?
#Example input (6,4,2,6) : (6-4+2)*(6) = 24

def eq(a,b,c,d):
    for array in set(permutations([a,b,c,d])):
        array = list(array)
        a=["("+str(array.pop())]
        
        #Breadth First Search
        while array:
            b = list(a)
            a = []
            dig = array.pop()
            
            for elem in b:
                for sign in list("+-*/")+[")*(",")/(",")*(-",")/(-",")+(",")-("]:
                    if not array:
                        a.append(elem+sign+str(dig)+")")
                        try:
                            if eval(elem+sign+str(dig)+")") == 24:
                                return a[-1]
                        except ZeroDivisionError:
                            continue
                    else:
                        a.append(elem+sign+str(dig))
    
    return "It's not possible!"
