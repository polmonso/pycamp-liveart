# pycamp-liveart
live art live coding sandbox for pycamp

# quickstart

## shoebot

`pip install shoebot`

`sbot shoebot/circle_circle.bot`

[tutorials](https://docs.shoebot.net/tutorial.html)

## foxdot

this can't be quick.

Install or connect to a supercollider server (**hard**)

The vscode extension FoxDot v0.0.5 **yasuyuky** also worked for me


```
$ sclang sc-foxdot-visual.scd
$ python3 foxdot-server.py
$ ./crt-live-coding -e vim
```


## obs

[obsstudio](https://obsproject.com/download#linux)

# brainstorm options

[pyprocessing 3.5.4 with python mode](https://processing.org/releases) -- [getting started](https://py.processing.org/tutorials/gettingstarted/)

[FoxDot](https://github.com/Qirky/FoxDot)

[godot]() gdcsript

[showbot](shoebot.net) `pip install shoebot`

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