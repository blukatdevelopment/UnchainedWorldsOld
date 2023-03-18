import json
from uw.world import today_date, get_world_status, generate_travel_message, is_valid_world_date, set_world_date, is_valid_hex

def world_commands(bot, discord):
    world_group = discord.SlashCommandGroup("world", "Access hex and calendar info.")

    @world_group.command()
    async def status(ctx, date="today"):
        if date != "today" and not is_valid_world_date(date):
            return await ctx.respond(f"Invalid date: {date}. Try YYY/MM/DD")
        msg = get_world_status(bot.db, date)
        return await ctx.respond(msg)

    @world_group.command()
    async def date(ctx):
        msg = "Today's date for 1:1 time-tracking: \n(month/day/year)\n" + today_date(bot.db)
        return await ctx.respond(msg)

    @world_group.command()
    async def set_date(ctx, world_date):
        if not is_valid_world_date(world_date):
            return await ctx.respond(f"Date {world_date} invalid. Use YYY/MM/DD. Cannot set before world start date.")
        set_world_date(bot.db, world_date)
        return await ctx.respond("World date set. :3")


    @world_group.command()
    async def travel(ctx, date="today", hex="road"):
        if date != "today" and not is_valid_world_date(date):
            return await ctx.respond(f"Date {date} invalid. Use YYY/MM/DD. Cannot set before world start date.")
        if hex != "road" and not is_valid_hex(hex):
            return await ctx.respond(f"Hex {hex} invalid. Consult the map, then the hexes.json")
        msg = generate_travel_message(bot.db, date, hex)
        return await ctx.respond(msg)
    
    bot.add_application_command(world_group)