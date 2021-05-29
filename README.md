# Instagram-Datacrawling
Data Crawling and Analytics of Instagram Influencer


Implement a scraper to pull Instagram social media Influencers data from some of the brands they are tagged with.
For this demo, keep in your db some of the famous fashion brands(10-20) on instagram( Nykka, myntra etc).
To get the JSON, append https://www.instagram.com/santoshishetty/?__a=1 as a query parameter to any public account for the same.
Parse this JSON and extract the post text,bio, tags and from there find influencers tagged with @Influencer_name_,
and build it’s database using the same method as used for pulling brand data. The fields of influencers that need to be pulled are mentioned below.
At a time, there are 12 most recent posts per account that can be scraped, so do this scraping on these 12 posts only per brand.
Influencer name, IG link, Bio, Email ID( if present In bio, make a simple rule
using regex or something similar as *@*.[com,in,co,co.in]), followers, posts data( likes, comments, text, tagged array)


# url for datacrawling app

url = "datacrawling/"

Django App name: datacrawling

database: Nosql

engine: mongoengine

Database Schema(Document):

    Brand (name, bio, Post)
                        |
      __________________|
     | 
     |
    Post(message, tags[])
                     |
         ............|
         |
         |
    Influencer(ig_link, bio, email_id, followers, post)
                                                   |
      _____________________________________________|
     |
     |
    InfluencerPost(likes, message, tags[], Comment)
                                                |
       _________________________________________|
      |
      |
    Comment (username, comment)
    
    
#Influencer user_name can be get from below any method

But most of the time they teagged in text message only!

get influencer from text messages
tags = re.findall('@[\w\.-]+',message) // extract the text with @user_name

#OR

 get influencer from post tagged in
 tags = []
 for i in e['node']['edge_media_to_tagged_user']['edges']:
      tags.append(i['node']['user']['username'])
          
          
   biography = jsonData['graphql']['user']['biography']
          
   List of post we can get from this:
   
   e = jsonData['graphql']['user']['edge_owner_to_timeline_media']['edges']
   
   List of tags user_name:
   
   e['node']['edge_media_to_tagged_user']['edges']
          
          
          
          
          
       
     
    




