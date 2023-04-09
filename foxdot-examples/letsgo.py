
Root.default.set("C")

p8 >> pads([2,4,6], sus=3, dur=8, room=1, mix=0.5)
p8.solo(0)
p8.stop()

p3.stop()
p1.stop()

p9 >> pads(4*[2,4,6]+4*[2,3,6], sus=3, scale=Scale.major)

p2 >> bass(4*3*[2]+4*3*[1])

p9.stop()

p2.stop()
p3 >> pluck(PTri(5), scale=Scale.default.pentatonic)

p3.stop()

p1.stop()
p1 >> pluck(PTri(7), scale=Scale.default.pentatonic, bpm=240, room=1, mix=0.5)

print(Scale.default.__dict__)

a1 >> play('    !   !')

p1.stop()

p3.solo(0)

p3.stop()
p4.stop()

p1.play()
p2.play()

Clock.bpm=120

a1 >> play('--------', bpm=120)
a2 >> play('x o xo  x o xoxx', bpm=120)

a3 >> play('---[--]')

a5 >> play('xtxo')

a1 >> play('--------', bpm=120)
a2 >> play('x o (x[xx])o ( o)', bpm=120)



c3 >> play('I have the beat')


c5 >> play(' ')
c5.solo()

c4.solo()


c5.solo()


a3 >> play(8*'x', bpm=120, amp=6)

a3.stop()

p8.solo(0)

b1 >> jbass(var([0,1,2,-1],4), chop=1, slide=var([0,--1],4))

b1.stop()

d1 >> dirt(var([0,2],8), sus=4, chop=2, amp=0.5)
d1.stop()

g1 >> gong(amp=0.2).follow(b1)

g1.stop()


p3 >> play('x-o-x-oo')

p3.stop()

p4 >> play('zw  ')
p4.stop()

print(Samples)

Samples.addPath('/home/pol/Music/livecoding')

s2 >> stretch('*', pshift=-5, sample=1, dur=60, room=1, mix=0.2)
s2.stop()

p1 >> play('x (o[ox]) ')
p1.stop()


p1.stop()

Clock.bpm = 183

s3 >> loop('/home/pol/Music/livecoding', dur=50, sample=8, room=1, mix=0)

s4 >> stretch('/home/pol/Music/livecoding', dur=10, sample=3, room=1, mix=0)

s3.solo()

s2 >> loop('*', sample=5, dur=10, bpm=100, room=1, mix=0.2, pan=[0,1])

s2 >> loop('*', sample=10, dur=11)

s2.stop()

Clock.bpm = 150

p0 >> play('-------------#--', room=1, mix=0.1)
p1 >> play('xxo[ o][ o]x o[ o][xx]o[ o][ o]x o', room=1, mix=0.1)

p1 >> play('xxu[ u][ u]x u[ u][xx]u[ u][ u]x u', room=1, mix=0.1)

p1 >> play('XXo[ o][ o]X o[ o][XX]o[ o][ o]X o', room=1, mix=0.1)


p0 >> play('-------------#--', room=1, mix=0.1)
p1 >> play('vvu[ u][ u]v u[ u][vv]u[ u][ u]v u', room=1, mix=0.1)


.sometimes('stutter', 4, dur=1).rarely('reverse')



s2.stop()

s2.solo()

u1 >> gong([3,2,1,2,0,0])

u2 >> play(' ~ ~ ~')

u3 >> play('x x x ')

u4 >> play(' ewezz')

u5 >> play('xo  xoo')

print(SynthDefs)

v1 >> varsaw('2  26 2 1 2 3   ', bpm=300)

v2 >> play(['C'], dur=16, bpm=300)

v3 >> play('x oox oox oox oo', bpm=300)

v4 >>play('p',bpm=100)

v5 >> gong('2   6   ', dur=4)

Clock.bpm=120

Root.default.set("D")

b0 >> play('-----(---,=#=)')
b1 >> play('x-o-x-o(o([oo](!*)))', room=1, mix=0.1)

c3 >> charm([(0,5,9),(0,9,15),(0,[3,4],5)], dur=4, sus=3, room=1, mix=0.3, scale=Scale.major, amp=linvar(1,0))

d4 >> jbass([0,[5,0]], sus=4, room=1, mix=0.7, amp=linvar(0,2))

d5 >> dirt(var([0,2],8), sus=4, chop=2, amp=0.5)

g1 >> gong(amp=0.2).follow(d5)

d4.solo()

b2 >> sitar([0,5,9,var([2,3,4],4),0], sus=2, dur=[1,1,1, 2, 1], room=1, mix=0.3, amp=linvar(1,0), scale=Scale.major)

b1.solo()

b3 >> arpy([0,5], oct=4, dur=8, sus=4, room=1, mix=0.6)


a2 >> jbass([1, [2,1], 0, 0])

a1 >> jbass([1,' ',4,' ', 5, ' ',[2,var([1,5])]], sus=1.5, room=1, mix=0.1)

a2.stop()
a1.stop()

a1 >> pads(P[0,2,5] + (0,2,var([4,5])), dur=var([2,3,4]))


p1 >> play('x-o')
