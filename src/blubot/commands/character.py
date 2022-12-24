from uw.character import parse_character, load_active_character
import json

'''
Character management commands.
'''

def character_commands(bot, discord):
    character_group = discord.SlashCommandGroup("character", "Character management")

    @character_group.command()
    async def update(ctx, data: str):
        char = parse_character(data)
        if "error" in char:
            return await ctx.respond(f"Error: {char['error']}")
        name = char["name"]
        data = json.dumps(char)

        characters = bot.db.get_all_characters(ctx.user.id)
        if name not in characters:
            bot.db.insert_character(ctx.user.id, name, data)
        else:
            bot.db.update_character(ctx.user.id, name, data)

        bot.db.set_active_character(ctx.user.id, char['name'])        

        await ctx.respond(f"Character {char['name']} parsed, updated, and set as active. Meow. :3")

    @character_group.command()
    async def list(ctx):
        characters = bot.db.get_all_characters(ctx.user.id)
        #characters = []
        if len(characters) == 0:
            await ctx.respond("You don't have any characters")
        await ctx.respond("Your characters: " + ', '.join(characters))

    @character_group.command()
    async def set(ctx, name):
        char = bot.db.get_character(ctx.user.id, name)
        if char is None:
            return await ctx.respond(f"Character '{name}' does not exist.")
        bot.db.set_active_character(ctx.user.id, name)
        await ctx.respond(f'Active character set to {name}.')

    @character_group.command()
    async def active(ctx):
        char = load_active_character(bot.db, ctx.user.id)
        if char is None:
            return await ctx.respond("No active character")
        name = char["name"]
        await ctx.respond(f'Active character: {name}')

    @character_group.command()
    async def get(ctx, name):
        char = bot.db.get_character(ctx.user.id, name)
        if char is None:
            return await ctx.respond(f"Character '{name}' does not exist.")
        await ctx.respond('Character fetched: ```json\n' + json.dumps(char) + '```')

    @character_group.command()
    async def delete(ctx, name: str):
        characters = bot.db.get_all_characters(ctx.user.id)
        if name not in characters:
            await ctx.respond(f"No such character exists: {name}")
        bot.db.delete_character(ctx.user.id, name)
        await ctx.respond(f"Deleted character: {name}")

    bot.add_application_command(character_group)