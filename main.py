def on_button_pressed_a():
    basic.show_string("Hello, <name> !")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_string("Goodbye, <name> !")
input.on_button_pressed(Button.b, on_button_pressed_b)

def on_gesture_shake():
    music.play(music.string_playable("C5 C5 C5 C5 C5 C5 C5 C ", 120),
        music.PlaybackMode.UNTIL_DONE)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)