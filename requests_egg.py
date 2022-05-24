import requests 
import json
import uuid

from requests.api import head, request


class Base():
    auth = 'Bearer sl.BINJTaCzyPw0ZOTvcsM5Ljq3xrVH1s-MiBehq6aYNEYD3zUk2J9ofGdiMOfVElS34YcfGRmcaAeOCqb0DkdyF04pcZs2ZmDwFXwE0AArX7RioV8kZG65Rlsq5esMgzOzfWiDmD6B'
    method = "POST"



class UploadRequest(Base):  
    
    def __init__(self) -> None:
        self.params = {
            'url':"https://content.dropboxapi.com/2/files/upload",
            'headers':{
                'Dropbox-API-Arg': '{"path": "/text.txt","mode": "add","autorename": true,"mute": false,"strict_conflict": false}',
                'Content-Type': 'application/octet-stream',
                'Authorization': self.auth
            }
        }

    def get_response(self, rdata='This is test message for a new file'):
        self.response = requests.request(
            method=self.method, 
            url=self.params['url'], 
            headers=self.params['headers'],
            data=rdata
        )
        self.id = json.loads(self.response.text)['id']



class GetFileMetadataRequest(Base):
    
    def __init__(self) -> None:
        self.params = {
            'url':"https://api.dropboxapi.com/2/sharing/get_file_metadata",
            'headers':{
                'Content-Type': 'application/json',
                'Authorization': self.auth
            }
        }

    def get_response(self, id):
        self.response = requests.request(
            method=self.method, 
            url=self.params['url'], 
            headers=self.params['headers'],
            data=json.dumps(
                {
                    "file": f"{id}",
                    "actions": []
                }
            )
        )
        self.file_path = json.loads(self.response.text)['path_display']



class DeleteRequest(Base):
    def __init__(self) -> None:
        self.params = {
            'url':"https://api.dropboxapi.com/2/files/delete_v2",
            'headers':{
                'Content-Type': 'application/json',
                'Authorization': self.auth
            }
        }

    def get_response(self,file_path):
        self.response = requests.request(
            method=self.method, 
            url=self.params['url'], 
            headers=self.params['headers'],
            data=json.dumps(
                {
                    "path": f"{file_path}"
                }
            )
        )
