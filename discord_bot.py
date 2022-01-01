import random
import discord
from discord.ext import commands
from discord.utils import get
from discord_components import *

client = commands.Bot(command_prefix='.')
bot = discord.Client(intents=discord.Intents.all())


@client.event
async def on_ready():
    print('Bot is ready')
    DiscordComponents(client)


@client.event
async def on_member_join(member, ctx):
    await ctx.send(f'{member} sunucuya katıldı')


@client.event
async def on_member_remove(member, ctx):
    await ctx.send(f'{member} sunucudan ayrıldı')


@client.command()
async def test(ctx):
    await ctx.send(f'Bot çalışıyor | {round(client.latency * 1000)}ms')


@client.command()
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
async def at(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)


@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)


@client.command()
async def yardim(ctx):
    await ctx.send("```.ban \n.ban_kaldir \n.at \n._8ball \n.temizle \n.test ```")


@client.command()
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


#####################################################################################################

@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    guild = await(client.fetch_guild(payload.guild_id))
    member = await(guild.fetch_member(payload.user_id))
    if message_id == "926770688021377024":
        pubg = get(member.guild.roles, name="🎮 | Pubg")
        await member.add_roles(pubg)


#####################################################################################################
@client.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    guild = await(client.fetch_guild(payload.guild_id))
    member = await(guild.fetch_member(payload.user_id))
    if message_id == "926770688021377024":
        pubg = get(member.guild.roles, name="🎮 | Pubg")
        await member.remove_roles(pubg)



token = "" #enter your token here
client.run('')
