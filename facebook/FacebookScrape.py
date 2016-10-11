#-*- coding: utf-8 -*-
import facebook
import json
import requests
import time
import MediaName as Media

#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')

#graph = facebook.GraphAPI(access_token=None)

class Facebook_post_scrape():
    def __init__(self, page_name):
        self.api = 'https://graph.facebook.com'
        self.version = 'v2.3'
        self.page_name = page_name
        self.token = 'EAACEdEose0cBAHZAAnBrGvatCaqeCeFUhlepaO3hmb5lJW3zYYJl9nzI1i8pdzW8TGGsCRZAbl1ovvMxSmZCFmYpjthEaaJFOMEj9qTo8dweOrnZBCfBbYkP1q0vxxwn0kglVh66sntpukk3IPkgDhYxWCAbzXb1ubjgNBMJ4wZDZD'
    def scrape(self):
        query = self.api + '/' + self.version + '/' + self.page_name + '/posts?access_token=' + self.token
        print 'Fetch from: ' + self.page_name
        print 'Query url: ' + query

        #Fetch data in json format via FB graph api
        #Total post number: 25
        #Total comment number: 25
        print 'Fetching Data...'
        try:
            res = requests.get(query)
            #print res.text
            print 'Fetching Succeed'
        except BaseException, e:
            print 'Fetching Data Failed!'
            print str(e)

        jsondata = json.loads(res.text)
        postsdata = jsondata['data']
        posts_count = 0
        fetchtime = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
        path = './'+self.page_name + '_' + fetchtime + '.csv'
        print 'Save result to: ' + path
        try:
            result_file = open(path, 'w')
            print >> result_file, 'Query url: ' + query
            for post in postsdata:
                posts_count += 1
                message = post['message'].encode('utf-8')
                comments = post['comments']['data']
                print >> result_file, '----------------Post:----------------'
                print >> result_file, message
                print >> result_file, '--------------Comments:--------------'
                comments_count = 1
                for comment in comments:
                    comment['message'] = ''.join(comment['message'].split('\n'))
                    print >> result_file, str(comments_count) + ' | ' + comment['from']['name'].encode('utf-8') + ' | ' + comment['message'].encode('utf-8')
                    comments_count += 1
            print >> result_file, 'Total Posts: ' + str(posts_count)
            print "Completed!"
        except IOError:
            print 'Failed To Open ' + path
        finally:
            result_file.close()

if __name__ == '__main__':
    index = 1
    for media in Media.media_dic:
        print str(index),
        print media + '\t==>' + 'FB page name: ' + Media.media_dic[media]['name'] + '\tid: ' + Media.media_dic[media]['id']
        index += 1
    name = raw_input("Please select a media company: ")
    selected_name = Media.media_dic[name]['name']
    print selected_name
    test = Facebook_post_scrape(selected_name)
    test.scrape()


'''
{
   "data": [
      {
         "id": "15704546335_10154683352356336",
         "from": {
            "name": "Fox News",
            "category": "Media/News/Publishing",
            "id": "15704546335"
         },
         "message": "House Speaker Paul Ryan told lawmakers Monday he will not defend or campaign with Donald J. Trump, and that they should do what is best for their own districts. http://fxn.ws/2cQKNNC",
         "message_tags": {
            "14": [
               {
                  "id": "155244824599302",
                  "name": "Paul Ryan",
                  "type": "page",
                  "offset": 14,
                  "length": 9
               }
            ],
            "82": [
               {
                  "id": "153080620724",
                  "name": "Donald J. Trump",
                  "type": "page",
                  "offset": 82,
                  "length": 15
               }
            ]
         },
         "picture": "https://scontent.xx.fbcdn.net/v/t1.0-0/p130x130/14572859_10154683352356336_4885397959154683616_n.jpg?oh=7f2888b0e5a8d85747ad6bdeaae6fe66&oe=58729AB0",
         "link": "https://www.facebook.com/FoxNews/photos/a.184044921335.134777.15704546335/10154683352356336/?type=3",
         "name": "Timeline Photos",
         "icon": "https://www.facebook.com/images/icons/photo.gif",
         "actions": [
            {
               "name": "Comment",
               "link": "https://www.facebook.com/15704546335/posts/10154683352356336"
            },
            {
               "name": "Like",
               "link": "https://www.facebook.com/15704546335/posts/10154683352356336"
            },
            {
               "name": "Share",
               "link": "https://www.facebook.com/15704546335/posts/10154683352356336"
            }
         ],
         "privacy": {
            "value": "",
            "description": "",
            "friends": "",
            "allow": "",
            "deny": ""
         },
         "type": "photo",
         "status_type": "added_photos",
         "object_id": "10154683352356336",
         "created_time": "2016-10-10T16:04:04+0000",
         "updated_time": "2016-10-10T17:07:27+0000",
         "shares": {
            "count": 676
         },
         "is_hidden": false,
         "is_expired": false,
         "likes": {
            "data": [
               {
                  "id": "800467363314569",
                  "name": "Keith Inwood"
               },
               {
                  "id": "802239479857956",
                  "name": "Tanner Morgan"
               }
            ],
            "paging": {
               "cursors": {
                  "before": "ODAwNDY3MzYzMzE0NTY5",
                  "after": "Nzg2ODc1MzQ0NzA0Nzky"
               },
               "next": "https://graph.facebook.com/v2.3/15704546335_10154683352356336/likes?access_token=EAACEdEose0cBAD5ND4d1ZB47I4PMhukWz3K8ZB81MhtOxShlD1ToINmjMFSFFT0t8DKBczo0c3FqCVHxyVB2u7mOmy4b69jRguBQmLHeQ7cJHC8QfK1qKki75kBUkkg4NX0himJjLQtGnJakTjgsHBqB53LmYZCBLVNHKgugAZDZD&pretty=1&limit=25&after=Nzg2ODc1MzQ0NzA0Nzky"
            }
         },
         "comments": {
            "data": [
               {
                  "created_time": "2016-10-10T16:04:35+0000",
                  "from": {
                     "name": "Godswill Forche",
                     "id": "991527684196246"
                  },
                  "message": "Paul Ryan, John McCain, Mitt Romney, Jeb Bush, Mitch McConnell, John Kasich and the other Prominent Republicans never come out and CRITICISE Hillary Clinton or hold her ACCOUNTABLE for her actions or her CRIMES. \nBut guess what? When it comes to Donald Trump, they can't wait to POUNCE on him and shred him to pieces.\nJust like the Mainstream Media does.\n\nI think most of these Republican elites are just Democrats in GOP skin.",
                  "can_remove": false,
                  "like_count": 4383,
                  "user_likes": false,
                  "id": "10154683352356336_10154683369211336"
               },
               {
                  "created_time": "2016-10-10T16:05:22+0000",
                  "from": {
                     "name": "CJ Del",
                     "id": "10202215911117595"
                  },
                  "message": "So what. Whether you like Trump or not, a Trump Presidency is a threat to the entire political system.\n\nIt will demonstrate that the highest office in the land does not have to go to a career politician. That \"The People\" are the ones who determine who will be President. \n\nShould this happen it will definitively prove that every political office is up for grabs by \"We The People\", from the highest office to the lowest. \n\nThis is what the establishment fears most.",
                  "can_remove": false,
                  "like_count": 2048,
                  "user_likes": false,
                  "id": "10154683352356336_10154683371231336"
               },
            ],
            "paging": {
               "cursors": {
                  "before": "NTMzMQZDZD",
                  "after": "NTMwNgZDZD"
               },
               "next": "https://graph.facebook.com/v2.3/15704546335_10154683352356336/comments?access_token=EAACEdEose0cBAD5ND4d1ZB47I4PMhukWz3K8ZB81MhtOxShlD1ToINmjMFSFFT0t8DKBczo0c3FqCVHxyVB2u7mOmy4b69jRguBQmLHeQ7cJHC8QfK1qKki75kBUkkg4NX0himJjLQtGnJakTjgsHBqB53LmYZCBLVNHKgugAZDZD&pretty=1&limit=25&after=NTMwNgZDZD"
            }
         }
      }
   ],
   "paging": {
      "previous": "https://graph.facebook.com/v2.3/15704546335/posts?since=1476118339&access_token=EAACEdEose0cBAD5ND4d1ZB47I4PMhukWz3K8ZB81MhtOxShlD1ToINmjMFSFFT0t8DKBczo0c3FqCVHxyVB2u7mOmy4b69jRguBQmLHeQ7cJHC8QfK1qKki75kBUkkg4NX0himJjLQtGnJakTjgsHBqB53LmYZCBLVNHKgugAZDZD&limit=25&__paging_token=enc_AdAO2P8rZBZBUCMXcWaMb7ZBddR4ZCZAF1BbH7kre9D7nnsbc0tmZCXfBMls9MTsutCDZBIzfcDcU1Ym7BvOxHHwQIjnk8S&__previous=1",
      "next": "https://graph.facebook.com/v2.3/15704546335/posts?access_token=EAACEdEose0cBAD5ND4d1ZB47I4PMhukWz3K8ZB81MhtOxShlD1ToINmjMFSFFT0t8DKBczo0c3FqCVHxyVB2u7mOmy4b69jRguBQmLHeQ7cJHC8QfK1qKki75kBUkkg4NX0himJjLQtGnJakTjgsHBqB53LmYZCBLVNHKgugAZDZD&limit=25&until=1476065033&__paging_token=enc_AdBbqJqwmZAn5Iqqi3WeFxBZCJP9r8ZB51OWRCzZBJ5r7F5OI1kV32Exlq1f4ERMsLpOM8oOLVtlCJyIcLqAxrfp8eA5"
   }
}            
'''