from libqtile.config import Key
from libqtile.lazy import lazy

mod = "mod4"

keys = [
    Key(key[0], key[1], *key[2:])
    for key in [
        # Cambiar entre ventana en stack panel actual
        ([mod], "h", lazy.layout.left()),
        ([mod], "j", lazy.layout.down()),
        ([mod], "k", lazy.layout.up()),
        ([mod], "l", lazy.layout.right()),
        # Mover ventanas entre columnas o filas en el stck panel actual
        ([mod, "shift"], "h", lazy.layout.shuffle_left()),
        ([mod, "shift"], "j", lazy.layout.shuffle_down()),
        ([mod, "shift"], "k", lazy.layout.shuffle_up()),
        ([mod, "shift"], "l", lazy.layout.shuffle_right()),
        # Ventana flotante
        ([mod, "shift"], "f", lazy.window.toggle_floating()),
        # Cambiar entre layouts
        ([mod], "Tab", lazy.next_layout()),
        ([mod, "shift"], "Tab", lazy.prev_layout()),
        # Matar ventana
        ([mod], "w", lazy.window.kill()),
        # Reiniciar Qtile
        ([mod, "control"], "r", lazy.restart()),
        # Cerrar Qtile
        ([mod, "control"], "q", lazy.shutdown()),
        # Lanzador de aplicaciones
        ([mod], "r", lazy.spawncmd()),
        # Lanzador de aplicaciones
        (
            [mod],
            "m",
            lazy.spawn(
                "rofi -show drun -show-icons -config /home/adroc/.config/rofi/dracula.rasi"
            ),
        ),
        # Ventanas abiertas
        ([mod, "shift"], "m", lazy.spawn("rofi -show")),
        # Navegador
        ([mod], "b", lazy.spawn("brave-browser")),
        # Explorador de archivos
        ([mod], "e", lazy.spawn("kitty ranger")),
        # Terminal
        ([mod], "Return", lazy.spawn("kitty zsh")),
        # Screenshot
        ([], "Print", lazy.spawn("flameshot gui")),
        # Multimedia
        (
            [],
            "XF86AudioLowerVolume",
            lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%"),
        ),
        (
            [],
            "XF86AudioRaiseVolume",
            lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%"),
        ),
        ([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
    ]
]
