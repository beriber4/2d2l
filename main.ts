function on_button_pressed_a() {
    basic.showString("Hello, <name> !")
    input.onButtonPressed(Button.A, function on_button_pressed_a2() {
        
    })
}

