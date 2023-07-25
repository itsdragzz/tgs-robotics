from PiicoDev_Buzzer import PiicoDev_Buzzer
from PiicoDev_Unified import sleep_ms

notes = {
    "C4":262,
    "Db4":277,
    "D4":294,
    "Eb4":311,
    "E4":330,
    "F4":349,
    "Gb4":370,
    "G4":392,
    "Ab4":415,
    "A4":440,
    "Bb4":466,
    "B4":494,
    "C5":523,
    "Db5":554,
    "D5":587,
    "Eb5":622,
    "E5":659,
    "F5":698,
    "Gb5":740,
    "G5":784,
    "Ab5":831,
    "A5":880,
    "Bb5":932,
    "B5":988,
    "C6":1047,
    'rest':0
}

#Fur Elise
melody = [['E5',    500],
          ['Eb5',    500],
          ['E5',   500],
          ['Eb5', 500],
          ['E5',    500],
          ['B4',    500],
          ['D5',   500],
          ['C5', 500],
          ['A4',    500]
          ]

buzz = PiicoDev_Buzzer(volume=2,bus=6)

for x in melody:
    noteName = x[0]
    duration = x[1]
    buzz.tone(notes[noteName],duration)
    sleep_ms(duration)