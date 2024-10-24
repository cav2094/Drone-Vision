# Drones & AI
Experiments with low costs drones and AI control

## Project Details

Simple drone experiments including:
* take off and video using threads : flying_video.py
* take off and video using threads with ML (face detection) : flying_face_recognition.py


## Getting Started

To set up your python environment to run the code in this repository, follow the instructions below.

1. Create (and activate) a new environment with Python 3.8.

- __Linux__ or __Mac__: 
	```bash
	conda create --name drone-ai python=3.8
	conda activate drone-ai
	conda env config vars list
	```

2. Clone the repository (if you haven't already!), and navigate to the `python/` folder.  Then, install several dependencies.
	```bash
	git clone https://github.com/bohoro/drone-ai.git
	cd drone-ai
	```
3. Install required packages:
- __Linux__ or __Mac__: 
	```bash
	pip install djitellopy
    pip install opencv-python
	conda install pytorch torchvision -c pytorch
	pip install ultralytics
	```

# Instructions

<TBD>

