* Create a S3 bucket and upload the airports-data.csv file in the bucket. Also create a folder to store the athena query results.
* In Athena, configure the query results s3 bucket under the settings tab
* In Athena, create a new table and provide the details of the database and table. In the table properties, add this property to skip the first row - skip.header.line.count" = 1
* Add the required columns in the table and create the table
* run the query to select the items - select * from airporttable limit 1

