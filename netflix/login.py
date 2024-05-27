import json
import requests

def login_to_netflix(username, password):
    headers = {
        'authority': 'www.netflix.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'en-GB,en;q=0.9',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.netflix.com',
        'referer': 'https://www.netflix.com/in/login',
        'sec-ch-ua': '"Brave";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"macOS"',
        'sec-ch-ua-platform-version': '"13.6.0"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }

    data = {
        'userLoginId': username,
        'password': password,
        'rememberMe': 'true',
        'flow': 'websiteSignUp',
        'mode': 'login',
        'action': 'loginAction',
        'withFields': 'rememberMe,nextPage,userLoginId,password,countryCode,countryIsoCode,recaptchaResponseToken,recaptchaError,recaptchaResponseTime',
        'authURL': '1697064441102.7hV02W+gKWfUta1ZbHpp3y6LaMA=',
        'nextPage': '',
        'showPassword': '',
        'countryCode': '+91',
        'countryIsoCode': 'IN',
        'cancelType': '',
        'cancelReason': '',
        'recaptchaResponseToken': '03AFcWeA4mKvCvQ9gSxcTCfLcV8ZCYIQ22MLbaCugLIW_fLAztG7Il9bai1n4uPfz4f8gJCCZDDfLcuRDuzE0S96HW6t4NuQs04SeNy60DmeJbV133t7l5TBiF8FZIuKUXDwIhSW7fjiMePbkrr4F3-6f1paQiqfqj5YGlIYg9hgiavCwwQ7YHNG5e2zeVdi5bAIjc0U7fUkW-ZjhtcH12j683z-8w-MPcqEPporyFGsHQqIP7ILqPmqxEDh4SrZnm1FazXMLg6yVLv3LM0zlCyNckPRNagFTGdqkVRUExrcQUa8Y4urovaUL-Ed_B3nnh3HCYfVzSsPdbzJmk76JYArCnY67NUXEfdj7w5Y8DcyU--N3Uvn9BnZh-8bV2c2QW6aEEkAvIAEfgaZNU09Yc24aQzXG_2qyIOCg_Pw5aFXAzb-dvtW2R_kcRPY3MQJgsWv5iZ-5NOBfDXGaM7YU078WuX6Q-yQwwKJEMS0OUxtjAYE8-dUvJHhMiDd-ZRIZuKoedyAXhVgz5kE_ADGfJRWVsF_9tal29rS29H1ngt8VGQqgJOoRd7ygxRPKhLjTjF54UykG9Y9ikhtiyOltmjqJOgklH7ByvikrET4Qm7vfhuJ3CqOBMzRjBCJeZIwhiRQufCnrmEytw9QJ9g8WRDgqXgTeMogZIKaRedDTW9cS0V22XsWpR5KN37dgrSsBvJf9PTOe5JXYj6bvyW7-UDrDMH_S-IjFcBhXQE_PIegKOaYCyM1HzoCvsPtGqfkdeZMiSfgQb5xA1leq6M3KPGhKZQj87Xy1j4YW5MsxO8gTxbAIemhTCJGJKwnyJXooud4UDWi88dnLD1owWTKnpfgvTfAAwz6gnSmeuv5FMuwiUetnDkRy3GYz2QpUX84NkzD0m9x561-NEo1_fqBFv-TiXRrR68WN496xPhBW3AjJIhiFb-y3z7lWMePm-BxynCWYjoIvYevXtqpS9sTOD1B4xDH-Lz9C_duvFPEy7jJ7yMBM_j2SbmQpCpcJm9z96Y67LYn_ZbplbKe5r6Zz2w1cJnAGDc7p28xVHr6ybc-TmUrxWuPxAegytgw_b_nOaGO3l1QL1WptoYOOgTwPIloKAtDX2D-xqUbMnKA0b-6TuWfZp5rZZ3OVu0V7aXo6foKAxPC3nB1-4imx8kSfbZtEnckGJJpd1Feex6zXHzqAJwL9iPDopWa0FdS82vIPyN5aE6SG2EKYMWieMG_nNbusFWTIjsc-bySVwt3Ruy44CQ8VWLkanuLukyOETDGx_drl3FAxwWM2iZkJ2rWMnDxo3CcDysTfGCGJZPk9ChF_hfI2k6fXTDPnVkj12_LDvxuXAoN97WZ1M7J94O9vrpdApbNqe75l1HsFOIDFB4u0uwkpD8mJWGCWaD99kAmQhvadH2dz5E0sNuY3KvgtZH_rbNBAHi1FgQJBwVxi1A1SXPGe5FtvVivcjDftC7flAyk8guuBsIdGGHg72Xtxc_NEQaI4VKYGcCiEO588Z0dt1vlJ3x58R0MzT_oQyvgyfUlYPuzNdYAnY',
        'recaptchaResponseTime': '254',
    }

    response = requests.post('https://www.netflix.com/in/login', headers=headers, data=data)

    cookies_dict = response.cookies.get_dict()
    return cookies_dict, response.headers
