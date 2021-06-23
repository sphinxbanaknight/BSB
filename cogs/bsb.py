import discord
import random
import os
from itertools import repeat
import pprint
import json
import gspread
import pprint
#import models
import io
from oauth2client import file as oauth_file, client, tools
from apiclient.discovery import build
from httplib2 import Http
import time
import datetime
import pytz
import asyncio
from pytz import timezone
from oauth2client.service_account import ServiceAccountCredentials
from discord.ext import commands, tasks

################ Channel, Server, and User IDs ###########################
sphinx_id = 108381986166431744
sk_server = 401186250335322113
bk_server = 691130488483741756
c_server = 800129405350707200
servers = [sk_server, bk_server, c_server]

sk_bot = 401212001239564288
bk_bot = 691205255664500757
bk_ann = 695801936095740024 #BK #announcement
c_bot = 800129405350707200
botinit_id = [sk_bot, bk_bot, c_bot]


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
'''
def zeroOut():
    cost.clear()
    trials.clear()
    for x in range(0, MAX_SIM):
        cost.append(0)
    for x in range(0, MAX_SIM):
        trials.append(0)
def refineBSB(n):
    global cost
    ctr = 0
    refine = 7
    while n < MAX_SIM:
        if refine != 9:
            RNG = random.random()
            if RNG >= 0 and RNG <= 0.4:
                if refine == 7:
                    cost[n] += BSB + Enriched
                else:
                    cost[n] += 2 * BSB + Enriched
                refine += 1
                ctr += 1
            else:
                if refine == 7:
                    cost[n] += BSB + Enriched
                else:
                    cost[n] += 2 * BSB + Enriched
                ctr += 1
                continue
        else:
            trials[n] = ctr
            ctr = 0
            refine = 7
            n += 1

def refineHD(n):
    global cost
    global trial
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

def refineHDBSB(n):
    global cost
    global trial
    flag = False
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
            if flag != True:
                if refine != 9:
                    if RNG >= 0 and RNG <= 0.4:
                        cost[n] += HD
                        refine += 1
                        ctr += 1
                    else:
                        flag = True
                        refine -= 1
                        cost[n] += HD
                        ctr += 1
                        continue
                else:
                    trials[n] = ctr
                    ctr = 0
                    refine = 7
                    n += 1
            else:
                if RNG >= 0 and RNG <= 0.4:
                    if refine == 7:
                        cost[n] += BSB + Enriched
                    else:
                        cost[n] += 2 * BSB + Enriched
                    refine += 1
                    ctr += 1
                    flag = False
                else:
                    if refine == 7:
                        cost[n] += BSB + Enriched
                    else:
                        cost[n] += 2 * BSB + Enriched
                    ctr += 1
                    continue'''

class Bsb(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(ctx):
        await ctx.channel.send(f"{client.latency}")
        '''
    zeroOut()
    refineBSB(0)
    totalCostBSB = 0
    totalTrialBSB = 0
    averageCostBSB = 0
    averageTrialBSB = 0
    for i in range(MAX_SIM):
        totalCostBSB += cost[i]
        totalTrialBSB += trials[i]
    averageCostBSB = totalCostBSB/MAX_SIM
    #print(cost)
    print(f"Based on {MAX_SIM} simulations.")
    print(f'Average cost for BSB+Enri from +7 to +9: {averageCostBSB}')
    averageTrialBSB = totalTrialBSB/MAX_SIM
    #print(trials)
    print(f'Average trial for BSB+Enri from +7 to +9: {averageTrialBSB}')

    zeroOut()
    refineHD(0)
    totalCostHD = 0
    totalTrialHD = 0
    averageCostHD = 0
    averageTrialHD = 0
    for i in range(MAX_SIM):
        totalCostHD += cost[i]
        totalTrialHD += trials[i]
    averageCostHD = totalCostHD/MAX_SIM
    print(f"Based on {MAX_SIM} simulations.")
    print(f'Average cost for HD from +7 to +9: {averageCostHD}')
    averageTrialHD = totalTrialHD/ MAX_SIM
    # print(trials)
    print(f'Average trial for HD from +7 to +9: {averageTrialHD}')

    zeroOut()
    refineHDBSB(0)
    totalCostHDBSB = 0
    totalTrialHDBSB = 0
    averageCostHDBSB = 0
    averageTrialHDBSB = 0
    for i in range(MAX_SIM):
        totalCostHDBSB += cost[i]
        totalTrialHDBSB += trials[i]
    averageCostHDBSB = totalCostHDBSB / MAX_SIM
    print(f"Based on {MAX_SIM} simulations.")
    print(f'Average cost for HD+BSB from +7 to +9: {averageCostHDBSB}')
    averageTrialHDBSB = totalTrialHDBSB / MAX_SIM
    # print(trials)
    print(f'Average trial for HD+BSB from +7 to +9: {averageTrialHDBSB}')'''
def setup(client):
    client.add_cog(Bsb(client))