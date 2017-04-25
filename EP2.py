#para sortear valores:
import random
#s1 e s2 sao os fatores de sorte que serao implementados na funcao da batalha para que a batalha nao seja previsivel

s1=[2,3,4,5,6]
s2=[1.6,1.7,1.8,1.9,2]
s1r=int(random.choice(s1))
s2r=int(random.choice(s2))

#Dicionario com os nomes dos Inspermons seguidos do poder de ataque, poder de defesa e quantidade de vida, respectiamente

Inspermons={"Hage":[50.11,35.34,60.17], "Tori":[45.54,40.19,55.32], "Pelicas":[40.76,45.39,50.18], "Fernandelas":[35.42,50.71,50.27]}
adversario=["Hage","Tori","Pelicas","Fernandelas"]

def batalha(bixo, outro):
    while Inspermons[bixo][2] >= 0 and int(Inspermons[outro][2]) >= 0:
        (Inspermons[bixo][2]) = (Inspermons[bixo][2]) - (((Inspermons[outro][0]) - (Inspermons[bixo][1]))*s1r)
        if Inspermons[bixo][2] <=0:
            print("Voce perdeu")
            print("GAME OVER!")
            break
        (Inspermons[outro][2]) = (Inspermons[outro][2]) - (((Inspermons[bixo][0]) - (Inspermons[outro][1]))*s2r)
        if Inspermons[outro][2] <=0:
            print("Parabéns, você ganhou!!")
            break
        if Inspermons[bixo][2] == Inspermons[outro][2]:
            print("Houve um empate!")
            break
            
            
#importei o tempo para consegui dar pausas no jogo e melhor a jogabilidade
import time
t=10000
x=50000
outro=str(random.choice(adversario))

#começo do jogo com frases interativas de introducao

print("Bem vindos ao Inspermon!")
time.sleep(1)
print("Neste jogo voce ira escolher um personagem e com ele voce podera realizar passeios e batalhas")
time.sleep(3)
bixo=input("Os personagens disponiveis sao: Hage, Tori, Pelicas e Fernandelas. Escolha entre um deles:")
time.sleep(1)
print("Boa escolha! Seu personagem de agora para frente é o {0}".format(bixo))
time.sleep(1)
#jogador seleciona o que ele gostaria de fazer (passear ou dormir)
for i in range(t):
    atividade=int(input("Agora, selecione sua atividade, se quiser passear digite 1, se quiser dormir digite 2: "))
    if atividade==1:
        print("Uhuu, vamos passear pelo campus de Insper")
        time.sleep(2)
        print("Que campus bonito! Ei! Espera ai! O que é aqulio ali perto do FabLab? Acho que é outro Inspermon!!")
        time.sleep(3)
        print("Seu adversario é o {0}" .format(outro))
        print("Vamos batalhar!!!")
        #comeco da batalha, com uma funcao semelhante a que foi pedida para o EP2 (note que o fator de sorte foi adicionado a ela)
        batalha(bixo,outro)
        break
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
        print("Seu adversario é o {0}" .format(outro))
        time.sleep(3)
        print("Vamos batalhar!!!")
        batalha(bixo,outro)
        if Inspermons[bixo][2] <=0:
            print("Infelizmente você nao possui mais vidas para continuar jogando!")
            break

        #Fim de Jogo