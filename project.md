Project:- Get Pull requests information on a github repo using python.
# you can say it is kubernetes project because kubernetes is open source product so lets say kubernetes project or your personal project

# now write alogrithm to perform this task ?
 
 - when you are writing a script by yourself you use API model...

 # Step1: - Install and  import request module ( talk to the github API)

 # Step2:- make the API call to access the pull request

 # step3:- convert JSON into dictionary(because python can't perfom directory)

 # Step4:- print the required thing 


# how to find the  API (url) for pull request-
 - Step1 : search Github api docs
  
  - step2: Then you have the rest api refrences

   - step3: now searching for pulls and click on them

   - step4: scroll and you find the URL in the List pull request section

- step5: url = "/repos/{owner}/{repo}/pulls" copy paste and start writing code.

- Step6: your api is look like  - response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls") #we are using kubernetes repo name we replace owner and project with kubernetes
