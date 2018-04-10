#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 27 mar 2016

@author: linky
'''

from Poster.Poster import  *
from Poster import RedditPoster
from time import sleep
import sys;
from Poster.RedditPoster import RedditBlog
from Poster.RedditPoster import RedditBlog_nsfw


#reload(sys);
#sys.setdefaultencoding("utf8")

if __name__ == '__main__':
    print ("working in progress...")


    #blogs= []
    blogs_reddit = []
    blogs_tumblr = []
    
    """
    o_blog_reddit = RedditBlog_nsfw("KjaEoe3jouUeY7JVNfLFdn7E7j30PQHA4k7xEQkfwIZshW7Fks",
                     "V1CLajKKP3WLX85P8K5edGgAKG34b415NEjzfNnOdXNAStJs7T",
                     "XolkTiGTOoVICsbazTSdZUBaCgQqDhSGSN0Kun9SmvvZTTJb3q",
                     "Z481e1liYFBExcisooULErglvMUjr2jouMUyB7CivjknSMzEeG",
                     "KjaEoe3jouUeY7JVNfLFdn7E7j30PQHA4k7xEQkfwIZshW7Fks",
                     "omgoface",
                     "o_faces",
                     ['o faces','nsfw', 'sexy',  'porn', 'sex', 'o face', 'hot', 'hot gifs','girls coming', 'omg face', 'omg hot', 'hot face', 'orgasm'])
    """
    
    
    cars_blog = Poster("s5ThrrONDBVMSqeeRXZZKfnc0YcoSeccbmE1o3asg5HlV1zZPe",
                     "hO27aURuoEPPAcmWTpIK8C6msBEm7t4ImsI7DfqnANhR85FH0f",
                     "69tajnyEkLjNN18azr8f1qvCrMEG51lRDMZpLBmorcqPAI0Tfl",
                     "ZaPn5wnJhJdltSw6jPqtAHXlFQBzmXg0Jekr8W63Q9be3KP6Jw",
                     "s5ThrrONDBVMSqeeRXZZKfnc0YcoSeccbmE1o3asg5HlV1zZPe",
                     "carsparadise",
                     "luxury cars",
                     ['cars', 'cool cars', 'luxury cars', 'auto', 'wow cars']
                       )
    cars_blog_r = RedditBlog("s5ThrrONDBVMSqeeRXZZKfnc0YcoSeccbmE1o3asg5HlV1zZPe",
                     "hO27aURuoEPPAcmWTpIK8C6msBEm7t4ImsI7DfqnANhR85FH0f",
                     "69tajnyEkLjNN18azr8f1qvCrMEG51lRDMZpLBmorcqPAI0Tfl",
                     "ZaPn5wnJhJdltSw6jPqtAHXlFQBzmXg0Jekr8W63Q9be3KP6Jw",
                     "s5ThrrONDBVMSqeeRXZZKfnc0YcoSeccbmE1o3asg5HlV1zZPe",
                     "carsparadise",
                     "autos",
                     ['cars', 'cool cars', 'luxury cars', 'auto', 'wow cars']
                       )
    earth_blog_r = RedditBlog("epNkKeTfXS0OcQoZO9naLSXdj58EqksbBH3N7BNCaSDJ0WPRH8",
                     "ZQnyDcZjUPhspLOYQDycy0EciO4EenwraiSErVvXx4FcTVIdIH",
                     "kRs4r5H8XJngbip3enFbp2MZyKcnBApuuISMZTqdn9xfwoRIhO",
                     "dDP9LQvahiC5GE4G4Au50qGO1bkoNvBgeUxg6cuvjKjb6tmygO",
                     "epNkKeTfXS0OcQoZO9naLSXdj58EqksbBH3N7BNCaSDJ0WPRH8",
                     "incredibleearth",
                     "EarthPorn",
                     ['Earth', 'cool place', 'photo', 'place', 'wow', 'amazing', 'pics', 'nature', 'wild'],

                       )
    meme2_r = RedditBlog("gn1tWsZ5Wq3tyOdZbKoOLHrUhlYwAnXqDjEeLRtwjGuCu1LKh2",
                     "vcIKu8qrHl8uguTgjkbGuwaQiVDajMfY3zi1u7AJXcUzlDVxiU",
                     "dC00e6YQxlwWT37Lm8A8ZIx1VpwHoVcTbCAHlinpptluI6R8YT",
                     "6gMoqbosWaQCfK1c56CPvCNmMyyFtZkZjKrDuUDNig4Bd10Vsw",
                     "gn1tWsZ5Wq3tyOdZbKoOLHrUhlYwAnXqDjEeLRtwjGuCu1LKh2",
                     "memesforages",
                     "funny",
                     ['meme', 'memes', 'funny', 'dank meme', 'funny picture'])
    programmingHumour_r = RedditBlog("UqBfts94LerDmvzD3kzVLO8bEFLk3cnMUyWJVixgtSQ6lJnJgs",
                                     "j5awYsaeIJLFRsp5Xa8HLw3NTRkIu0hOkabnxRMXrJRU2Nl7v9",
                                     "0E0OgPbLtfzCN3yXPD8ZKho6tU0GFfq16zM9twCsYCVhK2iOzC",
                                     "SOsRkfhgmMLr2rHSQUzEEjFCWhKMC3ZJ9pof62XbDMurAVECKN",
                                     "UqBfts94LerDmvzD3kzVLO8bEFLk3cnMUyWJVixgtSQ6lJnJgs",
                                     "programminghumour",
                                     "ProgrammerHumor",
                                     ['funny', 'programming', 'humour', 'programming humour'])
    aww_r = RedditBlog("fIJI5esiBwbsttsdd6QhPSB4GvNXMlwzkSAq43efSH8ri9cpQ9",
                     "Z4ce5s0NCGsvBOYcW5TrLKYkrDjt0Qodd6XHBzuvnzA0PolBXi",
                     "BhqpZ413I96sv99DRYmXiYrM8DhDnZgteD26O7QIeI4qdshtEq",
                     "6FyreJSHwWPSRAGPvVxFombUqZShVZMT8m9wvAknONSGTTSFao",
                     "fIJI5esiBwbsttsdd6QhPSB4GvNXMlwzkSAq43efSH8ri9cpQ9",
                     "awwsfordays",
                     "aww",
                     ['aww', 'cute', 'adorable', 'aww cute', 'lovely'])
    
    
    #blogs_reddit.append(o_blog_reddit)
    blogs_reddit.append(programmingHumour_r)
    blogs_reddit.append(aww_r)
    
    
    blogs_reddit.append(earth_blog_r)
    blogs_reddit.append(meme2_r)


    for k in blogs_tumblr:
        k.posta()

    for k in blogs_reddit:
        k.posta()


    print ("Finito tutto, gg wp!")
    pass
