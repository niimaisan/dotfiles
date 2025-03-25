from libqtile.config import Screen
from libqtile import bar

# from libqtile.log_utils import logger
from .widgets import primary_widgets
# import subprocess


def status_bar(widgets):
    return bar.Bar(widgets, 24, opacity=0.92)


screens = [Screen(top=status_bar(primary_widgets))]
# xrandr = "xrandr | grep -w 'connected' | cut -d ' ' -f 2 | ec -l"
# command = subprocess.run(
# xrandr,
# shell = True,
#     stdout = subprocess.PIPE,
#     stderr = subprocess.PIPE,
# )
#
# if command.returncode != 0:
#     error = command.stderr.decode("UTF-8")
#     logger.error(f"Error contando monitores usando {xrandr}:\n{error}")
#     connected_monitors = 1
#
# else:
# #    connected_monitors = int(command.stdout.decode("UTF-8"))
