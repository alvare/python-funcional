#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from pymonad.Either import Right, Left
from pymonad.Maybe import Just, Nothing
from pymonad import curry

def some(pred, coll):
    for x in coll:
        if pred(x): return True
    return False

@curry
def request_contains(keys, request):
    if all(map(lambda k: k in request, keys)):
        return Right(request)
    else:
        return Left('Falta usuario o clave. Contacte a su operador.')

@curry
def user_exists(users, req):
    if some(lambda u: u['username'] == req['username'], users):
        return Right(req)
    else:
        return Left('El usuario no existe.')

@curry
def user_authenticates(users, req):
    user = next(u for u in users if u['username'] == req['username'])
    if user['password'] == req['password']:
        return Right(user)
    else:
        return Left('Contraseña incorrecta.')

@curry
def user_is_tecnico(tecnicos, user):
    if user['username'] in tecnicos:
        return Right(user)
    else:
        return Left('Usuario no es técnico')

@curry
def get_nombre(user):
    return Right(user['name'])

@curry
def get_permisos(permisos, user):
    if user['username'] in permisos:
        return Right(permisos[user['username']])
    else:
        return Left('No tiene permisos.')


users = [{'username': 'chancho', 'password': '444', 'name': 'Chanchito'},
         {'username': 'pedro', 'password': '123', 'name': 'Pedro Gomez'},
         {'username': 'loly', 'password': 'qwertz', 'name': 'La Princesa'}]

tecnicos = ['pedro', 'loly']

permisos = {'pedro': ['archivar', 'borrar']}

req = {'username': sys.argv[1], 'password': sys.argv[2]}

val = request_contains(['username', 'password'], req) >>\
      user_exists(users) >>\
      user_authenticates(users) >>\
      user_is_tecnico(tecnicos) >> (lambda user:
      get_nombre(user) >> (lambda nombre:
      get_permisos(permisos, user) >> (lambda permisos:
      Right("El usuario {} tiene estos permisos: {}".format(nombre, ', '.join(permisos))))))

print(val)
