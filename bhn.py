import requests

from bs4 import BeautifulSoup
import json
number="01616858069"
headers={




"Cookie":"_ga=GA1.3.1129180962.1707931645; _gid=GA1.3.548974722.1707931646; _gat_gtag_UA_250674246_1=1; _fbp=fb.2.1707931647560.139901178; XSRF-TOKEN=eyJpdiI6IkZra0R5M0lDT1NZRFBRcTN3eDkrSnc9PSIsInZhbHVlIjoiTlJrVklnN2owclpnV1VWZ0dZRkVldGIxTTh0Tm9ESmNLSU1vbjI3QUFMKzA1M0dhZ3VwcElRczd5NjMyeHBLWktBRE82ekF1Vy8yemJ0M1VhUEpOU1Zxc1NYOGJqR3ZTRFp1azBjd0I0T3JwcnlwMlB3dEhXNENqTzN4emtFREEiLCJtYWMiOiIyOGQwNGE4MDMzNDQxZDQ0YjVjYWExMjMxYzg2NTVhNjUxMjg2ZWU2MmZhZGIyMDczODEyZjMxMTdkMWRiMmJjIiwidGFnIjoiIn0%3D; bhn_store_pwa_session=eyJpdiI6ImRWYzFVUzl4N2E4RkJLMkxpa0o3Nmc9PSIsInZhbHVlIjoiTE90QXBlTGlTcmxCY0NHQjNKdUNSb2ZNMTcrYVhDNDBhRm1UM3p1VGdHeXBWZmhPZEV4ZXFCZVJObGtqMnZDbkd1SXRiZlRmbFNhODlaemhITXM2Z1ZwMVFUb3VzanJ2YW5GMWdEdlJjUVhHeFlwbHBwalpleEtzUnBvR0hyNysiLCJtYWMiOiI5ZGI4ZGFmNjlhNmU1ZDI0OGFkNmM0NjY4MGE5ZGVjNGRjZGE0MzBiOTlmMGY3YTQ3NjAxMTNlMTdhZjI3Mjk2IiwidGFnIjoiIn0%3D; _ga_BGV7FV199E=GS1.1.1707931644.1.1.1707931663.41.0.0",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}
soup = BeautifulSoup(requests.get("https://www.buyherenow.com.bd/auth/register",headers=headers).text, 'html.parser')
token = soup.find("input", {"name": "_token"}).get("value")
x=requests.post("https://www.buyherenow.com.bd/auth/register/otp",json={
    "name": "Md Pudina",
    "phone_number": "01616858069",
    "email": "hedargmai12@gmail.com",
    "password": "01815688183",
    "password_confirmation": "01815688183",
    "token": None,
    "otp_code": "",
    "newsletter": True
},headers={
"Accept": "text/html, application/xhtml+xml",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-BD,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://www.buyherenow.com.bd",
    "Referer": "https://www.buyherenow.com.bd/auth/register",
    "Sec-Ch-Ua": '"Not_A Brand";v="8", "Chromium";v="120"',
    "Sec-Ch-Ua-Mobile": "?1",
    "Sec-Ch-Ua-Platform": '"Android"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "X-Inertia-Version": "9f30a7026045e9cc0f0f9291ebea3d6f",
    "X-Requested-With": "XMLHttpRequest",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
"Cookie":"_ga=GA1.3.1129180962.1707931645; _gid=GA1.3.548974722.1707931646; _gat_gtag_UA_250674246_1=1; _fbp=fb.2.1707931647560.139901178; XSRF-TOKEN=eyJpdiI6IkZra0R5M0lDT1NZRFBRcTN3eDkrSnc9PSIsInZhbHVlIjoiTlJrVklnN2owclpnV1VWZ0dZRkVldGIxTTh0Tm9ESmNLSU1vbjI3QUFMKzA1M0dhZ3VwcElRczd5NjMyeHBLWktBRE82ekF1Vy8yemJ0M1VhUEpOU1Zxc1NYOGJqR3ZTRFp1azBjd0I0T3JwcnlwMlB3dEhXNENqTzN4emtFREEiLCJtYWMiOiIyOGQwNGE4MDMzNDQxZDQ0YjVjYWExMjMxYzg2NTVhNjUxMjg2ZWU2MmZhZGIyMDczODEyZjMxMTdkMWRiMmJjIiwidGFnIjoiIn0%3D; bhn_store_pwa_session=eyJpdiI6ImRWYzFVUzl4N2E4RkJLMkxpa0o3Nmc9PSIsInZhbHVlIjoiTE90QXBlTGlTcmxCY0NHQjNKdUNSb2ZNMTcrYVhDNDBhRm1UM3p1VGdHeXBWZmhPZEV4ZXFCZVJObGtqMnZDbkd1SXRiZlRmbFNhODlaemhITXM2Z1ZwMVFUb3VzanJ2YW5GMWdEdlJjUVhHeFlwbHBwalpleEtzUnBvR0hyNysiLCJtYWMiOiI5ZGI4ZGFmNjlhNmU1ZDI0OGFkNmM0NjY4MGE5ZGVjNGRjZGE0MzBiOTlmMGY3YTQ3NjAxMTNlMTdhZjI3Mjk2IiwidGFnIjoiIn0%3D; _ga_BGV7FV199E=GS1.1.1707931644.1.1.1707931663.41.0.0",
"X-Csrf-Token":token,
"X-Requested-With":"XMLHttpRequest"})
print(x.text)