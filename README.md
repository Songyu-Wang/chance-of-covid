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

 Updated at: 2021-01-19T01:33:54.071123+00:00

| State                | Chance of encountering 1 person with COVID if you meet 1 person   | Chance of encountering 1 person with COVID if you meet 10 people   | Chance of encountering a person with COVID if you meet 100 people   |   Max count of new case increase in the past 14 days |   Estimated people count with COVID |
|:---------------------|:------------------------------------------------------------------|:-------------------------------------------------------------------|:--------------------------------------------------------------------|-----------------------------------------------------:|------------------------------------:|
| Alabama              | 3.13967%                                                          | 31.39673%                                                          | 313.96735%                                                          |                                                 5498 |                              153944 |
| Alaska               | 1.55397%                                                          | 15.53971%                                                          | 155.39714%                                                          |                                                  406 |                               11368 |
| Arizona              | 4.48464%                                                          | 44.84637%                                                          | 448.46365%                                                          |                                                11658 |                              326424 |
| Arkansas             | 3.81059%                                                          | 38.10585%                                                          | 381.05854%                                                          |                                                 4107 |                              114996 |
| California           | 3.73001%                                                          | 37.30005%                                                          | 373.00053%                                                          |                                                52636 |                             1473808 |
| Colorado             | 1.68863%                                                          | 16.88634%                                                          | 168.86345%                                                          |                                                 3473 |                               97244 |
| Connecticut          | 5.78332%                                                          | 57.83321%                                                          | 578.33212%                                                          |                                                 7364 |                              206192 |
| Delaware             | 3.50804%                                                          | 35.08037%                                                          | 350.80369%                                                          |                                                 1220 |                               34160 |
| Florida              | 2.52053%                                                          | 25.20526%                                                          | 252.05263%                                                          |                                                19334 |                              541352 |
| Georgia              | 2.73712%                                                          | 27.37124%                                                          | 273.71237%                                                          |                                                10379 |                              290612 |
| Hawaii               | 0.63480%                                                          | 6.34803%                                                           | 63.48031%                                                           |                                                  321 |                                8988 |
| Idaho                | 2.40976%                                                          | 24.09761%                                                          | 240.97613%                                                          |                                                 1538 |                               43064 |
| Illinois             | 2.04987%                                                          | 20.49871%                                                          | 204.98711%                                                          |                                                 9277 |                              259756 |
| Indiana              | 3.02367%                                                          | 30.23669%                                                          | 302.36687%                                                          |                                                 7270 |                              203560 |
| Iowa                 | 1.78380%                                                          | 17.83796%                                                          | 178.37956%                                                          |                                                 2010 |                               56280 |
| Kansas               | 5.28992%                                                          | 52.89921%                                                          | 528.99207%                                                          |                                                 5504 |                              154112 |
| Kentucky             | 3.57546%                                                          | 35.75463%                                                          | 357.54631%                                                          |                                                 5705 |                              159740 |
| Louisiana            | 4.14146%                                                          | 41.41461%                                                          | 414.14612%                                                          |                                                 6876 |                              192528 |
| Maine                | 1.71640%                                                          | 17.16396%                                                          | 171.63959%                                                          |                                                  824 |                               23072 |
| Maryland             | 1.74048%                                                          | 17.40482%                                                          | 174.04825%                                                          |                                                 3758 |                              105224 |
| Massachusetts        | 3.29866%                                                          | 32.98657%                                                          | 329.86565%                                                          |                                                 8120 |                              227360 |
| Michigan             | 1.43801%                                                          | 14.38010%                                                          | 143.80100%                                                          |                                                 5129 |                              143612 |
| Minnesota            | 1.22582%                                                          | 12.25825%                                                          | 122.58247%                                                          |                                                 2469 |                               69132 |
| Mississippi          | 3.06235%                                                          | 30.62347%                                                          | 306.23467%                                                          |                                                 3255 |                               91140 |
| Missouri             | 1.97633%                                                          | 19.76333%                                                          | 197.63328%                                                          |                                                 4332 |                              121296 |
| Montana              | 2.14301%                                                          | 21.43008%                                                          | 214.30082%                                                          |                                                  818 |                               22904 |
| Nebraska             | 2.21318%                                                          | 22.13184%                                                          | 221.31836%                                                          |                                                 1529 |                               42812 |
| Nevada               | 3.09257%                                                          | 30.92571%                                                          | 309.25706%                                                          |                                                 3402 |                               95256 |
| New Hampshire        | 2.05926%                                                          | 20.59261%                                                          | 205.92611%                                                          |                                                 1000 |                               28000 |
| New Jersey           | 2.48407%                                                          | 24.84072%                                                          | 248.40721%                                                          |                                                 7880 |                              220640 |
| New Mexico           | 2.45037%                                                          | 24.50367%                                                          | 245.03667%                                                          |                                                 1835 |                               51380 |
| New York             | 2.87030%                                                          | 28.70302%                                                          | 287.03023%                                                          |                                                19942 |                              558376 |
| North Carolina       | 3.09178%                                                          | 30.91775%                                                          | 309.17754%                                                          |                                                11581 |                              324268 |
| North Dakota         | 1.24189%                                                          | 12.41894%                                                          | 124.18937%                                                          |                                                  338 |                                9464 |
| Ohio                 | 2.45552%                                                          | 24.55518%                                                          | 245.55184%                                                          |                                                10251 |                              287028 |
| Oklahoma             | 4.59028%                                                          | 45.90279%                                                          | 459.02788%                                                          |                                                 6487 |                              181636 |
| Oregon               | 1.16973%                                                          | 11.69727%                                                          | 116.97268%                                                          |                                                 1762 |                               49336 |
| Pennsylvania         | 2.22609%                                                          | 22.26092%                                                          | 222.60916%                                                          |                                                10178 |                              284984 |
| Rhode Island         | 4.25804%                                                          | 42.58039%                                                          | 425.80386%                                                          |                                                 1611 |                               45108 |
| South Carolina       | 3.51039%                                                          | 35.10391%                                                          | 351.03911%                                                          |                                                 6455 |                              180740 |
| South Dakota         | 1.92436%                                                          | 19.24357%                                                          | 192.43573%                                                          |                                                  608 |                               17024 |
| Tennessee            | 3.69005%                                                          | 36.90051%                                                          | 369.00509%                                                          |                                                 9000 |                              252000 |
| Texas                | 3.05436%                                                          | 30.54365%                                                          | 305.43649%                                                          |                                                31630 |                              885640 |
| Utah                 | 4.53106%                                                          | 45.31064%                                                          | 453.10637%                                                          |                                                 5188 |                              145264 |
| Vermont              | 1.09938%                                                          | 10.99378%                                                          | 109.93784%                                                          |                                                  245 |                                6860 |
| Virginia             | 3.25220%                                                          | 32.52198%                                                          | 325.21983%                                                          |                                                 9914 |                              277592 |
| Washington           | 1.87196%                                                          | 18.71963%                                                          | 187.19633%                                                          |                                                 5091 |                              142548 |
| West Virginia        | 2.96226%                                                          | 29.62257%                                                          | 296.22570%                                                          |                                                 1896 |                               53088 |
| Wisconsin            | 2.16837%                                                          | 21.68372%                                                          | 216.83715%                                                          |                                                 4509 |                              126252 |
| Wyoming              | 3.27528%                                                          | 32.75284%                                                          | 327.52838%                                                          |                                                  677 |                               18956 |
| Puerto Rico          | 1.90162%                                                          | 19.01622%                                                          | 190.16224%                                                          |                                                 2169 |                               60732 |
| District of Columbia | 1.70599%                                                          | 17.05989%                                                          | 170.59890%                                                          |                                                  430 |                               12040 |