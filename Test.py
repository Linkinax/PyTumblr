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
    f_memes_r = RedditBlog("gn1tWsZ5Wq3tyOdZbKoOLHrUhlYwAnXqDjEeLRtwjGuCu1LKh2",
                "vcIKu8qrHl8uguTgjkbGuwaQiVDajMfY3zi1u7AJXcUzlDVxiU",
                "dC00e6YQxlwWT37Lm8A8ZIx1VpwHoVcTbCAHlinpptluI6R8YT",
                "6gMoqbosWaQCfK1c56CPvCNmMyyFtZkZjKrDuUDNig4Bd10Vsw",
                "gn1tWsZ5Wq3tyOdZbKoOLHrUhlYwAnXqDjEeLRtwjGuCu1LKh2",
                "memesforages",
                "memes",
                ['meme', 'memes', 'funny', 'dank meme', 'funny picture'])
    f_memes_r.reblog_adv()
    
    """
    aww_r = RedditBlog("fIJI5esiBwbsttsdd6QhPSB4GvNXMlwzkSAq43efSH8ri9cpQ9",
                     "Z4ce5s0NCGsvBOYcW5TrLKYkrDjt0Qodd6XHBzuvnzA0PolBXi",
                     "2t4n2rLlGJTJs9gV1Cpw0zjM93Q6HZuNeOZgdYefNfLygNgmIB",
                     "3fuSivbp9sH4kjMtXgx7Pdxl96NiGaQgxSiE2TmDy68LQ2FSIW",
                     "fIJI5esiBwbsttsdd6QhPSB4GvNXMlwzkSAq43efSH8ri9cpQ9",
                     "awwsfordays",
                     "aww",
                     ['aww', 'cute', 'adorable', 'aww cute', 'lovely', 'baby animals', 'animals'])
    aww_r.posta()
    """
    
    """
    meme2_r = Poster("gn1tWsZ5Wq3tyOdZbKoOLHrUhlYwAnXqDjEeLRtwjGuCu1LKh2",
                     "vcIKu8qrHl8uguTgjkbGuwaQiVDajMfY3zi1u7AJXcUzlDVxiU",
                     "dC00e6YQxlwWT37Lm8A8ZIx1VpwHoVcTbCAHlinpptluI6R8YT",
                     "6gMoqbosWaQCfK1c56CPvCNmMyyFtZkZjKrDuUDNig4Bd10Vsw",
                     "gn1tWsZ5Wq3tyOdZbKoOLHrUhlYwAnXqDjEeLRtwjGuCu1LKh2",
                     "memesforages",
                     "memes",
                     ['meme', 'memes', 'funny', 'dank meme', 'funny picture'])
    
    meme2_r.posta()
    """
    
    
    """
    quiver_blog_reddit = RedditBlog_nsfw("959G3YpGSduRNYOLHDw9W6xqyPGEp35dVZu6o7lg6rUgEtjE1g",
                     "XpdwD17p1M5Tyv2BmZy16ZKsGpcDCVMSAExpT5dmHyFXKWlzVH",
                     "VAW7pf5SQYijETj4tmUcSy6EFjkdpRijbOeNXCrJsWZo4lz3Gd",
                     "ArBWerIgRoi5CUrZh4eEVfuJFSnBbuxBp9oYBEIF01vjRCrZj3",
                     "959G3YpGSduRNYOLHDw9W6xqyPGEp35dVZu6o7lg6rUgEtjE1g",
                     "demquivers",
                     "quiver",
                     ['o faces','nsfw', 'sexy',  'porn', 'sex', 'quiver', 'hot', 'hot gifs','girls coming', 'hot face', 'orgasm'])
    quiver_blog_reddit.posta()
    """
    
    """
    insertion_blog_reddit = RedditBlog_nsfw("8nyz3B0XZpHPdgrrk8ulz0kByKffv1nQZvsvxVQcnpkv3MNAc5",
                     "LTpUoSGI3CzGtXNSRzxK9IGYZCJja8V3ZdeRC3EjA1kHh0tdbI",
                     "5qSCLsccZpxt7JONJyGl4jGBb2W69dFzwPPLV2u0sf1uhyXv0P",
                     "yWmU9VLy8H4ZjYrKlB8DaPMBNfLwWfFZi4IxGBLqMeS0PArOAU",
                     "8nyz3B0XZpHPdgrrk8ulz0kByKffv1nQZvsvxVQcnpkv3MNAc5",
                     "whenitgoesinlove",
                     "whenitgoesin",
                     ['girl faces','nsfw', 'sexy',  'porn', 'sex', 'o face', 'hot', 'hot gifs','penetration', 'omg face', 'omg hot', 'hot face', 'orgasm'])
    insertion_blog_reddit.posta()
    """
        
    print("Finito tutto, gg wp!")
    pass
