# What are the chance of encountering people with COVID if I go out today?
I do not know, but I would like to know

## Basic idea
Calculate the percentage of people may have COVID today in state population

### How can I find out how many people may have COVID today?
Please note this is an over simplified educated guess. Do not over interpret the result 
1. Using API https://covidtracking.com/ to get new case increase counts for the last 14 days for each state
2. Find the maximum increase count in the past 14 days
3. `Max value * 14 * 2` (This is by no means accurate. Too many factors are involved. I hope this is a conservative educated guess by using max value and `* 2` as fault tolerance mitigators ) 

### How can I find out population in each state?
https://www.census.gov/data/developers/data-sets/popest-popproj/popest.html

## Note
This project is under MIT license. I created it for personal reference. Feel free to do whatever you want with it. However, I am not responsible for any outcome regardless how you use or not use those data 

## Result

 Updated at: 2020-06-25T18:09:58.313251+00:00

| State                | Chance of encountering 1 person with COVID if you meet 1 person   | Chance of encountering 1 person with COVID if you meet 10 people   | Chance of encountering a person with COVID if you meet 100 people   |   Max count of new case increase in the past 14 days |   Estimated people count with COVID |
|:---------------------|:------------------------------------------------------------------|:-------------------------------------------------------------------|:--------------------------------------------------------------------|-----------------------------------------------------:|------------------------------------:|
| Alabama              | 0.57905%                                                          | 5.79052%                                                           | 57.90522%                                                           |                                                 1014 |                               28392 |
| Alaska               | 0.11100%                                                          | 1.10998%                                                           | 11.09980%                                                           |                                                   29 |                                 812 |
| Arizona              | 1.38217%                                                          | 13.82167%                                                          | 138.21667%                                                          |                                                 3593 |                              100604 |
| Arkansas             | 0.88515%                                                          | 8.85147%                                                           | 88.51469%                                                           |                                                  954 |                               26712 |
| California           | 0.50661%                                                          | 5.06608%                                                           | 50.66078%                                                           |                                                 7149 |                              200172 |
| Colorado             | 0.13906%                                                          | 1.39058%                                                           | 13.90583%                                                           |                                                  286 |                                8008 |
| Connecticut          | 0.23953%                                                          | 2.39532%                                                           | 23.95319%                                                           |                                                  305 |                                8540 |
| Delaware             | 0.32205%                                                          | 3.22049%                                                           | 32.20493%                                                           |                                                  112 |                                3136 |
| Florida              | 0.71846%                                                          | 7.18456%                                                           | 71.84556%                                                           |                                                 5511 |                              154308 |
| Georgia              | 0.47469%                                                          | 4.74691%                                                           | 47.46915%                                                           |                                                 1800 |                               50400 |
| Hawaii               | 0.05339%                                                          | 0.53395%                                                           | 5.33947%                                                            |                                                   27 |                                 756 |
| Idaho                | 0.38857%                                                          | 3.88570%                                                           | 38.85701%                                                           |                                                  248 |                                6944 |
| Illinois             | 0.18362%                                                          | 1.83620%                                                           | 18.36200%                                                           |                                                  831 |                               23268 |
| Indiana              | 0.21669%                                                          | 2.16689%                                                           | 21.66893%                                                           |                                                  521 |                               14588 |
| Iowa                 | 0.41444%                                                          | 4.14444%                                                           | 41.44441%                                                           |                                                  467 |                               13076 |
| Kansas               | 0.48536%                                                          | 4.85358%                                                           | 48.53579%                                                           |                                                  505 |                               14140 |
| Kentucky             | 0.31336%                                                          | 3.13362%                                                           | 31.33622%                                                           |                                                  500 |                               14000 |
| Louisiana            | 0.81673%                                                          | 8.16728%                                                           | 81.67280%                                                           |                                                 1356 |                               37968 |
| Maine                | 0.11248%                                                          | 1.12482%                                                           | 11.24823%                                                           |                                                   54 |                                1512 |
| Maryland             | 0.33902%                                                          | 3.39019%                                                           | 33.90189%                                                           |                                                  732 |                               20496 |
| Massachusetts        | 0.20759%                                                          | 2.07588%                                                           | 20.75879%                                                           |                                                  511 |                               14308 |
| Michigan             | 0.12561%                                                          | 1.25605%                                                           | 12.56051%                                                           |                                                  448 |                               12544 |
| Minnesota            | 0.22491%                                                          | 2.24908%                                                           | 22.49083%                                                           |                                                  453 |                               12684 |
| Mississippi          | 1.54858%                                                          | 15.48578%                                                          | 154.85784%                                                          |                                                 1646 |                               46088 |
| Missouri             | 0.33076%                                                          | 3.30757%                                                           | 33.07574%                                                           |                                                  725 |                               20300 |
| Montana              | 0.08383%                                                          | 0.83834%                                                           | 8.38341%                                                            |                                                   32 |                                 896 |
| Nebraska             | 0.41977%                                                          | 4.19767%                                                           | 41.97667%                                                           |                                                  290 |                                8120 |
| Nevada               | 0.41998%                                                          | 4.19979%                                                           | 41.99787%                                                           |                                                  462 |                               12936 |
| New Hampshire        | 0.14827%                                                          | 1.48267%                                                           | 14.82668%                                                           |                                                   72 |                                2016 |
| New Jersey           | 0.14816%                                                          | 1.48162%                                                           | 14.81617%                                                           |                                                  470 |                               13160 |
| New Mexico           | 0.40728%                                                          | 4.07282%                                                           | 40.72817%                                                           |                                                  305 |                                8540 |
| New York             | 0.13184%                                                          | 1.31842%                                                           | 13.18422%                                                           |                                                  916 |                               25648 |
| North Carolina       | 0.47200%                                                          | 4.72002%                                                           | 47.20023%                                                           |                                                 1768 |                               49504 |
| North Dakota         | 0.15432%                                                          | 1.54318%                                                           | 15.43182%                                                           |                                                   42 |                                1176 |
| Ohio                 | 0.17462%                                                          | 1.74624%                                                           | 17.46242%                                                           |                                                  729 |                               20412 |
| Oklahoma             | 0.34107%                                                          | 3.41069%                                                           | 34.10690%                                                           |                                                  482 |                               13496 |
| Oregon               | 0.30670%                                                          | 3.06705%                                                           | 30.67048%                                                           |                                                  462 |                               12936 |
| Pennsylvania         | 0.11504%                                                          | 1.15045%                                                           | 11.50446%                                                           |                                                  526 |                               14728 |
| Rhode Island         | 0.38589%                                                          | 3.85893%                                                           | 38.58930%                                                           |                                                  146 |                                4088 |
| South Carolina       | 0.69827%                                                          | 6.98271%                                                           | 69.82715%                                                           |                                                 1284 |                               35952 |
| South Dakota         | 0.28802%                                                          | 2.88021%                                                           | 28.80206%                                                           |                                                   91 |                                2548 |
| Tennessee            | 0.48709%                                                          | 4.87087%                                                           | 48.70867%                                                           |                                                 1188 |                               33264 |
| Texas                | 0.53603%                                                          | 5.36035%                                                           | 53.60348%                                                           |                                                 5551 |                              155428 |
| Utah                 | 0.56158%                                                          | 5.61579%                                                           | 56.15794%                                                           |                                                  643 |                               18004 |
| Vermont              | 0.08975%                                                          | 0.89745%                                                           | 8.97452%                                                            |                                                   20 |                                 560 |
| Virginia             | 0.21585%                                                          | 2.15851%                                                           | 21.58510%                                                           |                                                  658 |                               18424 |
| Washington           | 0.18973%                                                          | 1.89733%                                                           | 18.97335%                                                           |                                                  516 |                               14448 |
| West Virginia        | 0.08906%                                                          | 0.89055%                                                           | 8.90552%                                                            |                                                   57 |                                1596 |
| Wisconsin            | 0.20775%                                                          | 2.07748%                                                           | 20.77482%                                                           |                                                  432 |                               12096 |
| Wyoming              | 0.15965%                                                          | 1.59652%                                                           | 15.96519%                                                           |                                                   33 |                                 924 |
| Puerto Rico          | 0.23496%                                                          | 2.34963%                                                           | 23.49630%                                                           |                                                  268 |                                7504 |
| District of Columbia | 0.25788%                                                          | 2.57882%                                                           | 25.78821%                                                           |                                                   65 |                                1820 |