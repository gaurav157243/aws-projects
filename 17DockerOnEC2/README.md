* create a file named Dockerfile in your project. This file will contain the steps of building the docker image.
  
* Setup docker on cloudshell using the following commands:
  * sudo amazon-linux-extras install docker # install docker
  * sudo nohup dockerd &    # start the docker daemon
    
* Now, to build the following steps needs to be executed on your local machine or via the AWS Cloud Shell.
  * git clone  https://github.com/gaurav157243/aws-project.git  # clone the repo
  * sudo docker build -t webapp .                               # create a docker image for the spring boot application
  * sudo docker run -p 80:80 -d webapp                          # run the docker image
    
  Test the applciaton using the below command 
  * curl -X POST -d '{ "firstName" : "Sachin" , "Tendulkar" : "Agrawal", "emailId" : "st@gmail.com" }' http://localhost:80/api/v1/employees -H"Content-Type:application/json"
 
* Create a AWS ECR repository using the AWS UI. This repository is used for sharing or downloading the docker image.
  
* Now, lets push the image to the newly created ECR repository

  aws ecr get-login-password --region us-east-1 | sudo docker login --username AWS --password-stdin 665178635794.dkr.ecr.us-east-1.amazonaws.com </br>
  docker tag webapp:latest 665178635794.dkr.ecr.us-east-1.amazonaws.com/webapp:latest </br>
  docker push 665178635794.dkr.ecr.us-east-1.amazonaws.com/webapp:latest </br>


  
