# shooting game about a treasure lost in space
# https://www.youtube.com/user/shiffman

# variables
score = 0
ballSize = 40


def setup():
    size(800, 800)


def draw():
    # globals
    global score
    global ballSize

    # background
    background(255)
    beginning = color(1, 5, 32)
    ending = color(45, 135, 255)

    for i in range(801):
        stroke(lerpColor(beginning, ending, i/600.0))
        line(0, i, width, i)

    # title & score
    textSize(25)
    fill(255)
    text("Pew Pew!!!", 365, 50)
    text("score:", 645, 50)
    text(score, 730, 50)

    # stars
    strokeWeight(2)
    stroke(255)
    point(500, 400)
    point(300, 200)
    point(100, 300)
    point(600, 100)
    point(700, 250)
    point(430, 230)
    point(150, 60)
    point(360, 470)
    point(50, 140)
    point(230, 350)
    point(750, 430)
    point(150, 450)
    point(365, 320)
    point(600, 300)
    point(650, 550)

    # shooting stars
    stroke(500, 249, 238)
    # line()

    # player
    stroke(75)
    strokeWeight(5)
    noFill()
    ellipse(150, mouseY, ballSize, ballSize)