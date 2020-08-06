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

 Updated at: 2020-08-06T00:37:39.477927+00:00

| State                | Chance of encountering 1 person with COVID if you meet 1 person   | Chance of encountering 1 person with COVID if you meet 10 people   | Chance of encountering a person with COVID if you meet 100 people   |   Max count of new case increase in the past 14 days |   Estimated people count with COVID |
|:---------------------|:------------------------------------------------------------------|:-------------------------------------------------------------------|:--------------------------------------------------------------------|-----------------------------------------------------:|------------------------------------:|
| Alabama              | 1.36997%                                                          | 13.69967%                                                          | 136.99667%                                                          |                                                 2399 |                               67172 |
| Alaska               | 0.89564%                                                          | 8.95639%                                                           | 89.56387%                                                           |                                                  234 |                                6552 |
| Arizona              | 1.43872%                                                          | 14.38715%                                                          | 143.87151%                                                          |                                                 3740 |                              104720 |
| Arkansas             | 1.32123%                                                          | 13.21226%                                                          | 132.12256%                                                          |                                                 1424 |                               39872 |
| California           | 0.85320%                                                          | 8.53204%                                                           | 85.32043%                                                           |                                                12040 |                              337120 |
| Colorado             | 0.39335%                                                          | 3.93350%                                                           | 39.33502%                                                           |                                                  809 |                               22652 |
| Connecticut          | 0.42723%                                                          | 4.27231%                                                           | 42.72307%                                                           |                                                  544 |                               15232 |
| Delaware             | 0.79937%                                                          | 7.99372%                                                           | 79.93723%                                                           |                                                  278 |                                7784 |
| Florida              | 1.62229%                                                          | 16.22294%                                                          | 162.22938%                                                          |                                                12444 |                              348432 |
| Georgia              | 1.26927%                                                          | 12.69272%                                                          | 126.92722%                                                          |                                                 4813 |                              134764 |
| Hawaii               | 0.40738%                                                          | 4.07381%                                                           | 40.73815%                                                           |                                                  206 |                                5768 |
| Idaho                | 0.88838%                                                          | 8.88384%                                                           | 88.83840%                                                           |                                                  567 |                               15876 |
| Illinois             | 0.43751%                                                          | 4.37506%                                                           | 43.75062%                                                           |                                                 1980 |                               55440 |
| Indiana              | 0.41425%                                                          | 4.14247%                                                           | 41.42468%                                                           |                                                  996 |                               27888 |
| Iowa                 | 0.74635%                                                          | 7.46354%                                                           | 74.63543%                                                           |                                                  841 |                               23548 |
| Kansas               | 1.02262%                                                          | 10.22615%                                                          | 102.26155%                                                          |                                                 1064 |                               29792 |
| Kentucky             | 0.52206%                                                          | 5.22061%                                                           | 52.20615%                                                           |                                                  833 |                               23324 |
| Louisiana            | 2.31286%                                                          | 23.12858%                                                          | 231.28579%                                                          |                                                 3840 |                              107520 |
| Maine                | 0.06874%                                                          | 0.68739%                                                           | 6.87392%                                                            |                                                   33 |                                 924 |
| Maryland             | 0.59653%                                                          | 5.96525%                                                           | 59.65251%                                                           |                                                 1288 |                               36064 |
| Massachusetts        | 0.34368%                                                          | 3.43678%                                                           | 34.36778%                                                           |                                                  846 |                               23688 |
| Michigan             | 0.44551%                                                          | 4.45506%                                                           | 44.55055%                                                           |                                                 1589 |                               44492 |
| Minnesota            | 0.42797%                                                          | 4.27971%                                                           | 42.79712%                                                           |                                                  862 |                               24136 |
| Mississippi          | 1.66994%                                                          | 16.69943%                                                          | 166.99433%                                                          |                                                 1775 |                               49700 |
| Missouri             | 0.95076%                                                          | 9.50757%                                                           | 95.07566%                                                           |                                                 2084 |                               58352 |
| Montana              | 0.57898%                                                          | 5.78979%                                                           | 57.89790%                                                           |                                                  221 |                                6188 |
| Nebraska             | 0.64412%                                                          | 6.44125%                                                           | 64.41247%                                                           |                                                  445 |                               12460 |
| Nevada               | 1.14903%                                                          | 11.49033%                                                          | 114.90327%                                                          |                                                 1264 |                               35392 |
| New Hampshire        | 0.19975%                                                          | 1.99748%                                                           | 19.97483%                                                           |                                                   97 |                                2716 |
| New Jersey           | 0.21751%                                                          | 2.17514%                                                           | 21.75139%                                                           |                                                  690 |                               19320 |
| New Mexico           | 0.61426%                                                          | 6.14261%                                                           | 61.42609%                                                           |                                                  460 |                               12880 |
| New York             | 0.11673%                                                          | 1.16729%                                                           | 11.67293%                                                           |                                                  811 |                               22708 |
| North Carolina       | 0.62578%                                                          | 6.25777%                                                           | 62.57768%                                                           |                                                 2344 |                               65632 |
| North Dakota         | 0.67239%                                                          | 6.72386%                                                           | 67.23862%                                                           |                                                  183 |                                5124 |
| Ohio                 | 0.41512%                                                          | 4.15122%                                                           | 41.51218%                                                           |                                                 1733 |                               48524 |
| Oklahoma             | 0.99136%                                                          | 9.91364%                                                           | 99.13644%                                                           |                                                 1401 |                               39228 |
| Oregon               | 0.27218%                                                          | 2.72184%                                                           | 27.21839%                                                           |                                                  410 |                               11480 |
| Pennsylvania         | 0.26530%                                                          | 2.65303%                                                           | 26.53025%                                                           |                                                 1213 |                               33964 |
| Rhode Island         | 0.76914%                                                          | 7.69143%                                                           | 76.91429%                                                           |                                                  291 |                                8148 |
| South Carolina       | 1.08819%                                                          | 10.88194%                                                          | 108.81941%                                                          |                                                 2001 |                               56028 |
| South Dakota         | 0.47159%                                                          | 4.71594%                                                           | 47.15941%                                                           |                                                  149 |                                4172 |
| Tennessee            | 1.77655%                                                          | 17.76555%                                                          | 177.65545%                                                          |                                                 4333 |                              121324 |
| Texas                | 1.11330%                                                          | 11.13303%                                                          | 111.33030%                                                          |                                                11529 |                              322812 |
| Utah                 | 0.75372%                                                          | 7.53722%                                                           | 75.37217%                                                           |                                                  863 |                               24164 |
| Vermont              | 0.04936%                                                          | 0.49360%                                                           | 4.93598%                                                            |                                                   11 |                                 308 |
| Virginia             | 0.49370%                                                          | 4.93702%                                                           | 49.37017%                                                           |                                                 1505 |                               42140 |
| Washington           | 0.63906%                                                          | 6.39063%                                                           | 63.90635%                                                           |                                                 1738 |                               48664 |
| West Virginia        | 0.53746%                                                          | 5.37456%                                                           | 53.74559%                                                           |                                                  344 |                                9632 |
| Wisconsin            | 0.54053%                                                          | 5.40530%                                                           | 54.05300%                                                           |                                                 1124 |                               31472 |
| Wyoming              | 0.33382%                                                          | 3.33818%                                                           | 33.38177%                                                           |                                                   69 |                                1932 |
| Puerto Rico          | 0.95651%                                                          | 9.56510%                                                           | 95.65099%                                                           |                                                 1091 |                               30548 |
| District of Columbia | 0.34517%                                                          | 3.45165%                                                           | 34.51652%                                                           |                                                   87 |                                2436 |