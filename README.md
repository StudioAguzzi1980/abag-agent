# ABAG AI Business Advisor Agent

AI-powered business advisor for **American Business Advisory Group (ABAG)**, designed to help U.S. companies expand into Italy and Europe.

## What It Does

The agent acts as a senior international business consultant specializing in:

- **Market entry strategy** for Italy and Europe
- **Italian company formation** (SRL, SPA, branches, and representative offices)
- **Tax and regulatory guidance** for cross-border operations
- **Banking and compliance** for U.S.-Italy business
- **Business communication** — including LinkedIn content aimed at U.S. business leaders

## Requirements

- Python 3.10+
- An [OpenAI API key](https://platform.openai.com/api-keys)

## Setup

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Configure your API key
cp .env.example .env
# Edit .env and set OPENAI_API_KEY
```

## Usage

### Interactive chat

```bash
python agent.py
```

### Programmatic use

```python
from agent import get_single_response

response = get_single_response("What are the steps to open an SRL in Italy?")
print(response)
```

## Running Tests

```bash
pip install pytest
pytest test_agent.py -v
```
