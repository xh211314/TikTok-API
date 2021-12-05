#Import the TikTokAPI:
from TikTokAPI import TTAPI

#Create API object:
api = TTAPI()

#TikTok post url's can be in any formats:
#https://vm.tiktok.com/abcde
#https://vt.tiktok.com/abcde
#https://m.tiktok.com/v/12345
#https://tiktok.com/@user/video/12345

#Get the id of the post using a url:
postId = api.getPostId("https://www.tiktok.com/@tiktok/video/6839775130407750917")

#Print id
print("The post id is "+postId+"\n")

#Get post info
postInfo = api.getPost(postId)

#Print post info
print(postInfo)

#Print 30 comments of post
print(api.listComments(postId, "30"))

#Get user id
authorId = postInfo["aweme_detail"]["author"]["uid"]

#Print user info
print(api.getUser(authorId))

#Print user posts
print(api.listPosts(authorId))

#Print people following user
print(api.listFollowers(authorId))

#Print people user is following
print(api.listFollowing(authorId))
