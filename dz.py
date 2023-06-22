def palindrom():
    wrd = str(input("Введите слово: "))
    lenwrd = len(wrd)
    sps = []
    wrd1 = ""
    for i in range(lenwrd):
        sps.insert(0,wrd[i])
    for i in range(lenwrd):
        wrd1 += sps[i]
    if wrd == wrd1:
        return True
    else:
        return False
palindrom()