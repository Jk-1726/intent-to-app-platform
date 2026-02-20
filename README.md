# Intent-to-App Platform
### On-Demand Remote Application Execution via Containerized GUI Sessions

---

## Overview
This project explores a system where desktop applications can be launched dynamically and accessed through a web browser without installing them locally.

Instead of traditional remote desktops, each user session spawns an isolated containerized Linux environment running a specific application and streams its graphical output using noVNC.

The goal is to study session orchestration, lifecycle management, and lightweight application streaming — not to build a production VDI replacement.

---

## Core Idea
User clicks → API creates session → Container launches → GUI streamed in browser → Session destroyed after inactivity

This reduces:
- local hardware dependency
- environment conflicts
- installation overhead

---

## Architecture

**Components**

- FastAPI Orchestrator — handles session creation and tracking
- Docker Engine — spawns isolated application environments
- noVNC + X11 + WebSocket — streams GUI to browser
- Session Manager — maps user → container → port

Each session runs independently to simulate multi-tenant behavior.

---

## Current Capabilities
- Dynamically spawn GUI containers
- Access application from browser
- Per-session isolation
- Automatic port allocation
- Basic session tracking

---

## Known Limitations
This repository represents a systems prototype, not a finished platform.

- No authentication layer yet
- Not horizontally scalable
- Local-machine deployment
- Basic cleanup logic
- Resource limits not enforced

---

## Flow

1. User requests new session
2. Orchestrator checks active sessions
3. Docker container launches with app
4. noVNC exposes GUI over WebSocket
5. User interacts via browser
6. Session expires and container removed

---

## Run Locally

Requirements:
- Docker installed
- Python 3.10+
- Linux / WSL recommended
- pip install -r requirements.txt
- docker compose up --build
- uvicorn orchestrator.main:app --reload

## Open

http://localhost
:<assigned-port>/vnc.html


---

## Purpose
The project investigates treating applications as temporary compute resources instead of installed software.

Inspired by cloud gaming and ephemeral dev environments, implemented at small experimental scale to understand engineering challenges.

---

## Future Work
- Persistent sessions
- Multi-user routing
- Reverse proxy gateway
- Resource quota enforcement
- Cloud deployment

---

## Author
Jayakumar M
