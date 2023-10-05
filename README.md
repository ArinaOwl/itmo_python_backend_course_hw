Homework 2: FastAPI base project testing
==========================

Packages installation
-------------------------------------------------------------------------------
- Create and activate *conda* virtual environment for development:

    ```
    conda create -n BaseApp python=3.10
    conda activate BaseApp
    ```

- Install dependencies with Poetry:

    ```
    pip install poetry
    poetry install
    ```

- Start with

    ```
    uvicorn app.main:app
    ```

Testing
-------------------------------------------------------------------------------
- Run tests in root directory:

    ```
    python -m pytest
    ```
  