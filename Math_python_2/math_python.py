def math_python(Equations: str,border_1: int,border_2: int,steps: int):
    """Рисует график по уравнению"""
    import matplotlib.pyplot as plt
    import numpy as np
    import os
    os.system('cls')

    x = np.arange(border_1,border_2,steps)
    ypoints = eval(Equations)
    plt.plot(x, ypoints)
    plt.grid(True)
    plt.show()

    return(x,ypoints)

X,Y = (math_python('12.000000000000027*x**2 + 5.000000000000012*x + -5.000000000000023',-2,1.6,0.0005))
print(list(X))