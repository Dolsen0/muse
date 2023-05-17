chromatic = ["c", "c#", "d", "d#", "e", "f", "f#", "g", "g#", "a", "a#", "b"]

intervals = {
    "root": 0,
    "m2": 1,
    "M2": 2,
    "m3": 3,
    "M3": 4,
    "P4": 5,
    "A4": 6,
    "d5": 6,
    "P5": 7,
    "m6": 8,
    "M6": 9,
    "m7": 10,
    "M7": 11,
    "P8": 12
}

interval_names = {
    0: "Root",
    1: "m2",
    2: "M2",
    3: "m3",
    4: "M3",
    5: "P4",
    6: "A4/d5",
    7: "P5",
    8: "m6",
    9: "M6",
    10: "m7",
    11: "M7",
    12: "P8"
}

chord_types = {
    "major7": ["root", "M3", "P5", "M7"],
    "7": ["root", "M3", "P5", "m7"],
    "minor7": ["root", "m3", "P5", "m7"],
    "min6": ["root", "m3", "P5", "M6"],
    "dim7": ["root", "m3", "d5", "m7"],
    "aug7": ["root", "M3", "A4", "m7"]
}

def get_chromatic_scale(root):
    root_index = chromatic.index(root.lower())
    return chromatic[root_index:] + chromatic[:root_index + 1]

def get_chord(root, chord_type):
    root_index = chromatic.index(root.lower())
    interval_list = chord_types.get(chord_type)
    if not interval_list:
        return None
    intervals_str = "-".join(interval_names[intervals[interval_list[i]]] for i in range(len(interval_list)))
    notes_str = "-".join(chromatic[(root_index + intervals[interval_list[i]]) % 12] for i in range(len(interval_list)))
    return f"{root.capitalize()} {chord_type.capitalize()}: {notes_str} ({intervals_str})"

print(get_chord("B", "major7"))