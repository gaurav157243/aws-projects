## Configure EC2 to send application logs to Cloudwatch log groups

* Create a new IAM role, select EC2 Service and this policy  - CloudWatchAgentServerPolicy

* Create a EC2 instance, allow ssh port and attach the above IAM role to the instance.

* Install java <br>
sudo yum -y install java-1.8.0

* Download the spring application jar file <br>
sudo wget https://raw.githubusercontent.com/gaurav157243/aws-project/master/springboot-backend/springboot-backend.jar

* Start the application in background and redirect the output to a file <br>
sudo nohup java -jar springboot-backend.jar > /tmp/myapp.log 2> /tmp/myapp.log &

* Install the cloudwatch agent using the following command: <br>
sudo yum install amazon-cloudwatch-agent

* Configure the cloudwatch agent using the following command. Specify the location of the myapp.log (/tmp/myapp.log) file during configuration. <br>
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-config-wizard

* Starting the cloudwatch agent; use the config file returned from the above command:<br>
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -s -c file:/opt/aws/amazon-cloudwatch-agent/bin/config.json

* Check status:<br>
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -m ec2 -a status

* Check Cloudwatch -> Log groups and search for myapp.log and you will see your applications log.<br>
