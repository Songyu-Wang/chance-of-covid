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

 Updated at: 2020-10-04T18:19:31.411075+00:00

| State                | Chance of encountering 1 person with COVID if you meet 1 person   | Chance of encountering 1 person with COVID if you meet 10 people   | Chance of encountering a person with COVID if you meet 100 people   |   Max count of new case increase in the past 14 days |   Estimated people count with COVID |
|:---------------------|:------------------------------------------------------------------|:-------------------------------------------------------------------|:--------------------------------------------------------------------|-----------------------------------------------------:|------------------------------------:|
| Alabama              | 1.40023%                                                          | 14.00233%                                                          | 140.02327%                                                          |                                                 2452 |                               68656 |
| Alaska               | 0.99898%                                                          | 9.98982%                                                           | 99.89816%                                                           |                                                  261 |                                7308 |
| Arizona              | 0.27120%                                                          | 2.71202%                                                           | 27.12016%                                                           |                                                  705 |                               19740 |
| Arkansas             | 1.04288%                                                          | 10.42878%                                                          | 104.28775%                                                          |                                                 1124 |                               31472 |
| California           | 0.30224%                                                          | 3.02236%                                                           | 30.22356%                                                           |                                                 4265 |                              119420 |
| Colorado             | 0.34473%                                                          | 3.44728%                                                           | 34.47284%                                                           |                                                  709 |                               19852 |
| Connecticut          | 0.43980%                                                          | 4.39796%                                                           | 43.97963%                                                           |                                                  560 |                               15680 |
| Delaware             | 0.54058%                                                          | 5.40583%                                                           | 54.05827%                                                           |                                                  188 |                                5264 |
| Florida              | 0.42578%                                                          | 4.25780%                                                           | 42.57804%                                                           |                                                 3266 |                               91448 |
| Georgia              | 0.45359%                                                          | 4.53594%                                                           | 45.35941%                                                           |                                                 1720 |                               48160 |
| Hawaii               | 0.33026%                                                          | 3.30256%                                                           | 33.02558%                                                           |                                                  167 |                                4676 |
| Idaho                | 1.06073%                                                          | 10.60734%                                                          | 106.07337%                                                          |                                                  677 |                               18956 |
| Illinois             | 0.61980%                                                          | 6.19800%                                                           | 61.98004%                                                           |                                                 2805 |                               78540 |
| Indiana              | 0.60889%                                                          | 6.08893%                                                           | 60.88928%                                                           |                                                 1464 |                               40992 |
| Iowa                 | 1.01880%                                                          | 10.18805%                                                          | 101.88047%                                                          |                                                 1148 |                               32144 |
| Kansas               | 1.95777%                                                          | 19.57770%                                                          | 195.77704%                                                          |                                                 2037 |                               57036 |
| Kentucky             | 0.79845%                                                          | 7.98447%                                                           | 79.84470%                                                           |                                                 1274 |                               35672 |
| Louisiana            | 0.56376%                                                          | 5.63759%                                                           | 56.37591%                                                           |                                                  936 |                               26208 |
| Maine                | 0.11248%                                                          | 1.12482%                                                           | 11.24823%                                                           |                                                   54 |                                1512 |
| Maryland             | 0.36357%                                                          | 3.63565%                                                           | 36.35654%                                                           |                                                  785 |                               21980 |
| Massachusetts        | 0.30915%                                                          | 3.09147%                                                           | 30.91475%                                                           |                                                  761 |                               21308 |
| Michigan             | 0.44158%                                                          | 4.41580%                                                           | 44.15804%                                                           |                                                 1575 |                               44100 |
| Minnesota            | 0.72983%                                                          | 7.29835%                                                           | 72.98349%                                                           |                                                 1470 |                               41160 |
| Mississippi          | 0.69338%                                                          | 6.93379%                                                           | 69.33793%                                                           |                                                  737 |                               20636 |
| Missouri             | 0.90650%                                                          | 9.06504%                                                           | 90.65035%                                                           |                                                 1987 |                               55636 |
| Montana              | 1.31253%                                                          | 13.12527%                                                          | 131.25270%                                                          |                                                  501 |                               14028 |
| Nebraska             | 1.14640%                                                          | 11.46397%                                                          | 114.63972%                                                          |                                                  792 |                               22176 |
| Nevada               | 0.70178%                                                          | 7.01783%                                                           | 70.17826%                                                           |                                                  772 |                               21616 |
| New Hampshire        | 0.44686%                                                          | 4.46860%                                                           | 44.68597%                                                           |                                                  217 |                                6076 |
| New Jersey           | 0.29853%                                                          | 2.98530%                                                           | 29.85300%                                                           |                                                  947 |                               26516 |
| New Mexico           | 0.45268%                                                          | 4.52684%                                                           | 45.26836%                                                           |                                                  339 |                                9492 |
| New York             | 0.24915%                                                          | 2.49147%                                                           | 24.91472%                                                           |                                                 1731 |                               48468 |
| North Carolina       | 1.63973%                                                          | 16.39728%                                                          | 163.97275%                                                          |                                                 6142 |                              171976 |
| North Dakota         | 1.81875%                                                          | 18.18750%                                                          | 181.87497%                                                          |                                                  495 |                               13860 |
| Ohio                 | 0.35811%                                                          | 3.58111%                                                           | 35.81114%                                                           |                                                 1495 |                               41860 |
| Oklahoma             | 1.19162%                                                          | 11.91619%                                                          | 119.16185%                                                          |                                                 1684 |                               47152 |
| Oregon               | 0.29807%                                                          | 2.98075%                                                           | 29.80745%                                                           |                                                  449 |                               12572 |
| Pennsylvania         | 0.25393%                                                          | 2.53929%                                                           | 25.39293%                                                           |                                                 1161 |                               32508 |
| Rhode Island         | 0.50748%                                                          | 5.07476%                                                           | 50.74757%                                                           |                                                  192 |                                5376 |
| South Carolina       | 1.44929%                                                          | 14.49294%                                                          | 144.92939%                                                          |                                                 2665 |                               74620 |
| South Dakota         | 2.36430%                                                          | 23.64301%                                                          | 236.43008%                                                          |                                                  747 |                               20916 |
| Tennessee            | 0.86265%                                                          | 8.62652%                                                           | 86.26519%                                                           |                                                 2104 |                               58912 |
| Texas                | 1.72080%                                                          | 17.20796%                                                          | 172.07961%                                                          |                                                17820 |                              498960 |
| Utah                 | 1.23233%                                                          | 12.32331%                                                          | 123.23306%                                                          |                                                 1411 |                               39508 |
| Vermont              | 0.05833%                                                          | 0.58334%                                                           | 5.83344%                                                            |                                                   13 |                                 364 |
| Virginia             | 0.36609%                                                          | 3.66094%                                                           | 36.60937%                                                           |                                                 1116 |                               31248 |
| Washington           | 0.36329%                                                          | 3.63288%                                                           | 36.32881%                                                           |                                                  988 |                               27664 |
| West Virginia        | 0.44215%                                                          | 4.42151%                                                           | 44.21512%                                                           |                                                  283 |                                7924 |
| Wisconsin            | 1.46866%                                                          | 14.68664%                                                          | 146.86641%                                                          |                                                 3054 |                               85512 |
| Wyoming              | 0.81277%                                                          | 8.12774%                                                           | 81.27735%                                                           |                                                  168 |                                4704 |
| Puerto Rico          | 1.03629%                                                          | 10.36292%                                                          | 103.62921%                                                          |                                                 1182 |                               33096 |
| District of Columbia | 0.25788%                                                          | 2.57882%                                                           | 25.78821%                                                           |                                                   65 |                                1820 |