import json


FileName = 'youtube.txt'

def list_all_videos(videos):
    print('\n')
    print('*' * 50)
    print('\n')

    for index, video in enumerate(videos, start=1): # it will give data in the form of list and also gives indexing also. start=1 will start the indexing from 1
        print(f"{index}. {video['name']}, Duration: {video['time']}")
    
    print('\n')
    print('*' * 50)

def add_video(videos):
    name = input('Enter video name: ')
    time = input('Enter video time: ')
    videos.append({'name': name, 'time': time})
    save_data(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input('Enter Video number to update: '))
    if 1<= index <= len(videos):
        name = input('Enter new video name: ')
        time = input('Enter new video time: ')
        videos[index-1] = {'name': name, 'time': time}
        save_data(videos)
    else:
        print('Invalid video number selected')    

def delete_video(videos):
    list_all_videos(videos)
    index = int(input('Enter video number to be deleted: '))
    if 1<= index <= len(videos):
        del videos[index-1]
        save_data(videos)
    else:
        print('Invalid video number selected')

def load_data():
    try:
        with open(FileName, 'r') as file:
            test = json.load(file)
            return test
    except FileNotFoundError:
        return []

def save_data(videos):
    with open(FileName, 'w') as file:
        return json.dump(videos, file)

def main():
    videos = load_data()
    while True:
        print(' \n Youtube Manager | Choose your preference')
        print('1. List all  videos')
        print('2. Add a video')
        print('3. Update a video')
        print('4. Delete a video')
        print('5. Exit the app')
        choice = input('Enter your choice: ')

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print('Enter an valid input')


if __name__ == '__main__':
    main()