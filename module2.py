def loe_failist(file:str)->str:
    """Loeme tekst failist
    """
    f=open(file,'r')
    stroka=f.read()
    return stroka
stroka=loe_failist("TextFile.txt")
print(stroka)
