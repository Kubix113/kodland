import discord
from discord.ext import commands

# Ustawienia intencji i prefiksu bota
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')


@bot.command()
async def recykling(ctx):
    await ctx.send("🟦**Pojemnik Niebieski**🟦\n \n- Gazety, czasopisma, kartony, zeszyty, ulotki\n- Opakowania papierowe, torebki papierowe'\n \n🟩**Pojemnik Zielony**🟩\n \n- Butelki szklane, słoiki (bez pokrywek)\n- Opakowania szklane\n \n🟨**Pojemnik żółty**🟨\n- Plastikowe butelki po napojach (PET)\n- Kartony po mleku i sokach (Tetra Pak)\n- Puszki metalowe, folia aluminiowa\n- Opakowania plastikowe\n \n🟫**Pojemnik Brązowy**🟫\n- Resztki jedzenia\n- Owoce, warzywa, fusy po kawie i herbacie\n- Skórki owoców, obierki warzywne\n \n⬛**Pojemnik czarny**⬛\n- Odpady, które nie pasują do żadnej z kategorii powyżej\n- Zabrudzone opakowania (np. tłuste kartony po pizzy)\n- Jednorazowe ręczniki papierowe ")                                              

@bot.command()
async def rospiska(ctx):
    await ctx.send("Pojemnik Niebieski = **Papier**\n \nPojemnik Zielony = **Szkło**\n \nPojemnik Brązowy = **Bio**\n \nPojemnik czarny = **Zmieszane**\n")


@bot.command()
async def komendy(ctx):
    await ctx.send("**recykling**\n**rospiska**")



# Uruchomienie bota
bot.run('')
