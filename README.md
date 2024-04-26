# LinterProject

LinterProject is a Python code analysis tool that utilizes Flake8 and Pylint to identify suspicious code patterns. The tool provides a comprehensive report of potential vulnerabilities and code quality issues, aiding developers in maintaining high code standards.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Make sure you have Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Installing

1. **Clone the Repository**

    ```bash
    git clone https://github.com/VIZIIER/LinterProject.git
    cd LinterProject
    ```

2. **Set Up a Virtual Environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the linter analysis, navigate to the `scripts` directory and execute the `run_linters.py` script:

```bash
python scripts/run_linters.py
