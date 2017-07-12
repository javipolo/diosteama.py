#!/usr/bin/env python

import time
import telepot
from telepot.loop import MessageLoop
import pypd
import json
import ConfigParser
import os.path
import pprint

config_filenames = [ 'diosteama.ini', os.path.expanduser('~/.diosteama.ini'), '/etc/diosteama.ini' ]
quote = '''
<DrSlump> si yo fuera tia me pasaria l dia metiendome cosas por el co+o  <- y dejaria de tener el culo como un bebedero de patos

        quote 17547 by CoSMiC on 03 Aug 2005 10:02:07
'''

def usage():
    usage = '''
    Commands:
        /help       This help
        /quote      Get a random quote

    From inside a group you have to add @{} to the command. For example:
        /help@{}
    '''.format(config['telegram']['botname'],config['telegram']['botname'])
    return usage

def handler(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id, msg['text'])

    if content_type == 'text':
        command = msg['text']
        command = command.split(' ')[0]
        command = command.split('@')[0]
        if   command == '/quote':
            text = 'Not implemented yet'
        elif command == '/help':
            text = usage()
        elif command == '/start':
            text = usage()
        else:
            text = 'Sorry, I don\'t understand what you mean by "{}"'.format(msg['text'])
            text += usage()
        bot.sendMessage(chat_id,text)

def parse_config():
    sections = [ 'telegram' ]
    Config = ConfigParser.ConfigParser()
    Config.read(config_filenames)
    config = {}
    for section in sections:
        config[section] = {}
        options = Config.options(section)
        for option in options:
            config[section][option] = Config.get(section, option)
    return config


config = parse_config()

print('Starting {}'.format(config['telegram']['botname']))

bot = telepot.Bot(config['telegram']['token'])
MessageLoop(bot, handler).run_as_thread()

try:
    bot.sendMessage(config['telegram']['chat_id'],quote)
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    pass
