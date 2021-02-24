import discord
import json
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        self.channels = get_data("channels")["channels"]

    async def on_message(self, message):
        if not is_valid_channel(message, self.channels):
            return

        if(message.guild == None):
            print('Message from {0.author}: {0.content}'.format(message))
        else:
            user = await self.fetch_user(212619493866864650)
            await user.send('Message from {0.author}: {0.content}'.format(message))
        


def is_valid_channel(message, channels):
    if(message.guild == None):
        return True
    for channel in channels:
        if(message.channel.id == channel):
            return True
    return False


def get_data(name):
    with open('{0}.json'.format(name)) as file:
        data = json.load(file)
        return data


client = MyClient()
client.run(get_data("login")["token"])