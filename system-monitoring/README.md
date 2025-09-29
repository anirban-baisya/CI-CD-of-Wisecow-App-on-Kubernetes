# System Monitoring & Application Health Checker

## Folder Structure

```
system-monitoring/
├── README.md
├── requirements.txt
├── monitor_system.py
└── check_app_health.py
```

## How to Install Dependencies

First, make sure we have Python installed (3.6+ recommended).

Then, in our terminal:

```bash
pip install -r requirements.txt
```

## How to Run the Scripts

### System Health Monitoring Script
Checks CPU, memory, disk usage, and running processes. Alerts if thresholds are crossed.

```bash
python monitor_system.py
```

### Application Health Checker
Checks if our web app is 'UP' or 'DOWN' by inspecting HTTP status codes.

Edit `check_app_health.py` and set `APP_URL` to our app’s address.

```bash
python check_app_health.py
```

## My Observation 

- Change thresholds in `monitor_system.py` for our needs.
- For the health checker, any HTTP status other than 200 means the app may be down.
- Both scripts print their results and alerts to the console.
- If we want logs in a file, we can redirect output: `python monitor_system.py > health.log`

## Common Issues Solved

- **No EXTERNAL-IP after Kubernetes deployment:** Wait for AWS ELB provisioning and set Service type to LoadBalancer.
- **Site unreachable on ELB DNS:** Open correct port in AWS security group; ensure Service port matches app port.
- **Access app without port:** Set Service port to 80 in Kubernetes manifest.
- **Kubeconfig errors in CI/CD:** Use valid EKS kubeconfig and AWS credentials in GitHub Secrets.
