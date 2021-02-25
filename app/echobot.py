import json
import os
import sys
import time

from webwhatsapi import WhatsAPIDriver
from webwhatsapi.objects.message import Message

print("Environment", os.environ)
try:
    os.environ["SELENIUM"]
except KeyError:
    print("Please set the environment variable SELENIUM to Selenium URL")
    sys.exit(1)

profiledir = os.path.join(".", "firefox_cache")
if not os.path.exists(profiledir):
    os.makedirs(profiledir)

driver = WhatsAPIDriver(
    profile=profiledir, client="remote", command_executor=os.environ["SELENIUM"]
)
print("Waiting for QR")
time.sleep(120)
driver.wait_for_login()
print("Saving session")
driver.save_firefox_profile(remove_old=False)
print("Bot started")

while True:
    time.sleep(3)
    print("Checking for more messages, status", driver.get_status())
    for contact in driver.get_unread():
        for message in contact.messages:
            #print(json.dumps(message.get_js_obj(), indent=4))
            if isinstance(message, Message):  # Currently works for text messages only.
                contact.chat.send_message(message.content)
