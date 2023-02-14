fern = Actor('fern')
fern.pos = 100, 56

WIDTH = 300
HEIGHT = 300

WIDTH = 500
HEIGHT = fern.height + 20

def draw():
    screen.clear()
    screen.fill((128, 0, 0))
    fern.draw()
fern.topright = 0, 10

def update():
    fern.left += 2
    if fern.left > WIDTH:
        fern.right = 0

def set_fern_hurt():
    fern.image = 'fern_hurt'
    sounds.eep.play()
    clock.schedule_unique(set_fern_normal, 1.0)

def set_fern_normal():
    fern.image = 'fern'

def on_mouse_down(pos):
    if fern.collidepoint(pos):
        set_fern_hurt()
        print("Ahh!")
    else:
        print("Whats that clicking noise?")



