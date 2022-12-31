from uw.militia import militia_prompt
from uw.thieves import thieves_prompt
from uw.scouts import scouts_prompt
from uw.rebels import rebel_prompt
from uw.silent import silent_prompt
import json


def prompt_commands(bot, discord):
    prompt_group = discord.SlashCommandGroup("prompts", "Prompts for keepers")

    @prompt_group.command()
    async def militia(ctx):
        await ctx.respond(militia_prompt())

    @prompt_group.command()
    async def thieves(ctx):
        await ctx.respond(thieves_prompt())

    @prompt_group.command()
    async def scouts(ctx):
        await ctx.respond(scouts_prompt())

    @prompt_group.command()
    async def rebels(ctx):
        await ctx.respond(rebel_prompt())

    @prompt_group.command()
    async def silent(ctx):
        await ctx.respond(silent_prompt())

    bot.add_application_command(prompt_group)