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

 Updated at: 2020-08-10T18:15:01.412832+00:00

| State                | Chance of encountering 1 person with COVID if you meet 1 person   | Chance of encountering 1 person with COVID if you meet 10 people   | Chance of encountering a person with COVID if you meet 100 people   |   Max count of new case increase in the past 14 days |   Estimated people count with COVID |
|:---------------------|:------------------------------------------------------------------|:-------------------------------------------------------------------|:--------------------------------------------------------------------|-----------------------------------------------------:|------------------------------------:|
| Alabama              | 1.68291%                                                          | 16.82906%                                                          | 168.29061%                                                          |                                                 2947 |                               82516 |
| Alaska               | 0.60092%                                                          | 6.00920%                                                           | 60.09200%                                                           |                                                  157 |                                4396 |
| Arizona              | 1.23560%                                                          | 12.35602%                                                          | 123.56024%                                                          |                                                 3212 |                               89936 |
| Arkansas             | 1.32123%                                                          | 13.21226%                                                          | 132.12256%                                                          |                                                 1424 |                               39872 |
| California           | 0.72260%                                                          | 7.22602%                                                           | 72.26017%                                                           |                                                10197 |                              285516 |
| Colorado             | 0.36418%                                                          | 3.64177%                                                           | 36.41771%                                                           |                                                  749 |                               20972 |
| Connecticut          | 0.36362%                                                          | 3.63617%                                                           | 36.36173%                                                           |                                                  463 |                               12964 |
| Delaware             | 0.45719%                                                          | 4.57195%                                                           | 45.71950%                                                           |                                                  159 |                                4452 |
| Florida              | 1.29794%                                                          | 12.97939%                                                          | 129.79393%                                                          |                                                 9956 |                              278768 |
| Georgia              | 1.16642%                                                          | 11.66422%                                                          | 116.64224%                                                          |                                                 4423 |                              123844 |
| Hawaii               | 0.45682%                                                          | 4.56821%                                                           | 45.68210%                                                           |                                                  231 |                                6468 |
| Idaho                | 1.08424%                                                          | 10.84236%                                                          | 108.42359%                                                          |                                                  692 |                               19376 |
| Illinois             | 0.48391%                                                          | 4.83908%                                                           | 48.39084%                                                           |                                                 2190 |                               61320 |
| Indiana              | 0.51531%                                                          | 5.15313%                                                           | 51.53130%                                                           |                                                 1239 |                               34692 |
| Iowa                 | 0.67536%                                                          | 6.75357%                                                           | 67.53574%                                                           |                                                  761 |                               21308 |
| Kansas               | 1.02262%                                                          | 10.22615%                                                          | 102.26155%                                                          |                                                 1064 |                               29792 |
| Kentucky             | 0.49010%                                                          | 4.90099%                                                           | 49.00985%                                                           |                                                  782 |                               21896 |
| Louisiana            | 2.17734%                                                          | 21.77339%                                                          | 217.73389%                                                          |                                                 3615 |                              101220 |
| Maine                | 0.05832%                                                          | 0.58324%                                                           | 5.83241%                                                            |                                                   28 |                                 784 |
| Maryland             | 0.54141%                                                          | 5.41411%                                                           | 54.14114%                                                           |                                                 1169 |                               32732 |
| Massachusetts        | 0.22181%                                                          | 2.21806%                                                           | 22.18062%                                                           |                                                  546 |                               15288 |
| Michigan             | 0.28485%                                                          | 2.84854%                                                           | 28.48544%                                                           |                                                 1016 |                               28448 |
| Minnesota            | 0.45478%                                                          | 4.54781%                                                           | 45.47814%                                                           |                                                  916 |                               25648 |
| Mississippi          | 1.66994%                                                          | 16.69943%                                                          | 166.99433%                                                          |                                                 1775 |                               49700 |
| Missouri             | 0.95076%                                                          | 9.50757%                                                           | 95.07566%                                                           |                                                 2084 |                               58352 |
| Montana              | 0.52658%                                                          | 5.26583%                                                           | 52.65827%                                                           |                                                  201 |                                5628 |
| Nebraska             | 0.64412%                                                          | 6.44125%                                                           | 64.41247%                                                           |                                                  445 |                               12460 |
| Nevada               | 1.14903%                                                          | 11.49033%                                                          | 114.90327%                                                          |                                                 1264 |                               35392 |
| New Hampshire        | 0.15650%                                                          | 1.56504%                                                           | 15.65038%                                                           |                                                   76 |                                2128 |
| New Jersey           | 0.21751%                                                          | 2.17514%                                                           | 21.75139%                                                           |                                                  690 |                               19320 |
| New Mexico           | 0.61426%                                                          | 6.14261%                                                           | 61.42609%                                                           |                                                  460 |                               12880 |
| New York             | 0.11184%                                                          | 1.11836%                                                           | 11.18356%                                                           |                                                  777 |                               21756 |
| North Carolina       | 0.62578%                                                          | 6.25777%                                                           | 62.57768%                                                           |                                                 2344 |                               65632 |
| North Dakota         | 0.67239%                                                          | 6.72386%                                                           | 67.23862%                                                           |                                                  183 |                                5124 |
| Ohio                 | 0.41512%                                                          | 4.15122%                                                           | 41.51218%                                                           |                                                 1733 |                               48524 |
| Oklahoma             | 0.99136%                                                          | 9.91364%                                                           | 99.13644%                                                           |                                                 1401 |                               39228 |
| Oregon               | 0.27285%                                                          | 2.72848%                                                           | 27.28477%                                                           |                                                  411 |                               11508 |
| Pennsylvania         | 0.24496%                                                          | 2.44962%                                                           | 24.49619%                                                           |                                                 1120 |                               31360 |
| Rhode Island         | 0.76914%                                                          | 7.69143%                                                           | 76.91429%                                                           |                                                  291 |                                8148 |
| South Carolina       | 0.94462%                                                          | 9.44624%                                                           | 94.46242%                                                           |                                                 1737 |                               48636 |
| South Dakota         | 0.47159%                                                          | 4.71594%                                                           | 47.15941%                                                           |                                                  149 |                                4172 |
| Tennessee            | 1.77655%                                                          | 17.76555%                                                          | 177.65545%                                                          |                                                 4333 |                              121324 |
| Texas                | 1.11330%                                                          | 11.13303%                                                          | 111.33030%                                                          |                                                11529 |                              322812 |
| Utah                 | 0.51267%                                                          | 5.12670%                                                           | 51.26705%                                                           |                                                  587 |                               16436 |
| Vermont              | 0.04039%                                                          | 0.40385%                                                           | 4.03853%                                                            |                                                    9 |                                 252 |
| Virginia             | 0.66100%                                                          | 6.61003%                                                           | 66.10026%                                                           |                                                 2015 |                               56420 |
| Washington           | 0.63906%                                                          | 6.39063%                                                           | 63.90635%                                                           |                                                 1738 |                               48664 |
| West Virginia        | 0.34372%                                                          | 3.43722%                                                           | 34.37218%                                                           |                                                  220 |                                6160 |
| Wisconsin            | 0.56986%                                                          | 5.69865%                                                           | 56.98648%                                                           |                                                 1185 |                               33180 |
| Wyoming              | 0.33382%                                                          | 3.33818%                                                           | 33.38177%                                                           |                                                   69 |                                1932 |
| Puerto Rico          | 0.95651%                                                          | 9.56510%                                                           | 95.65099%                                                           |                                                 1091 |                               30548 |
| District of Columbia | 0.39674%                                                          | 3.96742%                                                           | 39.67416%                                                           |                                                  100 |                                2800 |