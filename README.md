# HissingChameleon
Silly discord bot for dumb things.

Everyone's got their own discord bot. Here's mine.


# On Heroku, add these buildpacks
- https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest.git
- https://github.com/xrisk/heroku-opus.git

### Note: I stopped using Heroku for 2 main reasons: youtube-dl doesn't work so well there, and more importantly, Heroku will be discontinuing its free tier soon.

# Quirks/Notes

I run the stream and game on an ubuntu machine, apparently PyAutoGui doesn't work with Wayland, so I had to switch to Xorg. See more [here](https://askubuntu.com/questions/1433002/ubuntu-gui-cant-take-virtual-keystrokes)

can't use PyAutoGui press, need to use keydown and keyup


# TODO

* Refactor the documentation because 'discord-pretty-help' will make it look nice in the chat
* General refactoring, some stuff can be further de-coupled
    * It's not *terrible* but it could be better
* More color format support would be nice
    * I think python has support for color conversion, or its getting it
* Use machine learning project to generate color from text.
   * this is basically the reverse of how it works now, but it could be interesting to grab the exact color from the sources I have, or generate one "from scratch"
* Some sort of queue system for the clips commands
    * one for playing clips and one for adding clips

* Maybe do something with openai/gpt-3
    * The obvious thing is just return a response from a given prompt, but people can easily do that, and I also don't want to constantly burn my API calls

# Quotes to add
- Kalin clips
- Kalin quotes
- Schmaden
- Jinzo
- dasher on em
- kaiba funny
- I'm jack atlas
- paradox brothers joey clocks
- BLACK ROSE DRAGON
- kaiba show me the god card
- junk warrior poem (from two become one)
- yugi boy
- shadows and curtains
- Sayer duel, carly and jack married
- Jacky boi - dark signer carly
- sayer dying
- time to duel with a ghoul
- synchro what
- master of faster
- special sign
- piercing
- Yugioh poems
- riding duel
