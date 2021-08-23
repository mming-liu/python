import requests

class flush:
    def __init__(self) -> None:
        self.server = '192.168.200.165:10001'
        self.webRoot = 'casualty'
        self.username = 'sh'
        self.password = '1'
        self.client_id = 'casualty-web'
        self.client_secret = '36ddda5af915d91549d3ab5bff1bafec'
        self.cacheName = 'feeStandardCache'

    def get_token(self):
        url = 'http://'+self.server+'/'+self.webRoot+'/oauth/token?grant_type=password&username='+self.password+'&password='+ self.password+'&client_id='+ self.client_id+'&client_secret='+self.client_secret
        response = requests.post(url)
        # print(response.text)
        return response
    
    def get_flush(self):
        url = 'http://'+self.server+'/'+self.webRoot+'/foundation/cache/flush?cacheName='+self.cacheName
        # print(self.get_token())
        headers = {'authorization': self.get_token()}
        response = requests.post(url,headers=headers)
        print(response.text)
        return response
        

if __name__ == '__main__':
    a = flush().get_flush()