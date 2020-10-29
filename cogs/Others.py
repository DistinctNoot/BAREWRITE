import discord
from discord.ext import commands
import time
from discord.utils import get
from replit import db

class Other(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(pass_context=True)
  async def ping(self, ctx):
    """ Get bot latency """
    before = time.monotonic()
    message = await ctx.send("Pong!")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"Pong!  ``{int(ping)}ms``")
    print(f'Ping {int(ping)}ms')

  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def announce(self, ctx, channel: discord.TextChannel, *, text):
    await ctx.message.delete()
    author = ctx.author
    #await message.channel.send(author.avatar_url)
    emb = discord.Embed(description=text, colour=(0xff0000) )
    emb.set_author(name=ctx.author.name, icon_url=author.avatar_url)
    await channel.send(embed=emb)

  @commands.command()
  async def ticket(self, ctx):
    author=ctx.author.name
    guild = ctx.message.guild
    cname='tickets'
    cov =  {
    guild.default_role: discord.PermissionOverwrite(read_messages=False),
    guild.me: discord.PermissionOverwrite(read_messages=True),
    ctx.author: discord.PermissionOverwrite(read_messages=True)
    }
    ctgry=discord.utils.get(ctx.guild.categories, name=cname)
    lowauthor=author.lower()
    await ctx.guild.create_text_channel(author, category=ctgry, overwrites=cov)
    channel = (discord.utils.get(ctx.guild.text_channels, name=lowauthor))
    confirm=(f':white_check_mark: I created you a ticket! {channel.mention}')
    c2=(f'Hey, please ping one of our moderators for help!')
    await channel.send(c2)
    await ctx.send(confirm)

  #Tickets+ expansion
  @commands.command(aliases=["rename"])
  @commands.has_permissions(manage_messages=True)
  async def setreason(self, ctx, channel: discord.TextChannel, *, new_name):
      await channel.edit(name=new_name)

  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def addmember(self, ctx, member: discord.Member):
      channel = ctx.channel
      cov = discord.PermissionOverwrite()
      cov.send_messages=True
      cov.read_messages=True
      await channel.set_permissions(member, overwrite=cov)
      emb = discord.Embed(title=":white_check_mark: Action successful!", description=f"Added {member.mention} to this ticket.")
      await ctx.send(embed=emb)

  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def removemember(self, ctx, member: discord.Member):
      channel = ctx.channel
      cov = discord.PermissionOverwrite()
      cov.send_messages=False
      cov.read_messages=False
      await channel.set_permissions(member, overwrite=cov)
      emb = discord.Embed(title=":white_check_mark: Action successful!", description=f"Removed {member.mention} from this ticket.")
      await ctx.send(embed=emb)

  @commands.command()
  async def team(self, ctx):
	  URL="https://cdn.discordapp.com/attachments/741475513201066035/754960568909037608/GIF-200914_144245.gif"
	  em = discord.Embed(color=0xff0000)
	  em.add_field(name="Meet our team!", value="""
	**CEO**
	AFK_Pilot

	**Senior Executives**
	Kabab.CPP
	FlyWithCaptainJoe
	Vex

	**Executives**
	74slats
	sir123skills

	**HR**
	royalbluesheep
	Mossy is stressed
	Shane
	Gordon Ramsay
	Ben
	A Stressed Potato

	**Moderators**
	BM2065
	Farish on the go
	LOA || faketp
	Mr Qantas
    Markov
  Kenthegreat8
	""")
	  em.set_image(url=URL)
	  await ctx.send(embed=em)

  @commands.command()
  async def about(self, ctx):
	  URL="https://cdn.discordapp.com/attachments/741475513201066035/754960568909037608/GIF-200914_144245.gif"
	  em = discord.Embed(color=0xff0000)
	  em.add_field(name="About section", value="""
	Welcome to British Airways, the Pride of Britain!
	----------------------------------------------------------------
	We're proud to be one of PTFS's biggest airlines and fly all around the map in our diverse and modern aircraft!

 	Our rules? - #│『✈』rules 
 	Our fleet? - #│『✈』airline-fleet 
 	Our destinations? - #│『✈』destinations 
 	Our subsidiaries? - #│『✈』subsidiaries 
 	Our team? - #│『✈』staff-list 

	Thanks for joining!
	To apply for a job or partnership, check #│『❓』how-to-apply!

	Before beginning to chat, please read the #│『✈』rules! 

	We wish you a pleasant stay!
	-The British Airways Staff Team
	--------------------------------------------------------‐-------
 	To fly, to serve!
	""")
	  em.set_image(url=URL)
	  await ctx.send(embed=em)

  @commands.command()
  async def fleet(self, ctx):
	  URL="https://cdn.discordapp.com/attachments/741475513201066035/754960568909037608/GIF-200914_144245.gif"
	  em = discord.Embed(color=0xff0000)
	  em.add_field(name="Fleet section", value="""
	```Aircraft Fleet:
	Boeing B777X-9 -20
	Airbus A350-1000XWB -20
	Boeing B747-400 -30
	Boeing B787-10 -20
	Boeing B787-9 -30
	Airbus A320-200 -40
	Bombardier Q400 -15
	ATR72-212 -10
	Airbus A380-800 -30
	Boeing B757-200 -20
	Boeing B767-300 -15
	Boeing B737-800 -30
	Boeing B747-8F -12
	DHC-6 Twin Otter -15
	Aérospatiale/BAC Concorde  -10

	Fleet Number:317```
	""")
	  em.set_image(url=URL)
	  await ctx.send(embed=em)

  @commands.command()
  async def staff(self, ctx):
    guild = self.client.get_guild(707183075624353952)
    role1 = discord.utils.get(guild.roles, id=712757255858290721)
    rolem = role1.members
    owner = [row.name for row in rolem]
    role2 = discord.utils.get(guild.roles, id=770454942304829491)
    role2m = role2.members
    coo = [row.name for row in role2m]
    role3 = discord.utils.get(guild.roles, id=721303406345453640)
    role3m = role3.members
    svp = [row.name for row in role3m if row.name not in coo]
    vp = discord.utils.get(guild.roles, id=747112646981189714)
    vpm = vp.members
    vps = [row.name for row in vpm]
    hrr = discord.utils.get(guild.roles, id=730022365744070727)
    hrm = hrr.members
    hr =[row.name for row in hrm]
    modr = discord.utils.get(guild.roles, id=707521891073785956)
    modm = modr.members
    helpr = discord.utils.get(guild.roles, id=745136852029407315)
    helpm = helpr.members
    help = [i.name for i in helpm]
    mod = [i.name for i in modm]
    em = discord.Embed(title="Our staff", color=0xff0000)
    em.add_field(name=role1.name, value = ', '.join(owner), inline=False)
    em.add_field(name=role2.name, value=', '.join(coo), inline=False)
    em.add_field(name=role3.name, value=', '.join(svp), inline=False)
    em.add_field(name=vp.name, value=', '.join(vps), inline=False)
    em.add_field(name=hrr.name, value =', '.join(hr), inline=False)
    em.add_field(name=modr.name, value=', '.join(mod), inline=False)
    em.add_field(name=helpr.name, value=', '.join(help), inline=False)
    await ctx.send(embed=em)

  @commands.command(aliases=['afk'])
  async def AFK(self,ctx, *, reason="`AFK`"):
    var = discord.utils.get(ctx.guild.roles, name = "AFK")
    var2 = discord.utils.get(ctx.guild.roles, name = "Flight Notifications")
    try:
      del db[ctx.author.id]
      nick1 = f"[AFK] {ctx.author.display_name}"
      nick2 = nick1.replace('[AFK]','')
      await ctx.send(f"Welcome back {ctx.author.mention}, i removed your AFK")
      try:
        await ctx.author.remove_roles(var)
        await ctx.author.add_roles(var2)
      except:
        print("cant update role")
      finally:
        try:
          await ctx.author.edit(nick=nick2)
        except:
          print("Cant rename")
    except:      
      db[ctx.author.id] = reason
      await ctx.send(f"I set you AFK: {reason}" .format(reason))
      try:
        await ctx.author.remove_roles(var2)
        await ctx.author.add_roles(var)
      except:
        print("cant change role")
      finally:
        try:
          await ctx.author.edit(nick=f"[AFK] {ctx.author.display_name}")
        except:
          print("Cant rename")

# AFK Command should work now right?.
# Think so
# Great.
# So didn't work. What do we do now?
# Database
# MOM GET THE DOCUMENTATION :irlm:
# Lemme pull up the Carberra tutorials Database

def setup(client):
    client.add_cog(Other(client))
    return