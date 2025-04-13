import subprocess, json, os

def run_and_log(command, log_path):
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)
    with open(log_path, 'w') as f:
        json.dump({"output": result.stdout}, f, indent=2)
    input("\nPress Enter to return to the menu...")

while True:
    print("\nDocker Status")
    print("1) Run check")
    print("2) Edit config")
    print("0) Back")
    choice = input("Choose an option: ")

    if choice == "1":
        run_and_log(['docker', 'ps', '-a'], os.path.join("output", "docker_status.json"))
    elif choice == "2":
        path = input("Enter full path to config file to edit: ")
        subprocess.run(["nano", path])
        input("\nPress Enter to return to the menu...")
    elif choice == "0":
        break
    else:
        print("Invalid choice.")
        input("\nPress Enter to return to the menu...")
