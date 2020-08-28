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

 Updated at: 2020-08-28T00:46:45.986820+00:00

| State                | Chance of encountering 1 person with COVID if you meet 1 person   | Chance of encountering 1 person with COVID if you meet 10 people   | Chance of encountering a person with COVID if you meet 100 people   |   Max count of new case increase in the past 14 days |   Estimated people count with COVID |
|:---------------------|:------------------------------------------------------------------|:-------------------------------------------------------------------|:--------------------------------------------------------------------|-----------------------------------------------------:|------------------------------------:|
| Alabama              | 1.14897%                                                          | 11.48967%                                                          | 114.89675%                                                          |                                                 2012 |                               56336 |
| Alaska               | 0.45547%                                                          | 4.55474%                                                           | 45.54744%                                                           |                                                  119 |                                3332 |
| Arizona              | 0.38314%                                                          | 3.83144%                                                           | 38.31444%                                                           |                                                  996 |                               27888 |
| Arkansas             | 0.82298%                                                          | 8.22983%                                                           | 82.29825%                                                           |                                                  887 |                               24836 |
| California           | 0.89388%                                                          | 8.93880%                                                           | 89.38804%                                                           |                                                12614 |                              353192 |
| Colorado             | 0.22512%                                                          | 2.25119%                                                           | 22.51188%                                                           |                                                  463 |                               12964 |
| Connecticut          | 0.38639%                                                          | 3.86392%                                                           | 38.63925%                                                           |                                                  492 |                               13776 |
| Delaware             | 1.07254%                                                          | 10.72539%                                                          | 107.25391%                                                          |                                                  373 |                               10444 |
| Florida              | 0.82809%                                                          | 8.28095%                                                           | 82.80947%                                                           |                                                 6352 |                              177856 |
| Georgia              | 0.86315%                                                          | 8.63147%                                                           | 86.31473%                                                           |                                                 3273 |                               91644 |
| Hawaii               | 0.77917%                                                          | 7.79166%                                                           | 77.91665%                                                           |                                                  394 |                               11032 |
| Idaho                | 0.84921%                                                          | 8.49214%                                                           | 84.92137%                                                           |                                                  542 |                               15176 |
| Illinois             | 0.52059%                                                          | 5.20588%                                                           | 52.05882%                                                           |                                                 2356 |                               65968 |
| Indiana              | 0.69041%                                                          | 6.90411%                                                           | 69.04113%                                                           |                                                 1660 |                               46480 |
| Iowa                 | 1.37645%                                                          | 13.76451%                                                          | 137.64512%                                                          |                                                 1551 |                               43428 |
| Kansas               | 1.48491%                                                          | 14.84907%                                                          | 148.49069%                                                          |                                                 1545 |                               43260 |
| Kentucky             | 0.79218%                                                          | 7.92180%                                                           | 79.21797%                                                           |                                                 1264 |                               35392 |
| Louisiana            | 0.78179%                                                          | 7.81794%                                                           | 78.17942%                                                           |                                                 1298 |                               36344 |
| Maine                | 0.06666%                                                          | 0.66656%                                                           | 6.66562%                                                            |                                                   32 |                                 896 |
| Maryland             | 0.37885%                                                          | 3.78849%                                                           | 37.88490%                                                           |                                                  818 |                               22904 |
| Massachusetts        | 0.33596%                                                          | 3.35959%                                                           | 33.59592%                                                           |                                                  827 |                               23156 |
| Michigan             | 0.39981%                                                          | 3.99805%                                                           | 39.98055%                                                           |                                                 1426 |                               39928 |
| Minnesota            | 0.57295%                                                          | 5.72945%                                                           | 57.29452%                                                           |                                                 1154 |                               32312 |
| Mississippi          | 1.26822%                                                          | 12.68216%                                                          | 126.82161%                                                          |                                                 1348 |                               37744 |
| Missouri             | 0.68980%                                                          | 6.89800%                                                           | 68.98004%                                                           |                                                 1512 |                               42336 |
| Montana              | 0.42179%                                                          | 4.21790%                                                           | 42.17901%                                                           |                                                  161 |                                4508 |
| Nebraska             | 0.60215%                                                          | 6.02148%                                                           | 60.21480%                                                           |                                                  416 |                               11648 |
| Nevada               | 0.99904%                                                          | 9.99040%                                                           | 99.90403%                                                           |                                                 1099 |                               30772 |
| New Hampshire        | 0.12150%                                                          | 1.21496%                                                           | 12.14964%                                                           |                                                   59 |                                1652 |
| New Jersey           | 0.17969%                                                          | 1.79685%                                                           | 17.96854%                                                           |                                                  570 |                               15960 |
| New Mexico           | 0.27642%                                                          | 2.76417%                                                           | 27.64174%                                                           |                                                  207 |                                5796 |
| New York             | 0.11385%                                                          | 1.13851%                                                           | 11.38506%                                                           |                                                  791 |                               22148 |
| North Carolina       | 0.55823%                                                          | 5.58234%                                                           | 55.82335%                                                           |                                                 2091 |                               58548 |
| North Dakota         | 1.22352%                                                          | 12.23522%                                                          | 122.35225%                                                          |                                                  333 |                                9324 |
| Ohio                 | 0.29799%                                                          | 2.97987%                                                           | 29.79870%                                                           |                                                 1244 |                               34832 |
| Oklahoma             | 0.76210%                                                          | 7.62098%                                                           | 76.20981%                                                           |                                                 1077 |                               30156 |
| Oregon               | 0.26886%                                                          | 2.68865%                                                           | 26.88646%                                                           |                                                  405 |                               11340 |
| Pennsylvania         | 0.18591%                                                          | 1.85909%                                                           | 18.59086%                                                           |                                                  850 |                               23800 |
| Rhode Island         | 0.40439%                                                          | 4.04395%                                                           | 40.43947%                                                           |                                                  153 |                                4284 |
| South Carolina       | 0.57537%                                                          | 5.75367%                                                           | 57.53670%                                                           |                                                 1058 |                               29624 |
| South Dakota         | 1.97183%                                                          | 19.71833%                                                          | 197.18332%                                                          |                                                  623 |                               17444 |
| Tennessee            | 0.82903%                                                          | 8.29031%                                                           | 82.90314%                                                           |                                                 2022 |                               56616 |
| Texas                | 0.79618%                                                          | 7.96182%                                                           | 79.61821%                                                           |                                                 8245 |                              230860 |
| Utah                 | 0.48210%                                                          | 4.82102%                                                           | 48.21024%                                                           |                                                  552 |                               15456 |
| Vermont              | 0.07628%                                                          | 0.76283%                                                           | 7.62834%                                                            |                                                   17 |                                 476 |
| Virginia             | 0.39890%                                                          | 3.98898%                                                           | 39.88978%                                                           |                                                 1216 |                               34048 |
| Washington           | 0.23533%                                                          | 2.35328%                                                           | 23.53283%                                                           |                                                  640 |                               17920 |
| West Virginia        | 0.28591%                                                          | 2.85914%                                                           | 28.59140%                                                           |                                                  183 |                                5124 |
| Wisconsin            | 0.50927%                                                          | 5.09272%                                                           | 50.92716%                                                           |                                                 1059 |                               29652 |
| Wyoming              | 0.32414%                                                          | 3.24142%                                                           | 32.41418%                                                           |                                                   67 |                                1876 |
| Puerto Rico          | 0.83552%                                                          | 8.35521%                                                           | 83.55215%                                                           |                                                  953 |                               26684 |
| District of Columbia | 0.37294%                                                          | 3.72937%                                                           | 37.29371%                                                           |                                                   94 |                                2632 |