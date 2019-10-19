#!/usr/bin/env python3

import os
import random
import discord
from discord.ext import commands

MINE = ':boom:'
NUMBERS = [':zero:',':one:',':two:',':three:',':four:',':five:',':six:',':seven:',':height:']

size = 10
mines_number = 10

bot = commands.Bot(command_prefix='/')

@bot.command()
async def demineur(ctx):
	grid = [None] * (size*size)
	for mine in range(0, mines_number):
		grid[random.randrange(0, len(grid))] = MINE;
	for case in range(0, len(grid)):
		if grid[case] != MINE:
			number = 0
			to_check = [(case-size)-1,(case-size),(case-size)+1,case-1,case+1,(case+size)-1,(case+size),(case+size)+1]
			for cursor in to_check:
				if cursor >= 0 and cursor < len(grid):
					if grid[cursor] == MINE:
						number += 1
			grid[case] = NUMBERS[number]
	value = ''
	for line in range(0, size):
		line_value = ''
		for case in range(0, size):
			line_value += '||'+grid[(line*size)+case]+'||'
		value += line_value + '\n'
	await ctx.send(value)

bot.run(os.environ['discord_bot_token'])