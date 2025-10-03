# car price prediction MLOps

Clone the repository

```bash
clone the git repo
```

# Step create the template.py
 

# Steps for running configuration of the application 


### STEP 01 - Create a conda environment after opening the repository

```bash
python -m venv venvCar 
```

```bash
venvCar\Scripts\activate 
```

# update the pip if using python <= 3.10
python.exe -m pip install --upgrade pip

### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

### step 03 create the logger carsales/src/logging/__init__.py

### Step 04 update the carsales/src/unitls/common.py  (e.g. read_yaml and create_directories)


## Workflows to be used after the creation of the templates

1. Update config/config.yaml
2. Update schema.yaml (updation once)
3. Update params.yaml (updation once)
4. Update the src/carsales/entity/config_entity.py
5. Update the src/carsales/constants/__init__.py (updation once)
6. Update the src/carsales/config/configuration.py
6. Update the src/components (multiple py files with steps)
7. Update the src/pipeline (multiple py files with steps) 
8. Update the main.py
9. Update the app.py


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```


## Step - 3 MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub

[dagshub](https://dagshub.com/)

# setup on the model evaluation file
os.environ["MLFLOW_TRACKING_URI"]=""https://dagshub.com/adyaan1989/car_price_prediction_MLOps.mlflow""
os.environ["MLFLOW_TRACKING_USERNAME"]="adyaan1989"
os.environ["MLFLOW_TRACKING_PASSWORD"]="your-access-token-here"


Run this on the git Bash to export as env variables:

### Add the .env file
MLFLOW_TRACKING_USERNAME="username-here"
MLFLOW_TRACKING_PASSWORD="your-access-token-here"



# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	### Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	### Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 646491289758.dkr.ecr.us-east-1.amazonaws.com/mlcarsalesproject

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	### optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	### required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one

Save the URI: 646491289758.dkr.ecr.us-east-1.amazonaws.com/mlcarsalesproject
# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  646491289758.dkr.ecr.us-east-1.amazonaws.com 

    ECR_REPOSITORY_NAME = mlcarsalesproject



## About MLflow 
MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & tagging your model



