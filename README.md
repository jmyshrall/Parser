# Air Quality Analysis

Welcome to the Air Quality Analysis repository! 🌬️

This repository contains Python classes for analyzing air quality data. Two main classes are provided: `PollutantPercentageCalculator` and `AQITrendsAnalyzer`. These classes are designed to process environmental data related to air quality measurements and provide insights into pollutant percentages and AQI trends over the years for different states.

## Dataset

The dataset used for analysis contains environmental data related to air quality index (AQI) measurements for different states over the years. The dataset includes the following columns:

- `Geo_Loc`: Geographic location coordinates.
- `Year`: The year of the data.
- `State`: The state for which the data is recorded.
- `Pop_Est`: Population estimate.
- `TTL_Cnty`: Total counties.
- `Cnty_Rpt`: Counties reporting.
- `Dys_w_AQI`: Days with AQI recorded.
- `Dys_NM`: Days with "NM" (not monitored).
- `Dys_Blw_Thr`: Days below threshold.
- `Dys_Abv_Thr`: Days above threshold.
- `Good Days`: Number of good air quality days.
- `Moderate Days`: Number of moderate air quality days.
- `Unhealthy for Sensitive Groups Days`: Number of days with unhealthy air quality for sensitive groups.
- `Unhealthy Days`: Number of unhealthy air quality days.
- `Very Unhealthy Days`: Number of very unhealthy air quality days.
- `Hazardous Days`: Number of hazardous air quality days.
- `Max AQI`: Maximum Air Quality Index value.
- `90th Percentile AQI`: 90th percentile AQI value.
- `Median AQI`: Median AQI value.
- `Days CO`: Number of days with carbon monoxide (CO) measurements.
- `Days NO2`: Number of days with nitrogen dioxide (NO2) measurements.
- `Days Ozone`: Number of days with ozone measurements.
- `Days PM2.5`: Number of days with fine particulate matter (PM2.5) measurements.
- `Days PM10`: Number of days with coarse particulate matter (PM10) measurements.

## Usage

To utilize the provided Python classes for air quality analysis:

1. Clone this repository to your local machine.
2. Make sure you have Python installed.
3. Replace `'dataset.csv'` in the main script with the path to your dataset file.
4. Run the main script:
    ```bash
    python aqi.py
    ```

## Acknowledgments

Special thanks to the contributors of the air quality dataset used in this analysis.

[Link to the dataset](https://www.kaggle.com/datasets/fedesoriano/air-quality-data-set)

Happy analyzing! 🌱


User
should you inform those who run it what happens when it executes
ChatGPT
Certainly! Including information about what happens when the script is executed would provide clarity to users. Here's the updated README.md with that information added:

markdown
Copy code
# Air Quality Analysis

Welcome to the Air Quality Analysis repository! 🌬️

This repository contains Python classes for analyzing air quality data. Two main classes are provided: `PollutantPercentageCalculator` and `AQITrendsAnalyzer`. These classes are designed to process environmental data related to air quality measurements and provide insights into pollutant percentages and AQI trends over the years for different states.

## Dataset

The dataset used for analysis contains environmental data related to air quality index (AQI) measurements for different states over the years. The dataset includes the following columns:

- `Geo_Loc`: Geographic location coordinates.
- `Year`: The year of the data.
- `State`: The state for which the data is recorded.
- `Pop_Est`: Population estimate.
- `TTL_Cnty`: Total counties.
- `Cnty_Rpt`: Counties reporting.
- `Dys_w_AQI`: Days with AQI recorded.
- `Dys_NM`: Days with "NM" (not monitored).
- `Dys_Blw_Thr`: Days below threshold.
- `Dys_Abv_Thr`: Days above threshold.
- `Good Days`: Number of good air quality days.
- `Moderate Days`: Number of moderate air quality days.
- `Unhealthy for Sensitive Groups Days`: Number of days with unhealthy air quality for sensitive groups.
- `Unhealthy Days`: Number of unhealthy air quality days.
- `Very Unhealthy Days`: Number of very unhealthy air quality days.
- `Hazardous Days`: Number of hazardous air quality days.
- `Max AQI`: Maximum Air Quality Index value.
- `90th Percentile AQI`: 90th percentile AQI value.
- `Median AQI`: Median AQI value.
- `Days CO`: Number of days with carbon monoxide (CO) measurements.
- `Days NO2`: Number of days with nitrogen dioxide (NO2) measurements.
- `Days Ozone`: Number of days with ozone measurements.
- `Days PM2.5`: Number of days with fine particulate matter (PM2.5) measurements.
- `Days PM10`: Number of days with coarse particulate matter (PM10) measurements.

## Usage

To utilize the provided Python classes for air quality analysis:

1. Clone this repository to your local machine.
2. Make sure you have Python installed.
3. Replace `'dataset.csv'` in the main script with the path to your dataset file.
4. Run the main script:
    ```bash
    python aqi.py
    ```

When executed, the script will perform the following actions:
- Read the dataset file.
- Calculate pollutant percentages for each year.
- Plot bar graphs showing the percentage of each pollutant over the years.
- Analyze AQI trends for each state.
- Print the average AQI for each state.

## Acknowledgments

Special thanks to the contributors of the air quality dataset used in this analysis.

[Link to the dataset](https://www.kaggle.com/datasets/fedesoriano/air-quality-data-set)

Happy analyzing! 🌱