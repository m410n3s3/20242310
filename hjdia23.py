

def compreensaolista():


    nomes = ["Larissa", "Rafael", "Marcos", "Joao"]
    strg_apr = " Aprovado"
    nomes_apr = []
    for nome in nomes:
        saida=nome + strg_apr
        nomes_apr.append(saida)

    print(nomes_apr)

    nomes2 = ["Ana","Carla","Rotundo","Henrique"]
    strg_repr = " Reprovado"
    nomes_repr = [nome+strg_repr for nome in nomes2]

    print(nomes_repr)

def compreensaolista2():

    nomes = ["Larissa", "Rafael", "Marcos", "Joao"]
    nomes2 = ["Ana","Carla","Rotundo","Henrique"]
    def aprovar_pessoa(nome):
        strg = " Aprovado"
        return nome+strg
    
    def reprovar_pessoa(nome):
        strg = " Reprovado"
        return nome+strg
    
    nomes_apr=[aprovar_pessoa(nome) for nome in nomes]
    nomes_repr=[reprovar_pessoa(nome) for nome in nomes2]
    print(" Aprovado")
    print(nomes_apr)
    print(" Reprovado")
    print(nomes_repr)

def compreensaolista3():
    nomes = ["Larissa", "Rafael", "Marcos", "Joao"]

    def aprovar_pessoa(nome):
        strg = " Aprovado"
        return nome+strg
    nomes2 = [aprovar_pessoa(nome) for nome in nomes if nome!="Rafael"]
    print(nomes2)
    lista1=[1,5,15,19]
    lista2=[0,2,18]
    numeros = [i for i in range(20) if i not in (lista1+lista2)]
    print(numeros)


    def eh_par(num):

        if num%2:
            return False
        else:
            return True
    num2 = [i for i in range(20) if eh_par(i)]
    print(num2)
    # for i in range(20):
    #     print(i%2, end = " ")
    # print()
    # for i in range(20):
    #     print(i%3, end = " ")
    # print()


if __name__=="__main__":
    # compreensaolista()
    # compreensaolista2()
    compreensaolista3()