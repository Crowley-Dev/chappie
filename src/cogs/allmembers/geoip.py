#!/usr/bin/env python3

import discord
from discord.ext import commands

from ..ui import *
from ..functions import *


class GeoLoc(commands.Cog, ):
  def __init__(self, bot: commands.Bot) -> None:
    self.bot = bot

  @commands.command(name="geoip")
  async def geoip(self, ctx: commands.Context, ip=None) -> None:
    query = GeoIP()
    query = await query.request_api(
      url="http://ip-api.com/json/{}?lang=pt-BR&fields=66846719",
      ip=ip
    )

    msg = discord.Embed(
       title = "Mensagem de erro.",
       color = discord.Color.from_rgb(220, 20, 60),
       description=query.get("msg")
    )

    if ip is None:
      return await ctx.reply(embed=msg, view=Github())

    if query.get("code") == 503:
      return await ctx.reply(embed=msg, view=Github())

    data = query.get("content")
    formatter = MySource(
      data,
      per_page=1,
      title="Geo Localizador | Consulta realizada.",
      bot=self.bot

    ); menu = MyMenuPages(formatter)
    await menu.start(ctx)


async def setup(bot):
  await bot.add_cog(GeoLoc(bot))
