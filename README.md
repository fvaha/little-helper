## Classic Version (CLI + API)

Use this version if you want to run everything locally without Docker.

### How to Run
```bash
git clone https://github.com/fvaha/little-helper.git
cd little-helper/classic
chmod +x launch.sh
./launch.sh
```

## Compose Version (Docker + Web Dashboard)

Use this version if you want an easy GUI and complete containerized setup.

### How to Run
```bash
git clone https://github.com/fvaha/little-helper.git
cd little-helper/compose
docker-compose up --build
```

- Open the dashboard at: http://localhost:8080
- API is available at: http://localhost:5000
