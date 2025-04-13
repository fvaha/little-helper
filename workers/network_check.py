import subprocess, os, json

def log_and_run(name, command):
    print(f"Running: {' '.join(command)}")
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)
    with open(f"output/{name}.json", "w") as f:
        json.dump({"output": result.stdout}, f, indent=2)
    input("\nPress Enter to return to the menu...")

while True:
    print("\nNetwork Diagnostics")
    print("1) Show interfaces")
    print("2) Ping a target")
    print("0) Back")
    choice = input("Choose an option: ")

    if choice == "1":
        log_and_run("network_interfaces", ["ip", "a"])
    elif choice == "2":
        target = input("Enter target to ping: ")
        log_and_run("ping", ["ping", "-c", "4", target])
    elif choice == "0":
        break
    else:
        print("Invalid choice.")
        input("\nPress Enter to return to the menu...")
