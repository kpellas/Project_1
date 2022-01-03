## Analysis of Fatal Crash Data - Austrlaia 1989 - 2020

### Overview

In this project, we analysed Fatal Crash Data collected by the Bureau of Infrastructure, Transport, Regional Development from 1989 to 2020. We merged population data segmented by state and sex dowloaded from the Australian Bureau of Statistics.

The objective was to determine if any relationship(s) can be made between the fatality rate and other variables for which data had been collected. This includes data on population demographic, geographic attributes, time and road useage. 

The crash dataset contains the following information:
* Time of the crash - month, day, year, day of the week 
* Demographic information - age, gende of individual
* Geographic information - state, speed limit. Categories were added to the dataset in recent years to include: Remote Areas, LGA, Road type
* Road User - driver, passenger, pedestrian, motorcycle rider, motorcycle passenger, pedal cyclists.

### Preparing Data 

Cleaning the crash dataset involved renaming columnns, changing datatypes, removing null values. The population dataset required more manipulation in order for ito merge with the crash dataset to include: renaming columns, creating dataframes for each state and re-combining inorder to merge.

### Time Analysis 

#### Year vs Population vs State

Initial analysis shows that inspite of a steady population increase, crash fatalities have decreased. Statistical testing indicates a negative correlation of 
-92. Breakdown by state shows the stength of correlation varies. 

#### Month Comparision

There seems to be an understanding that more fatalities occur over holiday periods - Christmas and Easter. Testing shows no statistical difference from month to month. This could be explained by a change in driving patterns causing a decrease in fatalities under normal circumstances. Further analysis could be done to determine if time of day patterns change during holiday periods.

#### Day of Week 

Testing does show a significant statistical difference when comparing days of the week. More fatalities occur on Saturday, Friday and Sunday respectively. 

#### Time of Day

Testing also inidicates a significant statistical difference regarding time of day with more deaths occuring during the hours associated with the evening commute. Further analysis considering Day of Week and Time of Day shows that the majority of deaths occuring on Saturday and Sunday occur at night, from midnight to 6:00 a.m. 


