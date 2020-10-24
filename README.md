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

 Updated at: 2020-10-24T12:43:43.798352+00:00

| State                | Chance of encountering 1 person with COVID if you meet 1 person   | Chance of encountering 1 person with COVID if you meet 10 people   | Chance of encountering a person with COVID if you meet 100 people   |   Max count of new case increase in the past 14 days |   Estimated people count with COVID |
|:---------------------|:------------------------------------------------------------------|:-------------------------------------------------------------------|:--------------------------------------------------------------------|-----------------------------------------------------:|------------------------------------:|
| Alabama              | 2.19971%                                                          | 21.99713%                                                          | 219.97130%                                                          |                                                 3852 |                              107856 |
| Alaska               | 1.08701%                                                          | 10.87014%                                                          | 108.70145%                                                          |                                                  284 |                                7952 |
| Arizona              | 0.42815%                                                          | 4.28152%                                                           | 42.81524%                                                           |                                                 1113 |                               31164 |
| Arkansas             | 1.92524%                                                          | 19.25241%                                                          | 192.52410%                                                          |                                                 2075 |                               58100 |
| California           | 0.43518%                                                          | 4.35177%                                                           | 43.51767%                                                           |                                                 6141 |                              171948 |
| Colorado             | 0.66758%                                                          | 6.67577%                                                           | 66.75771%                                                           |                                                 1373 |                               38444 |
| Connecticut          | 1.05158%                                                          | 10.51584%                                                          | 105.15843%                                                          |                                                 1339 |                               37492 |
| Delaware             | 0.62685%                                                          | 6.26846%                                                           | 62.68459%                                                           |                                                  218 |                                6104 |
| Florida              | 1.00409%                                                          | 10.04091%                                                          | 100.40909%                                                          |                                                 7702 |                              215656 |
| Georgia              | 0.58651%                                                          | 5.86508%                                                           | 58.65077%                                                           |                                                 2224 |                               62272 |
| Hawaii               | 0.32630%                                                          | 3.26301%                                                           | 32.63007%                                                           |                                                  165 |                                4620 |
| Idaho                | 1.71410%                                                          | 17.14095%                                                          | 171.40955%                                                          |                                                 1094 |                               30632 |
| Illinois             | 1.12757%                                                          | 11.27573%                                                          | 112.75727%                                                          |                                                 5103 |                              142884 |
| Indiana              | 1.18534%                                                          | 11.85345%                                                          | 118.53447%                                                          |                                                 2850 |                               79800 |
| Iowa                 | 1.27351%                                                          | 12.73506%                                                          | 127.35058%                                                          |                                                 1435 |                               40180 |
| Kansas               | 2.03081%                                                          | 20.30814%                                                          | 203.08144%                                                          |                                                 2113 |                               59164 |
| Kentucky             | 0.91000%                                                          | 9.10004%                                                           | 91.00039%                                                           |                                                 1452 |                               40656 |
| Louisiana            | 0.82094%                                                          | 8.20944%                                                           | 82.09441%                                                           |                                                 1363 |                               38164 |
| Maine                | 0.09998%                                                          | 0.99984%                                                           | 9.99842%                                                            |                                                   48 |                                1344 |
| Maryland             | 0.36959%                                                          | 3.69586%                                                           | 36.95862%                                                           |                                                  798 |                               22344 |
| Massachusetts        | 0.43468%                                                          | 4.34675%                                                           | 43.46752%                                                           |                                                 1070 |                               29960 |
| Michigan             | 1.40296%                                                          | 14.02964%                                                          | 140.29639%                                                          |                                                 5004 |                              140112 |
| Minnesota            | 1.13695%                                                          | 11.36954%                                                          | 113.69536%                                                          |                                                 2290 |                               64120 |
| Mississippi          | 1.24375%                                                          | 12.43755%                                                          | 124.37549%                                                          |                                                 1322 |                               37016 |
| Missouri             | 2.31120%                                                          | 23.11196%                                                          | 231.11962%                                                          |                                                 5066 |                              141848 |
| Montana              | 2.43119%                                                          | 24.31188%                                                          | 243.11878%                                                          |                                                  928 |                               25984 |
| Nebraska             | 1.86145%                                                          | 18.61448%                                                          | 186.14481%                                                          |                                                 1286 |                               36008 |
| Nevada               | 0.87905%                                                          | 8.79046%                                                           | 87.90464%                                                           |                                                  967 |                               27076 |
| New Hampshire        | 0.44068%                                                          | 4.40682%                                                           | 44.06819%                                                           |                                                  214 |                                5992 |
| New Jersey           | 0.40193%                                                          | 4.01928%                                                           | 40.19279%                                                           |                                                 1275 |                               35700 |
| New Mexico           | 1.09365%                                                          | 10.93651%                                                          | 109.36514%                                                          |                                                  819 |                               22932 |
| New York             | 0.29161%                                                          | 2.91607%                                                           | 29.16073%                                                           |                                                 2026 |                               56728 |
| North Carolina       | 0.72509%                                                          | 7.25090%                                                           | 72.50895%                                                           |                                                 2716 |                               76048 |
| North Dakota         | 3.78079%                                                          | 37.80795%                                                          | 378.07947%                                                          |                                                 1029 |                               28812 |
| Ohio                 | 0.60316%                                                          | 6.03160%                                                           | 60.31602%                                                           |                                                 2518 |                               70504 |
| Oklahoma             | 1.15199%                                                          | 11.51992%                                                          | 115.19923%                                                          |                                                 1628 |                               45584 |
| Oregon               | 0.35716%                                                          | 3.57158%                                                           | 35.71584%                                                           |                                                  538 |                               15064 |
| Pennsylvania         | 0.48533%                                                          | 4.85331%                                                           | 48.53308%                                                           |                                                 2219 |                               62132 |
| Rhode Island         | 1.38499%                                                          | 13.84986%                                                          | 138.49859%                                                          |                                                  524 |                               14672 |
| South Carolina       | 0.70534%                                                          | 7.05341%                                                           | 70.53412%                                                           |                                                 1297 |                               36316 |
| South Dakota         | 3.75060%                                                          | 37.50598%                                                          | 375.05977%                                                          |                                                 1185 |                               33180 |
| Tennessee            | 1.47848%                                                          | 14.78480%                                                          | 147.84804%                                                          |                                                 3606 |                              100968 |
| Texas                | 0.76132%                                                          | 7.61322%                                                           | 76.13219%                                                           |                                                 7884 |                              220752 |
| Utah                 | 1.71181%                                                          | 17.11813%                                                          | 171.18128%                                                          |                                                 1960 |                               54880 |
| Vermont              | 0.13013%                                                          | 1.30130%                                                           | 13.01305%                                                           |                                                   29 |                                 812 |
| Virginia             | 0.43695%                                                          | 4.36951%                                                           | 43.69506%                                                           |                                                 1332 |                               37296 |
| Washington           | 0.63980%                                                          | 6.39799%                                                           | 63.97989%                                                           |                                                 1740 |                               48720 |
| West Virginia        | 0.77806%                                                          | 7.78061%                                                           | 77.80612%                                                           |                                                  498 |                               13944 |
| Wisconsin            | 3.80631%                                                          | 38.06312%                                                          | 380.63119%                                                          |                                                 7915 |                              221620 |
| Wyoming              | 2.06096%                                                          | 20.60961%                                                          | 206.09615%                                                          |                                                  426 |                               11928 |
| Puerto Rico          | 1.70699%                                                          | 17.06989%                                                          | 170.69888%                                                          |                                                 1947 |                               54516 |
| District of Columbia | 0.35310%                                                          | 3.53100%                                                           | 35.31000%                                                           |                                                   89 |                                2492 |