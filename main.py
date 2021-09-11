
from get_list import getList

list_input = input("Ingresa una lista hecha en Markdown:  ")
list = getList(list_input, ".md", "r+t")

print(list.read())