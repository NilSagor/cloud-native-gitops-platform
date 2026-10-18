# Cloud Native apps with GitOps platform

- Multi-stage Dockerfile for `product-api` (Flask + gunicorn)
- `docker/docker-compose.yml` spins up `api` + `redis`
- Run: `docker compose -f docker/docker-compose.yml up --build`
<!-- - Image pushed to `docker push ghcr.io/${(L)GH_USER}/product-api:dev` -->
- Image pushed to `ghcr.io/${(L)GH_USER}/product-api:dev`

## Phase 2 — Node provisioning

- `ansible/site.yml` prepares Ubuntu VMs: Docker + Kubernetes kernel prerequisites
- Usage: `ansible-playbook -i ansible/inventory/hosts ansible/site.yml`