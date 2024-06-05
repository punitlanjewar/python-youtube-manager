**Project Description: YouTube Video Manager**

This project is a simple command-line application written in Python for managing a list of YouTube videos. 
It allows users to perform basic CRUD operations (Create, Read, Update, Delete) on a collection of videos stored in a JSON file.

**Features:**

**1. List All Videos:**

Displays all videos in the collection along with their names and durations.

**2. Add a Video:**

Allows the user to add a new video by entering its name and duration.

**3. Update a Video:**

Lists all videos with their current details.
Prompts the user to select a video by its number and enter new details for that video.

**4. Delete a Video:**

Lists all videos with their current details.
Prompts the user to select a video by its number for deletion.

**Data Storage:**

The videos are stored in a JSON file named youtube.txt. Each video is represented as a dictionary with two keys: name and time.

**Functions:**

list_all_videos(videos): Lists all the videos in the console.
add_video(videos): Prompts the user to add a new video and saves it.
update_video(videos): Allows the user to update the details of an existing video.
delete_video(videos): Allows the user to delete a video from the collection.
load_data(): Loads the video data from the JSON file.
save_data(videos): Saves the video data to the JSON file.
main(): The main function that runs the application and all functions, providing a menu for user interaction.

**Code Walkthrough:**

**1. File Operations:**

The load_data() function attempts to read the youtube.txt file and load its contents into a list. If the file does not exist, it returns an empty list.
The save_data(videos) function writes the list of videos back to the youtube.txt file in JSON format.

**2. User Interface:**

The main() function presents a menu to the user with options to list, add, update, delete videos, or exit the application.
The match statement (available in Python 3.10 and above) is used to handle user choices in a clean and readable way.

**3. Video Management:**

The list_all_videos(videos) function prints all videos with their index numbers, names, and durations.
The add_video(videos) function collects video details from the user and appends a new dictionary to the list of videos.
The update_video(videos) function allows the user to select a video by its index, then updates its details based on user input.
The delete_video(videos) function allows the user to select a video by its index and removes it from the list.
The enumerate() function is a built-in function in Python that allows to iterate over a sequence (such as a list, tuple, or string) while keeping track of the index of the current item. 
It adds a counter to an iterable and returns it as an enumerate object, which can then be converted to a list of tuples, where each tuple contains a pair of the (index, element).



**4. Error Handling:**

The code includes basic error handling for file operations (e.g., handling FileNotFoundError in load_data()).
It also includes validation for user input when selecting videos to update or delete, ensuring the input is within the valid range.

**How to Run:**

Ensure you have Python installed (version 3.10 or above).
Save the script to a file, for example, YoutubeManager.py.
Run the script using the command: python YoutubeManager.py.
Follow the on-screen prompts to manage your list of YouTube videos.
