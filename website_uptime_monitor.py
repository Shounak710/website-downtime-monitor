import requests
import json
from slack_account import SlackAccount

website_url = 'https://pro.threease.com'
downtime_detected = False

if(not downtime_detected):
    res = requests.get(website_url)
    slack_account = SlackAccount('sdfsf', 'sdfsf', 'dsfsf', 'sdfsdfdsf')
    if not res:
        downtime_detected = True
        slack_account.is_valid()
        print('Website down')
    else:
        downtime_detected = False
        slack_account.is_valid()