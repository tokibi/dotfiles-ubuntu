import re
from xkeysnail.transform import *

define_modmap({
    Key.LEFT_ALT: Key.LEFT_CTRL,
    Key.RIGHT_ALT: Key.LEFT_CTRL,
})

# Oneshot modifier
define_multipurpose_modmap({
    Key.SPACE:    [Key.SPACE,    Key.LEFT_SHIFT],
    Key.CAPSLOCK: [Key.ESC,      Key.LEFT_ALT],
    Key.MUHENKAN: [Key.MUHENKAN, Key.LEFT_CTRL],
    Key.HENKAN:   [Key.HENKAN,   Key.LEFT_CTRL],
})

# [Global keymap]
define_keymap(None, {
    # Vim lie key bindings
    K("M-h"): K("left"),
    K("M-l"): K("right"),
    K("M-k"): K("up"),
    K("M-j"): K("down"),
    K("Shift-M-h"): K("Shift-left"),
    K("Shift-M-l"): K("Shift-right"),
    K("Shift-M-k"): K("Shift-up"),
    K("Shift-M-j"): K("Shift-down"),

    # Globalize Home, End shortcuts
    K("M-a"): K("home"),
    K("M-e"): K("end"),
    K("Shift-M-a"): K("Shift-home"),
    K("Shift-M-e"): K("Shift-end"),

    # Exchange underscore and backslash
    K("RO"): K("Shift-RO"),
    K("Shift-RO"): K("RO"),

    # Delete
    K("M-d"): K("delete"),
}, "cursor move")
