#para sortear valores:
import random
#s1 e s2 sao os fatores de sorte que serao implementados na funcao da batalha para que a b atalha nao seja previsivel
s1=[0.1,0.2,0.3,0.4,0.5]
s2=[0.6,0.7,0.8,0.9,1]
s1r=str(random.choice(s1))
s2r=str(random.choice(s2))
#Dicionario com os nomes dos Inspermons seguidos do poder de ataque, poder de defesa e quantidade de vida, respectiamente
Inspermons={"Hage":[50,35,100], "Tori":[45,40,90], "Pelicas":[40,45,80], "Fernandelas":[35,50,70]}
adversario=["Hage","Tori","Pelicas","Fernandelas"]
#importei o tempo para consegui dar pausas no jogo e melhor a jogabilidade
import time
t=10000
x=50000
#começo do jogo com frases interativas de introducao
print("Bem vindos ao Inspermon!")
time.sleep(1)
print("Neste jogo voce ira escolher um personagem e com ele voce podera realizar passeios e batalhas")
time.sleep(3)
bixo=input("Os personagens disponiveis sao: Hage, Tori, Pelicas e Fernandelas. Escolha entre um deles: ")
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
        print("Vamos batalhar!!!")
        #comeco da batalha, com uma funcao semelhante a que foi pedida para o EP2 (note que o fator de sorte foi adicionado a ela)
        def batalha(bixo, outro):
            while Inspermons["bixo"][2] >= 0 and Inpsermons["outro"][2] >= 0:
                Inspermons["bixo"][2] = Inspermons["bixo"][2] - ((Inpsermons["outro"][0] - Inspermons["bixo"][1])*s1r)
                if Inspermons["bixo"][2] <=0:
                    print("Voce perdeu")
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
        outro=str(random.choice(adversario))
        print("Seu adversario é {0}" .format(outro))
        time.sleep(3)
        print("Vamos batalhar!!!")
        def batalha(bixo, outro):
            while Inspermons["bixo"][2] >= 0 and Inpsermons["outro"][2] >= 0:
                Inspermons["bixo"][2] = Inspermons["bixo"][2] - ((Inpsermons["outro"][0] - Inspermons["bixo"][1])*s2r)
                if Inspermons["bixo"][2] <=0:
                    print("Voce perdeu")
                    break
                    #Fim de Jogo