#!/bin/bash
clear

echo "System Info:"
python3 workers/network_check.py

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
  6) cd api && python3 app.py && cd .. ;;
  00)
    echo "Creating output directory..."
    mkdir -p output

    echo "Installing Python packages..."
    pip install -r api/requirements.txt

    echo "Installing system tools..."
    sudo apt update
    sudo apt install -y dnsutils traceroute net-tools iputils-ping

    echo "All set. You can now run the diagnostics."
    ;;
  0) break ;;
  *) echo "Invalid choice" ;;
esac
done
