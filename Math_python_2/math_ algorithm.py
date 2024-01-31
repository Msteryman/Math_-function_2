import numpy as np
from math_python import math_python

def function_with_graf(intersection_points_x: list ,intersection_points_y: list):
    """Определяет уравнения по графику """


    coefficient_matrix = []
    equation_ector = []

    for x,y in zip(intersection_points_x,intersection_points_y): # цыкл проходит по всем точками x и y
        coefficient_matrix.append([x**2,x,1]) # записывает в coefficient_matrix x в виде квадратного уравнения 
        equation_ector.append(y) # записывает в  equation_ecto y

    A = np.array(coefficient_matrix) # Создания array A из coefficient_matrix
    B = np.array(equation_ector) # Создания array И из equation_ector
    print(A,B)
    ans, residuals, rank, s = np.linalg.lstsq(A, B, rcond=None) # считает систему уравнения матричным способам. Подробние про этот способ есть на этом сайте https://github.com/Coursera-machine-learning-data-analysis/1/blob/master/1.ipynb
    ans = list(ans)
    print(ans)

    print(f"{round(ans[0])}*x**2 + {round(ans[1])}*x + {round(ans[2])} ") # Выводит уравнения в виде строки 


def points_on_a_graph_by_y(x_list: np.ndarray or list,  y_list: np.ndarray or list, gn_coord: list):#  x_lis Это все точки x в функций a y_list Это все точки y в функций.  gn_coord Это список со значения y с x которых вы хотите составить систему уравнения 
  """ Находит точки пересечения всех x cо списком y который был задан""" 

 
  coordinate_x = []
  coordinate_y = []
  ypoints = list(y_list)
  xpoints = list(x_list)

  for coord_y in gn_coord: # Проходим по списку gn_coord
    x_2 = []

    for y_len in range(len(ypoints)-1): # Проходим по списку ypoints

        if round(ypoints[y_len]) == coord_y: # Сравниваем round(ypoints[y_len]) с coord_y
          x_2.append(y_len)
    
    coordinate_x.append(xpoints[x_2[0]])
    coordinate_x.append(xpoints[x_2[-1]])

    coordinate_y.append(ypoints[x_2[0]])
    coordinate_y.append(ypoints[x_2[-1]])
  return(coordinate_x,coordinate_y)

gn_coord = [] # сюда надо загнать точки y для который вы хотите 
x = [] # сюда надо загнать все значения x в графике 
y = [] # сюда надо загнать все значения y в графике 


math_python(function_with_graf(x,y,gn_coord),-6,6,0.0001)
