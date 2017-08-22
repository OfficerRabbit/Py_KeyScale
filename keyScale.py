
def note_check():
    while True:
        notes_list = ["A","B","C","D","E","F","G"]
        print("Select a musical note!")
        note_start_raw = input(": ")
        note_start = note_start_raw.upper()
    
        if note_start not in notes_list:
            print("Please enter a valid note!\n")
            continue
        else:
            return note_start


def key_check():
    print("Choose your key: [M]ajor or M[i]nor")
    key = input(": ")

    major_steps = [0, 2, 4, 5, 7, 9, 11]
    minor_steps = [0, 2, 3, 5, 7, 8, 10]

    if key.upper() == "M":
        key_string = "Major"
        key_steps = major_steps
        
    elif key.upper() == "I":
        key_string = "Minor"
        key_steps = minor_steps

    return key_string, key_steps


def note_convert(note):
    note_list = { "Ab":"G#"
                , "A#":"Bb"
                , "Bb":"A#"
                , "B#":"C"
                , "Cb":"F#"
                , "Gb":"G#"
                , "C#":"Db"
                , "D#":"Eb"
                , "G#":"Ab"
                }

    return(note_list[note])

    
def music_chords():
    notes_full_s = " A A# B C C# D D# E F F# G G#"

    note_start = note_check()
    key_string, key_steps = key_check()
    
    print(note_start, key_string)

    second_s, start_s, first_s = notes_full_s.partition(note_start)

    scale_s = start_s + first_s + second_s

    scale_list_s = scale_s.split()

    key_chords = []
    
    for i in range(0,7):
        note = key_steps[i]

        base_note_full = scale_list_s[note]
        base_note = base_note_full[:1]
        
        if any(base_note in s for s in key_chords):
            base_note_convert = note_convert(base_note_full)    
            key_chords.append(base_note_convert)
        else:
            key_chords.append(scale_list_s[note])
                    
    print(key_chords)


music_chords()
