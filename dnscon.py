import requests
from threading import Thread, Lock
from queue import Queue

q = Queue()
list_lock = Lock()
discovered_domains = []

def scan_subdomains(domain):
    global q
    while True:
        subdomain = q.get()
        url = f"http://{subdomain}.{domain}"
        sub = f"{subdomain}.{domain}"
        try:
            requests.get(url)
        except requests.ConnectionError:
            pass
        else:
            print(sub)
            with list_lock:
                discovered_domains.append(sub)
        q.task_done()


def main(domain, n_threads, subdomains):
    global q
    for subdomain in subdomains:
        q.put(subdomain)

    for t in range(n_threads):
        worker = Thread(target=scan_subdomains, args=(domain,))
        worker.daemon = True
        worker.start()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Subdomain Scanner By SiadSec")
    parser.add_argument("domain", help="Domain to Scan")
    parser.add_argument("-l", "--wordlist", help="File that contains all subdomains", default="sub.txt")
    parser.add_argument("-t", "--num-threads", help="Number of threads to use. Default is 10", default=10, type=int)
    parser.add_argument("-o", "--output-file", help="Specify the output text file to write discovered subdomains", default="Discovered_subdomains.txt")
    
    args = parser.parse_args()
    domain = args.domain
    wordlist = args.wordlist
    num_threads = args.num_threads
    output_file = args.output_file

    main(domain=domain, n_threads=num_threads, subdomains=open(wordlist).read().splitlines())
    q.join()

    with open(output_file, "w") as f:
        for sub in discovered_domains:
            print(sub, file=f)
exit()