==========================
FastAPI base project
==========================

Packages installation
-------------------------------------------------------------------------------
- Create and activate *conda* virtual environment for development:

.. code::

    conda create -n BaseApp python=3.10
    conda activate BaseApp

- Install dependencies with Poetry:

.. code::

    pip install poetry
    poetry install

- Start with

.. code::

    uvicorn app.main:app