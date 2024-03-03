def simple_iteration_method(x, y, tolerance):
    iterations = 0
    max_iterations = 1000  # Максимальна кількість ітерацій
    while True:
        x_new = (1 - x * (y ** 3) - y ** 4) * (x ** (-3))
        y_new = (x ** 2 + y * x - 1) / y

        if abs(x_new - x) < tolerance and abs(y_new - y) < tolerance:
            break

        x, y = x_new, y_new
        iterations += 1

        if iterations >= max_iterations:
            print("Досягнута максимальна кількість ітерацій.")
            break

    return x, y, iterations

# Задані значення
x_initial = 0.9
y_initial = 0.6

# Обчислення з точністю 0.01
tolerance_01 = 0.01
x_solution_01, y_solution_01, iterations_01 = simple_iteration_method(x_initial, y_initial, tolerance_01)
print(f"Результат для точності {tolerance_01}: x = {x_solution_01}, y = {y_solution_01}, кількість ітерацій = {iterations_01}")
