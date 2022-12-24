from uw.character import parse_character, load_active_character, load_active_status, init_status, save_status
import json

def status_commands(bot, discord):
    status_group = discord.SlashCommandGroup("status", "Manage your character's status")

    def format_status(status, character):
        msg = f"HP: {status['hp']}/{character['hp']}"
        if status["thp"] > 0:
            msg += f"({status['thp']})\n"
        else:
            msg += "\n"
        msg += f"Stamina Dice: {status['stamina dice']}/{character['stamina dice']}"
        return msg

    @status_group.command()
    async def display(ctx):
        character = load_active_character(bot.db, ctx.user.id)
        if character is None:
            return await ctx.respond(f"No Active character selected.")
        status = load_active_status(bot.db, ctx.user.id, character)
        msg = f"{character['name']}'s status:\n" + format_status(status, character)
        return await ctx.respond(msg)
    
    @status_group.command()
    async def clear(ctx):
        character = load_active_character(bot.db, ctx.user.id)
        if character is None:
            return await ctx.respond(f"No Active character selected.")
        status = init_status(character)
        save_status(bot.db, ctx.user.id, status)
        return await ctx.respond(f"{character['name']}'s status cleared.\n" + format_status(status, character))

    @status_group.command()
    async def hp(ctx, change: int):
        character = load_active_character(bot.db, ctx.user.id)
        if character is None:
            return await ctx.respond(f"No Active character selected.")
        status = load_active_status(bot.db, ctx.user.id, character)
        if change < 0:
            status['thp'] += change
            if status['thp'] < 0:
                status['hp'] += status['thp']
                status['thp'] = 0
        else:
            status['hp'] += change

        save_status(bot.db, ctx.user.id, status)
        msg = f"{character['name']}'s HP "
        msg += 'drops' if change < 0 else 'increases'
        msg += f' by {change}\n'
        msg += format_status(status, character)
        return await ctx.respond(msg)

    @status_group.command()
    async def thp(ctx, change: int):
        character = load_active_character(bot.db, ctx.user.id)
        if character is None:
            return await ctx.respond(f"No Active character selected.")
        status = load_active_status(bot.db, ctx.user.id, character)
        status['thp'] += change

        save_status(bot.db, ctx.user.id, status)
        msg = f"{character['name']}'s Temporary hit points "
        msg += 'drop' if change < 0 else 'increase'
        msg += f' by {change}\n'
        msg += format_status(status, character)
        return await ctx.respond(msg)

    @status_group.command()
    async def stamina(ctx, change: int):
        character = load_active_character(bot.db, ctx.user.id)
        if character is None:
            return await ctx.respond(f"No Active character selected.")
        status = load_active_status(bot.db, ctx.user.id, character)
        status['stamina dice'] += change

        save_status(bot.db, ctx.user.id, status)
        msg = f"{character['name']}'s stamina dice "
        msg += 'drop' if change < 0 else 'increase'
        msg += f' by {change}\n'
        msg += format_status(status, character)
        return await ctx.respond(msg)

    bot.add_application_command(status_group)