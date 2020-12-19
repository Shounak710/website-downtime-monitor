import requests
import json

website_url = 'https://pro.threease.com'
downtime_detected = False

# slack credentials
slack_token = ''
slack_channel = ''
slack_icon_url = ''
slack_user_name = ''

if(not downtime_detected):
    res = requests.get(website_url)
    if not res:
        downtime_detected = True
        print('Website down')
    else:
        downtime_detected = False

# will complete this one in office, after getting slack credentials
def post_message_to_slack(text, )