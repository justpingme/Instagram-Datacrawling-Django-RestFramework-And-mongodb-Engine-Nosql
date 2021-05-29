
from datacrawling.serializers import BrandSerializer
from django.shortcuts import render
import requests
import json
import re
import os
from django.conf import settings
# Create your views here.


def index(request):
    
    if request.method == "GET":

        # get json Data for 'santoshysetty' brand
        jsonData = getJsonFile()

        # insert json data to model Brand using 'BrandSerializer'
        message = insertBrand(jsonData)

        context = {
            'message':message
        }
        return render(request, "datacrawling/index.html", context)


def getJsonFile():
    pfile = os.path.join(settings.BASE_DIR, 'santoshishetty.json')
    print (os.getcwd())
    with open(pfile,'r') as jsonFile:
        jsonData = json.load(jsonFile)
        jsonFile.close()
    return jsonData


def insertBrand(jsonData):

    # get post from brand username
    post = getPost(jsonData)

    # json data for "Brand model"
    result = {
    "name": jsonData['graphql']['user']['full_name'],
    "bio": jsonData['graphql']['user']['biography'],
    "post": post
    }

    data_serializer = BrandSerializer(data = result)

    if data_serializer.is_valid():

        # COMMIT to database
        data_serializer.save()

        return "Model 'Brand' Inserted"

    else:
        return data_serializer.errors


def getPost(jsonData):
    post = []

    for e in jsonData['graphql']['user']['edge_owner_to_timeline_media']['edges']:
        
        message =  e['node']['edge_media_to_caption']['edges'][0]['node']['text']
        
        # get influencer from text messages
        # tags = re.findall('@[\w\.-]+',message)
        
        tags = []

        # get influencer from post tagged in
        for i in e['node']['edge_media_to_tagged_user']['edges']:
            tags.append(i['node']['user']['username'])

        # single Brand Post json Data for "Post model"
        sPost = {
            'message': message,
            'tags': tags
        }

        # adding post to post list
        post.append(sPost)

    return post




def getJsonData(username):
    base_url = "https://www.instagram.com/"
    api_code = "/?__a=1"
    url = base_url+username+api_code

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
   
    response = requests.get(url,headers=headers)
    try:
        data = response.json()
    except:
        print("no json data found")
        data = {
            
        }
    return data

def insertData():
    data = getJsonData('santoshishetty')
    


