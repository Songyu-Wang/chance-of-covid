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

 Updated at: 2021-01-27T12:31:26.829986+00:00

| State                | Chance of encountering 1 person with COVID if you meet 1 person   | Chance of encountering 1 person with COVID if you meet 10 people   | Chance of encountering a person with COVID if you meet 100 people   |   Max count of new case increase in the past 14 days |   Estimated people count with COVID |
|:---------------------|:------------------------------------------------------------------|:-------------------------------------------------------------------|:--------------------------------------------------------------------|-----------------------------------------------------:|------------------------------------:|
| Alabama              | 2.04895%                                                          | 20.48954%                                                          | 204.89539%                                                          |                                                 3588 |                              100464 |
| Alaska               | 1.55397%                                                          | 15.53971%                                                          | 155.39714%                                                          |                                                  406 |                               11368 |
| Arizona              | 3.61525%                                                          | 36.15253%                                                          | 361.52525%                                                          |                                                 9398 |                              263144 |
| Arkansas             | 2.89853%                                                          | 28.98532%                                                          | 289.85315%                                                          |                                                 3124 |                               87472 |
| California           | 3.02271%                                                          | 30.22710%                                                          | 302.27102%                                                          |                                                42655 |                             1194340 |
| Colorado             | 1.18540%                                                          | 11.85399%                                                          | 118.53990%                                                          |                                                 2438 |                               68264 |
| Connecticut          | 5.26420%                                                          | 52.64205%                                                          | 526.42045%                                                          |                                                 6703 |                              187684 |
| Delaware             | 2.65116%                                                          | 26.51156%                                                          | 265.11557%                                                          |                                                  922 |                               25816 |
| Florida              | 2.13998%                                                          | 21.39983%                                                          | 213.99834%                                                          |                                                16415 |                              459620 |
| Georgia              | 1.93780%                                                          | 19.37796%                                                          | 193.77960%                                                          |                                                 7348 |                              205744 |
| Hawaii               | 0.45287%                                                          | 4.52866%                                                           | 45.28658%                                                           |                                                  229 |                                6412 |
| Idaho                | 1.91778%                                                          | 19.17781%                                                          | 191.77814%                                                          |                                                 1224 |                               34272 |
| Illinois             | 1.55602%                                                          | 15.56019%                                                          | 155.60195%                                                          |                                                 7042 |                              197176 |
| Indiana              | 1.94064%                                                          | 19.40638%                                                          | 194.06380%                                                          |                                                 4666 |                              130648 |
| Iowa                 | 1.27883%                                                          | 12.78831%                                                          | 127.88306%                                                          |                                                 1441 |                               40348 |
| Kansas               | 4.36245%                                                          | 43.62455%                                                          | 436.24546%                                                          |                                                 4539 |                              127092 |
| Kentucky             | 2.85348%                                                          | 28.53477%                                                          | 285.34765%                                                          |                                                 4553 |                              127484 |
| Louisiana            | 3.20006%                                                          | 32.00056%                                                          | 320.00558%                                                          |                                                 5313 |                              148764 |
| Maine                | 1.71640%                                                          | 17.16396%                                                          | 171.63959%                                                          |                                                  824 |                               23072 |
| Maryland             | 1.52466%                                                          | 15.24659%                                                          | 152.46589%                                                          |                                                 3292 |                               92176 |
| Massachusetts        | 2.41915%                                                          | 24.19150%                                                          | 241.91502%                                                          |                                                 5955 |                              166740 |
| Michigan             | 0.93839%                                                          | 9.38393%                                                           | 93.83933%                                                           |                                                 3347 |                               93716 |
| Minnesota            | 0.80778%                                                          | 8.07783%                                                           | 80.77832%                                                           |                                                 1627 |                               45556 |
| Mississippi          | 2.52138%                                                          | 25.21379%                                                          | 252.13791%                                                          |                                                 2680 |                               75040 |
| Missouri             | 1.26828%                                                          | 12.68284%                                                          | 126.82837%                                                          |                                                 2780 |                               77840 |
| Montana              | 1.50901%                                                          | 15.09013%                                                          | 150.90131%                                                          |                                                  576 |                               16128 |
| Nebraska             | 2.21318%                                                          | 22.13184%                                                          | 221.31836%                                                          |                                                 1529 |                               42812 |
| Nevada               | 1.98808%                                                          | 19.88081%                                                          | 198.80811%                                                          |                                                 2187 |                               61236 |
| New Hampshire        | 2.05926%                                                          | 20.59261%                                                          | 205.92611%                                                          |                                                 1000 |                               28000 |
| New Jersey           | 2.48407%                                                          | 24.84072%                                                          | 248.40721%                                                          |                                                 7880 |                              220640 |
| New Mexico           | 1.90154%                                                          | 19.01538%                                                          | 190.15380%                                                          |                                                 1424 |                               39872 |
| New York             | 2.87030%                                                          | 28.70302%                                                          | 287.03023%                                                          |                                                19942 |                              558376 |
| North Carolina       | 2.63232%                                                          | 26.32321%                                                          | 263.23206%                                                          |                                                 9860 |                              276080 |
| North Dakota         | 0.89284%                                                          | 8.92841%                                                           | 89.28407%                                                           |                                                  243 |                                6804 |
| Ohio                 | 1.83343%                                                          | 18.33435%                                                          | 183.34346%                                                          |                                                 7654 |                              214312 |
| Oklahoma             | 2.94154%                                                          | 29.41543%                                                          | 294.15429%                                                          |                                                 4157 |                              116396 |
| Oregon               | 0.88227%                                                          | 8.82274%                                                           | 88.22741%                                                           |                                                 1329 |                               37212 |
| Pennsylvania         | 1.74098%                                                          | 17.40979%                                                          | 174.09795%                                                          |                                                 7960 |                              222880 |
| Rhode Island         | 2.88627%                                                          | 28.86268%                                                          | 288.62682%                                                          |                                                 1092 |                               30576 |
| South Carolina       | 3.51039%                                                          | 35.10391%                                                          | 351.03911%                                                          |                                                 6455 |                              180740 |
| South Dakota         | 1.43061%                                                          | 14.30608%                                                          | 143.06077%                                                          |                                                  452 |                               12656 |
| Tennessee            | 2.27840%                                                          | 22.78401%                                                          | 227.84015%                                                          |                                                 5557 |                              155596 |
| Texas                | 3.01815%                                                          | 30.18153%                                                          | 301.81528%                                                          |                                                31255 |                              875140 |
| Utah                 | 4.53106%                                                          | 45.31064%                                                          | 453.10637%                                                          |                                                 5188 |                              145264 |
| Vermont              | 0.91989%                                                          | 9.19888%                                                           | 91.98880%                                                           |                                                  205 |                                5740 |
| Virginia             | 3.25220%                                                          | 32.52198%                                                          | 325.21983%                                                          |                                                 9914 |                              277592 |
| Washington           | 1.45940%                                                          | 14.59403%                                                          | 145.94033%                                                          |                                                 3969 |                              111132 |
| West Virginia        | 2.30450%                                                          | 23.04498%                                                          | 230.44985%                                                          |                                                 1475 |                               41300 |
| Wisconsin            | 1.51002%                                                          | 15.10021%                                                          | 151.00214%                                                          |                                                 3140 |                               87920 |
| Wyoming              | 1.99323%                                                          | 19.93230%                                                          | 199.32303%                                                          |                                                  412 |                               11536 |
| Puerto Rico          | 0.99772%                                                          | 9.97716%                                                           | 99.77161%                                                           |                                                 1138 |                               31864 |
| District of Columbia | 1.57506%                                                          | 15.75064%                                                          | 157.50642%                                                          |                                                  397 |                               11116 |