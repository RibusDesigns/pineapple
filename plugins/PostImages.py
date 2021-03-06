from util import Events
import glob
import os
import random


class Plugin(object):
    def __init__(self, pm):
        self.pm = pm

    @staticmethod
    def register_events():
        return [Events.Command("pat", desc="Pat someone else"),
                Events.Command("lewd", desc="Use this if things get too lewd"),
                Events.Command("weeb", desc="When someone is being a weeb"),
                Events.Command("doushio", desc="Doushio"),
                Events.Command("rekt", desc="When someone just got rekt"),
                Events.Command("kiss", desc="Share a kiss"),
                Events.Command("boop", desc="boop~"),
                Events.Command("smug", desc="smug face"),
                Events.Command("fistbump", desc="Fist bump someone")]

    async def handle_command(self, message_object, command, args):
        if command == "pat":
            await self.pat(message_object, args[1])
        if command == "kiss":
            await self.kiss(message_object, args[1])
        if command == "lewd":
            await self.lewd(message_object)
        if command == "weeb":
            await self.weeb(message_object)
        if command == "doushio":
            await self.doushio(message_object)
        if command == "rekt":
            await self.rekt(message_object)
        if command == "boop":
            await self.boop(message_object)
        if command == "smug":
            await self.smug(message_object)
        if command == "fistbump":
            await self.fist_bump(message_object, args[1])

    async def pat(self, message_object, user):
        files = glob.glob(os.getcwd() + "/images/pat/" + '*.gif')
        files.extend(glob.glob(os.getcwd() + "/images/pat/" + '*.png'))
        files.extend(glob.glob(os.getcwd() + "/images/pat/" + '*.jpg'))
        file = random.choice(files)
        await self.pm.client.delete_message(message_object)
        await self.pm.client.send_message(message_object.channel,
                                          "**" + user + "** you got a pat from **" + message_object.author.name + "**")
        await self.pm.client.send_file(message_object.channel, file)

    async def kiss(self, message_object, user):
        files = glob.glob(os.getcwd() + "/images/kiss/" + '*.gif')
        files.extend(glob.glob(os.getcwd() + "/images/kiss/" + '*.png'))
        files.extend(glob.glob(os.getcwd() + "/images/kiss/" + '*.jpg'))
        file = random.choice(files)
        await self.pm.client.delete_message(message_object)
        await self.pm.client.send_message(message_object.channel,
                                          "**" + user + "** you got a kiss from **" + message_object.author.name + "**")
        await self.pm.client.send_file(message_object.channel, file)

    async def lewd(self, message_object):
        files = glob.glob(os.getcwd() + "/images/lewd/" + '*.gif')
        files.extend(glob.glob(os.getcwd() + "/images/lewd/" + '*.png'))
        files.extend(glob.glob(os.getcwd() + "/images/lewd/" + '*.jpg'))
        file = random.choice(files)
        #await self.pm.client.delete_message(message_object)
        await self.pm.client.send_file(message_object.channel, file)

    async def weeb(self, message_object):
        files = glob.glob(os.getcwd() + "/images/weeb/" + '*.gif')
        files.extend(glob.glob(os.getcwd() + "/images/weeb/" + '*.png'))
        files.extend(glob.glob(os.getcwd() + "/images/weeb/" + '*.jpg'))
        file = random.choice(files)
        #await self.pm.client.delete_message(message_object)
        await self.pm.client.send_file(message_object.channel, file)

    async def doushio(self, message_object):
        files = glob.glob(os.getcwd() + "/images/doushio/" + '*.gif')
        files.extend(glob.glob(os.getcwd() + "/images/doushio/" + '*.png'))
        files.extend(glob.glob(os.getcwd() + "/images/doushio/" + '*.jpg'))
        file = random.choice(files)
        #await self.pm.client.delete_message(message_object)
        await self.pm.client.send_file(message_object.channel, file)

    async def rekt(self, message_object):
        files = glob.glob(os.getcwd() + "/images/rekt/" + '*.gif')
        files.extend(glob.glob(os.getcwd() + "/images/rekt/" + '*.png'))
        files.extend(glob.glob(os.getcwd() + "/images/rekt/" + '*.jpg'))
        file = random.choice(files)
        #await self.pm.client.delete_message(message_object)
        await self.pm.client.send_file(message_object.channel, file)

    async def boop(self, message_object):
        files = glob.glob(os.getcwd() + "/images/boop/" + '*.gif')
        files.extend(glob.glob(os.getcwd() + "/images/boop/" + '*.png'))
        files.extend(glob.glob(os.getcwd() + "/images/boop/" + '*.jpg'))
        file = random.choice(files)
        #await self.pm.client.delete_message(message_object)
        await self.pm.client.send_file(message_object.channel, file)

    async def smug(self, message_object):
        files = glob.glob(os.getcwd() + "/images/smug/" + '*.gif')
        files.extend(glob.glob(os.getcwd() + "/images/smug/" + '*.png'))
        files.extend(glob.glob(os.getcwd() + "/images/smug/" + '*.jpg'))
        file = random.choice(files)
        #await self.pm.client.delete_message(message_object)
        await self.pm.client.send_file(message_object.channel, file)

    async def fist_bump(self, message_object, user):
        files = glob.glob(os.getcwd() + "/images/fistbump/" + '*.gif')
        files.extend(glob.glob(os.getcwd() + "/images/fistbump/" + '*.png'))
        files.extend(glob.glob(os.getcwd() + "/images/fistbump/" + '*.jpg'))
        file = random.choice(files)
        await self.pm.client.delete_message(message_object)
        await self.pm.client.send_message(message_object.channel,
                                          "**" + user + "** you got a fist bump from **" + message_object.author.name + "**")
        await self.pm.client.send_file(message_object.channel, file)
