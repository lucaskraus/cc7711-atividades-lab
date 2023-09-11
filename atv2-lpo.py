# pip install aima3
from aima3.logic import expr,FolKB, fol_fc_ask

clauses = []

#Casos de paternidade e maternidade.
clauses.append(expr("Pai(Pedro,João)"))
clauses.append(expr("Pai(Pedro,Francisco)"))
clauses.append(expr("Pai(Pedro,Clara)"))
clauses.append(expr("Pai(Pedro,Ana)"))
clauses.append(expr("Pai(João,Mario)"))
clauses.append(expr("Pai(Mario,Carlos)")) 

clauses.append(expr("Mãe(Antonia,João)"))
clauses.append(expr("Mãe(Antonia,Francisco)"))
clauses.append(expr("Mãe(Antonia,Clara)"))
clauses.append(expr("Mãe(Antonia,Ana)"))
clauses.append(expr("Mãe(Helena,Mãe)"))
clauses.append(expr("Mãe(Ana,Helena)"))
clauses.append(expr("Mãe(Ana,Joana)"))
clauses.append(expr("Mãe(Clara,Pietro)"))
clauses.append(expr("Mãe(Clara,Enzo)"))

#Casos de avô e avó.
clauses.append(expr("Avô(Pedro,Pietro)"))
clauses.append(expr("Avô(Pedro,Enzo)"))
clauses.append(expr("Avô(Pedro,Mario)"))
clauses.append(expr("Avô(Pedro,Helena)"))
clauses.append(expr("Avô(Pedro,Joana)"))

clauses.append(expr("Avó(Antonia,Pietro)"))
clauses.append(expr("Avó(Antonia,Enzo)"))
clauses.append(expr("Avó(Antonia,Mario)"))
clauses.append(expr("Avó(Antonia,Helena)"))
clauses.append(expr("Avó(Antonia,Joana)"))

#Casos de tio e tia.
clauses.append(expr("Tio(João,Pietro)"))
clauses.append(expr("Tio(João,Enzo)"))
clauses.append(expr("Tio(João,Helena)"))
clauses.append(expr("Tio(João,Joana)"))

clauses.append(expr("Tio(Franscico,Pietro)"))
clauses.append(expr("Tio(Franscico,Enzo)"))
clauses.append(expr("Tio(Franscico,Helena)"))
clauses.append(expr("Tio(Franscico,Joana)"))

clauses.append(expr("Tia(Clara,Mario)"))
clauses.append(expr("Tia(Clara,Helena)"))
clauses.append(expr("Tia(Clara,Joana)"))

clauses.append(expr("Tia(Ana,Pietro)"))
clauses.append(expr("Tia(Ana,Enzo)"))
clauses.append(expr("Tia(Ana,Mario)"))

#Casos de primo e prima.
clauses.append(expr("Primo(Mario,Pietro)"))
clauses.append(expr("Primo(Mario,Enzo)"))
clauses.append(expr("Primo(Mario,Helena)"))
clauses.append(expr("Primo(Mario,Joana)"))

clauses.append(expr("Primo(Pietro,Mario)"))
clauses.append(expr("Primo(Pietro,Helena)"))
clauses.append(expr("Primo(Pietro,Joana)"))

clauses.append(expr("Prima(Helena,Mario)"))
clauses.append(expr("Prima(Helena,Pietro)"))
clauses.append(expr("Prima(Helena,Enzo)"))

clauses.append(expr("Prima(Joana,Mario)"))
clauses.append(expr("Prima(Joana,Pietro)"))
clauses.append(expr("Prima(Joana,Enzo)"))

#Casos de descendência e ascendência
clauses.append(expr("Pai(x,y) ==> Ascendente(x,y)"))
clauses.append(expr("Mãe(x,y) ==> Ascendente(x,y)"))
clauses.append(expr("Avô(x,y) ==> Ascendente(x,y)"))
clauses.append(expr("Avó(x,y) ==> Ascendente(x,y)"))

clauses.append(expr("Pai(x,y) ==> Descendente(y,x)"))
clauses.append(expr("Mãe(x,y) ==> Descendente(y,x)"))
clauses.append(expr("Avô(x,y) ==> Descendente(y,x)"))
clauses.append(expr("Avó(x,y) ==> Descendente(y,x)"))

Genealogia = FolKB(clauses)

perguntas = ["Primo(Mario,x)",
             "Pai(x,Ana)",
             "Avô(Pedro,x)",
             "Tio(João,x)",
             "Descendente(x,Pedro)",
             "Ascendente(x,Pietro)"]

for i in perguntas:
    resposta = fol_fc_ask(Genealogia, expr(i))
    print("%s -> %s" %(i, (list(resposta))))