# Command Line Certificate Generator Tool

Automating Certificate Creation for Every Event, Instantly.

## Overview

The *Command Line Certificate Generator Tool* is a Python-based CLI utility that automates the generation of participation certificates from a template image and participant data in Excel format. Ideal for educational institutions, event organizers, and NGOs, this tool saves time and reduces errors by generating certificates in bulk through a simple command.


## Installation

git clone https://github.com/Tulasi-Sahu/Certificate_Gen_CLI.git

cd certificate-generator

pip install .

**##Usage**

**Method1:Interactive**

Cgen  <excel path>

The tool will prompt for:
•	Event Name
•	From and To dates
•	Output Format(PNG or PDF)

**Method2:Direct Command-Line Execution**
cgen [-o <pdf|png >] [-f <from-date> [-t <to-date>]] [-n <program name>] <excel path>


