from pyrc.client import Client as irc

client = irc({
    'nickname': 'MyFunnyBot',
    'username': 'Bot',
    'gecos': 'type !help',
    'hostname': 'irc.host.tld',
    'port': 6667,
    'ssl': True,
    'debug': False,
})

client.run()
