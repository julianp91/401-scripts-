# julian pena
#https://www.youtube.com/watch?v=0MiWOIb0GfQ   all 3 parts 
# https://www.youtube.com/watch?v=IIvfqfKkiio
#This was the most challenging script I have encountered thus far. I feel that there are many missing components and that I did not fully comprehend the concept of this Python script. I had to resort to using ChatGPT because I was unable to find a solution on my own. Despite watching all three videos, I still require more information to complete this task effectively.

import os

def main():
    target = input("Enter URL or IP address: ")
    port = input("Enter port number: ")

    print("\nNetcat banner grab:")
    os.system(f'nc -v -n {target} {port}')

    print("\nTelnet banner grab:")
    os.system(f'echo | telnet {target} {port}')

    print("\nNmap banner grab on well-known ports:")
    os.system(f'nmap -sV {target}')

if __name__ == "__main__":
    main()
