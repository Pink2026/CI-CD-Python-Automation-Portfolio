# DevSecOps Pipeline: Python API + Automated Security Scanning

---

# Overview
This project is a containerized Flask microservice integrated into a CI/CD pipeline that enforces security standards before deployment.
I have focused on building a "Security-First" workflow where code is not just built, but verified against known vulnerabilities automatically.

---

# Key Features & Engineering Decisions
• Container Hardening: Used python:3.11-alpine as the base image.
    Decision: Alpine was chosen to minimize the attack surface and keep image sizes under 50MB for faster deployments.
• Automated CVE Scanning: Integrated Trivy into the GitHub Actions workflow.
    Decision: Configured the pipeline to scan the filesystem to catch issues in dependencies before the Docker build finishes.
• Registry Automation: Automated the lifecycle of the image from build to push using GHCR (GitHub Container Registry).
• K8s Readiness: Included a /health endpoint to support Kubernetes liveness/readiness probes.

---

# Technical Stack
• Runtime: Python 3.11
• Framework: Flask
• CI/CD: GitHub Actions
• Security: Aqua Security Trivy
• Registry: GHCR

---

# Pipeline Logic
The pipeline (devsecops.yml) executes the following steps on every push to main:
1. Checkout: Pulls the latest source code.
2. Security Audit: Runs Trivy. If critical vulnerabilities are found, the build can be configured to fail (exit-code 1), preventing insecure images from reaching the registry.
3. Build & Tag: Builds the Docker image using lowercase tagging to comply with OCI standards.
4. Registry Push: Authenticates via GITHUB_TOKEN and pushes the artifact to GHCR.

---

# Troubleshooting & Lessons Learned
• Registry Compliance: Initially encountered exit code 1 during the build step because Docker repository names must be strictly lowercase. Resolved by hardcoding the image tag to lowercase.
• Scan Failures: Experienced pipeline breaks due to transient network issues during the Trivy DB download. Implemented better error tracking in logs to differentiate between security risks and system timeouts.