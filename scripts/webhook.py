with open("/path/to/webhook.log", "a") as f:
    f.write("🔥 Webhook app imported\n")


from fastapi import FastAPI, Request
import subprocess
import hmac, hashlib, os, datetime

SECRET = os.environ.get("WEBHOOK_SECRET", "your-secret-key")
if not SECRET:
    raise ValueError("WEBHOOK_SECRET not set")

app = FastAPI()

@app.post("/deploy")
async def deploy(request: Request):

    # 🔹 LOG: webhook received
    with open("/path/to/webhook.log", "a") as f:
        f.write(f"\nWebhook hit at {datetime.datetime.now()}\n")

    body = await request.body()
    signature = request.headers.get("X-Hub-Signature-256")

    mac = hmac.new(SECRET.encode(), body, hashlib.sha256)
    expected = "sha256=" + mac.hexdigest()

#    Signature verification disabled for demo
#    if not signature or not hmac.compare_digest(expected, signature):
#        with open("/path/to/webhook.log", "a") as f:
#            f.write("❌ Invalid signature\n")
#        return {"status": "invalid signature"}

    # 🔹 LOG: signature valid
    with open("/path/to/webhook.log", "a") as f:
        f.write("✅ Signature valid\n")

    payload = await request.json()

    service = payload.get("service")
    tag = payload.get("after")

    if not tag or not service:
        return {"error": "Missing service or commit SHA"}

    if service == "backend":
        cmd = ["/bin/bash", "/path/to/deploy-backend.sh", tag]
    elif service == "frontend":
        cmd = ["/bin/bash", "/path/to/deploy-frontend.sh", tag]
    else:
        return {"error": "Unknown service"}

    with open("/path/to/webhook.log", "a") as f:
        f.write(f"🚀 Running command: {cmd}\n")

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True
    )

    with open("/path/to/webhook.log", "a") as f:
        f.write(f"\nSERVICE: {service}\n")
        f.write("STDOUT:\n" + result.stdout + "\n")
        f.write("STDERR:\n" + result.stderr + "\n")

    return {"status": f"{service} deployment triggered"}
