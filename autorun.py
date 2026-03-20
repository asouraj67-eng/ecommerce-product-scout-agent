#!/usr/bin/env python3
"""
autorun.py — Write formData config to .secrets/scout-config.json
Runs once on first activation if formData is provided by the platform.
"""
import json
import os
import sys

def main():
    raw = os.environ.get("OPENCLAW_FORM_DATA") or (sys.argv[1] if len(sys.argv) > 1 else None)
    if not raw:
        return

    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        return

    secrets_dir = os.path.join(os.path.dirname(__file__), ".secrets")
    os.makedirs(secrets_dir, exist_ok=True)
    config_path = os.path.join(secrets_dir, "scout-config.json")

    tmp_path = config_path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    os.replace(tmp_path, config_path)
    print(f"Config saved to {config_path}")

if __name__ == "__main__":
    main()
