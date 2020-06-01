# Public-APIs-List-Crawler

a. Steps to run code.
  
   Using Docker:
   
   	1) Open Command Prompt
	
	2) Enter "git clone https://github.com/sudhan247/Public-APIs-List-Crawler.git"(This will download the contents from git)
	
	3) Enter "cd Public-APIs-List-Crawler"(Move to the respective directory)
	
	4) Enter "docker-compose up"(This will build up the things and it takes roughly 20 minutes to retrieve the data)
	
	5) Then all API entries will be retrieved from the table.
	
   Using Windows:
    
        
	1) Install python and requirements.txt
	
	2) Install postgresql compatible with python version.
	
	3) Change the postman.py engine=create_engine('postgresql://user:pass@localhost',echo=True)
	
b. Details of all the tables and their schema.
    
    	
	| Column | Description |
	| --- | --- |
	| API | TEXT |
	| Description | TEXT |
	| Auth | TEXT |
	| HTTPS | BOOLEAN |
	| Cors | TEXT |
	| Link | TEXT |
	| Category | TEXT |
	
	
    CREATE TABLE sudhan_postmanapi (
	"API" TEXT, 
	"Description" TEXT, 
	"Auth" TEXT, 
	"HTTPS" BOOLEAN, 
	"Cors" TEXT, 
	"Link" TEXT, 
	"Category" TEXT
    )

c. What is done from “Points to achieve” and number of entries in your table

    1)Supports the concepts of OOPS.
    
    2)Support for handling authentication requirements & token expiration of server.
    
    3)Support for pagination to get all data.
    
    4)Support for rate limitation.
    
    5)All API entries for all categories are stored in a database.
    
    Number of entries in table: 524
d. What is not done from “Points to achieve”. If not achieved write the possible reasons and current workarounds.
     
     All features in Points to achieve are achieved in my code.

e. What would you improve if given more days
    
     I will improve my code to resolve network errors and improve the time efficiency of my code.
