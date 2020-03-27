# Shopping-Cart Project 
Hello Welcome to my shopping-cart project. In this program, you will input a product identifiers(1-20) corresponding to a certain grocery item. Once you input your identifiers, enter "done"(case does not matter) to print out an itemized receipt with a subtotal, tax, and final total.

## Prerequisites

  + Anaconda 3.7
  + Python 3.7
  + Pip

## Setup

### Repo-Setup
Use the GitHub.com online interface to create a new remote project repository called something like "shopping-cart". When prompted by the GitHub.com online interface, let's get in the habit of adding a "README.md" file and a Python-flavored ".gitignore" file (and also optionally a "LICENSE") during the repo creation process. After this process is complete, you should be able to view the repo on GitHub.com at an address like `https://github.com/YOUR_USERNAME/shopping-cart`.

After creating the remote repo, use GitHub Desktop software or the command-line to download or "clone" it onto your computer. Choose a familiar download location like the Desktop.

After cloning the repo, navigate there from the command-line:

```sh
cd ~/Desktop/shopping-cart
```
### Environment Setup
Use Anaconda to create and activate a new virtual environment, perhaps called "shopping-env":

```sh
conda create -n shopping-env python=3.7 # (first time only)
conda activate shopping-env
```
### Installation of Packages
From inside the virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```

> NOTE: if this command throws an error like "Could not open requirements file: [Errno 2] No such file or directory", make sure you are running it from the repository's root directory, where the requirements.txt file exists (see the initial `cd` step above)

## Running the program

From within the virtual environment, demonstrate your ability to run the Python script from the command-line:

```sh
python app/shopping-cart.py
```

## Testing Capabilities

### Testing with Pytest Package
After installing your package dependencies through requirments.txt, you are able to use the "pytest" package. By entering the command below, you are able to run the tests inputted in the file located at Test/my_test.py

```sh
pytest
```

### Automatic Testing with Travis-CI and Code Climate

Travis-CI: Code is compatible with Travis-CI to run tests to see if fundamental program functions are working properly.

Code Climate: Code can be used with Code Climate to check coding syntax and style
