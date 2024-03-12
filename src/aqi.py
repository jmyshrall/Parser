"""
Author: Justin Myhshrall
Date: 3/4/2024
"""
import matplotlib.pyplot as plt

class PollutantPercentageCalculator:
    
    """
    A class to calculate and print pollutant percentages for each year based on the given dataset.
    Attributes:
    - file_path (str): The file path to the dataset.
    - percentages (dict): A dictionary to store pollutant percentages for each year.
    """

    def __init__(self, file_path):
        """
        Initializes a PollutantPercentageCalculator instance.
        PARAM:
        - file_path (str): The file path to the dataset.
        """
        # initialize the file path
        self.file_path = file_path
        # initializes a dictionary to store pollutant percentages
        self.percentage = {}

    def read_data(self):
        """
        Reads the dataset file, extracts pollutant data, and populates the percentage dictionary.
        """
        # read the data from dataset.csv
        with open(self.file_path, 'r') as file:
            data_lines = file.readlines()
        # extract the header to identify pollutants by splitting top row by commas
        header = data_lines[0].strip().split(',')
        pollutants = header[19:]
        # pulls data from 20th column and after (pollutants)

        for line in data_lines[1:]:
            # iterates through each line skipping the header
            fields = line.strip().split(',')
            year = int(fields[1])
            # extracts year and converts to type int
            pollutant_values = [float(value) for value in fields[19:]]
            # extract pollutant values and sets as type float

            if year not in self.percentage:
                self.percentage[year] = {}

            for pollutant, value in zip(pollutants, pollutant_values):
                # iterates over pollutants and their values

                if pollutant not in self.percentage[year]:
                    self.percentage[year][pollutant] = 0
                    # add the current pollutant's value to the existing value in the year's data dictionary
                self.percentage[year][pollutant] += value

    def calculate_pollutant_percentages(self):
        """
        Calculates pollutant percentages for each year based on the accumulated
        values in the percentage dictionary.
        """
        # Calculate the percentage contribution of each pollutant for each year
        for year, year_data in self.percentage.items():
            # calculate the total AQI for the current year
            total_aqi = sum(year_data.values())

            if total_aqi != 0:
                # avoids division by zero errors
                for pollutant, value in year_data.items():
                    # `value` is amount of specific pollutant, `total_aqi` is all pollutant values that year
                    percentage = (value / total_aqi) * 100
                    # converts amount of pollutant to percentage
                    year_data[pollutant] = f"{percentage:.2f}%"
                    # update the pollutant's value in the year's data with the calculated percentage
            else:
                for pollutant in year_data:
                    # if total AQI is zero
                    year_data[pollutant] = "0.00%"

    def print_pollutant_percentages(self):
        """
        Prints the pollutant percentages for each year in a formatted table.
        """
        # print the header line for the pollutant percentages, including the 'Year' and pollutant names
        print("Pollutant Percentages for Each Year:")
        header = "\t".join(["Year"] + list(self.percentage[next(iter(self.percentage))].keys()))
        print(header)
        # makes a header with year and all pollutant variables

        # iterate over each year and its corresponding pollutant data in the percentage dictionary
        for year, year_data in self.percentage.items():
            # join the values for the current year into a string, separated by tabs
            values = "\t".join([str(year)] + list(year_data.values()))
            # print the string representing the pollutant percentages for the current year
            print(values)
        
    def get_pollutant_percentage_data(self):
        """
        Returns the pollutant percentages for each year.
        """
        return self.percentage
    
    def plot_pollutant_percentage_bar_graphs(self):
        """
        Generates bar graphs for each pollutant showing its percentage over the years.
        """
        years = list(self.percentage.keys())
        pollutants = list(self.percentage[years[0]].keys())
        
        for pollutant in pollutants:
            values = [float(self.percentage[year][pollutant].strip('%')) for year in years]
            plt.figure(figsize=(10, 6))
            plt.bar(years, values, color='skyblue')
            plt.xlabel('Year')
            plt.ylabel('Pollutant Percentage')
            plt.title(f'{pollutant} Percentage Over Years')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()

class AQITrendsAnalyzer:
    """
    A class for analyzing trends in air quality index (AQI) data for
    different states over the years.
    """

    def __init__(self, file_path):
        """
        Initializes the AQITrendsAnalyzer instance.
        PARAM: file_path (str): The file path to the dataset containing AQI data.
        """
        self.sorted_states = None
        # stores `sorted_states`
        self.file_path = file_path
        self.years = []
        # stores the `years` in a list
        self.states = []
        self.aqi_values = []
        self.state_data = {}
        # stores output as dictionary keys = `states` values = {year:AQI_value}

    def read_data(self):
        """
        Reads AQI data from the dataset file and extracts relevant information.
        Assumes the dataset is comma-separated.
        RETURN: None
        """
        with open(self.file_path, 'r') as file:
            # opens the dataset.csv file
            data_lines = file.readlines()
            # stores each line as a list of strings

        for line in data_lines[1:]:  # skip the header line
            fields = line.strip().split(',')
            # splits the lines at the commas and removes trailing whitespace
            self.years.append(int(fields[1]))
            self.states.append(fields[2])
            # index value is determined by column in dataset.csv
            self.aqi_values.append(int(fields[16]))
            # extracts data from AQI value and converts to type int

    def separate_data_by_states(self):
        """
        Separates the AQI data into dictionaries based on states.
        RETURN: None
        """
        for year, state, aqi in zip(self.years, self.states, self.aqi_values):
            # iterate over each year, state, and AQI value simultaneously using the zip function

            if state not in self.state_data:
                self.state_data[state] = {'years': [], 'aqi_values': []}
                # adds new state to dictionary if not already there
            self.state_data[state]['years'].append(year)
            # append the current year to the list of years for the current state
            self.state_data[state]['aqi_values'].append(aqi)
            # append the current AQI value to the list of AQI values for the current state

    def sort_states_alphabetically(self):
        """
        Sorts the states alphabetically.
        Returns: None
        """
        self.sorted_states = sorted(self.state_data.keys())

    def print_trends(self):
        """
        Prints AQI trends for each state.
        Returns: None
        """
        for state in self.sorted_states:
            # iterate over each state in the sorted list of states
            data = self.state_data[state]
            # access AQI data from `state_data`
            print(f"State: {state}")
            # makes the state a header
            print("Year\tAQI")
            # makes year and AQI column headers

            for year, aqi in zip(data['years'], data['aqi_values']):
                # iterate over each year and AQI value for the current state using zip
                print(f"{year}\t{aqi}")
    
    def print_average_aqi(self):
        """
        Prints the average AQI at the end of the dataset for each state.
        Returns: None
        """
        print("\nAverage AQI For Each State:")

        for state in self.sorted_states:
            data = self.state_data[state]
            # access current state AQI data from `state_data`
            avg_aqi = sum(data['aqi_values']) / len(data['aqi_values'])
            # calculates avg AQI for current state
            print(f"{state}: {avg_aqi:.2f}")
            # print the state name and its corresponding average AQI, formatted to two decimal places

    def get_state_data(self):
        """
        Returns the AQI data for each state.
        """
        return self.state_data

def plot_aqi_trends(data):
    """
    Plots the AQI trends for each state.
    """
    for state, state_data in data.items():
        years = state_data['years']
        aqi_values = state_data['aqi_values']
        plt.plot(years, aqi_values, label=state)

    plt.xlabel('Year')
    plt.ylabel('AQI')
    plt.title('AQI Trends by State')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    
    calculator = PollutantPercentageCalculator('dataset.csv')
    calculator.read_data()
    calculator.calculate_pollutant_percentages()
    calculator.plot_pollutant_percentage_bar_graphs()
    
    analyzer = AQITrendsAnalyzer('dataset.csv')
    analyzer.read_data()
    analyzer.separate_data_by_states()
    analyzer.sort_states_alphabetically()
    aqi_data = analyzer.get_state_data()
    plot_aqi_trends(aqi_data)
    analyzer.print_average_aqi()
