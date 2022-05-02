from django.shortcuts import render
from django.http import HttpResponse
from Familia.models import Familia
from django.template import loader
import datetime

def familia(self):
    familia1 = Familia(nombre="Federico", apellido="Pérez",edad=33, nacimiento=datetime.date(1981,8,31))
    familia1.save()
    familia2 = Familia(nombre="María", apellido="Pérez",edad=48, nacimiento=datetime.date(1974,2,10))
    familia2.save()
    familia3 = Familia(nombre="Rosana", apellido="Oliveira",edad=60, nacimiento=datetime.date(1962,6,15))
    familia3.save()
    familia4 = Familia(nombre="Mauricio", apellido="Faustino",edad=65, nacimiento=datetime.date(1957,12,1))
    familia4.save()

    documentoDeTexto = f""" Se han cargado en la BB.DD con éxito los siguientes datos: 
    Primo: {familia1.nombre}, {familia1.apellido} \t edad:{familia1.edad} nacimiento: {familia1.nacimiento}
    Primo: {familia2.nombre}, {familia2.apellido} \t edad:{familia2.edad} nacimiento: {familia2.nacimiento}
    Tía: {familia3.nombre}, {familia3.apellido} \t edad:{familia3.edad} nacimiento: {familia3.nacimiento}
    Tío-Abuelo: {familia4.nombre}, {familia4.apellido} \t edad:{familia4.edad} nacimiento: {familia3.nacimiento}
    """
    listaFamiliar1 = [ familia1.nombre, familia1.apellido,familia1.edad, familia1.nacimiento ]
    listaFamiliar2 = [ familia2.nombre, familia2.apellido,familia2.edad, familia2.nacimiento ]
    listaFamiliar3 = [ familia3.nombre, familia3.apellido,familia3.edad, familia3.nacimiento ]
    listaFamiliar4 = [ familia4.nombre, familia4.apellido,familia4.edad, familia4.nacimiento ]
    
    listaFamiliares = [listaFamiliar1, listaFamiliar2, listaFamiliar3, listaFamiliar4]

    diccionario = { 
        "familia": listaFamiliares,
        "documento":documentoDeTexto
    }

    plantilla = loader.get_template("plantilla1.html")

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)