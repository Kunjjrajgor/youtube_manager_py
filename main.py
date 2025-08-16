
import json

def load_data():
    try:
        with open("youtube.txt",'r') as file:
            videos = json.load(file)
            return videos
    except FileNotFoundError:
        return []
    
def save_data(videos):
    with open("youtube.txt",'w') as file:
        json.dump(videos,file)

def list_all_videos(videos):
    print("*"*70)
    for idx,video in enumerate(videos,start=1):
        print(f"{idx}. {video['title']} : {video['time']}")
    print("*"*70)
    


def update_videos(videos):
    list_all_videos(videos)
    index = int(input("\nEnter index of the video you want to update : "))
    if(1 <= index <= len(videos)):
        title = input("Enter new title of the video : ")
        time = input("Enter new time of the video : ")
        videos[index-1]['title'] = title
        videos[index-1]['time'] = time
        print("\nVideo details updated successfully! <3")
        save_data(videos)
    else: 
        print("\noppss... Wrong input! :/")
        
    

def add_video(videos):
    title = input("\nEnter the title of the video : ")
    time = input("Enter time of the video : ")
    videos.append({'title': title , 'time' : time})
    save_data(videos)
    print("\nVideo added successfully! <3\n")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("\nEnter the index of the video you want to delete : "))
    if(1 <= index <= len(videos)):
        del videos[index-1]
        print("\nVideo deleted successfully! <3")
    else:
        print("oppss... Wrong input! :/")
    
     


def main(): 
    videos = load_data()
    while True:
        print("Welcome to Youtube Manager <3")
        print("enter 1 to list all your favourite videos ")
        print("enter 2 to update your favourite video details ")
        print("enter 3 Add a favourite video ")
        print("enter 4 to delete a favourite video ")
        print("Enter 5 to Exit ")
        
        choice = input("\nEnter your choice : ")
        
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                update_videos(videos)
            case '3':
                add_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                print("\nBieeee....<3")
                break
            case _:
                print("\noppss... Wrong input! :/")
    
    
if(__name__ == "__main__"):
    main()
    