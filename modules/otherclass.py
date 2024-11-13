class Otherclass:

    def __init__(self, client):
        self.client = client
        self.someclass = self.client.modules['someclass']

        # Do something with someclass object

        self.client.on('001', self.welcome)
    
    async def welcome(self, event):
        print("connected")