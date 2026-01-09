# Project 1: Simple CI/CD Pipeline & Flask Containerization

---

# Overview
This was my first project in building an automated pipeline for a Python application. The goal was to take a simple Flask web app, "Dockerize" it, and set up a GitHub Actions workflow that automatically builds and tests the code whenever I push changes.

--- 

# What I Built
• Flask Application: A basic web server that serves a "Project 1" homepage.
• Docker Configuration: Created a Dockerfile using python:3.11-slim. I chose the "slim" version to keep the container small and efficient.
• CI/CD Pipeline: A GitHub Actions workflow (ci-cd.yml) that triggers on every push to the main branch. It handles setting up the environment, installing dependencies, and building the Docker image.
• K8s Manifest: A standard Deployment YAML to run 2 replicas of the app, ensuring high availability.

---

# Technical Stack
• Language: Python 3.11 (Flask)
• Containerization: Docker
• Automation: GitHub Actions
• Orchestration: Kubernetes 

# Challenges & Lessons Learned
• File Paths: I learned that GitHub Actions is very sensitive to folder structures. I had to adjust my YAML file to correctly point to the project-1-ci-cd-pipeline/app directory.
• Hidden Files: I dealt with an issue where a nested .git folder prevented my files from showing up on GitHub. I learned how to use git rm --cached to fix the repository index.
• Slim vs. Full Images: Using python-slim taught me the importance of keeping container sizes small for faster deployment times in a professional environment.