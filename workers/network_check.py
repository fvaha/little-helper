import subprocess, json, os

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
    print("3) DNS resolution")
    print("4) Run traceroute")
    print("5) Edit config file")
    print("0) Back")
    choice = input("Choose an option: ")

    if choice == "1":
        log_and_run("network_interfaces", ["ip", "a"])
    elif choice == "2":
        target = input("Enter target to ping: ")
        log_and_run("ping", ["ping", "-c", "4", target])
    elif choice == "3":
        domain = input("Enter domain for DNS resolution: ")
        log_and_run("dns", ["dig", domain, "+short"])
    elif choice == "4":
        target = input("Enter target for traceroute: ")
        log_and_run("traceroute", ["traceroute", target])
    elif choice == "5":
        path = input("Enter path to config file: ")
        subprocess.run(["nano", path])
        input("\nPress Enter to return to the menu...")
    elif choice == "0":
        break
    else:
        print("Invalid choice.")
        input("\nPress Enter to return to the menu...")
