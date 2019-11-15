# name = 'rafael'
# product = 'python elearning course'

# email_content = f"""
# hi {name}

# thank you porchesing {product}

# regards,

# sales team
# """

# print(email_content)

# name = 'rafael'
# product = 'Python elearning course'

# email_content = f"""
# Hi {name}

# Thank you for purchasing {product}

# Regards,

# Sales Team
# """

# print(email_content)





# nombre_completo = "Rafael Pinon Gonzales"
# nombre, _, apellido = nombre_completo.partition('Pinon ')
# partition=este es igual a quitar y poner es solo un comentario para saber el significado de la palabra 
# print(nombre)
# print(apellido)

# tags = 'pythone,coding,programing,development'

# list_of_tags  tags.split(',')

# print(list_of_tags)

# list_of_tags = tags.split()

# print(list_of_tags)

# heading = "pithon: an introduction"

# heading_list = heading.split(': ')

# print(heading_list)

# api_data = '5'
# greeting = 'Hi there'

# print(api_data.isalpha())
# print(greeting.isalpha())

# print(api_data.isnumeric())
# print(greeting.isnumeric())

# product_id = 123
# sale_price = 14.99
# tip_percentage = 1/5
# new_product = 150

# print(sale_price + new_product)


# print('Addition')
# print(100 + 42)

# print('Subtraction')
# print(100 - 42)

# print('Division')
# print(100 / 42)
# print(100 / 38)

# print('Floor Division')
# print(100 // 42)
# print(100 // 38)

# print('Multiplication')
# print(100 * 42)

# print('Modulus')
# print(100 % 42)

# print('Exponents')
# print(100 ** 42)

# total = 100
# total += 10

# print *= 2
# import math

# loss = -20.25
# product_cost = 89.99

# print(abs(loss))
# print(math.floor(product_cost))
# print(math.ceil(product_cost))
# print(abs(math.floor(loss)))
# print(round(product_cost))
# print(math.sqrt(product_cost))
# print(math.pow(5, 2))
# print(5 ** 2)
# from funtcools import reduce

# """
# manual_exponent(2, 3)
# #> 8
# manual_exponent(10, 2)
# #> 100
# """

# def manual_exponent(num, exp):
#     computed_list = [num] * exp
#     return (reduce(lamda total, element: total * element, computed_list))

       
#         print(manual_exponent)(2, 3))
#         print(manual_exponent)(10, 2))
           
# def some_func(total,element):
#     return(total * element

#     [2, 2, 2]

#     some_func(2, 2)
#     some_func(2, 2)
# """
# user database query
# rafael
# sabdi
# eduardo
# """
# users = ['rafael,sabdi','eduardo']

# print(users)

# users.insert(0,'nayeli')

# print(users)

# users.append('yuri')
# print(users)

# print(users)
# print([users[2]])

# users[4] = 'jaqui'
# print(users)

# """
# User Database Query
# Kristine
# Tiffany
# Jordan
# """

# users = ['Kristine', 'Tiffany', 'Jordan']

# print(users)

# users.insert(1, 'Anthony')

# print(users)

# users.append('Ian')

# print(users)

# print([users[2]])

# users[4] = 'Brayden'

# print(users)
# users = ['rafael','sabdi','eduardo','nayeli']

# ids = [1, 2, 3, 4,]

# mixed_list = [42, 10.3, 'altuve', users]

# print(mixed_list)

# user_list = mixed_list.pop()

# print(user_list)
# print(mixed_list)

# nested_lists = [[123], [234], [345]]

# tags= ['python', 'development','tutorials', 'code']

# number_of_tags = len(tags)
# last_item = tags[-1]
# index_of_last_item = tags. index(last_item)

# print(number_of_tags)
# print(last_item)
# print(index_of_last_item)

# tags= ['python', 'development','tutorials', 'code']

# print(tags)

# tags.sort()

# print(tags)

# tags.sort(reverse=True)

# print(tags)

# totals = [234, 1, 543, 2345]

# totals.sort(reverse=True)

# print(totals)

# USO DE FUNCION DE UNION EN Python PARA CONSTRUIR UNA CADENA DE CONSULTA URL.
# https://www.google.com/search?q=python+tuturial


# uri = 'https://www.google.com/search?q='
# tags = ['python' , 'development', 'tutorial']
# formatted_tags = '+'.join(tags)
# query_uri = f' {uri}{formatted_tags}'

# print(query_uri)
#DESCRIPCION GENERAL DE RANGOS EN LISTAS DE Python
# tags = ['python', 'development', 'tutorial', 'code']

# tag_range = tags[1:2]

# print(tag_range)
#TECNICAS AVANZADAS PARA IMPLEMENTAR RANGOS Y CORTES EN LISTAS DE Python
# tags = [
#     'python'
#     'development',
#     'tutorial',
#     'code',
#     'programming',

#     'computer science'
# ]
#  tag_range = tags[1:-1:2]
#  tag_range = tags[::-1]
# # cuando pones [::-1]la lista de etiquetas de pone alrreves inicia primero computer science y alultipo python
# #sorted_tags = tags . sort(reverse=True)

# print(tag_range)

# tags.sort(reverse=True)

# print(tags)
#DESCRIPCION GENERAL DE RANGOS el lista de python

# ESTO ES PARA IMPRIMIR SOLO development QUE SIGNIFICA DESARROLLO *tag_range = tags[1:2]*
# tags = ['pyton', 'development', 'tutorials', 'code']

# tag_range = tags[1:2]
 
# print(tag_range)

#SI QUEREMOS IMPRIMIR LOS ELEMENTOS DEL INDICE 1 Y 2 TENEMPS QUE IR 1 ARRIVA DE LA CADENA CON ESO IMPRIME DESARROLLO Y LOS TUTORIALES 
# tags = ['pyton', 'development', 'tutorials', 'code']

# tag_range = tags[1:3]
 
# print(tag_range)

#SI QUEREMOS RECUPERAR TODAS LAS ETIQUETAS COMENSAMOS EN EL INDICE QUE ES 
# development QUE ES EL DESARROLLO ASTA EL FINAL SE IMPRIMIO=['development', 'tutorials', 'code']
# SI TUBIERAMOS MAS ETIQUETAS SE IMPRIMEN TODAS.

# tags = ['pyton', 'development', 'tutorials', 'code']

# tag_range = tags[1:]
 
# print(tag_range)

# SI QUIERO IMPRIMIR DESDE EL INICIO DE LA CADENA DE ETIQUETAS ASTA DESARROLLO SOLO QUE PONER tags[:2]
# ATRAS DE LOS DOS PUNTOS PARA QUE PARE ASTA AHI IMPRIME=['pyton', 'development',]
# tags = ['pyton', 'development', 'tutorials', 'code']

# tag_range = tags[:2]
 
# print(tag_range)

# NOTA SI LOS PUNTOS ESTA ADELANTE DEL NUMERO QUIERE DECIR QUE INICIA DE ISQUIERA A DERECHA Y PARA DEPENDE 
# DEL VALOR DEL NUMERO SI ES 3 PARA EN LA ETIQUETA 3 Y SI LOS PUNTOS ESTAN AL INICIO DEL N UMERO LA CUENTA
# INICIADE DERECHA A IZQUIERDA.
# tags = ['pyton', 'development', 'tutorials', 'code']

# tag_range = tags[0:-1]
#  AQUI INICIA  DE DE 0 QIE ES Python Y LE RESTA 1 DE DERECHA A ISQUIERA QUE ES =['pyton', 'development', 'tutorials']
# print(tag_range)

#VIDEO =TECNICAS AVANZADAS PARA IMPLEMENTAR RANGOS Y CORTES EN LINEA DE Python
#si se pone este codigo tags[1:-1] se imprime desde desarrollo asta programacion
# tags = [
#   'pithon',
#   'development',
#   'tutorials',
#   'code',
#   'programming',
#   'computer science'
#  ]

# tag_range = tags[1:-1]

# print(tag_range)

#si queremos que se imprima la lista de etiquetas alrreves solo se tiene que poner este codigo= tags[::-1]
# tags = [
#   'pithon',
#   'development',
#   'tutorials',
#   'code',
#   'programming',
#   'computer science'
#  ]

# tag_range = tags[::-1]

# print(tag_range)

#si queremos poner la lista alreves y luego la quieres ordenar en orden alfebetico la setiquetas 
# se ponen estos codifos tag_range = tags[1:-1:2] y abajo tag_range = tags[::-1]
# tags = [
#   'python',
#   'development',
#   'tutorials',
#   'code',
#   'programming',
#   'computer science'
# ]

# tag_range = tags[1:-1:2]


# print(tag_range)

# tags.sort(reverse=True)

# print(tags)

#VIDEO GUIA DE LA FUNCION ORDENADA DE PYTHON
#sale_price significa presios de venta si los quiero ordenar de menor a mayorsees el codigo= sale_price.sort() 
#sort significa ordenar lo imprimes y listo.
# sale_prices = [
#     100,
#     83,
#     220,
#     40,
#     100,
#     400,
#     10,
#     1,
#     3
# ]
# sale_prices.sort()

# print(sale_prices)

# Si pones este codigo= sorted_list = sorted(sale_prices,reverse=True) que significa presios de venta ordenar verdadero. 

# sale_prices = [
#     100,
#     83,
#     220,
#     40,
#     100,
#     400,
#     10,
#     1,
#     3
# ]
# sorted_list = sorted(sale_prices,reverse=True)

# print(sorted_list)

# print(sorted_list)

# VIDEO COMO ENCONTRAR LA MEDIANA DE UNA LISTA DE PYTHON CON UN NUMERO IMPAR DE NUMEROS
#  tengo una lista de precios de venta AQUI
# para tener una lista de preicios ordenada de menor a mayor se pone el codigo
# sorted_list = sorted(sale_prices) nos da un resultado de [1, 3, 10, 40, 83, 100, 100, 220, 400]
# en este caso el valor de la media es 83 esta en el centro de la lista de precios.
# para saver la cantidad de precios que tenemos se pone este codigo num_of_sale = len(sorted_list) que esto
# significa numero de ventas de lista ordenada que nos da el resultado de 9.
#si ponemos todos estos datos sacamos la media de lista de precios 


  
# import math



# sale_prices = [
#   100,
#   83,
#   220,
#   40,
#   100,
#   400,
#   10,
#   1,
#   3
# ]

# sorted_list = sorted (sale_prices) 
# num_of_sales = len (sorted_list) 
# half_slice = math.floor (num_of_sales / 2 ) 
# first_sales_items = sorted_list [: half_slice] 
# last_sales_items = sorted_list [- (half_slice):]







  

# mediana = sorted_list [half_slice: (half_slice + 1 )] 

# print (sorted_list) 
# print (num_of_sales) 
# print (first_sales_items) 
# print (last_sales_items) 
# print (mediana)

# VIDEO TRABAJANDO CON LA CLASE REBANADA EN PYTHON PARA ALMACENAR REBANADAS
# 0 COMENTARIOS
#  VIDEO COMO AGREGAR UNA LISTA DE PYTHON CON PROCESOS TANTO IN SITU COMO DE COPIA 
# para remplasar una etiqqueta por otra y quitar la ultima que en este caso seria code se pone el codigo 
# tags[-1] = 'programming'  programing es el elemento que vamos agergar.

# tags = ['python', 'developemen', 'tutorials', 'code']

# tags[-1] = 'programming'

# print(tags)

# Si queremos agregar un elementio mas a las etiquetas se pone el codigo tags.extend(['programming']) que significa
# extencion de etiquetas.

# tags = ['python', 'developemen', 'tutorials', 'code']

# tags[-1] = 'programming'

# tags.extend(['programming'])

# print(tags)


# con este codigo new_tags = tags + ['progaramming'] se agrega la etiqueta al fina 

# tags = ['python', 'developemen', 'tutorials', 'code']

# new_tags = tags + ['progaramming']

# print(new_tags )

# comom se puede ver se puede inprimir la etiqueta sin el elemento agregado como tambien con el elemento agregado 
# en la mispa imprecion.
# tags = ['python', 'developemen', 'tutorials', 'code']

# new_tags = tags + ['progaramming']

# print(new_tags )

# print(tags)

#CONSTRUIR  UNA FINCION DE LA LOTERIA PONDERADA EN PYTHON
# SIGNIFICADOS
# weighted_lottery(weights): = loteria ponderada  pesos 
# for (name, weight) = para (nombre de pesos)
# in weights.items = en aritculos de pesos
#  for _ in range(weight): = para en rango de pesos 
#  container_list.append(name) = lisa de contenedores agregar (nombre) 
# return container_list = lista de contenedores de devolucion
# other_weights = otros pesos
# 'winning': 1, 'break_even': 2, 'losing': 3 = victorioso, punto de equilibrio, perdiendo. 
#  en este video aprendimos a seleccionar al apcion ue va ganar y cual va perder como tambien  el punto de equilibrio .
# import numpy as np

# def weighted_lottery(weights):
#     container_list = []

#     for (name, weight) in weights.items():
#         for _ in range(weight):
#             container_list.append(name)

#     return np.random.choice(container_list)

# other_weights = {
#     'green': 1,
#     'yellow': 2,
#     'red': 3
# }

# print(weighted_lottery(other_weights))

#VIDEO DISCRIPCION GENERAL DE LOS DICCIONARIOS DE PYTHON
#  en esta activida creamos en clave con valor convertimos ss = a correa al momento de imprimir.

# players = {
#     "ss": "Correa"
# }
# print(players)

# en esta actividad hicimos lo mismo solo que con mas claves y mas argumentos.
# players = {
#    " ss " : " Correa " ,
#    " 2b " : " Altuve " ,
#    " 3b " : " Bregman " ,
#    " DH " : " Gattis " ,
#    " OF " : " Springer " ,
# }

# print(players)

# en esta actividad al momento de imorimir se imprime el elemento del codigo que es Altuve
# #second_base = segunda base.
# players = {
#     " ss " : " Correa ",
#     " 2b " : " Altuve ",
#     " 3b " : " Bregman ",
#     " DH " : " Gattis ",
#     " OF " : " Springer ",
# }
# second_base = players['2b']

# print(second_base)

# con esta actividad podemos ver que se puede cambiar de dato al codigo se asino hitter a cmbio de players.
# players = {
#   "ss": "Correa",
#   "2b": "Altuve",
#   "3b": "Bregman",
#   "DH": "Gattis",
#   "OF": "Springer",
# }

# second_base = players['2b']
# designated_hitter = players['DH']

# print(designated_hitter)

#VIDEO GUIA DE COLECCIONES ANIDADAS EN DICCIONARIO DE PYTHON

# team es igual a equipo es esta actividad pusimos imprimir equipo astros se imprimieron todos los jugadores

# teams = {
#   "astros": ["Altuve", "Correa", "Bregman"]
# }

# print(teams['astros'])

# En esta actividad se imprimio solo los 2 primeros elementos ya que lo notificamos en la impercion 
# se imprimio altuve y correa. los 2 puntos estan de lado izquierdo por es empiesa a contarce los primeros 2
# de izquierda a derecha.

# teams = {
#   "astros": ["Altuve", "Correa", "Bregman"]
# }

# print(teams['astros'][:2])


# en esta actividad se imprimio como lo podemos ver facil
# teams = {
#   "astros": ["Altuve", "Correa", "Bregman"],
#   "angels": ["Trout", "Pujols"],
#   "yankees": ["Judge", "Stanton"],
# }

# astros = teams['astros']
# print(astros)
# print(teams['angels'])
# print(teams['yankees'])

#VIDEO COMO AGREGAR NUEVOS PARES CLAVE / VALOR A LOS DICCIONARIOS DE PYTHON
# si ponemos este codigo se imprime por equipo y se agrega el que indicmos el codigo o la formula que 
# aplicaos es = teams['red sox'] = ['price', 'Betts']

# teams = {
#     "astos": ["altuve", "correa", "Bregman"],
#     "angeles":["Trut", "pujols"],
#     "yankees": ["judge", "Stanton"],
# }

# teams['red sox'] = ['price', 'Betts']

# print(teams)

#VIDEO GUIA PARA USAR LA FUNCION GET EN LOS DICCIONARIOS DE PYTHON PARA CONFIGURAR VALORES DE  BUSQUEDA ALTERNATIVA
# aqui con esta clave podeos seleccionar el quipo que queremos imprimir  poniendo este codigo featured_team = teams['astros']
# que esto signific quipo destacado = equipo astros
# teams = {
#   "astros": ["Altuve", "Correa", "Bregman"],
#   "angels": ["Trout", "Pujols"],
#   "yankees": ["Judge", "Stanton"],
#   "red sox": ['Price', 'Betts'],
# }

# featured_team = teams['astros']

# print(featured_team)

# en esta actividad podimos sacar el equipo no destacado si imprimio los jugadores del equipo que imprimimos
# poniendo este codigo = featured_team = teams .get ('yankees', 'No factured team') que esto significa 
# equipo destacado = equipo yank , equipo no destacado

# teams = {
#   "astros": ["Altuve", "Correa", "Bregman"],
#   "angels": ["Trout", "Pujols"],
#   "yankees": ["Judge", "Stanton"],
#   "red sox": ['Price', 'Betts'],
# }

# featured_team = teams .get ('yankees', 'No factured team')

# print(featured_team)

#VIDEO QUIA DE OBJETOS DE VISUALIZACION DE DIRECCIONAIO DE PYTHON

# en esta activid no ensena que si queremos imprimir las llaves de los jugadores solo se pone este codigo
# print(players.keys()) que esto significa imprimir llaves de jugadores.

# players = {
#   "ss" : "Correa",
#   "2b" : "Altuve",
#   "3b" : "Bregman",
#   "DH" : "Gattis",
#   "OF" : "Springer",
# }
# print(players.keys())

# teams = {
#   "astros" : ["Altuve", "Correa", "Bregman"],
#   "angels":  ["Trout", "Pujols"],
#   "yankees": ["Judge", "Stanton"],
#   "red sox": ["Price", "Betts"],
# }

# en esta actividad imprimimos los juagadores con este codigo print(players.values())
# que esto significa imprimir valores de jugadores.

# players = {
#   "ss" : "Correa",
#   "2b" : "Altuve",
#   "3b" : "Bregman",
#   "DH" : "Gattis",
#   "OF" : "Springer",
# }
# print(players.values())

# teams = {
#   "astros" : ["Altuve", "Correa", "Bregman"],
#   "angels":  ["Trout", "Pujols"],
#   "yankees": ["Judge", "Stanton"],
#   "red sox": ["Price", "Betts"],
# }

# en esta actividad nos ensena a a imprimir las llaves que son los codigos que estan a los lados de los nombres 
# de lado de los juagadores y el nombre de los jugadores entre parentisis ls llaves y los nombre.
# con este codigo print(players.items()) que esto significa imprimir articuos y jugadores.

# # players = {
#   "ss" : "Correa",
#   "2b" : "Altuve",
#   "3b" : "Bregman",
#   "DH" : "Gattis",
#   "OF" : "Springer",
# }
# print(players.items())

# teams = {
#   "astros" : ["Altuve", "Correa", "Bregman"],
#   "angels":  ["Trout", "Pujols"],
#   "yankees": ["Judge", "Stanton"],
#   "red sox": ["Price", "Betts"],
# }

# aqui en esta actividad queremos imprimir los nombres de los jugadores para esto se pone este codigo
# print(players.values()) esto es igual a imprimir valores de jugadores.

# players = {
#   "ss" : "Correa",
#   "2b" : "Altuve",
#   "3b" : "Bregman",
#   "DH" : "Gattis",
#   "OF" : "Springer",
# }
# print(players.values())

# teams = {
#   "astros" : ["Altuve", "Correa", "Bregman"],
#   "angels":  ["Trout", "Pujols"],
#   "yankees": ["Judge", "Stanton"],
#   "red sox": ["Price", "Betts"],
# }

# en esta actividad no ensena a ser mas selecivo imprimimos un jugador esto fue posible por ingresar este codigo
# print(list(players.values())[1]) imprimir lista valor de jugadores y no lo marca con 1 que es el primer elemento 
# imprimiendo altuve.
# recordemos que en las listas se inicia de 0
# players = {
#   "ss" : "Correa",
#   "2b" : "Altuve",
#   "3b" : "Bregman",
#   "DH" : "Gattis",
#   "OF" : "Springer",
# }
# print(list(players.values())[1])

# teams = {
#   "astros" : ["Altuve", "Correa", "Bregman"],
#   "angels":  ["Trout", "Pujols"],
#   "yankees": ["Judge", "Stanton"],
#   "red sox": ["Price", "Betts"],
# }

# en esta actividad no ensena como imorimir la lista de los nombre de los jugadores 
# para esto tenemos que poner este codigo player_name = list(players.copy().values()) que esto significa
# nombre de jugadores = lista (copia de jugadores() valores

# players = {
#   "ss" : "Correa",
#   "2b" : "Altuve",
#   "3b" : "Bregman",
#   "DH" : "Gattis",
#   "OF" : "Springer",
# }
# player_name = list(players.copy().values())

# print(player_name)

# teams = {
#   "astros" : ["Altuve", "Correa", "Bregman"],
#   "angels":  ["Trout", "Pujols"],
#   "yankees": ["Judge", "Stanton"],
#   "red sox": ["Price", "Betts"],
# }

# en esta actividad nos ensena como imprimir los nombres de los jugadores y imprimir los equipos 
# e integrantes de los equipos este fu posible ponindo estos codigos.
# codigo1=player_name = list(players.copy().values()) codigo2=team_grupings = teams . items() esto significa
# eqipo grupos, equipos aritculos. se imprimen y listo


# players = {
#   "ss" : "Correa",
#   "2b" : "Altuve",
#   "3b" : "Bregman",
#   "DH" : "Gattis",
#   "OF" : "Springer",
# }
# player_name = list(players.copy().values())

# print(player_name)

# teams = {
#   "astros" : ["Altuve", "Correa", "Bregman"],
#   "angels":  ["Trout", "Pujols"],
#   "yankees": ["Judge", "Stanton"],
#   "red sox": ["Price", "Betts"],
# }

# team_grupings = teams . items()

# print(team_grupings)

# aqui en esta actividad fuimos mas selectivo con este formulario imprimimos Trout con este codigo fue posible 
# print(list(team_groupings)[1][1][0])


# players = {
#   "ss" : "Correa",
#   "2b" : "Altuve",
#   "3b" : "Bregman",
#   "DH" : "Gattis",
#   "OF" : "Springer",
# }

# player_names = list(players.copy().values())

# teams = {
#   "astros" : ["Altuve", "Correa", "Bregman"],
#   "angels":  ["Trout", "Pujols"],
#   "yankees": ["Judge", "Stanton"],
#   "red sox": ["Price", "Betts"],
# }

# team_groupings = teams.items()

# """
# [
#   ('astros', ['Altuve', 'Correa', 'Bregman']),
#   ('angels', ['Trout', 'Pujols']),
#   ('yankees', ['Judge', 'Stanton']),
#   ('red sox', ['Price', 'Betts'])
# ]
# """

# print(list(team_groupings)[1][1][0])

#VIDEO DISCRIPCION GENERAL DE LOS MULTIPLES METODOS PARA ELIMINAR ELEMENTOS EN UN DICCIONARIO DE PYTHON
#del esto significa borrar asi que al imprimir se borra el equipo de astros 

# teams = {
#  "astros" : ["Altuve", "Correa", "Bregman"],
#   "angels":  ["Trout", "Pujols"],
#   "yankees": ["Judge", "Stanton"],
#   "red sox": ["Price", "Betts"],
#  }

# del teams['astros']

# print(teams)

# en esta actividad pusimos aproposito otro equipo que no se encontraba y le agregamos eun mensaje en donde 
# nos indicara que no se cuenta con este esquipo para esto pusimos este codigo print(teams.get('mets','No se encontró ningún equipo con ese nombre ' ))



# teams = {
#   "astros" : ["Altuve", "Correa", "Bregman"],
#    "angels":  ["Trout", "Pujols"],
#    "yankees": ["Judge", "Stanton"],
#    "red sox": ["Price", "Betts"],
#   }

# print(teams.get('mets','No se encontró ningún equipo con ese nombre ' ))

#VIDEO GUIA PAR TRABAJAR CON LISTAS DE DIRECCIONARIOS ANADIDAS
# aqui en esta actividad queremos imprimir pujols para esto tenemos que poner este codigo angels = teams[1].get('angels', 'Team not found')
#  y inmprimir que es este print(list(angels.values())[1])
# teams = [
#   {
#     'astros': {
#       '2B': 'Altuve',
#       'SS': 'Correa',
#       '3B': 'Bregman',
#     }
#   },
#   {
#     'angels': {
#       'OF': 'Trout',
#       'DH': 'Pujols',
#     }
#   }
# ]

# # print(teams[0])

# angels = teams[1].get('angels', 'Team not found')

# print(list(angels.values())[1])

# #VIDEO CREA UN HISTOGRAMA DE PYTHON SIN BIBLIOTECAS DE TERCEROS
#  en este video podemos imprimir la catiad de signos al valor que se le agrega a cada uno 

# """
# g $$$$$$$$$$$$$$$$$$$$
# f $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# t $$$$$$$$$$
# o $$$$$$$$$$$$
# """

# sales = {
#   'google': 20,
#   'facebook': 42,
#   'twitter': 10,
#   'offline': 12,
# }

# print('g ' + sales['google'] * '$')
# print('f ' + sales['facebook'] * '$')
# print('t ' + sales['twitter'] * '$')
# print('o ' + sales['offline'] * '$')

# List: []
# Dictionary: {}
# Tuple: ()

# Tuple: immutable 
# List: mutable

#VIDEO INTRODUCCION DE PAYTHON TUPLES

# En este video pudimos aprender que se puede nombrar el titulo- subtitulo y contenido.
# anumerando segun sea su ubicacion que coresponda.

# post = ('Python Basics', 'Intro guide to python', 'Some cool python content')

# # Tuple unpacking
# title, sub_heading, content = post

# # Equivalent to Tuple unpacking
# # title = post[0]
# # sub_heading = post[1]
# # content = post[2]

# print(title)
# print(sub_heading)
# print(content)

#VIDEO COMO AGREGAR ELEMENTOS A UNA TUPLA APROBECHANDO LA RESIGNACION 
# La clave id es como un registro de dato en la compu identificacion.
# post = ('Python Basics', 'Intro guide to python', 'Some cool python content')

# print(id(post))
# print(id(post))

# post += ('published',)

# print(id(post))

# title, sub_heading, content, status = post

# print(title)
# print(sub_heading)
# print(content)
# print(status)


#VIDEO TRABAJANDO CON LISTAS ANIDADAS EN TUPLES 
# como podeos ver en este ejersicio se imprimio coding ya que la numeracion que se le puso es al que nombraba 

# post = ('Python Basics', 'Intro guide to Python', 'Some cool python content')

# tags = ['python', 'coding', 'tutorial']

# post += (tags,)

# print(post[-1][1])

#VIDEO GUIA REBANADAS EN TUPLES DE PYTHON
# AQUI PUDIMOS VER QUE SE IMPRIMIO LO QUE ESTA ANUMERADO POR LA UBICACION EN LA QUE SE ENCUANTRA
# post = ('Python Basics', 'Intro guide to Python', 'Some cool python content', 'published')

# print(post[1::2])

# post = ('python basics', 'Intro guide to python', 'somecool python content', 'published')

# # # removing element from end 
# # post = post[:-1]

# # removing element from beginning
# post = post[:-1]

# print(post)

#VIDEO TRABAJANDO COM LISTAS ANADIDAS EN TUPLES

# en esta actividad estamos agrupando o nombrando para a impresion poniendo post+=(tags) 
# que esto significa que al momento de imprimir se imprima los emvios y las etiquetas   
# post es = a envio tags es = a etiquetas.

# post = ('python basic', 'intro guide to python', ' some cool python content')

# tags = [ 'python', 'coding', 'tutorials']

# post += (tags,)

# print(post)

# en esta actividad estamos nombrando qye nadamas se imprima coding esto es posible piniendo este codigo
# print(post[-1][1])con esta numeracion nos da la ubicacion de coding

# post = ('python basic', 'intro guide to python', ' some cool python content')

# tags = [ 'python', 'coding', 'tutorials']

# post += (tags,)

# print(post[-1][1])

#VIDEO GUIA DE REBANADAS EN TUPLAS DE  PYTHON
#  En esta actividad y con estos codigos tenemos la capasidad de lo que queremos imprimir
#  para hacer esto posible ay que poner este codigo print(post[:2]) que sto signifiza que queremos imprimir
#  las 2 primeras post las 2 primeros envios en espanol.

# post = ('Python Basics', 'Intro guide to Python', 'Some cool python content', 'published')

# print(post[:2])

#VIDEO INTRODUCCION EN LA ESTRUCTURA DE DATOS  DEL CONJUNTO DE PYTHON

#  en esta actividad ponemos buscar si esta python en la lista de las etiquetas es verdadero pero como 
#  en este ejemlo ponemos buscar qye si en la lista de etieutas esta ruby automaticamente al imprimir 
#  nos pone que es falso ya que no esta en la lsita de etiquetas.
# tags = {
#   'python',
#   'coding',
#   'tutorials',
#   'coding'
# }

# #print(tags)

# # Nope
# #print(tags[0])

# query_one = 'python' in tags   
# query_two = 'ruby' in tags

# print(query_two)

#VIDEO  VARIOS METODOS PARA FUNCIONAR CONJUNTO DE PYTHON
#  en esta actividad y con este codigo se imprimio las etiquetas 1 y las etiquetas 2 los elementos si repetir os elementos .
# tags_one = {
#   'python',
#   'coding',
#   'tutorials',
#   'coding'
# }

# tags_two = {
#   'ruby',
#   'coding',
#   'tutorials',
#   'development'
# }
# merged_tags = tags_one | tags_two

# print(merged_tags)


# VIDEO Cómo implementar Python Loops para listas, tuplas y diccionarios
#  en este video podeos ver que se imprimio las posiciones que son las 

# players = {
#   '2b': 'Altuve',
#   '3b': 'Bregman',
#   'ss': 'Correa',
#   'dh': 'Gattis'
# }

# for position, player in players. items():

#   print('position',position)
#   print('player name', player)

#VIDEO Cómo recorrer los caracteres de una cadena de Python
# en este video podemos ver que se imprimio del 1 al 11 pero para uno menos empiesa en el 10
# y el ultimo mumero que se pone quiere decir que se valla de 2 en 2 y si ponemos 3 es de 3 en 3 asi susesivaente 

# for num in range(1, 11, 2):
#     print(num)

# usernames = [
#     'jon',
#     'tyrion',
#     'theon',
#     'cersei',
#     'sansa',
# ]
# for username in usernames:
#      if username  == 'cersei':
#          print(f'{username} was found at index  { username. index (username)}')
#   break
# print(username)

#VIDEO Descripción general de los bucles While en Python
 
 #en este ejersicio se imprimio dodo el listado de numeros del 1 al 100

# nums = list(range(1, 100))

# while len(nums) > 0:
#   print(nums.pop())
#  este es un juego de adivinanzas si le atienas 42 es el numero indicado si no es falso
# def guessing_game():
#   while True:
#     print('What is your guess?')
#     guess = input()

#     if guess == '42':
#       print('You correctly guessed it!')
#       return False
#     else:
#       print(f"No, {guess} isn't the answer, please try again\n")
# guessing_game()

#VIDEO Cómo combinar y aplanar listas en Python con el bucle For / In
 
 #aqui se imprimen los clientes eredados y clientes como se muestra en este codigo raw_db = [legacy_customers, new_customers]

# legacy_customers = [ ' Alice '  ' Bob ' ]
# new_customers = [ ' Tiffany ' , ' Kristine ' ]

# raw_db = [legacy_customers, new_customers]

# print(raw_db)

#VIDEO Introducción al uso de la comprensión de listas en Python
#  en esta actividad imprimimos solo los numeros multiplicados 

# num_list = range(1, 11)

# cubed_nums =[]

# for num in num_list:
#     cubed_nums.append(num ** 3)

# print(cubed_nums)

# en esta activiad imprimimos la numeracion del 1 al 10 y aparte la multiplicacion.
# la multiplicacion es uno al cuadrado cubicos
# num_list = range(1, 11)

# cubed_nums =[]

# for num in num_list:
#   cubed_nums.append(num ** 3)

# print(list(num_list))
# print(cubed_nums)
# *importante ejersicio para poner nombre o titulo y subtitulos*
# """
# heading_generator(title, heading_type)
# heading_genarator('greeting', '1')
# <hi>greeting</h1>

# heading_generator('hi there', '3')
# <h3>hi there</h3>

# """

# def heading_generator(title, heading_type):
#     return f'<h{heading_type}>{title}</h{heading_type}>'
# print(heading_generator('greeting', '1'))
# print(heading_generator('hi there', '3'))

# en esta actividad ponemos una condic

# def check():

#     edad = int(
#         input("Cuandos anos tienes?  ")
#     )

#     if edad < 25:
        
#         print("Lo siento, debes tener al menos 25 años")

#     else:
#         print("Estas bien")
   
# check()


# ESTE ES UN EJEMPLO DE CONDICIONES Y RESPUESTAS ALEXANDER PRACTICAR 
# pregunta = "cuanto es dos mas dos?"

# respuesta = 4

# while True:

#     print(pregunta)

#     guess = int(input())

#     if guess == respuesta:
#         print("Lo hicistes")
#         break

#     else:
#         print("Otra vez")
#         continue

# condiciones de edad 
# age =30

# if age <25:
    
#     print(f"lo siento deves tener menos de 25 anos")
    
# else:

#      print(f"tienes la edad para comprar un auto")   
    
# condiciones estudiar
# role = 'guest'

# auth = 'can access' if role == 'admin' else 'cannot access'

# if role == 'admin':
#   auth = 'can access'
# else:
#   auth = 'cannot access'

# print(auth)    
#  en este ejemlo ponemos una condicion que es si eres mayor de 25 pudes entrar y asignamos un mensaje de bienvenidad 
#  si cumples con la condicion.
# username = 'jonsnow'

# if username == 'jonsnow':
#   print('Welcome Jon')
# else:
#   print('You shall not pass!')

# age = 26


# if age <= 25:
#   print(f"I'm sorry, you need to be at least 25 years old")

# #condiciones para poder entrar a un sistema con contrase;a y nombre correcto
# JEMPLO DE CODIGOS CONDISIONES 
# nombre = 'rafael'
# correo = 'rafapinongonzalez@live.com.mx'
# contrasena = 'rpg131529'

# if nombre == 'rafael' and contrasena == 'rpg131529':
#   print('permitido entrar')
# else:
#   print('no autorizado')
  
# def full_name(first, last):
#     print(f'{first} {last}')

#     full_name('kristine', 'hudgens')

# pregunta = "cuanto es treina mas treinta?"

# respuesta = 60

# while True:

#     print(pregunta)
    
#     guess = int(input())

#     if guess == respuesta:
#         print("lo lograste")
#         break

#     else:

#         print("intentalo de nuevo")
#         continue

#VIDEO COMO VEREFICAR SI UN VALOR ESTE INCLUIDO EN UNA CADENA DE LISTA DE pithon


# oracion= 'El rápido zorro marrón saltó sobre el perro perezoso'
# palabra= 'rápido'

# if palabra in oracion:
#     print('la palabra fue encontrada en la oracion')
# else:
#     print('la palabra no fue encontrada en la oracion')

#VIDEO Sintaxis básica para crear funciones de Python

# def nombre_completo(primero, ultimo):
  
#   print(f'{primero} {ultimo}')


# nombre_completo('rafael', 'pinon')

# def auth(correo, contrasena):
#   if correo == 'kristine@hudgens.com' and contrasena == 'secret':
#     print('estas autorizado')
#   else:
#     print('no estas autorizado')

# auth('kristine@hudgens.com', 'asdf')

# def hundred():
#   for num in range(1, 101):
#     print(num)
# EN ESTE VIDEO APRENDIMOS ACOMODAR PALABRA USAMOS DE EJEMLO COMO ACOMODAR NOMBRE Y APELLIDO 
# ACOMODADNO PRIMERO EL NOMBRE Y DESPUES EL APELLIDO
# def nombre_completo(primero, ultimo):
#   print(f'{primero} {ultimo}')


# nombre_completo('rafael', 'pinon')
# nombre_completo(primero = 'rafael', ultimo = 'pinon')
# nombre_completo(ultimo = 'pinon', primero = 'rafael')
# ejersicios 
# def saludos(**ident):
#   print(ident)


# saludos()
# saludos(primero = 'rafael', ultimo = 'pinon')

# def saludos(**ident):
#   if ident:
#     print(f"hola {ident['primero']} {ident['ultimo']}, que tengas un gran dia!")
#   else:
#     print('hola invitado!')


# saludos()
# saludos(primero = 'rafel', ultimo = 'pinon')

#VIDEO Requisitos del proyecto: construir FizzBuzz en Python


# EJERCICIO MUY IMPORTANTE CONDICIONES E IMRECONES DE PALABRAS 
# """
# escribe un programa que imprima los números del 1 al 100.
# pero para múltiplos de tres letras "fizz" en lugar de
# número y para los múltiplos de cinco imprimir "zumbido". para
# números que son múltiplos de tres y cinco letras
# "fizzbuzz".
# """
# def fizz_buzz(max_num):
   
#   for num in range(1, max_num + 1):
#     if num % 3 == 0 and num % 5 == 0:
#         print('fizz_buzz')

#     elif num % 3 == 0:
#       print('fizz')
#     elif num % 5 == 0:
#       print('buzz')
#     else:
#       print(num)

# fizz_buzz(100)

#VIDEO INTRIDUCCION A LA SECCIONDE MODULOS DE IMPORTACION DE PYTHON


























  































