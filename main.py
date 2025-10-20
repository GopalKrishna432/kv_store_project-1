import os

DATA_FILE = "data.db"
store = {}

# ---- Load old data if exists ----
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        for line in f:
            parts = line.strip().split(" ", 2)
            if len(parts) == 3 and parts[0] == "SET":
                _, key, value = parts
                store[key] = value

# ---- Command loop ----
while True:
    try:
        command = input().strip()
    except EOFError:
        break

    if not command:
        continue

    parts = command.split(" ", 2)
    cmd = parts[0].upper()

    if cmd == "EXIT":
        break

    elif cmd == "SET" and len(parts) == 3:
        key, value = parts[1], parts[2]
        store[key] = value
        with open(DATA_FILE, "a") as f:
            f.write(f"SET {key} {value}\n")

    elif cmd == "GET" and len(parts) == 2:
        key = parts[1]
        print(store.get(key, ""))

    else:
        print("")