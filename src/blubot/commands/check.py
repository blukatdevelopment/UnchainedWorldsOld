from uw.character import parse_character, load_active_character, get_ability_modifier, parse_ability
from uw.dice import roll_normal, roll_advantage, roll_disadvantage
import json

def check_command(bot, discord):
    @bot.command(description="Makes a check. Rolls twice for auto advantage/disadvantage.")
    async def check(ctx, check_type):

        ability = parse_ability(check_type)
        if ability == '':
            return await ctx.respond(f"{check_type} is not a valid ability")

        character = load_active_character(bot.db, ctx.user.id)
        if character is None:
            return await ctx.respond(f"No Active character selected.")
        mod = get_ability_modifier(ability, character)
        
        if mod > 0:
            mod_text = "+" + str(mod)
        else:
            mod_text = "" + str(mod)
        
        result = roll_advantage(0)
        msg = f'{character["name"]} makes a {ability} check:\n'
        roll1 = result["roll1"]["sum"] 
        roll2 = result["roll2"]["sum"] 
        total1 = result["roll1"]["sum"] + mod
        total2 = result["roll2"]["sum"] + mod
        msg += f'({roll1},{roll2}){mod_text} -> ({total1}, {total2})'

        await ctx.respond(msg)