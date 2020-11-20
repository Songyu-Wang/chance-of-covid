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

 Updated at: 2020-11-20T00:42:26.480908+00:00

| State                | Chance of encountering 1 person with COVID if you meet 1 person   | Chance of encountering 1 person with COVID if you meet 10 people   | Chance of encountering a person with COVID if you meet 100 people   |   Max count of new case increase in the past 14 days |   Estimated people count with COVID |
|:---------------------|:------------------------------------------------------------------|:-------------------------------------------------------------------|:--------------------------------------------------------------------|-----------------------------------------------------:|------------------------------------:|
| Alabama              | 1.70175%                                                          | 17.01751%                                                          | 170.17510%                                                          |                                                 2980 |                               83440 |
| Alaska               | 2.80940%                                                          | 28.09397%                                                          | 280.93966%                                                          |                                                  734 |                               20552 |
| Arizona              | 1.33716%                                                          | 13.37159%                                                          | 133.71587%                                                          |                                                 3476 |                               97328 |
| Arkansas             | 2.52555%                                                          | 25.25545%                                                          | 252.55451%                                                          |                                                 2722 |                               76216 |
| California           | 0.77724%                                                          | 7.77238%                                                           | 77.72380%                                                           |                                                10968 |                              307104 |
| Colorado             | 3.13076%                                                          | 31.30756%                                                          | 313.07565%                                                          |                                                 6439 |                              180292 |
| Connecticut          | 3.64324%                                                          | 36.43241%                                                          | 364.32411%                                                          |                                                 4639 |                              129892 |
| Delaware             | 1.35146%                                                          | 13.51457%                                                          | 135.14568%                                                          |                                                  470 |                               13160 |
| Florida              | 1.28021%                                                          | 12.80209%                                                          | 128.02094%                                                          |                                                 9820 |                              274960 |
| Georgia              | 0.93250%                                                          | 9.32505%                                                           | 93.25050%                                                           |                                                 3536 |                               99008 |
| Hawaii               | 0.30652%                                                          | 3.06525%                                                           | 30.65249%                                                           |                                                  155 |                                4340 |
| Idaho                | 2.79050%                                                          | 27.90497%                                                          | 279.04973%                                                          |                                                 1781 |                               49868 |
| Illinois             | 3.40614%                                                          | 34.06140%                                                          | 340.61403%                                                          |                                                15415 |                              431620 |
| Indiana              | 3.46121%                                                          | 34.61206%                                                          | 346.12065%                                                          |                                                 8322 |                              233016 |
| Iowa                 | 3.88796%                                                          | 38.87964%                                                          | 388.79645%                                                          |                                                 4381 |                              122668 |
| Kansas               | 6.95263%                                                          | 69.52632%                                                          | 695.26320%                                                          |                                                 7234 |                              202552 |
| Kentucky             | 2.06380%                                                          | 20.63804%                                                          | 206.38037%                                                          |                                                 3293 |                               92204 |
| Louisiana            | 2.30623%                                                          | 23.06233%                                                          | 230.62325%                                                          |                                                 3829 |                              107212 |
| Maine                | 0.51242%                                                          | 5.12419%                                                           | 51.24192%                                                           |                                                  246 |                                6888 |
| Maryland             | 1.07495%                                                          | 10.74949%                                                          | 107.49494%                                                          |                                                 2321 |                               64988 |
| Massachusetts        | 1.23781%                                                          | 12.37809%                                                          | 123.78087%                                                          |                                                 3047 |                               85316 |
| Michigan             | 3.69021%                                                          | 36.90210%                                                          | 369.02100%                                                          |                                                13162 |                              368536 |
| Minnesota            | 4.31397%                                                          | 43.13969%                                                          | 431.39694%                                                          |                                                 8689 |                              243292 |
| Mississippi          | 1.51659%                                                          | 15.16591%                                                          | 151.65907%                                                          |                                                 1612 |                               45136 |
| Missouri             | 2.89515%                                                          | 28.95154%                                                          | 289.51541%                                                          |                                                 6346 |                              177688 |
| Montana              | 4.30174%                                                          | 43.01735%                                                          | 430.17353%                                                          |                                                 1642 |                               45976 |
| Nebraska             | 4.97930%                                                          | 49.79301%                                                          | 497.93012%                                                          |                                                 3440 |                               96320 |
| Nevada               | 2.06262%                                                          | 20.62623%                                                          | 206.26228%                                                          |                                                 2269 |                               63532 |
| New Hampshire        | 0.94520%                                                          | 9.45201%                                                           | 94.52009%                                                           |                                                  459 |                               12852 |
| New Jersey           | 1.43055%                                                          | 14.30548%                                                          | 143.05481%                                                          |                                                 4538 |                              127064 |
| New Mexico           | 3.86183%                                                          | 38.61831%                                                          | 386.18314%                                                          |                                                 2892 |                               80976 |
| New York             | 0.77738%                                                          | 7.77380%                                                           | 77.73795%                                                           |                                                 5401 |                              151228 |
| North Carolina       | 1.03718%                                                          | 10.37177%                                                          | 103.71770%                                                          |                                                 3885 |                              108780 |
| North Dakota         | 8.34053%                                                          | 83.40529%                                                          | 834.05287%                                                          |                                                 2270 |                               63560 |
| Ohio                 | 1.93332%                                                          | 19.33322%                                                          | 193.33225%                                                          |                                                 8071 |                              225988 |
| Oklahoma             | 3.18921%                                                          | 31.89207%                                                          | 318.92071%                                                          |                                                 4507 |                              126196 |
| Oregon               | 0.73622%                                                          | 7.36224%                                                           | 73.62242%                                                           |                                                 1109 |                               31052 |
| Pennsylvania         | 1.38644%                                                          | 13.86441%                                                          | 138.64408%                                                          |                                                 6339 |                              177492 |
| Rhode Island         | 3.65541%                                                          | 36.55411%                                                          | 365.54111%                                                          |                                                 1383 |                               38724 |
| South Carolina       | 1.04034%                                                          | 10.40337%                                                          | 104.03375%                                                          |                                                 1913 |                               53564 |
| South Dakota         | 6.39342%                                                          | 63.93424%                                                          | 639.34239%                                                          |                                                 2020 |                               56560 |
| Tennessee            | 3.25996%                                                          | 32.59955%                                                          | 325.99550%                                                          |                                                 7951 |                              222628 |
| Texas                | 1.12248%                                                          | 11.22477%                                                          | 112.24767%                                                          |                                                11624 |                              325472 |
| Utah                 | 4.67430%                                                          | 46.74297%                                                          | 467.42970%                                                          |                                                 5352 |                              149856 |
| Vermont              | 0.53398%                                                          | 5.33984%                                                           | 53.39838%                                                           |                                                  119 |                                3332 |
| Virginia             | 0.87817%                                                          | 8.78166%                                                           | 87.81657%                                                           |                                                 2677 |                               74956 |
| Washington           | 1.22996%                                                          | 12.29958%                                                          | 122.99582%                                                          |                                                 3345 |                               93660 |
| West Virginia        | 1.80141%                                                          | 18.01415%                                                          | 180.14147%                                                          |                                                 1153 |                               32284 |
| Wisconsin            | 4.09245%                                                          | 40.92447%                                                          | 409.24466%                                                          |                                                 8510 |                              238280 |
| Wyoming              | 6.09580%                                                          | 60.95802%                                                          | 609.58015%                                                          |                                                 1260 |                               35280 |
| Puerto Rico          | 1.16780%                                                          | 11.67801%                                                          | 116.78013%                                                          |                                                 1332 |                               37296 |
| District of Columbia | 0.97202%                                                          | 9.72017%                                                           | 97.20170%                                                           |                                                  245 |                                6860 |