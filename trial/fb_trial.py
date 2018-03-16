import requests as rq;
import json as jsonobj
from db import populate

graphApiPath="HTTPS://graph.facebook.com/v2.12/"
token = "EAACEdEose0cBAO70ymMwvUjDuhtU9CMiDUfOijDwkCD5FjwSvBEDfYIWs7N8dKA5D0ZCbyGtCbkwYdnabMW6rNWpMkBL52WLiv8DU8iL4rZBbhszIXmxbZAVPZC0MTQpyUxO7dofVkzPwZB8BX8CDo6lOwbJn9ZCsLgU0tp7ZBHKz6z1DTA4qba66g81bc6sWDyWtEZBuKtPawZDZD"
bearer_token = 'Bearer ' + token
header = {'Authorization': bearer_token}

def loadData(path):
    r=rq.get(graphApiPath+"?id="+path,headers=header);
    print(r.text)
    page_id=jsonobj.loads(r.text)["id"];
    get_posts(header,page_id)

#fetch the data using graph api
def get_posts(header,page_id) :
    r=rq.get(graphApiPath+page_id+"?fields=name,id,fan_count,talking_about_count",headers=header)
    json_data=jsonobj.loads(r.text)
    print(json_data);
    populate(json_data)


"""This function gets the details of a perticular post 
 from facebook by sending authentication token with get request """
def get_post_details(header,post_id):
    r=rq.get("HTTPS://graph.facebook.com/v2.12/"
             +post_id+"?fields=name,id",headers=header)
    print (r.text)
