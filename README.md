## 1. Classic Mode (CLI + Flask API)

This version runs directly on your server without Docker. Useful for minimal environments or direct access over SSH.

### How to Run

```bash
git clone https://github.com/fvaha/little-helper.git
cd little-helper
chmod +x launch.sh
./launch.sh
```

### Features
- Interactive CLI interface
- Python worker scripts for diagnostics
- Optional Flask API to expose results as JSON

---

## 2. Docker Compose Mode (Web Dashboard)

This version runs the API and a GUI dashboard inside containers.

### How to Run

```bash
git clone https://github.com/fvaha/little-helper.git
cd little-helper/compose
docker-compose up --build
```

Then open in your browser:

- Dashboard: http://localhost:8080
- API: http://localhost:5000
