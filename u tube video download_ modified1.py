import os
from pytube import YouTube

while True:
    link = input("Enter the URL of the video: ")
    
    # if video is found
    try:
        mainVideo = YouTube(link)
        print("Fetching data...")
        print("\nTitle: ",mainVideo.title)
        download = input("Enter 'D' to download and 'N' to skip: ")
        
        # if wrong choice download or quit
        while download!='D' and download!='N':
            download = input("Wrong choice! enter either 'D' or 'N': ")
         
        # if download
        if download=='D':
            choice = input("Enter 1 to download audio only and 2 to download video: ")
            
            # if wrong choice audio or video
            while choice!='1' and choice!='2':
                choice = input("Wrong choice! enter either 1 or 2: ")
                    
            # if audio download
            if choice=='1':
                print("Loading all audio streams...")
                streams = mainVideo.streams.filter(only_audio=True)
                list_of_streams = list(streams)
                print("\nAll audio streams in the video:")
                for i in range(len(list_of_streams)):
                    print("index:",i+1,"  ",list_of_streams[i])
                choice_stream = input("Enter the stream index according to which stream you want to download: ")
                
                # if choice of stream is wrong
                while choice_stream.isnumeric()==False or int(choice_stream)<1 or int(choice_stream)>len(list_of_streams):
                    choice_stream = input("stream index is out of range! choose the correct stream: ")
                
                # if correct choice then download
                print("Downloading...")
                os.chdir("C:\\Users\\PRITAM\\Downloads")
                downloaded_file = streams[int(choice_stream)-1].download()
                base, ext = os.path.splitext(downloaded_file)
                new_file = base+'.mp3'
                os.rename(downloaded_file, new_file)
                print("\nSuccessfully downloaded!")
                print("File is stored at:",os.getcwd())
                  
            # if video download
            if choice=='2':
                print("Loading all video streams...")
                streams = mainVideo.streams.filter.all()
                list_of_streams = list(streams)
                print("\nAll video streams in the video:")
                for i in range(len(list_of_streams)):
                    print("index:",i+1,"  ",list_of_streams[i])
                choice_stream = input("Enter the stream index according to which stream you want to download: ")
                
                # if choice of stream is wrong
                while choice_stream.isnumeric()==False or int(choice_stream)<1 or int(choice_stream)>len(list_of_streams):
                    choice_stream = input("stream index is out of range! choose the correct stream: ")
                
                # if correct choice then download
                print("Downloading...")
                os.chdir("C:\\Users\\PRITAM\\Downloads")
                streams[int(choice_stream)-1].download()
                print("\nSuccessfully downloaded!")
                print("File is stored at:",os.getcwd())        
        
    # if video is not found
    except Exception:
        print("cannot find video")