# AO3-GOPHER SERVER

## Introduction

Here is a project that I wanted to make after learning about the [Archive of Our Own](https://archiveofourown.org/) website
as well as the [Gopher Protocol](https://tools.ietf.org/html/rfc1436).

The main objective is to make an AO3 Website fast to browse and fast to load.

The gopher protocol is excellent for this task.


## Main Goals

- Accessing the different archives on AO3 with the Gopher Protocol
- Making querries to search for the archive you want
- Remembering what querry options you chose


## Usage

```bash
# Install dependencies
$ python -m pip install -r requirements.txt

# Run server
$ python server.py

# Accessing the Gopher Website
$ lynx gopher://0.0.0.0:7000/
```