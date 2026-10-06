#!/usr/bin/env python3
"""Signed 1Panel API caller. Stdlib only.

Usage:
  python 1panel_api.py swagger                       # fetch the swagger spec JSON
  python 1panel_api.py call METHOD PATH [JSON_BODY]  # e.g. call GET /api/v2/websites/list
  python 1panel_api.py self-check                    # verify signature vectors, no network

Env:
  ONEPANEL_BASE_URL         e.g. http://host:port  (required)
  ONEPANEL_API_KEY          API interface key from panel settings (required)
  ONEPANEL_API_ALGO         hmac-sha256 (default) | md5
  ONEPANEL_SKIP_TLS_VERIFY  true|1 to accept self-signed https certs
"""
import hashlib
import hmac
import json
import os
import ssl
import sys
import time
import urllib.error
import urllib.request

SWAGGER_DOC_CANDIDATES = ("/1panel/swagger/doc.json", "/1panel/swagger/swagger.json")


def sign(algo: str, key: str, ts: str) -> str:
    if algo == "md5":
        return hashlib.md5(("1panel" + key + ts).encode()).hexdigest()
    if algo == "hmac-sha256":
        return hmac.new(key.encode(), ("1panel:" + ts).encode(), hashlib.sha256).hexdigest()
    raise SystemExit(f"unknown ONEPANEL_API_ALGO: {algo!r} (use hmac-sha256 or md5)")


def request(base_url: str, method: str, path: str, body=None, sign_payload=True):
    base = base_url.rstrip("/")
    if not base.startswith(("http://", "https://")):
        raise SystemExit(f"ONEPANEL_BASE_URL must start with http:// or https://, got: {base_url!r}")
    key = os.environ.get("ONEPANEL_API_KEY", "")
    if sign_payload and not key:
        raise SystemExit("Missing ONEPANEL_API_KEY")
    algo = os.environ.get("ONEPANEL_API_ALGO", "hmac-sha256").lower()

    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    data = None
    if body is not None:
        data = json.dumps(body).encode()
    if sign_payload:
        ts = str(int(time.time()))
        headers["1Panel-Timestamp"] = ts
        headers["1Panel-Token"] = sign(algo, key, ts)

    req = urllib.request.Request(base + path, data=data, headers=headers, method=method)
    ctx = None
    if base.startswith("https://") and os.environ.get("ONEPANEL_SKIP_TLS_VERIFY", "").lower() in ("1", "true"):
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
            return resp.status, resp.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", "replace")


def pretty(status: int, raw: str) -> None:
    print(f"HTTP {status}")
    try:
        print(json.dumps(json.loads(raw), ensure_ascii=False, indent=2))
    except ValueError:
        print(raw)


def main() -> None:
    if len(sys.argv) > 1 and sys.argv[1] == "self-check":
        ts = "1700000000"
        assert sign("md5", "testkey", ts) == "3a9cbae012be83320037ba5982b23af7", "md5 vector mismatch"
        assert (
            sign("hmac-sha256", "testkey", ts)
            == "7dc0b3dd218827dc9312d121c05cd3b9fcef38b1add0b7948b763f0f1bb55824"
        ), "hmac-sha256 vector mismatch"
        try:
            request("ftp://example.com", "GET", "/")
            raise AssertionError("scheme check did not reject ftp://")
        except SystemExit:
            pass
        print("self-check ok")
        return

    base = os.environ.get("ONEPANEL_BASE_URL", "").strip()
    if not base:
        raise SystemExit("Missing ONEPANEL_BASE_URL")

    if len(sys.argv) > 1 and sys.argv[1] == "swagger":
        # Try signed too: some installs accept API-key headers, most want a browser session.
        for signed in (False, True):
            for candidate in SWAGGER_DOC_CANDIDATES:
                status, raw = request(base, "GET", candidate, sign_payload=signed)
                if status == 200 and ('"swagger"' in raw[:200] or '"openapi"' in raw[:200] or '"paths"' in raw[:200]):
                    pretty(status, raw)
                    return
                print(f"{'signed ' if signed else ''}{candidate} -> HTTP {status}")
        raise SystemExit("spec JSON not reachable via API key (this install requires a logged-in browser session for /1panel/swagger/). Discover endpoints from official docs or the 1panel-skills module files instead.")

    if len(sys.argv) < 4:
        raise SystemExit(__doc__)
    method, path = sys.argv[2], sys.argv[3]
    # Git Bash mangles leading-slash args into filesystem paths; accept both forms.
    if not path.startswith("/"):
        path = "/" + path
    body = json.loads(sys.argv[4]) if len(sys.argv) > 4 else None
    pretty(*request(base, method.upper(), path, body))


if __name__ == "__main__":
    main()
