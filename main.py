# Blinking hearts (from MakeCode tutorial)

# Start instructions
def on_forever():
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

# Run the instructions on a loop without end
basic.forever(on_forever)