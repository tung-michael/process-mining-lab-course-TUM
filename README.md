## Process Mining Web Service

This project provides a Web Service, where user can upload a standard log file (.xes) and have it visualized as Petri Net by the Alpha algorithm (Process Discovery).

The resulted Petri Net can be downloaded as PDF or PNG file.

This project was written with Python 3.
#### Project structure
```zsh
.
├── README.md
├── alpha_web_app 
│   ├── __init__.py
│   ├── app.py
│   ├── execute_pm_alg.py
│   ├── file_path.py  # set up file-paths
│   ├── process_mining_alg
│   │   ├── alphaAlg.py # implementation of alpha algorithm
│   │   ├── petri_visualize.py # implementation of Petri net visualization
│   │   ├── test_set  # test data
│   │   │   ├── L1.xes
│   │   │   ├── L2.xes
│   │   │   ├── L3.xes
│   │   │   ├── L4.xes
│   │   │   ├── L5.xes
│   │   │   ├── L6.xes
│   │   │   ├── L7.xes
│   │   │   ├── billinstances.xes
│   │   │   ├── description_of_datasets.txt
│   │   │   ├── flyerinstances.xes
│   │   │   ├── posterinstances.xes
│   │   │   └── running-example.xes
│   │   └── xes_importer.py # .xes file parser
│   ├── static
│   │   ├── pm_output # results of uploaded files
│   │   └── site.css
│   ├── templates
│   │   ├── about.html
│   │   ├── contact.html
│   │   ├── home.html
│   │   ├── layout.html
│   │   └── result-home.html
│   ├── test_alphaAlg.py
│   ├── uploads # files uploaded by users
│   └── views.py # routes for website
└── requirements.txt
```

## Installation

The Petri Net is visualized by *dot* language, which uses graphviz package to render to file (PDF, PNG,...). To install graphviz, please refer to [Graphviz](https://graphviz.org/download).

Activate your virtual environment or create a new one (insert your path):
`python -m venv /path/to/new/virtual/env`

Run requirements.txt to install project's dependencies:

`pip install -r /path/to/requirements.txt`


## Usage
Open the project directory in CLI.

You might have to activate the virtual environment to run the project with installed dependencies.

Run the project with `python -m flask run`.
