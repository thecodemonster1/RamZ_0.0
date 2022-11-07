from pocketsphinx import LiveSpeech
for phrase in LiveSpeech():
    print(phrase)

# from pocketsphinx import AudioFile
#
# for phrase in AudioFile("goforward.wav"):
#     print(phrase)  # => "go forward ten meters"
