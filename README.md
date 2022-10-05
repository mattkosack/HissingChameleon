# HissingChameleon
Silly discord bot for dumb things.

Everyone's got their own discord bot. Here's mine.

[Invite link](https://discord.com/api/oauth2/authorize?client_id=990806328295440424&permissions=413927852096&scope=bot)

# On Heroku, add these buildpacks
- https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest.git
- https://github.com/xrisk/heroku-opus.git

# On the pi
- `chmod +x auto_deploy.sh`
- make it a service/cron job
- `sudo apt install ffmpeg`
- https://obsproject.com/forum/threads/obs-raspberry-pi-build-instructions.115739/

# TODO

```
Traceback (most recent call last):                                                                                                     File "/home/matt/.local/lib/python3.9/site-packages/discord/ext/commands/core.py", line 190, in wrapped                                ret = await coro(*args, **kwargs)                                                                                                  File "/home/matt/HissingChameleon/hissing_chameleon.py", line 144, in color                                                            img.save(image_binary, "PNG")                                                                                                    AttributeError: 'tuple' object has no attribute 'save'                                                                                                                                                                                                                    The above exception was the direct cause of the following exception:                                                                                                                                                                                                      Traceback (most recent call last):                                                                                                     File "/home/matt/.local/lib/python3.9/site-packages/discord/ext/commands/bot.py", line 1347, in invoke                                 await ctx.command.invoke(ctx)                                                                                                      File "/home/matt/.local/lib/python3.9/site-packages/discord/ext/commands/core.py", line 986, in invoke                                 await injected(*ctx.args, **ctx.kwargs)  # type: ignore                                                                            File "/home/matt/.local/lib/python3.9/site-packages/discord/ext/commands/core.py", line 199, in wrapped                                raise CommandInvokeError(exc) from exc                                                                                           discord.ext.commands.errors.CommandInvokeError: Command raised an exception: AttributeError: 'tuple' object has no attribute 'save'
```