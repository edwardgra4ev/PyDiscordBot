import os
import discord
from discord.ext import commands
from discord.ext import tasks
import datetime

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

OFFSET = datetime.timedelta(hours=3)
MEETING_TIME = datetime.time(hour=10, minute=28, second=00, tzinfo=datetime.timezone(offset=OFFSET, name="МСК"))


@tasks.loop(time=MEETING_TIME)
async def notification_the_meeting():
    channel = bot.get_channel(1263053691808780360)
    message = discord.Embed(title="Собрание отдела", description=f"@everyone\nНапоминаю собрание отдела состоится в 10:30.\n[Присоедениться к собранию]({os.environ['CHANNEL_URL']})", color=0x00ff00)
    await channel.send(embed=message)


@bot.command(name="ping")
async def ping(ctx):
    await ctx.send("pong")


@bot.event
async def on_ready():
    if not notification_the_meeting.is_running():
        notification_the_meeting.start()


if __name__ == "__main__":
    bot.run(os.environ['TOKEN'])