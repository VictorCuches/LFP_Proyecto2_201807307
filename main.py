# =============== L I B R E R I A S ===============
import tkinter as tk
from tkinter import filedialog 
import webbrowser
import time
import os

# ================== C L A S E S ==================
class gramLibre():
    def __init__(self, nombre, noTerm, Term, inicial, produc):
        self.nombre = nombre
        self.noTerm = noTerm
        self.Term = Term
        self.inicial = inicial
        self.produc = list(produc)

class gramRegular():
    def __init__(self, nombre2, noTerm2, Term2, inicial2, produc2):
        self.nombre2 = nombre2
        self.noTerm2 = noTerm2
        self.Term2 = Term2
        self.inicial2 = inicial2
        self.produc2 = list(produc2)

class automataPila():
    def __init__(self, nameA, trani, tranp, tranq, tranf):
        self.nameA = nameA
        self.trani = trani
        self.tranp = tranp
        self.tranq = list(tranq)
        self.tranf = tranf

class infoReporte():
    def __init__(self, pila, entrada, transT, transR):
        self.pila = pila
        self.entrada = entrada
        self.transT = transT
        self.transR = transR


# ================= M E T O D O S =================
def inicio():
    print("==========================================")
    print("------------------------------------------")
    print("            PROYECTO 2 - LFP")
    print(" Lenguajes Formales y de Programación B-")
    print("Victor Alejandro Cuches de León 201807307")
    print("------------------------------------------")
    print("==========================================\n")
    

    num = 5
    for i in range(num):
        print(18*" "+"< "+str(num)+" >")
        time.sleep(1)
        #os.system("cls")
        num = num - 1 
        if (num == 0):
            print(18*" "+"< "+str(num)+" >\n")          
            print(10*" "+"¡B I E N V E N I D O!\n")

def invertPila(pilatx): 
    # metodo para invertir la lista de la pila y convertirla en string para mostrarla en la tabla mas facil
    strPila = ""
    pilatx.reverse()
    for i in range(len(pilatx)):
        strPila = strPila + str(pilatx[i])

    return strPila

def controlInfo(cont):
   
    contador = 0
    # variables para guardar la informacion de la gramatica
    name = ""
    noTer = ""
    term = ""
    ini = ""
    produc = []
    # variable para verificar que la gramatica sea correcta
    gramA = False
    
    for i in range(len(cont)):
        if (cont[i][0] == "*"):
            if (gramA == True):
                listGL.append(gramLibre(name, noTer, term, ini, produc))
            else: 
                listGR.append(gramRegular(name, noTer, term, ini, produc))
            name = ""
            noTer = ""
            term = ""
            ini = ""
            produc.clear()
            gramA = False
            contador = 0
            
        elif (contador == 0): 
            name = cont[i][0]
            contador = contador + 1
        elif (contador == 1):
            noTer = cont[i][0]
            term = cont[i][1]
            ini = cont[i][2]
            contador = contador + 1
        else: 
            produc.append(cont[i])
            if (len(cont[i]) > 3):
                gramA = True
            contador = contador + 1
    

    #showInfo()
        
def showInfo(nomG):
    sideR = ""
    prodPas = ""
    firsP = False
    space = ""
    for i in listGL:
        if (i.nombre == nomG):
            print("Nombre de la gramatica tipo 2: "+i.nombre)
            print("No terminales = { "+str(i.noTerm)+" }")
            print("Terminales = { "+str(i.Term)+" }")
            print("No terminal inicial = "+str(i.inicial))
            print("Producciones: ")
            for j in i.produc:
                limit = int(len(j))     
                for k in range(1, limit):
                    sideR = sideR + j[k]
                    sideR = sideR + " "
                
                if (firsP == False): # este algoritmo es para mostrar | cuando se repita un estado 
                    print(str(j[0])+" -> "+str(sideR))
                    prodPas = j[0]
                    firsP = True
                else: 
                    if (j[0] != prodPas):
                        print(str(j[0])+" -> "+str(sideR))
                        prodPas = j[0]
                    else:
                        space = int(len(j[0]))
                        print(space*" "+"  | "+str(sideR)) # uso del |

                sideR = ""
            print("")
           
def controlAutomata(nomA):
    #variable para guardar los terminales de la gramatica 
    termin = "" 
    #variables para guardar temporalmente los datos de la gramatica
    transi = ""
    transp = ""
    transq = []
    transf = ""
    #variable para guardar el lado derecho de las producciones
    sideR = ""
    for i in listGL:
        if (i.nombre == nomA):
            termin = i.Term.split(",") # para hacer la transicion terminal, terminal; lambda
            transi = "$,$;#" #esta variable la "quemo" ya que es la misma siempre segun el teorema
            transp = "$,$;"+str(i.inicial) #aqui lo unico que cambia es el no terminal inicial 
            transf = "$,#;$" #esta variable la "quemo" ya que es la misma siempre segun el teorema
            
            # empiezo el manejo de las transiciones de q 
            # manejo de transiciones de producciones lambda, prodIzq; prodDer
            # manejo de transiciones de los terminales terminal, terminal; lambda 
            # lo hago de esta manera ya que asi es la estructura segun el teorema

            for j in i.produc: #entro al listado de producciones guardadas
                limite = int(len(j))
                for k in range(1, limite): #para guardar el lado derecho en una sola cadena 
                    sideR = sideR + j[k]
                    sideR = sideR + " " # CAMBIOSSS! ----------------------------------------------------------------------------------
                    
                transq.append("$,"+str(j[0])+";"+str(sideR))
                sideR = ""

            for m in range(len(termin)):
                transq.append(str(termin[m])+","+str(termin[m])+";$")


            listAu.append(automataPila(i.nombre,transi,transp,transq,transf))
            #showAutomataPila2() #forma alternativa de mostrar la informacion guardada 
            AutomataPila(nomA) #metodo para mostrar el html con el automata

def showAutomataPila2():
    for i in listAu:
        print("Automata de pila de: "+str(i.nameA))
        print("Transiciones\n")
        print("i -------> ")
        print(i.trani)
        print("p -------> ")
        print(i.tranp)
        print("q -------> ")
        print(i.tranq)
        print("q -------> ")
        
        print(i.tranf)
        print("f -------> ")

        print("\n\n------------------------------\n\n")

def AutomataPila(nombreA):
    cadenaQ = ""
    cadeQ = False
    with open("auPila.dot",mode="w") as f:
       
        # caracteristicas de cada nodo     
        f.write("digraph automata{\n")
        f.write("rankdir=LR;\n")
        f.write("nodo1[label="+"\""+"i"+"\""+" shape=circle, width=0.6];\n")
        f.write("nodo2[label="+"\""+"p"+"\""+" shape=circle, width=0.6];\n")
        f.write("nodo3[label="+"\""+"q"+"\""+" shape=circle, width=1.4];\n")
        f.write("nodo4[label="+"\""+"f"+"\""+" shape=doublecircle, width=0.6];\n")
        f.write("flechita[label="+"\""+""+"\""+" , color="+"\"white\""+"];\n")
        
        for i in listAu:
            # recorro la lista donde guarde la informacion del automata
            f.write("flechita->nodo1[arrowsize="+"\"1.2\""+"] ")
            f.write("nodo1->nodo2[label="+"\""+str(i.trani)+"\""+"];\n")
            f.write("nodo2->nodo3[label="+"\""+str(i.tranp)+"\""+"];\n")
            # transiciones del estado q, las guardo en una sola cadena para que sea mas sencillo mostrar la transicion
            for j in i.tranq:
                if (cadeQ == False):
                    cadenaQ = str(j)
                    cadeQ = True
                else: 
                    cadenaQ = cadenaQ + " \\n " + str(j)
            
        f.write("nodo3->nodo3[label="+"\""+str(cadenaQ)+"\""+"];\n")
        f.write("nodo3->nodo4[label="+"\""+str(i.tranf)+"\""+"];\n") 
        f.write("}\n")
    os.system('dot -Tpng auPila.dot -o img/auPila.png') # guardo la imagen en la carpeta img para usarla luego en el html 
    showAutomataPila(nombreA)
 
def showAutomataPila(nombreA):
    html = open("automataPila.html","w")
    parte1 = """
    <html>
	<head>
		<title>Automata - P2</title>
	</head>
    <style type="text/css">
    body{
        background-color: #DFDBE5;
        background-image: url("data:image/svg+xml,%3Csvg width='100' height='20' viewBox='0 0 100 20' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M21.184 20c.357-.13.72-.264 1.088-.402l1.768-.661C33.64 15.347 39.647 14 50 14c10.271 0 15.362 1.222 24.629 4.928.955.383 1.869.74 2.75 1.072h6.225c-2.51-.73-5.139-1.691-8.233-2.928C65.888 13.278 60.562 12 50 12c-10.626 0-16.855 1.397-26.66 5.063l-1.767.662c-2.475.923-4.66 1.674-6.724 2.275h6.335zm0-20C13.258 2.892 8.077 4 0 4V2c5.744 0 9.951-.574 14.85-2h6.334zM77.38 0C85.239 2.966 90.502 4 100 4V2c-6.842 0-11.386-.542-16.396-2h-6.225zM0 14c8.44 0 13.718-1.21 22.272-4.402l1.768-.661C33.64 5.347 39.647 4 50 4c10.271 0 15.362 1.222 24.629 4.928C84.112 12.722 89.438 14 100 14v-2c-10.271 0-15.362-1.222-24.629-4.928C65.888 3.278 60.562 2 50 2 39.374 2 33.145 3.397 23.34 7.063l-1.767.662C13.223 10.84 8.163 12 0 12v2z' fill='%239C92AC' fill-opacity='0.4' fill-rule='evenodd'/%3E%3C/svg%3E");

    }
    #cuadro{
        background-color: white;
        width: 70%;
        border: 4px solid black;
    }
    #datos{
    
        text-align: left;
        padding-left: 30px;  
    }
    #autom{
             
        padding-left: 30px;
        padding-right: 30px;
    }
    </style>
    <body>
        <br>
       <br>

        <center>
            <div id="cuadro">

    """
    parte2 = """
    </section>
                <section id="autom">
                    <img src="img/auPila.png">
                    <br>
                    <br>
                    <br>
                    <br>

                </section>
            </div>
        </center>
    </body>
    </html>
    """
    html.write(parte1)
    for i in listGL:
        if (nombreA == i.nombre):
            html.write("<h1>Nombre: AP_"+str(nombreA)+"</h1>")
            html.write("<section id="+"\"datos\""+">")
            html.write("Terminales = {"+str(i.Term)+"}")
            html.write("<br>")
            alfabeto = str(i.Term) +","+ str(i.noTerm)
            html.write("Alfabeto de Pila = {"+str(alfabeto)+",#}")
            html.write("<br>")
            html.write("Estados = {i, p, q, f}")
            html.write("<br>")
            html.write("Estado inicial = {"+"i"+"}")
            html.write("<br>")
            html.write("Estado de aceptación = {"+"f"+"}")
            html.write("<br>")
            html.write("<br>")
            html.write("<br>")
    
    html.write(parte2)


    html.close()
    webbrowser.open_new_tab('automataPila.html') #abrir automaticamente el html con los datos

def verNoTerm(nome,note):
    for i in listGL:
        if (nome == i.nombre):
            word = i.noTerm
            word = word.split(",")
            for j in range(len(word)):
                if (note == word[j]):
                    return True

def verTerm(nome,note):
    for i in listGL:
        if (nome == i.nombre):
            word = i.Term
            word = word.split(",")
            for j in range(len(word)):
                if (note == word[j]):
                    return True

def pathAutomata(nameG, inpu, repor): # este metodo funciona como control de la opcion 4 y 5
    #input -> cadena a evaluar          repor -> opcion de reporte para enviar al final - 1 recorrido - 2 tabla

    pilaCa = []
    # variables para guardar informacion de la clase infoReporte
    pilaAu = ""
    caracter = ""
    transiT = ""
    transiR = ""
    # variable de estado para recorrer cada uno del automata de pila 
    estado = "i"
    nestado = "p"
    # lista de producciones 
    listPro = []
    
    # contador 
    no = 0 
    input2 = inpu
    inpu = inpu + "$" # para tener el ultimo estado f  ((1))$
    # longitud de la cadena a evaluar 
    lonCa = int(len(inpu)) 
    print(lonCa)
    
    for i in listAu:
        listPro = list(i.tranq) # hago esta copia de lista para no alterar la lista principal  # ["$,A;A"] 
        print("Datos antes de manipular ")
        print(listPro)
        print("----------------------------------------------------------------------------")
        if (nameG == i.nameA):
           
            #print(listPro)
            #print("-----------------------------")
                   
            for j in range(len(i.tranq)):
                listPro[j] = listPro[j].replace(","," ")
                listPro[j] = listPro[j].replace(";"," ")
                listPro[j] = listPro[j].split()
            print("Datos despues de manipular ")
            print(listPro)
            
            # empieza todo el proceso de tabla/recorrido         

            while (no <= lonCa): #5 a +1 b +1 c +1

                if(estado == "i"): # ***** ESTADO i ***** 
                    caracter = inpu[no] 
                    transiR = i.trani #
                                                    #$,$;#
                    transiT = "("+str(estado)+","+str(i.trani[0])+","+str(i.trani[2])+";"+str(nestado)+","+str(i.trani[4])+")"
                    listRep.append(infoReporte(pilaAu, caracter, transiT, transiR))

                    estado = "p"
                    nestado = "q"

                    pilaAu = "#" + pilaAu
                    pilaCa.append("#")        
                
                elif (estado == "p"): # ***** ESTADO p *****
                    caracter = inpu[no]
                    transiR = i.tranp
                    
                    esIni = i.tranp.replace(","," ") #$,$;A -> $ , $, A
                    esIni = esIni.replace(";"," ")
                    esIni = esIni.split()


                    transiT = "("+str(estado)+","+str(i.tranp[0])+","+str(i.tranp[2])+";"+str(nestado)+","+str(esIni[2])+")"
                    listRep.append(infoReporte(pilaAu, caracter, transiT, transiR))

                    estado = "q"
                    nestado = "q"

                    pilaAu = str(i.tranp[4]) + pilaAu
                    pilaCa.append(esIni[2])

                elif (estado == "q" and no < lonCa): # ***** ESTADO q *****
                    conta = 0 
                    for m in listPro: 
                        if (pilaCa[-1] == m[1]): 

                            if (verNoTerm(nameG, m[2])): # si tiene un no terminal del lado derecho
                                
                                caracter = inpu[no]
                                transiR = i.tranq[conta]

                                pilaCa2 = list(pilaCa)
                                pilaAu = invertPila(pilaCa2)

                                bros = "".join(m[2:]) # -> ["$","A","s","a"]  sa

                                transiT = "("+str(estado)+","+str(m[0])+","+str(m[1])+";"+str(nestado)+","+str(bros)+")"


                                listRep.append(infoReporte(pilaAu, caracter, transiT, transiR))
                            
                                pilaCa.pop() 

                                element = list(m[2:]) 
                                element.reverse() 
                               

                                pilaCa = list(pilaCa) + list(element) 
                               
                            elif (verTerm(nameG, m[2]) and inpu[no] == m[2]): # si tiene un terminal del lado derecho y la entrada coincide
                                
                                caracter = inpu[no]
                                transiR = i.tranq[conta]

                                pilaCa2 = list(pilaCa)
                                pilaAu = invertPila(pilaCa2)

                                bros = "".join(m[2:])

                                transiT = "("+str(estado)+","+str(m[0])+","+str(m[1])+";"+str(nestado)+","+str(bros)+")"


                                listRep.append(infoReporte(pilaAu, caracter, transiT, transiR))
                            
                                pilaCa.pop()

                                element = list(m[2:])
                                element.reverse()
                               
                                pilaCa = list(pilaCa) + list(element)

                            
 
                            elif (m[0] == inpu[no]): # si las entradas coinciden
                              
                                caracter = inpu[no]
                                transiR = i.tranq[conta]

                                pilaCa2 = list(pilaCa)
                                pilaAu = invertPila(pilaCa2)

                                bros = "".join(m[2:]) 

                                transiT = "("+str(estado)+","+str(m[0])+","+str(m[1])+";"+str(nestado)+","+str(bros)+")"


                                listRep.append(infoReporte(pilaAu, caracter, transiT, transiR))
                            
                                pilaCa.pop()



                                no = no + 1  #a - > b
                        

                              
                                if (inpu[no] == "$"): #abzb$
                                    estado = "f" 
                                    
                                   
                            
                            elif(m[2] == "$"):
                                #print("4C -> "+str(input[no]))
                                caracter = inpu[no]
                                transiR = i.tranq[conta]

                                pilaCa2 = list(pilaCa)
                                pilaAu = invertPila(pilaCa2)

                                bros = "".join(m[2:])

                                transiT = "("+str(estado)+","+str(m[0])+","+str(m[1])+";"+str(nestado)+","+str(bros)+")"


                                listRep.append(infoReporte(pilaAu, caracter, transiT, transiR))
                            
                                pilaCa.pop()
                                """

                                print(pilaCa)
                                print(input[no])
                                print("____________")
                                """
                           
 
                        conta = conta + 1 
      
                elif (estado == "f"): # ***** ESTADO f *****
                    
                    #print("5C -> "+str(inpu[no]))
                    caracter = inpu[no]
                    transiR = i.tranf

                    pilaCa2 = list(pilaCa)
                    pilaAu = invertPila(pilaCa2)

                    bros = "".join(m[2:])
                    estado = "q"
                    nestado = "f"

                    transiT = "("+str(estado)+","+str(transiR[0])+","+str(transiR[2])+";"+str(nestado)+","+str(bros)+")"


                    listRep.append(infoReporte(pilaAu, caracter, transiT, transiR))
                    listRep.append(infoReporte("$", caracter, nestado, " "))
                            
                    """
                    print(pilaCa)
                    print(inpu[no])
                    print("____________")
                    """

                    if (repor == 1): # si el usuario escogio mostrar el recorrido PENDIENTE

                        entro =" "
                        pruebaTabla(input2)
                        entro = str(input("\n¿Genero el recorrido? (Si/No) \n"))

                        if (entro.upper() == "SI"):                        
                            makeRecorrido(nameG, input2)

                        #grafos(input2)
                    else: # si el usuario escogio mostrar el reporte en tabla
                        entro =" "

                        pruebaTabla(input2)

                        entro = str(input("\n¿Genero la tabla? (Si/No) \n"))

                        if (entro.upper() == "SI"):                        
                            showTabla(input2)

                    break             
                
def makeRecorrido(nombreR, inp):
    noImg = 0
    limte = 0
    for y in listRep:
        limte = limte + 1

    limte = limte - 1

    for i in listRep:
       

        cadenaQ = ""
        cadeQ = False
               
        with open("auPila"+str(noImg)+".dot",mode="w") as f:
        
            # caracteristicas de cada nodo     
            f.write("digraph automata{\n")
            f.write("rankdir=LR;\n")
            f.write("label ="+"\""+" Iteracion No. "+str(noImg)+"\";\n" )
            if (noImg == 0):
                f.write("nodo1[label="+"\""+"i"+"\""+" shape=circle, width=0.6, style=filled, color="+"\""+"yellow"+"\""+"];\n")            
            else:
                f.write("nodo1[label="+"\""+"i"+"\""+" shape=circle, width=0.6];\n")   

            if (noImg == 1):
                f.write("nodo2[label="+"\""+"p"+"\""+" shape=circle, width=0.6, style=filled, color="+"\""+"yellow"+"\""+"];\n") 
                
            else:    
                f.write("nodo2[label="+"\""+"p"+"\""+" shape=circle, width=0.6];\n")

            if (noImg > 1 and noImg < limte):
                f.write("nodo3[label="+"\""+"q"+"\""+" shape=circle, width=1.4, style=filled, color="+"\""+"yellow"+"\""+"];\n") 

            else:
                f.write("nodo3[label="+"\""+"q"+"\""+" shape=circle, width=1.4];\n")

            if (noImg == limte):
                f.write("nodo4[label="+"\""+"f"+"\""+" shape=doublecircle, width=0.6, style=filled, color="+"\""+"yellow"+"\""+"];\n") 
            else: 

                f.write("nodo4[label="+"\""+"f"+"\""+" shape=doublecircle, width=0.6];\n")

           
            f.write("nodo5[label="+"\""+"{<n> Pila |<p> "+str(i.pila)+"}\""+" , shape=record];\n")
            f.write("nodo6[label="+"\""+"{<n> Entrada |<p> "+str(i.entrada)+"}\""+" , shape=record];\n")
            f.write("nodo7[label="+"\""+str(i.transR)+"\""+" , shape=record , fontcolor="+"\""+"blue"+"\""+"];\n")

            f.write("flechita[label="+"\""+""+"\""+" , color="+"\"white\""+"];\n")
            
            for i in listAu:
                # recorro la lista donde guarde la informacion del automata
                f.write("flechita->nodo1[arrowsize="+"\"1.2\""+"] ")
                f.write("nodo1->nodo2[label="+"\""+str(i.trani)+"\""+"];\n")
                f.write("nodo2->nodo3[label="+"\""+str(i.tranp)+"\""+"];\n")
                # transiciones del estado q, las guardo en una sola cadena para que sea mas sencillo mostrar la transicion
                for j in i.tranq:
                    if (cadeQ == False):
                        cadenaQ = str(j)
                        cadeQ = True
                    else: 
                        cadenaQ = cadenaQ + " \\n " + str(j)
                
            f.write("nodo3->nodo3[label="+"\""+str(cadenaQ)+"\""+"];\n")
            f.write("nodo3->nodo4[label="+"\""+str(i.tranf)+"\""+"];\n") 
            f.write("}\n")
            
            
        os.system('dot -Tpng auPila'+str(noImg)+'.dot -o recorrido/auPila'+str(noImg)+'.png') # guardo la imagen en la carpeta img para usarla luego en el html
        noImg = noImg + 1
    showRecorrido(nombreR, inp, noImg)
    
def showInfoGR(nomGR):
    sideR = ""
    prodPas = ""
    firsP = False
    space = ""
    for i in listGR:
        if (i.nombre2 == nomGR):
            print("Nombre de la gramatica tipo 2: "+i.nombre2)
            print("No terminales = { "+str(i.noTerm2)+" }")
            print("Terminales = { "+str(i.Term2)+" }")
            print("No terminal inicial = "+str(i.inicial2))
            print("Producciones: ")
            for j in i.produc2:
                limit = int(len(j))     
                for k in range(1, limit):
                    sideR = sideR + j[k]
                    sideR = sideR + " "
                
                if (firsP == False): # este algoritmo es para mostrar | cuando se repita un estado 
                    print(str(j[0])+" -> "+str(sideR))
                    prodPas = j[0]
                    firsP = True
                else: 
                    if (j[0] != prodPas):
                        print(str(j[0])+" -> "+str(sideR))
                        prodPas = j[0]
                    else:
                        space = int(len(j[0]))
                        print(space*" "+"  | "+str(sideR)) # uso del |

                sideR = ""
            print("")

# ================ R E P O R T E S ================
def showTabla(inputAu):

    html = open('TablaAutomata.html','w')
    #html.write("Nombre de restaurante: "+str(restaurante[0]))
    html.write("<br>")
    partea ="""
    <html>
    <head>
    <meta charset="utf-8">
    <title>Tabla Automata - P2</title>
    </head>
    <style type="text/css">
    table {
        width: 90%;
        background-color: white;
        text-align: left;
        border-collapse: collapse;
    }
    #entrada{
        background-color: white;
        width:fit-content;
        height: fit-content;
        border: 2px solid black;
        padding-left: 10px;
        padding-right: 10px;
        padding-top: 4px;
        padding-bottom: 4px;  
    }
    th, td{
        padding: 15px;
    }
    body{
        background-color: #58D68D;
        font-family: Arial;
    }
    thead{
        background-color: #246355;
        color: white;
        border-bottom: solid 5px #0F362D;
    }
    tr:nth-child(even){
        background-color: #ddd ;
    }
    tr:hover td{
        background-color: #369681;
        color: white;
    }
    div{
        background-color: #1D8348;
        font-family: Arial;
        width: 100%;
    }
    *{
        margin: 0px;
        padding: 0px;
    }
    </style>

    <body>
    <div>
    <center>
    <br>
    <br>
    <h1>REPORTE DE AUTOMATA</h1>
    <h3>Lenguajes Formales y de Programacion</h3>
    <h3>Victor Alejandro Cuches de Leon     201807307</h3>
    <br>
    <br>

    </center>
    

    </div>

    <center>
        <br>
        <b>Cadena a evaluar</b>
        <br>
    """
    parteb="""
    <br>

    <table >
       <thead>
        <tr>
            <th>Iteracion</th>
            <th>Pila</th>
            <th>Entrada</th>
            <th>Transiciones</th>
           
        </tr>

       </thead>    
    """
    partec = """
    </table>
    <br>
    <br>
    </center>
    </body>
    </html>
    """
    html.write(partea)
    html.write("<div id="+"\"entrada\""+">"+str(inputAu)+"</div>")
    html.write(parteb)

    count = 0
    for n in listRep:

        html.write("<tr>")
        html.write("<td>"+str(count)+"</td>")
        html.write("<td>"+str(n.pila)+"</td>")
        html.write("<td>"+str(n.entrada)+"</td>")
        html.write("<td>"+str(n.transT)+"</td>")
        
        
        html.write("</tr>")

        count = count + 1

    html.write(partec)

    html.close()
    webbrowser.open_new_tab('TablaAutomata.html')#Abrir automaticamente el html con los datos

def pruebaTabla(inputAu):
    con = 0
    print("Iteracion   |    Pila    |     Entrada      |      Transicion T      |   Transicion R")
    for i in listRep:
        print("------------------------------------------------------------------------------------------")        
        print(str(con)+"       "+str(i.pila)+"      "+str(i.entrada)+"      "+str(i.transT)+"       "+str(i.transR))
        con = con + 1

def showRecorrido(nombreRe, inputAu, vueltas):
    html = open("RecorridoAutomata.html","w")
    parte1 = """
    <html>
	<head>
		<title>Recorrido de Automata - P2</title>
	</head>
    <style type="text/css">
    body{
        background-color: #DFDBE5;
        background-image: url("data:image/svg+xml,%3Csvg width='100' height='20' viewBox='0 0 100 20' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M21.184 20c.357-.13.72-.264 1.088-.402l1.768-.661C33.64 15.347 39.647 14 50 14c10.271 0 15.362 1.222 24.629 4.928.955.383 1.869.74 2.75 1.072h6.225c-2.51-.73-5.139-1.691-8.233-2.928C65.888 13.278 60.562 12 50 12c-10.626 0-16.855 1.397-26.66 5.063l-1.767.662c-2.475.923-4.66 1.674-6.724 2.275h6.335zm0-20C13.258 2.892 8.077 4 0 4V2c5.744 0 9.951-.574 14.85-2h6.334zM77.38 0C85.239 2.966 90.502 4 100 4V2c-6.842 0-11.386-.542-16.396-2h-6.225zM0 14c8.44 0 13.718-1.21 22.272-4.402l1.768-.661C33.64 5.347 39.647 4 50 4c10.271 0 15.362 1.222 24.629 4.928C84.112 12.722 89.438 14 100 14v-2c-10.271 0-15.362-1.222-24.629-4.928C65.888 3.278 60.562 2 50 2 39.374 2 33.145 3.397 23.34 7.063l-1.767.662C13.223 10.84 8.163 12 0 12v2z' fill='%239C92AC' fill-opacity='0.4' fill-rule='evenodd'/%3E%3C/svg%3E");

    }
    #cuadro{
        background-color: white;
        width: 70%;
        border: 4px solid black;
    }
    #datos{
    
        text-align: left;
        padding-left: 30px;  
    }
    #autom{
             
        padding-left: 30px;
        padding-right: 30px;
    }
    </style>
    <body>
        <br>
       <br>

        <center>
            <div id="cuadro">

    """
    parte2 = """
    </section>
                <section id="autom">
                    
                    <br>
                    <br>
                    <br>
                    <br>
    """
    parte3 = """
                </section>
            </div>
        </center>
    </body>
    </html>
    """
    html.write(parte1)
    for i in listGL:
        if (nombreRe == i.nombre):
            html.write("<h1>Nombre: AP_"+str(nombreRe)+"</h1>")
            html.write("<section id="+"\"datos\""+">")
            html.write("Terminales = {"+str(i.Term)+"}")
            html.write("<br>")
            alfabeto = str(i.Term) +","+ str(i.noTerm)
            html.write("Alfabeto de Pila = {"+str(alfabeto)+",#}")
            html.write("<br>")
            html.write("Estados = {i, p, q, f}")
            html.write("<br>")
            html.write("Estado inicial = {"+"i"+"}")
            html.write("<br>")
            html.write("Estado de aceptación = {"+"f"+"}")
            html.write("<br>")
            html.write("<br>")
            html.write("<br>")
    
    html.write("<center><h2>Cadena a evaluar: "+str(inputAu)+"</h2></center>")

       
    html.write(parte2)

    conteo = 0
    vueltas = vueltas  # queda pendiente si le tengo que sumar 1
    for k in range(vueltas):
        html.write("<br>")
     
        html.write("<img src="+"\""+"recorrido/auPila"+str(conteo)+".png"+"\""+">")
        html.write("<br>")
        
        html.write("----------------------------------------------------------------------------------------------------------------------------")
        html.write("<br>")
        html.write("<br>")

        conteo = conteo + 1

    html.write("<h2>¡LA CADENA INGRESADA ES VALIDA!</h2>")
    html.write("<br>")

    html.write(parte3)





    html.close()
    webbrowser.open_new_tab('recorrido.html') #abrir automaticamente el html con los datos

# ==================== M A I N ====================

opc = 0
info = [] #

# listas para guardar la informacion de las gramaticas
listGL = []
listGR = []

# lista para guardar la informacion del automata de pila
listAu = []

# lista para guardar la informacion que se usara en los reportes
listRep = []


#inicio() # pantalla de bienvenida que incluye el timer 


while (opc != 7):

    print("----------------------------------------------")
    print("          M E N U  P R I N C I P A L")
    print("----------------------------------------------")
    print("1. Cargar archivo")
    print("2. Mostrar información general de la gramatica")
    print("3. Generar automata de pila equivalente")
    print("4. Reporte de recorrido")
    print("5. Reporte en tabla")
    print("6. Salir")
    opc = int(input("Seleccione una opción: "))
    print("")

    if (opc == 1):
        print("=-=-=-=-=-=-=-=-=-= C A R G A R  A R C H I V O =-=-=-=-=-=-=-=-=-=")
        nameFile = filedialog.askopenfilename(title = "Seleccione archivo", filetypes = (( "*.txt", "*.glc"),))
        txt_file = open(nameFile, "r", encoding="utf-8")
        with txt_file as fil: #para leer linea por linea del archivo
            texto = fil.readlines()
            
        for i in range(len(texto)):
            texto[i] = texto[i].replace("\n", "")
            texto[i] = texto[i].replace(">", " ")
            texto[i] = texto[i].replace("-", " ") #pendiente, esto me servira de flag para identificar el No Terminal de la produccion
            texto[i] = texto[i].replace(";", " ")
            texto[i] = texto[i].split()

      
        controlInfo(texto) #envio el contenido del archivo a un metodo para guardar correctamente cada cosa
       
        txt_file.close()
        
        print("\n¡Se ha cargado el archivo con exito!")

    elif (opc == 2):
        print("=-=-=-=-=-=-=-=-=-= I N F O R M A C I O N  G R A M A T I C A =-=-=-=-=-=-=-=-=-= ")
        opcG = ""
        print("\nListado de gramaticas cargadas en el sistema: ")
        for k in listGL: #muestro el listado de gramaticas para escoger
            print(" - "+str(k.nombre))
        
        
        opcG = input("\nEscriba el nombre de la gramatica que desea escoger: ")
        print("")
        showInfo(opcG)
        input("...")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

        
    elif (opc == 3):
        print("=-=-=-=-=-=-=-=-=-= A U T O M A T A  D E  P I L A =-=-=-=-=-=-=-=-=-= ")
        opcA = ""
        print("\nListado de gramaticas cargadas en el sistema: ")
        for k in listGL: #muestro el listado de gramaticas para escoger
            print(" - "+str(k.nombre))
          
        opcA = input("\nEscriba el nombre de la gramatica que desea escoger: ")
        print("")
        controlAutomata(opcA)

    elif (opc == 4):
        print("=-=-=-=-=-=-=-=-=-= R E P O R T E  D E  R E C O R R I D O =-=-=-=-=-=-=-=-=-= ")
        repor = 1
        opcRA = ""
        cadenA = ""
        
        print("\nListado de automatas cargados en el sistema: ")
        for i in listAu:
            print(" - "+str(i.nameA))

        opcRA = input("\nEscriba el nombre del automata que desea escoger: ")
        print("Se ha seleccionado "+str(opcRA))
        cadenA = input("\nIngrese la cadena a evaluar en el automata: ")

        pathAutomata(opcRA, cadenA, repor)

    elif (opc == 5):
        print("=-=-=-=-=-=-=-=-=-= R E P O R T E  E N  T A B L A =-=-=-=-=-=-=-=-=-= ")
        opcTA = ""
        cadenA = ""
        repor = 2

        print("\nListado de automatas cargados en el sistema: ")
        for i in listAu:
            print(" - "+str(i.nameA))

        opcTA = input("\nEscriba el nombre del automata que desea escoger: ")
        print("Se ha seleccionado "+str(opcTA))
        cadenA = input("\nIngrese la cadena a evaluar en el automata: ")

        pathAutomata(opcTA, cadenA, repor)

        #showTabla(cadenA)
        
    elif (opc == 6):
        print("........................................")
        print("Lenguajes Formales y de Programacion B-")
        print("Nombre: Victor Alejandro Cuches de León")
        print("Carnet: 201807307")
        print("Correo: vcuches55@gmail.com")
        input("adios...")

    elif (opc == 7): # para revisar como se guarda la informacion 
        opcGR = ""
        print("\nListado de gramaticas regulares cargadas en el sistema: ")
        for k in listGR: #muestro el listado de gramaticas para escoger
            print(" - "+str(k.nombre2))
        
        
        opcGR = input("\nEscriba el nombre de la gramatica que desea escoger: ")
        print("")
        showInfoGR(opcGR)
    
    elif (opc < 1 or opc > 7):
        print("¡Seleccione una opción correcta!")

