Create a security group and allow SSH (20), HTTP(80) and port 8080.
Create an EC2 instance with this security group
Connect to the EC2 instace using EC2 Instance Connect and change the user from "ec2-user" to "root" user.
Run the following commands:
* yum install -y httpd  # this command will install the http server by downloading from internet
* systemctl start httpd # this command will start the http server

Open a new browser tab and connect to the web server using the public ip address - http://<public ip address>

By default, the http server runs on port 80. To change the port, use the following commands:

* vi /etc/httpd/conf/httpd.conf
* search for line that starts with "Listen" 
* change the port from 80 to something like 8080, save the file by pressing [Esc] key and then  ":wq"
* restart the http server using command - systemctl restart httpd 

Now connect to the http server from the browser using - http://<public ip address>:8080

You should see an output - "It works!"
