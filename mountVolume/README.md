* create a new EC2 instance with ssh port allowed. Connect and run the below command to see the list of devices attached to the instance. Normally a root volume will be present
- sudo su lsblk

* create a new EBS volume of 1 GB in the same AZ as of EC2 instance
* Attach the volume to the EC2 instance
* Run the "lsblk" command again on the EC2 instance and you will see a new device attached.
* Use the file -s command to get information about a specific device, such as its file system type. If the output shows simply data, as in the following example output, there is no file system on the device
[ec2-user ~]$ sudo file -s /dev/xvdf
/dev/xvdf: data

If the device has a file system, the command shows information about the file system type. For example, the following output shows a root device with the XFS file system.
[ec2-user ~]$ sudo file -s /dev/xvda1
/dev/xvda1: SGI XFS filesystem data (blksz 4096, inosz 512, v2 dirs)

* Now create a filesystem on that volume using:
- sudo mkfs -t xfs /dev/xvdf

XFS is a highly scalable, high-performance file system which was originally designed at Silicon Graphics, Inc. XFS is the default file system for Red Hat Enterprise Linux 7.

* create a directory - sudo mkdir /data

* Mount the volume or partition at the mount point directory you created in the previous step.

sudo mount /dev/xvdf /data


*the  Use the blkid command to find the UUID of the device. Make a note of the UUID of the device that you want to mount after reboot. You'll need it in the following step.

[ec2-user ~]$ sudo blkid
/dev/xvda1: LABEL="/" UUID="ca774df7-756d-4261-a3f1-76038323e572" TYPE="xfs" PARTLABEL="Linux" PARTUUID="02dcd367-e87c-4f2e-9a72-a3cf8f299c10"
/dev/xvdf: UUID="aebf131c-6957-451e-8d34-ec978d9581ae" TYPE="xfs"

[ec2-user ~]$ sudo vim /etc/fstab
Add the following entry to /etc/fstab to mount the device at the specified mount point. The fields are the UUID value returned by blkid (or lsblk for Ubuntu 18.04), the mount point, the file system, and the recommended file system mount options. For more information about the required fields, run man fstab to open the fstab manual.

In the following example, we mount the device with UUID aebf131c-6957-451e-8d34-ec978d9581ae to mount point /data and we use the xfs file system. We also use the defaults and nofail flags. We specify 0 to prevent the file system from being dumped, and we specify 2 to indicate that it is a non-root device.

UUID=eb603571-4824-424f-b996-684262422a2a  /data  xfs  defaults,nofail  0  2

* use the df -h command to see the filesystem and the size.

Reference AWS page - https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-using-volumes.html
