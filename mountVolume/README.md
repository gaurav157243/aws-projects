- sudo lsblk
- sudo file -s /dev/xvdf <br>
/dev/xvdf: data  (this means that there is no filesystem on the device)
- sudo mkfs -t xfs /dev/xvdf
- sudo mkdir /data
- sudo mount /dev/xvdf /data
- sudo blkid

- sudo vim /etc/fstab <br>
UUID=eb603571-4824-424f-b996-684262422a2a  /data  xfs  defaults,nofail  0  2

- sudo df -h (command to see the filesystem and the size.)

Reference AWS page - https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-using-volumes.html
