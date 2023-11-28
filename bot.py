import discord
from discord.ext import commands
from bot_mantik import *
import math
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')
    await ctx.send(f"Hoşgeldin {ctx.author}!") 
@bot.command()
async def heh(ctx, count_heh=5):
    await ctx.send("he" * count_heh)

@bot.command()
async def topla(ctx,*args):
    try:
        sonuc=sum(int(arg) for arg in args)
        #for arg in args:
        #    sonuc+=int(arg) 
        await ctx.send(sonuc)
    except:
        await ctx.send("Lütfen doğru bir değer girin.")
@bot.command()
async def cikarma(ctx,s1=0,s2=0):
    await ctx.send(s1-s2)
@bot.command()
async def carpma(ctx,s1=1,s2=1):
    await ctx.send(s1*s2)
@bot.command()
async def bolme(ctx,s1=1,s2=1):
    await ctx.send(s1/s2)
@bot.command()
async def faktoriyel(ctx,s1=0):
    await ctx.send(math.factorial(s1))
@bot.command()
async def kuvvet(ctx,s1=0,s2=0):
    await ctx.send(s1**s2)
@bot.command()
async def joined(ctx):
    await ctx.send(f"Hoşgeldin {ctx.author}!")
@bot.command()
async def sifre(ctx,uzunluk=10):
    await ctx.send(p_g(uzunluk))
@bot.command()
async def zamanlayici(ctx,sure=10):
    await ctx.send(z(sure))
@bot.command()
async def r_s_y(ctx,b=0,s=100):
    await ctx.send(r_s_u(b,s))
@bot.command()
async def karekok(ctx,s1=1):
    await ctx.send(math.sqrt(s1))
@bot.command()
async def EBOB(ctx,s1=1,s2=1):
    await ctx.send(math.gcd(s1,s2))
@bot.command()
async def EKOK(ctx,s1=1,s2=1):
    await ctx.send(math.lcm(s1,s2))
@bot.command()
async def y_h(ctx,s1=1,s2=1):
    await ctx.send(h_y(s1,s2))
@bot.command()
async def c_h(ctx,c=1):
    await ctx.send(math.pi*c)
@bot.command()
async def yazi_tura(ctx,c):
    if c=="Yazı" or c=="Tura":
        x=y_t()
        if x==c:
            await ctx.send(f"Doğru bildin {x} çıktı.")
        else:
            await ctx.send(f"Bilemedin {x} çıktı.")
    else:
         await ctx.send("Lütfen Yazı veya Tura girin.")   
@bot.command()
async def z_a(ctx):
    zar=[1,2,3,4]
    olasilik=[0.20,0.25,0.50,0.05]
    await ctx.send(random.choices(zar,weights=olasilik,k=1)[0])

baskentler={
    "Türkiye":"Ankara",
    "Fransa":"Paris",
    "Birleşik_Krallık":"Londra"
}
@bot.command()
async def baskent_b(ctx,cevap):
    embed=discord.Embed(title="Başkent",color=discord.Color.red())
    embed.add_field(name="a",value=f"{cevap} başkenti {baskentler[cevap]}")
    await ctx.send(embed=embed)

@bot.command()
async def sayi_b(ctx):
    e=random.randint(1,100)
    await ctx.send("1 ile 100 arasında bir sayı seçtim ve bilmek için 8 hakkınız var.")
    s=0
    while True:
        tahmin_mesaji = await bot.wait_for("message", check=lambda m: m.author == ctx.author)
        y=tahmin_mesaji.content
        try:
            y=int(y)
        except:
            await ctx.send("Lütfen sayı girin.")
            continue
        s+=1
        if e==y:
            await ctx.send("Kazandın!")
            break
        elif s==8:
            await ctx.send("Bilemediniz hakkınız doldu.")
            break
        elif e>y:
            await ctx.send("Daha büyük bir sayı tahmin et.")
        else:
            await ctx.send("Daha küçük bir sayı tahmin et.")
    
bot.run("Lütfen tokenininizi buraya girin. ")
