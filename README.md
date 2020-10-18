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

 Updated at: 2020-10-18T01:16:57.097022+00:00

| State                | Chance of encountering 1 person with COVID if you meet 1 person   | Chance of encountering 1 person with COVID if you meet 10 people   | Chance of encountering a person with COVID if you meet 100 people   |   Max count of new case increase in the past 14 days |   Estimated people count with COVID |
|:---------------------|:------------------------------------------------------------------|:-------------------------------------------------------------------|:--------------------------------------------------------------------|-----------------------------------------------------:|------------------------------------:|
| Alabama              | 0.85088%                                                          | 8.50876%                                                           | 85.08755%                                                           |                                                 1490 |                               41720 |
| Alaska               | 1.04874%                                                          | 10.48739%                                                          | 104.87393%                                                          |                                                  274 |                                7672 |
| Arizona              | 0.42815%                                                          | 4.28152%                                                           | 42.81524%                                                           |                                                 1113 |                               31164 |
| Arkansas             | 1.92524%                                                          | 19.25241%                                                          | 192.52410%                                                          |                                                 2075 |                               58100 |
| California           | 0.30422%                                                          | 3.04220%                                                           | 30.42198%                                                           |                                                 4293 |                              120204 |
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
| Kansas               | 1.97507%                                                          | 19.75070%                                                          | 197.50703%                                                          |                                                 2055 |                               57540 |
| Kentucky             | 1.49975%                                                          | 14.99752%                                                          | 149.97517%                                                          |                                                 2393 |                               67004 |
| Louisiana            | 1.29857%                                                          | 12.98573%                                                          | 129.85734%                                                          |                                                 2156 |                               60368 |
| Maine                | 0.09998%                                                          | 0.99984%                                                           | 9.99842%                                                            |                                                   48 |                                1344 |
| Maryland             | 0.36959%                                                          | 3.69586%                                                           | 36.95862%                                                           |                                                  798 |                               22344 |
| Massachusetts        | 0.31158%                                                          | 3.11585%                                                           | 31.15849%                                                           |                                                  767 |                               21476 |
| Michigan             | 0.68915%                                                          | 6.89146%                                                           | 68.91457%                                                           |                                                 2458 |                               68824 |
| Minnesota            | 1.13695%                                                          | 11.36954%                                                          | 113.69536%                                                          |                                                 2290 |                               64120 |
| Mississippi          | 1.44697%                                                          | 14.46971%                                                          | 144.69706%                                                          |                                                 1538 |                               43064 |
| Missouri             | 2.31120%                                                          | 23.11196%                                                          | 231.11962%                                                          |                                                 5066 |                              141848 |
| Montana              | 1.89413%                                                          | 18.94126%                                                          | 189.41258%                                                          |                                                  723 |                               20244 |
| Nebraska             | 1.86145%                                                          | 18.61448%                                                          | 186.14481%                                                          |                                                 1286 |                               36008 |
| Nevada               | 0.87905%                                                          | 8.79046%                                                           | 87.90464%                                                           |                                                  967 |                               27076 |
| New Hampshire        | 0.44068%                                                          | 4.40682%                                                           | 44.06819%                                                           |                                                  214 |                                5992 |
| New Jersey           | 0.40918%                                                          | 4.09178%                                                           | 40.91784%                                                           |                                                 1298 |                               36344 |
| New Mexico           | 1.08430%                                                          | 10.84304%                                                          | 108.43040%                                                          |                                                  812 |                               22736 |
| New York             | 0.26426%                                                          | 2.64260%                                                           | 26.42601%                                                           |                                                 1836 |                               51408 |
| North Carolina       | 0.71655%                                                          | 7.16547%                                                           | 71.65465%                                                           |                                                 2684 |                               75152 |
| North Dakota         | 3.17454%                                                          | 31.74545%                                                          | 317.45449%                                                          |                                                  864 |                               24192 |
| Ohio                 | 0.53513%                                                          | 5.35131%                                                           | 53.51310%                                                           |                                                 2234 |                               62552 |
| Oklahoma             | 1.08477%                                                          | 10.84769%                                                          | 108.47691%                                                          |                                                 1533 |                               42924 |
| Oregon               | 0.31998%                                                          | 3.19982%                                                           | 31.99820%                                                           |                                                  482 |                               13496 |
| Pennsylvania         | 0.49233%                                                          | 4.92330%                                                           | 49.23297%                                                           |                                                 2251 |                               63028 |
| Rhode Island         | 0.75593%                                                          | 7.55927%                                                           | 75.59274%                                                           |                                                  286 |                                8008 |
| South Carolina       | 0.70534%                                                          | 7.05341%                                                           | 70.53412%                                                           |                                                 1297 |                               36316 |
| South Dakota         | 3.26001%                                                          | 32.60013%                                                          | 326.00132%                                                          |                                                 1030 |                               28840 |
| Tennessee            | 1.21567%                                                          | 12.15667%                                                          | 121.56668%                                                          |                                                 2965 |                               83020 |
| Texas                | 0.56684%                                                          | 5.66839%                                                           | 56.68391%                                                           |                                                 5870 |                              164360 |
| Utah                 | 1.31093%                                                          | 13.10934%                                                          | 131.09342%                                                          |                                                 1501 |                               42028 |
| Vermont              | 0.14359%                                                          | 1.43592%                                                           | 14.35923%                                                           |                                                   32 |                                 896 |
| Virginia             | 0.60491%                                                          | 6.04908%                                                           | 60.49076%                                                           |                                                 1844 |                               51632 |
| Washington           | 0.63980%                                                          | 6.39799%                                                           | 63.97989%                                                           |                                                 1740 |                               48720 |
| West Virginia        | 0.77806%                                                          | 7.78061%                                                           | 77.80612%                                                           |                                                  498 |                               13944 |
| Wisconsin            | 1.97409%                                                          | 19.74088%                                                          | 197.40885%                                                          |                                                 4105 |                              114940 |
| Wyoming              | 1.40300%                                                          | 14.03002%                                                          | 140.30019%                                                          |                                                  290 |                                8120 |
| Puerto Rico          | 0.85569%                                                          | 8.55686%                                                           | 85.56862%                                                           |                                                  976 |                               27328 |
| District of Columbia | 0.41658%                                                          | 4.16579%                                                           | 41.65787%                                                           |                                                  105 |                                2940 |