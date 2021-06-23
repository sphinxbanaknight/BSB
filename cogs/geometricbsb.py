import numpy as np

MAX_SIM = 100000

z = np.random.geometric(p=0.4, size=MAX_SIM)

print((((z==1).sum())/MAX_SIM)