import discord
from discord.ext import commands
import asyncio
import time
from replit import db

class Modmail(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def report(self, ctx, *, report):
        channel = self.client.get_channel(758468939595382785)
        em = discord.Embed(color=0xff0000)
        em.add_field(
            name=f"New report from {ctx.author.name}",
            value="{}".format(report))
        await channel.send(embed=em)
        await ctx.send(
            "Thanks for the report!\nA member of staff will review it and respond "
        )

    @commands.command()
    async def suggest(self, ctx, *, report):
        channel = self.client.get_channel(763807753079619666)
        author = ctx.author
        em = discord.Embed(color=0xff0000)
        em.add_field(
            name=f"New suggestion:", value="{}".format(report), inline=False)
        em.set_footer(
            text=
            f"Suggested by: {ctx.author.name}, ID: {author.id}. Use b!answer {author.id}"
        )
        em.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        await channel.send(embed=em)
        await ctx.send(
            "<a:BAcheck:758094859491082373> Succeeded, thank you for trying to help BA improve."
        )
        await asyncio.sleep(5)
        await ctx.channel.purge(limit=2)

    @commands.command()
    async def answer(self, ctx, user: discord.User, *, answer):
        #guild = discord.guild(707183075624353952)
        print(user)
        channel = await user.create_dm()
        answer = discord.Embed(
            title="Hello there!",
            description="{}".format(answer),
            color=0xff0000)
        answer.add_field(
            name="======", value=f"Kind Regards, \n -{ctx.author.name}")
        answer.set_author(
            name="BA Staff Team",
            icon_url=
            "http://logok.org/wp-content/uploads/2014/04/British-Airways-logo-ribbon-logo.png"
        )
        answer.set_image(
            url=
            "https://logos-download.com/wp-content/uploads/2016/03/British_Airways_logo.png"
        )
        answer.set_footer(text="To fly, to serve!")
        await channel.send(embed=answer)
        await ctx.send("<a:BAcheck:758094859491082373> Answer sent!")

    @commands.command  #()
    async def setappID(self, ctx, count):
        if ctx.author.id == 689802280102527124:
            db["appID"] = (count)
            appID = (db["appID"])
            await ctx.send(
                f"<a:BAcheck:758094859491082373> next_appID has been set to {appID}"
            )

        else:   
            ctx.send("Nope, you can't set this!")

    @commands.command(aliases=['apply-pilot'])
    async def apply_pilot(self, ctx):
        await ctx.message.add_reaction(str('✅'))
        author = ctx.author
        auID = ctx.author.id
        #list of questions
        p_list = [
            'How many minutes flown do you have?',
            'What airplane do you usually fly?',
            'What route do you usually take?',
            'Why do you want to become a pilot?',
            'How many crashes did you have on ATC 24?',
            'Do you agree with our rules and regulations?',
        ]

        b_list = []

        submit_channel = self.client.get_channel(
            765263048923414539)  #<-- change to your channel id
        channel = await ctx.author.create_dm()
        qn = 1

        def check(m):
            return m.content is not None and m.channel == channel and not m.author.bot

        for question in p_list:
            appembed = discord.Embed(
                title=f"Question {qn}",
                description=f"{question}",
                colour=0xff0000)
            time.sleep(0.5)
            await channel.send(embed=appembed)
            msg = await self.client.wait_for('message', check=check)
            b_list.append(msg.content)
            qn = qn + 1

        submit_wait = True
        while submit_wait:
            await channel.send(
                'End of questions - "submit" to finish or type anything else to cancel'
            )
            a1 = b_list[0]
            a2 = b_list[1]
            a3 = b_list[2]
            a4 = b_list[3]
            a5 = b_list[4]
            a6 = b_list[5]
            msg = await self.client.wait_for('message', check=check)
            if "submit" in msg.content.lower():
                submit_wait = False
                appID = (db["appID"])
                db["appID"] = (db["appID"]) + 1
                submit_embed = discord.Embed(
                    title=f"Pilot application by {author}",
                    description=
                    f"-------\nAnswers:\n\n -Minutes Flown:\n-->{a1}\n-Usual Airplane:\n-->{a2}\n-Usual Route:\n-->{a3}\n-Why does he want to become a pilot:\n-->{a4}\n-Crashes on ATC24:\n-->{a5}\n-Agree with rules and regulations?:\n-->{a6}",
                    colour=0xff0000)
                submit_embed.set_footer(
                    text=f"Applicant ID: {auID}, Application ID: #{appID}")
                await submit_channel.send(embed=submit_embed)
                await channel.send(
                    f"<a:BAcheck:758094859491082373> Application submitted! Your Application ID: #{(appID)}"
                )
            else:
                await channel.send("application canceled")
                submit_wait = False

    @commands.command(aliases=['apply-partner'])
    async def apply_partner(self, ctx):
        await ctx.message.add_reaction(str('✅'))
        author = ctx.author
        auID = ctx.author.id
        #list of questions
        q_list = [
            "What's the name of your company?",
            'What kind of operations does your company do?',
            'Tell us a bit more about your company. History, successes, ...',
            'Why do you want to partner with British Airways?',
            'What do you expect from our partnership?',
            'Now we get to the requirements! Are you ready?',
            'Does your group have more than 80 members?',
            'Is your group older than 2 weeks?',
            'Does your group have a raid-safe permission system?',
            'Done with the requirements! Do you have any additional notices?',
            'Last but not least: Please give us a permanent group link, not an advertisement. (Just the link)',
        ]

        a_list = []

        submit_channel = self.client.get_channel(
            765949560681922600)  #<-- change to your channel id
        channel = await ctx.author.create_dm()
        qn = 1

        def check(m):
            return m.content is not None and m.channel == channel and not m.author.bot

        for question in q_list:
            appembed = discord.Embed(
                title=f"Question {qn}",
                description=f"{question}",
                colour=0xff0000)
            time.sleep(0.5)
            await channel.send(embed=appembed)
            msg = await self.client.wait_for('message', check=check)
            a_list.append(msg.content)
            qn = qn + 1

        submit_wait = True
        while submit_wait:
            await channel.send(
                'End of questions - "submit" to finish or type anything else to cancel'
            )
            a1 = a_list[0]
            a2 = a_list[1]
            a3 = a_list[2]
            a4 = a_list[3]
            a5 = a_list[4]
            a6 = a_list[5]
            a7 = a_list[6]
            a8 = a_list[7]
            a9 = a_list[8]
            a10= a_list[9]
            a11= a_list[10]
            msg = await self.client.wait_for('message', check=check)
            if "submit" in msg.content.lower():
                submit_wait = False
                appID = (db["PAppID"])
                db["PAppID"] = (db["PAppID"]) + 1
                submit_embed = discord.Embed(
                    title=f"Partner application by {author}",
                    description=
                    f"-------\nAnswers:\n\n -Company name:\n--> {a1}\n-Kind of operations:\n--> {a2}\n-More info:\n--> {a3}\n-Why does the company want to partner?:\n--> {a4}\n-What are the expectations of our partnership:\n--> {a5}\n\n-More than 80 members?:\n--> {a7}\n-Older than 2 weeks?:\n--> {a8}\n-Raid-safe permissions?:\n--> {a9}\n\n-additional notices?:\n--> {a10}\n-------\nLink to group: {a11} ",
                    colour=0xff0000)
                submit_embed.set_footer(
                    text=f"Applicant ID: {auID}, Application ID: #{appID}")
                await submit_channel.send(embed=submit_embed)
                await channel.send(
                    f"<a:BAcheck:758094859491082373> Application submitted! Your Application ID: #{(appID)}"
                )
            else:
                await channel.send("application canceled")
                submit_wait = False


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def accept(self, ctx, user: int, role, *, notice):
        dg = self.client.get_guild(id=707183075624353952)
        dm = dg.get_member(user)
        channel = await dm.create_dm()
        if role.lower() == "pilot":
            accEmb = discord.Embed(
                title=
                f"<a:BAcheck:758094859491082373> Your Pilot application in British Airways has been accepted!",
                description="{}".format(notice),
                colour=0xff0000)
            accEmb.set_author(
                name="BA Staff Team",
                icon_url=
                "http://logok.org/wp-content/uploads/2014/04/British-Airways-logo-ribbon-logo.png"
            )
            accEmb.set_image(
                url=
                "https://logos-download.com/wp-content/uploads/2016/03/British_Airways_logo.png"
            )
            accEmb.set_footer(text="To fly, to serve!")
            role = discord.utils.get(dg.roles, id=739442933215789056)
            await dm.add_roles(role)
            await channel.send(embed=accEmb)
            await ctx.send(
                f"<a:BAcheck:758094859491082373> Application of {dm.name}#{dm.discriminator} was accepted! I've given them the F/O role, please continue with the further roles manually in BA!"
            )
        elif role.lower() == "partner":
          accEmb = discord.Embed(
              title=
              f"<a:BAcheck:758094859491082373> Your Partner application in British Airways has been accepted!",
              description="{}".format(notice),
              colour=0xff0000)
          accEmb.set_author(
              name="BA Staff Team",
              icon_url=
              "http://logok.org/wp-content/uploads/2014/04/British-Airways-logo-ribbon-logo.png"
          )
          accEmb.set_image(
              url=
              "https://logos-download.com/wp-content/uploads/2016/03/British_Airways_logo.png"
          )
          accEmb.set_footer(text="To fly, to serve!")
          role = discord.utils.get(dg.roles, id=708988303747317770)
          await dm.add_roles(role)
          await channel.send(embed=accEmb)
          await ctx.send(
              f"<a:BAcheck:758094859491082373> Partner application of {dm.name}#{dm.discriminator} was accepted!"
          )
        else:
          await ctx.send("Please state a valid role! b!accept [Applicant ID] [role: pilot/partner] [notice]")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def reject(self, ctx, user: discord.User, *, notice):
        channel = await user.create_dm()
        rejEmb = discord.Embed(
            title="Your application in British Airways has been rejected",
            description="{}".format(notice),
            color=0xff0000)
        rejEmb.add_field(
            name="======", value=f"Kind Regards, \n -The BA Staff Team")
        rejEmb.set_author(
            name="BA Staff Team",
            icon_url=
            "http://logok.org/wp-content/uploads/2014/04/British-Airways-logo-ribbon-logo.png"
        )
        rejEmb.set_image(
            url=
            "https://logos-download.com/wp-content/uploads/2016/03/British_Airways_logo.png"
        )
        rejEmb.set_footer(text="To fly, to serve!")
        await channel.send(embed=rejEmb)
        await ctx.send("<a:BAcheck:758094859491082373> Application rejected!")

    @commands.command()
    async def feedback(self, ctx, *, feedback):
        await ctx.send("<a:BAcheck:758094859491082373> Sent!")

        channel = self.client.get_channel(769368494533771264)
        em = discord.Embed(title=f"From {ctx.author.name}", description="{}" .format(feedback), color=0xff0000)
        em.set_footer(icon_url=ctx.author.avatar_url, text=f"Author ID: {ctx.author.id}")
        await channel.send(embed=em)
        


    #@commands.command
    #async def apply(self, ctx):
    #  p_list = [o
    #    'How many minutes flown do you have?',
    #    'What airplane do you usually fly?',
    #    'What route do you usually take?',
    #    'Why do you want to become a pilot?',
    #    'How many crashes did you have on ATC 24?',
    #    'Do you agree with our rules and regulations?',
    #  ]


#    b_list = []
#   submit_channel = self.client.get_channel(765263048923414539)
#  channel = await ctx.author.create_dm()
# qn = 1


def setup(client):
    client.add_cog(Modmail(client))
    return
