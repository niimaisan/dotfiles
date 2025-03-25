from libqtile.config import Key, Group
from libqtile.lazy import lazy
from libqtile import hook
from .keys import mod, keys

groups = [
    Group("1", label="1"),
    Group("2", label="2"),
    Group("3", label="3"),
    Group("4", label="4"),
    Group("5", label="5"),
    Group("6", label="6"),
    Group("7", label="7"),
    Group("8", label="8"),
    Group("9", label="9"),
    Group("0", label="10"),
]

for i in groups:
    keys.extend(
        [
            Key([mod], i.name, lazy.group[i.name].toscreen()),  # Cambiar workspace
            Key(
                [mod, "shift"], i.name, lazy.window.togroup(i.name)
            ),  # Enviar ventana a workspace
        ]
    )


@hook.subscribe.client_new
def assign_app_group(client):
    d = {}

    d["1"] = []
    d["2"] = [
        "brave-browser",
    ]
    d["3"] = []
    d["4"] = []
    d["5"] = []
    d["6"] = []
    d["7"] = []
    d["8"] = [
        "qbittorrent",
    ]
    d["9"] = []
    d["0"] = [
        "telegram-desktop",
        "discord",
        "bitwarden",
    ]

    wm_class = client.window.get_wm_class()[0]

    for i in range(len(d)):
        if wm_class in list(d.values())[i]:
            group = list(d.keys())[i]
            client.togroup(group)
            client.group.cmd_toscreen(toggle=False)
