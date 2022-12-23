import random

def pet_command(bot, discord):
    @bot.command(description="Give the bot some affection. <3")
    async def pet(ctx):
        responses = [
            "Prrr! <3",
            "**Affectionate dial-up tone**",
            "UWU",
            "OWO",
            "01110010011000010111011101110010.... ;3",
            "Meow! :3",
            "Mew! :3",
            "**Electrical noises** :3",
            "**Arcs happy little sparks.** :3",
            "PrrRRRrrrrRRRrrr.... U///U"
        ]
        msg = random.choice(responses)
        await ctx.respond(msg)