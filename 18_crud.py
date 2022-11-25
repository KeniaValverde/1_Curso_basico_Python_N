#CRUD Create, Read, Update and Delete.

#reemplazar un dato -1 es la ultima posicion
numbers = [1, 2, 3, 4, 5]
print(numbers[1])
numbers[-1] = 10
print(numbers)

#agrega el dato entre () en la ultima posicion de la lista
numbers.append(700)
print(numbers)

#insert nos ayuda a cambiar un dato,en este ejemplo
#hola se insertara o se reescribira en la posicion 0
numbers.insert(0,'hola')
print(numbers)

#este reescribira la posicion 3
numbers.insert(3, 'change')
print(numbers)

#aqui estamos uniendo 2 listas para crear una nueva
tasks = ['todo 1', 'todo 2', 'todo 3']
new_list = numbers + tasks 
print(new_list)

#para saber que posicion tiene un dato en una lista
index = new_list.index('todo 2')
new_list[index] = 'todo changed'
print(new_list)

#eliminar un dato de la lista
new_list.remove('todo 1')
print(new_list)

#pop eliminara el ultimo elemnto de la lista
new_list.pop()
print(new_list)

# a pop le podemos especificar que elemto va a eliminar
#(0) eliminara el elemento en esa posicion
new_list.pop(0)
print(new_list)

#reverse cambia la posicion de los elementos en el array
#los ultimos se hacen primeros y viceversa
new_list.reverse()
print(new_list)

#sort nos ordena de menor a mayor 
#y con strings ordena por orden alfabetico
numbers_a = [1,4,6,3]
numbers_a.sort()
print(numbers_a)

strings = ['re','ab','ed']
strings.sort()
print(strings)

#sort no puede ordenar cuando hay elemntos mezclados
new_list.sort()