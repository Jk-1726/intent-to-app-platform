# Intent-to-App Platform (Prototype)

Lightweight prototype that launches an isolated Linux GUI session on demand and streams it to a browser using container orchestration concepts.

This project demonstrates the **core execution flow of remote application streaming**, not a full cloud platform.

---

## What This Proves

Instead of installing applications locally, a user can request a session and interact with a remote GUI environment running inside a container.

Flow:

User → API request → container created → port assigned → browser connects → GUI streamed

This is the same fundamental model used by remote desktops, cloud IDEs, and application streaming platforms.

---

## Architecture Overview

FastAPI acts as the session orchestrator.

It:
- receives a session request
- starts a container
- maps a dynamic port
- exposes GUI via noVNC

Each request produces an isolated runtime environment.

---

## Execution Flow

1. Client sends session request
2. Backend creates container
3. Container exposes VNC server
4. noVNC bridges VNC → WebSocket
5. Browser renders GUI

---

## Demo (Actual Runtime)

### 1 — Session Creation
```md
![Create Session](demo/1_create_session.png)
```

### 2 — Browser Connection
```md
![Browser Access](demo/2_browser_access.png)
```

### 3 — Running GUI Application
```md
![Running App](demo/3_running_app.png)
```

---

## Running Locally

Install dependencies:

```bash
pip install fastapi uvicorn
```

Start server:

```bash
uvicorn main:app --reload
```

Open browser:

```
http://localhost:8000
```

Trigger session endpoint and connect using the returned port.

---

## Design Decisions

This is intentionally minimal.

No authentication  
No scaling  
No persistence

Because the goal is to demonstrate **session orchestration mechanics**, not build a full VDI platform.

---

## Future Work (Conceptual)

- multi-user session tracking
- container cleanup scheduler
- resource quotas
- cloud deployment
- intent-based app selection

---

## What To Look For

Focus on:
- lifecycle control
- port allocation logic
- isolation model
- streaming approach

This repository represents the foundation layer of a remote application execution platform.
