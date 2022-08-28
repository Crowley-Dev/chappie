#!/usr/bin/env python3

import discord
from discord import ui
from discord.ext import menus


class MyMenuPages(ui.View, menus.MenuPages):
  def __init__(self, source):
    super().__init__()
    self._source = source
    self.current_page = 0
    self.ctx = None
    self.message = None


  async def _get_kwargs_from_page(self, page):
    value = await super()._get_kwargs_from_page(page)
    if 'view' not in value:
      value.update({'view': self})
    return value


  async def send_initial_message(self, ctx, channel):
    page = await self._source.get_page(0)
    kwargs = await self._get_kwargs_from_page(page)
    return await ctx.reply(**kwargs)


  async def start(self, ctx, *, channel=None, wait=True):
    await self._source._prepare_once()
    self.ctx = ctx
    self.message = await self.send_initial_message(ctx, ctx.channel)


  async def interaction_check(self, interaction):
    return interaction.user.id == self.ctx.author.id


  @ui.button(label="Anterior ◀️", style=discord.ButtonStyle.grey)
  async def before_page(self, button, interaction):
    await self.show_checked_page(self.current_page - 1)


  @ui.button(label="▶️ Próximo", style=discord.ButtonStyle.grey)
  async def next_page(self, button, interaction):
    await self.show_checked_page(self.current_page + 1)


  @ui.button(emoji="🗑", style=discord.ButtonStyle.red)
  async def delete(self, button, interaction):
    self.stop()
    await self.message.delete()
    await self.ctx.message.delete()
