import json
import requests

cookies = {
    'SecureNetflixId': 'v%3D2%26mac%3DAQEAEQABABSso5AdAyc6d1rLm-N-ww2pmkw_gZ-MUSc.%26dt%3D1697065093678',
    'NetflixId': 'v%3D2%26ct%3DBQAOAAEBEPpZZEBgGGyA-6R91KRsj5uBwKBSBq3roimqQ-myMTBpr5EOJscSEGN-imXJuk_pqxAWCmWnIHItBFFjdOCphMGRG5YI_Dehl-jMpEtCC2tdaALH-LRJCC2qk1G-bJBQFPjBqDn_NhaxZ5No9iAXvoF7G6--GxfBfRpoiYi3WWrHpvdYnO19VZaiEQFUC7jydWYOK1AmnMK2gzx71-_Xy6S2qBoog9ro7SfWLyjBY7V-sgIf_h0Ax4NhUbaCj_saQntQ7FQ7v3u9YoH88cnboovO1Rhclb_hT0XpxaQu5sqkzzi_yba164AtFZv7Mrhv6bPNNuLiIaWCHlgLCh9VRQc24IajbuQSNL2r5iG8CH-T2_UGcCjaSNfwK8msk7_qzmfxwIAHGl3NGEXtdPWY31599cSYqUBpHKZqEt6dk6FHvLldaVY6iJdJDmAxQkf3DTi1rNx5VFzZR_kEzq7uj7OLKx1EK1WA1u344Is_m1b_G_U6MudCr4kuDW5lzrF0V0yrie-45ydG7k7U2Ky9LQC0WZCt1xF-WDx3X_u9Vh1LiywBNo3jGFgI00NxeEXk_6OWGUDEaKCFKbh2hNZxv8FeG68qwHUvTyYQrMKv2n0yeAI.%26bt%3Ddbl%26ch%3DAQEAEAABABRaung3lxsP7zP6KpvmzVirkNLdm8L31PE.%26mac%3DAQEAEAABABTNJh-SZrVtr2uOWNrPU1LpO1YHsE8ElEM.',
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