import discord
import requests
import os
import sys
sys.dont_write_bytecode = True
import random
from discord.ext import commands
from keep_alive import keep_alive
import time
import flask
import subprocess
from replit import db
import datetime
import asyncio
import warnings
import logging

warnings.filterwarnings("ignore")

subprocess.Popen(['java', '-jar', 'Lavalink.jar'])
time.sleep(40)

r = requests.get("https://repl.it/@BArewrite/botpy#captchA.png")


OWNER_ID = [541722893747224589, 645405908309901322, 689802280102527124]


intents = discord.Intents.all()

client = commands.Bot(command_prefix=('b!', 'B!', 'ba!', 'BA!'), help_command=None, intents=intents)


@client.event
async def on_member_join(member):
    if member.guild.id == 707183075624353952:
        channel = client.get_channel(712997663129468998)
        channel1 = client.get_channel(712955612467691520)
        em = discord.Embed(color=0xff0000)
        em.add_field(name="New Member!", value=f"Welcome to British Airways {member.name}\nPlease make sure to read our {channel1.mention}\nchannel to familiarize yourself with the rules and to be able to have fun!")
        em.set_footer(icon_url=member.avatar_url, text="British Airways Celebrating 500 members! To fly to serve")
        await channel.send(embed=em)

@client.event
async def on_member_remove(member):
    if member.guild.id == 707183075624353952:
        channel = client.get_channel(712997663129468998)
        await channel.send(
            f"Seems that {member.name} hasn't been enjoy British Airways lately,\n we hope to see him back again!\n**British Airways to fly to serve**"
        )

async def logger():
    logging.basicConfig(filename="log.txt", filemode="a", format="%(asctime)s %(msecs)d- %(process)d -%(levelname)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S %p", level=logging.INFO)

    channel = client.get_channel(768261473415594004)
    tn = datetime.datetime.utcnow()
    await channel.send(f'{tn.strftime("%c")} log, timezone: UTC', file=discord.File('log.txt'))
    with open("log.txt", "r+") as f:
        f.truncate()
    with open("./logs/spring.log", "r") as r:
        await channel.send(file=discord.File("spring.log"))
        r.truncate()
    await asyncio.sleep(10)
    
    client.loop.create_task(logger())
    client.loop_task(logger())

@client.event
async def on_ready():
    logging.basicConfig(filename="log.txt", filemode="a", format="%(asctime)s %(msecs)d- %(process)d -%(levelname)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S %p", level=logging.INFO)

    channel = client.get_channel(768261473415594004)
    tn = datetime.datetime.utcnow()
    await channel.send(f'{tn.strftime("%c")} log, timezone: UTC', file=discord.File('log.txt'))
    #await channel.send(file=discord.File("spring.log"))
    with open("log.txt", "r+") as f:
        f.truncate()
    #with open("./logs/spring.log", "r") as r:
        #r.truncate()
    await client.change_presence(
	    activity=discord.Activity(
	        type=discord.ActivityType.watching,
	        name=f'over British Airways!'))
    print('Bot Started')


    for filename in os.listdir('./cogs'):
	    if filename.endswith('.py'):
		    client.load_extension(f'cogs.{filename[:-3]}')
		    print(f'loading {filename}')

@client.event
async def on_command_error(ctx, error):
  embed = discord.Embed(color=0xff0000)
  if isinstance(error, commands.CommandNotFound):
    emv = "I can't find that command!"
  elif isinstance(error, commands.CommandOnCooldown):
    emv = "You are on cooldown, try again in {} seconds".format(error.retry_after)
  elif isinstance(error, commands.MessageNotFound):
    emv = "I can't find that message!"
  elif isinstance(error, commands.MemberNotFound) or isinstance(error, commands.UserNotFound):
    emv = "I can't find that user!"
  elif isinstance(error, commands.ChannelNotFound):
    emv = "I can't find that channel!"
  elif isinstance(error, commands.ChannelNotReadable):
    emv = "I don't have acces to read anything in that channel!"
  elif isinstance(error, commands.RoleNotFound):
    emv = "I can't find that role!"
  elif isinstance(error, commands.EmojiNotFound):
    emv = "I can't find that emoji!"
  elif isinstance(error, commands.MissingPermissions):
    emv = f"You don't have {error.missing_perms} permission(s) to run this command!"
  elif isinstance(error, commands.MissingRole):
    emv = f"You dont have {error.missing_role} role(s) to run this command!"
  elif isinstance(error, commands.MissingRequiredArgument):
    emv = "You didn't pass a required argument!"
  else:
    emv = "Unknown error occured!"
  embed.add_field(name="Oh no!", value=emv)
  await ctx.send(embed=embed)
  raise error
  logging.error(error)
  print(error)

@client.event
async def on_message(message):
  mention = message.mentions
  filter = [
	    'nigger', 'negro', 'https://pornhub.com', 'Nigger', 'NiGgEr', 'nIgGeR', 'https://pornhub.com/', 'pornhub.com', 'Pornhub.com', 'porn', 'Porn', 'Https://www.xnxx.com', 'https://www.xnxx.com', 'https://www.xnxx.com/', 'https://xvideos.com/',
        'https://www.xhamster.com/', 'https://www.redtube.com','https://www.redtube.com/','https://www.xhamster.com'
	]

  for word in filter:
    if message.content.count(word) > 0:
      print("%s Has said a bad word" % (message.author.name))
      await message.channel.purge(limit=1)
      await message.channel.send(
			    "%s Please don't say racist stuff like that" %
			    (message.author.name))
  for m in mention:
    try:
      val = db[m.id]
      await message.channel.send(f"{m.name} is AFK: {val}")
    except:
      print("passed")
  await client.process_commands(message)


@client.event
async def convert(ctx, argument):
	argument = await commands.MemberConverter().covert(ctx, argument)
	permission = argument.guild_permissions.manage_messages


@client.command()
async def softban(ctx, member: discord.Member, reason=None):
	if not member:
		return await ctx.send("Please specify a member")
	try:
		await ctx.member.ban(reason=reason)
		await ctx.send(f"{member.mention} has been softbanned")
	except discord.Forbidden:
		return await ctx.send("Something went wrong")


@client.command()
@commands.has_permissions(manage_messages=True)
async def poll(ctx, *args):
	mesg = ' '.join(args)
	await ctx.message.delete()
	embed = discord.Embed(title=":ballot_box: Poll", colour=0xff0000)
	embed.add_field(name="Question", value=mesg, inline=True)
	message = await ctx.send(embed=embed)
	await message.add_reaction(str('✅'))
	await message.add_reaction(str('❌'))


#@client.command()
#async def flight(ctx, *, message):
#	await ctx.message.delete()
#	number = random.randint(1, 5000)
#	embed = discord.Embed(colour=0xff0000)
#
#	embed.add_field(name=f"<:BritishAirwaysPTFS:740807866218446898> BA Flight {number}\n", value="{}" .format(message))
#
#	embed.set_footer(text="British Airways.\n*To fly to serve*")
#	await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(manage_messages=True)
async def flight(ctx, flnumber, dptr, arrvl, aircraft):
	flnots = 717681307483635722
	flight = discord.Embed(
	    title=
	    f"<:BA1:761894114484420609><:BA2:761894114785755176><:BA3:761894115087482930> British Airways Flight {flnumber}",
	    description=
	    f"Departure Airport: {dptr} \nArrival Airport: {arrvl} \n\nTodays Aircraft: {aircraft} \nTime Of Flight Is 3:00 PM /10:00 PM \nTimezone is BST/GMT+8 \n\nFirst Class: <:FirstClass:757170500454580224>\nBusiness Class: <:BusinessClass:757171994121732157>\nEconomy Class: <:GreatBritain:714843928431558676>\n\n Listing of passengers ends **30 minutes before flight**!\n-------------\n",
	    colour=0xff0000)
	flight.set_footer(text=f"To fly, to serve!")
	msg = await ctx.send(f"<@&717681307483635722>", embed=flight)

	await msg.add_reaction(emoji="<:FirstClass:757170500454580224>")
	await msg.add_reaction(emoji="<:BusinessClass:757171994121732157>")
	await msg.add_reaction(emoji="<:GreatBritain:714843928431558676>")


@client.command()
@commands.has_permissions(manage_messages=True)
async def boarding(ctx, flnumber, airport, gate):
	value = db["serverlink"]
	boarding = discord.Embed(
	    title=
	    f"<:BA1:761894114484420609><:BA2:761894114785755176><:BA3:761894115087482930> British Airways Flight {flnumber}",
	    description=
	    f"Flight {flnumber} is now boarding at:\n \n- Airport: {airport} \n- Gate: {gate} \n-------------------\n {value} \n-------------------\nPlease join VC for a better experience, \nthere's no need for a mic!\n-------------------",
	    colour=0xff0000)
	boarding.set_footer(text="To fly, to serve!")
	boarding.set_thumbnail(
	    url=
	    "http://logok.org/wp-content/uploads/2014/04/British-Airways-logo-ribbon-logo-880x660.png"
	)
	await ctx.send(f"<@&717681307483635722>", embed=boarding)


@client.command()
@commands.has_permissions(administrator=True)
async def serverlink(ctx, *, link):
		db["serverlink"] = link
		await ctx.send("done :thumbsup:")


@client.command()
@commands.has_permissions(manage_messages=True)
async def flightNA(ctx, flnumber, dptr, arrvl, aircraft):
	flnots = 717681307483635722
	flight = discord.Embed(
	    title=
	    f"<:BA1:761894114484420609><:BA2:761894114785755176><:BA3:761894115087482930> British Airways Flight {flnumber}",
	    description=
	    f"Departure Airport: {dptr} \nArrival Airport: {arrvl} \n\nTodays Aircraft: {aircraft} \nTime Of Flight Is 6:00PM \nTimezone is CST\n\nFirst Class: <:FirstClass:757170500454580224>\nBusiness Class: <:BusinessClass:757171994121732157>\nEconomy Class: <:GreatBritain:714843928431558676>\n\n Listing of passengers ends **30 minutes before flight**!\n-------------\n",
	    colour=0xff0000)
	flight.set_footer(text=f"To fly, to serve!")
	msg = await ctx.send(f"<@&717681307483635722>", embed=flight)

	await msg.add_reaction(emoji="<:FirstClass:757170500454580224>")
	await msg.add_reaction(emoji="<:BusinessClass:757171994121732157>")
	await msg.add_reaction(emoji="<:GreatBritain:714843928431558676>")

@client.command()
async def gstart(ctx, mins : int, * , prize: str):
    embed = discord.Embed(title = "Giveaway!", description = f"{prize}", color = ctx.author.color)

    end = datetime.datetime.utcnow() + datetime.timedelta(seconds = mins*60) 

    embed.add_field(name = "Ends At:", value = f"{end} UTC")
    embed.set_footer(text = f"Ends {mins} mintues from now!")

    my_msg = await ctx.send(embed = embed)


    await my_msg.add_reaction("🎉")


    await asyncio.sleep(mins*60)


    new_msg = await ctx.channel.fetch_message(my_msg.id)


    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(client.user))

    winner = random.choice(users)

    await ctx.send(f"Congratulations! {winner.mention} won {prize}!")

def convert(time):
    pos = ["s","m","h","d"]

    time_dict = {"s" : 1, "m" : 60, "h" : 3600 , "d" : 3600*24}

    unit = time[-1]

    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2


    return val * time_dict[unit]

@client.command()
async def giveaway(ctx):
    await ctx.send("Let's start with this giveaway! Answer these questions within 60 seconds!")

    questions = ["Which channel should it be hosted in?", 
                "What should be the duration of the giveaway? (s|m|h|d)",
                "What is the prize of the giveaway?"]

    answers = []

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel 

    for i in questions:
        await ctx.send(i)

        try:
            msg = await client.wait_for('message', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send('You didn\'t answer in time, please be quicker next time!')
            return
        else:
            answers.append(msg.content)
    try:
        c_id = int(answers[0][2:-1])
    except:
        await ctx.send(f"You didn't mention a channel properly. Do it like this {ctx.channel.mention} next time.")
        return

    channel = client.get_channel(c_id)

    time = convert(answers[1])
    if time == -1:
        await ctx.send(f"You didn't answer the time with a proper unit. Use (s|m|h|d) next time!")
        return
    elif time == -2:
        await ctx.send(f"The time must be an integer. Please enter an integer next time")
        return            

    prize = answers[2]

    await ctx.send(f"The Giveaway will be in {channel.mention} and will last {answers[1]}!")


    embed = discord.Embed(title = "Giveaway!", description = f"{prize}", color = ctx.author.color)

    embed.add_field(name = "Hosted by:", value = ctx.author.mention)

    embed.set_footer(text = f"Ends {answers[1]} from now!")

    my_msg = await channel.send(embed = embed)


    await my_msg.add_reaction(":tada:")


    await asyncio.sleep(time)


    new_msg = await channel.fetch_message(my_msg.id)


    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(client.user))

    winner = random.choice(users)

    await channel.send(f"Congratulations! {winner.mention} won {prize}!")

@client.command(pass_context=True)
async def make_me_dev(ctx):
  role = discord.utils.get(ctx.guild.roles, id=748751421876207705)
  await ctx.author.add_roles(role)

keep_alive()
client.run(os.getenv("DISCORD_TOKEN"))
