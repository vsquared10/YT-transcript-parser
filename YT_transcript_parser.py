import os
import platform
import sys
import re
import subprocess
from time import sleep
import google.oauth2.credentials
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

CLIENT_SECRETS_FILE = "client_secret.json"
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

def get_authenticated_service():
    credential_path = os.path.join('./', 'credential_sample.json')
    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRETS_FILE, SCOPES)
        credentials = tools.run_flow(flow, store)
    return build(API_SERVICE_NAME, API_VERSION, credentials=credentials)

def get_caption_id(videoId):
    resp = client.captions().list(part='snippet', videoId=videoId).execute()
    return resp['items'][0]['id']

def parse_captions(id):
    parsed = client.captions().download(id=id).execute().decode('utf-8')
    time_pattern = r'\d+:\d+:\d+.\d+,\d+:\d+:\d+.\d+'
    parsed = re.sub(time_pattern, '', parsed)

    stopwords = {'\n\n\n': ' ', '\n\n': ' ', '\n': ' ', 'you know ': ' ',
                 'I think ': ' ', 'if you like ': ' ', 'kind of ': ' ',
                 ' which': ' which'}

    for pattern, replacement in stopwords.items():
        parsed = parsed.replace(pattern, replacement)

    return parsed

if __name__ == '__main__':
  os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
  client = get_authenticated_service()

  url = input("what's the url? ")
  videoId = re.search('v=[\w-]+', url)[0][2:]
  caption_id = get_caption_id(videoId)
  cleaned_text = parse_captions(caption_id)
  with open('cleaned_transcript.doc', 'w') as f:
      f.write(cleaned_text)

  # command_list = ["/usr/bin/open", "-W", "-n", "-a", "/Applications/Pages.app",
  #                 'cleaned_transcript.doc']
  # ps = subprocess.Popen(command_list, stdout=subprocess.PIPE)
  if platform.system() == 'Darwin':
      subprocess.Popen(['open', 'cleaned_transcript.doc'])
      # if input('Do you use Pages (yes/no)? ') == 'yes':
      #     with open('cleaned_transcript.pdf', 'w') as f:
      #         f.write(cleaned_text)
      #     subprocess.Popen(command_list)
      # else:
      #     subprocess.Popen(['open', 'cleaned_transcript.doc'])
  elif platform.system() == 'Windows':
      os.startfile('cleaned_transcript.doc')
  else:
      subprocess.Popen(['xdg-open', 'cleaned_transcript.doc'])
  # sleep(5)
  # os.remove('cleaned_transcript')
  sys.exit()
