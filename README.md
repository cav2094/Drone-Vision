# Drone-Vision : Autonomous Object Detection on Low-Cost Drones with PyTorch


## Description:
This project showcases a computer vision pipeline for real-time object detection on low-cost drones using PyTorch. Designed to make aerial data collection accessible and efficient, the project enables drones to autonomously recognize and track specific objects or features in various environments. The implementation leverages deep learning, optimized for resource-constrained devices, and demonstrates end-to-end deployment on drones with minimal computational power.

## Key Features:

* Lightweight Model Architecture: Customized CNNs for fast inference on low-cost hardware.
* Real-Time Object Detection: Object recognition and tracking through efficient frame-by-frame processing.
* Optimized with PyTorch: Employing PyTorch for flexible, efficient model training and deployment.
* Cost-Effective Hardware Integration: Built for budget-friendly, widely available drones, enabling scalable field applications.
* This project is ideal for developers, researchers, and enthusiasts looking to explore drone-based computer vision with limited budgets and resources. It can be adapted for applications in environmental monitoring, agricultural surveys, and autonomous navigation systems.

## Example of MNIST Data-set
![IMAGE ALT TEXT HERE](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/MNIST_dataset_example.png/640px-MNIST_dataset_example.png) 


## Getting Started

To set up your python environment to run the code in this repository, follow the instructions below.

1. Create (and activate) a new environment with Python 3.8.

- __Linux__ or __Mac__: 
	```bash
	conda create --name Drone-Vision python=3.8
	conda activate Drone-Vision
	conda env config vars list
	```

2. Clone the repository (if you haven't already!), and navigate to the `python/` folder.  Then, install several dependencies.
	```bash
	git clone https://github.com/cav2094/Drone-Vision.git
	cd Drone-Vision
	```
3. Install required packages:
- __Linux__ or __Mac__: 
	```bash
  pip install djitellopy
  pip install opencv-python
  conda install pytorch torchvision -c pytorch
  pip install ultralytics
	```


