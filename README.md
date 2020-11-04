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

 Updated at: 2020-11-04T00:38:53.152239+00:00

| State                | Chance of encountering 1 person with COVID if you meet 1 person   | Chance of encountering 1 person with COVID if you meet 10 people   | Chance of encountering a person with COVID if you meet 100 people   |   Max count of new case increase in the past 14 days |   Estimated people count with COVID |
|:---------------------|:------------------------------------------------------------------|:-------------------------------------------------------------------|:--------------------------------------------------------------------|-----------------------------------------------------:|------------------------------------:|
| Alabama              | 2.19971%                                                          | 21.99713%                                                          | 219.97130%                                                          |                                                 3852 |                              107856 |
| Alaska               | 2.02476%                                                          | 20.24756%                                                          | 202.47558%                                                          |                                                  529 |                               14812 |
| Arizona              | 0.73128%                                                          | 7.31283%                                                           | 73.12827%                                                           |                                                 1901 |                               53228 |
| Arkansas             | 1.34628%                                                          | 13.46277%                                                          | 134.62770%                                                          |                                                 1451 |                               40628 |
| California           | 0.43518%                                                          | 4.35177%                                                           | 43.51767%                                                           |                                                 6141 |                              171948 |
| Colorado             | 1.42170%                                                          | 14.21701%                                                          | 142.17009%                                                          |                                                 2924 |                               81872 |
| Connecticut          | 2.08196%                                                          | 20.81964%                                                          | 208.19642%                                                          |                                                 2651 |                               74228 |
| Delaware             | 0.59522%                                                          | 5.95216%                                                           | 59.52161%                                                           |                                                  207 |                                5796 |
| Florida              | 0.71194%                                                          | 7.11937%                                                           | 71.19372%                                                           |                                                 5461 |                              152908 |
| Georgia              | 0.67644%                                                          | 6.76435%                                                           | 67.64353%                                                           |                                                 2565 |                               71820 |
| Hawaii               | 0.27686%                                                          | 2.76861%                                                           | 27.68612%                                                           |                                                  140 |                                3920 |
| Idaho                | 1.68119%                                                          | 16.81192%                                                          | 168.11923%                                                          |                                                 1073 |                               30044 |
| Illinois             | 1.87575%                                                          | 18.75753%                                                          | 187.57525%                                                          |                                                 8489 |                              237692 |
| Indiana              | 1.50476%                                                          | 15.04764%                                                          | 150.47639%                                                          |                                                 3618 |                              101304 |
| Iowa                 | 2.28077%                                                          | 22.80773%                                                          | 228.07735%                                                          |                                                 2570 |                               71960 |
| Kansas               | 3.88863%                                                          | 38.88630%                                                          | 388.86299%                                                          |                                                 4046 |                              113288 |
| Kentucky             | 1.23903%                                                          | 12.39034%                                                          | 123.90343%                                                          |                                                 1977 |                               55356 |
| Louisiana            | 0.82094%                                                          | 8.20944%                                                           | 82.09441%                                                           |                                                 1363 |                               38164 |
| Maine                | 0.26454%                                                          | 2.64542%                                                           | 26.45416%                                                           |                                                  127 |                                3556 |
| Maryland             | 0.44786%                                                          | 4.47857%                                                           | 44.78570%                                                           |                                                  967 |                               27076 |
| Massachusetts        | 0.64267%                                                          | 6.42669%                                                           | 64.26693%                                                           |                                                 1582 |                               44296 |
| Michigan             | 1.94015%                                                          | 19.40150%                                                          | 194.01499%                                                          |                                                 6920 |                              193760 |
| Minnesota            | 1.72579%                                                          | 17.25786%                                                          | 172.57864%                                                          |                                                 3476 |                               97328 |
| Mississippi          | 1.14027%                                                          | 11.40265%                                                          | 114.02655%                                                          |                                                 1212 |                               33936 |
| Missouri             | 1.39648%                                                          | 13.96481%                                                          | 139.64807%                                                          |                                                 3061 |                               85708 |
| Montana              | 2.78486%                                                          | 27.84863%                                                          | 278.48627%                                                          |                                                 1063 |                               29764 |
| Nebraska             | 2.32319%                                                          | 23.23191%                                                          | 232.31914%                                                          |                                                 1605 |                               44940 |
| Nevada               | 1.11994%                                                          | 11.19943%                                                          | 111.99433%                                                          |                                                 1232 |                               34496 |
| New Hampshire        | 0.41185%                                                          | 4.11852%                                                           | 41.18522%                                                           |                                                  200 |                                5600 |
| New Jersey           | 0.62291%                                                          | 6.22909%                                                           | 62.29094%                                                           |                                                 1976 |                               55328 |
| New Mexico           | 1.43951%                                                          | 14.39507%                                                          | 143.95070%                                                          |                                                 1078 |                               30184 |
| New York             | 0.35969%                                                          | 3.59687%                                                           | 35.96874%                                                           |                                                 2499 |                               69972 |
| North Carolina       | 0.77021%                                                          | 7.70207%                                                           | 77.02074%                                                           |                                                 2885 |                               80780 |
| North Dakota         | 5.26519%                                                          | 52.65188%                                                          | 526.51884%                                                          |                                                 1433 |                               40124 |
| Ohio                 | 1.01301%                                                          | 10.13012%                                                          | 101.30121%                                                          |                                                 4229 |                              118412 |
| Oklahoma             | 1.29422%                                                          | 12.94222%                                                          | 129.42223%                                                          |                                                 1829 |                               51212 |
| Oregon               | 0.39566%                                                          | 3.95662%                                                           | 39.56624%                                                           |                                                  596 |                               16688 |
| Pennsylvania         | 0.62881%                                                          | 6.28809%                                                           | 62.88085%                                                           |                                                 2875 |                               80500 |
| Rhode Island         | 1.48542%                                                          | 14.85424%                                                          | 148.54238%                                                          |                                                  562 |                               15736 |
| South Carolina       | 0.76734%                                                          | 7.67337%                                                           | 76.73372%                                                           |                                                 1411 |                               39508 |
| South Dakota         | 4.93433%                                                          | 49.34331%                                                          | 493.43306%                                                          |                                                 1559 |                               43652 |
| Tennessee            | 1.47848%                                                          | 14.78480%                                                          | 147.84804%                                                          |                                                 3606 |                              100968 |
| Texas                | 0.72579%                                                          | 7.25786%                                                           | 72.57858%                                                           |                                                 7516 |                              210448 |
| Utah                 | 2.00177%                                                          | 20.01773%                                                          | 200.17729%                                                          |                                                 2292 |                               64176 |
| Vermont              | 0.13462%                                                          | 1.34618%                                                           | 13.46178%                                                           |                                                   30 |                                 840 |
| Virginia             | 0.50879%                                                          | 5.08792%                                                           | 50.87916%                                                           |                                                 1551 |                               43428 |
| Washington           | 0.57655%                                                          | 5.76554%                                                           | 57.65544%                                                           |                                                 1568 |                               43904 |
| West Virginia        | 0.81868%                                                          | 8.18683%                                                           | 81.86828%                                                           |                                                  524 |                               14672 |
| Wisconsin            | 2.93540%                                                          | 29.35405%                                                          | 293.54047%                                                          |                                                 6104 |                              170912 |
| Wyoming              | 2.52057%                                                          | 25.20566%                                                          | 252.05656%                                                          |                                                  521 |                               14588 |
| Puerto Rico          | 1.70699%                                                          | 17.06989%                                                          | 170.69888%                                                          |                                                 1947 |                               54516 |
| District of Columbia | 0.48402%                                                          | 4.84025%                                                           | 48.40248%                                                           |                                                  122 |                                3416 |