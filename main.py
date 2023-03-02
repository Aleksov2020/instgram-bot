import time

from pymemuc import PyMemuc
import os
import requests
import droid_do as dd
from InstagramBot import InstagramBot


def rotate_proxy():
    url = 'https://thesocialproxy.com/wp-json/lmfwc/v2/licenses/rotate-proxy' \
          '/bmV3LXlvcmsxLnRoZXNvY2lhbHByb3h5LmNvbToxMDAwMEB6bXUya25jaXY2ZmE4dG83OnhscTRuNmNqbWt0M3V2enc=' \
          '=/?consumer_key=ck_47cab5b518a9f0f98681513a6198f8042148ddcd&consumer_secret' \
          '=cs_ddc1dacadc679bde6c09ff3e72c658f738512b35'

    payload = {}
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response)

#TODO add randomize at time.sleep function
#TODO add randomize at click function

def start_proxy(index):
    # open proxyDroid
    dd.click(219, 1023, index)
    time.sleep(4)

    # start proxy session
    dd.click(561, 227, index)
    time.sleep(3)

    # go home
    dd.home_button(index)
    time.sleep(1)

# create a PyMemuc instance, doing so will automatically link to the MEMUC executable
memuc = PyMemuc()
memuc.debug = True
index = 0
time.sleep(7)
instagram_bot = InstagramBot(index)

time.sleep(1000)
for index in range(0, 50):
    memuc.start_vm(index)
    print("Start VM")
    time.sleep(7)
    rotate_proxy()
    print("Start PROXY")
    start_proxy(index)
    time.sleep(2)
    instagram_bot = InstagramBot(index)
    time.sleep(2)
    instagram_bot.watch_target_reel('kristina.sense')

    memuc.stop_vm(index)

