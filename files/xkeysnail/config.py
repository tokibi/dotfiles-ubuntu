import re
from xkeysnail.transform import *


# Oneshot modifier
define_multipurpose_modmap({
    Key.SPACE: [Key.SPACE, Key.LEFT_SHIFT],
    Key.CAPSLOCK: [Key.ESC, Key.LEFT_CTRL],
})

# [Global keymap]
define_keymap(None, {
    # Vim lie key bindings
    K("C-h"): K("left"),
    K("C-l"): K("right"),
    K("C-k"): K("up"),
    K("C-j"): K("down"),
    K("Shift-C-h"): K("Shift-left"),
    K("Shift-C-l"): K("Shift-right"),
    K("Shift-C-k"): K("Shift-up"),
    K("Shift-C-j"): K("Shift-down"),

    # Globalize Home, End shortcuts
    K("C-a"): K("home"),
    K("C-e"): K("end"),
    K("Shift-C-a"): K("Shift-home"),
    K("Shift-C-e"): K("Shift-end"),

    # Select all
    K("M-a"): K("C-a"),

    # Exchange underscore and backslash
    K("RO"): K("Shift-RO"),
    K("Shift-RO"): K("RO"),

    # Delete
    K("C-d"): K("delete"),
}, "cursor move")

define_keymap(re.compile("Code"), {
    K("M-d"): K("C-d"),
}, "Visutal Studio Code")
