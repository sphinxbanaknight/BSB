import discord
import asyncio
import random
#from oauth2client import file as oauth_file, client, tools
from discord.ext import commands, tasks
import os

BSB = 5.8 * 10 ** 6
Enriched = 500 * 10 ** 3
HD = 1.5 * 10 ** 6

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


class Bsb(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def pong(self, ctx):
        await ctx.channel.send(f"{client.latency}")

    @commands.command()
    async def refineHD(self, ctx, *, arguments):
        channel = ctx.message.channel
        commander = ctx.author
        commander_name = commander.name

        if not channel.id in botinit_id:
            await ctx.send("Wrong channel! Please use #bot.")
            return

        arglist = [x.strip() for x in arguments.split(',')]
        no_of_args = len(arglist)

        if no_of_args < 1 or no_of_args > 1:
            await ctx.send(f"/refineHD 1 - 100000")
            return

        cost = []
        MAX_SIM = int(arglist[0])
        print(arglist[0])
        for x in range(0, MAX_SIM):
            cost.append(0)
        trials = []
        for x in range(0, MAX_SIM):
            trials.append(0)

        ctr = 0
        n = 0
        refine = 7

        while n < MAX_SIM:
            await ctx.send("Hi")
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

        totalCostHD = 0
        totalTrialHD = 0
        averageCostHD = 0
        averageTrialHD = 0
        for i in range(MAX_SIM):
            totalCostHD += cost[i]
            totalTrialHD += trials[i]
        averageCostHD = totalCostHD / MAX_SIM
        await ctx.send(f"Based on {MAX_SIM} simulations.")
        await ctx.send(f'Average cost for HD from +7 to +9: {averageCostHD}')
        averageTrialHD = totalTrialHD / MAX_SIM
        # print(trials)
        await ctx.send(f'Average trial for HD from +7 to +9: {averageTrialHD}')

    @commands.command()
    async def refineBSB(self, ctx, *, arguments):
        channel = ctx.message.channel
        commander = ctx.author
        commander_name = commander.name

        if not channel.id in botinit_id:
            await ctx.send("Wrong channel! Please use #bot.")
            return

        arglist = [x.strip() for x in arguments.split(',')]
        no_of_args = len(arglist)

        if no_of_args < 1 or no_of_args > 1:
            await ctx.send(f"/refineBSB 1 - 100000")
            return

        cost = []
        MAX_SIM = int(arglist[0])
        for x in range(0, MAX_SIM):
            cost.append(0)
        trials = []
        for x in range(0, MAX_SIM):
            trials.append(0)

        ctr = 0
        n = 0
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

        totalCostBSB = 0
        totalTrialBSB = 0
        averageCostBSB = 0
        averageTrialBSB = 0
        for i in range(MAX_SIM):
            totalCostBSB += cost[i]
            totalTrialBSB += trials[i]
        averageCostBSB = totalCostBSB / MAX_SIM
        # print(cost)
        await ctx.send(f"Based on {MAX_SIM} simulations.")
        await ctx.send(f'Average cost for BSB+Enri from +7 to +9: {averageCostBSB}')
        averageTrialBSB = totalTrialBSB / MAX_SIM
        # print(trials)
        await ctx.send(f'Average trial for BSB+Enri from +7 to +9: {averageTrialBSB}')

    @commands.command()
    async def refineHDBSB(self, ctx, *, arguments):
        channel = ctx.message.channel
        commander = ctx.author
        commander_name = commander.name

        if not channel.id in botinit_id:
            await ctx.send("Wrong channel! Please use #bot.")
            return

        arglist = [x.strip() for x in arguments.split(',')]
        no_of_args = len(arglist)

        if no_of_args < 1 or no_of_args > 1:
            await ctx.send(f"/refineHDBSB 1 - 100000")
            return

        cost = []
        MAX_SIM = int(arglist[0])
        for x in range(0, MAX_SIM):
            cost.append(0)
        trials = []
        for x in range(0, MAX_SIM):
            trials.append(0)

        ctr = 0
        n = 0
        refine = 7
        flag = False

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
                        continue
        totalCostHDBSB = 0
        totalTrialHDBSB = 0
        averageCostHDBSB = 0
        averageTrialHDBSB = 0
        for i in range(MAX_SIM):
            totalCostHDBSB += cost[i]
            totalTrialHDBSB += trials[i]
        averageCostHDBSB = totalCostHDBSB / MAX_SIM
        await ctx.send(f"Based on {MAX_SIM} simulations.")
        await ctx.send(f'Average cost for HD+BSB from +7 to +9: {averageCostHDBSB}')
        averageTrialHDBSB = totalTrialHDBSB / MAX_SIM
        # print(trials)
        await ctx.send(f'Average trial for HD+BSB from +7 to +9: {averageTrialHDBSB}')
def setup(client):
    client.add_cog(Bsb(client))
