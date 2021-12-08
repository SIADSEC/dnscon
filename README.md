# dnscon

dnscon, an active subdomain bruteforcing tool.

Usage: `python dnscon.py <domain>`

Options:

    "-l", "--wordlist",    "File that contains all subdomains", default="sub.txt"
    "-t", "--num-threads", "Number of threads to use. Default is 10", default=10, type=int
    "-o", "--output-file", "Specify the output text file to write discovered subdomains", default="Discovered_subdomains.txt"
