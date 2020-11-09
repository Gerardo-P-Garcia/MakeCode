//  Smiley buttons (from MakeCode tutorial)
//  Instructions if button A is pressed
//  End of instructions 
//  If the button pressed is A, follow those instructions
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    //  Show a happy icon
    basic.showIcon(IconNames.Happy)
})
//  Instructions if button B is pressed
//  End of instructions
//  If the button pressed is B, follow those instructions
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    //  Show a sad icon
    basic.showIcon(IconNames.Sad)
})
//  Instructions of both A and B are pressed together (a separate button in virtual version)
//  End of instructions 
//  If the buttons A and B are pressed together, follow those instructions
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    //  Show a silly icon
    basic.showIcon(IconNames.Silly)
    //  Show a surprised icon
    basic.showIcon(IconNames.Surprised)
})
