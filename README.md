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

 Updated at: 2020-10-30T06:14:20.625594+00:00

| State                | Chance of encountering 1 person with COVID if you meet 1 person   | Chance of encountering 1 person with COVID if you meet 10 people   | Chance of encountering a person with COVID if you meet 100 people   |   Max count of new case increase in the past 14 days |   Estimated people count with COVID |
|:---------------------|:------------------------------------------------------------------|:-------------------------------------------------------------------|:--------------------------------------------------------------------|-----------------------------------------------------:|------------------------------------:|
| Alabama              | 2.19971%                                                          | 21.99713%                                                          | 219.97130%                                                          |                                                 3852 |                              107856 |
| Alaska               | 2.02476%                                                          | 20.24756%                                                          | 202.47558%                                                          |                                                  529 |                               14812 |
| Arizona              | 0.53509%                                                          | 5.35094%                                                           | 53.50943%                                                           |                                                 1391 |                               38948 |
| Arkansas             | 1.24050%                                                          | 12.40505%                                                          | 124.05047%                                                          |                                                 1337 |                               37436 |
| California           | 0.43518%                                                          | 4.35177%                                                           | 43.51767%                                                           |                                                 6141 |                              171948 |
| Colorado             | 1.07503%                                                          | 10.75028%                                                          | 107.50276%                                                          |                                                 2211 |                               61908 |
| Connecticut          | 1.60761%                                                          | 16.07613%                                                          | 160.76125%                                                          |                                                 2047 |                               57316 |
| Delaware             | 0.62685%                                                          | 6.26846%                                                           | 62.68459%                                                           |                                                  218 |                                6104 |
| Florida              | 0.71194%                                                          | 7.11937%                                                           | 71.19372%                                                           |                                                 5461 |                              152908 |
| Georgia              | 0.58651%                                                          | 5.86508%                                                           | 58.65077%                                                           |                                                 2224 |                               62272 |
| Hawaii               | 0.27686%                                                          | 2.76861%                                                           | 27.68612%                                                           |                                                  140 |                                3920 |
| Idaho                | 1.71410%                                                          | 17.14095%                                                          | 171.40955%                                                          |                                                 1094 |                               30632 |
| Illinois             | 1.40599%                                                          | 14.05986%                                                          | 140.59858%                                                          |                                                 6363 |                              178164 |
| Indiana              | 1.50476%                                                          | 15.04764%                                                          | 150.47639%                                                          |                                                 3618 |                              101304 |
| Iowa                 | 1.72167%                                                          | 17.21673%                                                          | 172.16734%                                                          |                                                 1940 |                               54320 |
| Kansas               | 3.23796%                                                          | 32.37962%                                                          | 323.79620%                                                          |                                                 3369 |                               94332 |
| Kentucky             | 1.16383%                                                          | 11.63827%                                                          | 116.38273%                                                          |                                                 1857 |                               51996 |
| Louisiana            | 0.82094%                                                          | 8.20944%                                                           | 82.09441%                                                           |                                                 1363 |                               38164 |
| Maine                | 0.16664%                                                          | 1.66640%                                                           | 16.66404%                                                           |                                                   80 |                                2240 |
| Maryland             | 0.44554%                                                          | 4.45541%                                                           | 44.55413%                                                           |                                                  962 |                               26936 |
| Massachusetts        | 0.54680%                                                          | 5.46797%                                                           | 54.67970%                                                           |                                                 1346 |                               37688 |
| Michigan             | 1.40296%                                                          | 14.02964%                                                          | 140.29639%                                                          |                                                 5004 |                              140112 |
| Minnesota            | 1.42343%                                                          | 14.23426%                                                          | 142.34262%                                                          |                                                 2867 |                               80276 |
| Mississippi          | 1.14027%                                                          | 11.40265%                                                          | 114.02655%                                                          |                                                 1212 |                               33936 |
| Missouri             | 1.39648%                                                          | 13.96481%                                                          | 139.64807%                                                          |                                                 3061 |                               85708 |
| Montana              | 2.43119%                                                          | 24.31188%                                                          | 243.11878%                                                          |                                                  928 |                               25984 |
| Nebraska             | 1.86145%                                                          | 18.61448%                                                          | 186.14481%                                                          |                                                 1286 |                               36008 |
| Nevada               | 1.04177%                                                          | 10.41765%                                                          | 104.17654%                                                          |                                                 1146 |                               32088 |
| New Hampshire        | 0.27594%                                                          | 2.75941%                                                           | 27.59410%                                                           |                                                  134 |                                3752 |
| New Jersey           | 0.60179%                                                          | 6.01789%                                                           | 60.17885%                                                           |                                                 1909 |                               53452 |
| New Mexico           | 1.16442%                                                          | 11.64425%                                                          | 116.44249%                                                          |                                                  872 |                               24416 |
| New York             | 0.35969%                                                          | 3.59687%                                                           | 35.96874%                                                           |                                                 2499 |                               69972 |
| North Carolina       | 0.77021%                                                          | 7.70207%                                                           | 77.02074%                                                           |                                                 2885 |                               80780 |
| North Dakota         | 4.49360%                                                          | 44.93598%                                                          | 449.35976%                                                          |                                                 1223 |                               34244 |
| Ohio                 | 0.85995%                                                          | 8.59946%                                                           | 85.99464%                                                           |                                                 3590 |                              100520 |
| Oklahoma             | 1.29422%                                                          | 12.94222%                                                          | 129.42223%                                                          |                                                 1829 |                               51212 |
| Oregon               | 0.37508%                                                          | 3.75083%                                                           | 37.50827%                                                           |                                                  565 |                               15820 |
| Pennsylvania         | 0.60169%                                                          | 6.01688%                                                           | 60.16878%                                                           |                                                 2751 |                               77028 |
| Rhode Island         | 1.38499%                                                          | 13.84986%                                                          | 138.49859%                                                          |                                                  524 |                               14672 |
| South Carolina       | 0.72709%                                                          | 7.27094%                                                           | 72.70942%                                                           |                                                 1337 |                               37436 |
| South Dakota         | 4.01963%                                                          | 40.19628%                                                          | 401.96279%                                                          |                                                 1270 |                               35560 |
| Tennessee            | 1.47848%                                                          | 14.78480%                                                          | 147.84804%                                                          |                                                 3606 |                              100968 |
| Texas                | 0.76132%                                                          | 7.61322%                                                           | 76.13219%                                                           |                                                 7884 |                              220752 |
| Utah                 | 1.71181%                                                          | 17.11813%                                                          | 171.18128%                                                          |                                                 1960 |                               54880 |
| Vermont              | 0.13462%                                                          | 1.34618%                                                           | 13.46178%                                                           |                                                   30 |                                 840 |
| Virginia             | 0.46877%                                                          | 4.68771%                                                           | 46.87706%                                                           |                                                 1429 |                               40012 |
| Washington           | 0.57655%                                                          | 5.76554%                                                           | 57.65544%                                                           |                                                 1568 |                               43904 |
| West Virginia        | 0.77806%                                                          | 7.78061%                                                           | 77.80612%                                                           |                                                  498 |                               13944 |
| Wisconsin            | 3.80631%                                                          | 38.06312%                                                          | 380.63119%                                                          |                                                 7915 |                              221620 |
| Wyoming              | 2.10934%                                                          | 21.09341%                                                          | 210.93408%                                                          |                                                  436 |                               12208 |
| Puerto Rico          | 1.70699%                                                          | 17.06989%                                                          | 170.69888%                                                          |                                                 1947 |                               54516 |
| District of Columbia | 0.40071%                                                          | 4.00709%                                                           | 40.07090%                                                           |                                                  101 |                                2828 |