import sqlite3

conn = sqlite3.connect('youtube.db')
cursor = conn.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS videos(
                   id NUMBER PRIMARY KEY,
                   title TEXT NOT NULL,
                   time TEXT NOT NULL
               )
               ''')
print("Connection established!!")
conn.commit()


def list_all_videos():
    cursor.execute("SELECT * FROM videos")
    videos = cursor.fetchall()
    conn.commit()
    if videos:
        print("\nList of favourite videos:")
        for video in videos:
            print(f"ID: {video[0]}, Title: {video[1]}, Time: {video[2]}")
    else:
        print("\nNo videos found.")

def update_videos(videos):
    vid_id = int(input("Enter video ID : "))
    new_title = input("Enter new title : ")
    new_time = input("Enter new time : ")
    cursor.execute("UPDATE videos SET title = ? , time = ? WHERE id = ?",(new_title,new_time,vid_id))
    conn.commit()
    print("Updated successfully")
    

def add_video(videos):
    vid_id = int(input("Enter video ID : "))
    title = input("Enter title : ")
    time = input("Enter time : ")
    cursor.execute("INSERT into videos VALUES (?,?,?)",(vid_id,title,time))
    conn.commit()

def delete_video(videos):
    vid_id = int(input("Enter video ID : "))
    cursor.execute("DELETE FROM videos WHERE id = ?",(vid_id,))
    
     


def main(): 
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
                list_all_videos()
            case '2':
                update_videos()
            case '3':
                add_video()
            case '4':
                delete_video()
            case '5':
                print("\nBieeee....<3")
                break
            case _:
                print("\noppss... Wrong input! :/")
    
    
if(__name__ == "__main__"):
    main()
    
    conn.close()
    