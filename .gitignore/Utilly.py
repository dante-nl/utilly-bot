import discord.ext
from discord.ext import commands
from discord.utils import get
from discord.ext import commands
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
import asyncio
import time

prefixes = list(["<@716530326662545450> ", ">"])
bot = commands.Bot(command_prefix=["<@716530326662545450 >", "<@!716530326662545450> ", ">"], case_insensitive=True)
bot.remove_command('help')

@bot.event
async def on_ready():
    print("Turned on.")

@bot.command()
async def help(ctx):
    embed1 = discord.Embed(title="Help", description="Here are all the commands that I use. Please note for some commands you need special permissions", color=0x54C3A6)
    embed1.add_field(name="**Help (Page 1)**", value=f"""For these commands you don't need any permissions

    `>help` - Shows this message
    `>guild-id` - **AKA:** `>guildid` - Gives the guild id from this server
    `>server-info` - **AKA:** `>serverinfo` - Gives information about {ctx.message.guild}
    `>myinfo` - Gives info about yourself
    `>info @user` - Gives info about @user, replace @user with the person you want to get info about
    `>invite` - Gives an invite URL to invite Utilly
    `>invitestudio` - **AKA:** `>is` - Generates invite URL's for you, for more information, click [here](https://discord.gg/8kRTgkm)
    `>ping` - Gives my latency in ms
    `>leave` - Leave {ctx.message.guild}
    `>channelinfo` - **AKA:** `>channel-info`, `>ci` - Gives information about the current channel
    """)
    await ctx.send(content=None, embed=embed1)

    embed2 = discord.Embed(title="Moderation help", description="A list of commands that require a permission", color=0x54C3A6)
    embed2.add_field(name="**Help (Page 2)**", value=f"""For these commands, you need permissions

    `>kick @user <reason (optional)>` - Kicks @user for <reason>.
    *Requires the KICK_MEMBERS permission*
    `>ban @user <reason (optional)>` - Bans @user for <reason>.
    *Requires the BAN_MEMBERS permission*
    `>purge <amount>` - **AKA:** `>clear` - Deletes <amount> messages. The default is 5
    *Requres the MANGAE_MESSAGES permission*
    `>nuke` - Deletes all messages in a channel that are send. (Because of the Discord API, messages older then 2 weeks will not be deleted)
    *Requires the MANGAE_MESSAGES permission*
    `>slowmode <seconds>` - Set the slowmode to <seconds> seconds, 0 to turn it off
    *Requires the manage_channels permission*
    """)
    await ctx.send(content=None, embed=embed2)

    embed4 = discord.Embed(title="Bot help", descritpion="Need help with Utilly? These links may be something for you!", color=0x54C3A6)
    embed4.add_field(name="**Help (Page 3)**", value=f"""You need internet to open these links

    Official support server: [Join](https://discord.gg/FVczWXP)
    Direct invite: [Open](https://discord.com/oauth2/authorize?client_id=716530326662545450&scope=bot&permissions=470117503)
    Site: [Open](https://utilly.netlify.com)
    How to use invitestudio: [Open](https://discord.gg/8kRTgkm)""")
    await ctx.send(content=None, embed=embed4)

@bot.command(aliases= ["guild-id"])
async def guildid(ctx):
    await ctx.send(f"The guild id from {ctx.message.guild} is {ctx.message.guild.id}")

@bot.command(aliases= ["server-info"])
async def serverinfo(ctx):
    link = await ctx.channel.create_invite(unique=False)
    embed = discord.Embed(title="Server info", description=f"**Server name:** {ctx.message.guild} \n**Guild ID:** {ctx.message.guild.id} \n**Members:** {ctx.guild.member_count} \n**Invite URL:** {link}", color=0x54C3A6)
    embed.set_image(url=ctx.guild.icon_url)
    embed.set_footer(text=f"Requested by {ctx.message.author}")
    await ctx.send(content=None, embed=embed)

@bot.command()
async def myinfo(ctx):
    if str(ctx.message.author.status) is "online":
        status = "<:Online:716538516263272479> Online"
    elif str(ctx.message.author.status) is "idle":
        status = "<:Idle:716538477189136465> Idle"
    elif str(ctx.message.author.status) is "dnd":
        status = "<:DnD:716538437271945306> Do not disturb"
    elif str(ctx.message.author.status) is "offline":
        status = "<:offline:717391587595911210> Offline"

    embed = discord.Embed(title=f"Info about {ctx.message.author}", description=f"""
    **Ping:** {ctx.message.author.mention}
    **Name and tag:** {ctx.message.author}
    **ID:** {ctx.message.id}
    **Status:** {status}""", color=0x54C3A6)
    embed.set_image(url=ctx.message.author.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.message.author}")
    await ctx.send(content=None, embed=embed)

@bot.command()
async def info(ctx, member: discord.Member):
    if str(member.status) is "online":
            status = "<:Online:716538516263272479> Online"
    elif str(member.status) is "idle":
            status = "<:Idle:716538477189136465> Idle"
    elif str(member.status) is "dnd":
            status = "<:DnD:716538437271945306> Do not disturb"
    elif str(member.status) is "offline":
            status = "<:offline:717391587595911210> Offline"

    embed = discord.Embed(title=f"Info about {member}", description=f"""
    **Ping:** {member.mention}
    **Name and tag:** {member}
    **ID:** {member.id}
    **Status:** {status}
    **Bot:** {member.bot}""", color=0x54C3A6)
    embed.set_image(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.message.author}")
    await ctx.send(content=None, embed=embed)

@bot.command()
async def ping(ctx):
    embed = discord.Embed(title="Pong!", description=f"My latency is {round(bot.latency * 1000)}ms", color=0x54C3A6)
    embed.set_footer(text=f"Requested by {ctx.message.author}")
    await ctx.send(content=None, embed=embed)

@bot.command()
@has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason="Not provided"):
    embed = discord.Embed(title="Success!", description=f"Succesfully kicked {member}!", color=0x4ED626)
    embed.set_footer(text=f"Requested by {ctx.message.author}")
    await ctx.send(content=None, embed=embed)
    embed = discord.Embed(title="Kick", description=f"""You just got kicked from {ctx.message.guild}.
    Moderator: {ctx.message.author.mention}
    Reason: {reason}""", color=0x54C3A6)
    user = bot.get_user(member.id)
    await user.send(content=None, embed=embed)
    await member.kick(reason=reason)

@bot.command()
@has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason="The ban hammer has spoken"):
    embed = discord.Embed(title="Done", description=f"Banned <@{member.id}>! If this was a mistake, use `>unban {member.id}`", color=0x4ED626)
    embed.set_footer(text=f"Requested by {ctx.message.author}")
    await ctx.send(content=None, embed=embed)
    user = bot.get_user(member.id)
    embed = discord.Embed(title="Ban", description=f"""
    You just got banned from {ctx.message.guild}.
    Moderator: {ctx.message.author.mention}
    Reason: {reason}
    Get a DM when you are unbanned: [Join](https://discord.gg/g5pw763)""", color=0x54C3A6)
    embed.set_footer(text="Only you can see this | Messages here will be ignored, except commands")
    user = bot.get_user(member.id)
    await user.send(content=None, embed=embed)
    await member.ban(reason=reason)


@bot.command()
@has_permissions(ban_members=True)
async def unban(ctx, id: int):
    user1 = await bot.fetch_user(id)
    embed = discord.Embed(title="Verification", description=f"Are you sure that you want to unban <@{id}>? Please react to this message within 30 seconds to verify", color=0x54C3A6)
    embed.set_footer(text=f"Requested by {ctx.message.author}")
    message = await ctx.send(content=None, embed=embed)
    for emoji in ('✅'):
        await message.add_reaction(emoji)

        try:

            # the wait_for will only register if the following conditions are met
            def check(rctn, user):
                return user.id == ctx.author.id and str(rctn) == '✅'

            # timeout kwarg is optional
            rctn, user = await bot.wait_for("reaction_add", check=check, timeout=30)

            # then execute your code here if the author reacts, like so:
            await ctx.guild.unban(user1)
            embed = discord.Embed(title="Verified", description=f"Unbanned <@{id}>! Trying to send DM with the good news...", color=0x4ED626)
            embed.set_footer(text=f"Can't promise anything...")
            user = bot.get_user(id)
            link = await ctx.channel.create_invite(unique=False)
            embed = discord.Embed(title=f"Unbanned on {ctx.message.guild}", description=f"You just got unbanned on {ctx.message.guild} by {ctx.message.author.mention}! You can re-join by clicking [here]({link})!", color=0x4ED626)
            embed.set_footer(text=f"Only you can see this | Messages here will be ignored, except commands")
            await user.send(content=None, embed=embed)
            embed = discord.Embed(title=f"Done", description=f"Send <@{id}> a dm!", color=0x4ED626)
            embed.set_footer(text=f"Requested by {ctx.message.author}")
            await ctx.send(content=None, embed=embed)

        # throws this error if user doesn't react in time
        # you won't need this if you don't provide a timeout kwarg in wait_for()
        except asyncio.TimeoutError:
            embed = discord.Embed(title="Error", description=f"{ctx.message.author.mention}, you did not react in time, <@{id}> will not be unbanned!", color=0xEB3F3F)
            embed.set_footer(text="Error")
            await ctx.send(content=None, embed=embed)

@bot.command(aliases= ["clear"])
@has_permissions(manage_messages=True)
async def purge(ctx, amount=5):
    if amount <= 4:
        embed = discord.Embed(title="Error", description=f"You entered a number ({amount}) that is too low. The minimum is 5", color=0xEB3F3F)
        embed.set_footer(text=f"Error")
        await ctx.send(content=None, embed=embed)
    else:
        await ctx.channel.purge(limit=amount)

@bot.command()
@has_permissions(manage_messages=True)
async def nuke(ctx):
    await ctx.message.delete()
    count = 0
    async for _ in ctx.channel.history(limit=None):
        count += 1
    await ctx.channel.purge(limit=count)
    embed = discord.Embed(title="Nuked this channel", description="Messages older then 2 weeks are not deleted beacuse of the Discord API", color=0x4ED626)
    embed.set_image(url="https://media.giphy.com/media/urp8cVywl1Sk8/giphy.gif")
    await ctx.send(content=None, embed=embed)

@bot.command()
@has_permissions(manage_channels=True)
async def slowmode(ctx, amount):
    await ctx.channel.edit(reason=f'By {ctx.message.author}', slowmode_delay=int(amount))
    if int(amount) != 0:
        embed = discord.Embed(title="Slowmode on", description=f"Slowmode is turned on by {ctx.message.author.mention}, you can now type one message every {amount} second(s)", color=0x54C3A6)
        await ctx.send(content=None, embed=embed)
    elif int(amount) == 0:
        embed - discord.Embed(title="Slowmode off", description=f"Slowmode is turned off by {ctx.message.author.mention}", color=0x54C3A6)
        await ctx.send(content=None, embed=embed)

@bot.command()
async def invite(ctx):
    embed = discord.Embed(title="Invite Utilly", description="""
    You can invite me via [this link](https://discord.com/oauth2/authorize?client_id=716530326662545450&scope=bot&permissions=470117503)""", color=0x54C3A6)
    embed.set_footer(text=f"Requested by {ctx.message.author}")
    await ctx.send(content=None, embed=embed)

@bot.command(aliases=["is"])
async def invitestudio(ctx, MaxUses=0, ExpireAfter=0):
    link1 = await ctx.channel.create_invite(max_age=ExpireAfter, unique=False, max_uses=MaxUses)
    embed = discord.Embed(title="InviteStudio", description=f"""Your invite has been generated!
    **Max uses:** {MaxUses}
    **Expires after:** {ExpireAfter} seconds
    **Link:** {link1}

    `0` means ∞
    **PRO TIP:** Try playing with the invite studio, try `>is 1 10` for example!""", color=0x54C3A6)
    embed.set_footer(text=f"Requested by {ctx.message.author}")
    await ctx.send(content=None, embed=embed)


@bot.command()
async def leave(ctx):
    user1 = await bot.fetch_user(ctx.message.author.id)
    embed = discord.Embed(title="Verification", description=f"Are you sure that you want to leave {ctx.message.guild}?", color=0xEB3F3F)
    embed.set_footer(text=f"Requested by {ctx.message.author}")
    message = await ctx.send(content=f"{ctx.message.author.mention}", embed=embed)
    for emoji in ('✅'):
        await message.add_reaction(emoji)

        try:

            # the wait_for will only register if the following conditions are met
            def check(rctn, user):
                return user.id == ctx.author.id and str(rctn) == '✅'

            # timeout kwarg is optional
            rctn, user = await bot.wait_for("reaction_add", check=check, timeout=30)

            # then execute your code here if the author reacts, like so:
            member = ctx.message.author
            await member.kick()
            user = bot.get_user(ctx.message.author.id)
            link = await ctx.channel.create_invite(unique=True, max_uses=1)
            embed = discord.Embed(title="Success", description=f"You succesfully left {ctx.message.guild}. But you can re-join by clicking [here]({link})!", color=0x4ED626)
            embed.set_footer(text=f"Only you can see this | Messages here will be ignored, except commands")
            await user.send(content=None, embed=embed)

            # throws this error if user doesn't react in time
            # you won't need this if you don't provide a timeout kwarg in wait_for()
        except asyncio.TimeoutError:
            embed = discord.Embed(title="Error", description="You did not react in time!", color=0xEB3F3F)
            embed.set_footer(text=f"Requested by {ctx.message.author}")
            await ctx.send(content=None, embed=embed)


@bot.command(aliases= ["channel-info", "ci"])
async def channelinfo(ctx):
    count = 0
    async for _ in ctx.channel.history(limit=None):
        count += 1
    embed = discord.Embed(title=f"Info about #{bot.get_channel(ctx.channel.id)}", description=f"**ID:** {ctx.channel.id} \n**Mention:** <#{ctx.channel.id}> \n**Mention (raw):** `<#{ctx.channel.id}>` \n**Messages sent:** {count} \n**Slowmode:** {ctx.channel.slowmode_delay} second(s)", color=0x54C3A6)
    embed.set_footer(text=f"Requested by {ctx.message.author}")
    await ctx.send(content=None, embed=embed)

@bot.event
async def on_command_error(ctx, error):
    embed = discord.Embed(title="Error", description=f"Something went wrong! \n\n{error}", color=0xEB3F3F)
    await ctx.send(content=f"{ctx.message.author.mention}", embed=embed)

bot.run("NzE2NTMwMzI2NjYyNTQ1NDUw.XupR8A.fgfyAFKE0W1Kh9iVN_N0isS-H1I")
