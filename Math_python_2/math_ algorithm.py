def function_with_graf(intersection_points_x: list ,intersection_points_y: list):
    """Определяет уравнения по графику """
    import numpy as np
    coefficient_matrix = []
    equation_ector = []

    for x,y in zip(intersection_points_x,intersection_points_y): # цыкл проходит по всем точками x и y
        coefficient_matrix.append([x**2,x,1]) # записывает в  coefficient_matrix x в виде квадратного уравнения 
        equation_ector.append(y) # записывает в  equation_ecto y

    A = np.array(coefficient_matrix) # Создания array A из coefficient_matrix
    B = np.array(equation_ector) # Создания array И из equation_ector
    ans = np.linalg.solve(A,B) # считает систему уравнения матричным способам. Подробние про этот способ есть на этом сайте https://github.com/Coursera-machine-learning-data-analysis/1/blob/master/1.ipynb
    ans = list(ans)

    if abs(ans[1]) == ans[1]: # Определяет какой знак стоит перед ans[1]
        plus_minus_1 = '+'
    else:
        plus_minus_1 = '-'
    if abs(ans[2]) == ans[2]: # Определяет какой знак стоит перед ans[2]
        plus_minus_2 = '+'
    else:
        plus_minus_2 = '-'

    print(f"{ans[0]}*x**2 {plus_minus_1} {ans[1]}*x {plus_minus_2} {ans[2]} ") # Ввыводит уравнения в виде строки 