import os
import subprocess
import json





def add_all_to_group():
    ws_id =  json.loads(os.popen("hyprctl activewindow -j").read())["workspace"]["id"]
    ws = json.loads(os.popen("hyprctl workspaces -j").read())

    wc = 0


    for w in ws:
        if w["id"] == ws_id:
            wc = w["windows"]
            break



    os.system("hyprctl dispatch togglegroup")
    for i in range(wc):
        os.system("hyprctl dispatch cyclenext")
        os.system("hyprctl dispatch moveintogroup l")
        os.system("hyprctl dispatch moveintogroup d")
        os.system("hyprctl dispatch moveintogroup r")
        os.system("hyprctl dispatch moveintogroup t")
    os.system("hyprctl dispatch changegroupactive f")


if __name__ == "__main__":
    add_all_to_group()
