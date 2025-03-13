# Prompt Engineering Paper
This repository showcases two examples from Anglin et al. (In Progress) showcasing the differences in prompt engineering strategies across the examples.

## Downloading Python
This code was built using Python 3.13.0.
If you need to install Python, navigate to https://www.python.org/downloads/

## Installing the Required Packages
The required packages are included in requirements.txt. Two options for installing these packages are documented here (1) local installation and (2) virtual environment
### (1) Local Installation
From terminal run the following:
```
# change your current directory to the location of the requirements.txt file
cd "insert/path/here/requirements.txt"

# install the packages contained in the file
pip3 install -r requirements.txt
```
### (2) Virtual Environment
To set up a virtual environment from VS Code:
- open the Command Palette (⇧⌘P or View > Command Palette),
- search for Python: Create Environment,
- select Venv, select Python 3.13.0 and when prompted, 
- check the box for requirements.txt

<br />More information can be found here: https://code.visualstudio.com/docs/python/environments


## Running the Ollama Docker Container
If you do not have an account with docker, sign up at https://www.docker.com

To pull and run a docker container, run the following commands in terminal:
```
docker login

# pull the published ollama image from the docker repo
docker pull ollama/ollama:latest # docker

# run the docker container
# -d = run container in background
# -v = bind mount volume
# -p = publish containers ports to the host
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama_image ollama/ollama:latest

# download and run a model in the container
docker exec -it ollama_image ollama run llama3.2
```

To check that this worked, use an internet browser and navigate to localhost:11434 where it should read, "Ollama is running."