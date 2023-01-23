import json

def world_commands(bot, discord):
    world_group = discord.SlashCommandGroup("World", "Access hex and calendar info.")

    @world_group.command()
    async def set_status(ctx):
        msg = "Not implemented yet. :3 Meow."
        return await ctx.respond(msg)

    @world_group.command()
    async def status(ctx):
        msg = "Not implemented yet. :3 Meow."
        return await ctx.respond(msg)

    @world_group.command()
    async def today(ctx):
        msg = "Not implemented yet. :3 Meow."
        return await ctx.respond(msg)

    @world_group.command()
    async def here(ctx):
        msg = "Not implemented yet. :3 Meow."
        return await ctx.respond(msg)

    @world_group.command()
    async def encounter(ctx):
        msg = "Not implemented yet. :3 Meow."
        return await ctx.respond(msg)
    
    bot.add_application_command(world_group)