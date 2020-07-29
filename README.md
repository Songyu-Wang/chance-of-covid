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

 Updated at: 2020-07-29T12:16:48.816677+00:00

| State                | Chance of encountering 1 person with COVID if you meet 1 person   | Chance of encountering 1 person with COVID if you meet 10 people   | Chance of encountering a person with COVID if you meet 100 people   |   Max count of new case increase in the past 14 days |   Estimated people count with COVID |
|:---------------------|:------------------------------------------------------------------|:-------------------------------------------------------------------|:--------------------------------------------------------------------|-----------------------------------------------------:|------------------------------------:|
| Alabama              | 1.36997%                                                          | 13.69967%                                                          | 136.99667%                                                          |                                                 2399 |                               67172 |
| Alaska               | 1.53483%                                                          | 15.34834%                                                          | 153.48338%                                                          |                                                  401 |                               11228 |
| Arizona              | 1.50411%                                                          | 15.04111%                                                          | 150.41112%                                                          |                                                 3910 |                              109480 |
| Arkansas             | 1.29339%                                                          | 12.93391%                                                          | 129.33908%                                                          |                                                 1394 |                               39032 |
| California           | 0.90756%                                                          | 9.07557%                                                           | 90.75571%                                                           |                                                12807 |                              358596 |
| Colorado             | 0.39335%                                                          | 3.93350%                                                           | 39.33502%                                                           |                                                  809 |                               22652 |
| Connecticut          | 0.42723%                                                          | 4.27231%                                                           | 42.72307%                                                           |                                                  544 |                               15232 |
| Delaware             | 0.79937%                                                          | 7.99372%                                                           | 79.93723%                                                           |                                                  278 |                                7784 |
| Florida              | 1.82058%                                                          | 18.20583%                                                          | 182.05829%                                                          |                                                13965 |                              391020 |
| Georgia              | 1.26927%                                                          | 12.69272%                                                          | 126.92722%                                                          |                                                 4813 |                              134764 |
| Hawaii               | 0.14041%                                                          | 1.40408%                                                           | 14.04082%                                                           |                                                   71 |                                1988 |
| Idaho                | 1.13907%                                                          | 11.39074%                                                          | 113.90744%                                                          |                                                  727 |                               20356 |
| Illinois             | 0.35884%                                                          | 3.58843%                                                           | 35.88435%                                                           |                                                 1624 |                               45472 |
| Indiana              | 0.41425%                                                          | 4.14247%                                                           | 41.42468%                                                           |                                                  996 |                               27888 |
| Iowa                 | 0.74635%                                                          | 7.46354%                                                           | 74.63543%                                                           |                                                  841 |                               23548 |
| Kansas               | 1.31575%                                                          | 13.15752%                                                          | 131.57524%                                                          |                                                 1369 |                               38332 |
| Kentucky             | 0.61231%                                                          | 6.12310%                                                           | 61.23098%                                                           |                                                  977 |                               27356 |
| Louisiana            | 2.31286%                                                          | 23.12858%                                                          | 231.28579%                                                          |                                                 3840 |                              107520 |
| Maine                | 0.08540%                                                          | 0.85403%                                                           | 8.54032%                                                            |                                                   41 |                                1148 |
| Maryland             | 0.59653%                                                          | 5.96525%                                                           | 59.65251%                                                           |                                                 1288 |                               36064 |
| Massachusetts        | 0.25227%                                                          | 2.52274%                                                           | 25.22741%                                                           |                                                  621 |                               17388 |
| Michigan             | 0.44551%                                                          | 4.45506%                                                           | 44.55055%                                                           |                                                 1589 |                               44492 |
| Minnesota            | 0.44833%                                                          | 4.48327%                                                           | 44.83271%                                                           |                                                  903 |                               25284 |
| Mississippi          | 1.53823%                                                          | 15.38229%                                                          | 153.82294%                                                          |                                                 1635 |                               45780 |
| Missouri             | 0.75367%                                                          | 7.53671%                                                           | 75.36708%                                                           |                                                 1652 |                               46256 |
| Montana              | 0.57898%                                                          | 5.78979%                                                           | 57.89790%                                                           |                                                  221 |                                6188 |
| Nebraska             | 0.51530%                                                          | 5.15300%                                                           | 51.52998%                                                           |                                                  356 |                                9968 |
| Nevada               | 1.31539%                                                          | 13.15388%                                                          | 131.53879%                                                          |                                                 1447 |                               40516 |
| New Hampshire        | 0.19975%                                                          | 1.99748%                                                           | 19.97483%                                                           |                                                   97 |                                2716 |
| New Jersey           | 0.16172%                                                          | 1.61717%                                                           | 16.17169%                                                           |                                                  513 |                               14364 |
| New Mexico           | 0.61426%                                                          | 6.14261%                                                           | 61.42609%                                                           |                                                  460 |                               12880 |
| New York             | 0.12306%                                                          | 1.23062%                                                           | 12.30623%                                                           |                                                  855 |                               23940 |
| North Carolina       | 0.66235%                                                          | 6.62352%                                                           | 66.23517%                                                           |                                                 2481 |                               69468 |
| North Dakota         | 0.58788%                                                          | 5.87879%                                                           | 58.78787%                                                           |                                                  160 |                                4480 |
| Ohio                 | 0.40219%                                                          | 4.02187%                                                           | 40.21867%                                                           |                                                 1679 |                               47012 |
| Oklahoma             | 0.99136%                                                          | 9.91364%                                                           | 99.13644%                                                           |                                                 1401 |                               39228 |
| Oregon               | 0.28546%                                                          | 2.85461%                                                           | 28.54611%                                                           |                                                  430 |                               12040 |
| Pennsylvania         | 0.26530%                                                          | 2.65303%                                                           | 26.53025%                                                           |                                                 1213 |                               33964 |
| Rhode Island         | 0.76914%                                                          | 7.69143%                                                           | 76.91429%                                                           |                                                  291 |                                8148 |
| South Carolina       | 1.29104%                                                          | 12.91041%                                                          | 129.10408%                                                          |                                                 2374 |                               66472 |
| South Dakota         | 0.33233%                                                          | 3.32331%                                                           | 33.23314%                                                           |                                                  105 |                                2940 |
| Tennessee            | 1.28742%                                                          | 12.87418%                                                          | 128.74178%                                                          |                                                 3140 |                               87920 |
| Texas                | 1.44037%                                                          | 14.40370%                                                          | 144.03701%                                                          |                                                14916 |                              417648 |
| Utah                 | 0.83320%                                                          | 8.33199%                                                           | 83.31987%                                                           |                                                  954 |                               26712 |
| Vermont              | 0.05833%                                                          | 0.58334%                                                           | 5.83344%                                                            |                                                   13 |                                 364 |
| Virginia             | 0.49370%                                                          | 4.93702%                                                           | 49.37017%                                                           |                                                 1505 |                               42140 |
| Washington           | 0.46588%                                                          | 4.65877%                                                           | 46.58765%                                                           |                                                 1267 |                               35476 |
| West Virginia        | 0.53746%                                                          | 5.37456%                                                           | 53.74559%                                                           |                                                  344 |                                9632 |
| Wisconsin            | 0.55832%                                                          | 5.58323%                                                           | 55.83232%                                                           |                                                 1161 |                               32508 |
| Wyoming              | 0.33382%                                                          | 3.33818%                                                           | 33.38177%                                                           |                                                   69 |                                1932 |
| Puerto Rico          | 0.53480%                                                          | 5.34804%                                                           | 53.48039%                                                           |                                                  610 |                               17080 |
| District of Columbia | 0.40468%                                                          | 4.04676%                                                           | 40.46765%                                                           |                                                  102 |                                2856 |