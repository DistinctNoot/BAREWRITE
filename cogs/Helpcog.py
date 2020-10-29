import discord
from discord.ext import commands

class Helpcog(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def help(self, ctx):
      em = discord.Embed(color=0xff0000)
      em.add_field(name="Help commands", value="For more info on commands just type help-{categoryname}")
      em.add_field(name="Moderation Commands", value="Commands for staff")

      em.add_field(name="Regular Commands", value="Commands for members")

      em.add_field(name="VIP and CEO Certified Commands", value="Commands for VIP and CEO Certified Cool person members")
      await ctx.send(embed=em)

  @commands.command(aliases=['help-Moderation', 'help-moderation', 'help-mod'])
  async def helpModeration(self, ctx):
      em=discord.Embed(color=0xff0000)
      em.add_field(name="Ban", value="Ban members")
      em.add_field(name="Kick", value="Kick a member")
      em.add_field(name="Unban", value="Unban a member")
      em.add_field(name="Say", value="Send a message with the bot")
      em.add_field(name="Embed", value="Send an embeded message")
      em.add_field(name="Purge", value="Purge messages")
      em.add_field(name="rename", value="rename a channel")
      em.add_field(name="addmember", value="add a member to a ticket")
      em.add_field(name="removemember", value="remove member from a ticket")
      await ctx.send(embed=em)

  @commands.command()
  async def helpRegular(self, ctx):
      em=discord.Embed(color=0xff0000)
      em.add_field(name="Modmail", value="Send a report")
      em.add_field(name="Stats", value="Check stats")
      em.add_field(name="Ping", value="Check your latency")
      em.add_field(name="Ticket", value="Create a ticket")
      em.add_field(name="team", value="Know who our team includes")
      em.add_field(name="about", value="Know more about BA PTFS")
      em.add_field(name="fleet", value="Know our fleet")
      em.add_field(name="Suggest", value="suggest something")
      await ctx.send(embed=em)

  @commands.command()
  async def helpVIP(self, ctx):
      em=discord.Embed(color=0xff0000)

      em.add_field(name="VIP and CC commands", value="meme\npup\kitten")
      await ctx.send(embed=em)

    


def setup(client):
    client.add_cog(Helpcog(client))
    return