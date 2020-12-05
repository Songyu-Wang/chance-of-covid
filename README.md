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

 Updated at: 2020-12-05T12:24:19.401179+00:00

| State                | Chance of encountering 1 person with COVID if you meet 1 person   | Chance of encountering 1 person with COVID if you meet 10 people   | Chance of encountering a person with COVID if you meet 100 people   |   Max count of new case increase in the past 14 days |   Estimated people count with COVID |
|:---------------------|:------------------------------------------------------------------|:-------------------------------------------------------------------|:--------------------------------------------------------------------|-----------------------------------------------------:|------------------------------------:|
| Alabama              | 2.24311%                                                          | 22.43113%                                                          | 224.31134%                                                          |                                                 3928 |                              109984 |
| Alaska               | 2.90891%                                                          | 29.08912%                                                          | 290.89120%                                                          |                                                  760 |                               21280 |
| Arizona              | 3.97070%                                                          | 39.70700%                                                          | 397.06998%                                                          |                                                10322 |                              289016 |
| Arkansas             | 2.62297%                                                          | 26.22967%                                                          | 262.29669%                                                          |                                                 2827 |                               79156 |
| California           | 1.56029%                                                          | 15.60287%                                                          | 156.02868%                                                          |                                                22018 |                              616504 |
| Colorado             | 2.97225%                                                          | 29.72249%                                                          | 297.22495%                                                          |                                                 6113 |                              171164 |
| Connecticut          | 4.13958%                                                          | 41.39583%                                                          | 413.95826%                                                          |                                                 5271 |                              147588 |
| Delaware             | 2.70866%                                                          | 27.08665%                                                          | 270.86645%                                                          |                                                  942 |                               26376 |
| Florida              | 2.18952%                                                          | 21.89523%                                                          | 218.95230%                                                          |                                                16795 |                              470260 |
| Georgia              | 1.30461%                                                          | 13.04610%                                                          | 130.46104%                                                          |                                                 4947 |                              138516 |
| Hawaii               | 0.32037%                                                          | 3.20368%                                                           | 32.03679%                                                           |                                                  162 |                                4536 |
| Idaho                | 3.12893%                                                          | 31.28929%                                                          | 312.89293%                                                          |                                                 1997 |                               55916 |
| Illinois             | 2.77131%                                                          | 27.71314%                                                          | 277.13144%                                                          |                                                12542 |                              351176 |
| Indiana              | 3.51860%                                                          | 35.18602%                                                          | 351.86021%                                                          |                                                 8460 |                              236880 |
| Iowa                 | 2.87803%                                                          | 28.78034%                                                          | 287.80344%                                                          |                                                 3243 |                               90804 |
| Kansas               | 7.23327%                                                          | 72.33275%                                                          | 723.32745%                                                          |                                                 7526 |                              210728 |
| Kentucky             | 3.51968%                                                          | 35.19685%                                                          | 351.96846%                                                          |                                                 5616 |                              157248 |
| Louisiana            | 3.20789%                                                          | 32.07886%                                                          | 320.78857%                                                          |                                                 5326 |                              149128 |
| Maine                | 0.72072%                                                          | 7.20720%                                                           | 72.07196%                                                           |                                                  346 |                                9688 |
| Maryland             | 1.75623%                                                          | 17.56229%                                                          | 175.62292%                                                          |                                                 3792 |                              106176 |
| Massachusetts        | 2.71164%                                                          | 27.11642%                                                          | 271.16419%                                                          |                                                 6675 |                              186900 |
| Michigan             | 4.86944%                                                          | 48.69440%                                                          | 486.94399%                                                          |                                                17368 |                              486304 |
| Minnesota            | 4.47930%                                                          | 44.79299%                                                          | 447.92994%                                                          |                                                 9022 |                              252616 |
| Mississippi          | 2.33322%                                                          | 23.33217%                                                          | 233.32165%                                                          |                                                 2480 |                               69440 |
| Missouri             | 2.22451%                                                          | 22.24515%                                                          | 222.45149%                                                          |                                                 4876 |                              136528 |
| Montana              | 3.44244%                                                          | 34.42436%                                                          | 344.24361%                                                          |                                                 1314 |                               36792 |
| Nebraska             | 4.16293%                                                          | 41.62927%                                                          | 416.29274%                                                          |                                                 2876 |                               80528 |
| Nevada               | 2.87167%                                                          | 28.71673%                                                          | 287.16727%                                                          |                                                 3159 |                               88452 |
| New Hampshire        | 1.58975%                                                          | 15.89750%                                                          | 158.97496%                                                          |                                                  772 |                               21616 |
| New Jersey           | 1.78519%                                                          | 17.85190%                                                          | 178.51904%                                                          |                                                 5663 |                              158564 |
| New Mexico           | 3.27962%                                                          | 32.79619%                                                          | 327.96189%                                                          |                                                 2456 |                               68768 |
| New York             | 1.62226%                                                          | 16.22263%                                                          | 162.22634%                                                          |                                                11271 |                              315588 |
| North Carolina       | 2.13789%                                                          | 21.37893%                                                          | 213.78929%                                                          |                                                 8008 |                              224224 |
| North Dakota         | 5.59954%                                                          | 55.99544%                                                          | 559.95444%                                                          |                                                 1524 |                               42672 |
| Ohio                 | 4.08774%                                                          | 40.87740%                                                          | 408.77399%                                                          |                                                17065 |                              477820 |
| Oklahoma             | 4.42753%                                                          | 44.27528%                                                          | 442.75280%                                                          |                                                 6257 |                              175196 |
| Oregon               | 1.44324%                                                          | 14.43238%                                                          | 144.32384%                                                          |                                                 2174 |                               60872 |
| Pennsylvania         | 2.57276%                                                          | 25.72756%                                                          | 257.27565%                                                          |                                                11763 |                              329364 |
| Rhode Island         | 4.53821%                                                          | 45.38207%                                                          | 453.82075%                                                          |                                                 1717 |                               48076 |
| South Carolina       | 1.60428%                                                          | 16.04284%                                                          | 160.42841%                                                          |                                                 2950 |                               82600 |
| South Dakota         | 6.76690%                                                          | 67.66901%                                                          | 676.69011%                                                          |                                                 2138 |                               59864 |
| Tennessee            | 3.26980%                                                          | 32.69795%                                                          | 326.97951%                                                          |                                                 7975 |                              223300 |
| Texas                | 1.58599%                                                          | 15.85991%                                                          | 158.59908%                                                          |                                                16424 |                              459872 |
| Utah                 | 5.36426%                                                          | 53.64262%                                                          | 536.42624%                                                          |                                                 6142 |                              171976 |
| Vermont              | 1.00515%                                                          | 10.05146%                                                          | 100.51459%                                                          |                                                  224 |                                6272 |
| Virginia             | 1.06351%                                                          | 10.63509%                                                          | 106.35089%                                                          |                                                 3242 |                               90776 |
| Washington           | 2.30806%                                                          | 23.08056%                                                          | 230.80561%                                                          |                                                 6277 |                              175756 |
| West Virginia        | 1.79985%                                                          | 17.99852%                                                          | 179.98524%                                                          |                                                 1152 |                               32256 |
| Wisconsin            | 3.38024%                                                          | 33.80236%                                                          | 338.02358%                                                          |                                                 7029 |                              196812 |
| Wyoming              | 6.10548%                                                          | 61.05477%                                                          | 610.54774%                                                          |                                                 1262 |                               35336 |
| Puerto Rico          | 1.27301%                                                          | 12.73009%                                                          | 127.30086%                                                          |                                                 1452 |                               40656 |
| District of Columbia | 1.47191%                                                          | 14.71911%                                                          | 147.19114%                                                          |                                                  371 |                               10388 |