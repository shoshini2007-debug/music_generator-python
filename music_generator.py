from music21 import stream, note

song = stream.Stream()

song.append(note.Note("C4"))
song.append(note.Note("E4"))
song.append(note.Note("G4"))
song.append(note.Note("C5"))

song.write("midi", fp="generated_music.mid")

print("Music generated successfully!")
