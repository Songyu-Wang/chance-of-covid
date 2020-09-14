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

 Updated at: 2020-09-14T18:18:30.432904+00:00

| State                | Chance of encountering 1 person with COVID if you meet 1 person   | Chance of encountering 1 person with COVID if you meet 10 people   | Chance of encountering a person with COVID if you meet 100 people   |   Max count of new case increase in the past 14 days |   Estimated people count with COVID |
|:---------------------|:------------------------------------------------------------------|:-------------------------------------------------------------------|:--------------------------------------------------------------------|-----------------------------------------------------:|------------------------------------:|
| Alabama              | 0.88971%                                                          | 8.89707%                                                           | 88.97074%                                                           |                                                 1558 |                               43624 |
| Alaska               | 0.49758%                                                          | 4.97577%                                                           | 49.75770%                                                           |                                                  130 |                                3640 |
| Arizona              | 0.42007%                                                          | 4.20074%                                                           | 42.00740%                                                           |                                                 1092 |                               30576 |
| Arkansas             | 1.29154%                                                          | 12.91535%                                                          | 129.15352%                                                          |                                                 1392 |                               38976 |
| California           | 0.36318%                                                          | 3.63179%                                                           | 36.31788%                                                           |                                                 5125 |                              143500 |
| Colorado             | 0.20178%                                                          | 2.01780%                                                           | 20.17804%                                                           |                                                  415 |                               11620 |
| Connecticut          | 0.32749%                                                          | 3.27491%                                                           | 32.74912%                                                           |                                                  417 |                               11676 |
| Delaware             | 0.74761%                                                          | 7.47614%                                                           | 74.76144%                                                           |                                                  260 |                                7280 |
| Florida              | 0.98675%                                                          | 9.86752%                                                           | 98.67520%                                                           |                                                 7569 |                              211932 |
| Georgia              | 0.70544%                                                          | 7.05444%                                                           | 70.54442%                                                           |                                                 2675 |                               74900 |
| Hawaii               | 0.66842%                                                          | 6.68422%                                                           | 66.84220%                                                           |                                                  338 |                                9464 |
| Idaho                | 0.52175%                                                          | 5.21749%                                                           | 52.17493%                                                           |                                                  333 |                                9324 |
| Illinois             | 1.23607%                                                          | 12.36065%                                                          | 123.60654%                                                          |                                                 5594 |                              156632 |
| Indiana              | 0.52488%                                                          | 5.24879%                                                           | 52.48789%                                                           |                                                 1262 |                               35336 |
| Iowa                 | 0.96822%                                                          | 9.68219%                                                           | 96.82194%                                                           |                                                 1091 |                               30548 |
| Kansas               | 1.62811%                                                          | 16.28111%                                                          | 162.81115%                                                          |                                                 1694 |                               47432 |
| Kentucky             | 0.58411%                                                          | 5.84107%                                                           | 58.41072%                                                           |                                                  932 |                               26096 |
| Louisiana            | 0.94020%                                                          | 9.40201%                                                           | 94.02008%                                                           |                                                 1561 |                               43708 |
| Maine                | 0.10415%                                                          | 1.04150%                                                           | 10.41502%                                                           |                                                   50 |                                1400 |
| Maryland             | 0.37931%                                                          | 3.79312%                                                           | 37.93122%                                                           |                                                  819 |                               22932 |
| Massachusetts        | 0.22506%                                                          | 2.25056%                                                           | 22.50561%                                                           |                                                  554 |                               15512 |
| Michigan             | 0.39392%                                                          | 3.93918%                                                           | 39.39177%                                                           |                                                 1405 |                               39340 |
| Minnesota            | 0.51535%                                                          | 5.15353%                                                           | 51.53528%                                                           |                                                 1038 |                               29064 |
| Mississippi          | 0.80251%                                                          | 8.02514%                                                           | 80.25136%                                                           |                                                  853 |                               23884 |
| Missouri             | 0.90650%                                                          | 9.06504%                                                           | 90.65035%                                                           |                                                 1987 |                               55636 |
| Montana              | 0.51086%                                                          | 5.10864%                                                           | 51.08638%                                                           |                                                  195 |                                5460 |
| Nebraska             | 0.72663%                                                          | 7.26631%                                                           | 72.66306%                                                           |                                                  502 |                               14056 |
| Nevada               | 0.46179%                                                          | 4.61795%                                                           | 46.17948%                                                           |                                                  508 |                               14224 |
| New Hampshire        | 0.16268%                                                          | 1.62682%                                                           | 16.26816%                                                           |                                                   79 |                                2212 |
| New Jersey           | 0.14942%                                                          | 1.49423%                                                           | 14.94226%                                                           |                                                  474 |                               13272 |
| New Mexico           | 0.26707%                                                          | 2.67070%                                                           | 26.70699%                                                           |                                                  200 |                                5600 |
| New York             | 0.12796%                                                          | 1.27956%                                                           | 12.79560%                                                           |                                                  889 |                               24892 |
| North Carolina       | 0.56357%                                                          | 5.63573%                                                           | 56.35729%                                                           |                                                 2111 |                               59108 |
| North Dakota         | 1.71587%                                                          | 17.15871%                                                          | 171.58709%                                                          |                                                  467 |                               13076 |
| Ohio                 | 0.34805%                                                          | 3.48051%                                                           | 34.80507%                                                           |                                                 1453 |                               40684 |
| Oklahoma             | 0.81163%                                                          | 8.11631%                                                           | 81.16309%                                                           |                                                 1147 |                               32116 |
| Oregon               | 0.19318%                                                          | 1.93184%                                                           | 19.31842%                                                           |                                                  291 |                                8148 |
| Pennsylvania         | 0.25371%                                                          | 2.53711%                                                           | 25.37106%                                                           |                                                 1160 |                               32480 |
| Rhode Island         | 0.63699%                                                          | 6.36988%                                                           | 63.69878%                                                           |                                                  241 |                                6748 |
| South Carolina       | 1.33455%                                                          | 13.34547%                                                          | 133.45468%                                                          |                                                 2454 |                               68712 |
| South Dakota         | 1.05713%                                                          | 10.57130%                                                          | 105.71305%                                                          |                                                  334 |                                9352 |
| Tennessee            | 0.74539%                                                          | 7.45390%                                                           | 74.53903%                                                           |                                                 1818 |                               50904 |
| Texas                | 0.52937%                                                          | 5.29372%                                                           | 52.93717%                                                           |                                                 5482 |                              153496 |
| Utah                 | 0.57293%                                                          | 5.72933%                                                           | 57.29333%                                                           |                                                  656 |                               18368 |
| Vermont              | 0.04936%                                                          | 0.49360%                                                           | 4.93598%                                                            |                                                   11 |                                 308 |
| Virginia             | 0.42645%                                                          | 4.26453%                                                           | 42.64533%                                                           |                                                 1300 |                               36400 |
| Washington           | 0.29968%                                                          | 2.99676%                                                           | 29.96759%                                                           |                                                  815 |                               22820 |
| West Virginia        | 0.54214%                                                          | 5.42143%                                                           | 54.21430%                                                           |                                                  347 |                                9716 |
| Wisconsin            | 0.78098%                                                          | 7.80979%                                                           | 78.09792%                                                           |                                                 1624 |                               45472 |
| Wyoming              | 0.34349%                                                          | 3.43494%                                                           | 34.34936%                                                           |                                                   71 |                                1988 |
| Puerto Rico          | 0.73820%                                                          | 7.38205%                                                           | 73.82047%                                                           |                                                  842 |                               23576 |
| District of Columbia | 0.32136%                                                          | 3.21361%                                                           | 32.13607%                                                           |                                                   81 |                                2268 |