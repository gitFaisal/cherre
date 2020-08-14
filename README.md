# cherre

Solution to challenge: 
1) Used Jupyter Notebook to get top ten frequest browsers, and then exported them in a csv file.<br>
2) Created a function to do the same task using Python3, in order to run by providing "testdb.db" as an argument<br>
                          for dataframe() function.<br> 
                       
                       
Extra things done:

1) Django Framework:<br> 
                    - Used Django to create models for FrequentBrowser data.<br>
                     - Used csv.DictReader to loop through the FrequentBrowser data and insert rows into Django model.<br>
                     - Used Django rest_framework to create API from model. <br>
                 
2) Docker Container:<br> - Created Dockerfile in project directory for app.<br>
                     - Created Dockerfile for nginx.<br>
                     - Configured docker-compose.yml to manage the two containers. <br>
                     
3) Hosted API on AWS:<br>< https://www.cherreapi.tk/ > <br>
                      - GitHub Repo: < https://github.com/gitFaisal/cherre2 ><br>
                      - Created an EC2 instance.<br>
                      - Connected to instance via SSH & ran docker container.(after updates/necessary downloads) <br>
                      - Created Security groups, SSL certificate, Load Balancer control web traffic + use SSL certificate for security,<br>
                        & target groups.<br> 

4) React deployed on github:<br> < https://gitfaisal.github.io/frequentbrowsers/ ><br>
                      - GitHub Repo: < https://github.com/gitFaisal/frequentbrowsers ><br>
                      - Used React.js to create a dynamic table to consume/display FrequentBrowers data from API>.<br>
                      - Deployed to GitHub pages.<br>
