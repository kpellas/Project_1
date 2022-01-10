## Analysis of Fatal Crash Data - Austrlaia 1989 - 2020
Overview
In this project, we analysed Fatal Crash Data collected by the Bureau of Infrastructure, Transport, Regional Development from 1989 to 2020. We merged population data segmented by state and sex dowloaded from the Australian Bureau of Statistics.

The objective was to determine if any relationship(s) can be made between the fatality rate and other variables for which data had been collected. This includes data on population demographic, geographic attributes, time and road useage.

# The crash dataset contains the following information:

Time of the crash - month, day, year, day of the week Demographic information - age, gende of individual Geographic information - state, speed limit. Categories were added to the dataset in recent years to include: Remote Areas, LGA, Road type Road User - driver, passenger, pedestrian, motorcycle rider, motorcycle passenger, pedal cyclists.

# Preparing Data
Cleaning the crash dataset involved renaming columnns, changing datatypes, removing null values. The population dataset required more manipulation in order for ito merge with the crash dataset to include: renaming columns, creating dataframes for each state and re-combining inorder to merge.

# State vs fatality crashes percentage 
Initial analysis shows that inspite of a steady population increase, crash fatalities have decreased. Statistical testing indicates that some of the states or terotory (NT) has significant drop in fatality ratio while other maintain almost constant dropping towards zero deaths .

# Speed vs fatality
There seems to be an understanding that more fatalities occur while speed increase. Testing shows no statistical difference on evarage when the speed accede 50kmh. This could be explained by a change in driving patterns causing a decrease in fatalities under normal circumstances. Further analysis could be done to determine if the road sefaty on free way is leading to that results

# distance from the main cities 
Testing does show a significant statistical difference when comparing distance from main cities. More fatalities occur within the CBDs and city cinters than rural area
