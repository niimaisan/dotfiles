from libqtile import widget
from .theme import colors


def base(fg="text", bg="dark"):
    return {"foreground": colors[fg], "background": colors[bg]}


def separator():
    return widget.Sep(**base(), linewidth=0, padding=3)


def workspaces():
    return [
        separator(),
        widget.GroupBox(
            **base(fg="light"),
            font="FiraCode Nerd Font",
            fontsize=12,
            margin_y=3,
            margin_x=0,
            padding_y=5,
            padding_x=3,
            borderwidth=1,
            active=colors["active"],
            inactive=colors["inactive"],
            rounded=True,
            highlight_method="block",
            urgent_alert_method="block",
            urgent_border=colors["urgent"],
            this_current_screen_border=colors["focus"],
            this_screen_border=colors["grey"],
            other_current_screen_border=colors["dark"],
            other_screen_border=colors["dark"],
            disable_drag=True,
        ),
        separator(),
        widget.WindowName(**base(fg="focus"), fontsize=10, padding=3),
        separator(),
    ]


primary_widgets = [
    *workspaces(),
    widget.Maildir(
        **base(fg="light"),
        maildir_path="~/.mail",
        sub_folders=[
            {"label": "GMX", "path": "inbox"},
            {"label": "GMAIL", "path": "gmail"},
        ],
        hide_when_empty=True,
        update_interval=60,
    ),
    separator(),
    widget.CPU(**base(fg="light"), format="{freq_current}GHz {load_percent}%"),
    widget.Memory(**base(fg="light")),
    separator(),
    widget.OpenWeather(**base(fg="light"), cityid="3111158", language="es"),
    separator(),
    widget.Systray(**base(fg="light"), padding=1),
    separator(),
    widget.Clock(**base(fg="light"), format="%d/%m/%Y %H:%M "),
]

widget_defaults = {"font": "FiraCode Nerd Font", "fontsize": 10, "padding": 1}

extension_defaults = widget_defaults.copy()
