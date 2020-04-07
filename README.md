# Privacy Preserving Machine Learning using Fully Homomorphic Encryption
This repository includes the source code for learning Privacy Preserving Machine Learning using Fully Homomorphic Encryption process.
## Content
* [Introduction](#introduction)
* [Installation](#installation)
* [Project contents](#project-contents)
* [Acknowledments](#acknowledments)
* [Contact](#contact)

## Introduction
This repository uses [Pyfhel](https://github.com/ibarrond/Pyfhel) - a library for Fully Homomorphic Encrypion.
## Installation
**Importance Note:** This installation is for Linux only. 
For MacOS/ Windows, please take a look at the detailed instruction of each individual component.
* Python 3.5+ is required.

<h4>Ubuntu</h4>

**1. Clone project**

```sh
git clone https://github.com/kcsmta/PPML_FHE.git
```

**2. Run following command:**

```sh
# Create virtual enviroment
python venv ppml-fhe-env
# Active virtual enviroment
source ppml-fhe-env/bin/activate
# Install requirement packages
(venv) pip install -r requirements.txt
```

## Project contents 
`LinearRegression` contains the source code for Linear Regression using gradient descent method on data encrypted by the FHE scheme. 
File `customer.py` includes actions that take place on client side likes encrypt, decrypt data using the FHE scheme. 
File `server.py` includes actions that take place on the server side which is the calculation on encrypted data. 
In this way, the server can learn a linear regression model without directly accessing the data of the customer.

## Acknowledments
* [Pyfhel](https://github.com/ibarrond/Pyfhel): Python For Homomorphic Encryption Libraries

## Contact
Author: \
Khanh Duy Tung Nguyen: tungkhanh@lqdtu.edu.vn