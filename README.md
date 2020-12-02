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

 Updated at: 2020-12-02T00:48:10.973409+00:00

| State                | Chance of encountering 1 person with COVID if you meet 1 person   | Chance of encountering 1 person with COVID if you meet 10 people   | Chance of encountering a person with COVID if you meet 100 people   |   Max count of new case increase in the past 14 days |   Estimated people count with COVID |
|:---------------------|:------------------------------------------------------------------|:-------------------------------------------------------------------|:--------------------------------------------------------------------|-----------------------------------------------------:|------------------------------------:|
| Alabama              | 1.92789%                                                          | 19.27890%                                                          | 192.78897%                                                          |                                                 3376 |                               94528 |
| Alaska               | 2.58357%                                                          | 25.83573%                                                          | 258.35731%                                                          |                                                  675 |                               18900 |
| Arizona              | 3.97070%                                                          | 39.70700%                                                          | 397.06998%                                                          |                                                10322 |                              289016 |
| Arkansas             | 2.17854%                                                          | 21.78538%                                                          | 217.85378%                                                          |                                                 2348 |                               65744 |
| California           | 1.30036%                                                          | 13.00357%                                                          | 130.03571%                                                          |                                                18350 |                              513800 |
| Colorado             | 2.97225%                                                          | 29.72249%                                                          | 297.22495%                                                          |                                                 6113 |                              171164 |
| Connecticut          | 4.13958%                                                          | 41.39583%                                                          | 413.95826%                                                          |                                                 5271 |                              147588 |
| Delaware             | 1.98118%                                                          | 19.81178%                                                          | 198.11782%                                                          |                                                  689 |                               19292 |
| Florida              | 2.18952%                                                          | 21.89523%                                                          | 218.95230%                                                          |                                                16795 |                              470260 |
| Georgia              | 0.79775%                                                          | 7.97745%                                                           | 79.77454%                                                           |                                                 3025 |                               84700 |
| Hawaii               | 0.32037%                                                          | 3.20368%                                                           | 32.03679%                                                           |                                                  162 |                                4536 |
| Idaho                | 3.12893%                                                          | 31.28929%                                                          | 312.89293%                                                          |                                                 1997 |                               55916 |
| Illinois             | 3.22871%                                                          | 32.28707%                                                          | 322.87072%                                                          |                                                14612 |                              409136 |
| Indiana              | 3.02824%                                                          | 30.28244%                                                          | 302.82437%                                                          |                                                 7281 |                              203868 |
| Iowa                 | 3.08570%                                                          | 30.85700%                                                          | 308.57002%                                                          |                                                 3477 |                               97356 |
| Kansas               | 7.23327%                                                          | 72.33275%                                                          | 723.32745%                                                          |                                                 7526 |                              210728 |
| Kentucky             | 3.51968%                                                          | 35.19685%                                                          | 351.96846%                                                          |                                                 5616 |                              157248 |
| Louisiana            | 3.20789%                                                          | 32.07886%                                                          | 320.78857%                                                          |                                                 5326 |                              149128 |
| Maine                | 0.53117%                                                          | 5.31166%                                                           | 53.11662%                                                           |                                                  255 |                                7140 |
| Maryland             | 1.34774%                                                          | 13.47739%                                                          | 134.77392%                                                          |                                                 2910 |                               81480 |
| Massachusetts        | 1.89226%                                                          | 18.92259%                                                          | 189.22589%                                                          |                                                 4658 |                              130424 |
| Michigan             | 4.86944%                                                          | 48.69440%                                                          | 486.94399%                                                          |                                                17368 |                              486304 |
| Minnesota            | 4.47930%                                                          | 44.79299%                                                          | 447.92994%                                                          |                                                 9022 |                              252616 |
| Mississippi          | 1.85528%                                                          | 18.55283%                                                          | 185.52835%                                                          |                                                 1972 |                               55216 |
| Missouri             | 2.22451%                                                          | 22.24515%                                                          | 222.45149%                                                          |                                                 4876 |                              136528 |
| Montana              | 3.86423%                                                          | 38.64226%                                                          | 386.42262%                                                          |                                                 1475 |                               41300 |
| Nebraska             | 4.16293%                                                          | 41.62927%                                                          | 416.29274%                                                          |                                                 2876 |                               80528 |
| Nevada               | 2.87167%                                                          | 28.71673%                                                          | 287.16727%                                                          |                                                 3159 |                               88452 |
| New Hampshire        | 1.58975%                                                          | 15.89750%                                                          | 158.97496%                                                          |                                                  772 |                               21616 |
| New Jersey           | 1.47184%                                                          | 14.71844%                                                          | 147.18442%                                                          |                                                 4669 |                              130732 |
| New Mexico           | 4.89406%                                                          | 48.94057%                                                          | 489.40567%                                                          |                                                 3665 |                              102620 |
| New York             | 1.17679%                                                          | 11.76792%                                                          | 117.67923%                                                          |                                                 8176 |                              228928 |
| North Carolina       | 2.13789%                                                          | 21.37893%                                                          | 213.78929%                                                          |                                                 8008 |                              224224 |
| North Dakota         | 5.59954%                                                          | 55.99544%                                                          | 559.95444%                                                          |                                                 1524 |                               42672 |
| Ohio                 | 4.08774%                                                          | 40.87740%                                                          | 408.77399%                                                          |                                                17065 |                              477820 |
| Oklahoma             | 4.42753%                                                          | 44.27528%                                                          | 442.75280%                                                          |                                                 6257 |                              175196 |
| Oregon               | 1.11131%                                                          | 11.11307%                                                          | 111.13068%                                                          |                                                 1674 |                               46872 |
| Pennsylvania         | 1.84268%                                                          | 18.42682%                                                          | 184.26824%                                                          |                                                 8425 |                              235900 |
| Rhode Island         | 3.71356%                                                          | 37.13559%                                                          | 371.35594%                                                          |                                                 1405 |                               39340 |
| South Carolina       | 1.20457%                                                          | 12.04573%                                                          | 120.45726%                                                          |                                                 2215 |                               62020 |
| South Dakota         | 6.76690%                                                          | 67.66901%                                                          | 676.69011%                                                          |                                                 2138 |                               59864 |
| Tennessee            | 3.26980%                                                          | 32.69795%                                                          | 326.97951%                                                          |                                                 7975 |                              223300 |
| Texas                | 1.55847%                                                          | 15.58470%                                                          | 155.84696%                                                          |                                                16139 |                              451892 |
| Utah                 | 5.36426%                                                          | 53.64262%                                                          | 536.42624%                                                          |                                                 6142 |                              171976 |
| Vermont              | 0.79873%                                                          | 7.98732%                                                           | 79.87320%                                                           |                                                  178 |                                4984 |
| Virginia             | 1.06351%                                                          | 10.63509%                                                          | 106.35089%                                                          |                                                 3242 |                               90776 |
| Washington           | 2.30806%                                                          | 23.08056%                                                          | 230.80561%                                                          |                                                 6277 |                              175756 |
| West Virginia        | 1.79985%                                                          | 17.99852%                                                          | 179.98524%                                                          |                                                 1152 |                               32256 |
| Wisconsin            | 4.09245%                                                          | 40.92447%                                                          | 409.24466%                                                          |                                                 8510 |                              238280 |
| Wyoming              | 6.10548%                                                          | 61.05477%                                                          | 610.54774%                                                          |                                                 1262 |                               35336 |
| Puerto Rico          | 1.27301%                                                          | 12.73009%                                                          | 127.30086%                                                          |                                                 1452 |                               40656 |
| District of Columbia | 1.47191%                                                          | 14.71911%                                                          | 147.19114%                                                          |                                                  371 |                               10388 |