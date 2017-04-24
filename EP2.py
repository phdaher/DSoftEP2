Inspermons={"Hage":[50,35,100], "Tori":[45,40,90], "Pelicas":[40,45,80], "Fernandelas":[35,50,70]}
import time
t=10000
x=50000
print("Bem vindos ao Inspermon!")
time.sleep(1)
print("Neste jogo voce ira escolher um personagem e com ele voce podera realizar passeios e batalhas")
time.sleep(3)
bixo=input("Escolha um personagem: ")
time.sleep(1)
print("Boa escolha! Seu personagem de agora para frente é o {0}".format(bixo))
time.sleep(1)
for i in range(t):
    atividade=int(input("Agora, selecione sua atividade, se quiser passear digite 1, se quiser dormir digite 2: "))
    if atividade==1:
        print("Uhuu, vamos passear pelo campus de Insper")
        time.sleep(2)
        print("Que campus bonito! Ei! Espera ai! O que é aqulio ali perto do FabLab? Acho que é outro Inspermon!!")
        time.sleep(3)
        print("Vamos batalhar!!!")
    if atividade==2:
        print("Ai que sono, acho que eu vou dorm... zzz.. mimimi... zzz")
        time.sleep(3)
        print("Algumas horas depois...")
        time.sleep(1)
        print("Uahh, esses puffs do Insper realmente sao muito bons para tirar uma soneca! Mas agora eu queria fazer algo de diferente...")
        time.sleep(1)
        break
for i in range(x): 
    atividade=int(input("Apos ter descançado bastante agora é hora de um passeio, para passear digite 1: "))
    if atividade==1:
        print("Uhuu, vamos passear pelo campus de Insper")
        time.sleep(2)
        print("Que campus bonito! Ei! Espera ai! O que é aqulio ali perto do FabLab? Acho que é outro Inspermon!!")
        time.sleep(3)
        print("Vamos batalhar!!!")
        break