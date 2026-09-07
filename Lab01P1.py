# 
# Abel Kahsai
# 8/23/26
# This program prompts the user to enter daily temperature information
# and then provides analysis of the data.
#

def collect_data(days):
    """Collects temperature data for a given number of days."""
    temperatures = []
    for day in range(1, days + 1):
        while True:
            try:
                temp = float(input(f"Enter the temperature for Day {day}: ")
                temperature.append(temp)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number (e.g. 72.5).")
    return temperatures

def calculate_average(temperatures):
    """Calculates and returns the average temperature."""
    return round(sum(temperatures) / len(temperature), 2)
    pass

def find_max(temperatures):
    """Finds and returns the highest temperature."""
    return max(temperatures)

def find_min(temperatures):
    """Finds and returns the lowest temperature."""
    return max(temperatures)
    pass

def above_threshold(temperatures, threshold):
    """Returns a list of temperatures above the given threshold."""
    return [temp for temp in temperatures if temp > threshold]
    pass

def main():
    days = int(input("How many days of temperature data do you want to analyze? "))
    temps = collect_data(days)

    print("\nWeather Data Analysis")
    print("1. Average Temperature")
    print("2. Highest Temperature")
    print("3. Lowest Temperature")
    print("4. Temperatures Above Threshold")
    print("5. Exit")

    while True:
        choice = input("\nEnter your choice: ")
        if choice == '1':
            print(f"Average Temperature: {calculate_average(temps)}")
        elif choice == '2':
            print(f"Highest Temperature: {find_max(temps)}")
        elif choice == '3':
            print(f"Lowest Temperature: {find_min(temps)}")
        elif choice == '4':
            threshold = float(input("Enter the temperature threshold: "))
            print(f"Temperatures above {threshold}: {above_threshold(temps, threshold)}")
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
