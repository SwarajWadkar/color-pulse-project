# 🎨 Color Pulse App

A visually elegant and responsive web application designed to demonstrate **Canary Deployments** using **FastAPI**, **Docker**, and **Kubernetes**.

---

## 🚀 Features

- Smooth color pulsing animation
- Built using FastAPI and Tailwind CSS
- Containerized with Docker
- Deployable with Kubernetes (ideal for Canary rollout demos)

---

## 🛠️ Tech Stack

- **Frontend**: HTML, Tailwind CSS
- **Backend**: FastAPI (Python)
- **Containerization**: Docker
- **Orchestration**: Kubernetes

---

## 🧪 Run Locally

### Docker

docker pull swarajwadkar/color-pulse-app:latest
docker run -d -p 8000:8000 swarajwadkar/color-pulse-app
Open your browser and visit: http://localhost:8000

## Deploy with Kubernetes
bash
Copy
Edit
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
minikube service color-pulse-service


## Project Structure

color-pulse-project/
├── app
│   ├── v1
│   │   ├── Dockerfile
│   │   └── index.html
│   └── v2
│       ├── Dockerfile
│       └── index.html
└── deploy
    ├── deployment-canary.yaml
    ├── deployment-stable.yaml
    └── service.yaml




