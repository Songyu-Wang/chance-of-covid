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

 Updated at: 2020-10-22T18:35:26.826145+00:00

| State                | Chance of encountering 1 person with COVID if you meet 1 person   | Chance of encountering 1 person with COVID if you meet 10 people   | Chance of encountering a person with COVID if you meet 100 people   |   Max count of new case increase in the past 14 days |   Estimated people count with COVID |
|:---------------------|:------------------------------------------------------------------|:-------------------------------------------------------------------|:--------------------------------------------------------------------|-----------------------------------------------------:|------------------------------------:|
| Alabama              | 0.85088%                                                          | 8.50876%                                                           | 85.08755%                                                           |                                                 1490 |                               41720 |
| Alaska               | 0.98750%                                                          | 9.87499%                                                           | 98.74991%                                                           |                                                  258 |                                7224 |
| Arizona              | 0.42815%                                                          | 4.28152%                                                           | 42.81524%                                                           |                                                 1113 |                               31164 |
| Arkansas             | 1.92524%                                                          | 19.25241%                                                          | 192.52410%                                                          |                                                 2075 |                               58100 |
| California           | 0.29550%                                                          | 2.95503%                                                           | 29.55035%                                                           |                                                 4170 |                              116760 |
| Colorado             | 0.63792%                                                          | 6.37918%                                                           | 63.79178%                                                           |                                                 1312 |                               36736 |
| Connecticut          | 1.05158%                                                          | 10.51584%                                                          | 105.15843%                                                          |                                                 1339 |                               37492 |
| Delaware             | 0.62685%                                                          | 6.26846%                                                           | 62.68459%                                                           |                                                  218 |                                6104 |
| Florida              | 0.72615%                                                          | 7.26147%                                                           | 72.61473%                                                           |                                                 5570 |                              155960 |
| Georgia              | 0.43250%                                                          | 4.32497%                                                           | 43.24967%                                                           |                                                 1640 |                               45920 |
| Hawaii               | 0.32630%                                                          | 3.26301%                                                           | 32.63007%                                                           |                                                  165 |                                4620 |
| Idaho                | 1.71410%                                                          | 17.14095%                                                          | 171.40955%                                                          |                                                 1094 |                               30632 |
| Illinois             | 1.12757%                                                          | 11.27573%                                                          | 112.75727%                                                          |                                                 5103 |                              142884 |
| Indiana              | 1.03229%                                                          | 10.32290%                                                          | 103.22897%                                                          |                                                 2482 |                               69496 |
| Iowa                 | 1.18298%                                                          | 11.82985%                                                          | 118.29848%                                                          |                                                 1333 |                               37324 |
| Kansas               | 2.03081%                                                          | 20.30814%                                                          | 203.08144%                                                          |                                                 2113 |                               59164 |
| Kentucky             | 0.91000%                                                          | 9.10004%                                                           | 91.00039%                                                           |                                                 1452 |                               40656 |
| Louisiana            | 0.82094%                                                          | 8.20944%                                                           | 82.09441%                                                           |                                                 1363 |                               38164 |
| Maine                | 0.09998%                                                          | 0.99984%                                                           | 9.99842%                                                            |                                                   48 |                                1344 |
| Maryland             | 0.36959%                                                          | 3.69586%                                                           | 36.95862%                                                           |                                                  798 |                               22344 |
| Massachusetts        | 0.39649%                                                          | 3.96489%                                                           | 39.64888%                                                           |                                                  976 |                               27328 |
| Michigan             | 1.40296%                                                          | 14.02964%                                                          | 140.29639%                                                          |                                                 5004 |                              140112 |
| Minnesota            | 1.13695%                                                          | 11.36954%                                                          | 113.69536%                                                          |                                                 2290 |                               64120 |
| Mississippi          | 1.24375%                                                          | 12.43755%                                                          | 124.37549%                                                          |                                                 1322 |                               37016 |
| Missouri             | 2.31120%                                                          | 23.11196%                                                          | 231.11962%                                                          |                                                 5066 |                              141848 |
| Montana              | 1.89413%                                                          | 18.94126%                                                          | 189.41258%                                                          |                                                  723 |                               20244 |
| Nebraska             | 1.86145%                                                          | 18.61448%                                                          | 186.14481%                                                          |                                                 1286 |                               36008 |
| Nevada               | 0.87905%                                                          | 8.79046%                                                           | 87.90464%                                                           |                                                  967 |                               27076 |
| New Hampshire        | 0.44068%                                                          | 4.40682%                                                           | 44.06819%                                                           |                                                  214 |                                5992 |
| New Jersey           | 0.40918%                                                          | 4.09178%                                                           | 40.91784%                                                           |                                                 1298 |                               36344 |
| New Mexico           | 1.08430%                                                          | 10.84304%                                                          | 108.43040%                                                          |                                                  812 |                               22736 |
| New York             | 0.29161%                                                          | 2.91607%                                                           | 29.16073%                                                           |                                                 2026 |                               56728 |
| North Carolina       | 0.71655%                                                          | 7.16547%                                                           | 71.65465%                                                           |                                                 2684 |                               75152 |
| North Dakota         | 3.78079%                                                          | 37.80795%                                                          | 378.07947%                                                          |                                                 1029 |                               28812 |
| Ohio                 | 0.56675%                                                          | 5.66750%                                                           | 56.67502%                                                           |                                                 2366 |                               66248 |
| Oklahoma             | 1.08477%                                                          | 10.84769%                                                          | 108.47691%                                                          |                                                 1533 |                               42924 |
| Oregon               | 0.31998%                                                          | 3.19982%                                                           | 31.99820%                                                           |                                                  482 |                               13496 |
| Pennsylvania         | 0.40616%                                                          | 4.06156%                                                           | 40.61556%                                                           |                                                 1857 |                               51996 |
| Rhode Island         | 1.25283%                                                          | 12.52831%                                                          | 125.28307%                                                          |                                                  474 |                               13272 |
| South Carolina       | 0.70534%                                                          | 7.05341%                                                           | 70.53412%                                                           |                                                 1297 |                               36316 |
| South Dakota         | 2.77259%                                                          | 27.72594%                                                          | 277.25937%                                                          |                                                  876 |                               24528 |
| Tennessee            | 1.35999%                                                          | 13.59989%                                                          | 135.99888%                                                          |                                                 3317 |                               92876 |
| Texas                | 0.76132%                                                          | 7.61322%                                                           | 76.13219%                                                           |                                                 7884 |                              220752 |
| Utah                 | 1.31093%                                                          | 13.10934%                                                          | 131.09342%                                                          |                                                 1501 |                               42028 |
| Vermont              | 0.06731%                                                          | 0.67309%                                                           | 6.73089%                                                            |                                                   15 |                                 420 |
| Virginia             | 0.60491%                                                          | 6.04908%                                                           | 60.49076%                                                           |                                                 1844 |                               51632 |
| Washington           | 0.63980%                                                          | 6.39799%                                                           | 63.97989%                                                           |                                                 1740 |                               48720 |
| West Virginia        | 0.77806%                                                          | 7.78061%                                                           | 77.80612%                                                           |                                                  498 |                               13944 |
| Wisconsin            | 3.80631%                                                          | 38.06312%                                                          | 380.63119%                                                          |                                                 7915 |                              221620 |
| Wyoming              | 1.55782%                                                          | 15.57816%                                                          | 155.78159%                                                          |                                                  322 |                                9016 |
| Puerto Rico          | 0.85569%                                                          | 8.55686%                                                           | 85.56862%                                                           |                                                  976 |                               27328 |
| District of Columbia | 0.35310%                                                          | 3.53100%                                                           | 35.31000%                                                           |                                                   89 |                                2492 |