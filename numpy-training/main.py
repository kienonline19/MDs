import warnings

warnings.filterwarnings(
    "ignore",
    message=r"pkg_resources is deprecated as an API.*",
    category=UserWarning,
    module=r"vpython"
)

from vpython import sphere, box, vector, color, rate



ground = box(
    pos=vector(0, -0.1, 0),
    size=vector(6, 0.2, 4),
    color=color.green
)

ball = sphere(
    pos=vector(0, 5, 0),
    radius=0.2,
    color=color.red,
    make_trail=True 
)

g = 9.8
t = 0
dt = 0.002
h = 5

while ball.pos.y > ball.radius:
    rate(100)
    t += dt
    ball.pos.y = max(ball.radius, h - 0.5*g*t**2)

while True:
    rate(30)