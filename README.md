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
