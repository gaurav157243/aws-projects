* Create a new IAM role, select EC2 Service and this policy  - CloudWatchAgentServerPolicy

* Create a EC2 instance, allow ssh port and attach the above IAM role to the instance.
 
* Install the cloudwatch agent using the following command:
sudo yum install amazon-cloudwatch-agent

* Configure the cloudwatch agent using the following command. It will return the config file name.
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-config-wizard

* Starting the cloudwatch agent; use the config file returned from the above command:
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -s -c file:/opt/aws/amazon-cloudwatch-agent/bin/config.json

* Check status:
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -m ec2 -a status
