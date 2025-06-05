import sys

from config import *
from amount_btn import AmountBtn
from rgb_slider import RGBSlider
from lights import Lights
from togle import TogleBtn
from algs import A, B


screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# UI Element Positions
slider = RGBSlider((80, 400), (600, 200), FONT)
amount_btn = AmountBtn((650, 50), (40, 25), 'Amount', FONT)
lights = Lights()
togle_btn = TogleBtn((650, 120), (60, 25), 1)

a = A(30); b  = B(30)
algs = [a, b]


while True:
    screen.fill((240, 240, 240))

    lights.update(algs[togle_btn.value].get_seq(), algs[togle_btn.value].get_col())

    # Draw UI
    slider.draw(screen)
    amount_btn .draw(screen)
    lights.draw(screen, amount_btn.get_value())
    togle_btn.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        slider.handle_input(event, pygame.mouse.get_pos())
        amount_btn .handle_event(event)
        togle_btn.update(event)

        a.color = slider.color

    pygame.display.flip()
    clock.tick(10)
