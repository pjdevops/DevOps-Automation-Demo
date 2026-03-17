# DevOps-Automation-Demo

**Demo project for Git, GitHub Actions, and DevOps automation**

---

## Project Overview
This project demonstrates a simple **Python application** with **unit testing** and **CI/CD automation** using **GitHub Actions**. It simulates a DevOps workflow, including:

- Git branching (`dev` → `main`)  
- Automated unit tests  
- Deployment simulation (`scripts/deploy.py`)  
- End-to-end CI/CD pipeline  

This repo is designed to showcase **DevOps and SRE skills** for resumes and interviews.

---

## Folder Structure

DevOps-Automation-Demo/
├── src/ # Python application code
├── tests/ # Unit tests
├── scripts/ # Automation scripts (deployment, backup, etc.)
├── ci-cd/ # GitHub Actions workflow YAML
├── docs/ # Project documentation
├── README.md # Project overview
└── interview_notes.md # Git & DevOps Q&A


---

## How to Run Locally

1. Clone the repo:

```bash
git clone https://github.com/<your-username>/DevOps-Automation-Demo.git
cd DevOps-Automation-Demo

2. Create a virtual environment:

python -m venv venv
source venv/Scripts/activate    # Windows PowerShell: .\venv\Scripts\Activate.ps1

3.  Install dependencies:
 pip install -r requirements.txt

4. Run the app:
python src/app.py

5.  Run deployment script:
 python scripts/deploy.py

GitHub Actions CI/CD

The project includes a GitHub Actions workflow:

.github/workflows/python-ci.yml

Workflow steps:

Checkout code

Setup Python 3.11

Install dependencies

Run unit tests

Run deployment script if tests pass

Logs can be viewed in the Actions tab on GitHub.
