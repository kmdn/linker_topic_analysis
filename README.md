# 🔗 Linking with Bias: Domain-Specific Behaviour in Entity Linking Systems

[![DOMiNO (anonymised)](https://zenodo.org/badge/DOI/10.5281/zenodo.15620484.svg)](https://doi.org/10.5281/zenodo.15620484)
[![DOMeX (anonymised)](https://zenodo.org/badge/DOI/10.5281/zenodo.15620484.svg)](https://doi.org/10.5281/zenodo.15620537)
[![Domain-Split Collection (anonymised)](https://zenodo.org/badge/DOI/10.5281/zenodo.15620484.svg)](https://doi.org/10.5281/zenodo.15620503)
[![Benchmark Collection (anonymised)](https://zenodo.org/badge/DOI/10.5281/zenodo.15620484.svg)](https://doi.org/10.5281/zenodo.15620518)

Welcome to the official repository for the paper **"Linking with Bias"**. This project investigates the **systemic domain bias** present in modern **entity linking (EL)** systems and introduces benchmark resources to measure and mitigate such biases.

---

## 🧠 Summary

Entity linking systems are widely adopted in knowledge-driven NLP applications, but they are often trained and evaluated on narrow, homogeneous domains. Our work reveals how these systems perform inconsistently across different domains, exposing a **domain bias** that hinders fairness and generalizability.

We contribute:

- **📊 A comprehensive analysis** of domain bias in EL systems.
- **🧾 DOMiNO**, a new benchmark dataset *balanced across 37 domains*.
- **🗂️ DOMeX**, a resource linking existing EL datasets to explicit domain labels.
- **🧪 Novel dataset variants** (ACE2004N, AIDAN, etc.) with novel mentions (and anonymized triples) to isolate bias factors.
- **📦 All datasets provided in NIF format** for interoperability and benchmarking.
- **🧪 Dataset preparation and evaluation scripts**

---

## 🧾 Citing the Paper

> 📄 **Linking with Bias: Domain-Specific Behaviour in Entity Linking Systems**  
> _Authors: [Redacted for Review]_  
> 📚 Conference/Journal: [SEMANTICS2025]  
> 🔗 [Link to paper not yet available]

---


## 📦 Datasets

All datasets are released under open-access licenses (when possible) and available on Zenodo in NIF (NLP Interchange Format). Use these datasets to replicate, extend, or benchmark your own entity linking systems.
### 🧬 DOMiNO: Domain-Balanced EL Benchmark

A novel dataset containing documents balanced across 37 domains, with and without nif:topic annotations to enable domain-specific evaluation.

    📁 Zenodo: https://zenodo.org/records/15620484

    🔍 Includes: domain lookup, bias evaluation-ready annotations

    📄 Format: RDF/NIF
	


### 🗂️ DOMeX: Domain Metadata for EL Datasets

Provides domain mappings for several existing entity linking datasets to support bias analysis.

    📁 DOMeX: https://zenodo.org/records/15620537

    📁 Domain-Split Documents: https://zenodo.org/records/15620503

### 🧪 Novel Anonymized Datasets

Anonymized versions of popular EL datasets with **altered mentions** (preserving domain and document semantics) for controlled bias studies.

| Dataset Name | Original     | Description         | Zenodo Link                                                   |
|--------------|--------------|---------------------|----------------------------------------------------------------|
| ACE2004N     | ACE2004      | Anonymized variant  | [🔗 Link](https://zenodo.org/records/15620518)                |
| AIDAN        | AIDA-CoNLL   | Anonymized variant  | [🔗 Link](https://zenodo.org/records/15620518)                |
| AQUAINTN     | AQUAINT      | Anonymized variant  | [🔗 Link](https://zenodo.org/records/15620518)                |
| MSNBCN       | MSNBC        | Anonymized variant  | [🔗 Link](https://zenodo.org/records/15620518)                |

## 🚀 Getting Started

Download the datasets from Zenodo and place them in the defined directory as defined in constants.py

Then you may run the notebooks to reproduce our analyses.


## 📈 Evaluation Framework

Use our pipeline to:

    * Measure and visualize domain bias
    * Interface with existing EL models
    * Run cross-domain, domain-specific or domain-limited evaluations


## 🤝 Contributing

We welcome contributions! Please open an issue or pull request for feedback, improvements, or similar.

## 📬 Contact

For questions, please contact:
📧 [**Anonymised for now**]
## 📝 License

This project is released under the MIT License. Datasets are shared under their respective Zenodo licensing terms.