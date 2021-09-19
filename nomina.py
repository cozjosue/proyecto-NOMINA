import abc
from componentes import Menu,Valida
from componentes import*
from helpers import borrarPantalla,gotoxy
from crudArhivos import Archivo
from entidadesRol import *
from datetime import date
import time
def empAdministrativos():
    borrarPantalla()
    gotoxy(20,2);print("MANTENIMIENTO DE EMPLEADOS ADMINISTRATIVOS")
    gotoxy(15,4);print("Id: ")
    gotoxy(15,5);print("Nombre Empleado: ")
    gotoxy(15,6);print("Departamento: ")
    gotoxy(15,7);print("Cargo: ")
    gotoxy(15,8);print("Direccion: ")
    gotoxy(15,9);print("Cedula: ")
    gotoxy(15,10);print("Telefono: ")
    gotoxy(15,11);print("Fecha Ingreso: ")
    gotoxy(15,12);print("Sueldo: ")
    validar=Valida()
    nomEMp = validar.solo_letrass("Solo Letras",33,5)
    archiDep = Archivo('./archivos/departamento.txt','|')
    departamentos = archiDep.leer()  
    codep = None
    y=True
    while y:
        gotoxy(33,6);print('               ')
        gotoxy(33,6);Dep = input()
        for i in departamentos:
            if i[1].lower() == Dep.lower():
                codep = i  
                y=False
            else:
                gotoxy(70,6);print('Departamento no valido vuelva a ingresar!') 
    gotoxy(70,6);print('                                                      ')
    departamento = Departamento(codep[1],codep[0])
    archiCargo = Archivo("./archivos/cargo.txt","|")
    cargos = archiCargo.leer()
    codcar = None
    c=True
    while c:
        gotoxy(33,7);print('               ')
        gotoxy(33,7);Car = input()
        for i in cargos:
            if i[1].lower() == Car.lower():
                codcar = i  
                c=False
            else:
                gotoxy(70,7);print('Cargo no valido vuelva a ingresar!') 
    gotoxy(70,7);print('                                                      ')              
    cargoss = Cargo(codcar[1],codcar[0])
    gotoxy(33,8);Dir = input()
    Ced=validar.telefono("Solo números",33,9)
    Tel=validar.telefono("Solo números",33,10)
    Fec = validar.fechas("Solo números",33,11)
    Sue = validar.solo_numeros("Solo números",33,12)
    borrarPantalla()
    gotoxy(15,7);print("Esta seguro de Resgistrar este Empleado(s/n):")
    gotoxy(61,7);grabar = input().lower()
    if grabar == 's':
        archiEmpAd = Archivo('./archivos/administrativo.txt','|')
        la = archiEmpAd.leer()
        if la :idSig=int(la[-1][0][1])+1
        else:idSig=1
        ac = 'A'+str(idSig)
        adm = Administrativo(nomEMp,departamento,cargoss,Dir,Ced,Tel,Fec,Sue,ac)
        datos=adm.getEmpleado()
        datos = '|'.join(datos)
        archiEmpAd.escribir([datos],'a')
        gotoxy(10,10);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
    else:
        gotoxy(17,8);input("Empleado No Registrado\n presione una tecla para continuar...")
def empObreros():
    borrarPantalla()
    gotoxy(20,2);print("MANTENIMIENTO DE EMPLEADOS OBREROS")
    gotoxy(15,4);print("Id: ")
    gotoxy(15,5);print("Nombre Empleado: ")
    gotoxy(15,6);print("Departamento: ")
    gotoxy(15,7);print("Cargo: ")
    gotoxy(15,8);print("Direccion: ")
    gotoxy(15,9);print("Cedula: ")
    gotoxy(15,10);print("Telefono: ")
    gotoxy(15,11);print("Fecha Ingreso: ")
    gotoxy(15,12);print("Sueldo: ")
    validar=Valida()
    nomEMp = validar.solo_letrass("Solo Letras",33,5)
    archiDep = Archivo('./archivos/departamento.txt','|')
    departamentos = archiDep.leer()  
    codep = None
    y=True
    while y:
        gotoxy(33,6);print('               ')
        gotoxy(33,6);Dep = input()
        for i in departamentos:
            if i[1].lower() == Dep.lower():
                codep = i  
                y=False
            else:
                gotoxy(70,6);print('Departamento no valido vuelva a ingresar!') 
    gotoxy(70,6);print('                                                      ')
    departamento = Departamento(codep[1],codep[0])
    archiCargo = Archivo("./archivos/cargo.txt","|")
    cargos = archiCargo.leer()
    codcar = None
    c=True
    while c:
        gotoxy(33,7);print('               ')
        gotoxy(33,7);Car = input()
        for i in cargos:
            if i[1].lower() == Car.lower():
                codcar = i  
                c=False
            else:
                gotoxy(70,7);print('Cargo no valido vuelva a ingresar!') 
    gotoxy(70,7);print('                                                      ')              
    cargoss = Cargo(codcar[1],codcar[0])
    gotoxy(33,8);Dir = input()
    Ced=validar.telefono("Solo números",33,9)
    Tel=validar.telefono("Solo números",33,10)
    Fec = validar.fechas("Solo números",33,11)
    Sue = validar.solo_numeros("Solo números",33,12)  
    borrarPantalla()
    gotoxy(15,7);print("Esta seguro de Resgistrar este Empleado(s/n):")
    gotoxy(61,7);grabar = input().lower()
    if grabar == 's':
        archiEmpO = Archivo('./archivos/obrero.txt','|')
        la = archiEmpO.leer()
        if la :idSig=int(la[-1][0][1])+1
        else:idSig=1
        ac = 'O'+str(idSig)
        ob = Obrero(nomEMp,departamento,cargoss,Dir,Ced,Tel,Fec,Sue,ac)
        datos=ob.getEmpleado()
        datos = '|'.join(datos)
        archiEmpO.escribir([datos],'a')
        gotoxy(10,10);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
    else:
        gotoxy(17,8);input("Empleado No Registrado\n presione una tecla para continuar...")
def empresas():
    borrarPantalla()     
    gotoxy(20,2);print("Mantenimiento de la empresa: ")
    gotoxy(15,4);print("Razón social: ")
    gotoxy(15,5);print("Dirección: ")
    gotoxy(15,6);print("Teléfono: ")
    gotoxy(15,7);print("Ruc: ")
    gotoxy(33,4);razsocial=input().upper()
    gotoxy(33,5);direcc=input().upper()
    validas=Valida()
    telef=validas.telefono("¡Ingresar teléfono válido!",33,6)
    ruc=validas.ruc("¡Ingresar Ruc válido!",33,7)
    archiempresa = Archivo("./archivos/empresa.txt","|")
    empresanueva=Empresa(razsocial,direcc,telef,ruc)
    datos = empresanueva.getEmpresa()
    datos = '|'.join(datos)
    archiempresa.escribir([datos],"a")    
def cargos():
   borrarPantalla()     
   gotoxy(20,2);print("MANTENIMIENTO DE CARGOS")
   gotoxy(15,4);print("Codigo: ")
   gotoxy(15,5);print("Descripcion Cargo: ")
   validar=Valida()
   desCargo = validar.solo_letrass("Solo letras",35,5)
   archiCargo = Archivo("./archivos/cargo.txt","|")
   cargos = archiCargo.leer()
   if cargos : idSig = int(cargos[-1][0])+1
   else: idSig=1
   cargo = Cargo(desCargo,idSig)
   datos = cargo.getCargo()
   datos = '|'.join(datos)
   archiCargo.escribir([datos],"a")  
def departamentos():
    borrarPantalla()     
    gotoxy(20,2);print("MANTENIMIENTO DE Departamentos")
    gotoxy(15,4);print("Codigo:")
    gotoxy(15,5);print("Descripcion de partamento: ")
    validar=Valida()
    desDepartameno = validar.solo_letrass("Solo lestras",45,5)
    archiDepar = Archivo("./archivos/departamento.txt","|")
    departamentos = archiDepar.leer()
    if departamentos : idSig = int(departamentos[-1][0])+1
    else: idSig=1
    departamento = Departamento(desDepartameno,idSig)
    datos = departamento.getDepartamento()
    datos = '|'.join(datos)
    archiDepar.escribir([datos],"a")  
# Opciones del Menu Novedades
def sobretiempos():
   borrarPantalla()     
   gotoxy(20,2);print("INGRESO DE HORAS EXTRAS")
   empleado,entEmpleado = [],None
   aamm,h50,h100=0,0,0
   while not empleado:
      gotoxy(15,5);print("Empleado ID[   ]: ")
      gotoxy(28,5);id = input().upper()
      archiEmpleado = Archivo("./archivos/obrero.txt","|")
      empleado = archiEmpleado.buscar(id)
      if empleado:
          entEmpleado = Obrero(empleado[1],empleado[2],empleado[3],empleado[4],empleado[5],empleado[6],empleado[7],empleado[8],empleado[0]) 
          gotoxy(35,5);print(entEmpleado.nombre)
      else: 
         gotoxy(27,5);print("No existe Empleado con ese codigo[{}]:".format(id))
         time.sleep(2);gotoxy(27,5);print(" "*40) 
   gotoxy(15,6);print("Periodo:[aaaamm]")
   gotoxy(15,7);print("Horas50:")
   gotoxy(15,8);print("Horas100:")
   validar = Valida()
   aamm=validar.periodo("Ingresar peíodo válido",24,6)
   h50 = validar.solo_numeros("Solo números",23,7)
   h100 = validar.solo_numeros("Solo números",24,8)
   gotoxy(15,9);print("Esta seguro de Grabar El registro(s/n):")
   gotoxy(54,9);grabar = input().lower()
   if grabar == "s":
        archiSobretiempo = Archivo("./archivos/sobretiempo.txt","|")
        sobretiempos = archiSobretiempo.leer()
        if sobretiempos : idSig = int(sobretiempos[-1][0])+1
        else: idSig=1
        sobretiempo = Sobretiempo(entEmpleado,aamm,h50,h100,True,idSig)
        datos = sobretiempo.getSobretiempo()
        datos = '|'.join(datos)
        archiSobretiempo.escribir([datos],"a")                 
        gotoxy(10,10);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
   else:
       gotoxy(10,10);input("Registro No fue Grabado\n presione una tecla para continuar...")     
def prestamos():
    borrarPantalla()
    gotoxy(20,2);print('PRESTAMOS')
    empleado,entEmpleado = [],None
    aamm , valor , numpagos = 0,0,0
    gotoxy(15,4);print("Obrero-Administrativo(O/A): ")
    gotoxy(44,4);rol=input().lower()
    while not empleado:     
        gotoxy(15,6);print('Empleado ID[   ]:')
        if rol == 'o':
            archiEmpleado = Archivo('./archivos/obrero.txt','|')
            gotoxy(28,6);id=input().upper()
            empleado=archiEmpleado.buscar(id)
            if empleado:
                entEmpleado =Obrero(empleado[1],empleado[2],empleado[3],empleado[4],empleado[5],empleado[6],empleado[7],empleado[8],empleado[0])
                gotoxy(35,6);print(entEmpleado.nombre)
                gotoxy(15,7);print('Periodo[aaaamm]')
                gotoxy(15,8);print('Valor:')
                gotoxy(15,9);print('Num Pagos:')
                gotoxy(15,10);print('Saldo:')
                validar = Valida()
                aamm = validar.periodo('Error solo numeros',23,7)
                valor = validar.solo_numeros('Error solo numeros',21,8)
                npagos= validar.solo_numeros('Error solo numeros',25,9)
                saldo = validar.solo_numeros('Error solo numeros',21,10)
                gotoxy(15,11);print('Esta Seguro de guardar el prestamo (s/n):')
                gotoxy(57,11);grabar=input().lower()
                if grabar == 's':
                    archiPrestamo = Archivo('./archivos/prestamo.txt','|')
                    prestamo = archiPrestamo.leer()
                    if prestamo :idSig=int(prestamo[-1][0])+1
                    else:idSig=1
                    prestamos = Prestamo(entEmpleado,aamm,valor,npagos,saldo,True,idSig)
                    datos = prestamos.getPrestamo()
                    datos = '|'.join(datos)
                    archiPrestamo.escribir([datos],'a')
                    gotoxy(10,12);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
                else:
                    gotoxy(10,12);input("Registro No fue Grabado\n presione una tecla para continuar...")
            else:
                gotoxy(27,6);print("No existe Empleado con ese codigo[{}]:".format(id))
                time.sleep(2);gotoxy(27,6);print(" "*40)
        else:
            archiEmpleado = Archivo('./archivos/administrativo.txt','|')
            gotoxy(27,6);id=input().upper()
            empleado=archiEmpleado.buscar(id)
            if empleado:
                entEmpleado =Administrativo(empleado[1],empleado[2],empleado[3],empleado[4],empleado[5],empleado[6],empleado[7],empleado[8],empleado[0])
                gotoxy(35,6);print(entEmpleado.nombre)
                gotoxy(15,7);print('Periodo[aaaamm]')
                gotoxy(15,8);print('Valor:')
                gotoxy(15,9);print('Num Pagos:')
                gotoxy(15,10);print('Saldo:')
                validar = Valida()
                aamm = validar.solo_numeros('Error solo numeros',23,7)
                valor = validar.solo_numeros('Error solo numeros',21,8)
                npagos= validar.solo_numeros('Error solo numeros',25,9)
                saldo = validar.solo_numeros('Error solo numeros',21,10)
                gotoxy(15,11);print('Esta Seguro de guardar el prestamo (s/n):')
                gotoxy(57,11);grabar=input().lower()
                if grabar == 's':
                    archiPrestamo = Archivo('./archivos/prestamo.txt','|')
                    prestamo = archiPrestamo.leer()
                    if prestamo :idSig=int(prestamo[-1][0])+1
                    else:idSig=1
                    prestamos = Prestamo(entEmpleado,aamm,valor,npagos,saldo,True,idSig)
                    datos = prestamos.getPrestamo()
                    datos = '|'.join(datos)
                    archiPrestamo.escribir([datos],'a')
                    gotoxy(10,12);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
                else:
                    gotoxy(10,12);input("Registro No fue Grabado\n presione una tecla para continuar...")
            else:
                gotoxy(27,6);print("No existe Empleado con ese codigo[{}]:".format(id))
                time.sleep(2);gotoxy(27,6);print(" "*40)
# opciones de Rol de Pago
def rolAdministrativo():
   borrarPantalla()
   # Se ingresa los datos del rol a procesar     
   gotoxy(20,2);print("ROL ADMINISTRATIVO")
   aamm=0
   gotoxy(15,6);print("Periodo[aaaamm]")
   validar = Valida()
   aamm=validar.periodo("Error: Solo numeros",23,6)
   gotoxy(15,7);print("Esta seguro de Procesar el Rol(s/n):")
   gotoxy(54,7);grabar = input().lower()
   entEmpAdm = None
   # Se procesa el rol con la confirmacion del usuario
   if grabar == "s":
        # Obtener lista de empleados a procesar el rol
        archiEmp = Archivo("./archivos/administrativo.txt","|")
        ListaEmpAdm = archiEmp.leer()
        if ListaEmpAdm : 
            archiEmpresa = Archivo("./archivos/empresa.txt","|")
            empresa = archiEmpresa.leer()[0]
            entEmpresa = Empresa(empresa[0],empresa[1],empresa[2],empresa[3])
            archiDeducciones = Archivo("./archivos/deducciones.txt","|")
            deducciones = archiDeducciones.leer()[0]
            entDeduccion = Deduccion(float(deducciones[0]),float(deducciones[1]),float(deducciones[2]))
            #print(entDeduccion.getIess(),entDeduccion.getComision(),entDeduccion.getAntiguedad())
            nomina = Nomina(date.today(),aamm)
            for empleado in ListaEmpAdm:
              #print(empleado)
              entEmpAdm = Administrativo(empleado[1],empleado[2],empleado[3],empleado[4],empleado[5],empleado[6],empleado[7],float(empleado[8]),empleado[0]) 
              #print(entEmpAdm.nombre,entEmpAdm.sueldo)
              nomina.calcularNominaDetalle(entEmpAdm,entDeduccion)
            # grabar cabecera del rol
            datosCab = nomina.getNomina()
            datosCab = '|'.join(datosCab)
            archiRol = Archivo("./archivos/rolCabAdm.txt","|")
            archiRol.escribir([datosCab],"a")
            # grabar detalle del rol
            archiDet = Archivo("./archivos/rolDetAdm.txt","|")
            datosDet = nomina.getDetalle()
            # se graba en el detalle empleado por empleado           
            for dt in datosDet:
                dt = nomina.aamm+'|'+'|'.join(dt)
                archiDet.escribir([dt],"a")
            # imprimir rol
          
            nomina.mostrarCabeceraNomina(entEmpresa.razonSocial,entEmpresa.direccion,entEmpresa.telefono,entEmpresa.ruc,"A D M I N I S T R A T I V O")
            nomina.mostrarDetalleNomina()
   else:
       gotoxy(10,10);input("Rol No fue Procesado\n presione una tecla para continuar...")     

   input("               Presione una tecla continuar...")  
def consultaRol():
   borrarPantalla()
   validar = Valida()
   # Se ingresa los datos del rol a Consultar     
   gotoxy(20,2);print("CONSULTA DE ROL OBRERO - ADMINISTRATIVO")
   rol=0
   aamm=""
   gotoxy(15,4);print("Obrero-Administrativo(O/A): ")
   gotoxy(15,6);print("Periodo[aaaamm]")
   gotoxy(44,4)
   rol=input().upper()
   aamm=validar.periodo("Error: Solo numeros",23,6)
   gotoxy(15,7);print("Esta seguro de consultar el Rol(s/n):")
   gotoxy(54,7);procesar = input().lower()
   if procesar == "s":
        if rol == "A": 
            tit = "A D M I N I S T R A T I V O"
            archiRolCab = Archivo("./archivos/rolCabAdm.txt","|")
            archiRolDet = Archivo("./archivos/rolDetAdm.txt","|")
        else: 
            tit = "O B R E R O"
            archiRolCab = Archivo("./archivos/rolCabObr.txt","|")
            archiRolDet = Archivo("./archivos/rolDetObr.txt","|")
        cabrol = archiRolCab.buscar(aamm)
        if cabrol:
            entCabRol = Nomina(cabrol[1],cabrol[0])
            entCabRol.totIngresos=float(cabrol[2])
            entCabRol.totDescuentos=float(cabrol[3])
            entCabRol.totPagoNeto=float(cabrol[4])
            detalle= archiRolDet.buscarLista(aamm)
            for det in detalle:
                entCabRol.detalleNomina.append(det[1:])    
            archiEmpresa = Archivo("./archivos/empresa.txt","|")
            empresa = archiEmpresa.leer()[0]
            entEmpresa = Empresa(empresa[0],empresa[1],empresa[2],empresa[3])
            entCabRol.mostrarCabeceraNomina(entEmpresa.razonSocial,entEmpresa.direccion,entEmpresa.telefono,entEmpresa.ruc,tit)
            entCabRol.mostrarDetalleNomina()
        else:
            gotoxy(10,10);input("No existe rol con ese periodo\n presione una tecla para continuar...")               
   else:
       gotoxy(10,10);input("Consulta Cancelada\n presione una tecla para continuar...")     
   input("               Presione una tecla continuar...")  
def rolObrero():
   borrarPantalla()
   # Se ingresa los datos del rol a procesar     
   gotoxy(20,2);print("ROL OBRERO")
   aamm=0
   gotoxy(15,6);print("Periodo[aaaamm]")
   validar = Valida()
   aamm=validar.periodo("Error: Solo numeros",23,6)
   gotoxy(15,7);print("Esta seguro de Procesar el Rol(s/n):")
   gotoxy(54,7);grabar = input().lower()
   entEmpObre = None#Procedo a cambiar esta variable
   # Se procesa el rol con la confirmacion del usuario
   if grabar == "s":
        # Obtener lista de empleados a procesar el rol
        archiEmp = Archivo("./archivos/obrero.txt","|")
        ListaEmpObr = archiEmp.leer()
        if ListaEmpObr : 
            archiEmpresa = Archivo("./archivos/empresa.txt","|")
            empresa = archiEmpresa.leer()[0]
            entEmpresa = Empresa(empresa[0],empresa[1],empresa[2],empresa[3])
            archiDeducciones = Archivo("./archivos/deducciones.txt","|")
            deducciones = archiDeducciones.leer()[0]
            entDeduccion = Deduccion(float(deducciones[0]),float(deducciones[1]),float(deducciones[2]))
            #print(entDeduccion.getIess(),entDeduccion.getComision(),entDeduccion.getAntiguedad())
            nomina = Nomina(date.today(),aamm)
            for empleado in ListaEmpObr:
              #print(empleado)
              entEmpObre = Obrero(empleado[1],empleado[2],empleado[3],empleado[4],empleado[5],empleado[6],empleado[7],float(empleado[8]),empleado[0]) 
              #print(entEmpAdm.nombre,entEmpAdm.sueldo)
              nomina.calcularNominaDetalle(entEmpObre,entDeduccion)
            # grabar cabecera del rol
            datosCab = nomina.getNomina()
            datosCab = '|'.join(datosCab)
            archiRol = Archivo("./archivos/rolCabObr.txt","|")
            archiRol.escribir([datosCab],"a")
            # grabar detalle del rol
            archiDet = Archivo("./archivos/rolDetObr.txt","|")
            datosDet = nomina.getDetalle()
            # se graba en el detalle empleado por empleado           
            for dt in datosDet:
                dt = nomina.aamm+'|'+'|'.join(dt)
                archiDet.escribir([dt],"a")
            # imprimir rol
          
            nomina.mostrarCabeceraNomina(entEmpresa.razonSocial,entEmpresa.direccion,entEmpresa.telefono,entEmpresa.ruc,"O B R E R O S")
            nomina.mostrarDetalleNomina()   
   else:
       gotoxy(10,10);input("Rol No fue Procesado\n presione una tecla para continuar...")     
   input("               Presione una tecla continuar...")            
def parametros():
    borrarPantalla()
    gotoxy(20,2);print('PARAMETROS')
    gotoxy(20,5);print('PARAMETROS ACTUALES')
    archiDeducciones=Archivo('./archivos/deducciones.txt','|')
    deduccion=archiDeducciones.leer()
    gotoxy(20,6);print('IESS: {}  COMISION: {}  ANTIGUEDAD: {}'.format(deduccion[0][0],deduccion[0][1],deduccion[0][2]))
    gotoxy(20,7);print('Desea Actualizar los datos(s/n):')
    gotoxy(53,7);actualizar=input().lower()
    if actualizar == 's':
        validar = Valida()
        gotoxy(20,8);print('IESS:')
        gotoxy(20,9);print('COMISION:')
        gotoxy(20,10);print('ANTIGUEDAD:')
        iess = validar.solo_decimales('Solo decimales',33,8)
        comision = validar.solo_decimales('Solo decimales',33,9)
        antiguedad = validar.solo_decimales('Solo decimales',33,10)
        gotoxy(20,11);print('Desea guardar estos datos(s/n):')
        gotoxy(52,11);grabar=input().lower()
        if grabar == 's':
            deducciones = Deduccion(iess,comision,antiguedad)
            datos = deducciones.getDeduccion()
            datos = '|'.join(datos)
            archiDeducciones.escribir([datos],'w')
            gotoxy(20,13);input("Registro Grabado Satisfactoriamente\n                   Presione una tecla para continuar...")
        else:
            gotoxy(20,13);input("Registro No fue Grabado\n                   Presione una tecla para continuar...")
# Menu Proceso Principal
opc=''
while opc !='4':  
    borrarPantalla()      
    menu = Menu("Menu Principal",["1) Mantenimiento","2) Novedades","3) Rol de Pago","4) Salir"],20,10)
    opc = menu.menu()
    if opc == "1":
        opc1 = ''
        while opc1 !='7':
            borrarPantalla()    
            menu1 = Menu("Menu Mantenimiento",["1) Empleados Administratvos","2) Empleados Obreros","3) Cargos","4) Departamentos","5) Empresa","6) Parametros","7) Salir"],20,10)
            opc1 = menu1.menu()
            if opc1 == "1":
                empAdministrativos()
            elif opc1== "2":
                empObreros()
            elif opc1 == "3":
                cargos()
            elif opc1=="4":
                departamentos()
            elif opc1=="5":
                empresas()
            elif opc1=="6":
                parametros()                    
    elif opc == "2":
            borrarPantalla()
            menu2 = Menu("Menu Novedades",["1) Sobretiempo","2) Prestamos","3) Salir"],20,10)
            opc2 = menu2.menu()
            if opc2 == "1":
                sobretiempos()
            elif opc2 == "2":
                prestamos()
    elif opc == "3":
            borrarPantalla()
            menu3 = Menu("Menu Rol",["1) Rol Administrativos","2) Rol Obreros","3) Consulta Rol","4) Sobre Empleado","5) Salir"],20,10)
            opc3 = menu3.menu()
            if opc3 == "1":
                rolAdministrativo()
            elif opc3 == "2":
                rolObrero()
            elif opc3 == "3":
                consultaRol()
    # elif opc == "4":
    #         borrarPantalla()
    #         menu4 = Menu("Menu Consultas",["1) Empleados","2) Cargos","3) Departamentos","4) Empresa","5) Parametros","6) Salir"],20,10)
    #         opc4 = menu.menu()
    elif opc == "4":
           borrarPantalla()
           print("Gracias por su visita....")
    else:
          print("Opcion no valida") 
input("Presione una tecla para salir")
borrarPantalla()

