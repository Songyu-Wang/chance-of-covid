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

 Updated at: 2020-07-19T00:35:23.445287+00:00

| State                | Chance of encountering 1 person with COVID if you meet 1 person   | Chance of encountering 1 person with COVID if you meet 10 people   | Chance of encountering a person with COVID if you meet 100 people   |   Max count of new case increase in the past 14 days |   Estimated people count with COVID |
|:---------------------|:------------------------------------------------------------------|:-------------------------------------------------------------------|:--------------------------------------------------------------------|-----------------------------------------------------:|------------------------------------:|
| Alabama              | 1.26318%                                                          | 12.63179%                                                          | 126.31789%                                                          |                                                 2212 |                               61936 |
| Alaska               | 1.53483%                                                          | 15.34834%                                                          | 153.48338%                                                          |                                                  401 |                               11228 |
| Arizona              | 1.64375%                                                          | 16.43751%                                                          | 164.37512%                                                          |                                                 4273 |                              119644 |
| Arkansas             | 1.45112%                                                          | 14.51121%                                                          | 145.11214%                                                          |                                                 1564 |                               43792 |
| California           | 0.82869%                                                          | 8.28685%                                                           | 82.86853%                                                           |                                                11694 |                              327432 |
| Colorado             | 0.32382%                                                          | 3.23821%                                                           | 32.38211%                                                           |                                                  666 |                               18648 |
| Connecticut          | 0.20341%                                                          | 2.03406%                                                           | 20.34058%                                                           |                                                  259 |                                7252 |
| Delaware             | 0.64122%                                                          | 6.41223%                                                           | 64.12231%                                                           |                                                  223 |                                6244 |
| Florida              | 1.99462%                                                          | 19.94624%                                                          | 199.46235%                                                          |                                                15300 |                              428400 |
| Georgia              | 1.23657%                                                          | 12.36571%                                                          | 123.65712%                                                          |                                                 4689 |                              131292 |
| Hawaii               | 0.08306%                                                          | 0.83058%                                                           | 8.30584%                                                            |                                                   42 |                                1176 |
| Idaho                | 1.13907%                                                          | 11.39074%                                                          | 113.90744%                                                          |                                                  727 |                               20356 |
| Illinois             | 0.31531%                                                          | 3.15314%                                                           | 31.53138%                                                           |                                                 1427 |                               39956 |
| Indiana              | 0.34978%                                                          | 3.49781%                                                           | 34.97807%                                                           |                                                  841 |                               23548 |
| Iowa                 | 0.74635%                                                          | 7.46354%                                                           | 74.63543%                                                           |                                                  841 |                               23548 |
| Kansas               | 1.39072%                                                          | 13.90719%                                                          | 139.07186%                                                          |                                                 1447 |                               40516 |
| Kentucky             | 0.48634%                                                          | 4.86338%                                                           | 48.63382%                                                           |                                                  776 |                               21728 |
| Louisiana            | 1.59129%                                                          | 15.91294%                                                          | 159.12944%                                                          |                                                 2642 |                               73976 |
| Maine                | 0.07915%                                                          | 0.79154%                                                           | 7.91542%                                                            |                                                   38 |                                1064 |
| Maryland             | 0.38672%                                                          | 3.86722%                                                           | 38.67224%                                                           |                                                  835 |                               23380 |
| Massachusetts        | 0.14584%                                                          | 1.45840%                                                           | 14.58396%                                                           |                                                  359 |                               10052 |
| Michigan             | 0.29411%                                                          | 2.94107%                                                           | 29.41065%                                                           |                                                 1049 |                               29372 |
| Minnesota            | 0.39917%                                                          | 3.99175%                                                           | 39.91750%                                                           |                                                  804 |                               22512 |
| Mississippi          | 1.15720%                                                          | 11.57200%                                                          | 115.72001%                                                          |                                                 1230 |                               34440 |
| Missouri             | 0.51735%                                                          | 5.17350%                                                           | 51.73503%                                                           |                                                 1134 |                               31752 |
| Montana              | 0.37725%                                                          | 3.77253%                                                           | 37.72533%                                                           |                                                  144 |                                4032 |
| Nebraska             | 0.46030%                                                          | 4.60296%                                                           | 46.02959%                                                           |                                                  318 |                                8904 |
| Nevada               | 1.31539%                                                          | 13.15388%                                                          | 131.53879%                                                          |                                                 1447 |                               40516 |
| New Hampshire        | 0.10708%                                                          | 1.07082%                                                           | 10.70816%                                                           |                                                   52 |                                1456 |
| New Jersey           | 0.12389%                                                          | 1.23888%                                                           | 12.38884%                                                           |                                                  393 |                               11004 |
| New Mexico           | 0.43666%                                                          | 4.36659%                                                           | 43.66594%                                                           |                                                  327 |                                9156 |
| New York             | 0.13127%                                                          | 1.31266%                                                           | 13.12665%                                                           |                                                  912 |                               25536 |
| North Carolina       | 0.66235%                                                          | 6.62352%                                                           | 66.23517%                                                           |                                                 2481 |                               69468 |
| North Dakota         | 0.45561%                                                          | 4.55606%                                                           | 45.56060%                                                           |                                                  124 |                                3472 |
| Ohio                 | 0.40219%                                                          | 4.02187%                                                           | 40.21867%                                                           |                                                 1679 |                               47012 |
| Oklahoma             | 0.76068%                                                          | 7.60683%                                                           | 76.06829%                                                           |                                                 1075 |                               30100 |
| Oregon               | 0.46736%                                                          | 4.67360%                                                           | 46.73596%                                                           |                                                  704 |                               19712 |
| Pennsylvania         | 0.22571%                                                          | 2.25715%                                                           | 22.57149%                                                           |                                                 1032 |                               28896 |
| Rhode Island         | 0.46254%                                                          | 4.62543%                                                           | 46.25430%                                                           |                                                  175 |                                4900 |
| South Carolina       | 1.23992%                                                          | 12.39921%                                                          | 123.99213%                                                          |                                                 2280 |                               63840 |
| South Dakota         | 0.30068%                                                          | 3.00681%                                                           | 30.06808%                                                           |                                                   95 |                                2660 |
| Tennessee            | 1.35876%                                                          | 13.58759%                                                          | 135.87588%                                                          |                                                 3314 |                               92792 |
| Texas                | 1.44037%                                                          | 14.40370%                                                          | 144.03701%                                                          |                                                14916 |                              417648 |
| Utah                 | 0.83320%                                                          | 8.33199%                                                           | 83.31987%                                                           |                                                  954 |                               26712 |
| Vermont              | 0.07180%                                                          | 0.71796%                                                           | 7.17961%                                                            |                                                   16 |                                 448 |
| Virginia             | 0.35560%                                                          | 3.55596%                                                           | 35.55964%                                                           |                                                 1084 |                               30352 |
| Washington           | 0.52875%                                                          | 5.28753%                                                           | 52.87533%                                                           |                                                 1438 |                               40264 |
| West Virginia        | 0.38434%                                                          | 3.84343%                                                           | 38.43435%                                                           |                                                  246 |                                6888 |
| Wisconsin            | 0.49581%                                                          | 4.95806%                                                           | 49.58064%                                                           |                                                 1031 |                               28868 |
| Wyoming              | 0.43058%                                                          | 4.30576%                                                           | 43.05765%                                                           |                                                   89 |                                2492 |
| Puerto Rico          | 0.58653%                                                          | 5.86531%                                                           | 58.65308%                                                           |                                                  669 |                               18732 |
| District of Columbia | 0.31739%                                                          | 3.17393%                                                           | 31.73933%                                                           |                                                   80 |                                2240 |