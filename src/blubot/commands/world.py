import json
from uw.world import today_date, generate_encounter

def world_commands(bot, discord):
    world_group = discord.SlashCommandGroup("world", "Access hex and calendar info.")

    @world_group.command()
    async def status(ctx, date="today"):
        msg = "Not implemented yet. :3 Meow."
        return await ctx.respond(msg)

    @world_group.command()
    async def date(ctx):
        msg = "Today's date for 1:1 time-tracking: \n(month/day/year)\n" + today_date()
        return await ctx.respond(msg)

    @world_group.command()
    async def encounter(ctx, date="today", location="road"):
        msg = generate_encounter(date, location)
        return await ctx.respond(msg)
    
    bot.add_application_command(world_group)