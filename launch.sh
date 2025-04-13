#!/bin/bash
clear

echo "=== System Info Summary ==="
echo -n "CPU: "; lscpu | grep 'Model name' | sed 's/Model name:[ 	]*//'
echo -n "RAM: "; free -h | awk '/Mem:/ {print $2 " total, " $3 " used"}'
echo -n "Disk: "; df -h / | awk 'NR==2 {print $2 " total, " $3 " used"}'
echo -n "Main IP: "; hostname -I | awk '{print $1}'
echo "Interfaces: $(ip -o link show | awk -F': ' '{print $2}' | paste -sd ',' -)"
echo "============================"

while true; do
echo ""
echo "Select a category:"
echo "1) Network diagnostics"
echo "2) Database check"
echo "3) Docker status"
echo "4) Kubernetes info"
echo "5) Pipelines (Redis/Kafka)"
echo "6) Start Flask API"
echo "00) Install all requirements"
echo "0) Exit"
read -p "Enter choice: " choice

case $choice in
  1) python3 workers/network_check.py ;;
  2) python3 workers/db_check.py ;;
  3) python3 workers/docker_check.py ;;
  4) python3 workers/k8s_check.py ;;
  5) python3 workers/pipelines_check.py ;;
  6) source venv/bin/activate && python3 api/app.py && deactivate ;;
  00)
    echo "Creating output directory..."
    mkdir -p output

    echo "Creating virtual environment..."
    python3 -m venv venv

    echo "Activating and installing Python packages..."
    source venv/bin/activate
    pip install --upgrade pip
    pip install -r api/requirements.txt
    deactivate

    echo "Installing system tools..."
    sudo apt update
    sudo apt install -y dnsutils traceroute net-tools iputils-ping

    echo "All set. You can now run the diagnostics."
    ;;
  0) break ;;
  *) echo "Invalid choice" ;;
esac
done
