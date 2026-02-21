# Intent-to-App Platform (Prototype)
Remote GUI Session Orchestration over HTTP

Author: Jayakumar M

---

## What This Repository Is

A minimal runtime that launches an isolated Linux graphical environment on demand and exposes it inside a web browser.

The backend acts as a session orchestrator:
it receives a request → creates an execution environment → publishes a connection endpoint → user interacts with remote software.

This demonstrates the core mechanism used by remote desktops, browser IDEs and application streaming systems.

This is a prototype of the orchestration layer, not a full cloud service.

---

## Problem It Demonstrates

Local installation couples software to hardware.

This system decouples them:

client device → only displays pixels  
server → executes the application

The browser becomes a terminal for a remote operating system.

---

## Runtime Flow

1) User calls session endpoint  
2) Backend prepares runtime instance  
3) Instance exposes display via VNC  
4) noVNC bridges VNC → WebSocket  
5) Browser renders GUI stream

Interaction latency comes from network, not compute availability.

---

## Components

Orchestrator  
Handles session lifecycle and endpoint exposure

Runtime Environment  
Temporary graphical Linux session

Streaming Bridge  
Converts framebuffer updates into browser-readable stream

Client  
Standard web browser, no installation required

---

## Session Lifecycle

create → connect → interact → dispose

Sessions are intentionally ephemeral.  
The design models disposable compute rather than persistent machines.

---

## Demo Evidence

Session creation:

![image alt](https://github.com/Jk-1726/intent-to-app-platform/blob/fe9316d9614ad951f3da1724133ad59665bbb18b/session-created.png.png)

Browser connection:

![Browser Access](https://github.com/Jk-1726/intent-to-app-platform/blob/9a2812d4125355617856d2679e24e0546339adbb/session-before.png.png)


Remote GUI interaction:

![Running App]()


---

## Running

Install dependencies

```bash
pip install fastapi uvicorn
```

Start service

```bash
uvicorn main:app --reload
```

Open

http://localhost:8000

Call the session endpoint and connect using returned address.

---

## Design Intent

Focus:
runtime provisioning
process isolation
remote rendering
stateless access

Excluded deliberately:
authentication
persistence
multi-node scheduling
production security

The objective is to prove execution redirection, not build a hosted product.

---

## Limitations

Single host execution  
No resource quotas  
Manual cleanup  
No failure recovery  
Not safe for untrusted users

---

## Possible Extensions

container scheduling
session TTL cleanup
GPU forwarding
application presets
cloud worker nodes

---

## Why It Matters

The machine running software no longer needs to be the machine the user owns.

This is the foundation behind remote development environments and zero-install applications.

---

## Author

Jayakumar M
Computer Science Engineering
Focus: Systems, Runtime Infrastructure, Cloud Execution Models
