import discord
import time
import json
import requests
import asyncio
from discord.ext import commands
import typing


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await ctx.guild.kick(user=member, reason=reason)
        embed = discord.Embed(description=f"<a:BAcheck:758094859491082373> {member} Was kicked")
        await ctx.send(embed=embed)
        await member.send(f"Banned from {ctx.guild.name}")


        channel = self.bot.get_channel(758093741801078954)
        embed = discord.Embed(title=f"{ctx.author.name} kicked: {member.name}", description=reason, color=0xff0000)
        await channel.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await ctx.guild.ban(user=member, reason=reason)
        embed = discord.Embed(description=f"<a:BAcheck:758094859491082373> {member} Was banned")
        await ctx.send(f"Banned {member.mention}")

        channel = self.bot.get_channel(758093741801078954)
        embed = discord.Embed(title=f"{ctx.author.name} banned: {member.name}", description=reason, color=0xff0000)
        await channel.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(ban_members=True)
    async def unban(self, ctx, member, *, reason=None):
        member = await self.bot.fetch_user(int(member))
        await ctx.guild.unban(member, reason=reason)
        embed = discord.Embed(description=f"<a:BAcheck:758094859491082373> {member} Was unbanned")
        await ctx.send(
        f"Unbanned {member.name}"
        )        

        channel = self.bot.get_channel(758093741801078954)
        embed = discord.Embed(title=f"{ctx.author.name} unbanned: {member.name}", description=reason, color=0xff0000)
        await channel.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(manage_messages=True)
    async def purge(self, ctx, amount=1):
        await ctx.channel.purge(limit=amount+1)
        embed = discord.Embed(description=f"<a:BAcheck:758094859491082373> purged {amount}from channel")
		

        channel = self.bot.get_channel(758093741801078954)
        embed = discord.Embed(title=f"{ctx.author.name} purged: {ctx.channel.name}", description=f"{amount} messages were cleared by:\n{ctx.author.name}", color=0xff0000)
        await channel.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def embedsay(self, ctx, *, msg):
        time.sleep(1)
        embedsay = discord.Embed(description="{}" .format(msg),color=0xff0000)

        embedsay.set_footer(text="British Airways.\nTo fly to serve")
        embedsay.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        attachments = ctx.message.attachments
        embedsay.set_image(url=attachments[0].url)
        await ctx.send(embed=embedsay)
        await ctx.message.delete()

    @commands.command()
    @commands.has_guild_permissions(manage_messages=True)
    async def embed(self, ctx, *, msg):
      await asyncio.sleep(1)
      em = discord.Embed(description="{}" .format(msg), color=0xff0000)
      if ctx.message.attachments is not None:
        attachments = ctx.message.attachments
        em.set_image(url=attachments[0].url)
      elif ctx.message.attachments is None:
        em = discord.Embed(description="{}" .format(msg), color=0xff0000)
      else:
        el_em = discord.Embed(description="{}".format(msg))
        await ctx.send(embed=el_em)

      
      await ctx.send(embed=em)
      await ctx.message.delete()

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def say(self, ctx, *, msg):
        time.sleep(1)
        await ctx.message.delete()
        await ctx.send("{}" .format(msg))

    @commands.command(aliases=['slow', 'slowmode'])
    @commands.guild_only()
    @commands.has_guild_permissions(manage_channels=True)
    async def Slowmode(self, ctx, channel: typing.Optional[discord.TextChannel]=None, seconds: int = 0):
      if channel is None:
        await ctx.channel.edit(slowmode_delay=seconds)
        await ctx.send(f"Set the slowmode delay in this channel to {seconds} seconds!")
      else:
        await channel.edit(slowmode_delay=seconds)
        await ctx.send(f"Set the slowmode in {channel.mention} to {seconds}")

def setup(bot):
    bot.add_cog(Moderation(bot))
    return