from pygame import mixer

mixer.init()
mixer.music.load("music.wav")
mixer.music.play()

input("Press Enter to stop")