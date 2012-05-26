import requests
from pprint import pprint
import hashlib
import urllib

def get_token(tab_id):
  return hashlib.sha1('onlyUG_'+tab_id).hexdigest()

tab_id = '1116724'
token = get_token(tab_id)

target_url = 'http://www.ultimate-guitar.com/tab_download.php?tab_id=%s&token=%s' %(tab_id,token)
qtarget_url = 'http://code/testharness/test.php?tab_id=%s&token=%s' %(tab_id,token)

r = requests.get(target_url)

print (r.content)

