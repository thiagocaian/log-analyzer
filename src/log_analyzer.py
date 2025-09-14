import json, csv
from collections import Counter

def aggregate_auth_by_ip(filepath):
    """Conta falhas de login em auth.log por IP"""
    counts = Counter()
    with open(filepath) as f:
        for line in f:
            parts = line.strip().split()
            if "Failed" in line and parts:
                ip = parts[-4] if len(parts) >= 4 else "?"
                counts[ip] += 1
    return counts

def aggregate_access_by_ip(filepath):
    """Conta requisições em access.log por IP"""
    counts = Counter()
    with open(filepath) as f:
        for line in f:
            ip = line.split()[0] if line.strip() else "?"
            counts[ip] += 1
    return counts

def export_json(data, filepath):
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)

def export_csv(data, filepath):
    with open(filepath, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ip", "count"])
        for ip, cnt in data.items():
            writer.writerow([ip, cnt])
