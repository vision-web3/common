<img src="https://raw.githubusercontent.com/vision-web3/common/img/vision-logo.png" alt="Vision-web3 logo" align="right" width="120" />

[![CI](https://github.com/vision-web3/common/actions/workflows/ci.yaml/badge.svg?branch=main)](https://github.com/vision-web3/common/actions/workflows/ci.yaml) 
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=vision-web3_common&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=vision-web3_common)

# Common code for Vision-web3 off-chain components

## 1. Introduction

### 1.1 Overview

Welcome to the documentation for Vision-web3 Common. This repository is a centralized hub for storing shared code components used across multiple projects within our organization.

The primary purpose of the Common Repository is to promote code reusability, streamline collaboration, and maintain consistency across various projects. Centralizing shared code aims to enhance efficiency and reduce redundancy in our development processes.

### 1.2 Features

The Vision Common project currently offers the following functionalities:

#### Signing module
The **signer.py** module is used for signing and verifying signatures. The private key must be on the curve Ed25519 or Ed448 and encrypted in a PEM file.

#### Service nodes module
The **servicenodes.py** module is used for communicating with Vision-web3 service nodes. It can be used for querying the bids, sending transfers, and requesting the transfer status.

#### Blockchain utility modules
The blockchain utility modules extract common blockchain functionalities used across projects. Such functionalities include sending transactions or calling the blockchain nodes for read-only data.

The blockchain utility modules can be found in the **blockchains** package. There is a Python module for each Vision-web3-supported blockchain.

## 2. Installation

### 2.1  Prerequisites

Please make sure that your environment meets the following requirements:

#### Python Version

Vision-web3 Common supports **Python 3.13** or higher. Ensure that you have the correct Python version installed before the installation steps. You can download the latest version of Python from the official [Python website](https://www.python.org/downloads/).

#### Library Versions

The Vision-web3 Common project has been tested with the library versions specified in **poetry.lock**.

#### Poetry

Poetry is our tool of choice for dependency management and packaging.

Installing: 
https://python-poetry.org/docs/#installing-with-the-official-installer
or
https://python-poetry.org/docs/#installing-with-pipx

By default poetry creates the venv directory under under ```{cache-dir}/virtualenvs```. If you opt for creating the virtualenv inside the project’s root directory, execute the following command:
```bash
poetry config virtualenvs.in-project true
```

### 2.2  Installation Steps

#### From Pypi

```bash
$ pip install vision-common
```

#### From source code

Create the virtual environment and install the dependencies:

```bash
$ poetry install --no-root
```

## 3. Usage

The Vision-web3 Common project should be used as a utility library, for example as a submodule in an upstream project. After those steps, the modules can be imported directly from the Common library.

### 3.1 Configuration

The Vision-web3 Common library allows its configuration to be loaded from multiple predefined folders. This normally involves an environment file and a base YAML configuration file, which can be located in the following predefined paths:

```
    $PWD
    $HOME
    ~/.config
    /etc/vision
    /etc
```

Each service defines a default file name under which this file is searched. The service then expects the environment file to be present in the same location with the same name but with a different .env extension.

Alternatively one can define the location of such files by using the `VISION-WEB3_CONFIG` and `VISION-WEB3_ENV_FILE` environment variables.

### 3.2 Examples

https://github.com/vision-web3/client-library/blob/main/vision/client/library/blockchains/base.py
