from pydub import AudioSegment
from pygame import mixer # Load the required library

class morse_logic():
    def __init__(self):
        self.CODE = {'A': '.-',    'B': '-...',   'C': '-.-.',
                    'D': '-..',    'E': '.',      'F': '..-.',
                    'G': '--.',    'H': '....',   'I': '..',
                    'J': '.---',   'K': '-.-',    'L': '.-..',
                    'M': '--',     'N': '-.',     'O': '---',
                    'P': '.--.',   'Q': '--.-',   'R': '.-.',
                    'S': '...',    'T': '-',      'U': '..-',
                    'V': '...-',   'W': '.--',    'X': '-..-',
                    'Y': '-.--',   'Z': '--..'   }

    def process(self, msg):

        morse_msg = ''
        pause = AudioSegment.silent(duration=500)
        morse_sound = pause

        for word in msg.split():
            for char in word:
                morse_msg += self.CODE[char.upper()] + '  '
                sound_name = "mp3_samples/" + char.lower() + ".mp3"
                print(sound_name)
                sound = AudioSegment.from_mp3(sound_name)

                # Concatenation is just adding
                morse_sound += sound

                # writing mp3 files is a one liner
                morse_sound.export("file.mp3", format="mp3")

            morse_msg += '    '
            morse_sound += pause
        return morse_msg
