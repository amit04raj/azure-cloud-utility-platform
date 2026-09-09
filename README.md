# Azure Cloud Utility Platform

A small cloud-hosted web application that brings practical technical utilities together in one place.

The project is built with Python and FastAPI, deployed to Azure App Service, and managed with Terraform. GitHub Actions handles automated testing and deployment using OpenID Connect (OIDC) authentication with Microsoft Entra ID.

## Current Features

* Calculator with basic arithmetic operations
* IPv4 CIDR and subnet calculation
* Unit conversion utilities
* Notes functionality
* Health-check endpoint for deployment verification
* Automated API and unit tests

## Technology Stack

### Application

* Python 3.12
* FastAPI
* Uvicorn
* HTML
* CSS
* JavaScript

### Testing

* pytest
* FastAPI TestClient

### Cloud and Infrastructure

* Microsoft Azure
* Azure App Service
* Azure Service Plan
* Terraform

### CI/CD

* GitHub Actions
* GitHub OIDC
* Microsoft Entra ID
* Azure CLI
* `azure/login`
* `azure/webapps-deploy`

## Architecture

The application uses a simple architecture at this stage. The frontend and backend are served by the same FastAPI application running on Azure App Service.

The current deployment does not use a database, container platform, or separate frontend service.

![Azure Cloud Utility Platform Architecture](docs/architecture-diagram.png)

A more detailed explanation is available in [Architecture Documentation](docs/architecture.md).

## Project Structure

```text
azure-cloud-utility-platform/
│
├── app/
│   ├── static/
│   │   ├── script.js
│   │   └── style.css
│   ├── templates/
│   │   └── index.html
│   ├── calculator.py
│   ├── cidr.py
│   ├── converter.py
│   └── main.py
│
├── tests/
│   ├── test_api.py
│   └── test_calculator.py
│
├── terraform/
│   ├── app_service.tf
│   ├── main.tf
│   ├── outputs.tf
│   ├── providers.tf
│   └── variables.tf
│
├── docs/
│   ├── architecture.md
│   └── architecture-diagram.png
│
├── .github/
│   └── workflows/
│       └── deploy.yml
│
├── requirements.txt
└── README.md
```

## Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/amit04raj/azure-cloud-utility-platform.git
cd azure-cloud-utility-platform
```

### 2. Create a virtual environment

On Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

On Linux or macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Start the application

```bash
python -m uvicorn app.main:app --reload
```

The application will be available locally at:

```text
http://127.0.0.1:8000
```

## Running Tests

Run the complete test suite with:

```bash
python -m pytest
```

The current test suite covers the API health endpoint, calculator operations, division-by-zero handling, and invalid requests.

## Infrastructure

Azure infrastructure is defined using Terraform.

The current Terraform configuration provisions the core resources required to run the application on Azure App Service.

Typical Terraform workflow:

```bash
cd terraform
terraform init
terraform plan
terraform apply
```

Terraform state files and local Terraform working directories are excluded from Git through `.gitignore`.

## CI/CD Pipeline

Every push to the `main` branch triggers the GitHub Actions deployment workflow.

The pipeline performs the following steps:

```text
Push to main
    │
    ▼
Checkout repository
    │
    ▼
Set up Python
    │
    ▼
Install dependencies
    │
    ▼
Run automated tests
    │
    ▼
Authenticate to Azure using GitHub OIDC
    │
    ▼
Deploy to Azure App Service
    │
    ▼
Verify application health
```

The deployment uses GitHub's OIDC integration with Microsoft Entra ID instead of storing a long-lived Azure client secret in GitHub.

The Azure role assignment used for deployment is scoped to the App Service resource rather than the entire subscription.

After deployment, the pipeline requests the application's `/health` endpoint. A failed health check causes the workflow to fail.

## Security Considerations

The current deployment includes several basic security controls:

* HTTPS-only access is enabled for the App Service.
* Minimum TLS version is set to 1.2.
* FTP publishing with basic authentication is disabled.
* Web Deploy publishing with basic authentication is disabled.
* GitHub Actions authenticates to Azure through OIDC.
* No Azure client secret is stored in the GitHub workflow.
* The GitHub deployment identity has access scoped to the App Service.
* Terraform state and sensitive local configuration files are excluded through `.gitignore`.

This is a practical baseline rather than a claim that the application is production-hardened.

## Project Status

The first foundation phase is complete:

* Application implemented
* Automated tests added
* Azure infrastructure defined with Terraform
* Azure App Service deployed
* GitHub Actions CI/CD configured
* OIDC authentication configured
* Post-deployment health verification implemented
* Architecture documentation added

Future development will focus on expanding the platform's functionality and improving its cloud, security, reliability, and operational capabilities.

## License

This project is currently maintained as a personal engineering and portfolio project.
