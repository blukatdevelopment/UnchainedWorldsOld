from uw.character import load_active_character, list_attacks, use_attack

def attack_commands(bot, discord):
    attack_command_group = discord.SlashCommandGroup("attack", "Make or list attacks")

    @attack_command_group.command()
    async def use(ctx, attack_name):
        character = load_active_character(bot.db, ctx.user.id)
        if character is None:
            return await ctx.respond(f"No Active character selected.")
        await ctx.respond(f"{character['name']} uses their {attack_name} attack!\n" + use_attack(character, attack_name))

    @attack_command_group.command()
    async def list(ctx):
        character = load_active_character(bot.db, ctx.user.id)
        if character is None:
            return await ctx.respond(f"No Active character selected.")
        await ctx.respond(list_attacks(character))

    bot.add_application_command(attack_command_group)