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

 Updated at: 2021-01-04T18:42:42.146874+00:00

| State                | Chance of encountering 1 person with COVID if you meet 1 person   | Chance of encountering 1 person with COVID if you meet 10 people   | Chance of encountering a person with COVID if you meet 100 people   |   Max count of new case increase in the past 14 days |   Estimated people count with COVID |
|:---------------------|:------------------------------------------------------------------|:-------------------------------------------------------------------|:--------------------------------------------------------------------|-----------------------------------------------------:|------------------------------------:|
| Alabama              | 2.86442%                                                          | 28.64424%                                                          | 286.44238%                                                          |                                                 5016 |                              140448 |
| Alaska               | 3.06584%                                                          | 30.65840%                                                          | 306.58401%                                                          |                                                  801 |                               22428 |
| Arizona              | 6.62963%                                                          | 66.29630%                                                          | 662.96299%                                                          |                                                17234 |                              482552 |
| Arkansas             | 3.99337%                                                          | 39.93367%                                                          | 399.33674%                                                          |                                                 4304 |                              120512 |
| California           | 3.77996%                                                          | 37.79964%                                                          | 377.99645%                                                          |                                                53341 |                             1493548 |
| Colorado             | 1.57437%                                                          | 15.74373%                                                          | 157.43733%                                                          |                                                 3238 |                               90664 |
| Connecticut          | 6.64171%                                                          | 66.41709%                                                          | 664.17093%                                                          |                                                 8457 |                              236796 |
| Delaware             | 2.47288%                                                          | 24.72878%                                                          | 247.28784%                                                          |                                                  860 |                               24080 |
| Florida              | 3.98025%                                                          | 39.80252%                                                          | 398.02517%                                                          |                                                30531 |                              854868 |
| Georgia              | 2.29935%                                                          | 22.99353%                                                          | 229.93527%                                                          |                                                 8719 |                              244132 |
| Hawaii               | 0.56954%                                                          | 5.69543%                                                           | 56.95430%                                                           |                                                  288 |                                8064 |
| Idaho                | 2.69022%                                                          | 26.90221%                                                          | 269.02211%                                                          |                                                 1717 |                               48076 |
| Illinois             | 1.76969%                                                          | 17.69690%                                                          | 176.96904%                                                          |                                                 8009 |                              224252 |
| Indiana              | 2.69011%                                                          | 26.90109%                                                          | 269.01086%                                                          |                                                 6468 |                              181104 |
| Iowa                 | 1.41372%                                                          | 14.13725%                                                          | 141.37246%                                                          |                                                 1593 |                               44604 |
| Kansas               | 6.12512%                                                          | 61.25121%                                                          | 612.51207%                                                          |                                                 6373 |                              178444 |
| Kentucky             | 5.45814%                                                          | 54.58143%                                                          | 545.81434%                                                          |                                                 8709 |                              243852 |
| Louisiana            | 4.06196%                                                          | 40.61957%                                                          | 406.19567%                                                          |                                                 6744 |                              188832 |
| Maine                | 2.17466%                                                          | 21.74657%                                                          | 217.46570%                                                          |                                                 1044 |                               29232 |
| Maryland             | 1.64739%                                                          | 16.47391%                                                          | 164.73912%                                                          |                                                 3557 |                               99596 |
| Massachusetts        | 3.65737%                                                          | 36.57365%                                                          | 365.73651%                                                          |                                                 9003 |                              252084 |
| Michigan             | 2.66350%                                                          | 26.63501%                                                          | 266.35006%                                                          |                                                 9500 |                              266000 |
| Minnesota            | 1.34647%                                                          | 13.46471%                                                          | 134.64708%                                                          |                                                 2712 |                               75936 |
| Mississippi          | 2.84408%                                                          | 28.44078%                                                          | 284.40780%                                                          |                                                 3023 |                               84644 |
| Missouri             | 2.15745%                                                          | 21.57451%                                                          | 215.74510%                                                          |                                                 4729 |                              132412 |
| Montana              | 2.28972%                                                          | 22.89718%                                                          | 228.97178%                                                          |                                                  874 |                               24472 |
| Nebraska             | 2.19437%                                                          | 21.94366%                                                          | 219.43664%                                                          |                                                 1516 |                               42448 |
| Nevada               | 2.71623%                                                          | 27.16226%                                                          | 271.62261%                                                          |                                                 2988 |                               83664 |
| New Hampshire        | 2.60702%                                                          | 26.07025%                                                          | 260.70246%                                                          |                                                 1266 |                               35448 |
| New Jersey           | 1.73727%                                                          | 17.37274%                                                          | 173.72743%                                                          |                                                 5511 |                              154308 |
| New Mexico           | 2.56921%                                                          | 25.69213%                                                          | 256.92128%                                                          |                                                 1924 |                               53872 |
| New York             | 2.41835%                                                          | 24.18354%                                                          | 241.83542%                                                          |                                                16802 |                              470456 |
| North Carolina       | 5.18428%                                                          | 51.84283%                                                          | 518.42834%                                                          |                                                19419 |                              543732 |
| North Dakota         | 1.49542%                                                          | 14.95416%                                                          | 149.54164%                                                          |                                                  407 |                               11396 |
| Ohio                 | 3.42374%                                                          | 34.23737%                                                          | 342.37366%                                                          |                                                14293 |                              400204 |
| Oklahoma             | 5.67293%                                                          | 56.72925%                                                          | 567.29251%                                                          |                                                 8017 |                              224476 |
| Oregon               | 1.09471%                                                          | 10.94710%                                                          | 109.47103%                                                          |                                                 1649 |                               46172 |
| Pennsylvania         | 2.10077%                                                          | 21.00767%                                                          | 210.07673%                                                          |                                                 9605 |                              268940 |
| Rhode Island         | 3.13736%                                                          | 31.37363%                                                          | 313.73630%                                                          |                                                 1187 |                               33236 |
| South Carolina       | 4.86778%                                                          | 48.67779%                                                          | 486.77786%                                                          |                                                 8951 |                              250628 |
| South Dakota         | 2.22504%                                                          | 22.25038%                                                          | 222.50381%                                                          |                                                  703 |                               19684 |
| Tennessee            | 7.10540%                                                          | 71.05398%                                                          | 710.53981%                                                          |                                                17330 |                              485240 |
| Texas                | 3.14340%                                                          | 31.43398%                                                          | 314.33982%                                                          |                                                32552 |                              911456 |
| Utah                 | 4.40355%                                                          | 44.03551%                                                          | 440.35511%                                                          |                                                 5042 |                              141176 |
| Vermont              | 1.24297%                                                          | 12.42971%                                                          | 124.29706%                                                          |                                                  277 |                                7756 |
| Virginia             | 1.71861%                                                          | 17.18607%                                                          | 171.86067%                                                          |                                                 5239 |                              146692 |
| Washington           | 1.62597%                                                          | 16.25972%                                                          | 162.59716%                                                          |                                                 4422 |                              123816 |
| West Virginia        | 3.88406%                                                          | 38.84056%                                                          | 388.40564%                                                          |                                                 2486 |                               69608 |
| Wisconsin            | 2.02554%                                                          | 20.25545%                                                          | 202.55446%                                                          |                                                 4212 |                              117936 |
| Wyoming              | 2.43832%                                                          | 24.38321%                                                          | 243.83206%                                                          |                                                  504 |                               14112 |
| Puerto Rico          | 1.86918%                                                          | 18.69183%                                                          | 186.91835%                                                          |                                                 2132 |                               59696 |
| District of Columbia | 1.95197%                                                          | 19.51969%                                                          | 195.19688%                                                          |                                                  492 |                               13776 |