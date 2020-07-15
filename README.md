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

 Updated at: 2020-07-15T12:15:30.405465+00:00

| State                | Chance of encountering 1 person with COVID if you meet 1 person   | Chance of encountering 1 person with COVID if you meet 10 people   | Chance of encountering a person with COVID if you meet 100 people   |   Max count of new case increase in the past 14 days |   Estimated people count with COVID |
|:---------------------|:------------------------------------------------------------------|:-------------------------------------------------------------------|:--------------------------------------------------------------------|-----------------------------------------------------:|------------------------------------:|
| Alabama              | 1.26318%                                                          | 12.63179%                                                          | 126.31789%                                                          |                                                 2212 |                               61936 |
| Alaska               | 0.35979%                                                          | 3.59786%                                                           | 35.97865%                                                           |                                                   94 |                                2632 |
| Arizona              | 1.87610%                                                          | 18.76100%                                                          | 187.60999%                                                          |                                                 4877 |                              136556 |
| Arkansas             | 1.45112%                                                          | 14.51121%                                                          | 145.11214%                                                          |                                                 1564 |                               43792 |
| California           | 0.82869%                                                          | 8.28685%                                                           | 82.86853%                                                           |                                                11694 |                              327432 |
| Colorado             | 0.32382%                                                          | 3.23821%                                                           | 32.38211%                                                           |                                                  666 |                               18648 |
| Connecticut          | 0.20341%                                                          | 2.03406%                                                           | 20.34058%                                                           |                                                  259 |                                7252 |
| Delaware             | 0.63547%                                                          | 6.35472%                                                           | 63.54722%                                                           |                                                  221 |                                6188 |
| Florida              | 1.99462%                                                          | 19.94624%                                                          | 199.46235%                                                          |                                                15300 |                              428400 |
| Georgia              | 1.18251%                                                          | 11.82509%                                                          | 118.25092%                                                          |                                                 4484 |                              125552 |
| Hawaii               | 0.08306%                                                          | 0.83058%                                                           | 8.30584%                                                            |                                                   42 |                                1176 |
| Idaho                | 0.90405%                                                          | 9.04052%                                                           | 90.40522%                                                           |                                                  577 |                               16156 |
| Illinois             | 0.29322%                                                          | 2.93218%                                                           | 29.32175%                                                           |                                                 1327 |                               37156 |
| Indiana              | 0.32399%                                                          | 3.23994%                                                           | 32.39942%                                                           |                                                  779 |                               21812 |
| Iowa                 | 0.67270%                                                          | 6.72695%                                                           | 67.26951%                                                           |                                                  758 |                               21224 |
| Kansas               | 1.39072%                                                          | 13.90719%                                                          | 139.07186%                                                          |                                                 1447 |                               40516 |
| Kentucky             | 0.48634%                                                          | 4.86338%                                                           | 48.63382%                                                           |                                                  776 |                               21728 |
| Louisiana            | 1.59129%                                                          | 15.91294%                                                          | 159.12944%                                                          |                                                 2642 |                               73976 |
| Maine                | 0.09374%                                                          | 0.93735%                                                           | 9.37352%                                                            |                                                   45 |                                1260 |
| Maryland             | 0.33948%                                                          | 3.39482%                                                           | 33.94821%                                                           |                                                  733 |                               20524 |
| Massachusetts        | 0.12309%                                                          | 1.23090%                                                           | 12.30903%                                                           |                                                  303 |                                8484 |
| Michigan             | 0.19205%                                                          | 1.92052%                                                           | 19.20524%                                                           |                                                  685 |                               19180 |
| Minnesota            | 0.39917%                                                          | 3.99175%                                                           | 39.91750%                                                           |                                                  804 |                               22512 |
| Mississippi          | 1.79131%                                                          | 17.91308%                                                          | 179.13082%                                                          |                                                 1904 |                               53312 |
| Missouri             | 0.51735%                                                          | 5.17350%                                                           | 51.73503%                                                           |                                                 1134 |                               31752 |
| Montana              | 0.33272%                                                          | 3.32716%                                                           | 33.27164%                                                           |                                                  127 |                                3556 |
| Nebraska             | 0.32858%                                                          | 3.28576%                                                           | 32.85760%                                                           |                                                  227 |                                6356 |
| Nevada               | 1.00359%                                                          | 10.03586%                                                          | 100.35855%                                                          |                                                 1104 |                               30912 |
| New Hampshire        | 0.08237%                                                          | 0.82370%                                                           | 8.23704%                                                            |                                                   40 |                                1120 |
| New Jersey           | 0.13492%                                                          | 1.34922%                                                           | 13.49217%                                                           |                                                  428 |                               11984 |
| New Mexico           | 0.39793%                                                          | 3.97934%                                                           | 39.79342%                                                           |                                                  298 |                                8344 |
| New York             | 0.13213%                                                          | 1.32130%                                                           | 13.21301%                                                           |                                                  918 |                               25704 |
| North Carolina       | 0.65728%                                                          | 6.57279%                                                           | 65.72793%                                                           |                                                 2462 |                               68936 |
| North Dakota         | 0.39682%                                                          | 3.96818%                                                           | 39.68181%                                                           |                                                  108 |                                3024 |
| Ohio                 | 0.36530%                                                          | 3.65298%                                                           | 36.52976%                                                           |                                                 1525 |                               42700 |
| Oklahoma             | 0.70266%                                                          | 7.02659%                                                           | 70.26587%                                                           |                                                  993 |                               27804 |
| Oregon               | 0.26355%                                                          | 2.63554%                                                           | 26.35537%                                                           |                                                  397 |                               11116 |
| Pennsylvania         | 0.22068%                                                          | 2.20684%                                                           | 22.06845%                                                           |                                                 1009 |                               28252 |
| Rhode Island         | 0.46254%                                                          | 4.62543%                                                           | 46.25430%                                                           |                                                  175 |                                4900 |
| South Carolina       | 1.23992%                                                          | 12.39921%                                                          | 123.99213%                                                          |                                                 2280 |                               63840 |
| South Dakota         | 0.29752%                                                          | 2.97516%                                                           | 29.75158%                                                           |                                                   94 |                                2632 |
| Tennessee            | 1.35876%                                                          | 13.58759%                                                          | 135.87588%                                                          |                                                 3314 |                               92792 |
| Texas                | 1.03760%                                                          | 10.37596%                                                          | 103.75957%                                                          |                                                10745 |                              300860 |
| Utah                 | 0.75722%                                                          | 7.57215%                                                           | 75.72152%                                                           |                                                  867 |                               24276 |
| Vermont              | 0.07628%                                                          | 0.76283%                                                           | 7.62834%                                                            |                                                   17 |                                 476 |
| Virginia             | 0.31886%                                                          | 3.18856%                                                           | 31.88558%                                                           |                                                  972 |                               27216 |
| Washington           | 0.52875%                                                          | 5.28753%                                                           | 52.87533%                                                           |                                                 1438 |                               40264 |
| West Virginia        | 0.38434%                                                          | 3.84343%                                                           | 38.43435%                                                           |                                                  246 |                                6888 |
| Wisconsin            | 0.47176%                                                          | 4.71761%                                                           | 47.17615%                                                           |                                                  981 |                               27468 |
| Wyoming              | 0.43058%                                                          | 4.30576%                                                           | 43.05765%                                                           |                                                   89 |                                2492 |
| Puerto Rico          | 0.58653%                                                          | 5.86531%                                                           | 58.65308%                                                           |                                                  669 |                               18732 |
| District of Columbia | 0.28962%                                                          | 2.89621%                                                           | 28.96214%                                                           |                                                   73 |                                2044 |