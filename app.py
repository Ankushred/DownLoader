import subprocess
import os
def youtube_fun():
    url = input("Enter Url:")
    dict ={
        "0":"251/140/250/249/600/599/234/233",#mp3
        "1":"18+bestaudio/605+bestaudio/231+bestaudio/396+bestaudio/bestvideo+bestaudio",#360p
        "2":"606+bestaudio/135+bestaudio/397+bestaudio/244+bestaudio/bestvideo+bestaudio",#480p
        "3":"311+bestaudio/612+bestaudio/298+bestaudio/302+bestaudio/398+bestaudio/136+bestaudio/247+bestaudio/bestvideo+bestaudio",#7200p
        "4":"312+bestaudio/299+bestaudio/617+bestaudio/399+bestaudio/303+bestaudio/bestvideo+bestaudio",#1080p
        "5":"623+bestaudio/308+bestaudio/400+bestaudio/bestvideo+bestaudio",#1440p
        "6":"401+bestaudio/628+bestaudio/401+bestaudio/bestvideo+bestaudio",#2160p
        "7":"bestvideo+bestaudio"#4320p  
    }
    print("0.Mp3")
    print("1.360p")
    print("2.480p")
    print("3.720p")
    print("4.1080p60")
    print("5.1440p60")
    print("6.4k60")
    print("7.8k60")
    choice=(input("Enter Quality..."))
    script_path =  os.path.dirname(os.path.abspath(__file__))
    command = ["yt-dlp", "-f",dict[choice],"-P",script_path+"//videos", url]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print("DownLoaded!!")
        print("DownLoaded!!")
        print("DownLoaded!!")
    except subprocess.CalledProcessError as e:
        print("Error occurred:")
        print("Output:", e.stdout)
        print("Error:", e.stderr)

print("1.\033[32mYoutube Downloader\033[0m")
print("2.Instagram Downloader")
print("3.Tiktok Downloader")
print("4.Facebook Downloader")
choice = int(input("Enter Your Choice:"))
if(choice==1):
    youtube_fun()
