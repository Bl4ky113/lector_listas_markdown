
from sys import argv
from get_list import getListData

list_input = argv[1]
# list_input = input("Ingresa una lista hecha en Markdown:  ")
list_obj = getListData(list_input, ".md")

if list_obj["exists"] != False:
  print(list_obj["exists"])
else: 
  print("La lista que ingresaste no funciona")
