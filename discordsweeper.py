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
async def demineur(ctx):  # Init Discord bot command

	grid = [None] * (size*size)  # Generate grid

	for mine in range(0, mines_number):  # For numbers of mines desired
		grid[random.randrange(0, len(grid))] = MINE;  # Place mine randomly

	for case in range(0, len(grid)):  # For each case of grid
		if grid[case] != MINE:  # If it's not a mine
			number = 0  # Init counter for mines around
			to_check = [  # List all case around the current
				(case-size)-1,	# Top left
				(case-size),	# Top
				(case-size)+1,	# Top right
				case-1,			# Left
				case+1,			# Right
				(case+size)-1,	# Bottom left
				(case+size),	# Bottom
				(case+size)+1	# Bottom right
			]
			for cursor in to_check:  # For each case to check
				if cursor >= 0 and cursor < len(grid):  # If not outside the grid
					if grid[cursor] == MINE:  # If it's a mine
						number += 1  # Add the mine to the counter

			grid[case] = NUMBERS[number]  # After all cases around checked, write the counter value in current case

	value = ''  # Init Discord message value

	for line in range(0, size):  # Each line of grid
		line_value = ''  # Init line value
		for case in range(0, size):  # For each cases of this line
			line_value += '||'+grid[(line*size)+case]+'||'  # Add case value in spoiler
		value += line_value + '\n'  # Add line to global message with line break

	await ctx.send(value)  # Send message

bot.run(os.environ['discord_bot_token'])  # Start bot