import csv

# this is the main program, it allows users to choose from data input or analytics
def mainprogram():
    try:
        users_choice = input(
            "type 1 for data input, type 2 for analytics, type 3 to end the program"
        )
        # if user choose 1, it takes user to the function where they input game data
        if users_choice == ("1"):
            input_data()
        # if user choose 2, it takes user to the function where they see the analytics
        elif users_choice == ("2"):
            analytics()
        # if user inputs anything else, it ends the program

        else:
            print("thank u for using this program!")
    # if an error occurs with the input,it takes user back to the mainprogram
    except:
        print("pls type the correct input for the program to work")
        mainprogram()


# define the functions for later use
def input_data():  # this function collects input data from user for later calculations
    # set the value of gold_per_minute at whatever user inputs
    gold_per_minute = input("gold per minute pls").strip()
    # set the value of cs_per_minute at whatever user inputs
    cs_per_minute = input("cs per minute pls").strip()
    # set the value of gold_lead_before_minute_14 to whatever user inputs
    gold_lead_before_minute_14 = input("gold lead before minute 14 pls").strip()
    # set the value of towers_destroyed to whatever user inputs
    towers_destroyed = input("towers destroyed pls").strip()
    # set the value of win_loss to true or false depents on what the user inputs
    win_loss = input(
        "win or loss ,pls enter number 1 or 0, 1 means win, 0 means loss"
    ).strip()

    # checks if the data inputted by the user is empty or not
    if not gold_per_minute:
        print("input cannot be empty")
    elif not cs_per_minute:
        print("input cannot be empty")
    elif not gold_lead_before_minute_14:
        print("input cannot be empty")
    elif not towers_destroyed:
        print("input cannot be empty")
    elif not win_loss:
        print("input cannot be empty")
    else:
        # store input into the file after checking the all of the data needed
        # Convert inputs to correct types before storing
        try:
            # turns gold_per_minute into float
            gold_per_minute = float(gold_per_minute)
            # turns cs_per_minute into float
            cs_per_minute = float(cs_per_minute)
            # turns gold_lead_before_minute_14 into float
            gold_lead_before_minute_14 = float(gold_lead_before_minute_14)
            # turns towers_destroyed into integer
            towers_destroyed = int(towers_destroyed)
            # Handle win_loss (1 means True, 0 means False)
            if win_loss == "1":
                win_loss = True
            elif win_loss == "0":
                win_loss = False
            else:
                print(
                    "Error: 'win_loss' must be 1 (win) or 0 (loss)!,this set of data will not be store"
                )
                return

            # opens the file datastorage and set it into append MODE
            # place all of the data inputed by the user into the it
            with open("datastorage.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(
                    [
                        gold_per_minute,
                        cs_per_minute,
                        gold_lead_before_minute_14,
                        towers_destroyed,
                        int(win_loss),  # Convert to 1/0 for cleaner CSV storage
                    ]
                )
        except ValueError as e:
            print(f"Invalid input: {e}")
    mainprogram()


def analytics():  # this function reads data from the storage then calculate it into readable and usable information
    def read_csv(filename):
        data = []
        with open(filename, "r") as file:  # Opens the file
            reader = csv.reader(file)  # Reads the CSV
            for row in reader:  # Loops through each row
                data.append(row)
        return data

    data = read_csv("datastorage.csv")

    def calculate_stats(data):
        total_gold = 0
        total_cs = 0
        total_goldlead = 0
        total_towersdestroyed = 0
        total_wins = 0
        total_matches = len(data)  # Number of rows

        for row in data:
            gold = float(row[0])  # Column 0 = Gold
            cs = float(row[1])  # Column 1 = CS
            gold_lead14 = float(row[2])  # Column 2 = gold_lead_before_minute_14
            towers_destroyed = float(row[3])  # Column 3 = towers_destroyed
            win = int(row[4])  # Column 4 = win or lose, count 1 as a win, 0 as a lose

            total_gold += gold
            total_cs += cs
            total_goldlead += gold_lead14
            total_towersdestroyed += towers_destroyed
            total_wins += win  # 1 = win, 0 = loss

        avg_gold = total_gold / total_matches
        avg_cs = total_cs / total_matches
        avg_goldlead = total_goldlead / total_matches
        avg_towersdestroyed = total_towersdestroyed / total_matches
        win_rate = (
            total_wins / total_matches * 100
        )  # times a hundred for it to show as percentage Number

        return {
            "avg_gold": avg_gold,
            "avg_cs": avg_cs,
            "avg_goldlead": avg_goldlead,
            "avg_towersdestroyed": avg_towersdestroyed,
            "win_rate": win_rate,
            "total_matches": total_matches,
        }

    stats = calculate_stats(data)
    print(stats)

    mainprogram()


mainprogram()
