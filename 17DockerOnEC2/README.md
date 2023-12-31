* create a file named Dockerfile in your project. This file will contain the steps of building the docker image.
  
* Setup docker on cloudshell using the following commands:
  * sudo amazon-linux-extras install docker # install docker
  * sudo nohup dockerd &    # start the docker daemon
    
* Now, to build the following steps needs to be executed on your local machine or via the AWS Cloud Shell.
  * git clone  https://github.com/gaurav157243/aws-project.git  # clone the repo
  * sudo docker build -t webapp .                               # create a docker image for the spring boot application
  
* Create a AWS ECR repository using the AWS UI. This repository is used for sharing or downloading the docker image.
  
* Now, lets push the image to the newly created ECR repository

  aws ecr get-login-password --region us-east-1 | sudo docker login --username AWS --password-stdin 665178635794.dkr.ecr.us-east-1.amazonaws.com </br>
  sudo docker tag webapp:latest 665178635794.dkr.ecr.us-east-1.amazonaws.com/webapp:latest </br>
  sudo docker push 665178635794.dkr.ecr.us-east-1.amazonaws.com/webapp:latest </br>

* Now, lets run this docker image on an EC2 instance
  * First, we will need to create a IAM role with AmazonEC2ContainerRegistryFullAccess permissions
  * Then run the following commands to install docker and run the container </br>
  sudo dnf install -y docker </br>
  sudo systemctl start docker  </br>
  sudo systemctl enable docker </br>
  aws ecr get-login-password --region us-east-1 | sudo docker login --username AWS --password-stdin 665178635794.dkr.ecr.us-east-1.amazonaws.com </br>
  sudo docker run --publish 80:80 665178635794.dkr.ecr.us-east-1.amazonaws.com/webapp:latest </br>

* For testing, make a GET api call from the browser to verify that we are getting a response </br>
http://ec2-ip/api/v1/employees
  



  
