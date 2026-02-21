from fastapi import FastAPI
import subprocess

app = FastAPI()

IMAGE = "dorowu/ubuntu-desktop-lxde-vnc"
NAME = "testsession"
PORT = 6081


def container_running():
    result = subprocess.run(
        ["docker", "ps", "-q", "-f", f"name={NAME}"],
        capture_output=True,
        text=True
    )
    return result.stdout.strip() != ""


@app.get("/")
def home():
    return {"status": "backend running"}


@app.post("/start")
def start_desktop():

    if container_running():
        subprocess.run(["docker", "start", NAME])
        return {"url": f"http://localhost:{PORT}", "status": "reconnected"}

    subprocess.run([
        "docker", "run", "-d",
        "-p", f"{PORT}:80",
        "--name", NAME,
        IMAGE
    ])

    return {"url": f"http://localhost:{PORT}", "status": "created"}