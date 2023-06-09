# pycamp-liveart
live art live coding sandbox for pycamp

# quickstart

## shoebot

`pip install shoebot`

`sbot shoebot/circle_circle.bot`

[tutorials](https://docs.shoebot.net/tutorial.html)

## foxdot

this can't be quick.

what worked:
```
Install or connect to a supercollider server (**hard**), even 3.10
Quarks.install("FoxDot")
FoxDot.start
```

on a virtualenv

```
pip install FoxDot
```
run `FoxDot` it should say 'connected to supercollider' and if you send `p1 >> play('-x-o')`

maybe I did this

```bash
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys FABAEF95
sudo add-apt-repository ppa:supercollider/ppa
sudo apt-get update
sudo apt-get install supercollider-ide
```

once you're more advanced you can start it headless and use any client and just the FoxDot server.

```bash
sclang sc-foxdot-visual.scd
python3 foxdot-server.py
```

and then some live editor that sends commands to foxdot or simply run

```python
from FoxDot import *
Clock.bpm=150
p1 >> pads([0, 1, 2, 3])
d1 >> play("x-o-")
Go()
```

but for live coding, the vscode extension FoxDot v0.0.5 **yasuyuky** also worked for me. control+shift+p to start foxdot, super+enter to send codeblock

but there are many others


## obs

[obsstudio](https://obsproject.com/download#linux)

# brainstorm options

[pyprocessing 3.5.4 with python mode](https://processing.org/releases) -- [getting started](https://py.processing.org/tutorials/gettingstarted/)

[FoxDot](https://github.com/Qirky/FoxDot)

[godot]() gdcsript

[showbot](shoebot.net) `pip install shoebot`

[promap](promap) para mapear

run with `sbot somesbotscript.bot` e.g.

```python
from math import sin, cos, log10

size(400, 800)
background(0)

cX = random(1, 10)
cY = random(1, 10)

x = 200
y = 54
fontsize(10)

for i in range(278):
    x += cos(cY) * 11
    y += log10(cX) * 1.85 + sin(cX) * 5

    fill(random() - 0.4, 0.8, 0.8, random())

    s = 10 + cos(cX) * 15
    oval(x - s / 2, y - s / 2, s, s)
    # Try the next line instead of the previous one to see how
    # you can use other primitives.
    # star(x-s/2, y-s/2, random(5, 10), inner=2+s*0.1, outer=10+s*0.1)

    cX += random(0.25)
    cY += random(0.25)
```


# brainstorm ideas

we could live stream to a central server with [OBS](https://support.accelevents.com/en/articles/4102301-broadcasting-with-obs-or-wirecast-through-rtmp-stream)

# processing

[https://pypi.org/project/processing-py/](processing-py from pypi, cli only)

# FoxDot

[supercollider](https://supercollider.github.io/downloads) also available via linux repositories

[crt-live-coding](https://github.com/Swordfish90/crt-live-coding)

```bash
sclang sc-foxdot-visual.scd
python3 foxdot-server.py
```

And then something to run foxdot commands

vim `./crt-live-coding -e vim` and then `:!source ~/code/crt-live-coding/vimrc`, or place this to your vimrc

```
vnoremap <silent> <CR> y:call system('nc localhost 7088 -w 0', @")<CR>
nnoremap <silent> <CR> :call system('nc localhost 7088 -w 0', getline('.'))<CR>
:set filetype=python
syntax on
highlight EndOfBuffer ctermfg=black ctermbg=black
set shortmess=at
```

That way every time you press enter on normal mode, the line will be sent to the FoxDot server

Atom [FoxDOt plugin](https://github.com/KoltesDigital/atom-foxdot) also works well, and there's also an [extension for vscode](https://marketplace.visualstudio.com/items?itemName=vvzen.vscode-foxdot) (untested)