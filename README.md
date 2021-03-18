# cookiecutter-beet

Minimal [Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for [beet](https://github.com/mcbeet/beet) projects.

## Table of Contents
- [Getting Started](#Getting-Started)
    - [Generate project structure](#Generate-project-structure)
    - [Install build tools](#Install-build-tools)
    - [Install dependencies](#Install-dependencies)
    - [Project structure overview](#Project-structure-overview)
- [Features](#Features)

## Getting Started
### Generate project structure
Install [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and generate new project:
```bash
$ pip install cookiecutter
$ cookiecutter https://github.com/OrangeUtan/cookiecutter-beet
```

Cookiecutter prompts you for information about your project:
```
github_username []: OrangeUtan
minecraft_username [OrangeUtan]: Oran9eUtan
user_namespace [orangeutan]: oran9eutan
project_name []: Hello Beet
project_namespace [hello_beet]:
github_url: https://github.com/OrangeUtan/hello_beet
description []: My first Beet project
version [0.1.0]:
Select open_source_license:
1 - MIT license
2 - BSD license
3 - ISC license
4 - Apache Software License 2.0
5 - GNU General Public License v3
6 - Not open source
Choose from 1, 2, 3, 4, 5, 6 [1]: 1
minify_release [y]: y
```

### Install build tools
- [Invoke](http://www.pyinvoke.org/): `pip install invoke`<br>
- Poetry: https://python-poetry.org/docs/#installation

### Install dependencies
```
$ invoke install
```

### Project structure overview
```
hello_beet
├── datapack
|   └── data
|       ├── global
|       |   └── advancements
|       |       ├── oran9eutan.json
|       |       └── root.json
|       ├── minecraft
|       |   └── tags
|       |       └── functions
|       |           └── load.json
|       └── oran9eutan
|           ├── advancements
|           |   └── hello_beet
|           |       └── root.json
|           └── functions
|               └── hello_beet
|                   ├── load.mcfunction
|                   ├── install.mcfunction
|                   └── uninstall.mcfunction
|
├── resourcepack
|   ├── assets
|   |   └── .mcassetsroot
|   └── pack.png
├── beet-release.json
├── beet.json
├── LINCENSE
├── pyproject.toml
├── README.md
├── tasks.py
└── tbump.toml
```

## Features
- Preconfigured [Beet](https://github.com/mcbeet/beet) project
- Python dependency management with [Poetry](https://python-poetry.org/)
- Version bumping with [tbump](https://github.com/TankerHQ/tbump)
- Task execution using [Invoke](http://www.pyinvoke.org/) (Python Makefile equivalent)