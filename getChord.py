from scales import CHROMATIC_SCALE
from intervals import INTERVAL_NAMES, INTERVALS

chord_types = {
    "major7": ["root", "M3", "P5", "M7"],
    "7": ["root", "M3", "P5", "m7"],
    "minor7": ["root", "m3", "P5", "m7"],
    "min6": ["root", "m3", "P5", "M6"],
    "dim7": ["root", "m3", "d5", "m7"],
    "aug7": ["root", "M3", "A4", "m7"]
}

def get_chromatic_scale(root):
    root_index = CHROMATIC_SCALE.index(root.lower())
    return CHROMATIC_SCALE[root_index:] + CHROMATIC_SCALE[:root_index + 1]

def get_chord(root, chord_type):
    root_index = CHROMATIC_SCALE.index(root.lower())
    interval_list = chord_types.get(chord_type)
    if not interval_list:
        return None
    intervals_str = " - ".join(INTERVAL_NAMES[INTERVALS[interval_list[i]]] for i in range(len(interval_list)))
    notes_str = " - ".join(CHROMATIC_SCALE[(root_index + INTERVALS[interval_list[i]]) % 12] for i in range(len(interval_list)))
    return f"\n{root.capitalize()} {chord_type.capitalize()}:\n({notes_str.capitalize()}) \n({intervals_str})"

print(get_chord("B", "major7"))