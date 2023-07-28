import time

def start_timer(duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        print(f"Time remaining: {remaining_time} seconds")
        time.sleep(1)
    print("Time's up!")

def main():
    print("Welcome to the World Schools Debate Timer!")
    print("1. Normal Speaker (6 minutes)")
    print("2. Reply Speaker (3 minutes)")

    choice = input("Enter the number of the speaker type (1 or 2): ")
    if choice not in ['1', '2']:
        print("Invalid choice. Please select 1 or 2.")
        return

    if choice == '1':
        duration = 6 * 60
    else:
        duration = 3 * 60

    start_timer(duration)

if __name__ == "__main__":
    main()
