
class SomeClass:

    def __init__(self, client):
        self.client = client

        self.client.on('privmsg', self.on_privmsg)

    async def on_privmsg(self, event):
        pass
    
    