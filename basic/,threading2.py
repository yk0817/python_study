import threading,time,urllib2

def get_html(url):
    current_time = time.time()
    response = urllib2.urlopen(url)
    html = response.read()
    print(url + ':' + str(time.time() - current_time))
    urls = ['http://www.google.com', 'http://www.yahoo.co.jp/', 'https://www.bing.com/']
    threads = []

    # Start threads
    current_time = time.time()
    for url in urls:
        thread = threading.Thread(target=get_html,args=(url,))
        thread.start()
        threads.append(thread)

    # wait threads
    for thread in threads:
        thread.join()

    print('Time: ' + str(time.time() - current_time))
