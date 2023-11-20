# Data Processing using PySpark in Python via CLI

[![CI](https://github.com/nogibjj/IDS-706_rg361_week-10/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/IDS-706_rg361_week-10/actions/workflows/cicd.yml)

This repositroy contains files to process data in ``PySpark`` using ``Python`` and ``CLI``

All the queries are automatically ``logged`` in the ``query_logs`` file.

The repo has been created from [Week-5 Mini-Project](https://github.com/nogibjj/IDS-706_rg361_week-5) and modified as per requirements.

Created on on 05-Nov-2023

## Overview

The repository has the ``main.py`` file which makes use of the files in the mylib folder to perform data processing operations using PySpark. The main.py file can be interacted via ``CLI`` (Command Line Interface) by the user.

The repository automatically **``logs``** all the queries which are executed in the ``query_logs`` file.

``Github`` actions automatically runs the ``test_main.py`` which triggers the operations and logs them whenever there is an update in the repository.

![Schema](resources/schema.png)

## Instructions

Create a Codespace on main which will initialize the enviroment with the required packages and settings to execute the codes.

The ``main.py`` file accepts the commands via ``CLI``, the CLI are of the form:

```console
python main.py command args
```
the possible commands and their relevant arguments are:
1. ``create_data``: To create CSV file in the ``Data`` folder from the given source.<br>Args: (source, file_name, auto)
2. ``delete_data``: To delete the CSV file.<br>Args: (file_name, auto)
3. ``clear_log``: To clear the query_logs file.<br>Args: (log_file)
4. ``query``: Query to execute on the Dataset using PySpark

**Notes:** 
- All the arguments to the commands are optional as default values are set in the functions.
- The "auto" argument specfies to the function if the user is directly providing the full path (F) or wants the funtion to use the default path (T). Default value for auto is T

## Sample Execution and Test
  **Sample Execution:** 
  1. Query command is used without any arguments, so the average of the price column is returned:

   ![Auto Query](resources/query_auto.png)

  2. Custom Query is passed and returns the expected results:
  
     ![Auto Query](resources/query_manual.png)
   
**Testing:** "make test" command is run to verify all functionalities are working as expected and to see if the operations are being performed.

**Note:** Coverage is intentioanlly not kept at 100% as we do not call the clear_log funtion which would clear the logs.

![Test Execution](resources/test.png)


## Contents

### 1. query_logs
  Whenever a  PsSpark operation is performed, the query is automatically logged in the query_logs file with the timestamp for future reference and use. The log file can be cleared using the ``clear_log`` command

### 2. README.md
   contains the information about the repository and instructions for using it
   
### 3. requirements.txt
   contains the list of packages and libraries which are required for running the project. These are intalled and used in the virtual environment and Github actions.
   
### 4. .github/workflows
   github actions are used to automate the following processes whenever a change is made to the files in the repository:
   - ``install`` : installs the packages and libraries mentioned in the requirements.txt
   - ``test`` : uses ``pytest`` to test the python script
      
      **Note:** this action automatically triggers the sample operations whenever any changes are made in the repository
     
   - ``format`` : uses ``black`` to format the python files
   - ``lint`` : uses ``ruff`` to lint the python files
   
     
   **Note** -if all the processes run successfully the following output will be visible in github actions:
   ![Success Build](resources/build.png)
   
### 5. Makefile
   contains the instructions and sequences for the processes used in github actions and .devcontainer for creating the virtual environment
   
### 6. .devcontainer
   contains the ``dockerfile`` and ``devcontainer.json`` files which are used to build and define the setting of the virtual environment (codespaces - python) for running the codes.

### 7. Data
   The CSV files genereated by ``create_data`` are stored here by default for quick access and reference and can be delted using the ``delete_data`` command

### 8. resources 
   contains additonal files which are used in the README




  
