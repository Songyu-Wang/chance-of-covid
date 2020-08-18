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

 Updated at: 2020-08-18T06:16:13.326892+00:00

| State                | Chance of encountering 1 person with COVID if you meet 1 person   | Chance of encountering 1 person with COVID if you meet 10 people   | Chance of encountering a person with COVID if you meet 100 people   |   Max count of new case increase in the past 14 days |   Estimated people count with COVID |
|:---------------------|:------------------------------------------------------------------|:-------------------------------------------------------------------|:--------------------------------------------------------------------|-----------------------------------------------------:|------------------------------------:|
| Alabama              | 1.68291%                                                          | 16.82906%                                                          | 168.29061%                                                          |                                                 2947 |                               82516 |
| Alaska               | 0.45547%                                                          | 4.55474%                                                           | 45.54744%                                                           |                                                  119 |                                3332 |
| Arizona              | 0.65319%                                                          | 6.53192%                                                           | 65.31920%                                                           |                                                 1698 |                               47544 |
| Arkansas             | 1.24700%                                                          | 12.46999%                                                          | 124.69995%                                                          |                                                 1344 |                               37632 |
| California           | 0.89388%                                                          | 8.93880%                                                           | 89.38804%                                                           |                                                12614 |                              353192 |
| Colorado             | 0.28881%                                                          | 2.88813%                                                           | 28.88134%                                                           |                                                  594 |                               16632 |
| Connecticut          | 0.29058%                                                          | 2.90580%                                                           | 29.05797%                                                           |                                                  370 |                               10360 |
| Delaware             | 1.07254%                                                          | 10.72539%                                                          | 107.25391%                                                          |                                                  373 |                               10444 |
| Florida              | 1.10838%                                                          | 11.08385%                                                          | 110.83849%                                                          |                                                 8502 |                              238056 |
| Georgia              | 1.16642%                                                          | 11.66422%                                                          | 116.64224%                                                          |                                                 4423 |                              123844 |
| Hawaii               | 0.70006%                                                          | 7.00063%                                                           | 70.00633%                                                           |                                                  354 |                                9912 |
| Idaho                | 1.08424%                                                          | 10.84236%                                                          | 108.42359%                                                          |                                                  692 |                               19376 |
| Illinois             | 0.50733%                                                          | 5.07330%                                                           | 50.73304%                                                           |                                                 2296 |                               64288 |
| Indiana              | 0.51531%                                                          | 5.15313%                                                           | 51.53130%                                                           |                                                 1239 |                               34692 |
| Iowa                 | 0.76410%                                                          | 7.64103%                                                           | 76.41035%                                                           |                                                  861 |                               24108 |
| Kansas               | 1.28596%                                                          | 12.85958%                                                          | 128.59582%                                                          |                                                 1338 |                               37464 |
| Kentucky             | 0.72199%                                                          | 7.21987%                                                           | 72.19866%                                                           |                                                 1152 |                               32256 |
| Louisiana            | 2.17734%                                                          | 21.77339%                                                          | 217.73389%                                                          |                                                 3615 |                              101220 |
| Maine                | 0.06041%                                                          | 0.60407%                                                           | 6.04071%                                                            |                                                   29 |                                 812 |
| Maryland             | 0.42702%                                                          | 4.27016%                                                           | 42.70157%                                                           |                                                  922 |                               25816 |
| Massachusetts        | 0.22181%                                                          | 2.21806%                                                           | 22.18062%                                                           |                                                  546 |                               15288 |
| Michigan             | 0.32719%                                                          | 3.27190%                                                           | 32.71900%                                                           |                                                 1167 |                               32676 |
| Minnesota            | 0.45478%                                                          | 4.54781%                                                           | 45.47814%                                                           |                                                  916 |                               25648 |
| Mississippi          | 1.17131%                                                          | 11.71312%                                                          | 117.13123%                                                          |                                                 1245 |                               34860 |
| Missouri             | 1.17476%                                                          | 11.74759%                                                          | 117.47592%                                                          |                                                 2575 |                               72100 |
| Montana              | 0.45323%                                                          | 4.53228%                                                           | 45.32279%                                                           |                                                  173 |                                4844 |
| Nebraska             | 0.60215%                                                          | 6.02148%                                                           | 60.21480%                                                           |                                                  416 |                               11648 |
| Nevada               | 0.99904%                                                          | 9.99040%                                                           | 99.90403%                                                           |                                                 1099 |                               30772 |
| New Hampshire        | 0.15650%                                                          | 1.56504%                                                           | 15.65038%                                                           |                                                   76 |                                2128 |
| New Jersey           | 0.20680%                                                          | 2.06796%                                                           | 20.67958%                                                           |                                                  656 |                               18368 |
| New Mexico           | 0.30179%                                                          | 3.01789%                                                           | 30.17890%                                                           |                                                  226 |                                6328 |
| New York             | 0.10737%                                                          | 1.07374%                                                           | 10.73737%                                                           |                                                  746 |                               20888 |
| North Carolina       | 0.52833%                                                          | 5.28333%                                                           | 52.83329%                                                           |                                                 1979 |                               55412 |
| North Dakota         | 0.73852%                                                          | 7.38523%                                                           | 73.85226%                                                           |                                                  201 |                                5628 |
| Ohio                 | 0.34063%                                                          | 3.40625%                                                           | 34.06250%                                                           |                                                 1422 |                               39816 |
| Oklahoma             | 0.77908%                                                          | 7.79081%                                                           | 77.90808%                                                           |                                                 1101 |                               30828 |
| Oregon               | 0.27285%                                                          | 2.72848%                                                           | 27.28477%                                                           |                                                  411 |                               11508 |
| Pennsylvania         | 0.21675%                                                          | 2.16748%                                                           | 21.67476%                                                           |                                                  991 |                               27748 |
| Rhode Island         | 0.44404%                                                          | 4.44041%                                                           | 44.40413%                                                           |                                                  168 |                                4704 |
| South Carolina       | 0.77332%                                                          | 7.73319%                                                           | 77.33193%                                                           |                                                 1422 |                               39816 |
| South Dakota         | 0.49375%                                                          | 4.93750%                                                           | 49.37496%                                                           |                                                  156 |                                4368 |
| Tennessee            | 0.99713%                                                          | 9.97134%                                                           | 99.71338%                                                           |                                                 2432 |                               68096 |
| Texas                | 0.94663%                                                          | 9.46631%                                                           | 94.66310%                                                           |                                                 9803 |                              274484 |
| Utah                 | 0.51267%                                                          | 5.12670%                                                           | 51.26705%                                                           |                                                  587 |                               16436 |
| Vermont              | 0.07628%                                                          | 0.76283%                                                           | 7.62834%                                                            |                                                   17 |                                 476 |
| Virginia             | 0.66100%                                                          | 6.61003%                                                           | 66.10026%                                                           |                                                 2015 |                               56420 |
| Washington           | 0.34417%                                                          | 3.44168%                                                           | 34.41677%                                                           |                                                  936 |                               26208 |
| West Virginia        | 0.28591%                                                          | 2.85914%                                                           | 28.59140%                                                           |                                                  183 |                                5124 |
| Wisconsin            | 0.56986%                                                          | 5.69865%                                                           | 56.98648%                                                           |                                                 1185 |                               33180 |
| Wyoming              | 0.30963%                                                          | 3.09628%                                                           | 30.96280%                                                           |                                                   64 |                                1792 |
| Puerto Rico          | 0.66105%                                                          | 6.61053%                                                           | 66.10527%                                                           |                                                  754 |                               21112 |
| District of Columbia | 0.39674%                                                          | 3.96742%                                                           | 39.67416%                                                           |                                                  100 |                                2800 |