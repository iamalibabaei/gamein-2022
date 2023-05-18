from time import sleep

import requests

product_id = 201
line_id = 248
count = 1000

while True:
    res = requests.post(
        url="https://api-gamein.dariahamrah.ir/service/line/start",
        json={"lineId": line_id, "count": count, "productId": product_id},
        headers={
            "accept": "application/json, text/plain, */*",
            "accept-language": "en-US,en;q=0.9",
            "authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODUwIiwiaWF0IjoxNjg0MzI2NzQ2LCJleHAiOjE2ODQ0MTMxNDZ9.tdhfJX1ukm0i-Wbic_Rmv9jtb8FnFJe3q-Q85BcI5Rd0bW5i5V4ZJahLU9hfRWheTdy12Xn-gvZlEgdFsPKGHg",
            "content-type": "application/json",
            "sec-ch-ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Linux"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "Referer": "https://gamein.dariahamrah.ir/",
            "Referrer-Policy": "strict-origin-when-cross-origin",
            "Origin": "https://gamein.dariahamrah.ir",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        }
    )
    if res.status_code == 200:
        sleep(120)
    else:
        print(res.json())
