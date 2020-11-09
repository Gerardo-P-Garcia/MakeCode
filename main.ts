//  Blinking hearts with buttons
//  Instructions if button A is pressed
//  End of instructions
//  End of instructions 
//  If the button pressed is A, follow those instructions
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    led.enable(true)
    basic.forever(function a_loop() {
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
})
//  Instructions if button B is pressed
//  End of instructions
//  If the button pressed is B, follow those instructions
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    led.enable(false)
    basic.forever(function on_forever() {
        
    })
})
