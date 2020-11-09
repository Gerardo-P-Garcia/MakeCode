# Smiley buttons (from MakeCode tutorial)

# Instructions if button A is pressed
def on_button_pressed_a():
    # Show a happy icon
    basic.show_icon(IconNames.HAPPY)
# End of instructions 

# If the button pressed is A, follow those instructions
input.on_button_pressed(Button.A, on_button_pressed_a)

# Instructions if button B is pressed
def on_button_pressed_b():
    # Show a sad icon
    basic.show_icon(IconNames.SAD)
# End of instructions

# If the button pressed is B, follow those instructions
input.on_button_pressed(Button.B, on_button_pressed_b)

# Instructions of both A and B are pressed together (a separate button in virtual version)
def on_button_pressed_ab():
    # Show a silly icon
    basic.show_icon(IconNames.SILLY)
    # Show a surprised icon
    basic.show_icon(IconNames.SURPRISED)
# End of instructions 

# If the buttons A and B are pressed together, follow those instructions
input.on_button_pressed(Button.AB, on_button_pressed_ab)