from basedatos import crear_base, SessionLocal
import crud

def menu():
    print("=== GESTOR DE CATÁLOGO ===")
    print("1. Crear categoría")
    print("2. Ver categorías")
    print("3. Editar categoría")
    print("4. Eliminar categoría")
    print("5. Crear producto")
    print("6. Ver productos")
    print("7. Editar producto")
    print("8. Eliminar producto")
    print("9. Salir")

def main():
    crear_base()
    db = SessionLocal()


    while True:
        menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre de la categoría: ")
            crud.crear_categoria(db, nombre)

        elif opcion == "2":
            categorias = crud.obtener_categorias(db)
            for c in categorias:
                print(f"{c.id}: {c.nombre}")

        elif opcion == "3":
            id_cat = int(input("ID de la categoría a editar: "))
            nuevo_nombre = input("Nuevo nombre: ")
            crud.actualizar_categoria(db, id_cat, nuevo_nombre)

        elif opcion == "4":
            id_cat = int(input("ID de la categoría a eliminar: "))
            crud.eliminar_categoria(db, id_cat)

        elif opcion == "5":
            nombre = input("Nombre del producto: ")
            desc = input("Descripción: ")
            crud.crear_producto(db, nombre, desc)

        elif opcion == "6":
            productos = crud.obtener_productos(db)
            for p in productos:
                print(f"{p.id}: {p.nombre} - {p.descripcion}")

        elif opcion == "7":
            id_prod = int(input("ID del producto a editar: "))
            nombre = input("Nuevo nombre: ")
            desc = input("Nueva descripción: ")
            crud.actualizar_producto(db, id_prod, nombre, desc)

        elif opcion == "8":
            id_prod = int(input("ID del producto a eliminar: "))
            crud.eliminar_producto(db, id_prod)

        elif opcion == "9":
            print("Saliendo...")
            break

        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()