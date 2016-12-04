import time

stage.set_background("grid")
sprite = codesters.Sprite("bike")
sprite.set_size(0.4)
sprite.go_to(-200, 0)

sprite.set_gravity_off()

click_counter = 0

def handle_space_key():
    global click_counter
    click_counter = click_counter + 1
    if click_counter % 2 != 0:
        sprite.set_x_speed(5)
    else:
        x = sprite.get_x()
        y = sprite.get_y()
        sprite.go_to(x, y)
    # add other actions...

stage.event_space_key(handle_space_key)

# Problem :
# Turn the bike's rotation at a 45 degree angle in a for loop
# Call the time delay or sleep() function every 1/10 second
def handle_flip():
 # Replace this code block with a for loop
    sprite.set_rotation(45)
    time.sleep(.4)
    sprite.set_rotation(90)
    time.sleep(.4)
    sprite.set_rotation(135)
    time.sleep(.4)
    sprite.set_rotation(180)
    time.sleep(.4)
    sprite.set_rotation(225)
    time.sleep(.4)
    sprite.set_rotation(270)
    time.sleep(.4)
    sprite.set_rotation(315)
    time.sleep(.4)
    sprite.set_rotation(360)
    
stage.event_key("up", handle_flip)





