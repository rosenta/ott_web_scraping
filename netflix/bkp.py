import json
import requests

cookies = {
    'SecureNetflixId': '<your_netflix_id>',
    'NetflixId': '<your_netflix_id>',
}

headers = {
    'authority': 'www.netflix.com',
    'accept': '*/*',
    'accept-language': 'en-GB,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.netflix.com',
    'referer': 'https://www.netflix.com/browse/genre/34399?so=az',
    'sec-ch-ua': '"Brave";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"macOS"',
    'sec-ch-ua-platform-version': '"13.6.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'x-netflix.browsername': 'Chrome',
    'x-netflix.browserversion': '117',
    'x-netflix.client.request.name': 'ui/falcorUnclassified',
    'x-netflix.clienttype': 'akira',
    'x-netflix.esn': 'NFCDCH-MC-KJA5N1EWHGG3RYLYDJ4X0UC97AN6JG',
    'x-netflix.esnprefix': 'NFCDCH-MC-',
    'x-netflix.nq.stack': 'prod',
    'x-netflix.osfullname': 'Mac OS X',
    'x-netflix.osname': 'Mac OS X',
    'x-netflix.osversion': '10.15.7',
    'x-netflix.request.client.user.guid': 'WSAZV47GUFD4HITW5K7QSDLNPA',
    'x-netflix.uiversion': 'vc63e5850',
}

params = {
    'webp': 'true',
    'drmSystem': 'widevine',
    'isVolatileBillboardsEnabled': 'true',
    'routeAPIRequestsThroughFTL': 'false',
    'hasVideoMerchInBob': 'true',
    'hasVideoMerchInJaw': 'true',
    'falcor_server': '0.1.0',
    'withSize': 'true',
    'materialize': 'true',
    'original_path': '/shakti/mre/pathEvaluator',
}

data = {
    'path': [
        '["genres",34399,"az",{"from":0,"to":10},"itemSummary"]',
        '["genres",34399,"az",{"from":0,"to":10},"reference",["availability","episodeCount","inRemindMeList","queue","summary"]]',
    ],
    'authURL': '1697060641282.S8RDZDjKsQ5wO5euqI+1oE0e+Eg=',
}

response = requests.post(
    'https://www.netflix.com/nq/website/memberapi/vc63e5850/pathEvaluator',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)

import json
print(f"fetch status code --> {response.status_code}")
# json.dumps(response.json())
