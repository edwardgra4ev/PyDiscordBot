import os
import time
import datetime
from dotenv import load_dotenv
import discord
from discord.ext import commands
from discord.ext import tasks

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

OFFSET = datetime.timedelta(hours=3)
MEETING_TIME = datetime.time(hour=10, minute=29, second=00, tzinfo=datetime.timezone(offset=OFFSET, name="МСК"))
SHUTDOWN_TIME = datetime.time(hour=19, minute=00, second=00, tzinfo=datetime.timezone(offset=OFFSET, name="МСК"))

@tasks.loop(time=MEETING_TIME)
async def notification_the_meeting():
    if await not_day_off():
        channel = bot.get_channel(1263053691808780360)
        message = discord.Embed(title="Собрание отдела", description=f"@everyone\nНапоминаю собрание отдела состоится в 10:30.\n[Присоедениться к собранию]({os.getenv('CHANNEL_URL')})", color=0x00ff00)
        await channel.send(embed=message)

@tasks.loop(time=SHUTDOWN_TIME)
async def notification_the_shutdown():
    if await not_day_off():
        channel = bot.get_channel(1263053691808780360)
        message = discord.Embed(title="Окончание рабочего дня", description=f"@everyone\nВсем спасибо и хорошего вечера", color=0x00ff00)
        await channel.send(embed=message)

@bot.command(name="ping")
async def ping(ctx):
    print(await not_day_off())

async def not_day_off() -> bool:
    weekday = datetime.date.today().weekday()
    if weekday in [5, 6]:
        return False
    return True

@bot.event
async def on_ready():
    if not notification_the_meeting.is_running():
        notification_the_meeting.start()
    if not notification_the_shutdown.is_running():
        notification_the_shutdown.start()


if __name__ == "__main__":
    load_dotenv()
    bot.run(os.getenv('TOKEN'))