
from random import Random


class Campeon:
    """Clase Campeon

        Esta es la clase padre de todas las demas clases dentro del juego.
    """

    def __init__(self):
        pass

    def __init__(self, clase):
        """Constructor

            Args:
            clase (str): Tipo del personaje
        """

        self.clase = clase


class Soporte(Campeon):

    vida = 120
    ulti = "Vida extra"
    habilidad = "Magia negra"
    nombre = str
    clase = str

    def __init__(self):
        super().__init__()

    def __init__(self, nombre, clase):

        self.nombre = nombre
        self.clase = clase

        super().__init__(clase)

    def getVida(self):

        return self.vida

    def atacar(self):

        puntosDano = 20

        print(f"{str(self.nombre).upper()} ataca con su {str(self.habilidad).upper()}")

        return puntosDano

    def defenderse(self, puntosDano):

        print(
            f"{str(self.nombre).upper()} se cubre del ataque y recibe la mitad del daño esperado.")

        puntosDano = int(puntosDano/2)

        return self.recibirDano(puntosDano)

    def usarUlti(self):

        curacion = 40

        print(
            f"{str(self.nombre).upper()} utiliza su ultimate {str(self.ulti).upper()} para curarse {curacion} puntos de vida. ")

        self.vida = int(self.vida + curacion)

        if self.vida > 100:

            self.vida = 100

        return self.getVida()

    def recibirDano(self, puntosDano):

        self.vida = int(self.vida - puntosDano)

        print(
            f"La vida de {str(self.nombre).upper()} se reduce en {puntosDano} puntos.")

        if self.vida < 0:

            self.vida = 0

        return self.getVida()


class Ataque(Campeon):

    vida = 150
    ulti = "Tormenta de lava"
    habilidad = "Golpe ardiente"
    nombre = str
    clase = str

    def __init__(self):
        super().__init__()

    def __init__(self, nombre, clase):

        self.nombre = nombre
        self.clase = clase

        super().__init__(clase)

    # Muestra la vida del personaje
    def getVida(self):

        return self.vida

    # Hace daño
    def atacar(self):

        puntosDano = 25

        print(f"{str(self.nombre).upper()} ataca con su {str(self.habilidad).upper()}")

        return puntosDano

    # Recibe daño
    def defenderse(self, puntosDano):

        print(
            f"{str(self.nombre).upper()} se cubre del ataque y recibe la mitad del daño esperado.")

        puntosDano = int(puntosDano/2)

        return self.recibirDano(puntosDano)

    # Hace daño
    def usarUlti(self):

        puntosDano = 50

        print(f"{str(self.nombre).upper()} utiliza su ultimate {str(self.ulti).upper()} que resta {puntosDano} puntos de vida al enemigo. ")

        return puntosDano

    # Recibe daño
    def recibirDano(self, puntosDano):

        self.vida = int(self.vida - puntosDano)

        print(
            f"La vida de {str(self.nombre).upper()} se reduce en {puntosDano} puntos.")

        if self.vida < 0:

            self.vida = 0

        return self.getVida()


class Flanco(Campeon):

    vida = 100
    ulti = "Furia del emperador"
    habilidad = "Corte profundo"
    nombre = str
    clase = str

    def __init__(self):
        super().__init__()

    def __init__(self, nombre, clase):

        self.nombre = nombre
        self.clase = clase

        super().__init__(clase)

    # Muestra la vida del personaje
    def getVida(self):

        return self.vida

    # Hace daño
    def atacar(self):

        puntosDano = 30

        print(f"{str(self.nombre).upper()} ataca con su {str(self.habilidad).upper()}")

        return puntosDano

    # Recibe daño
    def defenderse(self, puntosDano):

        print(
            f"{str(self.nombre).upper()} se cubre del ataque y recibe la mitad del daño esperado.")

        puntosDano = int(puntosDano/2)

        return self.recibirDano(puntosDano)

    # Hace daño
    def usarUlti(self):

        puntosDano = 60

        print(f"{str(self.nombre).upper()} utiliza su ultimate {str(self.ulti).upper()} que resta {puntosDano} puntos de vida al enemigo. ")

        return puntosDano

    # Recibe daño
    def recibirDano(self, puntosDano):

        self.vida = int(self.vida - puntosDano)

        print(
            f"La vida de {str(self.nombre).upper()} se reduce en {puntosDano} puntos.")

        if self.vida < 0:

            self.vida = 0

        return self.getVida()


class Tanque(Campeon):

    vida = 200
    ulti = "Cañon destructivo"
    habilidad = "Golpe bajo"
    nombre = str
    clase = str

    def __init__(self):
        super().__init__()

    def __init__(self, nombre, clase):

        self.nombre = nombre
        self.clase = clase

        super().__init__(clase)

    # Muestra la vida del personaje
    def getVida(self):

        return self.vida

    # Hace daño
    def atacar(self):

        puntosDano = 10

        print(f"{str(self.nombre).upper()} ataca con su {str(self.habilidad).upper()}")

        return puntosDano

    # Recibe daño
    def defenderse(self, puntosDano):

        print(
            f"{str(self.nombre).upper()} se cubre del ataque y recibe la mitad del daño esperado.")

        puntosDano = int(puntosDano/2)

        return self.recibirDano(puntosDano)

    # Hace daño
    def usarUlti(self):

        puntosDano = 50

        print(f"{str(self.nombre).upper()} utiliza su ultimate {str(self.ulti).upper()} que resta {puntosDano} puntos de vida al enemigo. ")

        return puntosDano

    # Recibe daño
    def recibirDano(self, puntosDano):

        self.vida = int(self.vida - puntosDano)

        print(
            f"La vida de {str(self.nombre).upper()} se reduce en {puntosDano} puntos.")

        if self.vida < 0:

            self.vida = 0

        return self.getVida()


class Campeones:

    campeones = []
    campeonesSeleccionados = []

    def __init__(self):
        pass

    def agregarCampeon(self, campeon):

        self.campeones.append(campeon)

    def printCampeones(self):

        campeon = False

        if len(self.campeones) >= 2:

            for campeon in self.campeones:
                print(f"= {campeon.nombre}")

        return campeon

    def getCantidadCampeones(self):

        cantidad = len(self.campeones)

        return cantidad

    def buscarCampeon(self, encontrar):

        campeonEncontrado = False

        for campeon in self.campeones:

            if encontrar == campeon.nombre.upper():

                campeonEncontrado = campeon

        return campeonEncontrado

    # Metodos de campeones seleccionados
    # setters

    def setCampeonSeleccionado(self, campeonSeleccionado):

        self.campeonesSeleccionados.insert(0, campeonSeleccionado)

    def setCampeonEnemigoSeleccionado(self, campeonEnemigoSeleccionado):

        self.campeonesSeleccionados.insert(1, campeonEnemigoSeleccionado)

    # getters

    def getCampeonSeleccionado(self):
        """getCampeonSeleccionado

            Args:
            self (self): nada

            return: Campeon
        """

        selec = self.campeonesSeleccionados[0]

        return selec

    def getCampeonEnemigoSeleccionado(self):

        selec = self.campeonesSeleccionados[1]

        return selec


class Menu:

    # Imprimir menu principal
    def principal():
        """Principal

            1- CREAR PERSONAJE 2- ENFRENTAMIENTOS 3-SALIR
        """

        print("----------------------"
              "\nALBION OFFLINE"
              "\n----------------------"
              "\n1- Crear personaje"
              "\n2- Enfrentamientos"
              "\n3- Salir"
              "\n----------------------")

    def seleccionarNombre():

        print("---------------------------------------"
              "\nSelecciona el nombre de tu personaje"
              "\n---------------------------------------")

    def seleccionarClase():

        print("---------------------------------------"
              "\nSeleccione la clase de su personaje"
              "\n---------------------------------------"
              "\n1- Soporte"
              "\n2- Ataque"
              "\n3- Flanco"
              "\n4- Tanque"
              "\n----------------------")

    def programaFinalizado():

        print("-----------------------"
              "\nPrograma finalizado"
              "\n-----------------------")

    def otraOperacion():
        """otraOperacion

            Desea realizar otra operacion? 1-SI 2-NO
        """

        print("--------------------------------"
              "\nDesea realizar otra operacion?"
              "\n--------------------------------"
              "\n1- Si"
              "\n2- No"
              "\n--------------------------------")

    def opcionInvalida():

        print("----------------------------------------------------"
              "\nEsta opcion no es valida, seleccione nuevamnete."
              "\n----------------------------------------------------")

    def comienzanLosEnfrentamientos():

        campeones = Campeones()

        campeon = campeones.getCampeonSeleccionado()
        enemigo = campeones.getCampeonEnemigoSeleccionado()

        print("--------------------------------"
              "\nComienzan los enfrentamientos"
              "\n--------------------------------"

              # DETALLES CAMPEON
              f"\n{campeon.nombre.upper()}"
              f"\nCLASE: {campeon.clase.upper()}"
              f"\nHP: {campeon.getVida()}"
              f"\nHABILIDAD: {campeon.habilidad.upper()}"
              f"\nULTI: {campeon.ulti.upper()}"

              "\n--------------------------------"
              # DETALLES ENEMIGO
              f"\n{enemigo.nombre.upper()}"
              f"\nCLASE: {enemigo.clase.upper()}"
              f"\nHP: {enemigo.getVida()}"
              f"\nHABILIDAD: {enemigo.habilidad.upper()}"
              f"\nULTI: {enemigo.ulti.upper()}"

              "\n--------------------------------"
              # MENU DE OPCIONES
              "\n1- Ataque comun"
              "\n2- Defensa"
              "\n3- Ultimate"
              "\n4- Rendirse"
              "\n--------------------------------")


class Funcion:

    campeones = Campeones()

    def __init__(self):
        pass

    def crearPersonaje(self):

        print("-----------------------"
              "\nCrear personaje "
              "\n-----------------------")

        Menu.seleccionarNombre()
        nombre = input("Ingresa el nombre: ")

        Menu.seleccionarClase()
        opcion = Opcion.seleccionar()

        if opcion == 1:
            campeon = Soporte(nombre, "Soporte")
            self.campeones.agregarCampeon(campeon)

        elif opcion == 2:
            campeon = Ataque(nombre, "Ataque")
            self.campeones.agregarCampeon(campeon)

        elif opcion == 3:
            campeon = Flanco(nombre, "Flanco")
            self.campeones.agregarCampeon(campeon)

        elif opcion == 4:
            campeon = Tanque(nombre, "Tanque")
            self.campeones.agregarCampeon(campeon)

        else:
            campeon = False

        return campeon

    def seleccionarCampeon():

        print("-----------------------"
              "\nSelecciona tu campeon"
              "\n-----------------------")

        campeones = Campeones()
        campeon = campeones.printCampeones()

        print("-----------------------")

        opcionesList = [False, False]

        if campeon != False:

            opcion = input("Ingresa el nombre de tu campeon: ")

            campeonSeleccionado = campeones.buscarCampeon(opcion.upper())

            if campeonSeleccionado != False:

                print("--------------------------------------------------"
                      f"\n{opcion.upper()} ha sido seleccionado correctamente."
                      "\n--------------------------------------------------")

                opcionesList = [False, True]
                campeones.setCampeonSeleccionado(campeonSeleccionado)

            else:
                print(
                    f"{opcion.upper()} no coincide con ningun campeon de la lista.")

        return opcionesList

    def seleccionarEnemigo():

        print("-------------------------------"
              "\nSelecciona el campeon enemigo"
              "\n-------------------------------")

        campeones = Campeones()
        campeon = campeones.printCampeones()

        print("-------------------------------")

        opcionesList = [False, False]

        if campeon != False:

            opcion = input("Ingresa el nombre de tu campeon enemigo: ")

            campeonSeleccionado = campeones.buscarCampeon(opcion.upper())

            if campeonSeleccionado != False:

                print("--------------------------------------------------"
                      f"\n{opcion.upper()} ha sido seleccionado correctamente."
                      "\n--------------------------------------------------")

                opcionesList = [False, True]
                campeones.setCampeonEnemigoSeleccionado(campeonSeleccionado)

            else:
                print(
                    f"{opcion.upper()} no coincide con ningun campeon de la lista.")

        return opcionesList

    def enfrentarse(self):

        campeon = self.campeones.getCampeonSeleccionado()
        enemigo = self.campeones.getCampeonEnemigoSeleccionado()
        random = Random()

        salir = False
        opcion = -1

        defensaActivada = False
        defensaEnemigoActivada = False

        while salir == False:

            if campeon.getVida() <= 0:

                print("---------------------------"
                      "\nHas perdido el combate!"
                      "\n---------------------------")

                break

            elif enemigo.getVida() <= 0:

                print("---------------------------"
                      "\nHas ganado el combate!"
                      "\n---------------------------")

                break

            else:

                # OPCIONES PARA USUARIO
                # Comprobamos que la opcion sea una opcion correcta
                while opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4 or opcion == -1:

                    # Comprobamos si es la primera vez que ingresa o esta corrigiendo el valor incorrecto que ingreso anteriormente

                    Menu.comienzanLosEnfrentamientos()
                    opcion = Opcion.seleccionar()

                    # Opcion 1 = Ataque comun
                    if opcion == 1:
                        puntosDano = campeon.atacar()

                        if defensaEnemigoActivada == True:

                            enemigo.defenderse(puntosDano)
                            defensaEnemigoActivada = False

                        else:

                            enemigo.recibirDano(puntosDano)

                        opcion = -1

                        break

                    # Opcion 2 = Defensa
                    elif opcion == 2:

                        defensaActivada = True

                        print("---------------------------------------------------"
                              "\nTu campeon se defendera en cuanto reciba un ataque."
                              "\n---------------------------------------------------")

                        opcion = -1
                        break

                    # Opcion 3 = Ultimate
                    elif opcion == 3:

                        if campeon.clase.upper() == "SOPORTE":
                            campeon.usarUlti()

                        else:

                            puntosDano = campeon.usarUlti()

                            if defensaEnemigoActivada == True:

                                enemigo.defenderse(puntosDano)
                                defensaEnemigoActivada = False
                            else:

                                enemigo.recibirDano(puntosDano)

                        opcion = -1
                        break

                    # Opcion 4 = Salir
                    elif opcion == 4:

                        print("---------------------------------------"
                              "\nSaliendo del modo enfrentamiento..."
                              "\n---------------------------------------")

                        salir = True
                        opcion = -1
                        break

                else:

                    Menu.opcionInvalida()
                    opcion = Opcion.seleccionarValida()
                    break

                # OPCIONES PARA ENEMIGO (ALEATORIAS)

                opcionEnemigo = random.randint(1, 3)

                # Opcion 1 = Ataque comun
                if opcionEnemigo == 1:
                    puntosDano = enemigo.atacar()

                    if defensaActivada == True:

                        campeon.defenderse(puntosDano)
                        defensaActivada = False
                    else:

                        campeon.recibirDano(puntosDano)

                # Opcion 2 = Defensa
                elif opcionEnemigo == 2:

                    defensaEnemigoActivada = True

                    print("El enemigo se defendera en cuanto reciba un ataque.")

                # Opcion 3 = Ultimate
                elif opcionEnemigo == 3:

                    if enemigo.clase.upper() == "SOPORTE":

                        enemigo.usarUlti()

                    else:

                        puntosDano = enemigo.usarUlti()

                        if defensaActivada == True:

                            campeon.defenderse(puntosDano)
                        else:

                            campeon.recibirDano(puntosDano)


class Opcion:

    def seleccionar():
        """Seleccionar

            Realiza un input solicitando una opcion imprimendo
            "Selecciona una opcion: "
        """

        opcion = int(input("Selecciona una opcion: "))

        return opcion

    def seleccionarValida():
        """SeleccionarValida

            Realiza un input solicitando una opcion valida imprimendo
            "Selecciona una opcion valida: "
        """

        opcion = int(input("Selecciona una opcion valida: "))

        return opcion


class main:

    salir = False
    opcion = -1

    funcion = Funcion()
    campeones = Campeones()

    while salir == False:

        # Comprobamos que la opcion sea una opcion correcta
        while opcion == 1 or opcion == 2 or opcion == 3 or opcion == -1:

            # Comprobamos si es la primera vez que ingresa o esta corrigiendo el valor incorrecto que ingreso anteriormente
            if opcion != 1 and opcion != 2 and opcion != 3:
                Menu.principal()
                opcion = Opcion.seleccionar()

            # Opcion 1 = Crear personaje
            if opcion == 1:
                campeon = funcion.crearPersonaje()

                if campeon != False:
                    print("----------------------------------------------------------"
                          f"\n{campeon.nombre.upper()} de la clase {str(campeon.clase).upper()} ha sido creado correctamente."
                          "\n----------------------------------------------------------")

                else:
                    print("---------------------------------------------------------"
                          "\nEl personaje no pudo ser creado. Intente nuevamente."
                          "\n---------------------------------------------------------")
                    opcion = 1
                    break

                Menu.otraOperacion()
                opcionInterna = Opcion.seleccionar()

                while opcionInterna != 1 and opcionInterna != 2:

                    print("--------------------------------------"
                          "\nLa opcion seleccionada es incorrecta."
                          "\n--------------------------------------")
                    opcionInterna = Opcion.seleccionarValida()

                if opcionInterna == 1:
                    opcion = -1
                else:
                    opcion = 3

            # Opcion 2 = Enfrentamientos
            elif opcion == 2:

                # Seleccionamos nuestro campeon
                campeonSeleccionado = Funcion.seleccionarCampeon()

                camp1 = campeonSeleccionado[0]
                camp2 = campeonSeleccionado[1]

                # Validador de seleccion
                if camp1 == False and camp2 == False:

                    print("-----------------------------------------------------------------"
                          "\nNo existen campeones o no son suficientes. Cree mas campeones."
                          "\n-----------------------------------------------------------------")
                    opcion = 1
                    break

                # Seleccionamos el enemigo
                campeonEnemigo = Funcion.seleccionarEnemigo()

                camp1 = campeonSeleccionado[0]
                camp2 = campeonSeleccionado[1]

                # Validador de seleccion
                if camp1 == False and camp2 == False:

                    print("-----------------------------------------------------------------"
                          "\nNo existen campeones o no son suficientes. Cree mas campeones."
                          "\n-----------------------------------------------------------------")
                    opcion = 1
                    break

                print("---------------------------------------------------------------------------------------"
                      f"\nTu campeon es {campeones.getCampeonSeleccionado().nombre.upper()} de clase "
                      f"{campeones.getCampeonSeleccionado().clase.upper()} y tu enemigo es "
                      f"{campeones.getCampeonEnemigoSeleccionado().nombre.upper()} de clase "
                      f"{campeones.getCampeonEnemigoSeleccionado().clase.upper()}"
                      "\n---------------------------------------------------------------------------------------")

                # Comienzan los enfrentamientos
                funcion.enfrentarse()

                Menu.otraOperacion()
                opcionInterna = Opcion.seleccionar()

                while opcionInterna != 1 and opcionInterna != 2:

                    print("--------------------------------------"
                          "\nLa opcion seleccionada es incorrecta."
                          "\n--------------------------------------")
                    opcionInterna = Opcion.seleccionarValida()

                if opcionInterna == 1:
                    opcion = -1
                else:
                    opcion = 3

            # Opcion 3 = Salir
            elif opcion == 3:
                Menu.programaFinalizado()

                salir = True
                break
        else:

            Menu.opcionInvalida()
            opcion = Opcion.seleccionarValida()
