import os
import subprocess
import json

from allGroup import add_all_to_group

# os.system("telegram-desktop")
apps_by_workspace = {
    "1":[
    # "telegram-desktop",
    "discord",
    "vk",
    ],
    "2":[""],
    "3":["firefox"],
    "4":["clickup"]
}

grouped_workspaces = ["1","4"]
default_works3pace = 1

for w in apps_by_workspace:
    os.system(f"hyprctl dispatch workspace {w}")
    for a in apps_by_workspace[w]:
        os.system(a)
    
for g in grouped_workspaces:
    os.system(f"hyprctl dispatch workspace {g}")
    add_all_to_group()

os.system(f"hyprctl dispatch workspace {default_workspace}")