//  Blinking hearts (from MakeCode tutorial)
//  Start instructions
//  End of instructions
//  Run the instructions on a loop without end
basic.forever(function on_forever() {
    //  Show a heart icon
    basic.showIcon(IconNames.Heart)
    //  Clear the screen
    basic.clearScreen()
    //  Wait x milliseconds
    basic.pause(500)
    //  Show a small heart icon
    basic.showIcon(IconNames.SmallHeart)
    //  Clear the screen
    basic.clearScreen()
    //  Wait x milliseconds
    basic.pause(500)
})
