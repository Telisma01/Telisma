import random
debut = True
while debut:
    nonb_odinate = random.randint(0, 500)
    chans = 5
    while chans > 0:
        print("=======Jwenn nonb kache a=====")
        print("")
        chwa = int(input("Ki nonb ou panse li ye :"))
        print()
        if chwa == nonb_odinate:
            print("ou genyen, ou jwenn nonb lan ki te : ", nonb_odinate)
            break
        elif chwa > nonb_odinate:
            print("eseye anko avek yon nonb ki pi piti , ou pa jwenn bon nonb lan ")
            chans -= 1
            print()
        elif chwa < nonb_odinate:
            print("eseye anko avek yon nonb ki pi gran , ou pa jwenn bon nonb lan ")
            chans -= 1
            print()
        if chans == 0:
            print("ou pedi ou pa ret chans anko")
            print("bon nonb lan t  ", nonb_odinate)
            break
        print("chans = ", chans)

