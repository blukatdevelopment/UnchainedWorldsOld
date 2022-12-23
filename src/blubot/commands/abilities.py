def abilities_commands(bot, discord):
    abilities = discord.SlashCommandGroup("abilities", "Ability management")

    @abilities.command()
    async def set(ctx, character: str, str: int, dex: int, con: int, int: int, wis: int, cha: int):
      await ctx.respond(f"{character}'s new stats are [{str}, {dex}, {con}, {int}, {wis}, {cha}]")

    @abilities.command()
    async def get(ctx, character: str):
      await ctx.respond(f"Not implemented yet for {character}.¯\\_(ツ)_/¯")

    bot.add_application_command(abilities)