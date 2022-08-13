#!/usr/bin/env python3

import discord
from discord.ext import commands
import requests


intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(
  intents=intents,
  command_prefix="!",
  description="Um simples bot geo localizador de IPV4.",
)


class Github(discord.ui.View):
  def __init__(self, ):
    super().__init__()
    self.add_item(
      discord.ui.Button(
        label="Criador",
        url="https://github.com/Crowley-Dev",
      ),

    ); self.add_item(
     discord.ui.Button(
        label="Código do bot",
        url="https://github.com/Crowley-Dev/botdc-geoip",
      )
    )


@bot.event
async def on_ready():
  print(f"Logado em {bot.user} (ID: {bot.user.id})")
  print("------")


@bot.command()
async def geoip(ctx, ip):
  msg=""
  if ip is None:
    msg = discord.Embed(
      title="Comando inválido.",
      color=discord.Color.from_rgb(220, 20, 60)
    );msg.add_field(name="use:", value="!geoip <ip>")
    msg.add_field(name="exemplo:", value="!geoip 24.48.0.1")

    return await ctx.reply(embed=msg, view=Github());

  data = requests.request(
    method = "GET",
    url = f"http://ip-api.com/json/{ip}?fields=8966904",
  ).json()

  msg = discord.Embed(
    title = "Geolocalizador.",
    color = discord.Color.from_rgb(220, 20, 60)
  )

  msg.add_field(name="IP:", value=ip)
  msg.add_field(name="ISP:", value=data.get("isp") or "não encontrado.")
  msg.add_field(name="DNS:", value=data.get("reverse") or "não encontrado.")
  msg.add_field(name="Latitude:", value=data.get("lat") or "não encontrado.")
  msg.add_field(name="Longitude:", value=data.get("lon") or "não encontrado.")
  msg.add_field(name="Estado/Região:", value=data.get("regionName") or "não encontrado.")
  msg.add_field(name="Cidade:", value=data.get("city") or "não encontrado.")
  msg.add_field(name="Código postal:", value=data.get("zip") or "não encontrado.")
  msg.add_field(name="Distrito:", value=data.get("district") or "não encontrado.")
  msg.add_field(name="Moeda:", value=data.get("currency") or "não encontrado.")

  if data.get("status") != "success":
    msg = discord.Embed(
      title = "IP inválido.",
      color = discord.Color.from_rgb(220, 20, 60),
      description="Tem certeza de que é este IP?"
    )

  await ctx.reply(embed=msg, view=Github())


token = "SEU TOKEN AQUI"
bot.run(token)
