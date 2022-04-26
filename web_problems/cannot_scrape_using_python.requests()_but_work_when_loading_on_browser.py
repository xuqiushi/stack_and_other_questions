import socket

import requests

if __name__ == "__main__":
    from collections import OrderedDict
    from requests import Session
    import urllib.request

    headers = OrderedDict(
        {
            # "Accept-Encoding": "gzip, deflate, br",
            "Host": "raritysniffer.com",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
        }
    )

    response = urllib.request.Request(
        "https://raritysniffer.com/api/index.php?query=fetch&collection=0x6632a9d63e142f17a668064d41a21193b49b41a0&taskId=any&norm=true&partial=true&traitCount=true",
        headers=headers,
    )
    r = urllib.request.urlopen(response).read()
    print(r.decode("utf-8"))
    print(response)
    answers = socket.getaddrinfo("raritysniffer.com", 443)
    (family, type, proto, canonname, (address, port)) = answers[0]
    response = requests.get(
        f"http://{address}/api/index.php?query=fetch&collection=0x6632a9d63e142f17a668064d41a21193b49b41a0&taskId=any&norm=true&partial=true&traitCount=true",
        headers=headers,
        verify=False,
    )
    print(response)
