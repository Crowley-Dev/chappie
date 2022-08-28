#!/usr/bin/env python3

import discord
from discord import app_commands
from discord.ext import commands


class Ping(commands.Cog):
  def __init__(self, bot: commands.Bot) -> None:
    self.bot = bot

  @app_commands.command(
    name="ping",
    description="Mostrará a latência do bot."
  )

  async def ping(self, ctx: discord.Interaction) -> None:
    await ctx.response.send_message(
      embed = discord.Embed(
        title = "PING",
        description = "%sms"
          %(round(self.bot.latency * 100)),
        color = discord.Color.from_rgb(0, 0, 0)
      )
    )


async def setup(bot):
  await bot.add_cog(Ping(bot))
