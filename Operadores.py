def main():
    a = 25
    b = 6

    P_triangulo = 6 + 6 + 6
    P_cuadrado = 4 * b
    A_cuadrado = b * b
    P_rectangulo = 2 * a + 2 * b
    A_rectangulo = a * b

    print(f"El Perímetro de un triángulo de lado {b} es: {P_triangulo}")
    print(f"El Perímetro de un cuadrado de lado {b} es: {P_cuadrado}")
    print(f"El Área de un cuadrado de lado {b} es: {A_cuadrado}")
    print(f"El Perímetro de un rectángulo de lados {a} y {b} es: {P_rectangulo}")
    print(f"El Área de un rectángulo de lados {a} y {b} es: {A_rectangulo}")

if _name_ == "_main_":
    main()