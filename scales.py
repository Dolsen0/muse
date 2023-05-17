from intervals import INTERVAL_NAMES

CHROMATIC_SCALE = ["c", "c#", "d", "d#", "e", "f", "f#", "g", "g#", "a", "a#", "b"]

MAJOR_SCALE = [0, 2, 4, 5, 7, 9, 11, 12]

MINOR_SCALE = [0, 2, 3, 5, 7, 8, 10, 12]

DIMINISHED_SCALE = [0, 2, 3, 5, 6, 8, 9, 11, 12]

AUGMENTED_SCALE = [0, 2, 4, 6, 8, 10, 12]

def get_chromatic_scale(root):
    root_index = CHROMATIC_SCALE.index(root.lower())
    return f"\n {CHROMATIC_SCALE[root_index:] + CHROMATIC_SCALE[:root_index + 1]}"

def get_scale(root, scale_name):
    root_index = CHROMATIC_SCALE.index(root.lower())
    scale_list = globals().get(scale_name.upper() + "_SCALE")
    if scale_list is None:
        return None
    notes_str = " _ ".join(CHROMATIC_SCALE[(root_index + scale_list[i]) % 12] for i in range(len(scale_list)))
    intervals_str = " _ ".join(INTERVAL_NAMES[scale_list[i]] for i in range(len(scale_list)))
    return f"\n{root.capitalize()} {scale_name.capitalize()}: \n({notes_str}) \n({intervals_str})\n"

print(get_scale("E", "major"))
print(get_scale("E", "minor"))
print(get_scale("E", "diminished"))
print(get_scale("E", "augmented"))