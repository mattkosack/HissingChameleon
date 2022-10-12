# HissingChameleon
Silly discord bot for dumb things.

Everyone's got their own discord bot. Here's mine.

[Invite link](https://discord.com/api/oauth2/authorize?client_id=990806328295440424&permissions=413927852096&scope=bot)

I don't own the music. But what's the difference between my bot streaming it from youtube and me just downloading it and not selling it?

# On Heroku, add these buildpacks
- https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest.git
- https://github.com/xrisk/heroku-opus.git

# On the pi
- `chmod +x auto_deploy.sh`
- make it a service/cron job
- `sudo apt install ffmpeg`
- https://obsproject.com/forum/threads/obs-raspberry-pi-build-instructions.115739/

# youtube-dl
- `youtube-dl -x --audio-format mp3 <url>`

# TODO
