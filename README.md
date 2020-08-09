# cherre

Solution to challenge: 
1) Used Jupyter Notebook to get top ten frequest browsers, and then exported them in a csv file.<br>
2) Created a function to do the same task using Python3, in order to run by providing "testdb.db" as an argument<br>
                          for dataframe() function.<br> 
                       
                       
Extra things done:

1) Django Framework: - Used Django to create models for FrequentBrowser data.
                     - Used csv.DictReader to loop through the FrequentBrowser data and insert rows into Django model.
                     - Used Django rest_framework to create API from model. 
                 
2) Docker Container: - Created Dockerfile in project directory for app.
                     - Created Dockerfile for nginx.
                     - Configured docker-compose.yml to manage the two containers. 
                     
3) Hosted API on AWS: < https://www.cherreapi.tk/ > 
                      - GitHub Repo: < https://github.com/gitFaisal/cherre2 >
                      - Created an EC2 instance.
                      - Connected to instance via SSH & ran docker container.(after updates/necessary downloads) 
                      - Created Security groups, SSL certificate, Load Balancer control web traffic + use SSL certificate for security,
                        & target groups. 

4) React deployed on github: < https://gitfaisal.github.io/frequentbrowsers/ >
                      - GitHub Repo: < https://github.com/gitFaisal/frequentbrowsers >
                      - Used React.js to create a dynamic table to consume/display FrequentBrowers data from < www.cherreapi.tk >.
                      - Deployed to GitHub pages.
