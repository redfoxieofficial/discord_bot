import random
from datetime import datetime
import discord
from discord.ext import commands
from discord.utils import get
from discord_components import *

intents = discord.Intents.default()
client = commands.Bot(command_prefix='.', intents = intents)


@client.event
async def on_ready():
    print('Bot is ready')
    DiscordComponents(client)

@client.event
async def on_member_join(member):
    channel = client.get_channel(923965706935107614)
    embed = discord.Embed(title="Hoşgeldin!", description=f"{member.mention}"+str(datetime.date(datetime.now()))+"Tarihinde seni aramızda gördüğümüze çok sevindik. Üye olmak için kayıt odalarına gidebilirsin")
    await channel.send(embed=embed)
    role = discord.utils.get(member.server.roles, name="Kayıtsız")
    await client.add_roles(member, role)
    newnick = "𝒟𝐻𝒮"+str(member)
    await member.edit(nick=newnick)


@client.event
async def on_message_delete(message):
    embed = discord.Embed(title="{} Mesajı Sildi".format(message.author.name),
                          description="", color=0xFF0000)
    embed.add_field(name=message.content, value="This is the message that he has deleted",
                    inline=True)
    channel = client.get_channel(923639063964168279)
    await channel.send(channel, embed=embed)



@client.command()
async def test(ctx):
    await ctx.send(f'Bot çalışıyor | {round(client.latency * 1000)}ms')


@client.command()
@commands.has_permissions(administrator=True)
async def temizle(ctx, amount=5):
    await ctx.channel.purge(limit=amount + 1)


@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = [
        'Kesinlikle',
        'Kesinlikle öyle',
        'Kuşkusuz',
        'Elbette',
        'Belirtiler olduğu yönünde',
        'Gördüğüm kadarıyla, evet',
        'Dışarıdan iyi görünüyor',
        'Pek iyi görünmüyor',
        'Çok şüpheli',
        'Şimdi söylemesem daha iyi',
        'Kaynaklarım hayır diyor',
        'Bana güvenebilirsin',
        'Biraz belirsiz, tekrar dene',
        'Yanıtım hayır',
        'Yok artık daha neler',
        'Doğrudur',
        'Hissedemiyorum',
        'Hissettim',
        'İmkansız',
        'Olmaz gibi',
        'Bilemedim ki şimdi',
        'Yok daha neler'
    ]
    await ctx.send(f'Soru: {question}\nCevap: {random.choice(responses)}')


@client.command()
@commands.has_role("𝒟𝐻𝒮 | Ban Hammer")
async def at(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)


@client.command()
@commands.has_role("𝒟𝐻𝒮 | Ban Hammer")
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)


@client.command()
async def yardim(ctx):
    await ctx.send("```.ban \n.ban_kaldir \n.at \n._8ball \n.temizle \n.test ```")


@client.command()
@commands.has_role("Kayıt Sorumlusu")
async def kayit(ctx, member: discord.Member, *, cinsiyet):
    role = get(member.guild.roles, name="• Mysterious DHS User")
    await member.add_roles(role)
    if cinsiyet.lower() == "erkek":
        erkek = get(member.guild.roles, name="♂")
        await member.add_roles(erkek)
    elif cinsiyet.lower() == "erkek":
        erkek = get(member.guild.roles, name="♀")
        await member.add_roles(erkek)
    await ctx.send("*** Başarıyla kayıt edildi = *** " + "***" + str(member) + "***")


@client.event
async def on_message(message):
   if 'https://' in message.content:
      await message.delete()
      await message.channel.send(f"{message.author.mention} Sunucumuzda reklam yasaktır!")
   elif  'http://' in message.content:
       await message.delete()
       await message.channel.send(f"{message.author.mention} Sunucumuzda reklam yasaktır!")
   else:
      await client.process_commands(message)


client.run('TOKEN HERE!')
