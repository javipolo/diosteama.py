#!/usr/bin/env python

import time
import telepot
from telepot.loop import MessageLoop
import ConfigParser
import os.path
from plugins import load_plugins

config_filenames = [ 'diosteama.ini', os.path.expanduser('~/.diosteama.ini'), '/etc/diosteama.ini' ]

def usage(plugins):
    plugins_msg = list()
    for key, data in plugins.items():
        plugins_msg.append( '/%s : %s' % ( key, data['help_text'] ))
    usage = '''
    Commands: 
{}

    From inside a group you have to add @{} to the command. For example:
        /help@{}
    '''.format('\n'.join(plugins_msg),config['telegram']['botname'],config['telegram']['botname'])
    return usage

def handler(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id, msg['text'])

    plugins = load_plugins()

    if content_type == 'text':
        command = msg['text']
        command = command.split(' ')[0]
        command = command.split('@')[0]
        command = command.split('/', 1)[1]
        if command in plugins:
            text = plugins[command]['command']()
        else:
            text = 'Sorry, I don\'t understand what you mean by "{}"'.format(msg['text'])
            text += usage(plugins)
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
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    pass
