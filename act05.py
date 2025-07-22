sales = []
while True:
      print("--------MENU DE VENTAS--------\n"
            "1.Ingresar lista de valores\n"
            "2. Mostrar las ventas\n"
            "3. calcular la venta mas alta y la venta mas baja\n"
            "4. calcular promedio\n"
            "5. contar cuantos dias superaron los Q1000\n"
            "6. Buscar una venta especifica\n"
            "7. clasificar cada venta\n"
            "8. Salir ")
      option = input("Ingrese una opcion: ")
      match option:
            case "1":
                  n = int(input("Ingrese la lista de ventas: "))
                  for i in range(n):
                        print("La(s) venta(s) se han agregado")
                      sales.append(n)
            case "2":
                  print(sales)
            case "3":
                  print(f"la venta mas alta es: ")