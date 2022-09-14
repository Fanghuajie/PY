import json

import requests


class RequestUtil:
    # 建立会话
    session = requests.session()

    def request_api(self, method, url, data, **kwargs):
        method = str(method).lower()
        req = None
        if method == 'get':
            req = RequestUtil.session.request(method, url=url, params=data, **kwargs)
        else:
            # data = json.dumps(data)
            req = RequestUtil.session.request(method, url=url, data=data, **kwargs)
        return req
