# CloudScale Logistics: GitOps Manifest Guardrail

---

# Project Context
In this scenario, I acted as a DevOps Engineer for CloudScale Logistics, a shipping company moving to Kubernetes. To prevent "The Friday Afternoon Crash" (caused by misconfigured YAML files), I built an automated validation gate.


This project ensures that no Kubernetes manifest is deployed unless it follows strict production standards for security and stability.

---

# Key Implementation Details
• Standardized Deployment: Created a Deployment for the tracking-api with 3 replicas for high availability.
• Automated Guardrails: Integrated Kube-score into the GitHub Actions pipeline to catch "anti-patterns" (like missing resource limits) before they reach the cluster.
• Pod Hardening: Configured securityContext to ensure containers run as non-root and have readOnlyRootFilesystem enabled, significantly reducing the attack surface.
• Stability Features: Implemented both livenessProbes and readinessProbes to allow Kubernetes to monitor application health and perform zero-downtime updates.

---

# Technical Stack
• Platform: Kubernetes (Manifests) 
• Pipeline: GitHub Actions
• Validation: Kube-score
• Domain: Logistics / Supply Chain API

---

# Troubleshooting Experience
• The "S" Bug: Initially, the pipeline failed because of a naming mismatch between the directory (manifests) and the workflow file (manifest). This reinforced the importance of strict naming conventions in automated environments.
• Security Feedback: The original YAML failed Kube-score's audit because it lacked root-user protections. I successfully "hardened" the YAML by adding security contexts to pass the validation gate.

