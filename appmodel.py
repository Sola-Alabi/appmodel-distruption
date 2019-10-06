from pyautogui import press, typewrite, hotkey
import keyboard
import random
#randy contains a list of common song lyrics
randy = ["Move b***h get out the way", "drop it like its hot", "she got a big booty so I call her big booty", "do you ever feel, like a plastic bag",
            "I’m so 3008, you’re so 2000 and late", "Like a sprained ankle, boy, I ain’t nothin’ to play with", "Seven a.m., waking up in the morning Gotta be fresh, gotta go downstairs"
            'Hopped out the plane @ LAX with a dream and a cardigan', "Hey, I just met you and this is crazy", "But here's my number so call me, maybe?",
            "Rah, rah, ah, ah, ah, roma, roma, ma. Gaga, ooh, la, la... want your bad romance!", "And I was like baby, baby, baby oh like baby, baby, baby no",
            "There's vomit on his sweater already, mom's spaghetti", "My milkshake brings all the boys to the yard"]

while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        # if any vowel key is pressed
        if keyboard.is_pressed('a') or keyboard.is_pressed('e') or keyboard.is_pressed('i') or keyboard.is_pressed('o') or keyboard.is_pressed('u') or keyboard.is_pressed('s') or keyboard.is_pressed('y') or keyboard.is_pressed('r') or keyboard.is_pressed('backspace') :
            lyric = str(random.sample(randy,1)[0]) + "\n"
            typewrite(lyric)
    except:
        continue

keyboard.press()