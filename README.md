# Genetic Algorithm
For this assignment you will be creating a genetic algorithm from scratch.
You can only use the libraries laid out in the ```requirements.txt``` file.
Feel free to import whatever functions you wish as long as they are in the libraries laid out in the requirements file or are created in the assignment.

# Creating Your Environment
## Python Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## UV
```bash
uv init
uv pip install -r requirements.txt
```

# Running Program
In the highest level directory
```bash
python main.py
```

If using uv
```bash
uv run main.py
```

# Testing
You should also be try a testing suite to gain the exposure. 
The one that is being installed in called pytest. 
Look into it to learn how to properly test a function.
Once you have tests written, you can run 
```bash
pytest
```
and it will run all tests that are properly laid out in the ```src/tests``` directory.
