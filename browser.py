# write your code here
import sys
import os
from collections import deque
import requests
from bs4 import BeautifulSoup
from colorama import Fore
url = ""
saved_page = deque()
content = ""


# read command-line argument (directory)
def check_dir(dir_name_from_argument):
    is_exist = os.access(dir_name_from_argument, os.F_OK)
    if not is_exist:
        os.makedirs(dir_name_from_argument)
        # save all the web pages that the user downloads in this folder.
        directory = dir_name_from_argument
        path_bloomberg = directory + "/bloomberg"
        path_nytimes = directory + "/nytimes"
        save_page("bloomberg.com")
        save_page("nytimes.com")
    else:
        pass


def save_file(url, dir_name_from_argument):
    save_page(url)
    global content
    if url == "https://bloomberg.com":
        new_file = "bloomberg"
        new_filename_path = dir_name_from_argument + "/bloomberg"
        with open(new_filename_path, "w", encoding="utf-8") as new_file1:
            # save it to a file in the aforementioned directory
            # write to new file
            new_file1.writelines(content)
    if url == "https://nytimes.com":
        new_file = "nytimes"
        save_page(new_file)
        new_filename_path = dir_name_from_argument + "/nytimes"
        with open(new_filename_path, "w", encoding="utf-8") as new_file2:
            # save it to a file in the aforementioned directory
            # write to new file
            new_file2.writelines(content)


def save_page(url):
    if url not in saved_page:
        saved_page.append(url)
    return saved_page


def print_content(url):
    global content
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        content = soup.get_text()
        for i in soup.find_all("a"):
            i.string = "".join([Fore.BLUE, i.get_text(), Fore.RESET])
            print(i.string)
    except requests.exceptions.ConnectionError:
        print("Incorrect URL")


args = sys.argv
input1 = args[1]
dir_name_from_argument = args[1]
check_dir(dir_name_from_argument)

input2 = input()
while input2 != "exit":
    if not input2.startswith("https://"):
        url = "https://" + str(input2)
    print_content(url)
    save_file(url, dir_name_from_argument)
    input2 = input()
    check_dir(dir_name_from_argument)
