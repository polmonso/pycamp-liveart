from math import sin, cos, log10

boids = ximport("boids")

radius = 20


flock = boids.flock(10, 0, 0, 512, 512)
for boid in flock:
    print(boid.x, boid.y)
    ellipse(
        boid.x,
        boid.y,
        radius,
        radius,
    )
