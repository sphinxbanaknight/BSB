import math
import random
from itertools import repeat
random.seed(random.randint(0,1000))
MAX_SIM = 1 * 10 ** 2
cost = []
for x in range(0, MAX_SIM):
    cost.append(0)
trials = []
for x in range(0, MAX_SIM):
    trials.append(0)
BSB = 5.8 * 10 ** 6
Enriched = 500 * 10 ** 3
HD = 1.5 * 10 ** 6
#refine = 2k

def refineHD(n):
    global cost
    ctr = 0
    refine = 7
    while n < MAX_SIM:
        RNG = random.random()
        if refine == 7:
            if RNG >= 0 and RNG <= 0.4:
                cost[n] += BSB + Enriched
                refine += 1
                ctr += 1
            else:
                cost[n] += BSB + Enriched
                ctr += 1
                continue
        else:
            if refine != 9:
                if RNG >= 0 and RNG <= 0.4:
                    cost[n] += HD
                    refine += 1
                    ctr += 1
                else:
                    refine -= 1
                    cost[n] += HD
                    ctr += 1
                    continue
            else:
                trials[n] = ctr
                ctr = 0
                refine = 7
                n += 1


if __name__ == "__main__":
    refine(0)
    totalCost = 0
    totalTrial = 0
    averageCost = 0
    averageTrial = 0
    for i in range(MAX_SIM):
        totalCost += cost[i]
        totalTrial += trials[i]
    averageCost = totalCost/MAX_SIM
    #print(cost)
    print(f"Based on {MAX_SIM} simulations.")
    print(f'Average cost for HD from +7 to +9: {averageCost}')
    averageTrial = totalTrial/MAX_SIM
    #print(trials)
    print(f'Average trial for HD from +7 to +9: {averageTrial}')