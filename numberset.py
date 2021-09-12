from fractions import *
import fractions

nbr = input("What number do you want find is set: ")
res = ["N", "Z", "D", "Q", "R"]

def simplifyoperation(nbr:str):
    
    nbrreplace=nbr.replace("-","+-")

    nbrlist = nbrreplace.split("+")

    listdenominator = []
    for n in nbrlist :
        denominator = Fraction(n).denominator
        listdenominator.append(denominator)

    commondenominator = 1
    for n in listdenominator :
        commondenominator = commondenominator * n

    numeratorWithCommonDenominator = []
    for n in nbrlist :
        numeratorWithCommonDenominator.append(Fraction(n).numerator * commondenominator/Fraction(n).denominator)

    numeratorSum = 0
    for n in numeratorWithCommonDenominator :
        numeratorSum += n

    resultfull = (str(int(numeratorSum))+"/"+str(commondenominator))

    if Fraction(resultfull).denominator == 1 :
        result = str(Fraction(resultfull).numerator)
    else :
        result = str(Fraction(resultfull).numerator) + "/" + str(Fraction(resultfull).denominator)

    return result
def N(nbr):
    try:
        if int(nbr)>0 : 
            return 'N '
        else :
            return ""
    except :
        return ""
def Z(nbr):
    try:
        int(nbr)
        return "Z "
    except ValueError:
        return ""
def D(nbr):
    d = Fraction(nbr).denominator
    for n in (2, 5):
        while d % n == 0:
            d /= n
    if d ==  1:
        return "D "
    else:
        return ""
def Q(nbr):
    try:
        res = dict(denom = Fraction(nbr).denominator, num = Fraction(nbr).numerator)
        if Z(res["denom"]) == "Z " and Z(res["num"]) == "Z ":
            return "Q "
    except:
        return ""

nbr = simplifyoperation(nbr)

print(nbr + " belongs " + str(N(nbr)) + str(Z(nbr)) + str(D(nbr)) + str(Q(nbr)) + "R")
