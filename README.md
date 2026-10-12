# SLSA-Compliant Secure Software Delivery Platform on Kubernetes

## Project Overview

This project implements a secure software delivery platform on Kubernetes that verifies the integrity and authenticity of container images before deployment.

The platform integrates CI/CD security, Software Bill of Materials (SBOM), vulnerability scanning, image signing, SLSA provenance, GitOps deployment, admission control, and runtime security monitoring.

## Technology Stack

- GitHub Actions
- Docker
- AWS ECR
- Amazon EKS / Kubernetes
- Syft
- Trivy or Grype
- Sigstore Cosign and Rekor
- SLSA Provenance
- Argo CD
- Kyverno
- Falco
- Terraform
- Prometheus and Grafana

## Project Phases

1. Hardened Build Pipeline
2. SBOM and Vulnerability Scanning
3. Image Signing and Provenance
4. Kubernetes Admission Control
5. GitOps Promotion and Rollback
6. Runtime Security and Monitoring
7. Documentation and Live Demonstration

## Project Status

- [ ] Repository initialization
- [ ] Secure CI/CD pipeline
- [ ] SBOM and vulnerability gates
- [ ] Image signing and provenance
- [ ] Admission policies
- [ ] GitOps deployment
- [ ] Runtime security
- [ ] Final report and demonstration

## Security Objective

Ensure that only authorized, verified, and policy-compliant container images are deployed to Kubernetes, with traceability from source-code commit to running workload.