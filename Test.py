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




#reload(sys)
#sys.setdefaultencoding("utf8")


if __name__ == '__main__':
    print (" TEST --->Working in progress<---..")
    
    
    """
    memes_pages= [ "memes"]#, 'deepfriedmemes', 'dankmemes']#funny
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
    
    """
    aww_r = RedditBlog("fIJI5esiBwbsttsdd6QhPSB4GvNXMlwzkSAq43efSH8ri9cpQ9",
                     "Z4ce5s0NCGsvBOYcW5TrLKYkrDjt0Qodd6XHBzuvnzA0PolBXi",
                     "i0YJqjj5plA4GN906vuirucDdLFO1uief2jKPbDVQAB6oiwzFd",
                     "4uqPSXZHaz15WuSK03lETB8QLUhqf9LvqZhjvetwIKPNSRXG0D",
                     "fIJI5esiBwbsttsdd6QhPSB4GvNXMlwzkSAq43efSH8ri9cpQ9",
                     "awwsfordays",
                     "aww",
                     ['aww', 'cute', 'adorable', 'aww cute', 'lovely'])
    aww_r.posta()
    
    """
    """
    programmingHumour_r = RedditBlog("UqBfts94LerDmvzD3kzVLO8bEFLk3cnMUyWJVixgtSQ6lJnJgs",
                                     "j5awYsaeIJLFRsp5Xa8HLw3NTRkIu0hOkabnxRMXrJRU2Nl7v9",
                                     "0E0OgPbLtfzCN3yXPD8ZKho6tU0GFfq16zM9twCsYCVhK2iOzC",
                                     "SOsRkfhgmMLr2rHSQUzEEjFCWhKMC3ZJ9pof62XbDMurAVECKN",
                                     "UqBfts94LerDmvzD3kzVLO8bEFLk3cnMUyWJVixgtSQ6lJnJgs",
                                     "programminghumour",
                                     "ProgrammerHumor",
                                     ['funny', 'programming', 'humour', 'programming humour'])
    programmingHumour_r.posta()
    """
    
    
    #like_ig()
    #affiliate_marketing("https://azaazafightng.tumblr.com/tagged/14871q7")

    """
    for i in range(3,8):
        affiliate_marketing("https://bigbig8899.tumblr.com/tagged/14871m" + str(i))
      """  
    pageAM("https://ourloudsongcollection.tumblr.com/tagged/14871L1", 8)
    #follow_ig()
    #unfollow_ig()
    #insta_account()
    print("Finito tutto, gg wp!")
    pass
