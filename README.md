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

 Updated at: 2020-09-06T12:21:15.112494+00:00

| State                | Chance of encountering 1 person with COVID if you meet 1 person   | Chance of encountering 1 person with COVID if you meet 10 people   | Chance of encountering a person with COVID if you meet 100 people   |   Max count of new case increase in the past 14 days |   Estimated people count with COVID |
|:---------------------|:------------------------------------------------------------------|:-------------------------------------------------------------------|:--------------------------------------------------------------------|-----------------------------------------------------:|------------------------------------:|
| Alabama              | 1.14897%                                                          | 11.48967%                                                          | 114.89675%                                                          |                                                 2012 |                               56336 |
| Alaska               | 0.49758%                                                          | 4.97577%                                                           | 49.75770%                                                           |                                                  130 |                                3640 |
| Arizona              | 0.42007%                                                          | 4.20074%                                                           | 42.00740%                                                           |                                                 1092 |                               30576 |
| Arkansas             | 1.01504%                                                          | 10.15043%                                                          | 101.50427%                                                          |                                                 1094 |                               30632 |
| California           | 0.48025%                                                          | 4.80246%                                                           | 48.02463%                                                           |                                                 6777 |                              189756 |
| Colorado             | 0.22317%                                                          | 2.23174%                                                           | 22.31740%                                                           |                                                  459 |                               12852 |
| Connecticut          | 0.38639%                                                          | 3.86392%                                                           | 38.63925%                                                           |                                                  492 |                               13776 |
| Delaware             | 0.76487%                                                          | 7.64867%                                                           | 76.48671%                                                           |                                                  266 |                                7448 |
| Florida              | 0.98675%                                                          | 9.86752%                                                           | 98.67520%                                                           |                                                 7569 |                              211932 |
| Georgia              | 0.70544%                                                          | 7.05444%                                                           | 70.54442%                                                           |                                                 2675 |                               74900 |
| Hawaii               | 0.75939%                                                          | 7.59391%                                                           | 75.93907%                                                           |                                                  384 |                               10752 |
| Idaho                | 0.63456%                                                          | 6.34560%                                                           | 63.45600%                                                           |                                                  405 |                               11340 |
| Illinois             | 1.23607%                                                          | 12.36065%                                                          | 123.60654%                                                          |                                                 5594 |                              156632 |
| Indiana              | 0.69041%                                                          | 6.90411%                                                           | 69.04113%                                                           |                                                 1660 |                               46480 |
| Iowa                 | 1.37645%                                                          | 13.76451%                                                          | 137.64512%                                                          |                                                 1551 |                               43428 |
| Kansas               | 1.50317%                                                          | 15.03168%                                                          | 150.31679%                                                          |                                                 1564 |                               43792 |
| Kentucky             | 0.79218%                                                          | 7.92180%                                                           | 79.21797%                                                           |                                                 1264 |                               35392 |
| Louisiana            | 0.97815%                                                          | 9.78146%                                                           | 97.81462%                                                           |                                                 1624 |                               45472 |
| Maine                | 0.11040%                                                          | 1.10399%                                                           | 11.03993%                                                           |                                                   53 |                                1484 |
| Maryland             | 0.37931%                                                          | 3.79312%                                                           | 37.93122%                                                           |                                                  819 |                               22932 |
| Massachusetts        | 0.26893%                                                          | 2.68930%                                                           | 26.89299%                                                           |                                                  662 |                               18536 |
| Michigan             | 0.38971%                                                          | 3.89712%                                                           | 38.97122%                                                           |                                                 1390 |                               38920 |
| Minnesota            | 0.57295%                                                          | 5.72945%                                                           | 57.29452%                                                           |                                                 1154 |                               32312 |
| Mississippi          | 0.85050%                                                          | 8.50495%                                                           | 85.04951%                                                           |                                                  904 |                               25312 |
| Missouri             | 0.90650%                                                          | 9.06504%                                                           | 90.65035%                                                           |                                                 1987 |                               55636 |
| Montana              | 0.49253%                                                          | 4.92525%                                                           | 49.25251%                                                           |                                                  188 |                                5264 |
| Nebraska             | 0.68610%                                                          | 6.86101%                                                           | 68.61014%                                                           |                                                  474 |                               13272 |
| Nevada               | 0.57452%                                                          | 5.74516%                                                           | 57.45164%                                                           |                                                  632 |                               17696 |
| New Hampshire        | 0.11532%                                                          | 1.15319%                                                           | 11.53186%                                                           |                                                   56 |                                1568 |
| New Jersey           | 0.14154%                                                          | 1.41542%                                                           | 14.15417%                                                           |                                                  449 |                               12572 |
| New Mexico           | 0.27642%                                                          | 2.76417%                                                           | 27.64174%                                                           |                                                  207 |                                5796 |
| New York             | 0.12796%                                                          | 1.27956%                                                           | 12.79560%                                                           |                                                  889 |                               24892 |
| North Carolina       | 0.69012%                                                          | 6.90117%                                                           | 69.01165%                                                           |                                                 2585 |                               72380 |
| North Dakota         | 1.37417%                                                          | 13.74166%                                                          | 137.41664%                                                          |                                                  374 |                               10472 |
| Ohio                 | 0.34805%                                                          | 3.48051%                                                           | 34.80507%                                                           |                                                 1453 |                               40684 |
| Oklahoma             | 0.81163%                                                          | 8.11631%                                                           | 81.16309%                                                           |                                                 1147 |                               32116 |
| Oregon               | 0.19451%                                                          | 1.94512%                                                           | 19.45119%                                                           |                                                  293 |                                8204 |
| Pennsylvania         | 0.25371%                                                          | 2.53711%                                                           | 25.37106%                                                           |                                                 1160 |                               32480 |
| Rhode Island         | 0.45990%                                                          | 4.59900%                                                           | 45.98999%                                                           |                                                  174 |                                4872 |
| South Carolina       | 0.88589%                                                          | 8.85891%                                                           | 88.58911%                                                           |                                                 1629 |                               45612 |
| South Dakota         | 1.34515%                                                          | 13.45151%                                                          | 134.51511%                                                          |                                                  425 |                               11900 |
| Tennessee            | 0.79377%                                                          | 7.93771%                                                           | 79.37710%                                                           |                                                 1936 |                               54208 |
| Texas                | 0.61280%                                                          | 6.12804%                                                           | 61.28043%                                                           |                                                 6346 |                              177688 |
| Utah                 | 0.44804%                                                          | 4.48041%                                                           | 44.80408%                                                           |                                                  513 |                               14364 |
| Vermont              | 0.07180%                                                          | 0.71796%                                                           | 7.17961%                                                            |                                                   16 |                                 448 |
| Virginia             | 0.70004%                                                          | 7.00039%                                                           | 70.00394%                                                           |                                                 2134 |                               59752 |
| Washington           | 0.37469%                                                          | 3.74687%                                                           | 37.46868%                                                           |                                                 1019 |                               28532 |
| West Virginia        | 0.40153%                                                          | 4.01530%                                                           | 40.15296%                                                           |                                                  257 |                                7196 |
| Wisconsin            | 0.74155%                                                          | 7.41546%                                                           | 74.15455%                                                           |                                                 1542 |                               43176 |
| Wyoming              | 0.24190%                                                          | 2.41897%                                                           | 24.18969%                                                           |                                                   50 |                                1400 |
| Puerto Rico          | 0.63300%                                                          | 6.32997%                                                           | 63.29974%                                                           |                                                  722 |                               20216 |
| District of Columbia | 0.29359%                                                          | 2.93589%                                                           | 29.35888%                                                           |                                                   74 |                                2072 |