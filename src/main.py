#!/usr/bin/env python3

import discord, os
from discord.ext import commands


TOKEN="SEU TOKEN AQUI"
PREFIX=["c!", "d!"]
GUILD_ID=0


class Bot(commands.Bot):
  def __init__(self) -> None:
    super().__init__(
      command_prefix=PREFIX,
      help_command=None,
      intents=discord.Intents.all()
    )


  async def load(self, bot, path: list):
    for dir in path:
      dirI = dir.replace(".", "/")
      if not os.path.exists(dirI):
        raise FileNotFoundError(
          "Nenhum diretório nomeado '%s' foi encontrado."
          %(dir)
        )

      for file in os.listdir(dirI):
        if file.endswith(".py"):
          await bot.load_extension(
            "%s.%s"
            %(dir, file[:-3])
          )


  async def setup_hook(self) -> None:
    await self.load(
      self, [ # pretendo mudar isso na proxima att
        # "cogs.admin",
        "cogs.allmembers",
      ]
    )
    self.tree.copy_global_to(guild=discord.Object(id=GUILD_ID))
    await self.tree.sync()

  async def on_ready(self):
    await self.change_presence(
      status=discord.Status.dnd,
      activity=discord.Game(
        name=f"prefix -> {self.command_prefix} | Geo Localizador.",
        type=3
      )
    )


bot = Bot()
bot.run(TOKEN)
