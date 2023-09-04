
# run the following command to install postgres database
sudo dnf update  
sudo dnf install -y postgresql15.x86_64 postgresql15-server  
sudo postgresql-setup --initdb  
sudo systemctl start postgresql  
sudo systemctl enable postgresql  
sudo systemctl status postgresql  

Normally the postgres database is not listenin for requests from outside, to enable that:  

# take a backup of the below file
sudo cp /var/lib/pgsql/data/postgresql.conf /var/lib/pgsql/data/postgresql.conf.bak

# modify the file to accept connections from anywhere.
sudo vi /var/lib/pgsql/data/postgresql.conf
# change the following in the above file
# press /listen to search for the "listen" work
# press x to delete a character in vi; you will need to press x muliptle times
# press i to start inserting characters
listen_addresses = '*'  

# now change the password of the postgres user 
sudo passwd postgres

# Login using Postgres system account-
su - postgres

# Now, change the database postgres password
psql -c "ALTER USER postgres WITH PASSWORD 'postgres';"

# exit from this user
exit

# modify the following file to allow remote connections
sudo vi /var/lib/pgsql/data/pg_hba.conf

# press x  to delete a single character
# press i to start inserting characters
#host    all             all             127.0.0.1/32            ident
host    all             all             0.0.0.0/0           md5 

# restart the database
sudo systemctl restart postgresql
