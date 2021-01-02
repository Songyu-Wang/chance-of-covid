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

 Updated at: 2021-01-02T01:07:22.452952+00:00

| State                | Chance of encountering 1 person with COVID if you meet 1 person   | Chance of encountering 1 person with COVID if you meet 10 people   | Chance of encountering a person with COVID if you meet 100 people   |   Max count of new case increase in the past 14 days |   Estimated people count with COVID |
|:---------------------|:------------------------------------------------------------------|:-------------------------------------------------------------------|:--------------------------------------------------------------------|-----------------------------------------------------:|------------------------------------:|
| Alabama              | 2.86442%                                                          | 28.64424%                                                          | 286.44238%                                                          |                                                 5016 |                              140448 |
| Alaska               | 1.89462%                                                          | 18.94620%                                                          | 189.46203%                                                          |                                                  495 |                               13860 |
| Arizona              | 3.87991%                                                          | 38.79915%                                                          | 387.99146%                                                          |                                                10086 |                              282408 |
| Arkansas             | 2.97276%                                                          | 29.72758%                                                          | 297.27577%                                                          |                                                 3204 |                               89712 |
| California           | 3.55320%                                                          | 35.53199%                                                          | 355.31992%                                                          |                                                50141 |                             1403948 |
| Colorado             | 1.57437%                                                          | 15.74373%                                                          | 157.43733%                                                          |                                                 3238 |                               90664 |
| Connecticut          | 6.64171%                                                          | 66.41709%                                                          | 664.17093%                                                          |                                                 8457 |                              236796 |
| Delaware             | 2.95308%                                                          | 29.53077%                                                          | 295.30769%                                                          |                                                 1027 |                               28756 |
| Florida              | 2.19369%                                                          | 21.93695%                                                          | 219.36948%                                                          |                                                16827 |                              471156 |
| Georgia              | 2.29935%                                                          | 22.99353%                                                          | 229.93527%                                                          |                                                 8719 |                              244132 |
| Hawaii               | 0.56954%                                                          | 5.69543%                                                           | 56.95430%                                                           |                                                  288 |                                8064 |
| Idaho                | 2.69022%                                                          | 26.90221%                                                          | 269.02211%                                                          |                                                 1717 |                               48076 |
| Illinois             | 1.76969%                                                          | 17.69690%                                                          | 176.96904%                                                          |                                                 8009 |                              224252 |
| Indiana              | 2.69635%                                                          | 26.96347%                                                          | 269.63472%                                                          |                                                 6483 |                              181524 |
| Iowa                 | 1.41372%                                                          | 14.13725%                                                          | 141.37246%                                                          |                                                 1593 |                               44604 |
| Kansas               | 6.12512%                                                          | 61.25121%                                                          | 612.51207%                                                          |                                                 6373 |                              178444 |
| Kentucky             | 3.31099%                                                          | 33.10985%                                                          | 331.09854%                                                          |                                                 5283 |                              147924 |
| Louisiana            | 4.06196%                                                          | 40.61957%                                                          | 406.19567%                                                          |                                                 6744 |                              188832 |
| Maine                | 1.55809%                                                          | 15.58088%                                                          | 155.80876%                                                          |                                                  748 |                               20944 |
| Maryland             | 1.64739%                                                          | 16.47391%                                                          | 164.73912%                                                          |                                                 3557 |                               99596 |
| Massachusetts        | 3.11869%                                                          | 31.18693%                                                          | 311.86929%                                                          |                                                 7677 |                              214956 |
| Michigan             | 2.20846%                                                          | 22.08463%                                                          | 220.84626%                                                          |                                                 7877 |                              220556 |
| Minnesota            | 1.36335%                                                          | 13.63351%                                                          | 136.33514%                                                          |                                                 2746 |                               76888 |
| Mississippi          | 2.84408%                                                          | 28.44078%                                                          | 284.40780%                                                          |                                                 3023 |                               84644 |
| Missouri             | 2.15745%                                                          | 21.57451%                                                          | 215.74510%                                                          |                                                 4729 |                              132412 |
| Montana              | 2.28972%                                                          | 22.89718%                                                          | 228.97178%                                                          |                                                  874 |                               24472 |
| Nebraska             | 2.19437%                                                          | 21.94366%                                                          | 219.43664%                                                          |                                                 1516 |                               42448 |
| Nevada               | 2.71623%                                                          | 27.16226%                                                          | 271.62261%                                                          |                                                 2988 |                               83664 |
| New Hampshire        | 2.12310%                                                          | 21.23098%                                                          | 212.30982%                                                          |                                                 1031 |                               28868 |
| New Jersey           | 1.73412%                                                          | 17.34122%                                                          | 173.41219%                                                          |                                                 5501 |                              154028 |
| New Mexico           | 2.56921%                                                          | 25.69213%                                                          | 256.92128%                                                          |                                                 1924 |                               53872 |
| New York             | 2.41835%                                                          | 24.18354%                                                          | 241.83542%                                                          |                                                16802 |                              470456 |
| North Carolina       | 5.18428%                                                          | 51.84283%                                                          | 518.42834%                                                          |                                                19419 |                              543732 |
| North Dakota         | 1.49542%                                                          | 14.95416%                                                          | 149.54164%                                                          |                                                  407 |                               11396 |
| Ohio                 | 2.63925%                                                          | 26.39245%                                                          | 263.92451%                                                          |                                                11018 |                              308504 |
| Oklahoma             | 3.51683%                                                          | 35.16831%                                                          | 351.68314%                                                          |                                                 4970 |                              139160 |
| Oregon               | 1.09471%                                                          | 10.94710%                                                          | 109.47103%                                                          |                                                 1649 |                               46172 |
| Pennsylvania         | 2.15085%                                                          | 21.50853%                                                          | 215.08533%                                                          |                                                 9834 |                              275352 |
| Rhode Island         | 3.13736%                                                          | 31.37363%                                                          | 313.73630%                                                          |                                                 1187 |                               33236 |
| South Carolina       | 3.96285%                                                          | 39.62854%                                                          | 396.28536%                                                          |                                                 7287 |                              204036 |
| South Dakota         | 1.78509%                                                          | 17.85095%                                                          | 178.50946%                                                          |                                                  564 |                               15792 |
| Tennessee            | 6.57485%                                                          | 65.74851%                                                          | 657.48508%                                                          |                                                16036 |                              449008 |
| Texas                | 3.14340%                                                          | 31.43398%                                                          | 314.33982%                                                          |                                                32552 |                              911456 |
| Utah                 | 4.08040%                                                          | 40.80403%                                                          | 408.04028%                                                          |                                                 4672 |                              130816 |
| Vermont              | 0.83014%                                                          | 8.30143%                                                           | 83.01428%                                                           |                                                  185 |                                5180 |
| Virginia             | 1.71861%                                                          | 17.18607%                                                          | 171.86067%                                                          |                                                 5239 |                              146692 |
| Washington           | 1.62597%                                                          | 16.25972%                                                          | 162.59716%                                                          |                                                 4422 |                              123816 |
| West Virginia        | 3.88406%                                                          | 38.84056%                                                          | 388.40564%                                                          |                                                 2486 |                               69608 |
| Wisconsin            | 2.07508%                                                          | 20.75077%                                                          | 207.50772%                                                          |                                                 4315 |                              120820 |
| Wyoming              | 2.43832%                                                          | 24.38321%                                                          | 243.83206%                                                          |                                                  504 |                               14112 |
| Puerto Rico          | 1.86918%                                                          | 18.69183%                                                          | 186.91835%                                                          |                                                 2132 |                               59696 |
| District of Columbia | 1.95197%                                                          | 19.51969%                                                          | 195.19688%                                                          |                                                  492 |                               13776 |