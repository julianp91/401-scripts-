#julian Pena
#https://www.analyticsvidhya.com/blog/2024/01/ways-to-convert-python-scripts-to-exe-files/
#https://hackerbase.pro/blog/1950
#I used ChatGPT because I could make it execute, and it looks like I made a few mistakes.

import os

def search_files():
    file_name = input("Enter the file name to search for: ")
    directory = input("Enter the directory to search in: ")

    files_searched = hits_found = 0

    for root, _, files in os.walk(directory):
        for file in files:
            if file == file_name:
                hits_found += 1
                print("Found:", os.path.join(root, file))
            files_searched += 1

    print("\nSearch completed.")
    print("Total files searched:", files_searched)
    print("Total hits found:", hits_found)

if __name__ == "__main__":
    search_files()
