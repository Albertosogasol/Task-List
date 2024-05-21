import os

# Clase Tarea
class Task:
    def __init__(self, name, done=False):
        self.name = name
        self.done = done

    def get_name(self):
        return self.name
    
    def get_status(self):
        return "Finalizada" if self.done else "Pendiente"

# Clase Lista de Tareas    
class TaskList:
    def __init__(self):
        self.task_list = []

    def add_task(self, name):
        new_task = Task(name)
        self.task_list.append(new_task)
        print(f"Tarea '{name}' añadida con éxito.")

    def complete_task(self, pos):
        try:
            task = self.task_list[pos]
            task.done = True
            print(f"La tarea '{task.name}' ha sido completada.")
        except IndexError:
            print("La posición indicada no es válida!")

    def show_tasks(self):
        if not self.task_list:
            print("No hay tareas en la lista.")
            return
        for idx, task in enumerate(self.task_list, start=1):
            print(f"{idx}. {task.get_name()} --> {task.get_status()}")
    
    def delete_task(self, pos):
        try:
            task = self.task_list.pop(pos)
            print(f"La tarea '{task.name}' ha sido eliminada con éxito.")
        except IndexError:
            print("La posición indicada no es válida!")

# Función para limpiar la consola
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Función principal
def main():
    task_list = TaskList()
    while True:
        try:
            print("\n--- Gestión de Tareas ---")
            print("1. Agregar tarea")
            print("2. Marcar tarea como completada")
            print("3. Mostrar todas las tareas")
            print("4. Eliminar tarea")
            print("5. Salir")

            choice = int(input("Seleccione una opción: "))

            if choice == 1:
                name = input("Inserte la descripción de la tarea: ")
                task_list.add_task(name)
            elif choice == 2:
                task_list.show_tasks()
                try:
                    task_number = int(input("Seleccione el número de la tarea a completar: ")) - 1
                    task_list.complete_task(task_number)
                except ValueError:
                    print("Por favor, introduzca un número válido.")
            elif choice == 3:
                task_list.show_tasks()
            elif choice == 4:
                task_list.show_tasks()
                try:
                    task_number = int(input("Seleccione el número de la tarea a eliminar: ")) - 1
                    task_list.delete_task(task_number)
                except ValueError:
                    print("Por favor, introduzca un número válido.")
            elif choice == 5:
                print("Hasta pronto!")
                break
            else:
                print("Por favor, seleccione una opción válida del 1 al 5.")
        except ValueError:
            print("Por favor, introduzca un número válido.")
        finally:
            input("\nPresione Enter para continuar...")
            clear_console()

# Ejecución del programa
if __name__ == '__main__':
    main()
