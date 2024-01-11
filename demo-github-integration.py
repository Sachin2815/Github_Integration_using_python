# install requests package "pip install requests"
import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls") #we are using kubernetes repo name in place of owner and project replace kubernetes

#print(response)
#print(response.json() 

#print(response.status_code)

complete_detail = response.json()
for i in range(len(complete_detail)): 

    print(complete_detail[i] ["user"]["login"]) #they give the all users name
