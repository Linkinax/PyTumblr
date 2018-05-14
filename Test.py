# coding=utf8
'''
Created on 27 mar 2016

@author: linky
'''
import os
import sys
from Poster import *
from Poster import RedditPoster
from time import sleep
import sys
from Poster.RedditPoster import RedditBlog
from Poster.RedditPoster import RedditBlog_nsfw
from Poster.Poster import Poster
from Poster.QuotesRedditBlog import Quotes
from bs4 import BeautifulSoup
from selenium import webdriver
from Poster.Funzioni_PyTumblr import *
from Funzioni_PyTumblr import get_titoli_from_new_reddit, get_quotes, like_ig,\
    affiliate_marketing, blondie, follow_ig, insta_account, blondie_2



#reload(sys)
#sys.setdefaultencoding("utf8")


if __name__ == '__main__':
    print (" TEST --->Working in progress<---..")
    
    """
    memes_pages= ["funny", "memes", 'deepfriedmemes', 'dankmemes'] 
    for query in memes_pages:
        f_memes_r = RedditBlog("gn1tWsZ5Wq3tyOdZbKoOLHrUhlYwAnXqDjEeLRtwjGuCu1LKh2",
                "vcIKu8qrHl8uguTgjkbGuwaQiVDajMfY3zi1u7AJXcUzlDVxiU",
                "dC00e6YQxlwWT37Lm8A8ZIx1VpwHoVcTbCAHlinpptluI6R8YT",
                "6gMoqbosWaQCfK1c56CPvCNmMyyFtZkZjKrDuUDNig4Bd10Vsw",
                "gn1tWsZ5Wq3tyOdZbKoOLHrUhlYwAnXqDjEeLRtwjGuCu1LKh2",
                "memesforages",
                query,
                ['meme', 'memes', 'funny', 'dank meme', 'funny picture'])
        f_memes_r.posta()
    """
    
    #like_ig()
    affiliate_marketing("https://dior9999.tumblr.com/tagged/14871i2")
    #follow_ig()
    #unfollow_ig()
    #insta_account()
    print("Finito tutto, gg wp!")
    pass
