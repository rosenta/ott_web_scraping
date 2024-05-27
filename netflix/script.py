import logging
from mitmproxy import http

def request(flow: http.HTTPFlow):
    if "netflix.com/nq/website/memberapi" in flow.request.pretty_url:
        if hasattr(flow.request.data, 'content'):
            content = flow.request.data.content
            content = content.decode('utf-8')
            index = content.find("videos")
            if index >= 0:
                index2 = 0
                while content[index2 + 3] != '%':
                    index = content.find("%2C", index)
                    while content[index + 3] == '%':
                        index += 3
                    index2 = content.find("%", index + 3)
                    logging.info(content[index + 3:index2])
                    index = index2
