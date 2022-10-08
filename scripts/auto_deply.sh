#!/bin/sh
# This is a horrible way to do this, but I don't care.
result=$(git pull)
if [ "$result" = "Already up-to-date." ]; then
    # No change, do nothing
    echo "No changes"
else
    echo "Changes detected, deploying"
    # stop python script
    sudo killall python
    # start python script
    python ~/home/matt/HissingChameleon/hissomg_chameleon.py &
fi