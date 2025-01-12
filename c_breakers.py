
from concurrent.futures import ThreadPoolExecutor, as_completed
from curses import panel
import random
import re
from wsgiref import headers


class Color:
    BLUE = '\033[94m'
    GREEN = '\033[1;92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    RESET = '\033[0m'
    ORANGE = '\033[38;5;208m'
    BOLD = '\033[1m'
    UNBOLD = '\033[22m'
    ITALIC = '\033[3m'
    UNITALIC = '\033[23m'

try:
    import os
    import sys
    import subprocess
    from colorama import Fore, Style, init
    from time import sleep
    from rich import print as rich_print
    from rich.panel import Panel
    from rich.table import Table
    import concurrent.futures
    from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
    from bs4 import BeautifulSoup
    import time
    import requests
    import urllib3
    from prompt_toolkit import prompt
    from prompt_toolkit.completion import PathCompleter
    import subprocess
    import sys
    import random
    from urllib.parse import urlparse, quote



    init(autoreset=True)

    def check_and_install_packages(packages):
        for package, version in packages.items():
            try:
                __import__(package)
            except ImportError:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', f"{package}=={version}"])

    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')



    def display_menu():
        title = """
    ████████╗      ████████╗ ███████╗ ████████╗██████╗  ██╗  ███╗███████╗███████  ████████╗
     ██╚════╝      ██╚═══╝██║██╚══╝██║██╚═════╝██╚═╝██║ ██║ ██║  ██╚════╝██╚══╝██║██╚═════╝
    ██║            ████████║ ████████║████████║████████║████║    ███████║████████║████████║
    ██║            ██║    ██║██   ██║ ██║      ██║  ██║ ██║ ██║  ██║     ██║  ██║       ██║
    ████████╗ ███╗ ███████╗  ██╗   ██╗ ███████╗██╗  ██╗ ██╗  ███╗ ██████ ██╗   ██╗████████╗
    ╚═══════╝ ╚══╝ ╚══════╝  ╚═╝   ╚═╝ ╚══════╝╚═╝  ╚═╝ ╚═╝  ╚══╝ ╚════╝ ╚═╝   ╚═╝╚═══════╝
    """
        print(Color.ORANGE + Style.BRIGHT + title.center(63))
        print(Fore.WHITE + Style.BRIGHT + "─" * 63)
        border_color = Color.CYAN + Style.BRIGHT
        option_color = Fore.WHITE + Style.BRIGHT  
        
        print(border_color + "┌" + "─" * 61 + "┐")
        
        options = [
            "1] Exit",
            "2] XSS Scanner"
            
        ]
        
        for option in options:
            print(border_color + "│" + option_color + option.ljust(59) + border_color + "│")
        
        print(border_color + "└" + "─" * 61 + "┘")
        authors = "Created by: Akmal, Deyrrel, Syed"
        instructions = "Select an option by entering the corresponding number:"
        
        print(Fore.WHITE + Style.BRIGHT + "─" * 63)
        print(Fore.WHITE + Style.BRIGHT + authors.center(63))
        print(Fore.WHITE + Style.BRIGHT + "─" * 63)
        print(Fore.WHITE + Style.BRIGHT + instructions.center(63))
        print(Fore.WHITE + Style.BRIGHT + "─" * 63)

    def print_exit_menu():
        clear_screen()

        panel = Panel(
            """        
   
  Credit - Akmal x Deyrrel x Syed
            """,
            style="bold green",
            border_style="blue",
            expand=False
        )
        rich_print(panel)
        print(Color.RED + "\n\nSession Off ...\n")
        exit()




    def run_xss_scanner():
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        import argparse
        import subprocess
        import sys
        import time
        import aiohttp
        import asyncio
        import logging
        import os
        from colorama import Fore, init
        from urllib.parse import urlencode, parse_qs, urlsplit, urlunsplit
        from prompt_toolkit import prompt
        from prompt_toolkit.completion import PathCompleter
        from rich import print as rich_print
        from rich.panel import Panel
        from rich.table import Table
        from requests.adapters import HTTPAdapter
        from urllib3.util.retry import Retry
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service as ChromeService
        from selenium.webdriver.common.by import By
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from webdriver_manager.chrome import ChromeDriverManager
        import logging
        logging.getLogger('WDM').setLevel(logging.ERROR)


        init(autoreset=True)
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

        USER_AGENTS = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Version/14.1.2 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/91.0.864.70",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/89.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:91.0) Gecko/20100101 Firefox/91.0",
        "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Mobile Safari/537.36",
            ]
        WAF_SIGNATURES = {
            'Cloudflare': ['cf-ray', 'cloudflare', 'cf-request-id', 'cf-cache-status'],
            'Akamai': ['akamai', 'akamai-ghost', 'akamai-x-cache', 'x-akamai-request-id'],
            'Sucuri': ['x-sucuri-id', 'sucuri', 'x-sucuri-cache'],
            'ModSecurity': ['mod_security', 'modsecurity', 'x-modsecurity-id', 'x-mod-sec-rule'],
            'Barracuda': ['barra', 'x-barracuda', 'bnmsg'],
            'Imperva': ['x-cdn', 'imperva', 'incapsula', 'x-iinfo', 'x-cdn-forward'],
            'F5 Big-IP ASM': ['x-waf-status', 'f5', 'x-waf-mode', 'x-asm-ver'],
            'DenyAll': ['denyall', 'sessioncookie'],
            'FortiWeb': ['fortiwafsid', 'x-fw-debug'],
            'Jiasule': ['jsluid', 'jiasule'],
            'AWS WAF': ['awswaf', 'x-amzn-requestid', 'x-amzn-trace-id'],
            'StackPath': ['stackpath', 'x-sp-url', 'x-sp-waf'],
            'BlazingFast': ['blazingfast', 'x-bf-cache-status', 'bf'],
            'NSFocus': ['nsfocus', 'nswaf', 'nsfocuswaf'],
            'Edgecast': ['ecdf', 'x-ec-custom-error'],
            'Alibaba Cloud WAF': ['ali-cdn', 'alibaba'],
            'AppTrana': ['apptrana', 'x-wf-sid'],
            'Radware': ['x-rdwr', 'rdwr'],
            'SafeDog': ['safedog', 'x-sd-id'],
            'Comodo WAF': ['x-cwaf', 'comodo'],
            'Yundun': ['yundun', 'yunsuo'],
            'Qiniu': ['qiniu', 'x-qiniu'],
            'NetScaler': ['netscaler', 'x-nsprotect'],
            'Securi': ['x-sucuri-id', 'sucuri', 'x-sucuri-cache'],
            'Reblaze': ['x-reblaze-protection', 'reblaze'],
            'Microsoft Azure WAF': ['azure', 'x-mswaf', 'x-azure-ref'],
            'NAXSI': ['x-naxsi-sig'],
            'Wallarm': ['x-wallarm-waf-check', 'wallarm'],
        }

        def check_and_install_packages(packages):
            for package, version in packages.items():
                try:
                    __import__(package)
                except ImportError:
                    subprocess.check_call([sys.executable, '-m', 'pip', 'install', f"{package}=={version}"])

        def clear_screen():
            os.system('cls' if os.name == 'nt' else 'clear')


        def get_random_user_agent():
            return random.choice(USER_AGENTS)

        def get_retry_session(retries=3, backoff_factor=0.3, status_forcelist=(500, 502, 504)):
            session = requests.Session()
            retry = Retry(
                total=retries,
                read=retries,
                connect=retries,
                backoff_factor=backoff_factor,
                status_forcelist=status_forcelist,
            )
            adapter = HTTPAdapter(max_retries=retry)
            session.mount('http://', adapter)
            session.mount('https://', adapter)
            return session
        
        def detect_waf(url, headers):
            session = get_retry_session()
            waf_detected = None

            try:
                response = session.get(url, headers=headers, verify=False)
                for waf_name, waf_identifiers in WAF_SIGNATURES.items():
                    if any(identifier in response.headers.get('server', '').lower() for identifier in waf_identifiers):
                        print(f"{Fore.GREEN}[+] WAF Detected: {waf_name}{Fore.RESET}")
                        waf_detected = waf_name
                        break
            except requests.exceptions.RequestException as e:
                logging.error(f"Error detecting WAF: {e}")

            if not waf_detected:
                print(f"{Fore.GREEN}[+] No WAF detected.{Fore.RESET}")
            
            return waf_detected

        class MassScanner:
            def __init__(self, urls, output, concurrency, timeout, payload_file, auto_continue=False):
                self.urls = urls
                self.output = output
                self.payloads = self.load_payloads(payload_file)
                self.concurrency = concurrency
                self.timeout = timeout
                self.auto_continue = auto_continue
                self.payload_file = payload_file
                self.injectables = []
                self.totalFound = 0
                self.totalScanned = 0
                self.t0 = time.time()
                self.first_vulnerability_prompt = True

            @staticmethod
            def load_payloads(payload_file):
                payloads = []

                if payload_file:
                    try:
                        with open(payload_file, "r") as file:
                            payloads = [line.strip() for line in file if line.strip()]
                            if not payloads:
                                raise ValueError("Payload file is empty.")
                            print(f"{Fore.YELLOW}\n[i] Payloads loaded from file.")
                    except Exception as e:
                        logging.error(f"Error loading payload file: {payload_file}. Exception: {str(e)}\n")
                        print(f"{Fore.RED}[!] Error loading payload file. Please check the file and try again.")
                        sys.exit(1)
                else:
                    print(f"{Fore.RED}[!] No payload file provided. Exiting.")
                    sys.exit(1)
                        
                return payloads

            def generate_payload_urls(self, url, payload):
                url_combinations = []
                try:
                    scheme, netloc, path, query_string, fragment = urlsplit(url)
                    if not scheme:
                        scheme = 'http'
                    query_params = parse_qs(query_string, keep_blank_values=True)
                    for key in query_params.keys():
                        modified_params = query_params.copy()
                        modified_params[key] = [payload]
                        modified_query_string = urlencode(modified_params, doseq=True)
                        modified_url = urlunsplit((scheme, netloc, path, modified_query_string, fragment))
                        url_combinations.append(modified_url)
                except Exception as e:
                    logging.error(f"Error generating payload URL for {url} with payload {payload}: {str(e)}")
                return url_combinations

            async def fetch(self, sem: asyncio.Semaphore, session: aiohttp.ClientSession, url: str):
                async with sem:
                    try:
                        response_text = ""
                        async with session.get(url, allow_redirects=True) as resp:
                            response_headers = resp.headers
                            content_type = response_headers.get("Content-Type", "")
                            content_length = int(response_headers.get("Content-Length", -1))

                            if "text/html" in content_type and (content_length < 0 or content_length <= 1000000):
                                content = await resp.read()
                                encoding = 'utf-8'
                                response_text = content.decode(encoding, errors="ignore")
                            else:
                                logging.info(f"Skipping URL due to content type or size: {url}")
                    except asyncio.TimeoutError:
                        logging.warning(f"Request timed out for {url}")
                    except Exception as e:
                        logging.error(f"Error fetching {url}: {str(e)}")
                            
                    await asyncio.sleep(0)
                    return (response_text, url)

            def process_tasks(self, done):
                for response_text, url in done:
                    self.totalScanned += 1
                    chrome_options = Options()
                    chrome_options.add_argument("--headless") 
                    service = ChromeService(executable_path=ChromeDriverManager().install())
                    driver = webdriver.Chrome(service=service, options=chrome_options)

                    try:
                        driver.get(url)

                        try:
                            WebDriverWait(driver, 1).until(EC.alert_is_present())
                            alert = driver.switch_to.alert
                            print(Color.GREEN + f"Vulnerable URL : {url}")
                            alert.dismiss() 
                            self.injectables.append(url)
                        except:
                            print(Color.RED + "Not vulnerable")
                    finally:
                        driver.quit()

            async def scan(self):
                sem = asyncio.Semaphore(self.concurrency)
                timeout = aiohttp.ClientTimeout(total=self.timeout)

                async with aiohttp.ClientSession(timeout=timeout, connector=aiohttp.TCPConnector(ssl=False, limit=0, enable_cleanup_closed=True)) as session:
                    for payload in self.payloads:
                        print(f"{Fore.YELLOW}[i] Scanning with payload: {payload}\n")
                        pending = []
                        for url in self.urls:
                            urls_with_payload = self.generate_payload_urls(url.strip(), payload)
                            for payload_url in urls_with_payload:
                                pending.append(asyncio.ensure_future(self.fetch(sem, session, payload_url)))

                            if len(pending) >= self.concurrency:
                                done = await asyncio.gather(*pending)
                                self.process_tasks(done)
                                pending = []

                        if pending:
                            done = await asyncio.gather(*pending)
                            self.process_tasks(done)

                        if self.payload_file:
                            if self.totalFound > 0:
                                if self.first_vulnerability_prompt and not self.auto_continue:
                                    continue_scan = input(f"{Fore.CYAN}\n[?] Vulnerability found. Do you want to continue testing other payloads? (y/n, press Enter for n): ").strip().lower()
                                    if continue_scan != 'y':
                                        break
                                    self.first_vulnerability_prompt = False
                                elif not self.auto_continue:
                                    self.first_vulnerability_prompt = False


            def save_injectables_to_file(self):
                if self.injectables:
                    with open(self.output, "w") as output_file:
                        for url in self.injectables:
                            output_file.write(url + "\n")
                    print(f"{Fore.GREEN}[+] Vulnerable URLs saved to {self.output}")


            def run(self):
                asyncio.run(self.scan())

                print(f"{Fore.YELLOW}\n[i] Scanning finished.")
                print(f"{Fore.YELLOW}[i] Total scanned: {self.totalScanned}")
                print(f"{Fore.YELLOW}[i] Time taken: {int(time.time() - self.t0)} seconds\n")
                print(f"{Fore.GREEN}[i] Vulnerabilities found: {len(self.injectables)}")

                if self.injectables:  
                    save_option = input(f"{Fore.CYAN}[?] Do you want to save the vulnerable URLs to {self.output}? (y/n, press Enter for n): ").strip().lower()
                    if save_option == 'y':
                        self.save_injectables_to_file()
                        os._exit(0)
                    else:
                        print(f"{Fore.YELLOW}Vulnerable URLs will not be saved.")
                        os._exit(0)
                else:
                    print(f"{Fore.YELLOW}No vulnerabilities found. No URLs to save.")
                    os._exit(0)


                                    
            def save_injectables_to_file(self):
                with open(self.output, "w") as output_file:
                    for url in self.injectables:
                        output_file.write(url + "\n")

        def get_file_path(prompt_text):
            completer = PathCompleter()
            return prompt(prompt_text, completer=completer).strip()

        def prompt_for_urls():
            while True:
                try:
                    url_input = None
                    if url_input:
                        if not os.path.isfile(url_input):
                            raise FileNotFoundError(f"File not found: {url_input}")
                        with open(url_input) as file:
                            urls = [line.strip() for line in file if line.strip()]
                        return urls
                    else:
                        single_url = input(f"{Fore.CYAN}[?] Enter a single URL to scan: ").strip()
                        if single_url:
                            return [single_url]
                        else:
                            print(f"{Fore.RED}[!] You must provide either a file with URLs or a single URL.")
                            input(f"{Fore.YELLOW}[i] Press Enter to try again...")
                            clear_screen()

                            print(f"{Fore.GREEN}Welcome to the xlsNinja XSS-Scanner! - AnonKryptiQuz x Coffinxp x Hexsh1dow x Naho\n")
                except Exception as e:
                    print(f"{Fore.RED}[!] Error reading input file: {url_input}. Exception: {str(e)}")
                    input(f"{Fore.YELLOW}[i] Press Enter to try again...")
                    clear_screen()

                    print(f"{Fore.GREEN}Welcome to the xlsNinja XSS-Scanner! - AnonKryptiQuz x Coffinxp x Hexsh1dow x Naho\n")

        def prompt_for_valid_file_path(prompt_text):
            while True:
                file_path = get_file_path(prompt_text).strip()
                if not file_path:
                    print(f"{Fore.RED}[!] You must provide a file containing the Payloads.")
                    input(f"{Fore.YELLOW}[i] Press Enter to try again...")
                    clear_screen()
                    print(f"{Fore.GREEN}Welcome to the xlsNinja XSS-Scanner! - AnonKryptiQuz x Coffinxp x Hexsh1dow x Naho\n")
                    continue
                if os.path.isfile(file_path):
                    return file_path
                else:
                    print(f"{Fore.RED}[!] Error reading input file: {file_path}.")
                    input(f"{Fore.YELLOW}[i] Press Enter to try again...")
                    clear_screen()
                    print(f"{Fore.GREEN}Welcome to the xlsNinja XSS-Scanner! - AnonKryptiQuz x Coffinxp x Hexsh1dowx Naho\n")

        def main():
            clear_screen()
            required_packages = {
                'aiohttp': '3.8.6',
                'requests': '2.28.1',
                'prompt_toolkit': '3.0.36',
                'colorama': '0.4.6'
            }

            check_and_install_packages(required_packages)
            
            time.sleep(3)
            clear_screen()
            panel = Panel("""
   _  __________  ____________   _  ___  __________
  | |/_/ __/ __/ / __/ ___/ _ | / |/ / |/ / __/ _  |
 _>  <_\ \_\ \  _\ \/ /__/ __ |/    /    / _// , _/
/_/|_/___/___/ /___/\___/_/ |_/_/|_/_/|_/___/_/|_| 
                                                   
                                """,
                style="bold green",
                border_style="blue",
                expand=False
            )
            
            rich_print(panel, "\n")

            print(Fore.GREEN + "Welcome to the XSS Testing Tool!\n")
            urls = prompt_for_urls()

            payload_file = prompt_for_valid_file_path("[?] Enter the path to the payload file: ")

            output_file = "vulnerable_urls.txt"
            concurrency = int(input("\n[?] Enter the number of concurrent threads (0-10, press Enter for 5): ").strip() or 5)
            timeout = float(input("[?] Enter the request timeout in seconds (press Enter for 3): ").strip() or 3)
                                
            print(f"\n{Fore.YELLOW}[i] Loading, Please Wait...")
            time.sleep(3)
            clear_screen()
            print(f"{Fore.CYAN}[i] Starting scan...")
            print(f"{Fore.CYAN}[i] Checking for WAF on target URLs...")

            for url in urls:
                headers = {'User-Agent': get_random_user_agent()}
                detect_waf(url, headers)

            scanner = MassScanner(
                urls=urls,
                output=output_file,
                concurrency=concurrency,
                timeout=timeout,
                payload_file=payload_file,
                auto_continue='n'
            )

            scanner.run()

        if __name__ == "__main__":
            try:
                main()
            except KeyboardInterrupt:
                sys.exit(0)


    

        if __name__ == "__main__":
            try:
                main()
            except KeyboardInterrupt:
                sys.exit(0)
            except Exception as e:
                print(Fore.RED + f"[!] An unexpected error occurred: {e}")
                sys.exit(1)


    def handle_selection(selection):
        if selection == '1':
            clear_screen()
            print_exit_menu()

        elif selection == '2':
            clear_screen()
            run_xss_scanner()
        
        else:
            print_exit_menu()

    def main():
        clear_screen()
        required_packages = {
            'aiohttp': '3.8.6',
            'requests': '2.28.1',
            'prompt_toolkit': '3.0.36',
            'colorama': '0.4.6'
        }

        check_and_install_packages(required_packages)

        sleep(3)
        clear_screen()

        while True:
            display_menu()
            choice = input(f"\n{Fore.CYAN}[?] Select an option (0-2): {Style.RESET_ALL}").strip()
            handle_selection(choice)

    if __name__ == "__main__":
        try:
            main()
        except KeyboardInterrupt:
            print_exit_menu()
            sys.exit(0)

except KeyboardInterrupt:
    print_exit_menu()
    sys.exit(0)