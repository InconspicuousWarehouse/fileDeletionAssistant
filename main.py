import os
import time
import send2trash
import threading
import keyboard

elements_to_delete = []
event_flag = threading.Event()
interrupted = False

def set_deletion_time():
    global event_flag, elements_to_delete

    while True:
        print("Choose an option (1 - date and time of deletion, 2 - number of days, hours, and minutes until deletion, s - stop deletion, q - exit):")
        choice = input()

        if choice == 'q':
            return 0

        if choice == 's':
            on_interrupt()
            continue

        if choice not in ['1', '2']:
            print("Incorrect option. Try again.")
            continue

        file_path = input("Enter the path to the file or folder: ")

        if not os.path.exists(file_path):
            print("The specified file or folder does not exist.")
            continue

        if choice == '1':
            try:
                deletion_time_input = input("Enter the deletion date and time (YYYY-MM-DD HH:MM): ")
                deletion_time = time.strptime(deletion_time_input, "%Y-%m-%d %H:%M")
                deletion_time_seconds = time.mktime(deletion_time)
                time_difference = deletion_time_seconds - time.time()
            except ValueError:
                print("Invalid date or time format. Please try again.")
                continue

        elif choice == '2':
            try:
                days = int(input("Enter the number of days until deletion: "))
                hours = int(input("Enter the number of hours until deletion: "))
                minutes = int(input("Enter the number of minutes until deletion: "))
                seconds = int(input("Enter the number of seconds until deletion: "))
            except ValueError:
                print("Please enter an integer. Try again.")
                continue

            deletion_time = time.time() + days * 86400 + hours * 3600 + minutes * 60 + seconds
            time_difference = deletion_time - time.time()

        elements_to_delete.append((file_path, deletion_time, time.time()))

        if choice == '1':
            formatted_time = time.strftime('%Y-%m-%d %H:%M and 00s', time.localtime(deletion_time_seconds))
        else:
            formatted_time = time.strftime('%Y-%m-%d %H:%M and %Ss', time.localtime(deletion_time))

        print(f"The element will be deleted at {formatted_time}")

        event_flag.clear()

        timer_thread = threading.Thread(target=wait_and_delete, args=(time_difference,))
        timer_thread.start()

def on_interrupt():
    global interrupted
    print("All operations waiting to delete elements from the elements_to_delete list have been interrupted.")
    interrupted = True
    event_flag.set()

def wait_and_delete(time_difference):
    global event_flag, elements_to_delete

    while time_difference > 0 and not event_flag.is_set():
        time.sleep(min(1, time_difference))
        time_difference -= 1

    if not event_flag.is_set() and not interrupted:
        current_time = time.mktime(time.localtime())
        elements_to_remove = [element for element in elements_to_delete if current_time - element[2] >= time_difference]

        for element in elements_to_remove:
            elements_to_delete.remove(element)

        for i, tuple_file_path in enumerate(elements_to_remove):
            element = tuple_file_path[0]
            try:
                if os.path.isfile(element):
                    send2trash.send2trash(element)
                    print(f"The file '{os.path.basename(element)}' has been moved to the trash.")
                elif os.path.isdir(element):
                    send2trash.send2trash(element)
                    print(f"The folder '{os.path.basename(element)}' has been moved to the trash.")
                else:
                    print(f"Unable to delete. The object '{element}' is neither a file nor a folder.")
            except Exception as e:
                print(f"An error occurred while deleting '{element}': {e}")


if __name__ == "__main__":
    keyboard.add_hotkey('ctrl+p', on_interrupt)

    set_deletion_time()
