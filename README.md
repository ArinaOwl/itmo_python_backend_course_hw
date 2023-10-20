Homework 3: FastAPI project with microservices
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

- Start **from root directory** with

  - Main API service

      ```
      cd api & uvicorn app.main:app
      ```
  
  - Auth service

      ```
      cd auth & uvicorn app.main:app --port 8001
      ```
    
  - Dictionary service

      ```
      cd dictionary & uvicorn app.main:app --port 8002
      ```

Testing
-------------------------------------------------------------------------------
- Run tests **from root directory**:

  - Main API service (*Auth and Dictionary services need to be started*)

      ```
      cd api & python -m pytest
      ```
    
  - Dictionary service

      ```
      cd dictionary & python -m pytest
      ```