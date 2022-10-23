# Global SoMN

## What is Global SoMN?
Global SoMN stands for Global Speed of Mobile Network.</br>
To be more specific, it is about the network speed of mobile devices around the globe.

## What are the problems?
* What datasets is the eligible one to use?
  - 'Speedtest Data by Ookla' on Kaggle: [View the dataset](https://www.kaggle.com/datasets/dimitrisangelide/speedtest-data-by-ookla?select=mobile_year_2021_quarter_04.csv)
    - Ookla is the global leader in network intelligence and connectivity insights
    - The company owns the world-renowned Speedtest platform
* How to effectively visualize the analyzed data? 
  - Mapping the SoMN data to a geographical scale
  - Building a dashboard showing these transformed geographical data
* ***What can we learn from this?***
  - What insights can we get from this analysis?

## Preparing the data
* Download the latest (2020 and 2021) datasets of mobile network speedtest from the [site](https://www.kaggle.com/datasets/dimitrisangelide/speedtest-data-by-ookla?select=mobile_year_2021_quarter_04.csv)

## Processing the data
* Remove unwanted data types such as Rank Upload and Rank Download
* Check the blank undocumented data instances
* Check any duplicated data instances

## Analysis
* Examine and compare certain metrics in different countries
  - The average speed of uploading and downloading
  - The number of devices and tests ran on the devices
  - The average latency (ms) tested on mobile devices

## Visualization
* Use Tableau to map the processed data to world map to better show the difference and similarity of data based on all sorts of standards
  - The difference and similarity can be how different or similar the mobile network conditions are among the enlisted countries
  - The standards are basically the ones mentioned in the ***Analysis*** section
* Import the generated map data into a Streamlit powered, interactive web-app
  - Contains only necessary features (such as description, map data, and toggles for different metrics) dilvering better view quality
  - The toggles enable viewers to control the metrics to examine the data in different angles

## Insights
