from django.shortcuts import render
from django.http import HttpResponse
import requests
from threading import Thread
from datetime import datetime, timedelta
import pytz
from store.models import contacts

def call(request):


    phone_number = request.GET["phone"].strip()

    if len(phone_number) == 11:
        phone_number = "88"+str(phone_number)



    def print_date_time(days):
        # Define the timezone for GMT+6
        tz = pytz.timezone('Asia/Dhaka')
        
        # Get the current date and time in UTC
        now_utc = datetime.now(pytz.utc)
        
        # Add the specified number of days
        future_date_utc = now_utc + timedelta(days=days)
        
        # Convert the future date to GMT+6
        future_date_gmt6 = future_date_utc.astimezone(tz)
        
        # Format the date and time
        formatted_date = future_date_gmt6.strftime("%Y-%m-%d %H:%M:%S")
        
        # Print the formatted date and time

        return str(formatted_date)

    message1 = "ভাই এটা প্রথম টেস্টিং মেসেজ যেটা সাথে সাথেই যায়। আরও একটা মেসেজ কাল যাবে। ভাল থাকেন"
    message2 = "ভাই, এটা সেকেন্ড মেসেজ। আজকে আসলো। আমাদের প্রোডাক্টে এনরোল করে ফেলেন।"
    message3 = "ভাই , এটা শেষ সুযোগ। আমরা ৫০% ডিস্কাউন্ট দিচ্ছি। এনরোল করেন"


    message_list = [message1,message2,message3]

    i=0

    api_key = "U3t1FG9gYXjXJkJ9S2HAw7nN6pvWZ59AgHtT39Kz"

    url_list = []

    for msg in message_list:
        message = msg.replace(" ","+")
        if i==0:
            url=f"https://api.sms.net.bd/sendsms?api_key={api_key}&msg={message}&to={phone_number}"
            url_list.append(url)
            i+=1

        
        else:
            get_date_time = print_date_time(i)
            url_format_datetime = get_date_time.replace(" ","+")
            url = f"https://api.sms.net.bd/sendsms?api_key={api_key}&msg={message}&to={phone_number}&schedule={url_format_datetime}"

            url_list.append(url)
            i+=1

    def fetch_url(url):
        try:
            response = requests.get(url)
            print(f"URL: {url} | Status Code: {response.status_code}")
        except requests.RequestException as e:
            print(f"URL: {url} | Error: {e}")

    
    threads = []

    '''
    for url in url_list:
        thread = Thread(target=fetch_url, args=(url,))
        threads.append(thread)
        thread.start()

    
    for thread in threads:
        thread.join()

    '''

    contacts.objects.create(phone_number=phone_number)

    
    
    return render(request,"video.html")
    






    
def index(request):
    if request.method == "GET":
        return render(request,"index.html")
