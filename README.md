# TikTok API
## Introduction:
The API is for __scraping only__ and gives the ability to access the following data from tiktok:

* [Post information (Including the watermark and no watermark video url)](#getpostpost_id)
* [Post comments](#listcommentspost_id-amount)
* [User data](#getuseruser_id)
* [User posts](#listpostsuser_id)
* [People following a user](#listfollowersuser_id)
* [People the user is following](#listfollowinguser_id)
### Version:
__12-12-2021:__ V0.1.1 Beta for Python 3.x.x
### Requirements:
* BeautifulSoup: https://pypi.org/project/beautifulsoup4/
* Requests: https://pypi.org/project/requests/
### Example:
Check example.py for an overall understanding of how to use this api
## Usage:
### Creating an api instance:
Example:
```Python
from TikTokAPI import TTAPI
api = TTAPI()
```
### Receiving data from tiktok api:
__Note: If the api response is {} then try a different input, if that does not work try updating the device parameters, if that also fails then the tiktok api might not be working or the script expired__
#### .getPost(post_id)
Gets a post.

Example:
```Python
api.getPost(post_id)

#Returns: { author: {...}, aweme_id: '999', desc: 'description', music: {...}, statistics: {...}, video: {...}, ... }
```
#### .listComments(post_id, amount)
Lists comments for a post.

Example:
```Python
api.listComments(post_id, amount)

#Returns: [{ text: 'first!', user: {...} }, { text: 'second!', user: {...} }, ...]
```
#### .getUser(user_id)
Gets a user's profile.

Example:
```Python
api.getUser(user_id)

#Returns: { aweme_count: 1000, nickname: 'example', unique_id: 'musername', ... }
```
#### .listPosts(user_id)
Lists a user's posts.

Example:
```Python
api.listPosts(user_id)

#Returns: [{ author: {...}, aweme_id: '999', desc: 'description', music: {...}, statistics: {...}, video: {...} }, ...]
```
#### .listFollowers(user_id)
Lists the users that follow the specified user.

Example:
```Python
api.listFollowers(user_id)

#Returns: [{ unique_id: 'follower1' }, { unique_id: 'follower2' }, ...]
```
#### .listFollowing(user_id)
Lists the users that the specified user follows.

Example:
```Python
api.listFollowing(user_id)

#Returns: [{ unique_id: 'following1' }, { unique_id: 'following2' }, ...]
```
### Extracting id's from url's:
#### .getPostId(url)

Extracts and returns the id of a post by using a tiktok url.

Example:

```Python
#Any post url should work

api.getPostId("https://www.tiktok.com/@tiktok/video/6839775130407750917")

#Returns: 6839775130407750917
```
#### .getUserId(url)

Extracts and returns the id of a user by using a tiktok url to their post or account.

Example:

```Python
#Any post/user url should work

api.getUserId("https://www.tiktok.com/@tiktok/video/6839775130407750917")

#Returns: 107955
```
### Finding and setting device parameters:
__Note: This step will be required in the future because the default parameters will eventually expire__
#### .getDeviceParams(url)

Device parameters are required to be able to use the tiktok's api service, they are specific to your device and account, using your own parameters is a much more stable solution because you are the one who owns them.

This function returns a dictionary of needed parameters from a sniffed tiktok url, if the returned dictionary is blank then not all required parameters are present. You can use a mitm proxy to scan the url's the tiktok app gets/posts and look for keywords like tiktokv, api, passport, or aweme.

Example:
```Python
#Any tiktok api url's similar to this one should work

api.getDeviceParams("https://api-h2.tiktokv.com/aweme/v1/aweme/detail/?aweme_id=7026288424218807553&origin_type=web&request_source=0&os_api=25&device_type=ONEPLUS+A3010&ssmix=a&manifest_version_code=170804&dpi=240&uoo=0&carrier_region=US&region=US&carrier_region_v2=310&app_name=trill&version_name=17.8.4&timezone_offset=-18000&ts=1639622884&ab_version=17.8.4&cpu_support64=false&ac2=unknown&ac=wifi&app_type=normal&host_abi=armeabi-v7a&channel=apkpure&update_version_code=170804&_rticket=1639622884&device_platform=android&iid=7032045377013942018&build_number=17.8.4&locale=en&op_region=US&version_code=170804&timezone_name=America%2FNew_York&cdid=ddbd4b01-a3d7-4e69-8a31-7ff76e4469fc&openudid=9b842ece932f071b&device_id=7031670777339250182&sys_region=US&app_language=en&resolution=900*1563&language=en&device_brand=OnePlus&os_version=7.1.1&aid=1180")

#Returns: {'os_api': '25', 'device_type': 'ONEPLUS+A3010', 'app_name': 'trill', 'version_name': '17.8.4', 'channel': 'apkpure', 'device_platform': 'android', 'iid': '7032045377013942018', 'version_code': '170804', 'device_id': '7031670777339250182', 'os_version': '7.1.1', 'aid': '1180'}
```
#### .setDeviceParams(param_dict)

This function sets the device parameters of the tiktok api class to the dictionary you input. You can create a working device parameter dictionary using .getDeviceParams(url).

Example:
```Python
api.setDeviceParams({'os_api': '25', 'device_type': 'ONEPLUS+A3010', 'app_name': 'trill', 'version_name': '17.8.4', 'channel': 'apkpure', 'device_platform': 'android', 'iid': '7032045377013942018', 'version_code': '170804', 'device_id': '7031670777339250182', 'os_version': '7.1.1', 'aid': '1180'})

#Device parameters are now updated
```
## Credits:
Parameter generation: https://www.codenong.com/cs109390694/

TikTok API methods: https://github.com/szdc/tiktok-api
