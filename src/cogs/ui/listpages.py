#!/usr/bin/env python3

import discord
from discord.ext import menus


class MySource(menus.ListPageSource):
  def __init__(self, entries, *, per_page, title, bot):
    super().__init__(entries, per_page=per_page)
    self.title = title
    self.bot = bot


  async def disabled_button(self, button, this_page, max_pages):
    if this_page == 1:
      button.children[0].disabled = True

    elif this_page == max_pages:
      button.children[1].disabled = True

    else:
      button.children[0].disabled = False
      button.children[1].disabled = False


  async def format_entries(self, entries: dict, embed: discord.Embed):
    for key, value in entries.items():
      embed.add_field(
        name=key,
        value=value or "Não encontrado.",
        inline=False
      )
    return embed


  async def format_page(self, menu, entries):
    this_page = self.entries.index(entries) + 1
    max_pages = self.get_max_pages()
    ping = round(self.bot.latency * 100)

    await self.disabled_button(menu, this_page, max_pages)

    embed = discord.Embed(
      title = self.title,
      color = discord.Colour.random()

    ); embed.set_footer(text = "página %s/%s | ping %s"
      %(this_page, max_pages, ping))

    await self.format_entries(entries=entries, embed=embed)
    return embed
