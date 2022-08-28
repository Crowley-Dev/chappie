#!/usr/bin/env python3

import discord


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
        label="Código do bot",
        url="https://github.com/Crowley-Dev/botdc-geoip",
      )
    )
