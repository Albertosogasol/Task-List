'''
Escribe un programa en Python utilizando Programación Orientada a Objetos que gestione una lista de tareas pendientes. El programa deberá permitir al usuario realizar las siguientes operaciones:
    • Agregar una nueva tarea: El programa deberá permitir al usuario agregar una nueva tareaa
    la lista de tareas pendientes.
    • Marcar una tarea como completada: El programa deberá permitir al usuario marcar una tarea como completada, dada su posición en la lista.
    • Mostrar todas las tareas: El programa deberá imprimir en pantalla todas las tareas pendientes, numeradas y mostrando su estado (completada o pendiente).
    • Eliminar una tarea: El programa deberá permitir al usuario eliminar una tarea de la lista, dada su posición.
El programa deberá incluir las siguientes características:
    • Manejo de excepciones: El programa deberá manejar excepciones en caso de que el usuario ingrese una opción no válida o una posición que no exista en la lista.
    • Comentarios explicativos: El código deberá estar comentado para explicar su
    funcionamiento en cada parte relevante.
'''
import os #Importar librería de S.O

#Clase Tarea
class Task:
    def __init__(self, name, done=False): #Inicializa una nueva tarea pasando el nombre por parámetro. 
        #El estado se inicializa sin finalizar
        self.name = name
        self.done = done

    def get_name(self): #Devuelve el nombre de la tarea
        return self.name
    
    def get_status(self): #Devuelve le estado de la tarea
        if self.done == True:
            return "Finalizada"
        else:
            return "Pendiente"

#Clase Lista de Tareas    
class Task_List:
    def __init__(self): #Método constructor
        #Inicializa una nueva lista vacía
        self.task_list = []

    def add_task(self, name): #Añade una nueva tarea a la lista
        new_task = Task(name)
        self.task_list.append(new_task)

    def completed_task(self,pos): #Marca la tarea como completada.
        #El argumento es la posición de la tarea
        try:
            task = self.task_list[pos]
            task.done = True
            print("La tarea '",task.name, "' ha sido completada." )
        except IndexError:
            print("La posición indicada no es válida")

    def show_tasks(self): #Muestra la lista de tareas
        counter = 1 #Contador para escribir en la lista
        for i in self.task_list: #Bucle que recorre la lista completa
            current_task = i #El objeto de tipo Task se almacena en una varaible temporal
            print(counter, ".- ", current_task.get_name(), " --> ", current_task.get_status(), sep="")
            counter += 1
    
    def del_task(self, pos): #Elimina la tarea en la posición pasada por argumento
        try:
            task = self.task_list[pos]
            deleted_task = self.task_list.pop(pos)
            print("La tarea", task.name, " ha sido eliminada con éxito")
        except IndexError:
            print("La posición indicada no es válida!")
            clear()

#Función para limpiar la consola
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#Función principal
def main():
    task_list = Task_List() #Instancia para crear una nueva lista al iniciar el programa
    while True: #Bucle para mantenerse dentro del programa
        try:
            print("\n--- Gestión de Tareas ---")
            print("1. Agregar tarea")
            print("2. Marcar tarea como completada")
            print("3. Mostrar todas las tareas")
            print("4. Eliminar tarea")
            print("5. Salir")

            choice = int(input("Seleccione una opción: ")) #Opción elegida

            if choice == 1: #Añadir tarea
                name = input("Inserte la descripción de la tarea: ")
                task_list.add_task(name)
                clear()
            elif choice == 2: #Marcar tarea como completada
                clear()
                print("Elija una tarea de la lista para marcar como completada: ")
                task_list.show_tasks()
                try:
                    task_number = int(input("Nº: "))
                    if task_number > 0:
                        task_list.completed_task(task_number - 1)
                        clear()
                    else:
                        print("Debe introducir un número de la lista")
                        press = input("\n\nPresione una tecla para continuar...")
                except ValueError:
                    print("Introduzca un número válido")
            elif choice == 3: #Mostrar todas las tareas
                clear()
                task_list.show_tasks()
                press = input("\n\nPresione una tecla para continuar...")
                clear()
            elif choice == 4: #Eliminar tarea
                clear()
                print("Elija una tarea de la lista para eliminarla: ")
                task_list.show_tasks()
                try:
                    task_number = int(input("Nº: "))
                    if task_number > 0:
                        task_list.del_task(task_number - 1)
                    else:
                        print("Debe introducir un número de la lista.")
                        press = input("\n\nPresione una tecla para continuar...")
                except ValueError:
                    print("Introduzca un número válido")
                    continue
            elif choice == 5: #Salir del programa
                print("Hasta pronto!")
                break
            else:
                clear()
                print("Introduzca un número de la lista!")
                continue
        except:
            clear()
            print("Introduzca un número de la lista!")
            continue

#Ejecución del programa
if __name__ == '__main__':
    #clear = lambda: os.system('cls') #Método para limpiar la consola cada vez que se invoca. Se añade para hacer un programa más limpio
    main() #Ejecutamos el programa principal