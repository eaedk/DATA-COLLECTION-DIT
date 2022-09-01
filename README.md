# DATA-COLLECTION-DIT

# Description
This is the repository containing all the Data Collection assignments.
# Setup
Install the required packages to be able to run the evaluation locally.

You need to have [`Python3`](https://www.python.org/) on your system. Then you can clone this repo and being at the repo's `machine@username repo_root_folder> ...`  follow the steps below:

- Windows:
        
        python3 -m venv venv; venv\Scripts\activate; python -m pip install --upgrade pip; python -m pip install -qr requirements.txt; python COURSE/setup.py install 

- Linux & MacOs:
        
        python3 -m venv venv; source venv/bin/activate; python -m pip install --upgrade pip; python -m pip install -qr requirements.txt; python COURSE/setup.py install 


## Evaluation
This evaluation will be automatically grade, so please follow the instructions carefully. 

You can run this command bellow being at the root of the repository and having the `venv` activated.
```command
pytest -v
```