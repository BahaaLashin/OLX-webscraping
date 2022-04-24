import requests
from bs4 import BeautifulSoup
import json

class SellerInfo:

    user_phone = '+2001060837560'
    password = 'bhaa5248289'
    token = ''
    def __init__(self):
        r = requests.post('https://auth.olx.com.eg/auth/realms/olx-eg/protocol/openid-connect/token', data = {'grant_type':'password',
                                                                                                      'client_id': 'frontend',
                                                                                                      'scope': 'openid','type': 'phone_password','phone_number': self.user_phone,'password': self.password})
        soup = BeautifulSoup(r.content, "html.parser")
        self.token = json.loads(soup.text)['access_token']
        

    def get_product_seller_info_by_productID(self,product_id):
        url = "https://www.olx.com.eg/api/listing/"+product_id+"/contactInfo/"

        payload={}
        headers = {
        'authority': 'www.olx.com.eg',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': '_rtb_user_id=5f010f97-61b4-949e-b26b-3969429a67f2; _fbp=fb.2.1638179907450.513744458; __gads=ID=03288c6a788f0dc9:T=1638179913:S=ALNI_MYRRADJy-5jQC6WjTv13pBFfWsAiA; _hjSessionUser_1919863=eyJpZCI6IjkxOTNjYzZjLTliMWEtNTFmZC05Y2FlLWNlZmNlNmJkN2U3YyIsImNyZWF0ZWQiOjE2MzgxNzk5MDkyNDgsImV4aXN0aW5nIjp0cnVlfQ==; _gcl_au=1.1.562144227.1646776157; _gcl_aw=GCL.1647049908.CjwKCAiAg6yRBhBNEiwAeVyL0BAZV4rRCQKNX1dMriRTZvUrWFlRAdfmtgjruH6l0DVy9akhnv8-hxoCf3IQAvD_BwE; _gac_=1.1647049908.CjwKCAiAg6yRBhBNEiwAeVyL0BAZV4rRCQKNX1dMriRTZvUrWFlRAdfmtgjruH6l0DVy9akhnv8-hxoCf3IQAvD_BwE; _gac_UA-52442898-2=1.1647049910.CjwKCAiAg6yRBhBNEiwAeVyL0BAZV4rRCQKNX1dMriRTZvUrWFlRAdfmtgjruH6l0DVy9akhnv8-hxoCf3IQAvD_BwE; __gfp_64b=u63QHlLKqPOa2imLyjp62nFm2m3HCS_1uMiNJiOSJZD.q7|1638179912; __utmz=1.1649641765.34.28.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); layerappsSeen=1; onap=17d6b21a28cxadd8036-35-18017f92816x10dfc1ab-1-1649671446; __utma=1.457188509.1638179906.1649641765.1649669646.35; device_id=l28b7asdbdkh740zt; _gid=GA1.3.234222111.1650765328; settings=%7B%22area%22%3Anull%2C%22currency%22%3A%22EGP%22%2C%22searchHitsLayout%22%3A%22GRID%22%7D; banners=%7B%7D; abTests=%7B%7D; userGeoLocation=%7B%22coordinates%22%3Anull%2C%22closestLocation%22%3Anull%2C%22loading%22%3Afalse%2C%22error%22%3Anull%7D; __gpi=UID=000003e31bfa1cfa:T=1649559296:RT=1650815191:S=ALNI_MYVG-A-EbtCqeRuOeeoIFGWBkoKYQ; anonymous_session_id=30b99feb-bbe1-4e60-a1a9-2a82ab1affbc; moe_uuid=54d0041d-b51d-4988-8c2d-af15869416cd; csrftoken=PjF81uMal9RbLTmRw1mN0J46UlkFqbh9H3mV5wxVmqjGNijRC0XglUHASxzDkImL; kc_access_token='+self.token+'; kc_refresh_token=eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI3Y2Y5MTczNC00MGIyLTQ4YTEtODMzZC1iZmEyYTRkY2ViNmYifQ.eyJleHAiOjE2NTM0MjUxMzYsImlhdCI6MTY1MDgzMzEzNiwianRpIjoiODljNzcyZDMtOTlhZi00NmUyLThlYWYtMGJhMDFkNWQxMGFlIiwiaXNzIjoiaHR0cHM6Ly9hdXRoLm9seC5jb20uZWcvYXV0aC9yZWFsbXMvb2x4LWVnIiwiYXVkIjoiaHR0cHM6Ly9hdXRoLm9seC5jb20uZWcvYXV0aC9yZWFsbXMvb2x4LWVnIiwic3ViIjoiYzY1ZDIwYjAtMGFiZi00ODVmLTgwZDgtODg1OThhNzZkZTZiIiwidHlwIjoiUmVmcmVzaCIsImF6cCI6ImZyb250ZW5kIiwic2Vzc2lvbl9zdGF0ZSI6ImM2ZGY5N2Q4LWY0M2MtNGNjZi04YTdmLTVhMDk2OTZkOTczMCIsInNjb3BlIjoib3BlbmlkIHVzZXJfcHJvZmlsZSIsInNpZCI6ImM2ZGY5N2Q4LWY0M2MtNGNjZi04YTdmLTVhMDk2OTZkOTczMCJ9.9ZbYjpg8bNEDletMh83Tt1a-OA51j4cQwzTftQfc8DI; kc_id_token=eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI3X0VYa3FxVjhsWG02RDFHeFgxYkw1QV9rNktFYUd0XzI0OFJWU0d5cWRRIn0.eyJleHAiOjE2NTA4MzQwMzYsImlhdCI6MTY1MDgzMzEzNiwiYXV0aF90aW1lIjowLCJqdGkiOiJiMTNjYzQ2OS0yNDc0LTRmYjYtYjhlNi1kZjA0NDc2MmNmZTkiLCJpc3MiOiJodHRwczovL2F1dGgub2x4LmNvbS5lZy9hdXRoL3JlYWxtcy9vbHgtZWciLCJhdWQiOiJmcm9udGVuZCIsInN1YiI6ImM2NWQyMGIwLTBhYmYtNDg1Zi04MGQ4LTg4NTk4YTc2ZGU2YiIsInR5cCI6IklEIiwiYXpwIjoiZnJvbnRlbmQiLCJzZXNzaW9uX3N0YXRlIjoiYzZkZjk3ZDgtZjQzYy00Y2NmLThhN2YtNWEwOTY5NmQ5NzMwIiwiYXRfaGFzaCI6ImkzYWYwS1BXMTl5Y3ZOckJsb2JNR0EiLCJhY3IiOiIxIiwic2lkIjoiYzZkZjk3ZDgtZjQzYy00Y2NmLThhN2YtNWEwOTY5NmQ5NzMwIiwibmFtZSI6IkJhaGFhIEVsZGluIE1vaGFtZWQiLCJkZXNjcmlwdGlvbiI6IiIsImV4dGVybmFsX2lkIjoiYzY1ZDIwYjAtMGFiZi00ODVmLTgwZDgtODg1OThhNzZkZTZiIiwicGhvbmVfbnVtYmVyIjoiKzIwMTA2MDgzNzU2MCIsImlzX3Bhc3N3b3JkbGVzc19sb2dpbiI6ZmFsc2V9.GYstFhoUnpDCQn95TYzoAkzEgF2WjPyB7SJmdlUUxvxR2kXipWpADgkp42TNnXGE_3uzpQmPLtqqKvBLIWsZlqgpz2i4rQ-9xWm-8qLntjMJ3kKzbXcC1DzydTbSzyZkf-x-wREtHh8ae8E9Fkz0cxY8HA8DakIUi0vIghzekCHzSzBQ-bVERmdWjXD7z_A0Gw1b6b0F1W8jEHiGi73DC_B98m0HVUMhm033FNlFTnH2aPgDkoPinbDhG3XJEg96KEDZ72pjh1iojQ4u7VU2UkEqqywpR6l-mc4fekSwvcRYWjFtLaZeDnyiYZyAS4ydV9nOgjn2U8n_dyIV9esCXg; _ga=GA1.3.457188509.1638179906; referrer=%2F; original_referrer=https%3A%2F%2Fwww.olx.com.eg%2Fad%2F%25D8%25B4%25D9%2585%25D9%258A%25D8%25B2-%25D8%25A8%25D9%2586%25D8%25A7%25D8%25AA%25D9%258A-ID190322067.html; landing_url=%2Fad%2F%D8%B4%D9%85%D9%8A%D8%B2-%D8%A8%D9%86%D8%A7%D8%AA%D9%8A-ID190322067.html; _ga_547QBEKWP2=GS1.1.1650831034.12.1.1650833734.0; anonymous_session_id=4be0536a-3541-46a5-9e9b-a3dae49eb88b; device_id=l291tk2w264s1u4c2; csrftoken=PjF81uMal9RbLTmRw1mN0J46UlkFqbh9H3mV5wxVmqjGNijRC0XglUHASxzDkImL',
        'referer': 'https://www.olx.com.eg/api/listing/'+product_id+'/contactInfo/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        return json.loads(response.text)