# Dataset
1. RegularSeasonCompactResults.csv: This file identifies the game-by-game results for 32 seasons of historical data, from 1985 to 2016. Each year, it includes all games played from daynum 0 through 132 (which by definition is "Selection Sunday," the day that tournament pairings are announced). Each row in the file represents a single game played.
2. RegularSeasonDetailedResults.csv: This file is a more detailed set of game results, covering seasons 2003-2016. This includes team-level total statistics for each game (total field goals attempted, offensive rebounds, etc.) The column names should be self-explanatory to basketball fans (as above, "w" or "l" refers to the winning or losing team)
3. Teams.csv: This file identifies the different college teams present in the dataset. Each team has a 4 digit id number.
4. Seasons.csv: This file identifies the different seasons included in the historical data, along with certain season-level properties.
5. TourneyCompactResults.csv: This file identifies the game-by-game NCAA tournament results for all seasons of historical data. The data is formatted exactly like the regular_season_compact_results.csv data. Note that these games also include the play-in games (which always occurred on day 134/135) for those years that had play-in games.
6. TourneyDetailedResults.csv: This file contains the more detailed results for tournament games from 2003 onward.
7. TourneySeeds.csv: This file identifies the seeds for all teams in each NCAA tournament, for all seasons of historical data. Thus, there are between 64-68 rows for each year, depending on the bracket structure.
8. TourneySlots.csv: This file identifies the mechanism by which teams are paired against each other, depending upon their seeds. Because of the existence of play-in games for particular seed numbers, the pairings have small differences from year to year. If there were N teams in the tournament during a particular year, there were N-1 teams eliminated (leaving one champion) and therefore N-1 games played, as well as N-1 slots in the tournament bracket, and thus there will be N-1 records in this file for that season. 
10. PCBR csv series (02PCBR.csv to 16PCBR.csv): These 15 files are the evaluations in 9 dimensions for all teams from 2002 to 2016, based on the analysis of Pomeroy College Basketball Ratings (http://kenpom.com/index.php). Notations: 
    conf: conference;
    W-L: Win-Lose;
    AdjEM: Adjusted Efficiency Margin;
    AdjO: Adjusted offensive efficiency (Points scored per 100 possessions, adjusted for opponent);
    AdjD: Adjusted defensive efficiency (Points allowed per 100 possessions, adjusted for opponent);
    AdjT: AdjO Adjusted Tempo (possessions per 40 minutes, adjusted for opponent);
    Luck: Luck rating;
    SOS: Strength of Schedule;
    SOS AdjEM: Strength of Schedule rating;
    SOS OppO: average AdjO of opposing offenses;
    SOS OppD: average AdjE of opposing defenses;
    NCSOS AdjEM: Non-Conference Strength of Schedule rating.
