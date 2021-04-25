# English Premier League Top 4 Prediction
<p align="center">
    <img src="imgs/epl_logo.png" width="50%" height="50%">
</p>

## Motivation 
Every year in English Premier League (EPL), all clubs are striving to get into the top 4 in the league so that they can participate in the Champions League, which is the biggest competition in Europe besides their own league. We have sort of ideas about what a team should do to win a match such as good passing, high pressure, more shots on target, etc… As a Data science enthusiast and a huge soccer fan, I was curious to see if  I can prove or find out what features are actually important to win a match. This could make a confident statement about what a team has to focus on to be in the top 4. Moreover, it can help to predict what teams are highly likely to be in the top 4 using machine learning models.

## Dataset
**Source:** Data is gathered by web scraping on EPL official website.  
**Period:** From 1993 to 2020   
**Features:** Total 23 columns and 566 rows  
**Characteristics:** Dataset is composed into two tables. One with final results of its season (it’s called “table.csv”) and one with clubs’ statistics (“club_statistics.csv”). “Table.csv” has all data from 1993 to 2020; however, “club_statistics.csv” missing many factors from 1993 to 2006 due to the data gathering method that EPL had applied in matches. More details are in this link: https://www.premierleague.com/stats/clarification

## Limitations
Dataset does not include other features that might be important for performance of a team such as Team mentality, number of players who are injured, whether a team has world class players or not, tatics, etc… Therefore, there might be other important features that have a positive relationship with getting into the top 4. 

