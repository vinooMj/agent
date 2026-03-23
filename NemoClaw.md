# NVIDIA NemoClaw Docker Labspace

This repository contains the configuration and environment setup for a secure AI agent labspace. Based on my exploration of **NVIDIA NemoClaw**, this project demonstrates how to isolate agentic workflows using Docker and OpenShell runtimes.

##  Overview
NemoClaw is NVIDIA's stack for the **OpenClaw** agent platform. It provides an infrastructure layer (OpenShell) that sits between the AI agent and the host OS, enforcing:
- **Network Egress Control**: Preventing unauthorized data exfiltration.
- **Filesystem Sandboxing**: Restricting agents to `/sandbox` and `/tmp`.
- **Policy Enforcement**: Using Landlock and seccomp to limit system calls.

## Architecture
- **Agent**: OpenClaw / Claude Code / Custom LLM Agent.
- **Runtime**: OpenShell (NVIDIA Agent Toolkit).
- **Isolation**: Docker Containers with custom seccomp profiles.

## Getting Started

### Prerequisites
- Docker & Docker Compose
- NVIDIA Container Toolkit (for GPU acceleration)
- Python 3.10+

### Installation
1. Clone the repo:
   ```bash
   git clone [https://github.com/your-username/nemoclaw-docker-lab.git](https://github.com/your-username/nemoclaw-docker-lab.git)
   cd nemoclaw-docker-lab

nemo-claw init --blueprint basic-sandbox
docker-compose up -d
### 2. `docker-compose.yml`
```yaml
version: '3.8'

services:
  nemoclaw-agent:
    build:
      context: .
      dockerfile: Dockerfile
    image: nemoclaw-lab-env:latest
    volumes:
      - ./sandbox:/sandbox
      - /var/run/docker.sock:/var/run/docker.sock # Optional: for agents managing containers
    environment:
      - NVIDIA_VISIBLE_DEVICES=all
      - OPENAI_API_KEY=${OPENAI_API_KEY}
    security_opt:
      - seccomp:./configs/nemoclaw-seccomp.json # Hardened profile
    networks:
      - secure-agent-net

networks:
  secure-agent-net:
    driver: bridge


FROM nvidia/cuda:12.2.0-base-ubuntu22.04

# Install dependencies for NemoClaw and OpenClaw
RUN apt-get update && apt-get install -y \
    python3-pip \
    nodejs \
    npm \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install NVIDIA Agent Toolkit
RUN pip install nvidia-agent-toolkit

# Set up the sandbox directory
WORKDIR /sandbox

# Entry point to start the NemoClaw/OpenShell runtime
CMD ["nemo-claw", "run"]

FROM nvidia/cuda:12.2.0-base-ubuntu22.04

# Install dependencies for NemoClaw and OpenClaw
RUN apt-get update && apt-get install -y \
    python3-pip \
    nodejs \
    npm \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install NVIDIA Agent Toolkit
RUN pip install nvidia-agent-toolkit

# Set up the sandbox directory
WORKDIR /sandbox

# Entry point to start the NemoClaw/OpenShell runtime
CMD ["nemo-claw", "run"]

Key Highlights for your GitHub "About" section:
Focus: Converting theoretical AI safety (NemoClaw) into a practical, repeatable Docker environment.
Problem Solved: Prevents "Autonomous Agent Chaos" by wrapping agents in a security-first containerized layer.
Tech Stack: NVIDIA NemoClaw, Docker, OpenShell, Python, Shell.
