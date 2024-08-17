import random
import time

print("Bienvenido al Blackjack\n Repartiendo cartas........")
def Carta():
    return(random.randint(1,11))

vida = True
jgd_crt1 = Carta()
jgd_crt2 = Carta()
Total = jgd_crt1 + jgd_crt2
print(f"Tus cartas son: \nPrimera:{jgd_crt1}\nSegunda: {jgd_crt2}\n Total:{Total}")
dlr_crt1 = Carta()
dlr_total = dlr_crt1
print(f"Las cartas del dealer son: \nPrimera:{dlr_crt1}\n Total:{dlr_total}")
while vida is True:
    if Total>21:
        time.sleep(1)
        print("Has perdido, te has pasado de 21")
        vida = False
        break
    elif Total== 21:
        time.sleep(1)
        print("Has ganado, BlackJack")
        break
    elif dlr_total== 21:
        time.sleep(1)
        print("Ha ganado el dealer, Blackjack")
        vida = False
        break
    
    elif Total< 21:
        
        op = input("(1) para Pedir, (2) para quedarte\n")
        if op =="1":
            nv = Carta()
            Total = Total+nv
            print(f"Has sacado un:{nv}, tu nuevo total es:{Total} ")
        elif op =="2":
            print(f"Te has quedado con un Total de:{Total}")
            for i in range(0,99):
                time.sleep(2)
                nv2 = Carta()
                dlr_total = dlr_total+nv2
                print(f"El dealer a sacado un:{nv2}\nSu nuevo total es:{dlr_total}")
                if dlr_total == Total and dlr_total>=17:
                    time.sleep(1)
                    print("Empate")
                    vida = False
                    break
                    exit()
                elif dlr_total >= 17 and dlr_total> Total and dlr_total < 21:
                    time.sleep(1)
                    print("El dealer se ha quedado, Has perdido!")
                    vida = False
                    break
                    exit()
                elif dlr_total > 21:
                    time.sleep(1)
                    print("El dealer se ha pasado, Has ganado!")
                    vida = False
                    break
                    exit()
