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

 Updated at: 2021-01-23T12:48:07.994266+00:00

| State                | Chance of encountering 1 person with COVID if you meet 1 person   | Chance of encountering 1 person with COVID if you meet 10 people   | Chance of encountering a person with COVID if you meet 100 people   |   Max count of new case increase in the past 14 days |   Estimated people count with COVID |
|:---------------------|:------------------------------------------------------------------|:-------------------------------------------------------------------|:--------------------------------------------------------------------|-----------------------------------------------------:|------------------------------------:|
| Alabama              | 2.77705%                                                          | 27.77052%                                                          | 277.70521%                                                          |                                                 4863 |                              136164 |
| Alaska               | 1.55397%                                                          | 15.53971%                                                          | 155.39714%                                                          |                                                  406 |                               11368 |
| Arizona              | 4.30884%                                                          | 43.08836%                                                          | 430.88363%                                                          |                                                11201 |                              313628 |
| Arkansas             | 3.08966%                                                          | 30.89664%                                                          | 308.96639%                                                          |                                                 3330 |                               93240 |
| California           | 3.73001%                                                          | 37.30005%                                                          | 373.00053%                                                          |                                                52636 |                             1473808 |
| Colorado             | 1.37940%                                                          | 13.79400%                                                          | 137.93999%                                                          |                                                 2837 |                               79436 |
| Connecticut          | 5.78332%                                                          | 57.83321%                                                          | 578.33212%                                                          |                                                 7364 |                              206192 |
| Delaware             | 2.79493%                                                          | 27.94928%                                                          | 279.49277%                                                          |                                                  972 |                               27216 |
| Florida              | 2.13998%                                                          | 21.39983%                                                          | 213.99834%                                                          |                                                16415 |                              459620 |
| Georgia              | 2.36212%                                                          | 23.62117%                                                          | 236.21174%                                                          |                                                 8957 |                              250796 |
| Hawaii               | 0.49044%                                                          | 4.90440%                                                           | 49.04398%                                                           |                                                  248 |                                6944 |
| Idaho                | 1.91778%                                                          | 19.17781%                                                          | 191.77814%                                                          |                                                 1224 |                               34272 |
| Illinois             | 1.55602%                                                          | 15.56019%                                                          | 155.60195%                                                          |                                                 7042 |                              197176 |
| Indiana              | 2.48132%                                                          | 24.81322%                                                          | 248.13215%                                                          |                                                 5966 |                              167048 |
| Iowa                 | 1.27883%                                                          | 12.78831%                                                          | 127.88306%                                                          |                                                 1441 |                               40348 |
| Kansas               | 4.97852%                                                          | 49.78523%                                                          | 497.85227%                                                          |                                                 5180 |                              145040 |
| Kentucky             | 2.85348%                                                          | 28.53477%                                                          | 285.34765%                                                          |                                                 4553 |                              127484 |
| Louisiana            | 3.25125%                                                          | 32.51252%                                                          | 325.12518%                                                          |                                                 5398 |                              151144 |
| Maine                | 1.71640%                                                          | 17.16396%                                                          | 171.63959%                                                          |                                                  824 |                               23072 |
| Maryland             | 1.74048%                                                          | 17.40482%                                                          | 174.04825%                                                          |                                                 3758 |                              105224 |
| Massachusetts        | 3.01185%                                                          | 30.11852%                                                          | 301.18522%                                                          |                                                 7414 |                              207592 |
| Michigan             | 1.43801%                                                          | 14.38010%                                                          | 143.80100%                                                          |                                                 5129 |                              143612 |
| Minnesota            | 1.22582%                                                          | 12.25825%                                                          | 122.58247%                                                          |                                                 2469 |                               69132 |
| Mississippi          | 3.01342%                                                          | 30.13424%                                                          | 301.34244%                                                          |                                                 3203 |                               89684 |
| Missouri             | 1.74503%                                                          | 17.45031%                                                          | 174.50307%                                                          |                                                 3825 |                              107100 |
| Montana              | 1.50901%                                                          | 15.09013%                                                          | 150.90131%                                                          |                                                  576 |                               16128 |
| Nebraska             | 2.21318%                                                          | 22.13184%                                                          | 221.31836%                                                          |                                                 1529 |                               42812 |
| Nevada               | 2.40715%                                                          | 24.07151%                                                          | 240.71508%                                                          |                                                 2648 |                               74144 |
| New Hampshire        | 2.05926%                                                          | 20.59261%                                                          | 205.92611%                                                          |                                                 1000 |                               28000 |
| New Jersey           | 2.48407%                                                          | 24.84072%                                                          | 248.40721%                                                          |                                                 7880 |                              220640 |
| New Mexico           | 2.00035%                                                          | 20.00354%                                                          | 200.03539%                                                          |                                                 1498 |                               41944 |
| New York             | 2.87030%                                                          | 28.70302%                                                          | 287.03023%                                                          |                                                19942 |                              558376 |
| North Carolina       | 3.09178%                                                          | 30.91775%                                                          | 309.17754%                                                          |                                                11581 |                              324268 |
| North Dakota         | 0.89284%                                                          | 8.92841%                                                           | 89.28407%                                                           |                                                  243 |                                6804 |
| Ohio                 | 2.00590%                                                          | 20.05903%                                                          | 200.59029%                                                          |                                                 8374 |                              234472 |
| Oklahoma             | 4.59028%                                                          | 45.90279%                                                          | 459.02788%                                                          |                                                 6487 |                              181636 |
| Oregon               | 1.16973%                                                          | 11.69727%                                                          | 116.97268%                                                          |                                                 1762 |                               49336 |
| Pennsylvania         | 2.19700%                                                          | 21.97002%                                                          | 219.70024%                                                          |                                                10045 |                              281260 |
| Rhode Island         | 3.66598%                                                          | 36.65984%                                                          | 366.59836%                                                          |                                                 1387 |                               38836 |
| South Carolina       | 3.51039%                                                          | 35.10391%                                                          | 351.03911%                                                          |                                                 6455 |                              180740 |
| South Dakota         | 1.43061%                                                          | 14.30608%                                                          | 143.06077%                                                          |                                                  452 |                               12656 |
| Tennessee            | 3.04183%                                                          | 30.41832%                                                          | 304.18320%                                                          |                                                 7419 |                              207732 |
| Texas                | 3.01815%                                                          | 30.18153%                                                          | 301.81528%                                                          |                                                31255 |                              875140 |
| Utah                 | 4.53106%                                                          | 45.31064%                                                          | 453.10637%                                                          |                                                 5188 |                              145264 |
| Vermont              | 0.91989%                                                          | 9.19888%                                                           | 91.98880%                                                           |                                                  205 |                                5740 |
| Virginia             | 3.25220%                                                          | 32.52198%                                                          | 325.21983%                                                          |                                                 9914 |                              277592 |
| Washington           | 1.87196%                                                          | 18.71963%                                                          | 187.19633%                                                          |                                                 5091 |                              142548 |
| West Virginia        | 2.93726%                                                          | 29.37259%                                                          | 293.72591%                                                          |                                                 1880 |                               52640 |
| Wisconsin            | 1.69084%                                                          | 16.90839%                                                          | 169.08393%                                                          |                                                 3516 |                               98448 |
| Wyoming              | 3.27528%                                                          | 32.75284%                                                          | 327.52838%                                                          |                                                  677 |                               18956 |
| Puerto Rico          | 0.99772%                                                          | 9.97716%                                                           | 99.77161%                                                           |                                                 1138 |                               31864 |
| District of Columbia | 1.70599%                                                          | 17.05989%                                                          | 170.59890%                                                          |                                                  430 |                               12040 |