from uw.character import parse_character, load_active_character, parse_ability, get_save_modifier
from uw.dice import roll_advantage
import json

def save_command(bot, discord):
    @bot.command(description="Makes a saving throw. Rolls twice for auto advantage/disadvantage.")
    async def save(ctx, ability):
        ability = parse_ability(ability)
        if ability == '':
            return await ctx.respond(f"{ability} is not an ability. Try again. :3")

        character = load_active_character(bot.db, ctx.user.id)
        if character is None:
            return await ctx.respond(f"No Active character selected. Mow.")

        mod = get_save_modifier(ability, character)
        
        if mod > 0:
            mod_text = "+" + str(mod)
        else:
            mod_text = "" + str(mod)
        
        result = roll_advantage(0)
        msg = f'{character["name"]} makes a(n) {ability} save:\n'
        roll1 = result["roll1"]["sum"] 
        roll2 = result["roll2"]["sum"] 
        total1 = result["roll1"]["sum"] + mod
        total2 = result["roll2"]["sum"] + mod
        msg += f'({roll1},{roll2}){mod_text} -> ({total1}, {total2})'

        await ctx.respond(msg)