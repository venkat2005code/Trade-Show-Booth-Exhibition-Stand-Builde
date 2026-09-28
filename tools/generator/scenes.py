"""Booth compositions: portfolio renders, hero art, service visuals, process steps, blog covers."""
from kit import Scene, shade, mix

OR = '#ff5a1f'
INK = '#0e1013'


def floor(sc, m=5, c='#1d2129', top='#232833'):
    sc.box(-m, -m, -.4, sc.W + 2 * m, sc.D + 2 * m, .4, c, top=top, edge=False)


def deck(sc, c='#2c313b', top='#303643', carpet='#0e1115', h=.5, m=1.5):
    sc.box(0, 0, 0, sc.W, sc.D, h, c, top=top)
    sc.box(m, m, h, sc.W - 2 * m, sc.D - 2 * m, .1, carpet, top=shade(carpet, .06), edge=False)


def counter(sc, x, y, dx, dy, c='#f5f3ee', top=OR, h=3.4, z=.6):
    sc.box(x, y, z, dx, dy, h, c, top=top)


# ------------------------------------------------------------------ portfolio renders
def nova(sc):
    W, D = sc.W, sc.D
    sc.hall('#181c24', '#090b0e')
    floor(sc)
    deck(sc)
    sc.box(4, 1.5, .6, 32, .8, 10, '#1c2027')
    sc.screen_y(5, 35, 1.6, 9.6, 2.31, OR, '#ffb347', bars=4)
    sc.box(1.5, 5, .6, .8, 19, 10, '#1c2027')
    sc.screen_x(6, 23, 1.6, 9.6, 2.31, '#2d6bff', '#7be0ff', bars=3)
    sc.box(17, 12, .6, 6, 6, 6.4, '#ebe8e1')
    sc.box(16.7, 11.7, 7, 6.6, 6.6, 1.2, OR)
    sc.box(17, 12, 8.2, 6, 6, 3.6, '#ebe8e1')
    sc.ty(17.4, 18.01, 9.4, 'NOVA', 1.7, INK, w=900)
    sc.tx(23.01, 18, 9.4, 'TECH', 1.7, OR, w=900)
    sc.ring(20, 15, 14.2, 12.5, .6, '#f4f4f4', inner=OR)
    for dx, dy in ((8.8, 0), (-8.8, 0), (0, 8.8), (0, -8.8)):
        sc.cable(20 + dx, 15 + dy, 14.2, 23)
    counter(sc, 5, 20, 10, 2.2)
    counter(sc, 27, 25, 9, 2.2)
    sc.cyl(31, 12, 2.3, .6, 3.3, '#f5f3ee', top=OR)
    sc.cyl(9, 12, 2.3, .6, 3.3, '#f5f3ee', top='#7be0ff')
    for x, y, c in ((12, 26, '#8b93a1'), (24, 22, '#c9cdd6'), (33, 19, '#6b7280'), (13, 15, '#a3a9b3')):
        sc.person(x, y, c)
    sc.spot(20, 15, 14, 20, 15, 9, '#ffb98f', .22)
    sc.spot(9, 12, 12, 9, 12, 4, '#7be0ff', .2)


def kite(sc):
    W, D = sc.W, sc.D
    sc.hall('#f3efe8', '#d8d2c6', glow='#ffffff', grid=.06, gridc='#000000')
    floor(sc, 4, '#e5dfd2', '#efe9dc')
    deck(sc, '#cfc8b9', '#dcd5c6', '#e9e3d6')
    for i in range(5):
        c = ('#ffffff', '#ffe6da', '#ffffff', '#ffd1bb', '#ffffff')[i]
        sc.box(1 + i * 3.7, 1.2, .6, 3.5, .7, 9.5, c, top='#fff')
    sc.box(1 + 3.7, 1.2, 6.4, 3.5, .8, 1.6, OR, top='#ff8a5c')
    sc.ty(5.2, 2.11, 6.85, 'KITE', 1.1, '#fff', w=900)
    sc.fy(12.5, 16, 1.8, 4.4, 2.11, '#111418')
    counter(sc, 3, 6.5, 6, 1.6, '#ffffff', '#ffffff', 3.2)
    sc.box(3, 6.5, 3.8, 6, 1.6, .25, OR, edge=False)
    sc.box(12, 2.4, .6, 5, .7, .3, '#cfc8b9', edge=False)
    for k in range(3):
        sc.box(12.4 + k * 1.5, 2.5, .9 + k * 0, 1, .5, 1.1 + k * .2, ('#ff5a1f', '#0e1013', '#ffffff')[k])
    sc.box(16.5, 4.5, .6, .5, .5, 8, '#0e1013')
    sc.box(15.3, 4.5, 8.6, 3, .3, 2, OR)
    sc.plant(18, 8)
    sc.person(11, 8.6, '#7a808c')
    sc.spot(9, 6, 11.5, 6, 7, 3, '#fff5ec', .3)


def meridian(sc):
    sc.hall('#e9f3f4', '#c3d6d9', grid=.06, gridc='#000')
    floor(sc, 5, '#dce8ea', '#e8f1f2')
    deck(sc, '#b5cdd1', '#c6dadd', '#f3f8f8')
    sc.frame(0, 0, 0, 60, 40, 14, '#ffffff', .7)
    sc.box(0, 0, 12.4, 60, .8, 1.6, '#0d7d84')
    sc.ty(3, .81, 12.9, 'MERIDIAN HEALTH', 1.1, '#fff', w=900, ls=.15)
    sc.box(0, 0, 12.4, .8, 40, 1.6, '#0d7d84')
    for i, (x, y, c) in enumerate(((3, 4, '#12a3ab'), (22, 4, '#ffffff'), (41, 4, '#0d7d84'))):
        sc.box(x, y, .6, 16, .6, 8, c)
        sc.box(x, y, .6, .6, 8, 8, shade(c, -.06))
        sc.screen_y(x + 2, x + 14, 2.2, 6.6, y + .61, '#e8fbfb', '#9ee3e6', bars=2, bc='#0d7d84')
    sc.cyl(30, 24, 5, .6, 3.2, '#ffffff', top='#12a3ab')
    sc.cyl(30, 24, 3.4, 3.8, .3, '#12a3ab')
    sc.cyl(10, 30, 2.6, .6, 3, '#ffffff', top='#12a3ab')
    sc.cyl(50, 30, 2.6, .6, 3, '#ffffff', top='#12a3ab')
    sc.box(4, 34, .6, 12, 2, 3.2, '#ffffff', top='#0d7d84')
    sc.box(44, 20, .6, 2, 12, 3.2, '#ffffff', top='#0d7d84')
    sc.plant(6, 22)
    sc.plant(55, 12)
    for x, y, c in ((26, 32, '#5f7c83'), (37, 26, '#8fb0b6'), (18, 20, '#3f5e66'), (46, 14, '#7a9aa1')):
        sc.person(x, y, c)
    sc.spot(30, 24, 13, 30, 24, 7, '#ffffff', .3)


def curalis(sc):
    sc.hall('#eef5f6', '#cfdde0', grid=.06, gridc='#000')
    floor(sc, 4, '#dde8ea', '#e9f1f2')
    deck(sc, '#b9ced2', '#c9dcdf', '#f5f9f9')
    sc.box(1.2, 1.2, .6, 17.6, .7, 10, '#ffffff', top='#fff')
    sc.box(1.2, 1.2, .6, .7, 7.6, 10, '#f1f6f6')
    sc.disc_y(10, 1.91, 6, 3.2, '#12a3ab')
    sc.disc_y(10, 1.92, 6, 1.7, '#ffffff')
    sc.ty(6, 1.93, 1.5, 'CURALIS', 1.5, '#0d7d84', w=900)
    sc.box(4, 6, .6, 8, 1.8, 3.3, '#ffffff', top='#12a3ab')
    sc.cyl(15, 6.5, 1.1, .6, 1.8, '#0d7d84')
    sc.cyl(17, 4.5, 1.1, .6, 1.8, '#12a3ab')
    sc.box(3, 3.2, .6, 1.2, 1.2, 3, '#0e1013')
    sc.box(2.2, 3.2, 3.6, 2.8, .2, 2.4, '#12a3ab', edge=False)
    sc.plant(18, 8)
    sc.person(8.5, 8.9, '#5f7c83')
    sc.spot(10, 5, 12, 10, 6, 4, '#ffffff', .28)


def vantage(sc):
    sc.hall('#1b1214', '#0a0708', glow='#ff8a7a')
    floor(sc, 5, '#241a1c', '#2b2022')
    deck(sc, '#34292b', '#3a2f31', '#100b0c')
    sc.box(1, 1, .6, 48, .8, 8.4, '#241a1c')
    sc.screen_y(3, 47, 1.6, 8, 1.81, '#c1121f', '#ff6b4a', bars=3)
    sc.box(1, 1, .6, .8, 38, 8.4, '#241a1c')
    sc.cyl(24, 22, 9, .6, .7, '#d8d8d8', top='#efefef')
    sc.car(17, 19, 1.3, '#c1121f')
    sc.ring(24, 22, 9, 10, .35, '#fff', inner='#ff6b4a')
    # upper deck
    sc.box(0, 0, 8.6, 50, 20, .6, '#2b2022', top='#3a2f31')
    for x in range(0, 50, 10):
        sc.box(x, 19.4, 2.5, .6, .6, 6.1, '#7d868f', edge=False)
    sc.box(0, 19.4, 9.2, 50, .3, 3.2, '#9fd2e8', op=.28, edge=False)
    sc.box(0, 0, 9.2, 50, .8, 5, '#3a2f31')
    sc.box(3, 3, 9.2, 10, 4, 2.2, '#c1121f', top='#e04b3b')
    sc.box(18, 4, 9.2, 5, 5, 1.6, '#ffffff', top='#ffffff')
    sc.box(30, 3, 9.2, 10, 4, 2.2, '#c1121f', top='#e04b3b')
    sc.box(0, 0, 14.2, 50, 20, 1.6, '#c1121f', top='#e04b3b')
    sc.ty(2, 20.01, 14.6, 'VANTAGE MOTORS', 1.3, '#fff', w=900, ls=.2)
    for i in range(10):
        sc.box(41 + i * .2, 24 + i * 1.5, .6 + i * .9, 6, 1.5, .9, '#c9c1bb', edge=False)
    sc.person(10, 30, '#b8b0aa')
    sc.person(33, 28, '#8b8380')
    sc.person(30, 12, '#d0c8c2')
    sc.spot(24, 22, 13, 24, 22, 8, '#ffb0a0', .24)


def torque(sc):
    sc.hall('#0d1a1a', '#06090a', glow='#5dffc2')
    floor(sc, 5, '#122020', '#17282a')
    sc.cyl(20, 20, 16, 0, .6, '#1b2f31', top='#20383a')
    sc.cyl(20, 20, 12, .6, .3, '#0c1416', top='#101c1e')
    sc.car(13, 17, .9, '#e9eef0')
    sc.ring(20, 20, 14, 12, .5, '#5dffc2', inner='#ffffff')
    for dx, dy in ((8.5, 8.5), (-8.5, -8.5), (8.5, -8.5), (-8.5, 8.5)):
        sc.cable(20 + dx, 20 + dy, 14, 22)
    for x, y in ((3, 3), (34, 3), (3, 34), (34, 34)):
        sc.box(x, y, 0, 3, 3, 10, '#0c1416')
        sc.box(x + .6, y + .6, .6, 1.8, 1.8, 9.4, '#5dffc2', top='#b6ffe4')
    sc.ty(20.2, 10.4, 2, 'TORQUE EV', 1.4, '#5dffc2', anchor='middle', w=900)
    for x, y in ((6, 20), (6, 24), (34, 14)):
        sc.box(x, y, 0, 1.4, 1.4, 4, '#e9eef0', top='#5dffc2')
    for x, y, c in ((28, 30, '#8ea6a6'), (10, 30, '#6a8484'), (31, 24, '#b3c6c6')):
        sc.person(x, y, c)
    sc.spot(20, 20, 13.6, 20, 20, 9, '#5dffc2', .22)


def ironbridge(sc):
    sc.hall('#1c1c1a', '#0b0b0a', glow='#ffd24a')
    floor(sc, 5, '#262624', '#2d2d2a')
    deck(sc, '#3a3a36', '#42423d', '#151513')
    for i in range(0, 30, 3):
        sc.box(i, 17.2, .6, 1.5, 1.6, .05, '#ffc21a', edge=False)
    sc.box(1, 1, .6, 28, .8, 11, '#e9e5da')
    sc.box(1, 1, .6, 28, .8, 1.1, '#151513', edge=False)
    sc.box(1, 1, 8.8, 28, .9, 2.8, '#ffc21a')
    sc.ty(2, 1.91, 9.3, 'IRONBRIDGE', 1.7, INK, w=900, ls=.12)
    sc.box(4, 5, .6, 8, 5, 5, '#5a5f66')
    sc.box(4.6, 5.6, 5.6, 6.8, 3.8, 1, '#ffc21a')
    sc.box(7, 7, 6.6, 1.2, 1.2, 4, '#ffc21a')
    sc.box(7, 7, 10.6, 5, 1.1, 1.1, '#ffc21a')
    sc.cyl(12.2, 7.6, .8, 9.3, 1.6, '#151513', top='#5a5f66')
    sc.box(15, 4, .6, 12, 2.6, 2.2, '#3a3d42')
    for i in range(6):
        sc.cyl(15.8 + i * 2, 5.3, .8, 2.8, .5, '#9aa0a8')
    sc.box(3, 13, .6, 7, 1.8, 3.4, '#ffffff', top='#ffc21a')
    sc.screen_y(16, 27, 5, 8.4, 1.81, '#ffc21a', '#ffe28a', bars=3, bc=INK)
    sc.frame(0, 0, 0, 30, 20, 14, '#d5d5d0', .5)
    for x, y, c in ((17, 14, '#a8a8a0'), (22, 16, '#6e6e68')):
        sc.person(x, y, c)
    sc.spot(9, 8, 13, 9, 8, 5, '#ffe28a', .3)


def solara(sc):
    sc.hall('#e8f0e0', '#bccbb0', grid=.06, gridc='#000')
    floor(sc, 5, '#d5dfc9', '#e1ead6')
    deck(sc, '#a9b79b', '#b9c6ab', '#e5ecda')
    for k in range(4):
        sc.box(3 + k * 1.4, 22 - k * 1.4, .6 + k * .5, 24 - k * 2.8, 5, .5, '#8a6b45', top='#a4825a')
    # solar panels (tilted)
    for i in range(4):
        y0 = 4 + i * 4.6
        pts = [sc.P(4, y0, 1.5), sc.P(26, y0, 1.5), sc.P(26, y0 + 3.8, 5), sc.P(4, y0 + 3.8, 5)]
        sc.add((4, y0, 1.5, 26, y0 + 3.8, 5), sc._poly(pts, '#1d3b66', '#8fb4e8', 1.1))
        for j in range(1, 9):
            a, b = sc.P(4 + j * 2.44, y0, 1.5), sc.P(4 + j * 2.44, y0 + 3.8, 5)
            sc.add((4 + j * 2.44, y0, 1.5, 4 + j * 2.44 + .01, y0 + 3.8, 5), '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#8fb4e8" stroke-opacity=".5" stroke-width=".8"/>' % (a + b))
    sc.box(1, 1, .6, 1.2, 28, 10, '#b98d5a', top='#d5aa73')
    for k in range(14):
        sc.box(2.2, 1.6 + k * 2, .6, .5, .9, 10, '#8a6b45', edge=False)
    sc.box(12, 1, .6, 16, .8, 8, '#ffffff')
    sc.ty(13.5, 1.91, 4, 'SOLARA', 2.2, '#2f7d3a', w=900, ls=.1)
    sc.cyl(10, 6, 1.6, .6, 4, '#f6f8f0', top='#3a9b4b')
    sc.plant(27, 27, leaf='#3f9d55')
    sc.plant(4, 27)
    sc.person(20, 25, '#7a856d')
    sc.person(26, 21, '#4c5644')
    sc.spot(15, 15, 13, 15, 15, 8, '#fff7d6', .3)


def lumen(sc):
    sc.hall('#1a1424', '#09070f', glow='#d68aff')
    floor(sc, 4, '#211a2c', '#281f35')
    deck(sc, '#2b2238', '#332a41', '#120e19')
    sc.box(1, 1, .6, 18, .8, 10, '#151019')
    sc.box(1, 1, .6, .8, 9, 10, '#151019')
    sc.ty(3.2, 1.83, 6.3, 'LUMEN', 2.8, '#ff6bd5', w=900, ls=.15)
    sc.ty(3.2, 1.83, 6.3, 'LUMEN', 2.8, '#ffd1f3', w=900, ls=.15)
    for k in range(3):
        sc.box(3 + k * 4.6, 1.85, 1.5 + k * 0, 3.6, .4, .2, '#3d3050', edge=False)
        for j in range(3):
            sc.box(3.4 + k * 4.6 + j * 1, 1.85, 1.7, .7, .4, .9 + .3 * ((j + k) % 3), ('#ff6bd5', '#7be0ff', '#ffe066')[(j + k) % 3], edge=False)
    sc.cyl(10, 6.5, 1.5, .6, 2.6, '#f3f0f7', top='#ff6bd5')
    sc.cyl(5, 6.5, 1.3, .6, 1.8, '#f3f0f7', top='#7be0ff')
    sc.cyl(15, 6.5, 1.3, .6, 3.4, '#f3f0f7', top='#ffe066')
    counter(sc, 3, 3.2, 4, 1.4, '#f3f0f7', '#ff6bd5', 3.2)
    sc.person(12, 9, '#a38bb6')
    sc.spot(10, 6, 11, 10, 6.5, 3.4, '#ff8ae0', .26)


def nordic(sc):
    sc.hall('#f6f1e6', '#ddd3bf', grid=.06, gridc='#000')
    floor(sc, 5, '#e6dcc8', '#efe6d3')
    deck(sc, '#cdbf9f', '#d9cdb1', '#f3ebdb')
    sc.frame(0, 0, 0, 40, 30, 12, '#ffffff', .5)
    cols = ('#e7b6a6', '#a9c4b8', '#b8c3e0', '#f0d38a')
    for i in range(4):
        x, y = 2 + (i % 2) * 19, 2 + (i // 2) * 14
        sc.box(x, y, .6, 16, .5, 9, cols[i])
        sc.box(x, y, .6, .5, 10, 9, shade(cols[i], -.06))
        sc.box(x + 5, y + 4.5, .6, 4, 2.2, 1.6, '#f6f1e6', top='#ffffff')
        sc.cyl(x + 12, y + 6, .9, .6, 3, '#d1a86a', top='#e9c68d')
    sc.box(0, 0, 10.4, 40, .6, 1.4, '#22252a')
    sc.ty(1.5, .61, 10.75, 'NORDIC DESIGN COLLECTIVE', .78, '#fff', w=800, ls=.1)
    sc.plant(19.5, 15)
    sc.person(20, 26, '#8b8378')
    sc.person(11, 20, '#a89f94')
    sc.spot(20, 15, 11.6, 20, 15, 7, '#fff3d6', .3)


def halcyon(sc):
    sc.hall('#101a2c', '#070b13', glow='#f2c96b')
    floor(sc, 5, '#152036', '#1b2942')
    deck(sc, '#243250', '#2b3a5a', '#0c1220')
    sc.box(1, 1, .6, 28, .8, 8.6, '#1a2540')
    sc.box(2, 1.8, 1.4, 8, .3, 5.6, '#f2c96b', edge=False)
    sc.box(8, 12, .6, 8, 2.4, 3.4, '#f7f4ea', top='#f2c96b')
    sc.cyl(23, 12, 3, .6, 2.4, '#243250', top='#f2c96b')
    sc.cyl(23, 12, 1.8, 3.0, 1.4, '#f2c96b', top='#fff1c4')
    sc.box(0, 0, 9.4, 30, 15, .5, '#1a2540', top='#2b3a5a')
    sc.box(0, 14.4, 9.9, 30, .3, 3.4, '#9fd2e8', op=.25, edge=False)
    sc.box(0, 0, 9.9, .5, 15, 3.4, '#9fd2e8', op=.16, edge=False)
    sc.box(4, 3, 9.9, 8, 3.4, 1.6, '#f2c96b', top='#fff1c4')
    sc.box(16, 3, 9.9, 5, 5, 1.2, '#f7f4ea', top='#ffffff')
    sc.box(0, 0, 13.3, 30, 15, 1.2, '#f2c96b', top='#fff1c4')
    sc.ty(1.5, 15.01, 13.55, 'HALCYON CAPITAL', .9, '#101a2c', w=900, ls=.15)
    for i in range(7):
        sc.box(24 + i * .3, 19 + i * 1.6, .6 + i * 1.25, 5, 1.6, 1.25, '#e9e2cf', edge=False)
    sc.person(6, 22, '#9aa6c0')
    sc.person(16, 24, '#c7cfe0')
    sc.person(12, 8, '#6b789a')
    sc.spot(23, 12, 8, 23, 12, 4, '#ffe08a', .28)


def harvest(sc):
    sc.hall('#f8efdf', '#e2d3b9', grid=.06, gridc='#000')
    floor(sc, 5, '#eadcc3', '#f3e8d2')
    deck(sc, '#c9b48f', '#d6c2a0', '#efe2c9')
    sc.box(1, 1, .6, 28, .8, 9, '#f3ede0')
    for k in range(14):
        sc.box(1.2 + k * 2, 1.8, .6, 1.1, .5, 9, '#b98d5a', edge=False)
    sc.box(5, 1.8, 5.2, 20, .4, 2.8, '#2f6b3a')
    sc.ty(7, 2.21, 5.8, 'HARVEST & HEARTH', 1.4, '#f8efdf', w=900, ls=.08)
    sc.box(4, 6, .6, 22, 2.4, 3.4, '#fdfaf1', top='#2f6b3a')
    sc.box(4, 6, .6, 2.4, 8, 3.4, '#fdfaf1', top='#2f6b3a')
    for i in range(5):
        sc.cyl(9 + i * 3.6, 12.4, .8, .6, 2.4, '#b98d5a', top='#d9b07a')
    for x in (8, 14, 20):
        sc.cable(x, 3, 9, 14, '#6e6250')
        sc.cyl(x, 3, .9, 8.1, .9, '#f2c96b', top='#fff1c4')
    sc.plant(27, 16, leaf='#3f9d55')
    sc.plant(3, 17, leaf='#3f9d55')
    sc.person(12, 16, '#a89a83')
    sc.person(22, 14, '#7d6f5a')
    sc.spot(14, 3, 8, 14, 8, 5, '#ffe9a6', .3)


PROJECT_SCENES = [
    ('project-01', nova, dict(W=40, D=30, H=15), 'NovaTech island booth render'),
    ('project-02', kite, dict(W=20, D=10, H=11), 'Kite modular rental inline stand render'),
    ('project-03', meridian, dict(W=60, D=40, H=14), 'Meridian Health pavilion render'),
    ('project-04', curalis, dict(W=20, D=10, H=11), 'Curalis rental inline stand render'),
    ('project-05', vantage, dict(W=50, D=40, H=16), 'Vantage Motors double-decker stand render'),
    ('project-06', torque, dict(W=40, D=40, H=14), 'Torque EV island stand render'),
    ('project-07', ironbridge, dict(W=30, D=20, H=14), 'Ironbridge peninsula booth render'),
    ('project-08', solara, dict(W=30, D=30, H=12), 'Solara solar island booth render'),
    ('project-09', lumen, dict(W=20, D=10, H=11), 'Lumen retail inline booth render'),
    ('project-10', nordic, dict(W=40, D=30, H=12), 'Nordic Design Collective rental pavilion render'),
    ('project-11', halcyon, dict(W=30, D=30, H=15), 'Halcyon Capital double-decker stand render'),
    ('project-12', harvest, dict(W=30, D=20, H=10), 'Harvest & Hearth peninsula booth render'),
]


# ------------------------------------------------------------------ hero art
def hero_scene(w=1200, h=900, zoom=1.0, focus=None, transparent=True):
    sc = Scene(w, h, 40, 30, 17, fit=.86, cy=.62, zoom=zoom, focus=focus)
    if not transparent:
        sc.hall('#181c24', '#090b0e')
    sc.ground(-4, -4, 48, 38, '#ffffff', z=-.3, op=.05)
    sc.box(0, 0, -.1, 40, 30, .6, '#2b303a', top='#343a46')
    sc.box(1.5, 1.5, .5, 37, 27, .1, '#10131a', top='#141821', edge=False)
    # back walls
    sc.box(1.5, 1.5, .6, 24, .8, 11, '#f2f0ea', top='#ffffff')
    sc.box(1.5, 1.5, .6, .8, 15, 11, '#e6e3dc')
    sc.box(1.5, 1.5, 8.3, 24, .9, 3.3, OR, top='#ff8a5c')
    sc.ty(3, 2.42, 8.9, 'YOUR BRAND', 2, INK, w=900, ls=.15)
    sc.screen_y(5, 22, 1.6, 7, 2.31, '#12161d', '#242b39', bars=4)
    sc.screen_x(4, 13, 1.6, 7, 2.31, '#2d6bff', '#7be0ff', bars=2)
    # tower + hanging sign
    sc.box(27, 15, .6, 5, 5, 5, '#1b1f27')
    sc.box(26.7, 14.7, 5.6, 5.6, 5.6, 1.1, OR)
    sc.box(27, 15, 6.7, 5, 5, 4.6, '#1b1f27')
    sc.ty(27.3, 20.01, 8, 'STAND', 1.3, '#fff', w=900)
    sc.tx(32.01, 20, 8, '4B-212', 1.2, OR, w=900)
    sc.box(11, 9, 14.6, 16, 8, 1.8, '#ffffff', top='#ffffff')
    sc.box(11, 9, 14.6, 16, 8, .3, OR, edge=False)
    sc.ty(12, 17.01, 15.2, 'YOUR BRAND', 1.3, INK, w=900, ls=.1)
    sc.tx(27.01, 17, 15.2, 'HERE', 1.3, OR, w=900)
    for dx, dy in ((1, 1), (14, 1), (1, 6.4), (14, 6.4)):
        sc.cable(11 + dx, 9 + dy, 16.4, 25)
    counter(sc, 6, 19, 11, 2.4, '#f5f3ee', OR)
    sc.box(7.5, 19.5, 4, 4, .2, 2.4, '#0e1013')
    counter(sc, 24, 3, 2.4, 9, '#f5f3ee', '#ffffff')
    sc.cyl(20, 21, 2.2, .6, 3.3, '#f5f3ee', top=OR)
    sc.cyl(33, 8, 1.8, .6, 2.6, '#f5f3ee', top='#7be0ff')
    sc.plant(36, 24)
    sc.plant(3, 25)
    for x, y, c in ((14, 25, '#9aa1ad'), (23, 26, '#d0d4dc'), (31, 25, '#7a808c'), (12, 14, '#c3c8d1'), (34, 13, '#8b93a1')):
        sc.person(x, y, c)
    sc.spot(19, 14, 14.4, 19, 14, 8, '#ffb98f', .22)
    return sc


# ------------------------------------------------------------------ services (640x480)
def svc_base(c1='#151a22', c2='#0b0e13', W=24, D=24, H=12, **kw):
    glow = kw.pop('glow', '#ffffff')
    sc = Scene(640, 480, W, D, H, fit=.72, cy=.6, **kw)
    sc.hall(c1, c2, glow=glow)
    return sc


def s_design():
    sc = svc_base(W=26, D=22, H=10)
    sc.box(-2, -2, -.3, 30, 26, .3, '#1c222c', top='#222a36', edge=False)
    sc.box(2, 2, 0, 22, 18, .25, '#eef2f7', top='#f5f8fc', edge=False)
    for i in range(1, 11):
        a, b = sc.P(2 + i * 2, 2, .3), sc.P(2 + i * 2, 20, .3)
        sc.add((2 + i * 2, 2, .3, 2 + i * 2 + .01, 20, .31), '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#2d6bff" stroke-opacity=".25"/>' % (a + b))
    sc.wire(5, 5, .3, 10, 8, 6, '#0e1013', .9, 1.4)
    sc.wire(15, 9, .3, 6, 6, 3, '#0e1013', .6, 1.2, '4 3')
    sc.box(7, 7, .3, 4, 3, 3, OR, top='#ff8a5c')
    sc.wire(3, 3, 6.4, 18, 14, 0.01, '#2d6bff', .8, 1, '5 4')
    sc.box(19, 3, .3, 4, .5, .5, '#ffc21a', edge=False)
    return sc.render('Custom booth design blueprint')


def s_construct():
    sc = svc_base(W=26, D=20, H=12)
    sc.box(-3, -3, -.3, 32, 26, .3, '#1c222c', top='#222a36', edge=False)
    sc.box(0, 0, 0, 20, 16, .6, '#2c313b', top='#343a46')
    sc.frame(1, 1, .6, 18, 14, 10, '#d5d8de', .55)
    sc.box(1.5, 1, 1.2, 8, .3, 8, '#f2f0ea', edge=False)
    sc.box(9.5, 1, 1.2, 8, .3, 8, OR, edge=False)
    for k in range(4):
        sc.box(21, 2 + k * .8, .1 + k * 0, 4, .7, 5, '#f2f0ea' if k % 2 else '#cfd3da', edge=False)
    sc.box(3, 16.5, 0, 12, 1, .6, '#8a6b45')
    sc.person(11, 9, '#9aa1ad')
    return sc.render('Exhibition stand construction frame')


def s_rental():
    sc = svc_base(W=26, D=16, H=10)
    sc.box(-3, -3, -.3, 32, 22, .3, '#1c222c', top='#222a36', edge=False)
    sc.box(0, 0, 0, 22, 12, .4, '#2c313b', top='#343a46')
    for i in range(6):
        sc.box(1 + i * 3.4, 1.2, .4, 3.2, .6, 8.6, ('#f2f0ea', OR, '#f2f0ea', '#cfd3da', OR, '#f2f0ea')[i])
    counter(sc, 3, 6, 6, 1.6, '#f5f3ee', OR, 3.2, .4)
    sc.box(12, 6.5, .4, 1.6, 1.6, 2.2, '#0e1013')
    sc.box(16, 6, .4, 4, 1.6, 1.4, '#f5f3ee', top='#ffffff')
    for k in range(3):
        sc.box(23, 3 + k * 3.2, .1, 2.6, 3, 2.4, '#3a4150', top='#4a5266')
    return sc.render('Rental exhibition stand modular kit')


def s_install():
    sc = svc_base(W=26, D=22, H=13)
    sc.box(-3, -3, -.3, 32, 28, .3, '#1c222c', top='#222a36', edge=False)
    sc.box(0, 0, 0, 20, 16, .5, '#2c313b', top='#343a46')
    sc.box(1, 1, .5, 12, .7, 8, '#f2f0ea')
    sc.frame(13, 1, .5, 7, 14, 9, '#d5d8de', .5)
    sc.box(2, 1.7, 5.6, 8, .3, 2.4, OR, edge=False)
    sc.box(22, 4, 0, 4, 10, 2, '#3a4150', top='#4a5266')
    sc.box(22, 4, 2, 1, 1, 6, '#ffc21a')
    sc.box(22, 4, 8, 4, 1, .8, '#ffc21a')
    sc.person(8, 11, '#c9cdd6')
    sc.person(16, 12, '#8b93a1')
    sc.cyl(4, 14, 1.2, .5, 1.6, '#ffc21a')
    return sc.render('Booth installation team on the show floor')


def s_dismantle():
    sc = svc_base(W=26, D=20, H=10)
    sc.box(-3, -3, -.3, 32, 26, .3, '#1c222c', top='#222a36', edge=False)
    sc.box(1, 1, 0, 8, 8, .6, '#8a6b45')
    for k in range(4):
        sc.box(2, 2 + k * .6, .6 + k * 0, 6, .5, 5.5 - k * .2, ('#f2f0ea', OR, '#cfd3da', '#f2f0ea')[k])
    sc.box(12, 1, 0, 9, 7, 5, '#22272f', top='#2f3541')
    sc.box(12, 1, 5, 9, 7, .8, '#ffc21a', edge=False)
    sc.box(12, 10, 0, 9, 7, 3.4, '#22272f', top='#2f3541')
    sc.box(4, 12, 0, 6, 5, 1.4, '#3a4150', top='#4a5266')
    sc.wire(3, 10, .3, 8, 8, 6, '#ffffff', .35, 1, '4 4')
    sc.person(6, 10.5, '#9aa1ad')
    return sc.render('Booth dismantling and crating')


def s_graphics():
    sc = svc_base(W=26, D=18, H=12)
    sc.box(-3, -3, -.3, 32, 24, .3, '#1c222c', top='#222a36', edge=False)
    sc.box(2, 2, 0, 16, .8, 10, '#f2f0ea')
    g = sc.lin([(0, OR), (.55, '#ff9b6a'), (1, '#ffd166')], 0, 0, 1, 1)
    sc.fy(2.6, 17.4, .8, 9.4, 2.81, 'url(#%s)' % g)
    sc.disc_y(9, 2.82, 5.4, 2.6, '#0e1013')
    sc.disc_y(9, 2.83, 5.4, 1.2, '#ffffff')
    sc.fy(3.4, 8.6, 1.4, 2, 2.82, '#0e1013', .9)
    sc.cyl(21, 5, 1.1, 0, 9, '#e9e6de')
    sc.cyl(24, 6.5, 1.1, 0, 9, '#c9c5bb')
    sc.cyl(22.6, 9, 1.1, 0, 9, '#f2f0ea')
    sc.box(4, 8, 0, 10, 6, .5, '#3a4150')
    for k, c in enumerate((OR, '#0e1013', '#2d6bff', '#ffc21a', '#f2f0ea')):
        sc.box(4.6 + k * 1.8, 9, .5, 1.5, 1.5, .15, c, edge=False)
    return sc.render('Large-format graphic production')


def s_lighting():
    sc = svc_base(W=24, D=20, H=15, glow='#ffb98f')
    sc.box(-3, -3, -.3, 30, 26, .3, '#1c222c', top='#222a36', edge=False)
    sc.frame(1, 1, 0, 20, 16, 12, '#d5d8de', .5)
    for i in range(4):
        x = 4 + i * 4.4
        sc.cyl(x, 9, .7, 10, 1.6, '#0e1013', top='#ffe9a6')
        sc.spot(x, 9, 10, 6 + i * 3.4, 12 + (i % 2) * 2, 2.4, '#ffe9a6', .3)
    sc.box(6, 12, 0, 3, 3, 2.4, '#f2f0ea', top='#ffffff')
    sc.box(12, 13, 0, 3, 3, 3.6, OR, top='#ff8a5c')
    sc.box(19, 3, 0, 2.5, 1.2, 3.2, '#3a4150')
    sc.box(19.4, 3.2, 1.6, 1.7, .3, 1, '#ffc21a', edge=False)
    return sc.render('Exhibition lighting rig and power distribution')


def s_pm():
    sc = svc_base(W=26, D=16, H=12)
    sc.box(-3, -3, -.3, 32, 22, .3, '#1c222c', top='#222a36', edge=False)
    sc.box(1, 1, 0, 22, .7, 11, '#f2f0ea')
    for i, (a, b, c) in enumerate(((0, 8, OR), (4, 10, '#0e1013'), (9, 15, OR), (13, 19, '#2d6bff'), (17, 21, '#0e1013'))):
        sc.fy(2 + a, 2 + b, 8.4 - i * 1.5, 9.2 - i * 1.5, 1.72, c)
    for i in range(5):
        sc.fy(2, 22, 1.3 + i * 1.5, 1.35 + i * 1.5, 1.72, '#0e1013', .18)
    sc.box(4, 6, 0, 8, 4, 2.6, '#22272f', top='#2f3541')
    for k in range(3):
        sc.box(5 + k * 2.4, 7, 2.6, 2, 2, .25, ('#f2f0ea', OR, '#ffc21a')[k], edge=False)
    sc.person(16, 8, '#c9cdd6')
    sc.person(19, 11, '#8b93a1')
    return sc.render('Exhibition project management timeline')


SERVICE_SCENES = [('service-01', s_design), ('service-02', s_construct), ('service-03', s_rental), ('service-04', s_install),
                  ('service-05', s_dismantle), ('service-06', s_graphics), ('service-07', s_lighting), ('service-08', s_pm)]


# ------------------------------------------------------------------ process (400x300)
def pr_base(W=14, D=12, H=8):
    sc = Scene(400, 300, W, D, H, fit=.7, cy=.6)
    sc.hall('#151a22', '#0b0e13', grid=.06)
    sc.box(-2, -2, -.3, W + 4, D + 4, .3, '#1c222c', top='#222a36', edge=False)
    return sc


def p1():
    sc = pr_base()
    sc.box(1, 1, 0, 11, 9, .2, '#eef2f7', top='#f5f8fc', edge=False)
    sc.wire(3, 3, .2, 5, 4, 3, '#0e1013', .9, 1.3)
    sc.ring(9, 7, .4, 2.2, .35, OR)
    a, b = sc.P(10.6, 8.6, .4), sc.P(13, 11, .4)
    sc.add((10, 8, .4, 13, 11, .5), '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="5" stroke-linecap="round"/>' % (a + b + (OR,)))
    return sc.render('Project discovery')


def p2():
    sc = pr_base()
    for i, c in enumerate((OR, '#f2f0ea', '#2d6bff')):
        sc.box(1 + i * 3.6, 3, 0, 3, .4, 4.6 - i * .5, c)
    sc.box(2, 6, 0, 8, 3, .5, '#3a4150', top='#4a5266')
    sc.cyl(11, 8, 1.2, 0, .3, '#ffc21a')
    sc.cyl(11, 8, .5, .3, 2, '#ffe066', top='#fff1c4')
    return sc.render('Concept and strategy')


def p3():
    sc = pr_base()
    sc.box(1, 1, 0, 11, 9, .2, '#1c2f52', top='#22396a', edge=False)
    sc.wire(2, 2, .2, 9, 7, 5, '#ffffff', .9, 1.3)
    sc.box(4, 4, .2, 3, 3, 2.4, OR, top='#ff8a5c')
    sc.wire(2, 2, 5.2, 9, 7, .01, '#7be0ff', .8, 1, '4 3')
    return sc.render('3D booth design')


def p4():
    sc = pr_base()
    sc.box(2, 2, 0, 9, 7, .5, '#f2f0ea', top='#ffffff')
    for k in range(3):
        sc.box(3, 3 + k * 1.8, .5, 5.5 - k, .3, .06, '#0e1013', edge=False)
    sc.box(2, 2, .5, 9, 7, .01, '#f2f0ea', edge=False)
    p = [sc.P(6.5, 6.2, .6), sc.P(7.4, 7.2, .6), sc.P(9.6, 4.4, .6), sc.P(9.1, 4, .6), sc.P(7.4, 6.2, .6), sc.P(6.9, 5.6, .6)]
    sc.add((6, 4, .6, 10, 7.5, .7), sc._poly(p, OR, OR, 2))
    return sc.render('Client approval')


def p5():
    sc = pr_base()
    sc.frame(1, 1, 0, 8, 8, 6, '#d5d8de', .5)
    sc.box(1.3, 1, .5, 3.6, .3, 4.5, OR, edge=False)
    for k in range(4):
        sc.box(10, 2 + k * .8, 0, 3.2, .7, 4.4, '#f2f0ea' if k % 2 else '#cfd3da', edge=False)
    sc.box(2, 9.5, 0, 5, 1.2, 1.2, '#8a6b45')
    return sc.render('Fabrication and production')


def p6():
    sc = pr_base()
    sc.cyl(2.5, 3, .9, 0, 6, '#e9e6de')
    sc.cyl(4.7, 4.5, .9, 0, 6, OR)
    sc.box(6.5, 2, 0, 5.5, .5, 6.2, '#f2f0ea')
    g = sc.lin([(0, OR), (1, '#ffd166')], 0, 0, 1, 1)
    sc.fy(6.8, 11.7, .6, 6, 2.51, 'url(#%s)' % g)
    sc.disc_y(9.2, 2.52, 3.4, 1.3, '#0e1013')
    sc.box(4, 8, 0, 8, 3, .5, '#3a4150')
    return sc.render('Graphics and branding production')


def p7():
    sc = pr_base(16, 10, 8)
    sc.box(1, 2, .8, 5, 5, 4.6, '#22272f', top='#2f3541')
    sc.box(1, 2, 5.4, 5, 5, .6, '#ffc21a', edge=False)
    sc.box(6.2, 2.5, .8, 4, 4.2, 2.6, '#f2f0ea')
    sc.box(10.2, 2.5, .8, 3, 4.2, 4.6, '#f2f0ea', top='#ffffff')
    sc.box(10.6, 2.2, .8, 2.2, .3, 1.6, OR, edge=False)
    for x in (2, 8, 11.6):
        sc.cyl(x, 8, 1, 0, .8, '#0b0c0e')
    return sc.render('Logistics and delivery')


def p8():
    sc = pr_base()
    sc.box(1, 1, 0, 10, .6, 6, '#f2f0ea')
    sc.box(1, 1, 3.6, 10, .7, 1.6, OR, edge=False)
    sc.frame(1, 4, 0, 9, 6, 5.5, '#d5d8de', .45)
    sc.person(6, 8, '#c9cdd6')
    sc.box(12, 3, 0, 1.6, 1.6, 6, '#ffc21a')
    return sc.render('On-site installation')


def p9():
    sc = pr_base()
    sc.box(1, 1, 0, 11, .6, 7, '#f2f0ea')
    sc.box(1, 1, 4.2, 11, .7, 1.8, OR, edge=False)
    counter(sc, 3, 5, 6, 1.6, '#f5f3ee', OR, 3, 0)
    for x, y, c in ((5, 8.5, '#9aa1ad'), (9, 7.5, '#c9cdd6'), (11, 5, '#7a808c')):
        sc.person(x, y, c)
    sc.cyl(2.2, 8.8, 1.2, 6.2, .01, '#2d6bff')
    px, py = sc.P(2.2, 8.8, 6.6)
    sc.add((1, 8, 6, 3, 10, 8), '<circle cx="%.1f" cy="%.1f" r="14" fill="#2d6bff"/><circle cx="%.1f" cy="%.1f" r="2" fill="#fff"/><circle cx="%.1f" cy="%.1f" r="2" fill="#fff"/><circle cx="%.1f" cy="%.1f" r="2" fill="#fff"/>' % (px, py, px - 6, py, px, py, px + 6, py))
    return sc.render('Event support')


def p10():
    sc = pr_base()
    for i in range(3):
        sc.box(1 + i * 3.8, 1, 0, 3.4, 2.6, 2.6, '#22272f', top='#2f3541')
        sc.box(1 + i * 3.8, 1, 2.6, 3.4, 2.6, .5, '#ffc21a', edge=False)
    sc.box(2, 5, 0, 8, 4, .8, '#8a6b45')
    for k in range(3):
        sc.box(2.4, 5.4 + k * 1, .8, 6.8 - k, .5, 3.4, ('#f2f0ea', OR, '#cfd3da')[k], edge=False)
    sc.wire(1, 4.5, 0, 10, 5.5, 4.6, '#ffffff', .3, 1, '3 4')
    return sc.render('Dismantling and return')


PROCESS_SCENES = [('process-%02d' % (i + 1), f) for i, f in enumerate((p1, p2, p3, p4, p5, p6, p7, p8, p9, p10))]


# ------------------------------------------------------------------ blog covers (800x500)
def bl_base(pal, W=26, D=20, H=12, glow='#ffffff', light=False):
    sc = Scene(800, 500, W, D, H, fit=.74, cy=.6)
    if light:
        sc.hall(pal[0], pal[1], grid=.06, gridc='#000')
    else:
        sc.hall(pal[0], pal[1], glow=glow)
    sc.box(-3, -3, -.3, W + 6, D + 6, .3, shade(pal[1], .08), top=shade(pal[1], .16), edge=False)
    return sc


def b1():
    sc = bl_base(('#181c24', '#090b0e'), glow='#ffb98f')
    sc.box(2, 2, 0, 20, .8, 9, '#f2f0ea')
    sc.box(2, 2, 6, 20, .9, 2.4, OR, edge=False)
    sc.box(9, 8, 0, 5, 5, 8, '#1b1f27')
    sc.box(8.6, 7.6, 8, 5.8, 5.8, .8, OR)
    sc.ring(11.5, 10.5, 12, 8, .4, '#fff')
    sc.spot(11.5, 10.5, 12, 11.5, 10.5, 6, '#ffb98f', .3)
    sc.person(18, 14, '#9aa1ad')
    return sc.render('Designing a high-impact trade show booth')


def b2():
    sc = bl_base(('#1a1e26', '#0a0c10'), W=30)
    sc.box(1, 3, 0, 12, .8, 9, '#f2f0ea')
    sc.box(1, 3, 0, .8, 8, 9, '#e6e3dc')
    sc.box(3, 8, 0, 6, 1.6, 3.2, OR, top='#ff8a5c')
    for i in range(3):
        sc.box(17 + i * 3.4, 3, 0, 3.2, .6, 7, ('#cfd3da', '#ffffff', '#cfd3da')[i])
    sc.box(18, 8, 0, 6, 1.6, 2.8, '#cfd3da', top='#ffffff')
    a = sc.P(14.5, 6, 3)
    sc.add((14, 5, 3, 15, 7, 4), '<text x="%.1f" y="%.1f" font-family="Arial" font-weight="800" font-size="34" fill="#fff" text-anchor="middle">VS</text>' % a)
    return sc.render('Custom booth versus rental stand')


def b3():
    sc = bl_base(('#151a22', '#0a0d12'), W=28)
    for i, h in enumerate((3, 5, 4, 7, 6, 9)):
        sc.box(2 + i * 3.6, 2, 0, 3, 3, h, (OR if i == 5 else '#3a4150'), top=(OR if i == 5 else '#4a5266'))
    for k, (x, n) in enumerate(((5, 5), (9, 7), (13, 3))):
        for j in range(n):
            sc.cyl(x, 12, 1.5, j * .55, .5, '#ffc21a', top='#ffe28a')
    sc.box(18, 9, 0, 7, 5, 4, '#f2f0ea', top='#ffffff')
    sc.box(18, 9, 4, 7, 5, .6, OR, edge=False)
    return sc.render('Exhibition stand costs and budget')


def b4():
    sc = bl_base(('#0f1a17', '#060a09'), glow='#5dffc2')
    for i, (x, y, r) in enumerate(((5, 5, 3), (13, 4, 2.2), (19, 9, 3.4), (8, 12, 2.4))):
        sc.cyl(x, y, r, 0, 3 + i * 1.6, ('#f2f0ea', '#5dffc2', '#f2f0ea', '#2d6bff')[i])
    sc.ring(13, 9, 11, 9, .4, '#5dffc2', inner='#fff')
    sc.plant(22, 15, leaf='#3f9d55')
    sc.plant(3, 15, leaf='#3f9d55')
    return sc.render('Trade show booth design trends')


def b5():
    sc = bl_base(('#1a1e26', '#0a0c10'))
    sc.box(2, 2, 0, 12, .6, 9, '#f2f0ea')
    for i in range(5):
        sc.fy(3, 3.9, 7.4 - i * 1.4, 7.9 - i * 1.4, 2.61, OR if i < 3 else '#cfd3da')
        sc.fy(4.4, 12.4 - i * .7, 7.5 - i * 1.4, 7.8 - i * 1.4, 2.61, '#0e1013', .55)
    for i in range(3):
        sc.box(16, 3 + i * 4, 0, 5, 3.4, 2.6 + (i % 2), '#22272f', top='#2f3541')
        sc.box(16, 3 + i * 4, 2.6 + (i % 2), 5, 3.4, .4, '#ffc21a', edge=False)
    sc.box(4, 9, 0, 8, 6, .4, '#3a4150')
    return sc.render('How to prepare for an exhibition')


def b6():
    sc = bl_base(('#101018', '#050508'), glow='#ffe9a6', W=28, D=20, H=14)
    sc.frame(1, 1, 0, 24, 16, 12, '#d5d8de', .45)
    for i in range(6):
        x = 4 + i * 3.6
        sc.cyl(x, 8, .7, 10, 1.6, '#0e1013', top='#ffe9a6')
        sc.spot(x, 8, 10, 4 + i * 3.4, 10 + (i % 2) * 3, 2.2, ('#ffe9a6', '#ff8ae0', '#7be0ff')[i % 3], .3)
    for x in (6, 12, 19):
        sc.box(x, 11, 0, 3, 3, 1.6 + (x % 3), '#f2f0ea', top='#ffffff')
    return sc.render('Exhibition lighting ideas')


def b7():
    sc = bl_base(('#20141a', '#0b0609'), glow='#ff8a7a')
    for i, (x, y, w, d, h, c) in enumerate(((3, 3, 4, 3, 8, '#3a4150'), (8, 5, 6, 4, 4, OR), (15, 3, 3, 3, 10, '#f2f0ea'), (6, 11, 8, 3, 3, '#5a5f66'), (17, 10, 5, 4, 5, '#c1121f'))):
        sc.box(x, y, 0, w, d, h, c)
    sc.wire(2, 2, 0, 22, 16, 11, '#ffffff', .25, 1, '3 4')
    a, b = sc.P(20, 5, 12), sc.P(24, 9, 12)
    sc.ov.append('<g stroke="#ff4d4d" stroke-width="10" stroke-linecap="round"><line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/><line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/></g>' % (a[0], a[1] - 30, b[0] + 60, b[1] + 30, b[0] + 60, a[1] - 30, a[0], b[1] + 30))
    return sc.render('Common booth design mistakes')


def b8():
    sc = bl_base(('#f4f1ea', '#d9d3c5'), W=20, D=20, H=10, light=True)
    sc.box(-3, -3, -.3, 26, 26, .3, '#e2dccd', top='#ece6d8', edge=False)
    sc.box(0, 0, 0, 12, 12, .4, '#cfc8b9', top='#dcd5c6')
    sc.box(.5, .5, .4, 10, .6, 8, '#ffffff')
    sc.box(.5, .5, .4, .6, 7, 8, '#f1efe9')
    sc.box(3, 5, .4, 4, 1.4, 3, OR, top='#ff8a5c')
    sc.box(8, 3, .4, 1.4, 1.4, 5.4, '#0e1013')
    sc.wire(-.5, -.5, 0, 13, 13, 9, '#0e1013', .35, 1, '4 4')
    sc.person(9, 9, '#7a808c')
    return sc.render('How to maximise small booth spaces')


BLOG_SCENES = [('blog-%02d' % (i + 1), f) for i, f in enumerate((b1, b2, b3, b4, b5, b6, b7, b8))]
