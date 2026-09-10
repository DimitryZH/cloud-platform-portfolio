# Dmitry Zhuravlev

## Cloud DevOps, Platform Engineering & AI Infrastructure Portfolio

Production-grade cloud platforms, AI infrastructure, reliability-focused systems, and secure delivery solutions built around operational challenges.

### GitHub Developer Program Member

Recognized as a developer building integrations, automation, and tooling on the GitHub platform.

**Focus Areas:** AI Infrastructure • Distributed Agent Systems • DevSecOps • Platform Engineering • SRE • Cloud Architecture • Kubernetes • CI/CD • FinOps • Infrastructure as Code • Observability • Automation

---

# Featured Platform Projects

## 1. AI Infrastructure & Operations Platform

### [AI Operations Platform](https://github.com/DimitryZH/ai-operations-platform)

GCP-first AI-native operations control plane for governed DevOps, SRE, Platform Engineering, FinOps, security, and cloud operations workflows.

**Core Components:**

- Python control plane — durable task, attempt, review, and execution workflow management  
- PostgreSQL — persistent operational state independent of agent sessions  
- Executor adapters — replaceable agent and automation backends behind capability boundaries  
- Capability verification — validates executor capabilities before active attempts  
- Human review — explicit approval gates for governed operational actions  
- GCP Stateful Agent Runtime — persistent private runtime foundation for AI agents  
- Secret Manager & IAP — protected secrets and operator access  
- GitHub — repository workflows, validation evidence, and auditable engineering changes  

**What this project delivers:**

- Durable orchestration independent of individual AI agent sessions  
- Governed execution with explicit human approval boundaries  
- Replaceable executors instead of dependency on a single agent framework  
- Capability-aware dispatch and controlled retry workflows  
- Foundation for coordinated AI-assisted operations across SRE, CI/CD, FinOps, security, and cloud platforms  

---

## 2. Continuous Integration Build Platform

### [CI Build Platform](https://github.com/DimitryZH/ci-build-platform)

GCP-based CI platform for on-demand ephemeral self-hosted GitHub Actions runners with a Cloud Run controller and Terraform-managed GCE infrastructure.

**Core Components:**

- GitHub Actions — runner request and CI workflow orchestration  
- GitHub REST API — short-lived runner registration tokens  
- Cloud Run — controller for authenticated provisioning requests  
- Terraform — GCE runner infrastructure provisioning and management  
- Compute Engine — hosts the self-hosted runner  
- Docker / Docker Hub — container image build and publishing  

**What this project delivers:**

- On-demand self-hosted runner provisioning  
- Ephemeral GitHub runner registration  
- Isolated CI execution on GCE  
- Automated VM shutdown after workload completion  
- Historical end-to-end workflow validation  

---

## 3. SRE & Reliability Engineering Platform

### [SLO-Driven Progressive Delivery Platform](https://github.com/DimitryZH/sre-platform)

GitOps-based SRE platform implementing SLO- and error budget–driven release governance with validated canary promotion, automated abort, and recovery workflows on GKE.

**Core Components:**

- Kubernetes (GKE) — multi-environment runtime for SLO-governed application delivery  
- Argo CD — GitOps control plane for declarative application deployment  
- Argo Rollouts — canary delivery with SLO-based analysis gates at 10% and 50%  
- Prometheus — multi-window SLO, error-ratio, and burn-rate evaluation  
- Grafana — visualization of SLOs, error budgets, rollout health, and decision signals  
- k6 — deterministic baseline and failure traffic for validating rollout decisions  
- Helm — reusable application and platform configuration  
- Terraform — modular provisioning of GKE and supporting infrastructure  

**What this project delivers:**

- SLO-gated progressive delivery  
- Automated canary promotion or abort based on service-level signals  
- Multi-window burn-rate and error-budget evaluation  
- Deterministic failure injection and rollout validation  
- Operational recovery from failed releases  

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