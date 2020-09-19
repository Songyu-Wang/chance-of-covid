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

 Updated at: 2020-09-19T06:19:19.037658+00:00

| State                | Chance of encountering 1 person with COVID if you meet 1 person   | Chance of encountering 1 person with COVID if you meet 10 people   | Chance of encountering a person with COVID if you meet 100 people   |   Max count of new case increase in the past 14 days |   Estimated people count with COVID |
|:---------------------|:------------------------------------------------------------------|:-------------------------------------------------------------------|:--------------------------------------------------------------------|-----------------------------------------------------:|------------------------------------:|
| Alabama              | 0.80519%                                                          | 8.05191%                                                           | 80.51909%                                                           |                                                 1410 |                               39480 |
| Alaska               | 0.47844%                                                          | 4.78439%                                                           | 47.84395%                                                           |                                                  125 |                                3500 |
| Arizona              | 0.67435%                                                          | 6.74350%                                                           | 67.43496%                                                           |                                                 1753 |                               49084 |
| Arkansas             | 1.09484%                                                          | 10.94836%                                                          | 109.48358%                                                          |                                                 1180 |                               33040 |
| California           | 0.35120%                                                          | 3.51203%                                                           | 35.12027%                                                           |                                                 4956 |                              138768 |
| Colorado             | 0.28541%                                                          | 2.85410%                                                           | 28.54099%                                                           |                                                  587 |                               16436 |
| Connecticut          | 0.44686%                                                          | 4.46864%                                                           | 44.68644%                                                           |                                                  569 |                               15932 |
| Delaware             | 0.74761%                                                          | 7.47614%                                                           | 74.76144%                                                           |                                                  260 |                                7280 |
| Florida              | 0.47662%                                                          | 4.76624%                                                           | 47.66238%                                                           |                                                 3656 |                              102368 |
| Georgia              | 0.58624%                                                          | 5.86244%                                                           | 58.62440%                                                           |                                                 2223 |                               62244 |
| Hawaii               | 0.53592%                                                          | 5.35924%                                                           | 53.59242%                                                           |                                                  271 |                                7588 |
| Idaho                | 0.62046%                                                          | 6.20459%                                                           | 62.04587%                                                           |                                                  396 |                               11088 |
| Illinois             | 0.62002%                                                          | 6.20021%                                                           | 62.00214%                                                           |                                                 2806 |                               78568 |
| Indiana              | 0.52488%                                                          | 5.24879%                                                           | 52.48789%                                                           |                                                 1262 |                               35336 |
| Iowa                 | 1.04987%                                                          | 10.49866%                                                          | 104.98658%                                                          |                                                 1183 |                               33124 |
| Kansas               | 1.62811%                                                          | 16.28111%                                                          | 162.81115%                                                          |                                                 1694 |                               47432 |
| Kentucky             | 0.58411%                                                          | 5.84107%                                                           | 58.41072%                                                           |                                                  932 |                               26096 |
| Louisiana            | 0.94020%                                                          | 9.40201%                                                           | 94.02008%                                                           |                                                 1561 |                               43708 |
| Maine                | 0.08957%                                                          | 0.89569%                                                           | 8.95692%                                                            |                                                   43 |                                1204 |
| Maryland             | 0.37468%                                                          | 3.74681%                                                           | 37.46808%                                                           |                                                  809 |                               22652 |
| Massachusetts        | 0.22506%                                                          | 2.25056%                                                           | 22.50561%                                                           |                                                  554 |                               15512 |
| Michigan             | 0.39392%                                                          | 3.93918%                                                           | 39.39177%                                                           |                                                 1405 |                               39340 |
| Minnesota            | 0.53869%                                                          | 5.38688%                                                           | 53.86876%                                                           |                                                 1085 |                               30380 |
| Mississippi          | 0.80251%                                                          | 8.02514%                                                           | 80.25136%                                                           |                                                  853 |                               23884 |
| Missouri             | 0.90650%                                                          | 9.06504%                                                           | 90.65035%                                                           |                                                 1987 |                               55636 |
| Montana              | 0.58684%                                                          | 5.86838%                                                           | 58.68384%                                                           |                                                  224 |                                6272 |
| Nebraska             | 0.72663%                                                          | 7.26631%                                                           | 72.66306%                                                           |                                                  502 |                               14056 |
| Nevada               | 0.46179%                                                          | 4.61795%                                                           | 46.17948%                                                           |                                                  508 |                               14224 |
| New Hampshire        | 0.16268%                                                          | 1.62682%                                                           | 16.26816%                                                           |                                                   79 |                                2212 |
| New Jersey           | 0.17937%                                                          | 1.79370%                                                           | 17.93702%                                                           |                                                  569 |                               15932 |
| New Mexico           | 0.21499%                                                          | 2.14991%                                                           | 21.49913%                                                           |                                                  161 |                                4508 |
| New York             | 0.12896%                                                          | 1.28964%                                                           | 12.89635%                                                           |                                                  896 |                               25088 |
| North Carolina       | 0.41674%                                                          | 4.16740%                                                           | 41.67396%                                                           |                                                 1561 |                               43708 |
| North Dakota         | 1.86284%                                                          | 18.62841%                                                          | 186.28406%                                                          |                                                  507 |                               14196 |
| Ohio                 | 0.32122%                                                          | 3.21222%                                                           | 32.12223%                                                           |                                                 1341 |                               37548 |
| Oklahoma             | 0.88381%                                                          | 8.83807%                                                           | 88.38073%                                                           |                                                 1249 |                               34972 |
| Oregon               | 0.32662%                                                          | 3.26621%                                                           | 32.66206%                                                           |                                                  492 |                               13776 |
| Pennsylvania         | 0.25852%                                                          | 2.58522%                                                           | 25.85223%                                                           |                                                 1182 |                               33096 |
| Rhode Island         | 0.63699%                                                          | 6.36988%                                                           | 63.69878%                                                           |                                                  241 |                                6748 |
| South Carolina       | 1.33455%                                                          | 13.34547%                                                          | 133.45468%                                                          |                                                 2454 |                               68712 |
| South Dakota         | 1.25020%                                                          | 12.50199%                                                          | 125.01992%                                                          |                                                  395 |                               11060 |
| Tennessee            | 1.00451%                                                          | 10.04514%                                                          | 100.45139%                                                          |                                                 2450 |                               68600 |
| Texas                | 0.58190%                                                          | 5.81903%                                                           | 58.19033%                                                           |                                                 6026 |                              168728 |
| Utah                 | 0.97556%                                                          | 9.75559%                                                           | 97.55586%                                                           |                                                 1117 |                               31276 |
| Vermont              | 0.05385%                                                          | 0.53847%                                                           | 5.38471%                                                            |                                                   12 |                                 336 |
| Virginia             | 0.42645%                                                          | 4.26453%                                                           | 42.64533%                                                           |                                                 1300 |                               36400 |
| Washington           | 0.28460%                                                          | 2.84600%                                                           | 28.46002%                                                           |                                                  774 |                               21672 |
| West Virginia        | 0.54214%                                                          | 5.42143%                                                           | 54.21430%                                                           |                                                  347 |                                9716 |
| Wisconsin            | 1.24072%                                                          | 12.40718%                                                          | 124.07182%                                                          |                                                 2580 |                               72240 |
| Wyoming              | 0.61926%                                                          | 6.19256%                                                           | 61.92560%                                                           |                                                  128 |                                3584 |
| Puerto Rico          | 0.73820%                                                          | 7.38205%                                                           | 73.82047%                                                           |                                                  842 |                               23576 |
| District of Columbia | 0.32136%                                                          | 3.21361%                                                           | 32.13607%                                                           |                                                   81 |                                2268 |