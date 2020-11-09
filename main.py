# Blinking hearts with buttons

# Instructions if button A is pressed

def a_loop():
    # Show a heart icon
    basic.show_icon(IconNames.HEART)

    # Clear the screen
    basic.clear_screen()

    # Wait x milliseconds
    basic.pause(500)

    # Show a small heart icon
    basic.show_icon(IconNames.SMALL_HEART)

    # Clear the screen
    basic.clear_screen()

    # Wait x milliseconds
    basic.pause(500)
    # End of instructions

def on_button_pressed_a():
    led.enable(True)
    basic.forever(a_loop)

# End of instructions 

# If the button pressed is A, follow those instructions
input.on_button_pressed(Button.A, on_button_pressed_a)

# Instructions if button B is pressed
def on_button_pressed_b():
    led.enable(False)
    def on_forever():
        pass
    basic.forever(on_forever)
# End of instructions

# If the button pressed is B, follow those instructions
input.on_button_pressed(Button.B, on_button_pressed_b)