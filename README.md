# Dmitry Zhuravlev — Cloud DevOps, Platform Engineering & AI Infrastructure Portfolio

Production-grade cloud platforms, AI infrastructure, reliability-focused systems, and secure delivery solutions built around operational challenges.

**Focus Areas:** AI Infrastructure • Distributed Agent Systems • DevSecOps • Platform Engineering • SRE • Cloud Architecture • Kubernetes • CI/CD • FinOps • Infrastructure as Code • Observability • Automation

---

## Featured Platform Projects

## 1. AI Infrastructure & Operations Platform

### [AI Operations Platform](https://github.com/DimitryZH/ai-operations-platform)

AI operations platform designed to coordinate domain-specific agents across SRE, CI/CD, secure delivery, FinOps, and cloud operations.

**Core Components:**

- AI agents — domain-specific operational agents for diagnostics, delivery, cost analysis, and infrastructure workflows  
- Agent orchestration — coordination layer for multi-agent execution across connected engineering systems  
- Python — platform services, integrations, and automation components  
- OpenTelemetry — telemetry collection and tracing across agent workflows and platform services  
- Cloud Run and Compute Engine — hybrid execution model for stateless services and stateful agent workloads  
- Terraform — modular provisioning of shared platform infrastructure and isolated agent environments  

**What this project delivers:**

- Unified control plane for AI-assisted cloud operations  
- Distributed agent architecture spanning multiple engineering domains  
- Integration path for SRE, CI/CD, FinOps, and secure delivery systems  
- Governance boundaries for safe, observable, and progressively enabled agent actions  

---

## 2. Continuous Integration Build Platform

### [CI Build Platform](https://github.com/DimitryZH/ci-build-platform)

Scalable build platform based on ephemeral self-hosted runners for cloud CI workloads.

**Core Components:**

- GitHub Actions — orchestration of CI workflows and job scheduling  
- Compute Engine — ephemeral runners providing isolated execution environments  
- Cloud Run — control plane service managing runner lifecycle and scaling decisions  
- Terraform — dynamic provisioning and teardown of compute resources  
- Docker — standardized build environment and artifact packaging  
- Container Registry — storage and distribution of build artifacts  
- Cloud Logging & Monitoring — visibility into runner execution, failures, and system behavior  

**What this project delivers:**

- On-demand provisioning of isolated CI runners  
- Scalable parallel build execution  
- Automated lifecycle management of build infrastructure  
- Platform-style abstraction over CI workloads  

---

## 3. SRE & Reliability Engineering Platform

### [SLO-Driven Delivery Platform on GKE](https://github.com/DimitryZH/sre-platform)

GitOps-based platform implementing SLO- and error budget–driven release governance for Kubernetes workloads.

**Core Components:**

- Kubernetes (GKE) — multi-environment cluster setup with namespace isolation and autoscaling for workload segmentation  
- Argo CD — GitOps control plane implementing the app-of-apps pattern and environment-based deployment promotion  
- Argo Rollouts — canary deployment strategy with analysis templates driven by Prometheus metrics  
- Prometheus — metrics collection and multi-window SLO evaluation  
- Grafana — visualization of SLOs, error budgets, and live rollout health signals  
- Helm — reusable and environment-specific configuration management for microservice deployment  
- Terraform — modular infrastructure provisioning for clusters, networking, and platform components  

**What this project delivers:**

- Progressive delivery controlled by observability signals  
- SLO- and error budget–driven deployment decisions  
- Automated promotion and rollback strategies  
- Platform-level control over service reliability and release safety  

---

## 4. Secure Delivery Platform

### [GCP Secure Delivery Platform](https://github.com/DimitryZH/gcp-secure-delivery-platform)

Secure cloud-native delivery platform focused on trusted builds, policy enforcement, and Kubernetes-native deployment controls.

**Core Components:**

- Cloud Build — reproducible and isolated build pipeline for trusted artifact creation  
- Artifact Registry — immutable artifact storage with controlled access  
- Binary Authorization — policy-based deployment validation ensuring only trusted images are deployed  
- Cloud Deploy — progressive delivery with controlled rollout strategies  
- Kubernetes (GKE) — controlled runtime environment with enforced deployment policies  
- Secret Manager — centralized secret storage with secure injection into workloads  
- Terraform — standardized infrastructure provisioning using reusable and customized Google Cloud modules  
- Cloud Logging & Monitoring — audit trail, deployment visibility, and operational signals  

**What this project delivers:**

- Controlled software delivery pipeline with integrated policy validation  
- Deployment verification and enforcement mechanisms  
- Trusted artifact lifecycle from build to runtime  
- Security integrated into the delivery workflow  

---

## 5. Enterprise Cloud Migration

### [Enterprise App Migration to Cloud](https://github.com/DimitryZH/app-migration)

Migration and modernization project focused on architecture, delivery automation, and cloud operating models.

**Core Components:**

**Compute & Runtime**

- Compute Engine + Managed Instance Groups — scalable and resilient application hosting layer  
- Cloud Run — containerized services for flexible workload execution  

**Networking**

- Custom VPC with private subnets — isolated network environment  
- No public IPs on instances — reduced attack surface  
- Cloud NAT — controlled outbound connectivity  
- HTTPS Load Balancer — secure entry point with TLS termination  

**Identity & Access**

- Dedicated service accounts — workload-level identity isolation  
- Granular IAM roles — least-privilege access to Firestore and Cloud Storage  

**Data & Storage**

- Firestore (Datastore mode) — managed NoSQL database  
- Cloud Storage — object storage for application data  

**Infrastructure & Delivery**

- Terraform — infrastructure as code with reproducible environments  
- GitHub Actions — automated build and deployment workflows  

**What this project delivers:**

- Migration from traditional infrastructure to cloud-native architecture  
- Private networking model with controlled access patterns  
- Integration of infrastructure, identity, and application delivery  
- Multi-layer system design across compute, networking, and CI/CD  

---

## 6. FinOps & Cloud Cost Assessment

### [FinOps Assessment Platform](https://github.com/DimitryZH/finops-assessment-platform)

Advanced cloud assessment platform for identifying waste, evaluating optimization opportunities, and producing structured FinOps findings across Google Cloud environments.

**Core Components:**

- Python — modular assessment engine separating resource discovery, normalization, evaluation, and reporting  
- Google Cloud APIs — structured discovery of projects, resources, utilization signals, and billing-relevant metadata  
- Cloud Run — stateless execution layer for repeatable assessment workloads  
- Cloud Scheduler — scheduled assessment cycles for recurring cost visibility  
- Terraform — modular provisioning of assessment infrastructure and supporting cloud resources  
- Reporting pipeline — structured transformation of collected facts into findings and recommendations  

**What this project delivers:**

- Multi-project cloud cost and resource assessment  
- Deterministic fact-to-finding evaluation workflow  
- Prioritized optimization recommendations with supporting evidence  
- Repeatable assessment structure suitable for client delivery and governance reviews  

**Open-source note:**  
Selected components, architecture documentation, and implementation patterns are published publicly while protected commercial logic remains separate. The earlier [Cloud Optimization Engine](https://github.com/DimitryZH/cloud-optimization-engine) represents the open-source foundation from which this platform evolved.

---

## Engineering Approach

All flagship projects follow consistent engineering principles:

- Architecture-first design with clear system boundaries and responsibilities  
- Integrated security controls across identity, infrastructure, AI agents, and delivery workflows  
- Cost-aware infrastructure decisions and resource modeling  
- Structured documentation covering architecture, deployment, security, operations, and cost analysis  
- Troubleshooting guides and operational scenarios captured as part of implementation  
- Modular infrastructure and reusable configuration patterns  
- Infrastructure as Code as the default provisioning model  

---

## Supporting Work

### [Cloud DevOps Toolkit](https://github.com/DimitryZH/cloud-devops-toolkit)

A curated collection of supporting implementations, AI infrastructure projects, experiments, and reusable engineering patterns complementing the flagship platform projects.

Includes:

- AI infrastructure and distributed agent systems  
- CI/CD implementations (GitHub Actions, Cloud Build, Jenkins)  
- Multi-cloud infrastructure examples (AWS, Azure, GCP)  
- Kubernetes patterns (Ingress, Istio, Kustomize, OpenShift)  
- GitOps workflows (Argo CD, Helm)  
- Observability setups (OpenTelemetry, Prometheus, Grafana, Datadog)  
- Infrastructure modules (Terraform, Ansible)  
- Automation scripts (Python, Bash)  