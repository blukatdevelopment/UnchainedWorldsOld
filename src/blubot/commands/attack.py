from uw.character import load_active_character, list_attacks, use_attack, update_hp, roll_attack
import json

def attack_commands(bot, discord):
    class MyView(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View
        def __init__(self, damage_1, damage_2):
            super().__init__()
            self.damage_1 = damage_1 * -1
            self.damage_2 = damage_2 * -1

        @discord.ui.button(label="Apply Damage 1", style=discord.ButtonStyle.primary, emoji="⚔️") # Create a button with the label "😎 Click me!" with color Blurple
        async def damage_1(self, button, interaction):
            result = update_hp(interaction, bot, self.damage_1)
            await interaction.response.send_message(result)

        @discord.ui.button(label="Apply Damage 2", style=discord.ButtonStyle.primary, emoji="⚔️") # Create a button with the label "😎 Click me!" with color Blurple
        async def damage_2(self, button, interaction):
            result = update_hp(interaction, bot, self.damage_2)
            await interaction.response.send_message(result)

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
        return await ctx.respond(list_attacks(character))

    @attack_command_group.command()
    async def keeper(ctx, to_hit, damage):
        (msg, attack1, attack2, damage1, damage2) = roll_attack("", int(to_hit), damage, "")
        return await ctx.respond(msg, view = MyView(damage1, damage2))


    bot.add_application_command(attack_command_group)