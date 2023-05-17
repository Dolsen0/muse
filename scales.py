chromatic = ["c", "c#", "d", "d#", "e", "f", "f#", "g", "g#", "a", "a#", "b", "c"]

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

major = [0, 2, 4, 5, 7, 9, 11, 12]

minor = [0, 2, 3, 5, 7, 8, 10, 12]

diminished = [0, 2, 3, 5, 6, 8, 9, 11, 12]

augmented = [0, 2, 4, 6, 8, 10, 12]

def get_chromatic_scale(root):
    root_index = chromatic.index(root.lower())
    return f"\n {chromatic[root_index:] + chromatic[:root_index + 1]}"

def get_scale(root, scale_name):
    root_index = chromatic.index(root.lower())
    scale_list = globals().get(scale_name.lower())
    if scale_list is None:
        return None
    intervals_str = "-".join(interval_names[scale_list[i]] for i in range(len(scale_list)))
    notes_str = "-".join(chromatic[(root_index + scale_list[i]) % 12] for i in range(len(scale_list)))
    return f"\n{root.capitalize()} {scale_name.capitalize()}: {notes_str} ({intervals_str})"

print(get_scale("E", "major"))

print(get_scale("E", "minor"))

print(get_chromatic_scale("E"))