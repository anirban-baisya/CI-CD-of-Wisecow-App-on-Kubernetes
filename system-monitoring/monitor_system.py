"""
System Health Monitoring Script
------------------------------
Checks CPU usage, memory usage, disk space, and running processes.
Alerts if any metric crosses a threshold (CPU > 80%, Memory > 80%, Disk > 80%).
Logs alerts to the console.

How to run:
$ python monitor_system.py

Dependencies:
- psutil (install with: pip install -r requirements.txt)
"""

import psutil
import time

# Thresholds for alerts
CPU_THRESHOLD = 80  # percent
MEMORY_THRESHOLD = 80  # percent
DISK_THRESHOLD = 80  # percent

def check_cpu():
    cpu = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu}%")
    if cpu > CPU_THRESHOLD:
        print(f"ALERT: CPU usage exceeded threshold ({CPU_THRESHOLD}%)!")

def check_memory():
    mem = psutil.virtual_memory()
    print(f"Memory Usage: {mem.percent}%")
    if mem.percent > MEMORY_THRESHOLD:
        print(f"ALERT: Memory usage exceeded threshold ({MEMORY_THRESHOLD}%)!")

def check_disk():
    disk = psutil.disk_usage('/')
    print(f"Disk Usage: {disk.percent}%")
    if disk.percent > DISK_THRESHOLD:
        print(f"ALERT: Disk usage exceeded threshold ({DISK_THRESHOLD}%)!")

def check_processes():
    procs = len(psutil.pids())
    print(f"Running Processes: {procs}")
    # We can set a threshold for processes if you want

def main():
    print("---- System Health Monitor ----")
    check_cpu()
    check_memory()
    check_disk()
    check_processes()
    print("-------------------------------")

if __name__ == "__main__":
    main()