## Prompt Engineering
This code works through the two examples from XX paper showcasing the differences in prompt engineering strategies.

## Downloading Python
This code was built using Python 3.13.0
If you need to install Python, navigate to https://www.python.org/downloads/

## Installing the Required Packages
The required packages are included in requirements.txt. Two options for installing these packages are documented here (1) local installation and (2) virtual environment
### Local Installation
From terminal run the following:
```
# change the working directory to the location of the requirements.txt file
cd "insert/path/here/requirements.txt"

# install the packages contained in the file
pip3 install -r requirements.txt
```
### Virtual Environment
To set up a virtual environment from VS Code open the command palette (⇧⌘P or View > Command Palette) and search for Python: Create Environment, select Venv, select Python 3.13.0 and when prompted, check the box for requirements.txt. More information can be found here: https://code.visualstudio.com/docs/python/environments


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
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama

# download and run a model in the container
docker exec -it ollama ollama run llama3.2
```

To check that this worked, use an internet browser and navigate to localhost:11434