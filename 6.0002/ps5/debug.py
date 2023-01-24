import numpy as np
import random
import pylab as pl
import ps5

# random.seed(0.3101475693193326)

# def test_eval():
#     x = np.linspace(1, 50, 50)
#     y = [0] * len(x)
#     y = np.array(y, dtype = float)
#     r = random.random()
#     print(r)
#     for i in range(round(r * 50)):
#         print(i)
#         y += round(r * 100) * (x ** (i / 10))
#     y += random.gauss(0, 10000000000)
#     y = np.log(y)
#     pl.plot(x, y, 'o')
#     pl.show()
#     degrees = np.linspace(1, 20, 20)
#     models = ps5.generate_models(x, y, degrees)
#     ps5.evaluate_models_on_training(x, y, models)
    
 
def test_eval():
    x = np.linspace(1, 20, 20)
    r = round(random.random() * random.choice(np.linspace(1, 5, 5))) + random.choice(np.linspace(1, 3, 3))
    y = x ** r
    for i in range(len(y)):
        y[i] += random.gauss(0, 50)
    pl.plot(x, y, 'o')
    pl.show()
    degrees = np.linspace(1, 20, 20)
    models = ps5.generate_models(x, y, degrees)
    ps5.evaluate_models_on_training(x, y, models)
    
test_eval()