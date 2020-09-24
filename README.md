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

 Updated at: 2020-09-24T12:23:05.036726+00:00

| State                | Chance of encountering 1 person with COVID if you meet 1 person   | Chance of encountering 1 person with COVID if you meet 10 people   | Chance of encountering a person with COVID if you meet 100 people   |   Max count of new case increase in the past 14 days |   Estimated people count with COVID |
|:---------------------|:------------------------------------------------------------------|:-------------------------------------------------------------------|:--------------------------------------------------------------------|-----------------------------------------------------:|------------------------------------:|
| Alabama              | 0.74295%                                                          | 7.42946%                                                           | 74.29457%                                                           |                                                 1301 |                               36428 |
| Alaska               | 0.47844%                                                          | 4.78439%                                                           | 47.84395%                                                           |                                                  125 |                                3500 |
| Arizona              | 0.67435%                                                          | 6.74350%                                                           | 67.43496%                                                           |                                                 1753 |                               49084 |
| Arkansas             | 1.09484%                                                          | 10.94836%                                                          | 109.48358%                                                          |                                                 1180 |                               33040 |
| California           | 0.32775%                                                          | 3.27747%                                                           | 32.77467%                                                           |                                                 4625 |                              129500 |
| Colorado             | 0.31799%                                                          | 3.17986%                                                           | 31.79864%                                                           |                                                  654 |                               18312 |
| Connecticut          | 0.44686%                                                          | 4.46864%                                                           | 44.68644%                                                           |                                                  569 |                               15932 |
| Delaware             | 0.74761%                                                          | 7.47614%                                                           | 74.76144%                                                           |                                                  260 |                                7280 |
| Florida              | 0.47584%                                                          | 4.75842%                                                           | 47.58416%                                                           |                                                 3650 |                              102200 |
| Georgia              | 0.60233%                                                          | 6.02331%                                                           | 60.23307%                                                           |                                                 2284 |                               63952 |
| Hawaii               | 0.33421%                                                          | 3.34211%                                                           | 33.42110%                                                           |                                                  169 |                                4732 |
| Idaho                | 0.73640%                                                          | 7.36403%                                                           | 73.64030%                                                           |                                                  470 |                               13160 |
| Illinois             | 0.55881%                                                          | 5.58815%                                                           | 55.88147%                                                           |                                                 2529 |                               70812 |
| Indiana              | 0.52488%                                                          | 5.24879%                                                           | 52.48789%                                                           |                                                 1262 |                               35336 |
| Iowa                 | 1.04987%                                                          | 10.49866%                                                          | 104.98658%                                                          |                                                 1183 |                               33124 |
| Kansas               | 1.60889%                                                          | 16.08889%                                                          | 160.88894%                                                          |                                                 1674 |                               46872 |
| Kentucky             | 0.61294%                                                          | 6.12937%                                                           | 61.29365%                                                           |                                                  978 |                               27384 |
| Louisiana            | 0.77155%                                                          | 7.71555%                                                           | 77.15549%                                                           |                                                 1281 |                               35868 |
| Maine                | 0.09165%                                                          | 0.91652%                                                           | 9.16522%                                                            |                                                   44 |                                1232 |
| Maryland             | 0.37468%                                                          | 3.74681%                                                           | 37.46808%                                                           |                                                  809 |                               22652 |
| Massachusetts        | 0.24334%                                                          | 2.43337%                                                           | 24.33369%                                                           |                                                  599 |                               16772 |
| Michigan             | 0.44158%                                                          | 4.41580%                                                           | 44.15804%                                                           |                                                 1575 |                               44100 |
| Minnesota            | 0.64345%                                                          | 6.43446%                                                           | 64.34462%                                                           |                                                 1296 |                               36288 |
| Mississippi          | 1.08382%                                                          | 10.83817%                                                          | 108.38167%                                                          |                                                 1152 |                               32256 |
| Missouri             | 0.90057%                                                          | 9.00573%                                                           | 90.05727%                                                           |                                                 1974 |                               55272 |
| Montana              | 0.76499%                                                          | 7.64986%                                                           | 76.49858%                                                           |                                                  292 |                                8176 |
| Nebraska             | 0.72663%                                                          | 7.26631%                                                           | 72.66306%                                                           |                                                  502 |                               14056 |
| Nevada               | 0.46270%                                                          | 4.62704%                                                           | 46.27038%                                                           |                                                  509 |                               14252 |
| New Hampshire        | 0.16268%                                                          | 1.62682%                                                           | 16.26816%                                                           |                                                   79 |                                2212 |
| New Jersey           | 0.17937%                                                          | 1.79370%                                                           | 17.93702%                                                           |                                                  569 |                               15932 |
| New Mexico           | 0.21633%                                                          | 2.16327%                                                           | 21.63267%                                                           |                                                  162 |                                4536 |
| New York             | 0.14192%                                                          | 1.41917%                                                           | 14.19175%                                                           |                                                  986 |                               27608 |
| North Carolina       | 0.41434%                                                          | 4.14337%                                                           | 41.43369%                                                           |                                                 1552 |                               43456 |
| North Dakota         | 1.86284%                                                          | 18.62841%                                                          | 186.28406%                                                          |                                                  507 |                               14196 |
| Ohio                 | 0.29751%                                                          | 2.97508%                                                           | 29.75079%                                                           |                                                 1242 |                               34776 |
| Oklahoma             | 0.88381%                                                          | 8.83807%                                                           | 88.38073%                                                           |                                                 1249 |                               34972 |
| Oregon               | 0.32662%                                                          | 3.26621%                                                           | 32.66206%                                                           |                                                  492 |                               13776 |
| Pennsylvania         | 0.25852%                                                          | 2.58522%                                                           | 25.85223%                                                           |                                                 1182 |                               33096 |
| Rhode Island         | 0.47047%                                                          | 4.70472%                                                           | 47.04723%                                                           |                                                  178 |                                4984 |
| South Carolina       | 1.44929%                                                          | 14.49294%                                                          | 144.92939%                                                          |                                                 2665 |                               74620 |
| South Dakota         | 1.40845%                                                          | 14.08452%                                                          | 140.84523%                                                          |                                                  445 |                               12460 |
| Tennessee            | 1.00451%                                                          | 10.04514%                                                          | 100.45139%                                                          |                                                 2450 |                               68600 |
| Texas                | 1.72080%                                                          | 17.20796%                                                          | 172.07961%                                                          |                                                17820 |                              498960 |
| Utah                 | 0.97556%                                                          | 9.75559%                                                           | 97.55586%                                                           |                                                 1117 |                               31276 |
| Vermont              | 0.05385%                                                          | 0.53847%                                                           | 5.38471%                                                            |                                                   12 |                                 336 |
| Virginia             | 0.42645%                                                          | 4.26453%                                                           | 42.64533%                                                           |                                                 1300 |                               36400 |
| Washington           | 0.23717%                                                          | 2.37167%                                                           | 23.71668%                                                           |                                                  645 |                               18060 |
| West Virginia        | 0.54214%                                                          | 5.42143%                                                           | 54.21430%                                                           |                                                  347 |                                9716 |
| Wisconsin            | 1.24072%                                                          | 12.40718%                                                          | 124.07182%                                                          |                                                 2580 |                               72240 |
| Wyoming              | 0.74020%                                                          | 7.40204%                                                           | 74.02045%                                                           |                                                  153 |                                4284 |
| Puerto Rico          | 1.14764%                                                          | 11.47637%                                                          | 114.76366%                                                          |                                                 1309 |                               36652 |
| District of Columbia | 0.32136%                                                          | 3.21361%                                                           | 32.13607%                                                           |                                                   81 |                                2268 |