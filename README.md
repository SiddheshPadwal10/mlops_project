# Project Setup with Poetry

This guide provides step-by-step instructions to set up Poetry for managing dependencies and environments in this project.

---

## Prerequisites

1. **Install Python**:
   - Ensure Python is installed on your system.
   - Verify the installation:
     ```powershell
     py --version
     ```
   - If Python is not installed, download and install it from the [official Python website](https://www.python.org/downloads/).

2. **Install Poetry**:
   - Run the following command to install Poetry:
     ```powershell
     (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
     ```
   - Verify the installation:
     ```powershell
     poetry --version
     ```

---

## Setting Up the Project

1. **Navigate to the Project Directory**:
   - Open a terminal and navigate to the project directory:
     ```powershell
     cd D:\siddhesh_projects\mlops_project
     ```

2. **Initialize Poetry**:
   - If the `pyproject.toml` file does not exist, create one by running:
     ```powershell
     poetry init
     ```
   - Follow the prompts to configure the project (e.g., name, version, dependencies).

3. **Install Dependencies**:
   - If a `pyproject.toml` file already exists, install the dependencies:
     ```powershell
     poetry install
     ```

4. **Activate the Virtual Environment**:
   - To activate the virtual environment created by Poetry, run:
     ```powershell
     poetry shell
     ```

---

## Managing Dependencies

1. **Add a Dependency**:
   - To add a new dependency:
     ```powershell
     poetry add <package_name>
     ```

2. **Add a Development Dependency**:
   - To add a dependency for development only:
     ```powershell
     poetry add --dev <package_name>
     ```

3. **Remove a Dependency**:
   - To remove a dependency:
     ```powershell
     poetry remove <package_name>
     ```

---

## Additional Tips

- **Check Poetry Version**:
  - To verify the installed version of Poetry:
    ```powershell
    poetry --version
    ```

- **Update Poetry**:
  - To update Poetry to the latest version:
    ```powershell
    poetry self update
    ```

- **Learn More**:
  - Refer to the [Poetry Documentation](https://python-poetry.org/docs/) for advanced usage and troubleshooting.