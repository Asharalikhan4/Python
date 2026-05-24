'''
-> In Python, a package manager is a tool that automates the process of finding, downloading, installing, and updating third-party libraries (packages) that aren't included in Python's standard library.
-> Package managers allow you to manage the dependencies (external code written by you or someone else) that your project needs to work correctly.
-> Need of package managers:
    1. Dependency Resolution.
    2. Version Control.
    3. Centralized Sourcing.
-> Package Managers available:
    1. Pip - (The undisputed king of sheer volume because it ships with Python). Most used & Most Popular
    2. PyPI
    3. Conda - (Unmatched for handling complex math and machine learning libraries). Most Preferred for Data Science
    4. uv - (A blazing-fast tool built in Rust that is rapidly taking over modern workflows). Most Emerging & Fastest Growing
    5. Poetry - (Highly valued for strict, reproducible environments). Most Preferred for Enterprise Teams.
    6. pdm
'''


'''
-> Project Setup using pip
1. mkdir my-pip-project
2. cd my-pip-project
3. python -m venv .venv
4. source .venv/bin/activate
5. .venv\Scripts\activate.bat
6. pip install requests
7. pip freeze > requirements.txt
'''


'''
-> Project Setup using uv
1. curl -LsSf https://astral.sh/uv/install.sh | sh (for mac) or powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex" (for windows)
2. uv init my-uv-project
3. cd my-uv-project
4. uv add requests
5. uv run hello.py
'''