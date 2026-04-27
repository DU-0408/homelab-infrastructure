# ⚙️ Automation Scripts

This directory contains scripts used for automation in the homelab.

---

## 📦 media-import.py

A Python CLI tool that:

- Downloads media from URL
- Extracts archives
- Renames files into Jellyfin format
- Organizes movies and TV shows
- Fixes permissions
- Refreshes Jellyfin

---

## 🔁 deploy.sh

Automates deployment pipeline:

- Pulls latest code
- Updates Kubernetes resources
- Restarts services

---

## 🌐 webhook.py

Handles incoming webhook events:

- Triggers deployment automatically on Git push
- Connects CI/CD pipeline to local infrastructure
- Set WEBHOOK_SECRET as environment variable
