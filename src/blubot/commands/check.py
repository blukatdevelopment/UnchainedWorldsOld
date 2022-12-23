from uw.character import parse_character, load_active_character, get_check_modifier, is_valid_check_type
from uw.dice import roll_normal, roll_advantage, roll_disadvantage
import json

def check_commands(bot, discord):
    check_group = discord.SlashCommandGroup("check", "Ability and skill checks")

    @check_group.command()
    async def normal(ctx, check_type):
        if not is_valid_check_type(check_type):
            return await ctx.respond(f"{check_type} is not a valid check type.")

        character = load_active_character(bot.db, ctx.user.id)
        if character is None:
            return await ctx.respond(f"No Active character selected.")
        mod = get_check_modifier(check_type, character)
        
        if mod > 0:
            mod_text = "+" + str(mod)
        else:
            mod_text = "" + str(mod)
        
        result = roll_normal(0)
        total = result + mod
        

        await ctx.respond(f'{character["name"]} makes a {check_type} check:  ({result}){mod_text} = {total}')

    @check_group.command()
    async def advantage(ctx, check_type):
        if not is_valid_check_type(check_type):
            return await ctx.respond(f"{check_type} is not a valid check type.")

        character = load_active_character(bot.db, ctx.user.id)
        if character is None:
            return await ctx.respond(f"No Active character selected.")
        mod = get_check_modifier(check_type, character)
        
        if mod > 0:
            mod_text = "+" + str(mod)
        else:
            mod_text = "" + str(mod)
        
        result = roll_advantage(0)
        msg = f'{character["name"]} makes a {check_type} check with advantage:\n'
        roll1 = result["roll1"]["sum"] if not result["roll1"]["dropped"] else "~~" + str(result["roll1"]["sum"]) + "~~"
        roll2 = result["roll2"]["sum"] if not result["roll2"]["dropped"] else "~~" + str(result["roll2"]["sum"]) + "~~"
        total = result["sum"] + mod
        
        msg += f'({roll1},{roll2}){mod_text} = {total}'

        await ctx.respond(msg)

    @check_group.command()
    async def disadvantage(ctx, check_type):
        if not is_valid_check_type(check_type):
            return await ctx.respond(f"{check_type} is not a valid check type.")

        character = load_active_character(bot.db, ctx.user.id)
        if character is None:
            return await ctx.respond(f"No Active character selected.")
        mod = get_check_modifier(check_type, character)
        
        if mod > 0:
            mod_text = "+" + str(mod)
        else:
            mod_text = "" + str(mod)
        
        result = roll_disadvantage(0)
        msg = f'{character["name"]} makes a {check_type} check with disadvantage:\n'
        roll1 = result["roll1"]["sum"] if not result["roll1"]["dropped"] else "~~" + str(result["roll1"]["sum"]) + "~~"
        roll2 = result["roll2"]["sum"] if not result["roll2"]["dropped"] else "~~" + str(result["roll2"]["sum"]) + "~~"
        total = result["sum"] + mod
        
        msg += f'({roll1},{roll2}){mod_text} = {total}'

        await ctx.respond(msg)
    bot.add_application_command(check_group)

