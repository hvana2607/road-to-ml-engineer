# What your program should do:
import json
marks = {"Alice": 95, "Bob": 88, "Charlie": 72}

# 1. Save to "marks.json"
with open("marks.json","w") as f:
    json.dump(marks,f,indent=4)

# 2. Load from "marks.json"
with open("marks.json","r") as f:
    s = json.load(f)
# 3. Print: "Alice: 95 — Pass"
for n,m in s.items():
    if m>=75:
        print(f"{n}: {m} — Pass")
    else: 
        print(f"{n}: {m} — Fail")
# Bonus: mark students Pass/Fail (pass = 75+)


#----------------------------------------------------------------------------------------------

# Config to save:
config = {
    "app_name": "MyApp",
    "version": "1.0",
    "debug": False,
    "max_users": 100
}
# Bonus: update just "debug" to True and re-save

with open("config.json","w") as f:
    json.dump(config,f,indent=4)

with open("config.json","r") as f:
    config = json.load(f)

config["debug"] = True

print(config)

with open("config.json","w") as f:
    json.dump(config,f,indent=4)

#----------------------------------------------------------------------------------------------

from datetime import datetime

# Each log line should look like:
# [2026-06-07 10:23:45] INFO: App started
# [2026-06-07 10:24:01] ERROR: File not found

# Functions to build:
# log(level, message) — appends to log.txt
# show_last(n) — prints last n lines

def log(level, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("log.txt","a") as f:
        f.write(f"[{timestamp}] {level}: {message}\n")
    

def show_last(n):
    with open("log.txt","r") as f:
        lines = f.readlines()
    last_n = lines[-n:]

    for line in last_n:
        print(line.strip())

log("INFO","App started")
log("ERROR", "File not found")

show_last(2)