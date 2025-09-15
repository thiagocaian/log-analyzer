# log-analyzer

[![CI](https://github.com/thiagocaian/log-analyzer/actions/workflows/tests.yml/badge.svg)](https://github.com/thiagocaian/log-analyzer/actions)

Simple log analyzer (e.g., `auth.log`, `nginx access.log`) that detects failed authentications and aggregates requests by IP.  
Includes automated tests (pytest) and a CI pipeline on GitHub Actions.

---

## 🚀 How to Run

Create and activate a virtual environment, install dependencies, and run the CLI:

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python main.py --helpc 

## 📊 Usage Examples

### Auth log (SSH login failures)

```bash
python main.py auth --file tests/fixtures/auth.log --json out_auth.jsonve 
### Access log (Nginx requests)

```bash
python main.py access --file tests/fixtures/access.log --csv out_access.csv