from math import sin, cos, log10

var('frame', NUMBER,  32, 3, 250)

size(400, 800)
background(0)

cX = random(1, 10)
cY = random(1, 10)

x = 200
y = 54
fontsize(10)

for i in range(int(frame)):
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