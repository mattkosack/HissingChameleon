This is from [linuxize](https://linuxize.com/post/how-to-use-linux-screen/)

## Starting Linux Screen

To start a screen session, simply type screen in your console:

```
screen
```

This will open a screen session, create a new window, and start a shell in that window.

Now that you have opened a screen session, you can get a list of commands by typing:

```
Ctrl+a ?
```

## Starting Named Session

Named sessions are useful when you run multiple screen sessions. To create a named session, run the screen command with the following arguments:

```
screen -S session_name
```

It’s always a good idea to choose a descriptive session name.

## Working with Linux Screen Windows

When you start a new screen session, it creates a single window with a shell in it.

You can have multiple windows inside a Screen session.

To create a new window with shell type `Ctrl+a c`, the first available number from the range `0...9` will be assigned to it.

Below are some most common commands for managing Linux Screen Windows:

```
    Ctrl+a c Create a new window (with shell).
    Ctrl+a " List all windows.
    Ctrl+a 0 Switch to window 0 (by number).
    Ctrl+a A Rename the current window.
    Ctrl+a S Split current region horizontally into two regions.
    Ctrl+a | Split current region vertically into two regions.
    Ctrl+a tab Switch the input focus to the next region.
    Ctrl+a Ctrl+a Toggle between the current and previous windows
    Ctrl+a Q Close all regions but the current one.
    Ctrl+a X Close the current region.
```

## Detach from Linux Screen Session

You can detach from the screen session at any time by typing:

```
Ctrl+a d
```

The program running in the screen session will continue to run after you detach from the session.
Reattach to a Linux Screen

To resume your screen session use the following command:

```
screen -r
```

In case you have multiple screen sessions running on your machine, you will need to append the screen session ID after the r switch.

To find the session ID list the current running screen sessions with:

```
screen -ls
```

```
There are screens on:
    10835.pts-0.linuxize-desktop   (Detached)
    10366.pts-0.linuxize-desktop   (Detached)
2 Sockets in /run/screens/S-linuxize.
```

If you want to restore screen 10835.pts-0, then type the following command:

```
screen -r 10835
```