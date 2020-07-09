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

 Updated at: 2020-07-09T18:12:22.861471+00:00

| State                | Chance of encountering 1 person with COVID if you meet 1 person   | Chance of encountering 1 person with COVID if you meet 10 people   | Chance of encountering a person with COVID if you meet 100 people   |   Max count of new case increase in the past 14 days |   Estimated people count with COVID |
|:---------------------|:------------------------------------------------------------------|:-------------------------------------------------------------------|:--------------------------------------------------------------------|-----------------------------------------------------:|------------------------------------:|
| Alabama              | 1.00163%                                                          | 10.01635%                                                          | 100.16347%                                                          |                                                 1754 |                               49112 |
| Alaska               | 0.18372%                                                          | 1.83721%                                                           | 18.37208%                                                           |                                                   48 |                                1344 |
| Arizona              | 1.87610%                                                          | 18.76100%                                                          | 187.60999%                                                          |                                                 4877 |                              136556 |
| Arkansas             | 0.96865%                                                          | 9.68651%                                                           | 96.86514%                                                           |                                                 1044 |                               29232 |
| California           | 0.82869%                                                          | 8.28685%                                                           | 82.86853%                                                           |                                                11694 |                              327432 |
| Colorado             | 0.19789%                                                          | 1.97891%                                                           | 19.78906%                                                           |                                                  407 |                               11396 |
| Connecticut          | 0.20341%                                                          | 2.03406%                                                           | 20.34058%                                                           |                                                  259 |                                7252 |
| Delaware             | 0.63547%                                                          | 6.35472%                                                           | 63.54722%                                                           |                                                  221 |                                6188 |
| Florida              | 1.49375%                                                          | 14.93751%                                                          | 149.37514%                                                          |                                                11458 |                              320824 |
| Georgia              | 0.91563%                                                          | 9.15627%                                                           | 91.56271%                                                           |                                                 3472 |                               97216 |
| Hawaii               | 0.08108%                                                          | 0.81081%                                                           | 8.10808%                                                            |                                                   41 |                                1148 |
| Idaho                | 0.76304%                                                          | 7.63039%                                                           | 76.30388%                                                           |                                                  487 |                               13636 |
| Illinois             | 0.21654%                                                          | 2.16543%                                                           | 21.65435%                                                           |                                                  980 |                               27440 |
| Indiana              | 0.23956%                                                          | 2.39564%                                                           | 23.95644%                                                           |                                                  576 |                               16128 |
| Iowa                 | 0.67270%                                                          | 6.72695%                                                           | 67.26951%                                                           |                                                  758 |                               21224 |
| Kansas               | 0.94380%                                                          | 9.43805%                                                           | 94.38049%                                                           |                                                  982 |                               27496 |
| Kentucky             | 0.48634%                                                          | 4.86338%                                                           | 48.63382%                                                           |                                                  776 |                               21728 |
| Louisiana            | 1.25460%                                                          | 12.54605%                                                          | 125.46050%                                                          |                                                 2083 |                               58324 |
| Maine                | 0.11040%                                                          | 1.10399%                                                           | 11.03993%                                                           |                                                   53 |                                1484 |
| Maryland             | 0.24917%                                                          | 2.49170%                                                           | 24.91697%                                                           |                                                  538 |                               15064 |
| Massachusetts        | 0.15153%                                                          | 1.51527%                                                           | 15.15270%                                                           |                                                  373 |                               10444 |
| Michigan             | 0.18252%                                                          | 1.82520%                                                           | 18.25199%                                                           |                                                  651 |                               18228 |
| Minnesota            | 0.28002%                                                          | 2.80018%                                                           | 28.00183%                                                           |                                                  564 |                               15792 |
| Mississippi          | 1.79131%                                                          | 17.91308%                                                          | 179.13082%                                                          |                                                 1904 |                               53312 |
| Missouri             | 0.35266%                                                          | 3.52656%                                                           | 35.26559%                                                           |                                                  773 |                               21644 |
| Montana              | 0.20435%                                                          | 2.04346%                                                           | 20.43455%                                                           |                                                   78 |                                2184 |
| Nebraska             | 0.36332%                                                          | 3.63315%                                                           | 36.33153%                                                           |                                                  251 |                                7028 |
| Nevada               | 0.99904%                                                          | 9.99040%                                                           | 99.90403%                                                           |                                                 1099 |                               30772 |
| New Hampshire        | 0.15033%                                                          | 1.50326%                                                           | 15.03261%                                                           |                                                   73 |                                2044 |
| New Jersey           | 0.13492%                                                          | 1.34922%                                                           | 13.49217%                                                           |                                                  428 |                               11984 |
| New Mexico           | 0.38325%                                                          | 3.83245%                                                           | 38.32454%                                                           |                                                  287 |                                8036 |
| New York             | 0.13213%                                                          | 1.32130%                                                           | 13.21301%                                                           |                                                  918 |                               25704 |
| North Carolina       | 0.56037%                                                          | 5.60369%                                                           | 56.03693%                                                           |                                                 2099 |                               58772 |
| North Dakota         | 0.26822%                                                          | 2.68220%                                                           | 26.82196%                                                           |                                                   73 |                                2044 |
| Ohio                 | 0.57298%                                                          | 5.72978%                                                           | 57.29782%                                                           |                                                 2392 |                               66976 |
| Oklahoma             | 0.60713%                                                          | 6.07131%                                                           | 60.71311%                                                           |                                                  858 |                               24024 |
| Oregon               | 0.42222%                                                          | 4.22217%                                                           | 42.22169%                                                           |                                                  636 |                               17808 |
| Pennsylvania         | 0.24627%                                                          | 2.46274%                                                           | 24.62742%                                                           |                                                 1126 |                               31528 |
| Rhode Island         | 0.18237%                                                          | 1.82374%                                                           | 18.23741%                                                           |                                                   69 |                                1932 |
| South Carolina       | 1.00825%                                                          | 10.08252%                                                          | 100.82518%                                                          |                                                 1854 |                               51912 |
| South Dakota         | 0.28802%                                                          | 2.88021%                                                           | 28.80206%                                                           |                                                   91 |                                2548 |
| Tennessee            | 1.01353%                                                          | 10.13534%                                                          | 101.35340%                                                          |                                                 2472 |                               69216 |
| Texas                | 0.96836%                                                          | 9.68358%                                                           | 96.83582%                                                           |                                                10028 |                              280784 |
| Utah                 | 0.63058%                                                          | 6.30576%                                                           | 63.05759%                                                           |                                                  722 |                               20216 |
| Vermont              | 0.07628%                                                          | 0.76283%                                                           | 7.62834%                                                            |                                                   17 |                                 476 |
| Virginia             | 0.23488%                                                          | 2.34877%                                                           | 23.48773%                                                           |                                                  716 |                               20048 |
| Washington           | 0.39969%                                                          | 3.99690%                                                           | 39.96904%                                                           |                                                 1087 |                               30436 |
| West Virginia        | 0.38434%                                                          | 3.84343%                                                           | 38.43435%                                                           |                                                  246 |                                6888 |
| Wisconsin            | 0.37318%                                                          | 3.73177%                                                           | 37.31773%                                                           |                                                  776 |                               21728 |
| Wyoming              | 0.37252%                                                          | 3.72521%                                                           | 37.25212%                                                           |                                                   77 |                                2156 |
| Puerto Rico          | 0.58653%                                                          | 5.86531%                                                           | 58.65308%                                                           |                                                  669 |                               18732 |
| District of Columbia | 0.28962%                                                          | 2.89621%                                                           | 28.96214%                                                           |                                                   73 |                                2044 |