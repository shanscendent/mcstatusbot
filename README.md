# Minecraft Status Discord Bot
Bot still incomplete.

## Getting started
Install the necessary dependencies: `mcstatus`, `discord.py`
```
pip install mcstatus
pip install -U discord.py
```

## Configuration file format
The configuration file is not pushed as it contains the bot token and the local server IP.
Format:
```
[shan]
Token = <Discord bot token>
IP = <server IP>:<port>
```

## What is working
- Commands:
  - Ping IP from server (sanitized)
  - List currently available players
  - Relay communications from the discord channel to the server (unsanitized)
  - Play rock paper scissors (unsanitized)
  
## To-do
- Include crontab scripts to:
  - Autostart script
  - Autostart server in a `tmux` session
  - Check whether server is running
  - Check whether server is running slow and requires a restart
- Use the `libtmux` library to enable communications between the python script and the currently running `tmux` session. After that is established:
  - Enable sending restart commands from discord bot
  - Enable sending whitelist commands from discord bot
  - Enable bot to mirror game chat to discord server