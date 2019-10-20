#!/usr/bin/env python3

import os
import random
import discord
from discord.ext import commands

MINE = ':boom:'
NUMBERS = [':zero:',':one:',':two:',':three:',':four:',':five:',':six:',':seven:',':height:']
SPOILER = '||'

size = 10
mines_number = 10

bot = commands.Bot(command_prefix='/')

@bot.command()
async def demineur(ctx, mines_number: int = 10, size: int = 5, show_grid: bool = False):  # Init Discord bot command
	
	response = ''  # Init Discord message value

	if size <= 0 or size > 12:
		response = "Wow ! That's a huge grid, I don't feel able to do that :pensive:"
	elif mines_number < 0 or mines_number > (size*size):
		response = "WTF !?! You sure ? :thinking:"
	else:
		grid = [None] * (size*size)  # Generate grid

		for mine in range(0, mines_number):  # For numbers of mines desired
			grid[random.randrange(0, len(grid))] = MINE;  # Place mine randomly

		for case in range(0, len(grid)):  # For each case of grid
			if grid[case] != MINE:  # If it's not a mine
				number = 0  # Init counter for mines around

				# Check placement on line to not check case on other side of grid
				placement_on_line = (case%size)
				place_on_left = (len(grid*2)) if placement_on_line == 0 else 1
				place_on_right = (len(grid*2)) if placement_on_line == (size - 1) else 1

				to_check = [  # List all case around the current
					(case-size)-place_on_left,	# Top left
					(case-size),				# Top
					(case-size)+place_on_right,	# Top right
					case-place_on_left,			# Left
					case+place_on_right,		# Right
					(case+size)-place_on_left,	# Bottom left
					(case+size),				# Bottom
					(case+size)+place_on_right	# Bottom right
				]
				for cursor in to_check:  # For each case to check
					if cursor >= 0 and cursor < len(grid):  # If not outside the grid
						if grid[cursor] == MINE:  # If it's a mine
							number += 1  # Add the mine to the counter

				grid[case] = NUMBERS[number]  # After all cases around checked, write the counter value in current case

		for line in range(0, size):  # Each line of grid
			line_value = ''  # Init line value
			for case in range(0, size):  # For each cases of this line
				tag = '' if show_grid else SPOILER
				line_value += tag+grid[(line*size)+case]+tag  # Add case value in spoiler
			response += line_value + '\n'  # Add line to global message with line break

	await ctx.send(response)  # Send message

bot.run(os.environ['discord_bot_token'])  # Start bot