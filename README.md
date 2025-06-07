# IFRS Reporting Tool

This repository contains a minimal example of a command line tool for generating simple IFRS-style financial reports from a YAML file.

## Setup

Install the required dependencies:

```bash
pip install pyyaml
```

## Usage

```
python -m ifrs_reporting.main data/sample.yml
```

You can also specify an output file:

```
python -m ifrs_reporting.main data/sample.yml -o report.txt
```

The sample data located in `data/sample.yml` demonstrates the expected structure of the input file. Running the command will produce a basic report in the terminal or save it to `report.txt` if an output path is provided.
