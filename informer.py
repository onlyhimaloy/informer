
#This tool has developed to get information of server owner via gmail.

from apiclient import discovery
from apiclient import errors
from httplib2 import Http
from oauth2client import file, client, tools
import base64
import re
import time
import dateutil.parser as parser
from datetime import datetime
import datetime
try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None
#tstests
# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/gmail-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Gmail API Python Quickstart'

store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
GMAIL = discovery.build('gmail', 'v1', http=creds.authorize(Http()))

user_id = 'me'
label_id_one = 'INBOX'
label_id_two = 'UNREAD'

# Getting all the unread messages from Inbox
# labelIds can be changed accordingly
unread_msgs = GMAIL.users().messages().list(userId='me', labelIds=[label_id_one, label_id_two]).execute()

# We get a dictonary. Now reading values for the key 'messages'
mssg_list = unread_msgs['messages']

print("Total unread messages in inbox: ", str(len(mssg_list)))

final_list = []

for mssg in mssg_list:
    temp_dict = {}
    m_id = mssg['id']  # get id of individual message
    message = GMAIL.users().messages().get(userId=user_id, id=m_id).execute()  # fetch the message using API
    payld = message['payload']  # get payload of the message
    headr = payld['headers']  # get header of the payload

    for one in headr:  # getting the Subject
        if one['name'] == 'Subject':
            msg_subject = one['value']
            temp_dict['Subject'] = msg_subject
        else:
            pass

    for two in headr:  # getting the date
        if two['name'] == 'Date':
            msg_date = two['value']
            date_parse = (parser.parse(msg_date))
            m_date = (date_parse.date())
            temp_dict['Date'] = str(m_date)
        else:
            pass

    for three in headr:  # getting the Sender
        if three['name'] == 'From':
            msg_from = three['value']
            temp_dict['Sender'] = msg_from
        else:
            pass

    temp_dict['Snippet'] = message['snippet']  # fetching message snippet

    try:

        # Fetching message body
        mssg_parts = payld['parts']  # fetching the message parts
        part_one = mssg_parts[0]  # fetching first element of the part
        part_body = part_one['body']  # fetching body of the message
        part_data = part_body['data']  # fetching data from the body
        clean_one = part_data.replace("-", "+")  # decoding from Base64 to UTF-8
        clean_one = clean_one.replace("_", "/")  # decoding from Base64 to UTF-8
        clean_two = base64.b64decode(bytes(clean_one, 'UTF-8'))  # decoding from Base64 to UTF-8
        soup = BeautifulSoup(clean_two, "lxml")
        mssg_body = soup.body()
        # mssg_body is a readible form of message body
        # depending on the end user's requirements, it can be further cleaned
        # using regex, beautiful soup, or any other method
        temp_dict['Message_body'] = mssg_body

    except:
        pass

    print(temp_dict)