# Project Setup with Poetry

This guide provides step-by-step instructions to set up Poetry for managing dependencies and environments in this project.

---

## Prerequisites

1. **Install Python**:
   - Ensure Python is installed on your system.
   - Verify the installation:
     `powershell
     py --version
     `
   - If Python is not installed, download and install it from the [official Python website](https://www.python.org/downloads/).

2. **Install Poetry**:
   - Run the following command to install Poetry:
     `powershell
     (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
     `
   - Verify the installation:
     `powershell
     poetry --version
     `

[![CI](https://github.com/SiddheshPadwal10/mlops_project/actions/workflows/python-ci.yml/badge.svg?branch=dev)](https://github.com/SiddheshPadwal10/mlops_project/actions/workflows/python-ci.yml)

---

## Setting Up the Project

1. **Navigate to the Project Directory**:
   - Open a terminal and navigate to the project directory:
     `powershell
     cd D:\siddhesh_projects\mlops_project
     `

2. **Initialize Poetry**:
   - If the `pyproject.toml` file does not exist, create one by running:
     `powershell
     poetry init
     `
   - Follow the prompts to configure the project (e.g., name, version, dependencies).

3. **Install Dependencies**:
   - If a `pyproject.toml` file already exists, install the dependencies:
     `powershell
     poetry install
     `

4. **Activate the Virtual Environment**:
   - To activate the virtual environment created by Poetry, run:
     `powershell
     poetry shell
     `

---

## Managing Dependencies

1. **Add a Dependency**:
   - To add a new dependency:
     `powershell
     poetry add <package_name>
     `

2. **Add a Development Dependency**:
   - To add a dependency for development only:
     `powershell
     poetry add --dev <package_name>
     `

3. **Remove a Dependency**:
   - To remove a dependency:
     `powershell
     poetry remove <package_name>
     `

---

## Additional Tips

- **Check Poetry Version**:
  - To verify the installed version of Poetry:
    `powershell
    poetry --version
    `

- **Update Poetry**:
  - To update Poetry to the latest version:
    `powershell
    poetry self update
    `

- **Learn More**:
  - Refer to the [Poetry Documentation](https://python-poetry.org/docs/) for advanced usage and troubleshooting.

---

## Data

- **What was added**:
  - A small example dataset (local path: `data/raw/sample.csv`). Note: the repository is configured to ignore the top-level `data/` directory, so this file is present locally but not committed to the remote by default.
  - A data helper package at `src/mlops_project/data/` providing utilities used in examples and tests:
    - `load_csv` (in `ingest.py`)  loads a CSV into a pandas DataFrame and logs progress.
    - `validate.py`  schema validation helpers.
    - `transform.py`  basic transform helpers.
    - `schema.py`  data schema definition using Pandera.

- **How to run the examples locally**:
  - From the project root (PowerShell):
    `powershell
    # Run a quick one-liner that imports the ingestion helper and prints the DataFrame head
    poetry run python -c "from mlops_project.data.ingest import load_csv; df = load_csv('data/raw/sample.csv'); print(df.head())"
    `

  - Or run the module directly (module prints logs when executed):
    `powershell
    poetry run python -m mlops_project.data.ingest
    `

- **Notes**:
  - The top-level `data/` folder is ignored in this repo on purpose (see `.gitignore`). If you want the sample CSV tracked in the repository, remove `/data/` from `.gitignore` or add an explicit negation rule (e.g., `!data/raw/sample.csv`). We currently track package code under `src/mlops_project/data/`, not repository-level dataset files.
  - For larger or sensitive datasets, prefer storing data in external storage (S3, Google Cloud Storage, or Git LFS) and use small fixtures or synthetic samples in the repo for tests.

---

## Data Schema Validation with Pandera

This project uses **Pandera** to validate data schema and ensure data quality. Pandera is a lightweight, flexible data validation library for pandas DataFrames.

- **What is Pandera?**:
  - Pandera enables you to define and enforce data schemas using simple, declarative code.
  - You define expected column types, constraints (ranges, allowed values), and nullable flags.
  - When data is loaded, Pandera validates it and raises a `SchemaError` if validation fails.
  - This ensures data quality early in the pipeline and prevents invalid data from propagating downstream.

- **Schema Definition** (`src/mlops_project/data/schema.py`):
  - The training data schema is defined in the `get_training_schema()` function:
    `python
    def get_training_schema() -> DataFrameSchema:
        return DataFrameSchema(
            {
                "age": Column(int, Check.between(18, 100), nullable=False),
                "income": Column(float, Check.ge(0), nullable=False),
                "target": Column(int, Check.isin([0, 1]), nullable=False),
            },
            strict=True,
            coerce=True,
        )
    `
  - Columns defined:
    - `age` (int): values must be between 18 and 100.
    - `income` (float): values must be  0. Integers are automatically coerced to float (`coerce=True`).
    - `target` (int): values must be either 0 or 1 (binary classification label).
  - `strict=True`: no extra columns allowed; `coerce=True`: auto-convert compatible types (e.g., int  float).

- **Validation Integration** (`src/mlops_project/data/validate.py` and `ingest.py`):
  - The `validate_dataframe()` function in `validate.py` loads the schema and validates the DataFrame:
    `python
    from mlops_project.data.schema import get_training_schema
    
    def validate_dataframe(df):
        schema = get_training_schema()
        logger.info("Validating data schema")
        validated_df = schema.validate(df)
        logger.info("Data validation successful")
        return validated_df
    `
  - The `load_csv()` function in `ingest.py` automatically calls `validate_dataframe()` after loading:
    `python
    def load_csv(filepath: str) -> pd.DataFrame:
        logger.info(f"Loading data from {filepath}")
        df = pd.read_csv(filepath)
        df = validate_dataframe(df)
        logger.info(f"Loaded validated dataframe with shape {df.shape}")
        return df
    `
  - **Result**: When you call `load_csv()`, data is loaded, validated against the schema, and returned only if validation succeeds.

- **How to run with schema validation**:
  `powershell
  # Load and validate sample data
  poetry run python -c "from mlops_project.data.ingest import load_csv; df = load_csv('data/raw/sample.csv'); print(df)"
  `
  - If validation passes, logs will show:
    `
    Loading data from data/raw/sample.csv
    Validating data schema
    Data validation successful
    Loaded validated dataframe with shape (3, 3)
    `
  - If validation fails (e.g., invalid values or missing columns), a detailed `SchemaError` is raised with the constraint(s) that failed.

- **Adding more constraints**:
  - To add additional validation rules, edit `get_training_schema()` in `schema.py`. Examples:
    `python
    "age": Column(int, [Check.between(18, 100), Check.ne(25)]),  # age  25
    "income": Column(float, Check.isin([50000.0, 64000.0, 120000.0])),  # only these values
    `
  - For more information, see the [Pandera Documentation](https://pandera.readthedocs.io/).
