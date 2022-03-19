import os
from MemoBot import MemoBot, MemoData, ParseDatetime
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
mb = MemoBot()

from discord.ext import tasks, commands


class MyCog(commands.Cog):
    def __init__(self):
        self.printer.start()

    def cog_unload(self):
        self.printer.cancel()

    @tasks.loop(seconds=5.0)
    async def printer(self):
        print("Check")
        for d in mb.check():
            await d.Channel.send(f"{d.Author.mention} {d.Content}")
            # TODO: Pop Data Needed


@bot.event
async def on_ready():
    bot.add_cog(MyCog())
    print(f"{bot.user} | Ready")


@bot.command(aliases=["備忘錄"])
async def memo(ctx, *args):
    if len(args) < 2:
        await ctx.channel.send("Usage: !memo <Time[mmddHHMM]> <Content>")
        return

    ts = ParseDatetime(args[0])
    if ts is None:
        await ctx.channel.send("Invalid Time Format: mmddHHMM Required")
        return
    content = " ".join(args[1:])

    m = MemoData(ctx.channel, ctx.author, ts, content)
    mb.add(m)

    await ctx.channel.send("Done")


if __name__ == "__main__":
    token = os.getenv("TOKEN")
    bot.run(token)
