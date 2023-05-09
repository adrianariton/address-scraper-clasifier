TRAINING_DATA2 = [
(
"Virginia VA 540-809-7456 22401 Fredericksburg 3316 Meadowview Drive 434-250-3816"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 11, "STATE"),
(12, 24, "TELEPHONE_NUMBER"),
(25, 30, "ZIPCODE"),
(31, 45, "CITY"),
(46, 67, "STREET_ADDRESS"),
(68, 80, "MOBILE_NUMBER"),
]
}),
(
"540-809-7456 Virginia 3316 Meadowview Drive Fredericksburg VA 434-250-3816 22401"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 21, "STATE_FULL"),
(22, 43, "STREET_ADDRESS"),
(44, 58, "CITY"),
(59, 61, "STATE"),
(62, 74, "MOBILE_NUMBER"),
(75, 80, "ZIPCODE"),
]
}),
(
"540-809-7456 Fredericksburg VA 3316 Meadowview Drive 434-250-3816 Virginia 22401"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 27, "CITY"),
(28, 30, "STATE"),
(31, 52, "STREET_ADDRESS"),
(53, 65, "MOBILE_NUMBER"),
(66, 74, "STATE_FULL"),
(75, 80, "ZIPCODE"),
]
}),
(
"3316 Meadowview Drive Virginia VA 540-809-7456 Fredericksburg 22401 434-250-3816"
, {
"entities":[
(0, 21, "STREET_ADDRESS"),
(22, 30, "STATE_FULL"),
(31, 33, "STATE"),
(34, 46, "TELEPHONE_NUMBER"),
(47, 61, "CITY"),
(62, 67, "ZIPCODE"),
(68, 80, "MOBILE_NUMBER"),
]
}),
(
"540-809-7456 VA Fredericksburg Virginia 434-250-3816 22401 3316 Meadowview Drive"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 15, "STATE"),
(16, 30, "CITY"),
(31, 39, "STATE_FULL"),
(40, 52, "MOBILE_NUMBER"),
(53, 58, "ZIPCODE"),
(59, 80, "STREET_ADDRESS"),
]
}),
(
"540-809-7456 Fredericksburg 22401 434-250-3816 VA 3316 Meadowview Drive Virginia"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 27, "CITY"),
(28, 33, "ZIPCODE"),
(34, 46, "MOBILE_NUMBER"),
(47, 49, "STATE"),
(50, 71, "STREET_ADDRESS"),
(72, 80, "STATE_FULL"),
]
}),
(
"3316 Meadowview Drive 540-809-7456 434-250-3816 Virginia VA 22401 Fredericksburg"
, {
"entities":[
(0, 21, "STREET_ADDRESS"),
(22, 34, "TELEPHONE_NUMBER"),
(35, 47, "MOBILE_NUMBER"),
(48, 56, "STATE_FULL"),
(57, 59, "STATE"),
(60, 65, "ZIPCODE"),
(66, 80, "CITY"),
]
}),
(
"540-809-7456 Virginia Fredericksburg 22401 434-250-3816 3316 Meadowview Drive VA"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 21, "STATE_FULL"),
(22, 36, "CITY"),
(37, 42, "ZIPCODE"),
(43, 55, "MOBILE_NUMBER"),
(56, 77, "STREET_ADDRESS"),
(78, 80, "STATE"),
]
}),
(
"540-809-7456 434-250-3816 Virginia 3316 Meadowview Drive VA 22401 Fredericksburg"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 25, "MOBILE_NUMBER"),
(26, 34, "STATE_FULL"),
(35, 56, "STREET_ADDRESS"),
(57, 59, "STATE"),
(60, 65, "ZIPCODE"),
(66, 80, "CITY"),
]
}),
(
"22401 VA 434-250-3816 Virginia 540-809-7456 3316 Meadowview Drive Fredericksburg"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 21, "MOBILE_NUMBER"),
(22, 30, "STATE_FULL"),
(31, 43, "TELEPHONE_NUMBER"),
(44, 65, "STREET_ADDRESS"),
(66, 80, "CITY"),
]
}),
(
"713-592-5335 TX 832-453-7456 728 Gore Street 77025 Houston Texas"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 15, "STATE"),
(16, 28, "MOBILE_NUMBER"),
(29, 44, "STREET_ADDRESS"),
(45, 50, "ZIPCODE"),
(51, 58, "CITY"),
(59, 64, "STATE_FULL"),
]
}),
(
"728 Gore Street 832-453-7456 713-592-5335 77025 Texas TX Houston"
, {
"entities":[
(0, 15, "STREET_ADDRESS"),
(16, 28, "MOBILE_NUMBER"),
(29, 41, "TELEPHONE_NUMBER"),
(42, 47, "ZIPCODE"),
(48, 53, "STATE_FULL"),
(54, 56, "STATE"),
(57, 64, "CITY"),
]
}),
(
"77025 832-453-7456 713-592-5335 728 Gore Street Texas Houston TX"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "MOBILE_NUMBER"),
(19, 31, "TELEPHONE_NUMBER"),
(32, 47, "STREET_ADDRESS"),
(48, 53, "STATE_FULL"),
(54, 61, "CITY"),
(62, 64, "STATE"),
]
}),
(
"832-453-7456 TX 728 Gore Street Texas 77025 713-592-5335 Houston"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 15, "STATE"),
(16, 31, "STREET_ADDRESS"),
(32, 37, "STATE_FULL"),
(38, 43, "ZIPCODE"),
(44, 56, "TELEPHONE_NUMBER"),
(57, 64, "CITY"),
]
}),
(
"TX 728 Gore Street Houston Texas 832-453-7456 77025 713-592-5335"
, {
"entities":[
(0, 2, "STATE"),
(3, 18, "STREET_ADDRESS"),
(19, 26, "CITY"),
(27, 32, "STATE_FULL"),
(33, 45, "MOBILE_NUMBER"),
(46, 51, "ZIPCODE"),
(52, 64, "TELEPHONE_NUMBER"),
]
}),
(
"Texas 713-592-5335 TX 728 Gore Street 77025 Houston 832-453-7456"
, {
"entities":[
(0, 5, "STATE_FULL"),
(6, 18, "TELEPHONE_NUMBER"),
(19, 21, "STATE"),
(22, 37, "STREET_ADDRESS"),
(38, 43, "ZIPCODE"),
(44, 51, "CITY"),
(52, 64, "MOBILE_NUMBER"),
]
}),
(
"Texas 713-592-5335 77025 Houston 832-453-7456 TX 728 Gore Street"
, {
"entities":[
(0, 5, "STATE_FULL"),
(6, 18, "TELEPHONE_NUMBER"),
(19, 24, "ZIPCODE"),
(25, 32, "CITY"),
(33, 45, "MOBILE_NUMBER"),
(46, 48, "STATE"),
(49, 64, "STREET_ADDRESS"),
]
}),
(
"TX 77025 832-453-7456 713-592-5335 728 Gore Street Houston Texas"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 21, "MOBILE_NUMBER"),
(22, 34, "TELEPHONE_NUMBER"),
(35, 50, "STREET_ADDRESS"),
(51, 58, "CITY"),
(59, 64, "STATE_FULL"),
]
}),
(
"728 Gore Street TX Texas Houston 77025 832-453-7456 713-592-5335"
, {
"entities":[
(0, 15, "STREET_ADDRESS"),
(16, 18, "STATE"),
(19, 24, "STATE_FULL"),
(25, 32, "CITY"),
(33, 38, "ZIPCODE"),
(39, 51, "MOBILE_NUMBER"),
(52, 64, "TELEPHONE_NUMBER"),
]
}),
(
"713-592-5335 77025 Houston Texas 832-453-7456 TX 728 Gore Street"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 26, "CITY"),
(27, 32, "STATE_FULL"),
(33, 45, "MOBILE_NUMBER"),
(46, 48, "STATE"),
(49, 64, "STREET_ADDRESS"),
]
}),
(
"1758 Hillcrest Circle 612-239-3225 Minnesota MN 763-550-6336 55446 Plymouth in"
, {
"entities":[
(0, 21, "STREET_ADDRESS"),
(22, 34, "MOBILE_NUMBER"),
(35, 44, "STATE_FULL"),
(45, 47, "STATE"),
(48, 60, "TELEPHONE_NUMBER"),
(61, 66, "ZIPCODE"),
(67, 75, "CITY"),
]
}),
(
"612-239-3225 55446 Minnesota in 763-550-6336 MN 1758 Hillcrest Circle Plymouth"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 28, "STATE_FULL"),
(32, 44, "TELEPHONE_NUMBER"),
(45, 47, "STATE"),
(48, 69, "STREET_ADDRESS"),
(70, 78, "CITY"),
]
}),
(
"Plymouth Minnesota 763-550-6336 1758 Hillcrest Circle in 55446 MN 612-239-3225"
, {
"entities":[
(0, 8, "CITY"),
(9, 18, "STATE_FULL"),
(19, 31, "TELEPHONE_NUMBER"),
(32, 53, "STREET_ADDRESS"),
(57, 62, "ZIPCODE"),
(63, 65, "STATE"),
(66, 78, "MOBILE_NUMBER"),
]
}),
(
"55446 Minnesota MN 1758 Hillcrest Circle 612-239-3225 763-550-6336 Plymouth in"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 15, "STATE_FULL"),
(16, 18, "STATE"),
(19, 40, "STREET_ADDRESS"),
(41, 53, "MOBILE_NUMBER"),
(54, 66, "TELEPHONE_NUMBER"),
(67, 75, "CITY"),
]
}),
(
"Plymouth in 1758 Hillcrest Circle 55446 612-239-3225 MN 763-550-6336 Minnesota"
, {
"entities":[
(0, 8, "CITY"),
(12, 33, "STREET_ADDRESS"),
(34, 39, "ZIPCODE"),
(40, 52, "MOBILE_NUMBER"),
(53, 55, "STATE"),
(56, 68, "TELEPHONE_NUMBER"),
(69, 78, "STATE_FULL"),
]
}),
(
"1758 Hillcrest Circle in Minnesota 763-550-6336 MN 612-239-3225 Plymouth 55446"
, {
"entities":[
(0, 21, "STREET_ADDRESS"),
(25, 34, "STATE_FULL"),
(35, 47, "TELEPHONE_NUMBER"),
(48, 50, "STATE"),
(51, 63, "MOBILE_NUMBER"),
(64, 72, "CITY"),
(73, 78, "ZIPCODE"),
]
}),
(
"MN in 55446 1758 Hillcrest Circle Minnesota Plymouth 763-550-6336 612-239-3225"
, {
"entities":[
(0, 2, "STATE"),
(6, 11, "ZIPCODE"),
(12, 33, "STREET_ADDRESS"),
(34, 43, "STATE_FULL"),
(44, 52, "CITY"),
(53, 65, "TELEPHONE_NUMBER"),
(66, 78, "MOBILE_NUMBER"),
]
}),
(
"in 763-550-6336 1758 Hillcrest Circle Plymouth 55446 Minnesota MN 612-239-3225"
, {
"entities":[
(3, 15, "TELEPHONE_NUMBER"),
(16, 37, "STREET_ADDRESS"),
(38, 46, "CITY"),
(47, 52, "ZIPCODE"),
(53, 62, "STATE_FULL"),
(63, 65, "STATE"),
(66, 78, "MOBILE_NUMBER"),
]
}),
(
"MN 55446 612-239-3225 763-550-6336 1758 Hillcrest Circle Plymouth Minnesota in"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 21, "MOBILE_NUMBER"),
(22, 34, "TELEPHONE_NUMBER"),
(35, 56, "STREET_ADDRESS"),
(57, 65, "CITY"),
(66, 75, "STATE_FULL"),
]
}),
(
"Plymouth MN 1758 Hillcrest Circle 612-239-3225 55446 763-550-6336 Minnesota in"
, {
"entities":[
(0, 8, "CITY"),
(9, 11, "STATE"),
(12, 33, "STREET_ADDRESS"),
(34, 46, "MOBILE_NUMBER"),
(47, 52, "ZIPCODE"),
(53, 65, "TELEPHONE_NUMBER"),
(66, 75, "STATE_FULL"),
]
}),
(
"Tallahassee 850-309-8780 352-412-7987 FL 32301 Florida 1271 Star Trek Drive"
, {
"entities":[
(0, 11, "CITY"),
(12, 24, "TELEPHONE_NUMBER"),
(25, 37, "MOBILE_NUMBER"),
(38, 40, "STATE"),
(41, 46, "ZIPCODE"),
(47, 54, "STATE_FULL"),
(55, 75, "STREET_ADDRESS"),
]
}),
(
"1271 Star Trek Drive 352-412-7987 32301 Tallahassee 850-309-8780 FL Florida"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 33, "MOBILE_NUMBER"),
(34, 39, "ZIPCODE"),
(40, 51, "CITY"),
(52, 64, "TELEPHONE_NUMBER"),
(65, 67, "STATE"),
(68, 75, "STATE_FULL"),
]
}),
(
"FL Florida 32301 1271 Star Trek Drive 352-412-7987 850-309-8780 Tallahassee"
, {
"entities":[
(0, 2, "STATE"),
(3, 10, "STATE_FULL"),
(11, 16, "ZIPCODE"),
(17, 37, "STREET_ADDRESS"),
(38, 50, "MOBILE_NUMBER"),
(51, 63, "TELEPHONE_NUMBER"),
(64, 75, "CITY"),
]
}),
(
"352-412-7987 1271 Star Trek Drive Tallahassee FL Florida 32301 850-309-8780"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 33, "STREET_ADDRESS"),
(34, 45, "CITY"),
(46, 48, "STATE"),
(49, 56, "STATE_FULL"),
(57, 62, "ZIPCODE"),
(63, 75, "TELEPHONE_NUMBER"),
]
}),
(
"850-309-8780 Florida 32301 Tallahassee 352-412-7987 1271 Star Trek Drive FL"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 20, "STATE_FULL"),
(21, 26, "ZIPCODE"),
(27, 38, "CITY"),
(39, 51, "MOBILE_NUMBER"),
(52, 72, "STREET_ADDRESS"),
(73, 75, "STATE"),
]
}),
(
"352-412-7987 Tallahassee Florida FL 850-309-8780 1271 Star Trek Drive 32301"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 24, "CITY"),
(25, 32, "STATE_FULL"),
(33, 35, "STATE"),
(36, 48, "TELEPHONE_NUMBER"),
(49, 69, "STREET_ADDRESS"),
(70, 75, "ZIPCODE"),
]
}),
(
"Florida Tallahassee 1271 Star Trek Drive 32301 352-412-7987 FL 850-309-8780"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 19, "CITY"),
(20, 40, "STREET_ADDRESS"),
(41, 46, "ZIPCODE"),
(47, 59, "MOBILE_NUMBER"),
(60, 62, "STATE"),
(63, 75, "TELEPHONE_NUMBER"),
]
}),
(
"Florida 850-309-8780 1271 Star Trek Drive 352-412-7987 32301 Tallahassee FL"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 20, "TELEPHONE_NUMBER"),
(21, 41, "STREET_ADDRESS"),
(42, 54, "MOBILE_NUMBER"),
(55, 60, "ZIPCODE"),
(61, 72, "CITY"),
(73, 75, "STATE"),
]
}),
(
"FL 352-412-7987 850-309-8780 32301 Tallahassee Florida 1271 Star Trek Drive"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "MOBILE_NUMBER"),
(16, 28, "TELEPHONE_NUMBER"),
(29, 34, "ZIPCODE"),
(35, 46, "CITY"),
(47, 54, "STATE_FULL"),
(55, 75, "STREET_ADDRESS"),
]
}),
(
"Tallahassee 1271 Star Trek Drive FL Florida 32301 850-309-8780 352-412-7987"
, {
"entities":[
(0, 11, "CITY"),
(12, 32, "STREET_ADDRESS"),
(33, 35, "STATE"),
(36, 43, "STATE_FULL"),
(44, 49, "ZIPCODE"),
(50, 62, "TELEPHONE_NUMBER"),
(63, 75, "MOBILE_NUMBER"),
]
}),
(
"614-354-6902 OH Columbus 43215 Ohio 740-734-0528 2986 Viking Drive"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 15, "STATE"),
(16, 24, "CITY"),
(25, 30, "ZIPCODE"),
(31, 35, "STATE_FULL"),
(36, 48, "TELEPHONE_NUMBER"),
(49, 66, "STREET_ADDRESS"),
]
}),
(
"43215 740-734-0528 Ohio 614-354-6902 Columbus 2986 Viking Drive OH"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "TELEPHONE_NUMBER"),
(19, 23, "STATE_FULL"),
(24, 36, "MOBILE_NUMBER"),
(37, 45, "CITY"),
(46, 63, "STREET_ADDRESS"),
(64, 66, "STATE"),
]
}),
(
"OH Columbus 2986 Viking Drive 43215 614-354-6902 Ohio 740-734-0528"
, {
"entities":[
(0, 2, "STATE"),
(3, 11, "CITY"),
(12, 29, "STREET_ADDRESS"),
(30, 35, "ZIPCODE"),
(36, 48, "MOBILE_NUMBER"),
(49, 53, "STATE_FULL"),
(54, 66, "TELEPHONE_NUMBER"),
]
}),
(
"OH 740-734-0528 43215 Columbus 2986 Viking Drive 614-354-6902 Ohio"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "TELEPHONE_NUMBER"),
(16, 21, "ZIPCODE"),
(22, 30, "CITY"),
(31, 48, "STREET_ADDRESS"),
(49, 61, "MOBILE_NUMBER"),
(62, 66, "STATE_FULL"),
]
}),
(
"614-354-6902 OH 2986 Viking Drive Columbus 43215 740-734-0528 Ohio"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 15, "STATE"),
(16, 33, "STREET_ADDRESS"),
(34, 42, "CITY"),
(43, 48, "ZIPCODE"),
(49, 61, "TELEPHONE_NUMBER"),
(62, 66, "STATE_FULL"),
]
}),
(
"740-734-0528 614-354-6902 OH Columbus Ohio 43215 2986 Viking Drive"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 25, "MOBILE_NUMBER"),
(26, 28, "STATE"),
(29, 37, "CITY"),
(38, 42, "STATE_FULL"),
(43, 48, "ZIPCODE"),
(49, 66, "STREET_ADDRESS"),
]
}),
(
"740-734-0528 2986 Viking Drive Columbus OH 614-354-6902 Ohio 43215"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 30, "STREET_ADDRESS"),
(31, 39, "CITY"),
(40, 42, "STATE"),
(43, 55, "MOBILE_NUMBER"),
(56, 60, "STATE_FULL"),
(61, 66, "ZIPCODE"),
]
}),
(
"Ohio Columbus 740-734-0528 OH 614-354-6902 2986 Viking Drive 43215"
, {
"entities":[
(0, 4, "STATE_FULL"),
(5, 13, "CITY"),
(14, 26, "TELEPHONE_NUMBER"),
(27, 29, "STATE"),
(30, 42, "MOBILE_NUMBER"),
(43, 60, "STREET_ADDRESS"),
(61, 66, "ZIPCODE"),
]
}),
(
"614-354-6902 43215 Columbus 2986 Viking Drive 740-734-0528 OH Ohio"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 27, "CITY"),
(28, 45, "STREET_ADDRESS"),
(46, 58, "TELEPHONE_NUMBER"),
(59, 61, "STATE"),
(62, 66, "STATE_FULL"),
]
}),
(
"2986 Viking Drive Columbus Ohio OH 740-734-0528 614-354-6902 43215"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 26, "CITY"),
(27, 31, "STATE_FULL"),
(32, 34, "STATE"),
(35, 47, "TELEPHONE_NUMBER"),
(48, 60, "MOBILE_NUMBER"),
(61, 66, "ZIPCODE"),
]
}),
(
"Texas that 2013 Giraffe Hill Drive TX 979-753-1426 Richardson 75081 972-238-9254"
, {
"entities":[
(0, 5, "STATE_FULL"),
(11, 34, "STREET_ADDRESS"),
(35, 37, "STATE"),
(38, 50, "MOBILE_NUMBER"),
(51, 61, "CITY"),
(62, 67, "ZIPCODE"),
(68, 80, "TELEPHONE_NUMBER"),
]
}),
(
"Texas 2013 Giraffe Hill Drive Richardson TX 979-753-1426 75081 972-238-9254 that"
, {
"entities":[
(0, 5, "STATE_FULL"),
(6, 29, "STREET_ADDRESS"),
(30, 40, "CITY"),
(41, 43, "STATE"),
(44, 56, "MOBILE_NUMBER"),
(57, 62, "ZIPCODE"),
(63, 75, "TELEPHONE_NUMBER"),
]
}),
(
"2013 Giraffe Hill Drive TX Texas that Richardson 979-753-1426 75081 972-238-9254"
, {
"entities":[
(0, 23, "STREET_ADDRESS"),
(24, 26, "STATE"),
(27, 32, "STATE_FULL"),
(38, 48, "CITY"),
(49, 61, "MOBILE_NUMBER"),
(62, 67, "ZIPCODE"),
(68, 80, "TELEPHONE_NUMBER"),
]
}),
(
"972-238-9254 TX 2013 Giraffe Hill Drive that Richardson 75081 Texas 979-753-1426"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 15, "STATE"),
(16, 39, "STREET_ADDRESS"),
(45, 55, "CITY"),
(56, 61, "ZIPCODE"),
(62, 67, "STATE_FULL"),
(68, 80, "MOBILE_NUMBER"),
]
}),
(
"Texas TX Richardson 2013 Giraffe Hill Drive that 979-753-1426 972-238-9254 75081"
, {
"entities":[
(0, 5, "STATE_FULL"),
(6, 8, "STATE"),
(9, 19, "CITY"),
(20, 43, "STREET_ADDRESS"),
(49, 61, "MOBILE_NUMBER"),
(62, 74, "TELEPHONE_NUMBER"),
(75, 80, "ZIPCODE"),
]
}),
(
"that 979-753-1426 Richardson 75081 Texas TX 972-238-9254 2013 Giraffe Hill Drive"
, {
"entities":[
(5, 17, "MOBILE_NUMBER"),
(18, 28, "CITY"),
(29, 34, "ZIPCODE"),
(35, 40, "STATE_FULL"),
(41, 43, "STATE"),
(44, 56, "TELEPHONE_NUMBER"),
(57, 80, "STREET_ADDRESS"),
]
}),
(
"979-753-1426 Richardson Texas that 972-238-9254 TX 75081 2013 Giraffe Hill Drive"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 23, "CITY"),
(24, 29, "STATE_FULL"),
(35, 47, "TELEPHONE_NUMBER"),
(48, 50, "STATE"),
(51, 56, "ZIPCODE"),
(57, 80, "STREET_ADDRESS"),
]
}),
(
"that 75081 TX Texas 979-753-1426 2013 Giraffe Hill Drive 972-238-9254 Richardson"
, {
"entities":[
(5, 10, "ZIPCODE"),
(11, 13, "STATE"),
(14, 19, "STATE_FULL"),
(20, 32, "MOBILE_NUMBER"),
(33, 56, "STREET_ADDRESS"),
(57, 69, "TELEPHONE_NUMBER"),
(70, 80, "CITY"),
]
}),
(
"Texas 2013 Giraffe Hill Drive 979-753-1426 75081 972-238-9254 Richardson that TX"
, {
"entities":[
(0, 5, "STATE_FULL"),
(6, 29, "STREET_ADDRESS"),
(30, 42, "MOBILE_NUMBER"),
(43, 48, "ZIPCODE"),
(49, 61, "TELEPHONE_NUMBER"),
(62, 72, "CITY"),
(78, 80, "STATE"),
]
}),
(
"Richardson 75081 2013 Giraffe Hill Drive 972-238-9254 TX that 979-753-1426 Texas"
, {
"entities":[
(0, 10, "CITY"),
(11, 16, "ZIPCODE"),
(17, 40, "STREET_ADDRESS"),
(41, 53, "TELEPHONE_NUMBER"),
(54, 56, "STATE"),
(62, 74, "MOBILE_NUMBER"),
(75, 80, "STATE_FULL"),
]
}),
(
"286 Rebecca Street Park Ridge 847-696-3652 60068 Illinois IL 847-207-8493"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 29, "CITY"),
(30, 42, "TELEPHONE_NUMBER"),
(43, 48, "ZIPCODE"),
(49, 57, "STATE_FULL"),
(58, 60, "STATE"),
(61, 73, "MOBILE_NUMBER"),
]
}),
(
"60068 Park Ridge 847-696-3652 Illinois 847-207-8493 286 Rebecca Street IL"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 16, "CITY"),
(17, 29, "TELEPHONE_NUMBER"),
(30, 38, "STATE_FULL"),
(39, 51, "MOBILE_NUMBER"),
(52, 70, "STREET_ADDRESS"),
(71, 73, "STATE"),
]
}),
(
"286 Rebecca Street 60068 847-696-3652 IL 847-207-8493 Illinois Park Ridge"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 24, "ZIPCODE"),
(25, 37, "TELEPHONE_NUMBER"),
(38, 40, "STATE"),
(41, 53, "MOBILE_NUMBER"),
(54, 62, "STATE_FULL"),
(63, 73, "CITY"),
]
}),
(
"Park Ridge 847-207-8493 847-696-3652 IL 60068 Illinois 286 Rebecca Street"
, {
"entities":[
(0, 10, "CITY"),
(11, 23, "MOBILE_NUMBER"),
(24, 36, "TELEPHONE_NUMBER"),
(37, 39, "STATE"),
(40, 45, "ZIPCODE"),
(46, 54, "STATE_FULL"),
(55, 73, "STREET_ADDRESS"),
]
}),
(
"IL Illinois 60068 847-207-8493 Park Ridge 847-696-3652 286 Rebecca Street"
, {
"entities":[
(0, 2, "STATE"),
(3, 11, "STATE_FULL"),
(12, 17, "ZIPCODE"),
(18, 30, "MOBILE_NUMBER"),
(31, 41, "CITY"),
(42, 54, "TELEPHONE_NUMBER"),
(55, 73, "STREET_ADDRESS"),
]
}),
(
"847-696-3652 847-207-8493 Illinois 286 Rebecca Street 60068 Park Ridge IL"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 25, "MOBILE_NUMBER"),
(26, 34, "STATE_FULL"),
(35, 53, "STREET_ADDRESS"),
(54, 59, "ZIPCODE"),
(60, 70, "CITY"),
(71, 73, "STATE"),
]
}),
(
"Illinois 60068 286 Rebecca Street 847-207-8493 IL 847-696-3652 Park Ridge"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 14, "ZIPCODE"),
(15, 33, "STREET_ADDRESS"),
(34, 46, "MOBILE_NUMBER"),
(47, 49, "STATE"),
(50, 62, "TELEPHONE_NUMBER"),
(63, 73, "CITY"),
]
}),
(
"Illinois 286 Rebecca Street 847-696-3652 60068 847-207-8493 Park Ridge IL"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 27, "STREET_ADDRESS"),
(28, 40, "TELEPHONE_NUMBER"),
(41, 46, "ZIPCODE"),
(47, 59, "MOBILE_NUMBER"),
(60, 70, "CITY"),
(71, 73, "STATE"),
]
}),
(
"60068 Park Ridge 286 Rebecca Street 847-696-3652 Illinois 847-207-8493 IL"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 16, "CITY"),
(17, 35, "STREET_ADDRESS"),
(36, 48, "TELEPHONE_NUMBER"),
(49, 57, "STATE_FULL"),
(58, 70, "MOBILE_NUMBER"),
(71, 73, "STATE"),
]
}),
(
"Illinois 60068 Park Ridge 286 Rebecca Street IL 847-207-8493 847-696-3652"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 14, "ZIPCODE"),
(15, 25, "CITY"),
(26, 44, "STREET_ADDRESS"),
(45, 47, "STATE"),
(48, 60, "MOBILE_NUMBER"),
(61, 73, "TELEPHONE_NUMBER"),
]
}),
(
"NY 212-298-7580 917-457-6877 10007 New York New York 1378 Farnum Road"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "TELEPHONE_NUMBER"),
(16, 28, "MOBILE_NUMBER"),
(29, 34, "ZIPCODE"),
(35, 43, "CITY"),
(44, 52, "STATE_FULL"),
(53, 69, "STREET_ADDRESS"),
]
}),
(
"New York New York 10007 1378 Farnum Road 917-457-6877 NY 212-298-7580"
, {
"entities":[
(0, 8, "CITY"),
(9, 17, "STATE_FULL"),
(18, 23, "ZIPCODE"),
(24, 40, "STREET_ADDRESS"),
(41, 53, "MOBILE_NUMBER"),
(54, 56, "STATE"),
(57, 69, "TELEPHONE_NUMBER"),
]
}),
(
"212-298-7580 917-457-6877 1378 Farnum Road NY New York 10007 New York"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 25, "MOBILE_NUMBER"),
(26, 42, "STREET_ADDRESS"),
(43, 45, "STATE"),
(46, 54, "CITY"),
(55, 60, "ZIPCODE"),
(61, 69, "STATE_FULL"),
]
}),
(
"917-457-6877 212-298-7580 New York New York 1378 Farnum Road 10007 NY"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 25, "TELEPHONE_NUMBER"),
(26, 34, "STATE_FULL"),
(35, 43, "CITY"),
(44, 60, "STREET_ADDRESS"),
(61, 66, "ZIPCODE"),
(67, 69, "STATE"),
]
}),
(
"New York 1378 Farnum Road NY New York 10007 917-457-6877 212-298-7580"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 25, "STREET_ADDRESS"),
(26, 28, "STATE"),
(29, 37, "CITY"),
(38, 43, "ZIPCODE"),
(44, 56, "MOBILE_NUMBER"),
(57, 69, "TELEPHONE_NUMBER"),
]
}),
(
"212-298-7580 New York 917-457-6877 10007 NY 1378 Farnum Road New York"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 21, "CITY"),
(22, 34, "MOBILE_NUMBER"),
(35, 40, "ZIPCODE"),
(41, 43, "STATE"),
(44, 60, "STREET_ADDRESS"),
(61, 69, "STATE_FULL"),
]
}),
(
"1378 Farnum Road New York 212-298-7580 10007 New York 917-457-6877 NY"
, {
"entities":[
(0, 16, "STREET_ADDRESS"),
(17, 25, "STATE_FULL"),
(26, 38, "TELEPHONE_NUMBER"),
(39, 44, "ZIPCODE"),
(45, 53, "CITY"),
(54, 66, "MOBILE_NUMBER"),
(67, 69, "STATE"),
]
}),
(
"New York 10007 917-457-6877 1378 Farnum Road New York 212-298-7580 NY"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 14, "ZIPCODE"),
(15, 27, "MOBILE_NUMBER"),
(28, 44, "STREET_ADDRESS"),
(45, 53, "CITY"),
(54, 66, "TELEPHONE_NUMBER"),
(67, 69, "STATE"),
]
}),
(
"New York NY 10007 1378 Farnum Road New York 917-457-6877 212-298-7580"
, {
"entities":[
(0, 8, "CITY"),
(9, 11, "STATE"),
(12, 17, "ZIPCODE"),
(18, 34, "STREET_ADDRESS"),
(35, 43, "STATE_FULL"),
(44, 56, "MOBILE_NUMBER"),
(57, 69, "TELEPHONE_NUMBER"),
]
}),
(
"212-298-7580 NY 917-457-6877 New York 1378 Farnum Road 10007 New York"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 15, "STATE"),
(16, 28, "MOBILE_NUMBER"),
(29, 37, "CITY"),
(38, 54, "STREET_ADDRESS"),
(55, 60, "ZIPCODE"),
(61, 69, "STATE_FULL"),
]
}),
(
"86001 928-863-5915 928-779-0118 Arizona 2124 Martha Street Flagstaff AZ"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "MOBILE_NUMBER"),
(19, 31, "TELEPHONE_NUMBER"),
(32, 39, "STATE_FULL"),
(40, 58, "STREET_ADDRESS"),
(59, 68, "CITY"),
(69, 71, "STATE"),
]
}),
(
"2124 Martha Street 928-779-0118 AZ Flagstaff Arizona 86001 928-863-5915"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 31, "TELEPHONE_NUMBER"),
(32, 34, "STATE"),
(35, 44, "CITY"),
(45, 52, "STATE_FULL"),
(53, 58, "ZIPCODE"),
(59, 71, "MOBILE_NUMBER"),
]
}),
(
"Arizona AZ 928-779-0118 Flagstaff 2124 Martha Street 928-863-5915 86001"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 10, "STATE"),
(11, 23, "TELEPHONE_NUMBER"),
(24, 33, "CITY"),
(34, 52, "STREET_ADDRESS"),
(53, 65, "MOBILE_NUMBER"),
(66, 71, "ZIPCODE"),
]
}),
(
"Flagstaff 928-863-5915 86001 AZ 928-779-0118 Arizona 2124 Martha Street"
, {
"entities":[
(0, 9, "CITY"),
(10, 22, "MOBILE_NUMBER"),
(23, 28, "ZIPCODE"),
(29, 31, "STATE"),
(32, 44, "TELEPHONE_NUMBER"),
(45, 52, "STATE_FULL"),
(53, 71, "STREET_ADDRESS"),
]
}),
(
"Flagstaff 86001 928-779-0118 Arizona 928-863-5915 AZ 2124 Martha Street"
, {
"entities":[
(0, 9, "CITY"),
(10, 15, "ZIPCODE"),
(16, 28, "TELEPHONE_NUMBER"),
(29, 36, "STATE_FULL"),
(37, 49, "MOBILE_NUMBER"),
(50, 52, "STATE"),
(53, 71, "STREET_ADDRESS"),
]
}),
(
"86001 2124 Martha Street 928-779-0118 Flagstaff 928-863-5915 Arizona AZ"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 24, "STREET_ADDRESS"),
(25, 37, "TELEPHONE_NUMBER"),
(38, 47, "CITY"),
(48, 60, "MOBILE_NUMBER"),
(61, 68, "STATE_FULL"),
(69, 71, "STATE"),
]
}),
(
"928-779-0118 928-863-5915 86001 2124 Martha Street Arizona Flagstaff AZ"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 25, "MOBILE_NUMBER"),
(26, 31, "ZIPCODE"),
(32, 50, "STREET_ADDRESS"),
(51, 58, "STATE_FULL"),
(59, 68, "CITY"),
(69, 71, "STATE"),
]
}),
(
"Flagstaff AZ 2124 Martha Street 86001 Arizona 928-863-5915 928-779-0118"
, {
"entities":[
(0, 9, "CITY"),
(10, 12, "STATE"),
(13, 31, "STREET_ADDRESS"),
(32, 37, "ZIPCODE"),
(38, 45, "STATE_FULL"),
(46, 58, "MOBILE_NUMBER"),
(59, 71, "TELEPHONE_NUMBER"),
]
}),
(
"928-779-0118 928-863-5915 Arizona Flagstaff AZ 86001 2124 Martha Street"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 25, "MOBILE_NUMBER"),
(26, 33, "STATE_FULL"),
(34, 43, "CITY"),
(44, 46, "STATE"),
(47, 52, "ZIPCODE"),
(53, 71, "STREET_ADDRESS"),
]
}),
(
"AZ Flagstaff 86001 2124 Martha Street 928-779-0118 Arizona 928-863-5915"
, {
"entities":[
(0, 2, "STATE"),
(3, 12, "CITY"),
(13, 18, "ZIPCODE"),
(19, 37, "STREET_ADDRESS"),
(38, 50, "TELEPHONE_NUMBER"),
(51, 58, "STATE_FULL"),
(59, 71, "MOBILE_NUMBER"),
]
}),
(
"818-247-2569 4227 Oakway Lane Glendale 91204 818-913-2748 California free CA"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 29, "STREET_ADDRESS"),
(30, 38, "CITY"),
(39, 44, "ZIPCODE"),
(45, 57, "MOBILE_NUMBER"),
(58, 68, "STATE_FULL"),
(74, 76, "STATE"),
]
}),
(
"4227 Oakway Lane CA 818-913-2748 free 818-247-2569 91204 Glendale California"
, {
"entities":[
(0, 16, "STREET_ADDRESS"),
(17, 19, "STATE"),
(20, 32, "MOBILE_NUMBER"),
(38, 50, "TELEPHONE_NUMBER"),
(51, 56, "ZIPCODE"),
(57, 65, "CITY"),
(66, 76, "STATE_FULL"),
]
}),
(
"818-913-2748 91204 CA free California Glendale 818-247-2569 4227 Oakway Lane"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 21, "STATE"),
(27, 37, "STATE_FULL"),
(38, 46, "CITY"),
(47, 59, "TELEPHONE_NUMBER"),
(60, 76, "STREET_ADDRESS"),
]
}),
(
"California 91204 Glendale 4227 Oakway Lane 818-913-2748 818-247-2569 free CA"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 16, "ZIPCODE"),
(17, 25, "CITY"),
(26, 42, "STREET_ADDRESS"),
(43, 55, "MOBILE_NUMBER"),
(56, 68, "TELEPHONE_NUMBER"),
(74, 76, "STATE"),
]
}),
(
"CA free Glendale 91204 818-247-2569 California 818-913-2748 4227 Oakway Lane"
, {
"entities":[
(0, 2, "STATE"),
(8, 16, "CITY"),
(17, 22, "ZIPCODE"),
(23, 35, "TELEPHONE_NUMBER"),
(36, 46, "STATE_FULL"),
(47, 59, "MOBILE_NUMBER"),
(60, 76, "STREET_ADDRESS"),
]
}),
(
"California free 91204 CA 818-913-2748 4227 Oakway Lane 818-247-2569 Glendale"
, {
"entities":[
(0, 10, "STATE_FULL"),
(16, 21, "ZIPCODE"),
(22, 24, "STATE"),
(25, 37, "MOBILE_NUMBER"),
(38, 54, "STREET_ADDRESS"),
(55, 67, "TELEPHONE_NUMBER"),
(68, 76, "CITY"),
]
}),
(
"818-247-2569 CA free Glendale 818-913-2748 4227 Oakway Lane California 91204"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 15, "STATE"),
(21, 29, "CITY"),
(30, 42, "MOBILE_NUMBER"),
(43, 59, "STREET_ADDRESS"),
(60, 70, "STATE_FULL"),
(71, 76, "ZIPCODE"),
]
}),
(
"CA California Glendale free 818-913-2748 818-247-2569 91204 4227 Oakway Lane"
, {
"entities":[
(0, 2, "STATE"),
(3, 13, "STATE_FULL"),
(14, 22, "CITY"),
(28, 40, "MOBILE_NUMBER"),
(41, 53, "TELEPHONE_NUMBER"),
(54, 59, "ZIPCODE"),
(60, 76, "STREET_ADDRESS"),
]
}),
(
"818-247-2569 California CA free 4227 Oakway Lane 91204 818-913-2748 Glendale"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 23, "STATE_FULL"),
(24, 26, "STATE"),
(32, 48, "STREET_ADDRESS"),
(49, 54, "ZIPCODE"),
(55, 67, "MOBILE_NUMBER"),
(68, 76, "CITY"),
]
}),
(
"91204 free 818-913-2748 California 4227 Oakway Lane Glendale CA 818-247-2569"
, {
"entities":[
(0, 5, "ZIPCODE"),
(11, 23, "MOBILE_NUMBER"),
(24, 34, "STATE_FULL"),
(35, 51, "STREET_ADDRESS"),
(52, 60, "CITY"),
(61, 63, "STATE"),
(64, 76, "TELEPHONE_NUMBER"),
]
}),
(
"32097 FL Yulee 904-468-3783 Florida 4729 Arrowood Drive 904-548-7364"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 14, "CITY"),
(15, 27, "MOBILE_NUMBER"),
(28, 35, "STATE_FULL"),
(36, 55, "STREET_ADDRESS"),
(56, 68, "TELEPHONE_NUMBER"),
]
}),
(
"32097 Yulee FL 904-548-7364 4729 Arrowood Drive Florida 904-468-3783"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 11, "CITY"),
(12, 14, "STATE"),
(15, 27, "TELEPHONE_NUMBER"),
(28, 47, "STREET_ADDRESS"),
(48, 55, "STATE_FULL"),
(56, 68, "MOBILE_NUMBER"),
]
}),
(
"904-468-3783 Yulee Florida 32097 FL 4729 Arrowood Drive 904-548-7364"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 18, "CITY"),
(19, 26, "STATE_FULL"),
(27, 32, "ZIPCODE"),
(33, 35, "STATE"),
(36, 55, "STREET_ADDRESS"),
(56, 68, "TELEPHONE_NUMBER"),
]
}),
(
"Yulee 904-548-7364 Florida FL 32097 904-468-3783 4729 Arrowood Drive"
, {
"entities":[
(0, 5, "CITY"),
(6, 18, "TELEPHONE_NUMBER"),
(19, 26, "STATE_FULL"),
(27, 29, "STATE"),
(30, 35, "ZIPCODE"),
(36, 48, "MOBILE_NUMBER"),
(49, 68, "STREET_ADDRESS"),
]
}),
(
"32097 4729 Arrowood Drive Yulee FL Florida 904-468-3783 904-548-7364"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 25, "STREET_ADDRESS"),
(26, 31, "CITY"),
(32, 34, "STATE"),
(35, 42, "STATE_FULL"),
(43, 55, "MOBILE_NUMBER"),
(56, 68, "TELEPHONE_NUMBER"),
]
}),
(
"Yulee 32097 4729 Arrowood Drive 904-468-3783 FL Florida 904-548-7364"
, {
"entities":[
(0, 5, "CITY"),
(6, 11, "ZIPCODE"),
(12, 31, "STREET_ADDRESS"),
(32, 44, "MOBILE_NUMBER"),
(45, 47, "STATE"),
(48, 55, "STATE_FULL"),
(56, 68, "TELEPHONE_NUMBER"),
]
}),
(
"904-548-7364 Florida FL 4729 Arrowood Drive 32097 904-468-3783 Yulee"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 20, "STATE_FULL"),
(21, 23, "STATE"),
(24, 43, "STREET_ADDRESS"),
(44, 49, "ZIPCODE"),
(50, 62, "MOBILE_NUMBER"),
(63, 68, "CITY"),
]
}),
(
"Yulee 4729 Arrowood Drive 904-468-3783 904-548-7364 Florida FL 32097"
, {
"entities":[
(0, 5, "CITY"),
(6, 25, "STREET_ADDRESS"),
(26, 38, "MOBILE_NUMBER"),
(39, 51, "TELEPHONE_NUMBER"),
(52, 59, "STATE_FULL"),
(60, 62, "STATE"),
(63, 68, "ZIPCODE"),
]
}),
(
"32097 904-548-7364 Florida FL 4729 Arrowood Drive Yulee 904-468-3783"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "TELEPHONE_NUMBER"),
(19, 26, "STATE_FULL"),
(27, 29, "STATE"),
(30, 49, "STREET_ADDRESS"),
(50, 55, "CITY"),
(56, 68, "MOBILE_NUMBER"),
]
}),
(
"Yulee Florida 32097 4729 Arrowood Drive 904-548-7364 FL 904-468-3783"
, {
"entities":[
(0, 5, "CITY"),
(6, 13, "STATE_FULL"),
(14, 19, "ZIPCODE"),
(20, 39, "STREET_ADDRESS"),
(40, 52, "TELEPHONE_NUMBER"),
(53, 55, "STATE"),
(56, 68, "MOBILE_NUMBER"),
]
}),
(
"North Billerica 01862 3491 Hampton Meadows 774-209-3057 978-314-1569 Massachusetts MA"
, {
"entities":[
(0, 15, "CITY"),
(16, 21, "ZIPCODE"),
(22, 42, "STREET_ADDRESS"),
(43, 55, "MOBILE_NUMBER"),
(56, 68, "TELEPHONE_NUMBER"),
(69, 82, "STATE_FULL"),
(83, 85, "STATE"),
]
}),
(
"North Billerica 978-314-1569 3491 Hampton Meadows MA 01862 774-209-3057 Massachusetts"
, {
"entities":[
(0, 15, "CITY"),
(16, 28, "TELEPHONE_NUMBER"),
(29, 49, "STREET_ADDRESS"),
(50, 52, "STATE"),
(53, 58, "ZIPCODE"),
(59, 71, "MOBILE_NUMBER"),
(72, 85, "STATE_FULL"),
]
}),
(
"Massachusetts 01862 North Billerica 774-209-3057 MA 3491 Hampton Meadows 978-314-1569"
, {
"entities":[
(0, 13, "STATE_FULL"),
(14, 19, "ZIPCODE"),
(20, 35, "CITY"),
(36, 48, "MOBILE_NUMBER"),
(49, 51, "STATE"),
(52, 72, "STREET_ADDRESS"),
(73, 85, "TELEPHONE_NUMBER"),
]
}),
(
"978-314-1569 Massachusetts North Billerica 3491 Hampton Meadows 774-209-3057 MA 01862"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 26, "STATE_FULL"),
(27, 42, "CITY"),
(43, 63, "STREET_ADDRESS"),
(64, 76, "MOBILE_NUMBER"),
(77, 79, "STATE"),
(80, 85, "ZIPCODE"),
]
}),
(
"01862 North Billerica 774-209-3057 978-314-1569 Massachusetts MA 3491 Hampton Meadows"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 21, "CITY"),
(22, 34, "MOBILE_NUMBER"),
(35, 47, "TELEPHONE_NUMBER"),
(48, 61, "STATE_FULL"),
(62, 64, "STATE"),
(65, 85, "STREET_ADDRESS"),
]
}),
(
"774-209-3057 3491 Hampton Meadows MA North Billerica 01862 Massachusetts 978-314-1569"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 33, "STREET_ADDRESS"),
(34, 36, "STATE"),
(37, 52, "CITY"),
(53, 58, "ZIPCODE"),
(59, 72, "STATE_FULL"),
(73, 85, "TELEPHONE_NUMBER"),
]
}),
(
"MA 3491 Hampton Meadows 978-314-1569 North Billerica Massachusetts 01862 774-209-3057"
, {
"entities":[
(0, 2, "STATE"),
(3, 23, "STREET_ADDRESS"),
(24, 36, "TELEPHONE_NUMBER"),
(37, 52, "CITY"),
(53, 66, "STATE_FULL"),
(67, 72, "ZIPCODE"),
(73, 85, "MOBILE_NUMBER"),
]
}),
(
"MA 01862 Massachusetts 978-314-1569 3491 Hampton Meadows 774-209-3057 North Billerica"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 22, "STATE_FULL"),
(23, 35, "TELEPHONE_NUMBER"),
(36, 56, "STREET_ADDRESS"),
(57, 69, "MOBILE_NUMBER"),
(70, 85, "CITY"),
]
}),
(
"774-209-3057 978-314-1569 MA 3491 Hampton Meadows Massachusetts 01862 North Billerica"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 25, "TELEPHONE_NUMBER"),
(26, 28, "STATE"),
(29, 49, "STREET_ADDRESS"),
(50, 63, "STATE_FULL"),
(64, 69, "ZIPCODE"),
(70, 85, "CITY"),
]
}),
(
"MA 774-209-3057 3491 Hampton Meadows 01862 978-314-1569 North Billerica Massachusetts"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "MOBILE_NUMBER"),
(16, 36, "STREET_ADDRESS"),
(37, 42, "ZIPCODE"),
(43, 55, "TELEPHONE_NUMBER"),
(56, 71, "CITY"),
(72, 85, "STATE_FULL"),
]
}),
(
"615-757-7045 Hendersonville TN 37075 865-742-9734 1306 Hidden Pond Road Tennessee"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 27, "CITY"),
(28, 30, "STATE"),
(31, 36, "ZIPCODE"),
(37, 49, "MOBILE_NUMBER"),
(50, 71, "STREET_ADDRESS"),
(72, 81, "STATE_FULL"),
]
}),
(
"Tennessee 865-742-9734 TN Hendersonville 37075 1306 Hidden Pond Road 615-757-7045"
, {
"entities":[
(0, 9, "STATE_FULL"),
(10, 22, "MOBILE_NUMBER"),
(23, 25, "STATE"),
(26, 40, "CITY"),
(41, 46, "ZIPCODE"),
(47, 68, "STREET_ADDRESS"),
(69, 81, "TELEPHONE_NUMBER"),
]
}),
(
"TN Tennessee Hendersonville 615-757-7045 865-742-9734 1306 Hidden Pond Road 37075"
, {
"entities":[
(0, 2, "STATE"),
(3, 12, "STATE_FULL"),
(13, 27, "CITY"),
(28, 40, "TELEPHONE_NUMBER"),
(41, 53, "MOBILE_NUMBER"),
(54, 75, "STREET_ADDRESS"),
(76, 81, "ZIPCODE"),
]
}),
(
"TN Hendersonville 1306 Hidden Pond Road 615-757-7045 37075 Tennessee 865-742-9734"
, {
"entities":[
(0, 2, "STATE"),
(3, 17, "CITY"),
(18, 39, "STREET_ADDRESS"),
(40, 52, "TELEPHONE_NUMBER"),
(53, 58, "ZIPCODE"),
(59, 68, "STATE_FULL"),
(69, 81, "MOBILE_NUMBER"),
]
}),
(
"TN Tennessee 37075 615-757-7045 1306 Hidden Pond Road 865-742-9734 Hendersonville"
, {
"entities":[
(0, 2, "STATE"),
(3, 12, "STATE_FULL"),
(13, 18, "ZIPCODE"),
(19, 31, "TELEPHONE_NUMBER"),
(32, 53, "STREET_ADDRESS"),
(54, 66, "MOBILE_NUMBER"),
(67, 81, "CITY"),
]
}),
(
"TN 865-742-9734 615-757-7045 Hendersonville 1306 Hidden Pond Road 37075 Tennessee"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "MOBILE_NUMBER"),
(16, 28, "TELEPHONE_NUMBER"),
(29, 43, "CITY"),
(44, 65, "STREET_ADDRESS"),
(66, 71, "ZIPCODE"),
(72, 81, "STATE_FULL"),
]
}),
(
"Tennessee Hendersonville 37075 1306 Hidden Pond Road TN 865-742-9734 615-757-7045"
, {
"entities":[
(0, 9, "STATE_FULL"),
(10, 24, "CITY"),
(25, 30, "ZIPCODE"),
(31, 52, "STREET_ADDRESS"),
(53, 55, "STATE"),
(56, 68, "MOBILE_NUMBER"),
(69, 81, "TELEPHONE_NUMBER"),
]
}),
(
"615-757-7045 37075 Hendersonville 1306 Hidden Pond Road Tennessee 865-742-9734 TN"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 33, "CITY"),
(34, 55, "STREET_ADDRESS"),
(56, 65, "STATE_FULL"),
(66, 78, "MOBILE_NUMBER"),
(79, 81, "STATE"),
]
}),
(
"1306 Hidden Pond Road TN Tennessee 615-757-7045 Hendersonville 865-742-9734 37075"
, {
"entities":[
(0, 21, "STREET_ADDRESS"),
(22, 24, "STATE"),
(25, 34, "STATE_FULL"),
(35, 47, "TELEPHONE_NUMBER"),
(48, 62, "CITY"),
(63, 75, "MOBILE_NUMBER"),
(76, 81, "ZIPCODE"),
]
}),
(
"Hendersonville 1306 Hidden Pond Road TN 37075 Tennessee 865-742-9734 615-757-7045"
, {
"entities":[
(0, 14, "CITY"),
(15, 36, "STREET_ADDRESS"),
(37, 39, "STATE"),
(40, 45, "ZIPCODE"),
(46, 55, "STATE_FULL"),
(56, 68, "MOBILE_NUMBER"),
(69, 81, "TELEPHONE_NUMBER"),
]
}),
(
"718-951-8361 Brooklyn 917-753-9315 New York 11230 1444 Lady Bug Drive NY"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 21, "CITY"),
(22, 34, "MOBILE_NUMBER"),
(35, 43, "STATE_FULL"),
(44, 49, "ZIPCODE"),
(50, 69, "STREET_ADDRESS"),
(70, 72, "STATE"),
]
}),
(
"718-951-8361 1444 Lady Bug Drive NY 11230 New York Brooklyn 917-753-9315"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 32, "STREET_ADDRESS"),
(33, 35, "STATE"),
(36, 41, "ZIPCODE"),
(42, 50, "STATE_FULL"),
(51, 59, "CITY"),
(60, 72, "MOBILE_NUMBER"),
]
}),
(
"11230 1444 Lady Bug Drive 718-951-8361 917-753-9315 Brooklyn New York NY"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 25, "STREET_ADDRESS"),
(26, 38, "TELEPHONE_NUMBER"),
(39, 51, "MOBILE_NUMBER"),
(52, 60, "CITY"),
(61, 69, "STATE_FULL"),
(70, 72, "STATE"),
]
}),
(
"Brooklyn New York 718-951-8361 1444 Lady Bug Drive 11230 917-753-9315 NY"
, {
"entities":[
(0, 8, "CITY"),
(9, 17, "STATE_FULL"),
(18, 30, "TELEPHONE_NUMBER"),
(31, 50, "STREET_ADDRESS"),
(51, 56, "ZIPCODE"),
(57, 69, "MOBILE_NUMBER"),
(70, 72, "STATE"),
]
}),
(
"11230 1444 Lady Bug Drive 917-753-9315 Brooklyn 718-951-8361 New York NY"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 25, "STREET_ADDRESS"),
(26, 38, "MOBILE_NUMBER"),
(39, 47, "CITY"),
(48, 60, "TELEPHONE_NUMBER"),
(61, 69, "STATE_FULL"),
(70, 72, "STATE"),
]
}),
(
"718-951-8361 917-753-9315 NY 1444 Lady Bug Drive Brooklyn 11230 New York"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 25, "MOBILE_NUMBER"),
(26, 28, "STATE"),
(29, 48, "STREET_ADDRESS"),
(49, 57, "CITY"),
(58, 63, "ZIPCODE"),
(64, 72, "STATE_FULL"),
]
}),
(
"917-753-9315 1444 Lady Bug Drive 718-951-8361 11230 New York Brooklyn NY"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 32, "STREET_ADDRESS"),
(33, 45, "TELEPHONE_NUMBER"),
(46, 51, "ZIPCODE"),
(52, 60, "STATE_FULL"),
(61, 69, "CITY"),
(70, 72, "STATE"),
]
}),
(
"11230 New York NY 917-753-9315 1444 Lady Bug Drive Brooklyn 718-951-8361"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 14, "STATE_FULL"),
(15, 17, "STATE"),
(18, 30, "MOBILE_NUMBER"),
(31, 50, "STREET_ADDRESS"),
(51, 59, "CITY"),
(60, 72, "TELEPHONE_NUMBER"),
]
}),
(
"718-951-8361 11230 New York Brooklyn NY 1444 Lady Bug Drive 917-753-9315"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 27, "STATE_FULL"),
(28, 36, "CITY"),
(37, 39, "STATE"),
(40, 59, "STREET_ADDRESS"),
(60, 72, "MOBILE_NUMBER"),
]
}),
(
"New York 718-951-8361 NY 11230 Brooklyn 1444 Lady Bug Drive 917-753-9315"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 21, "TELEPHONE_NUMBER"),
(22, 24, "STATE"),
(25, 30, "ZIPCODE"),
(31, 39, "CITY"),
(40, 59, "STREET_ADDRESS"),
(60, 72, "MOBILE_NUMBER"),
]
}),
(
"956-206-1197 956-206-9057 Texas TX 78041 Laredo 2314 Jerome Avenue"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 25, "MOBILE_NUMBER"),
(26, 31, "STATE_FULL"),
(32, 34, "STATE"),
(35, 40, "ZIPCODE"),
(41, 47, "CITY"),
(48, 66, "STREET_ADDRESS"),
]
}),
(
"TX 956-206-9057 2314 Jerome Avenue 78041 Texas Laredo 956-206-1197"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "MOBILE_NUMBER"),
(16, 34, "STREET_ADDRESS"),
(35, 40, "ZIPCODE"),
(41, 46, "STATE_FULL"),
(47, 53, "CITY"),
(54, 66, "TELEPHONE_NUMBER"),
]
}),
(
"956-206-9057 Laredo Texas TX 956-206-1197 78041 2314 Jerome Avenue"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 19, "CITY"),
(20, 25, "STATE_FULL"),
(26, 28, "STATE"),
(29, 41, "TELEPHONE_NUMBER"),
(42, 47, "ZIPCODE"),
(48, 66, "STREET_ADDRESS"),
]
}),
(
"2314 Jerome Avenue 956-206-1197 78041 Laredo 956-206-9057 Texas TX"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 31, "TELEPHONE_NUMBER"),
(32, 37, "ZIPCODE"),
(38, 44, "CITY"),
(45, 57, "MOBILE_NUMBER"),
(58, 63, "STATE_FULL"),
(64, 66, "STATE"),
]
}),
(
"TX 956-206-1197 78041 Texas 2314 Jerome Avenue Laredo 956-206-9057"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "TELEPHONE_NUMBER"),
(16, 21, "ZIPCODE"),
(22, 27, "STATE_FULL"),
(28, 46, "STREET_ADDRESS"),
(47, 53, "CITY"),
(54, 66, "MOBILE_NUMBER"),
]
}),
(
"956-206-9057 TX 2314 Jerome Avenue Texas Laredo 78041 956-206-1197"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 15, "STATE"),
(16, 34, "STREET_ADDRESS"),
(35, 40, "STATE_FULL"),
(41, 47, "CITY"),
(48, 53, "ZIPCODE"),
(54, 66, "TELEPHONE_NUMBER"),
]
}),
(
"Texas TX Laredo 2314 Jerome Avenue 78041 956-206-9057 956-206-1197"
, {
"entities":[
(0, 5, "STATE_FULL"),
(6, 8, "STATE"),
(9, 15, "CITY"),
(16, 34, "STREET_ADDRESS"),
(35, 40, "ZIPCODE"),
(41, 53, "MOBILE_NUMBER"),
(54, 66, "TELEPHONE_NUMBER"),
]
}),
(
"Laredo 78041 2314 Jerome Avenue 956-206-1197 TX Texas 956-206-9057"
, {
"entities":[
(0, 6, "CITY"),
(7, 12, "ZIPCODE"),
(13, 31, "STREET_ADDRESS"),
(32, 44, "TELEPHONE_NUMBER"),
(45, 47, "STATE"),
(48, 53, "STATE_FULL"),
(54, 66, "MOBILE_NUMBER"),
]
}),
(
"956-206-1197 Texas Laredo 78041 2314 Jerome Avenue TX 956-206-9057"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 18, "STATE_FULL"),
(19, 25, "CITY"),
(26, 31, "ZIPCODE"),
(32, 50, "STREET_ADDRESS"),
(51, 53, "STATE"),
(54, 66, "MOBILE_NUMBER"),
]
}),
(
"Laredo 956-206-1197 78041 956-206-9057 TX 2314 Jerome Avenue Texas"
, {
"entities":[
(0, 6, "CITY"),
(7, 19, "TELEPHONE_NUMBER"),
(20, 25, "ZIPCODE"),
(26, 38, "MOBILE_NUMBER"),
(39, 41, "STATE"),
(42, 60, "STREET_ADDRESS"),
(61, 66, "STATE_FULL"),
]
}),
(
"Springfield Missouri 417-834-1456 417-295-6044 MO 65865 938 Lighthouse Drive"
, {
"entities":[
(0, 11, "CITY"),
(12, 20, "STATE_FULL"),
(21, 33, "MOBILE_NUMBER"),
(34, 46, "TELEPHONE_NUMBER"),
(47, 49, "STATE"),
(50, 55, "ZIPCODE"),
(56, 76, "STREET_ADDRESS"),
]
}),
(
"Springfield 65865 417-834-1456 938 Lighthouse Drive MO 417-295-6044 Missouri"
, {
"entities":[
(0, 11, "CITY"),
(12, 17, "ZIPCODE"),
(18, 30, "MOBILE_NUMBER"),
(31, 51, "STREET_ADDRESS"),
(52, 54, "STATE"),
(55, 67, "TELEPHONE_NUMBER"),
(68, 76, "STATE_FULL"),
]
}),
(
"417-834-1456 417-295-6044 MO Missouri 65865 Springfield 938 Lighthouse Drive"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 25, "TELEPHONE_NUMBER"),
(26, 28, "STATE"),
(29, 37, "STATE_FULL"),
(38, 43, "ZIPCODE"),
(44, 55, "CITY"),
(56, 76, "STREET_ADDRESS"),
]
}),
(
"65865 938 Lighthouse Drive MO Missouri 417-295-6044 Springfield 417-834-1456"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 26, "STREET_ADDRESS"),
(27, 29, "STATE"),
(30, 38, "STATE_FULL"),
(39, 51, "TELEPHONE_NUMBER"),
(52, 63, "CITY"),
(64, 76, "MOBILE_NUMBER"),
]
}),
(
"Missouri MO 65865 Springfield 417-834-1456 417-295-6044 938 Lighthouse Drive"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 11, "STATE"),
(12, 17, "ZIPCODE"),
(18, 29, "CITY"),
(30, 42, "MOBILE_NUMBER"),
(43, 55, "TELEPHONE_NUMBER"),
(56, 76, "STREET_ADDRESS"),
]
}),
(
"MO Missouri 65865 Springfield 938 Lighthouse Drive 417-295-6044 417-834-1456"
, {
"entities":[
(0, 2, "STATE"),
(3, 11, "STATE_FULL"),
(12, 17, "ZIPCODE"),
(18, 29, "CITY"),
(30, 50, "STREET_ADDRESS"),
(51, 63, "TELEPHONE_NUMBER"),
(64, 76, "MOBILE_NUMBER"),
]
}),
(
"417-295-6044 MO Missouri 938 Lighthouse Drive Springfield 417-834-1456 65865"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 15, "STATE"),
(16, 24, "STATE_FULL"),
(25, 45, "STREET_ADDRESS"),
(46, 57, "CITY"),
(58, 70, "MOBILE_NUMBER"),
(71, 76, "ZIPCODE"),
]
}),
(
"417-834-1456 417-295-6044 Missouri 65865 MO Springfield 938 Lighthouse Drive"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 25, "TELEPHONE_NUMBER"),
(26, 34, "STATE_FULL"),
(35, 40, "ZIPCODE"),
(41, 43, "STATE"),
(44, 55, "CITY"),
(56, 76, "STREET_ADDRESS"),
]
}),
(
"Missouri 65865 417-834-1456 MO Springfield 417-295-6044 938 Lighthouse Drive"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 14, "ZIPCODE"),
(15, 27, "MOBILE_NUMBER"),
(28, 30, "STATE"),
(31, 42, "CITY"),
(43, 55, "TELEPHONE_NUMBER"),
(56, 76, "STREET_ADDRESS"),
]
}),
(
"Missouri MO Springfield 938 Lighthouse Drive 65865 417-295-6044 417-834-1456"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 11, "STATE"),
(12, 23, "CITY"),
(24, 44, "STREET_ADDRESS"),
(45, 50, "ZIPCODE"),
(51, 63, "TELEPHONE_NUMBER"),
(64, 76, "MOBILE_NUMBER"),
]
}),
(
"Texas address 713-436-1179 TX 14 Monroe Street 77047 Houston 832-890-9456"
, {
"entities":[
(0, 5, "STATE_FULL"),
(14, 26, "TELEPHONE_NUMBER"),
(27, 29, "STATE"),
(30, 46, "STREET_ADDRESS"),
(47, 52, "ZIPCODE"),
(53, 60, "CITY"),
(61, 73, "MOBILE_NUMBER"),
]
}),
(
"832-890-9456 Texas TX 77047 Houston 14 Monroe Street address 713-436-1179"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 18, "STATE_FULL"),
(19, 21, "STATE"),
(22, 27, "ZIPCODE"),
(28, 35, "CITY"),
(36, 52, "STREET_ADDRESS"),
(61, 73, "TELEPHONE_NUMBER"),
]
}),
(
"14 Monroe Street TX 713-436-1179 Texas 77047 address Houston 832-890-9456"
, {
"entities":[
(0, 16, "STREET_ADDRESS"),
(17, 19, "STATE"),
(20, 32, "TELEPHONE_NUMBER"),
(33, 38, "STATE_FULL"),
(39, 44, "ZIPCODE"),
(53, 60, "CITY"),
(61, 73, "MOBILE_NUMBER"),
]
}),
(
"TX 832-890-9456 77047 14 Monroe Street 713-436-1179 address Houston Texas"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "MOBILE_NUMBER"),
(16, 21, "ZIPCODE"),
(22, 38, "STREET_ADDRESS"),
(39, 51, "TELEPHONE_NUMBER"),
(60, 67, "CITY"),
(68, 73, "STATE_FULL"),
]
}),
(
"77047 TX Houston 713-436-1179 address Texas 14 Monroe Street 832-890-9456"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 16, "CITY"),
(17, 29, "TELEPHONE_NUMBER"),
(38, 43, "STATE_FULL"),
(44, 60, "STREET_ADDRESS"),
(61, 73, "MOBILE_NUMBER"),
]
}),
(
"TX address 713-436-1179 77047 832-890-9456 Houston 14 Monroe Street Texas"
, {
"entities":[
(0, 2, "STATE"),
(11, 23, "TELEPHONE_NUMBER"),
(24, 29, "ZIPCODE"),
(30, 42, "MOBILE_NUMBER"),
(43, 50, "CITY"),
(51, 67, "STREET_ADDRESS"),
(68, 73, "STATE_FULL"),
]
}),
(
"713-436-1179 address Houston 832-890-9456 77047 14 Monroe Street Texas TX"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(21, 28, "CITY"),
(29, 41, "MOBILE_NUMBER"),
(42, 47, "ZIPCODE"),
(48, 64, "STREET_ADDRESS"),
(65, 70, "STATE_FULL"),
(71, 73, "STATE"),
]
}),
(
"77047 Texas address TX 713-436-1179 Houston 14 Monroe Street 832-890-9456"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 11, "STATE_FULL"),
(20, 22, "STATE"),
(23, 35, "TELEPHONE_NUMBER"),
(36, 43, "CITY"),
(44, 60, "STREET_ADDRESS"),
(61, 73, "MOBILE_NUMBER"),
]
}),
(
"832-890-9456 TX Houston 713-436-1179 77047 Texas 14 Monroe Street address"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 15, "STATE"),
(16, 23, "CITY"),
(24, 36, "TELEPHONE_NUMBER"),
(37, 42, "ZIPCODE"),
(43, 48, "STATE_FULL"),
(49, 65, "STREET_ADDRESS"),
]
}),
(
"Texas 713-436-1179 832-890-9456 77047 TX address Houston 14 Monroe Street"
, {
"entities":[
(0, 5, "STATE_FULL"),
(6, 18, "TELEPHONE_NUMBER"),
(19, 31, "MOBILE_NUMBER"),
(32, 37, "ZIPCODE"),
(38, 40, "STATE"),
(49, 56, "CITY"),
(57, 73, "STREET_ADDRESS"),
]
}),
(
"Minnesota Minneapolis 763-374-7810 55405 MN 2294 Willison Street 612-991-9858"
, {
"entities":[
(0, 9, "STATE_FULL"),
(10, 21, "CITY"),
(22, 34, "TELEPHONE_NUMBER"),
(35, 40, "ZIPCODE"),
(41, 43, "STATE"),
(44, 64, "STREET_ADDRESS"),
(65, 77, "MOBILE_NUMBER"),
]
}),
(
"Minnesota 55405 763-374-7810 MN 612-991-9858 2294 Willison Street Minneapolis"
, {
"entities":[
(0, 9, "STATE_FULL"),
(10, 15, "ZIPCODE"),
(16, 28, "TELEPHONE_NUMBER"),
(29, 31, "STATE"),
(32, 44, "MOBILE_NUMBER"),
(45, 65, "STREET_ADDRESS"),
(66, 77, "CITY"),
]
}),
(
"Minnesota Minneapolis 612-991-9858 2294 Willison Street 763-374-7810 55405 MN"
, {
"entities":[
(0, 9, "STATE_FULL"),
(10, 21, "CITY"),
(22, 34, "MOBILE_NUMBER"),
(35, 55, "STREET_ADDRESS"),
(56, 68, "TELEPHONE_NUMBER"),
(69, 74, "ZIPCODE"),
(75, 77, "STATE"),
]
}),
(
"Minneapolis 2294 Willison Street Minnesota 612-991-9858 MN 55405 763-374-7810"
, {
"entities":[
(0, 11, "CITY"),
(12, 32, "STREET_ADDRESS"),
(33, 42, "STATE_FULL"),
(43, 55, "MOBILE_NUMBER"),
(56, 58, "STATE"),
(59, 64, "ZIPCODE"),
(65, 77, "TELEPHONE_NUMBER"),
]
}),
(
"2294 Willison Street MN 612-991-9858 Minnesota 763-374-7810 55405 Minneapolis"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 23, "STATE"),
(24, 36, "MOBILE_NUMBER"),
(37, 46, "STATE_FULL"),
(47, 59, "TELEPHONE_NUMBER"),
(60, 65, "ZIPCODE"),
(66, 77, "CITY"),
]
}),
(
"Minneapolis 763-374-7810 55405 MN 612-991-9858 2294 Willison Street Minnesota"
, {
"entities":[
(0, 11, "CITY"),
(12, 24, "TELEPHONE_NUMBER"),
(25, 30, "ZIPCODE"),
(31, 33, "STATE"),
(34, 46, "MOBILE_NUMBER"),
(47, 67, "STREET_ADDRESS"),
(68, 77, "STATE_FULL"),
]
}),
(
"612-991-9858 763-374-7810 55405 2294 Willison Street Minnesota MN Minneapolis"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 25, "TELEPHONE_NUMBER"),
(26, 31, "ZIPCODE"),
(32, 52, "STREET_ADDRESS"),
(53, 62, "STATE_FULL"),
(63, 65, "STATE"),
(66, 77, "CITY"),
]
}),
(
"2294 Willison Street MN Minneapolis 612-991-9858 763-374-7810 55405 Minnesota"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 23, "STATE"),
(24, 35, "CITY"),
(36, 48, "MOBILE_NUMBER"),
(49, 61, "TELEPHONE_NUMBER"),
(62, 67, "ZIPCODE"),
(68, 77, "STATE_FULL"),
]
}),
(
"2294 Willison Street Minneapolis 55405 MN 763-374-7810 Minnesota 612-991-9858"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 32, "CITY"),
(33, 38, "ZIPCODE"),
(39, 41, "STATE"),
(42, 54, "TELEPHONE_NUMBER"),
(55, 64, "STATE_FULL"),
(65, 77, "MOBILE_NUMBER"),
]
}),
(
"Minneapolis 763-374-7810 Minnesota 2294 Willison Street 55405 612-991-9858 MN"
, {
"entities":[
(0, 11, "CITY"),
(12, 24, "TELEPHONE_NUMBER"),
(25, 34, "STATE_FULL"),
(35, 55, "STREET_ADDRESS"),
(56, 61, "ZIPCODE"),
(62, 74, "MOBILE_NUMBER"),
(75, 77, "STATE"),
]
}),
(
"615-965-2058 free 615-256-6879 Nashville 37201 Tennessee TN 3204 Cottonwood Lane"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(18, 30, "MOBILE_NUMBER"),
(31, 40, "CITY"),
(41, 46, "ZIPCODE"),
(47, 56, "STATE_FULL"),
(57, 59, "STATE"),
(60, 80, "STREET_ADDRESS"),
]
}),
(
"TN Tennessee 37201 615-965-2058 615-256-6879 3204 Cottonwood Lane Nashville free"
, {
"entities":[
(0, 2, "STATE"),
(3, 12, "STATE_FULL"),
(13, 18, "ZIPCODE"),
(19, 31, "TELEPHONE_NUMBER"),
(32, 44, "MOBILE_NUMBER"),
(45, 65, "STREET_ADDRESS"),
(66, 75, "CITY"),
]
}),
(
"3204 Cottonwood Lane TN Tennessee 615-256-6879 free Nashville 37201 615-965-2058"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 23, "STATE"),
(24, 33, "STATE_FULL"),
(34, 46, "MOBILE_NUMBER"),
(52, 61, "CITY"),
(62, 67, "ZIPCODE"),
(68, 80, "TELEPHONE_NUMBER"),
]
}),
(
"Nashville free TN 615-256-6879 Tennessee 615-965-2058 3204 Cottonwood Lane 37201"
, {
"entities":[
(0, 9, "CITY"),
(15, 17, "STATE"),
(18, 30, "MOBILE_NUMBER"),
(31, 40, "STATE_FULL"),
(41, 53, "TELEPHONE_NUMBER"),
(54, 74, "STREET_ADDRESS"),
(75, 80, "ZIPCODE"),
]
}),
(
"Nashville TN Tennessee 615-256-6879 615-965-2058 37201 free 3204 Cottonwood Lane"
, {
"entities":[
(0, 9, "CITY"),
(10, 12, "STATE"),
(13, 22, "STATE_FULL"),
(23, 35, "MOBILE_NUMBER"),
(36, 48, "TELEPHONE_NUMBER"),
(49, 54, "ZIPCODE"),
(60, 80, "STREET_ADDRESS"),
]
}),
(
"free 615-256-6879 3204 Cottonwood Lane 615-965-2058 Tennessee TN 37201 Nashville"
, {
"entities":[
(5, 17, "MOBILE_NUMBER"),
(18, 38, "STREET_ADDRESS"),
(39, 51, "TELEPHONE_NUMBER"),
(52, 61, "STATE_FULL"),
(62, 64, "STATE"),
(65, 70, "ZIPCODE"),
(71, 80, "CITY"),
]
}),
(
"615-256-6879 615-965-2058 Tennessee 37201 3204 Cottonwood Lane Nashville TN free"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 25, "TELEPHONE_NUMBER"),
(26, 35, "STATE_FULL"),
(36, 41, "ZIPCODE"),
(42, 62, "STREET_ADDRESS"),
(63, 72, "CITY"),
(73, 75, "STATE"),
]
}),
(
"Tennessee 37201 615-965-2058 free Nashville 615-256-6879 3204 Cottonwood Lane TN"
, {
"entities":[
(0, 9, "STATE_FULL"),
(10, 15, "ZIPCODE"),
(16, 28, "TELEPHONE_NUMBER"),
(34, 43, "CITY"),
(44, 56, "MOBILE_NUMBER"),
(57, 77, "STREET_ADDRESS"),
(78, 80, "STATE"),
]
}),
(
"TN 615-965-2058 Nashville Tennessee 615-256-6879 3204 Cottonwood Lane 37201 free"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "TELEPHONE_NUMBER"),
(16, 25, "CITY"),
(26, 35, "STATE_FULL"),
(36, 48, "MOBILE_NUMBER"),
(49, 69, "STREET_ADDRESS"),
(70, 75, "ZIPCODE"),
]
}),
(
"615-256-6879 Nashville TN 3204 Cottonwood Lane free 37201 615-965-2058 Tennessee"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 22, "CITY"),
(23, 25, "STATE"),
(26, 46, "STREET_ADDRESS"),
(52, 57, "ZIPCODE"),
(58, 70, "TELEPHONE_NUMBER"),
(71, 80, "STATE_FULL"),
]
}),
(
"Indiana 1222 Bernardo Street Boonville 812-202-9234 address 47601 812-897-4179 IN"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 28, "STREET_ADDRESS"),
(29, 38, "CITY"),
(39, 51, "MOBILE_NUMBER"),
(60, 65, "ZIPCODE"),
(66, 78, "TELEPHONE_NUMBER"),
(79, 81, "STATE"),
]
}),
(
"47601 Indiana IN Boonville 1222 Bernardo Street 812-897-4179 address 812-202-9234"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 13, "STATE_FULL"),
(14, 16, "STATE"),
(17, 26, "CITY"),
(27, 47, "STREET_ADDRESS"),
(48, 60, "TELEPHONE_NUMBER"),
(69, 81, "MOBILE_NUMBER"),
]
}),
(
"Indiana 47601 Boonville 1222 Bernardo Street IN 812-202-9234 812-897-4179 address"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 13, "ZIPCODE"),
(14, 23, "CITY"),
(24, 44, "STREET_ADDRESS"),
(45, 47, "STATE"),
(48, 60, "MOBILE_NUMBER"),
(61, 73, "TELEPHONE_NUMBER"),
]
}),
(
"812-897-4179 Boonville Indiana address 47601 IN 812-202-9234 1222 Bernardo Street"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 22, "CITY"),
(23, 30, "STATE_FULL"),
(39, 44, "ZIPCODE"),
(45, 47, "STATE"),
(48, 60, "MOBILE_NUMBER"),
(61, 81, "STREET_ADDRESS"),
]
}),
(
"812-202-9234 Boonville 1222 Bernardo Street 47601 IN Indiana 812-897-4179 address"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 22, "CITY"),
(23, 43, "STREET_ADDRESS"),
(44, 49, "ZIPCODE"),
(50, 52, "STATE"),
(53, 60, "STATE_FULL"),
(61, 73, "TELEPHONE_NUMBER"),
]
}),
(
"IN 812-202-9234 address 47601 Boonville 812-897-4179 Indiana 1222 Bernardo Street"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "MOBILE_NUMBER"),
(24, 29, "ZIPCODE"),
(30, 39, "CITY"),
(40, 52, "TELEPHONE_NUMBER"),
(53, 60, "STATE_FULL"),
(61, 81, "STREET_ADDRESS"),
]
}),
(
"812-897-4179 Indiana 1222 Bernardo Street address Boonville 47601 IN 812-202-9234"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 20, "STATE_FULL"),
(21, 41, "STREET_ADDRESS"),
(50, 59, "CITY"),
(60, 65, "ZIPCODE"),
(66, 68, "STATE"),
(69, 81, "MOBILE_NUMBER"),
]
}),
(
"IN address Indiana 47601 812-897-4179 Boonville 812-202-9234 1222 Bernardo Street"
, {
"entities":[
(0, 2, "STATE"),
(11, 18, "STATE_FULL"),
(19, 24, "ZIPCODE"),
(25, 37, "TELEPHONE_NUMBER"),
(38, 47, "CITY"),
(48, 60, "MOBILE_NUMBER"),
(61, 81, "STREET_ADDRESS"),
]
}),
(
"47601 Indiana address Boonville 1222 Bernardo Street 812-897-4179 IN 812-202-9234"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 13, "STATE_FULL"),
(22, 31, "CITY"),
(32, 52, "STREET_ADDRESS"),
(53, 65, "TELEPHONE_NUMBER"),
(66, 68, "STATE"),
(69, 81, "MOBILE_NUMBER"),
]
}),
(
"address Indiana IN 812-202-9234 1222 Bernardo Street 812-897-4179 47601 Boonville"
, {
"entities":[
(8, 15, "STATE_FULL"),
(16, 18, "STATE"),
(19, 31, "MOBILE_NUMBER"),
(32, 52, "STREET_ADDRESS"),
(53, 65, "TELEPHONE_NUMBER"),
(66, 71, "ZIPCODE"),
(72, 81, "CITY"),
]
}),
(
"4001 Saints Alley 813-786-0870 Florida FL 33605 813-706-9611 Tampa"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 30, "MOBILE_NUMBER"),
(31, 38, "STATE_FULL"),
(39, 41, "STATE"),
(42, 47, "ZIPCODE"),
(48, 60, "TELEPHONE_NUMBER"),
(61, 66, "CITY"),
]
}),
(
"813-786-0870 Florida 4001 Saints Alley FL Tampa 813-706-9611 33605"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 20, "STATE_FULL"),
(21, 38, "STREET_ADDRESS"),
(39, 41, "STATE"),
(42, 47, "CITY"),
(48, 60, "TELEPHONE_NUMBER"),
(61, 66, "ZIPCODE"),
]
}),
(
"813-786-0870 813-706-9611 Tampa FL 4001 Saints Alley 33605 Florida"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 25, "TELEPHONE_NUMBER"),
(26, 31, "CITY"),
(32, 34, "STATE"),
(35, 52, "STREET_ADDRESS"),
(53, 58, "ZIPCODE"),
(59, 66, "STATE_FULL"),
]
}),
(
"813-786-0870 Florida 813-706-9611 33605 Tampa 4001 Saints Alley FL"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 20, "STATE_FULL"),
(21, 33, "TELEPHONE_NUMBER"),
(34, 39, "ZIPCODE"),
(40, 45, "CITY"),
(46, 63, "STREET_ADDRESS"),
(64, 66, "STATE"),
]
}),
(
"Tampa 4001 Saints Alley FL 33605 Florida 813-786-0870 813-706-9611"
, {
"entities":[
(0, 5, "CITY"),
(6, 23, "STREET_ADDRESS"),
(24, 26, "STATE"),
(27, 32, "ZIPCODE"),
(33, 40, "STATE_FULL"),
(41, 53, "MOBILE_NUMBER"),
(54, 66, "TELEPHONE_NUMBER"),
]
}),
(
"33605 813-786-0870 FL Tampa 4001 Saints Alley Florida 813-706-9611"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "MOBILE_NUMBER"),
(19, 21, "STATE"),
(22, 27, "CITY"),
(28, 45, "STREET_ADDRESS"),
(46, 53, "STATE_FULL"),
(54, 66, "TELEPHONE_NUMBER"),
]
}),
(
"813-786-0870 4001 Saints Alley FL Tampa Florida 33605 813-706-9611"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 30, "STREET_ADDRESS"),
(31, 33, "STATE"),
(34, 39, "CITY"),
(40, 47, "STATE_FULL"),
(48, 53, "ZIPCODE"),
(54, 66, "TELEPHONE_NUMBER"),
]
}),
(
"813-786-0870 33605 4001 Saints Alley FL Tampa 813-706-9611 Florida"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 36, "STREET_ADDRESS"),
(37, 39, "STATE"),
(40, 45, "CITY"),
(46, 58, "TELEPHONE_NUMBER"),
(59, 66, "STATE_FULL"),
]
}),
(
"4001 Saints Alley FL Florida 813-706-9611 33605 Tampa 813-786-0870"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 20, "STATE"),
(21, 28, "STATE_FULL"),
(29, 41, "TELEPHONE_NUMBER"),
(42, 47, "ZIPCODE"),
(48, 53, "CITY"),
(54, 66, "MOBILE_NUMBER"),
]
}),
(
"Tampa 813-706-9611 33605 FL Florida 813-786-0870 4001 Saints Alley"
, {
"entities":[
(0, 5, "CITY"),
(6, 18, "TELEPHONE_NUMBER"),
(19, 24, "ZIPCODE"),
(25, 27, "STATE"),
(28, 35, "STATE_FULL"),
(36, 48, "MOBILE_NUMBER"),
(49, 66, "STREET_ADDRESS"),
]
}),
(
"4130 Simpson Street IL 309-754-8374 61263 Matherville Illinois 847-992-2868"
, {
"entities":[
(0, 19, "STREET_ADDRESS"),
(20, 22, "STATE"),
(23, 35, "TELEPHONE_NUMBER"),
(36, 41, "ZIPCODE"),
(42, 53, "CITY"),
(54, 62, "STATE_FULL"),
(63, 75, "MOBILE_NUMBER"),
]
}),
(
"Matherville 61263 847-992-2868 Illinois 4130 Simpson Street IL 309-754-8374"
, {
"entities":[
(0, 11, "CITY"),
(12, 17, "ZIPCODE"),
(18, 30, "MOBILE_NUMBER"),
(31, 39, "STATE_FULL"),
(40, 59, "STREET_ADDRESS"),
(60, 62, "STATE"),
(63, 75, "TELEPHONE_NUMBER"),
]
}),
(
"Illinois Matherville 847-992-2868 4130 Simpson Street 61263 309-754-8374 IL"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 20, "CITY"),
(21, 33, "MOBILE_NUMBER"),
(34, 53, "STREET_ADDRESS"),
(54, 59, "ZIPCODE"),
(60, 72, "TELEPHONE_NUMBER"),
(73, 75, "STATE"),
]
}),
(
"4130 Simpson Street Matherville Illinois 61263 847-992-2868 309-754-8374 IL"
, {
"entities":[
(0, 19, "STREET_ADDRESS"),
(20, 31, "CITY"),
(32, 40, "STATE_FULL"),
(41, 46, "ZIPCODE"),
(47, 59, "MOBILE_NUMBER"),
(60, 72, "TELEPHONE_NUMBER"),
(73, 75, "STATE"),
]
}),
(
"IL 61263 309-754-8374 847-992-2868 Illinois Matherville 4130 Simpson Street"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 21, "TELEPHONE_NUMBER"),
(22, 34, "MOBILE_NUMBER"),
(35, 43, "STATE_FULL"),
(44, 55, "CITY"),
(56, 75, "STREET_ADDRESS"),
]
}),
(
"61263 Illinois 309-754-8374 Matherville 4130 Simpson Street IL 847-992-2868"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 14, "STATE_FULL"),
(15, 27, "TELEPHONE_NUMBER"),
(28, 39, "CITY"),
(40, 59, "STREET_ADDRESS"),
(60, 62, "STATE"),
(63, 75, "MOBILE_NUMBER"),
]
}),
(
"IL 61263 847-992-2868 309-754-8374 Illinois Matherville 4130 Simpson Street"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 21, "MOBILE_NUMBER"),
(22, 34, "TELEPHONE_NUMBER"),
(35, 43, "STATE_FULL"),
(44, 55, "CITY"),
(56, 75, "STREET_ADDRESS"),
]
}),
(
"309-754-8374 4130 Simpson Street IL 847-992-2868 Illinois 61263 Matherville"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 32, "STREET_ADDRESS"),
(33, 35, "STATE"),
(36, 48, "MOBILE_NUMBER"),
(49, 57, "STATE_FULL"),
(58, 63, "ZIPCODE"),
(64, 75, "CITY"),
]
}),
(
"IL 61263 847-992-2868 Illinois 309-754-8374 4130 Simpson Street Matherville"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 21, "MOBILE_NUMBER"),
(22, 30, "STATE_FULL"),
(31, 43, "TELEPHONE_NUMBER"),
(44, 63, "STREET_ADDRESS"),
(64, 75, "CITY"),
]
}),
(
"Illinois 847-992-2868 IL 309-754-8374 61263 4130 Simpson Street Matherville"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 21, "MOBILE_NUMBER"),
(22, 24, "STATE"),
(25, 37, "TELEPHONE_NUMBER"),
(38, 43, "ZIPCODE"),
(44, 63, "STREET_ADDRESS"),
(64, 75, "CITY"),
]
}),
(
"Arizona 85226 520-610-1894 Chandler 1793 Cambridge Court AZ 480-209-0897"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 13, "ZIPCODE"),
(14, 26, "MOBILE_NUMBER"),
(27, 35, "CITY"),
(36, 56, "STREET_ADDRESS"),
(57, 59, "STATE"),
(60, 72, "TELEPHONE_NUMBER"),
]
}),
(
"Arizona 480-209-0897 85226 AZ 1793 Cambridge Court 520-610-1894 Chandler"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 20, "TELEPHONE_NUMBER"),
(21, 26, "ZIPCODE"),
(27, 29, "STATE"),
(30, 50, "STREET_ADDRESS"),
(51, 63, "MOBILE_NUMBER"),
(64, 72, "CITY"),
]
}),
(
"Arizona 85226 AZ Chandler 480-209-0897 520-610-1894 1793 Cambridge Court"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 13, "ZIPCODE"),
(14, 16, "STATE"),
(17, 25, "CITY"),
(26, 38, "TELEPHONE_NUMBER"),
(39, 51, "MOBILE_NUMBER"),
(52, 72, "STREET_ADDRESS"),
]
}),
(
"520-610-1894 AZ Arizona Chandler 480-209-0897 1793 Cambridge Court 85226"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 15, "STATE"),
(16, 23, "STATE_FULL"),
(24, 32, "CITY"),
(33, 45, "TELEPHONE_NUMBER"),
(46, 66, "STREET_ADDRESS"),
(67, 72, "ZIPCODE"),
]
}),
(
"480-209-0897 AZ Arizona 520-610-1894 85226 1793 Cambridge Court Chandler"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 15, "STATE"),
(16, 23, "STATE_FULL"),
(24, 36, "MOBILE_NUMBER"),
(37, 42, "ZIPCODE"),
(43, 63, "STREET_ADDRESS"),
(64, 72, "CITY"),
]
}),
(
"85226 Arizona 480-209-0897 1793 Cambridge Court AZ Chandler 520-610-1894"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 13, "STATE_FULL"),
(14, 26, "TELEPHONE_NUMBER"),
(27, 47, "STREET_ADDRESS"),
(48, 50, "STATE"),
(51, 59, "CITY"),
(60, 72, "MOBILE_NUMBER"),
]
}),
(
"Arizona 1793 Cambridge Court 85226 480-209-0897 520-610-1894 AZ Chandler"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 28, "STREET_ADDRESS"),
(29, 34, "ZIPCODE"),
(35, 47, "TELEPHONE_NUMBER"),
(48, 60, "MOBILE_NUMBER"),
(61, 63, "STATE"),
(64, 72, "CITY"),
]
}),
(
"AZ Chandler 85226 520-610-1894 1793 Cambridge Court Arizona 480-209-0897"
, {
"entities":[
(0, 2, "STATE"),
(3, 11, "CITY"),
(12, 17, "ZIPCODE"),
(18, 30, "MOBILE_NUMBER"),
(31, 51, "STREET_ADDRESS"),
(52, 59, "STATE_FULL"),
(60, 72, "TELEPHONE_NUMBER"),
]
}),
(
"1793 Cambridge Court Chandler 480-209-0897 520-610-1894 Arizona AZ 85226"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 29, "CITY"),
(30, 42, "TELEPHONE_NUMBER"),
(43, 55, "MOBILE_NUMBER"),
(56, 63, "STATE_FULL"),
(64, 66, "STATE"),
(67, 72, "ZIPCODE"),
]
}),
(
"480-209-0897 Chandler 520-610-1894 1793 Cambridge Court AZ Arizona 85226"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 21, "CITY"),
(22, 34, "MOBILE_NUMBER"),
(35, 55, "STREET_ADDRESS"),
(56, 58, "STATE"),
(59, 66, "STATE_FULL"),
(67, 72, "ZIPCODE"),
]
}),
(
"IN Indiana 46804 Fort Wayne 812-201-3793 2041 Cessna Drive 260-435-5924"
, {
"entities":[
(0, 2, "STATE"),
(3, 10, "STATE_FULL"),
(11, 16, "ZIPCODE"),
(17, 27, "CITY"),
(28, 40, "MOBILE_NUMBER"),
(41, 58, "STREET_ADDRESS"),
(59, 71, "TELEPHONE_NUMBER"),
]
}),
(
"IN 2041 Cessna Drive Fort Wayne 260-435-5924 46804 Indiana 812-201-3793"
, {
"entities":[
(0, 2, "STATE"),
(3, 20, "STREET_ADDRESS"),
(21, 31, "CITY"),
(32, 44, "TELEPHONE_NUMBER"),
(45, 50, "ZIPCODE"),
(51, 58, "STATE_FULL"),
(59, 71, "MOBILE_NUMBER"),
]
}),
(
"812-201-3793 Fort Wayne 260-435-5924 2041 Cessna Drive Indiana 46804 IN"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 23, "CITY"),
(24, 36, "TELEPHONE_NUMBER"),
(37, 54, "STREET_ADDRESS"),
(55, 62, "STATE_FULL"),
(63, 68, "ZIPCODE"),
(69, 71, "STATE"),
]
}),
(
"Fort Wayne Indiana IN 2041 Cessna Drive 46804 260-435-5924 812-201-3793"
, {
"entities":[
(0, 10, "CITY"),
(11, 18, "STATE_FULL"),
(19, 21, "STATE"),
(22, 39, "STREET_ADDRESS"),
(40, 45, "ZIPCODE"),
(46, 58, "TELEPHONE_NUMBER"),
(59, 71, "MOBILE_NUMBER"),
]
}),
(
"46804 IN Fort Wayne 2041 Cessna Drive 260-435-5924 812-201-3793 Indiana"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 19, "CITY"),
(20, 37, "STREET_ADDRESS"),
(38, 50, "TELEPHONE_NUMBER"),
(51, 63, "MOBILE_NUMBER"),
(64, 71, "STATE_FULL"),
]
}),
(
"46804 812-201-3793 Fort Wayne Indiana IN 2041 Cessna Drive 260-435-5924"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "MOBILE_NUMBER"),
(19, 29, "CITY"),
(30, 37, "STATE_FULL"),
(38, 40, "STATE"),
(41, 58, "STREET_ADDRESS"),
(59, 71, "TELEPHONE_NUMBER"),
]
}),
(
"46804 260-435-5924 2041 Cessna Drive IN 812-201-3793 Fort Wayne Indiana"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "TELEPHONE_NUMBER"),
(19, 36, "STREET_ADDRESS"),
(37, 39, "STATE"),
(40, 52, "MOBILE_NUMBER"),
(53, 63, "CITY"),
(64, 71, "STATE_FULL"),
]
}),
(
"46804 Fort Wayne IN Indiana 260-435-5924 812-201-3793 2041 Cessna Drive"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 16, "CITY"),
(17, 19, "STATE"),
(20, 27, "STATE_FULL"),
(28, 40, "TELEPHONE_NUMBER"),
(41, 53, "MOBILE_NUMBER"),
(54, 71, "STREET_ADDRESS"),
]
}),
(
"260-435-5924 2041 Cessna Drive Fort Wayne Indiana 812-201-3793 46804 IN"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 30, "STREET_ADDRESS"),
(31, 41, "CITY"),
(42, 49, "STATE_FULL"),
(50, 62, "MOBILE_NUMBER"),
(63, 68, "ZIPCODE"),
(69, 71, "STATE"),
]
}),
(
"2041 Cessna Drive Fort Wayne Indiana 46804 260-435-5924 IN 812-201-3793"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 28, "CITY"),
(29, 36, "STATE_FULL"),
(37, 42, "ZIPCODE"),
(43, 55, "TELEPHONE_NUMBER"),
(56, 58, "STATE"),
(59, 71, "MOBILE_NUMBER"),
]
}),
(
"1751 Strother Street Birmingham 205-954-8341 35203 Alabama 205-569-0918 AL"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 31, "CITY"),
(32, 44, "MOBILE_NUMBER"),
(45, 50, "ZIPCODE"),
(51, 58, "STATE_FULL"),
(59, 71, "TELEPHONE_NUMBER"),
(72, 74, "STATE"),
]
}),
(
"Birmingham 205-569-0918 1751 Strother Street 35203 Alabama AL 205-954-8341"
, {
"entities":[
(0, 10, "CITY"),
(11, 23, "TELEPHONE_NUMBER"),
(24, 44, "STREET_ADDRESS"),
(45, 50, "ZIPCODE"),
(51, 58, "STATE_FULL"),
(59, 61, "STATE"),
(62, 74, "MOBILE_NUMBER"),
]
}),
(
"AL 205-569-0918 1751 Strother Street Birmingham Alabama 35203 205-954-8341"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "TELEPHONE_NUMBER"),
(16, 36, "STREET_ADDRESS"),
(37, 47, "CITY"),
(48, 55, "STATE_FULL"),
(56, 61, "ZIPCODE"),
(62, 74, "MOBILE_NUMBER"),
]
}),
(
"Alabama 205-954-8341 205-569-0918 35203 Birmingham 1751 Strother Street AL"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 20, "MOBILE_NUMBER"),
(21, 33, "TELEPHONE_NUMBER"),
(34, 39, "ZIPCODE"),
(40, 50, "CITY"),
(51, 71, "STREET_ADDRESS"),
(72, 74, "STATE"),
]
}),
(
"Alabama 205-954-8341 35203 1751 Strother Street Birmingham 205-569-0918 AL"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 20, "MOBILE_NUMBER"),
(21, 26, "ZIPCODE"),
(27, 47, "STREET_ADDRESS"),
(48, 58, "CITY"),
(59, 71, "TELEPHONE_NUMBER"),
(72, 74, "STATE"),
]
}),
(
"Birmingham 35203 1751 Strother Street Alabama AL 205-569-0918 205-954-8341"
, {
"entities":[
(0, 10, "CITY"),
(11, 16, "ZIPCODE"),
(17, 37, "STREET_ADDRESS"),
(38, 45, "STATE_FULL"),
(46, 48, "STATE"),
(49, 61, "TELEPHONE_NUMBER"),
(62, 74, "MOBILE_NUMBER"),
]
}),
(
"35203 205-569-0918 Birmingham Alabama 205-954-8341 1751 Strother Street AL"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "TELEPHONE_NUMBER"),
(19, 29, "CITY"),
(30, 37, "STATE_FULL"),
(38, 50, "MOBILE_NUMBER"),
(51, 71, "STREET_ADDRESS"),
(72, 74, "STATE"),
]
}),
(
"205-954-8341 35203 AL Alabama Birmingham 205-569-0918 1751 Strother Street"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 21, "STATE"),
(22, 29, "STATE_FULL"),
(30, 40, "CITY"),
(41, 53, "TELEPHONE_NUMBER"),
(54, 74, "STREET_ADDRESS"),
]
}),
(
"Alabama AL 1751 Strother Street 205-954-8341 Birmingham 35203 205-569-0918"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 10, "STATE"),
(11, 31, "STREET_ADDRESS"),
(32, 44, "MOBILE_NUMBER"),
(45, 55, "CITY"),
(56, 61, "ZIPCODE"),
(62, 74, "TELEPHONE_NUMBER"),
]
}),
(
"205-954-8341 1751 Strother Street 35203 Alabama 205-569-0918 Birmingham AL"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 33, "STREET_ADDRESS"),
(34, 39, "ZIPCODE"),
(40, 47, "STATE_FULL"),
(48, 60, "TELEPHONE_NUMBER"),
(61, 71, "CITY"),
(72, 74, "STATE"),
]
}),
(
"Chicago 60626 Illinois 773-761-2359 IL 708-252-3497 3462 Vesta Drive"
, {
"entities":[
(0, 7, "CITY"),
(8, 13, "ZIPCODE"),
(14, 22, "STATE_FULL"),
(23, 35, "TELEPHONE_NUMBER"),
(36, 38, "STATE"),
(39, 51, "MOBILE_NUMBER"),
(52, 68, "STREET_ADDRESS"),
]
}),
(
"Chicago IL 708-252-3497 3462 Vesta Drive 60626 773-761-2359 Illinois"
, {
"entities":[
(0, 7, "CITY"),
(8, 10, "STATE"),
(11, 23, "MOBILE_NUMBER"),
(24, 40, "STREET_ADDRESS"),
(41, 46, "ZIPCODE"),
(47, 59, "TELEPHONE_NUMBER"),
(60, 68, "STATE_FULL"),
]
}),
(
"Chicago Illinois 3462 Vesta Drive IL 708-252-3497 773-761-2359 60626"
, {
"entities":[
(0, 7, "CITY"),
(8, 16, "STATE_FULL"),
(17, 33, "STREET_ADDRESS"),
(34, 36, "STATE"),
(37, 49, "MOBILE_NUMBER"),
(50, 62, "TELEPHONE_NUMBER"),
(63, 68, "ZIPCODE"),
]
}),
(
"708-252-3497 3462 Vesta Drive Illinois 60626 Chicago IL 773-761-2359"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 29, "STREET_ADDRESS"),
(30, 38, "STATE_FULL"),
(39, 44, "ZIPCODE"),
(45, 52, "CITY"),
(53, 55, "STATE"),
(56, 68, "TELEPHONE_NUMBER"),
]
}),
(
"773-761-2359 Chicago IL 60626 Illinois 3462 Vesta Drive 708-252-3497"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 20, "CITY"),
(21, 23, "STATE"),
(24, 29, "ZIPCODE"),
(30, 38, "STATE_FULL"),
(39, 55, "STREET_ADDRESS"),
(56, 68, "MOBILE_NUMBER"),
]
}),
(
"708-252-3497 3462 Vesta Drive 773-761-2359 IL Chicago Illinois 60626"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 29, "STREET_ADDRESS"),
(30, 42, "TELEPHONE_NUMBER"),
(43, 45, "STATE"),
(46, 53, "CITY"),
(54, 62, "STATE_FULL"),
(63, 68, "ZIPCODE"),
]
}),
(
"3462 Vesta Drive Chicago 773-761-2359 60626 708-252-3497 Illinois IL"
, {
"entities":[
(0, 16, "STREET_ADDRESS"),
(17, 24, "CITY"),
(25, 37, "TELEPHONE_NUMBER"),
(38, 43, "ZIPCODE"),
(44, 56, "MOBILE_NUMBER"),
(57, 65, "STATE_FULL"),
(66, 68, "STATE"),
]
}),
(
"708-252-3497 773-761-2359 Illinois 3462 Vesta Drive 60626 Chicago IL"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 25, "TELEPHONE_NUMBER"),
(26, 34, "STATE_FULL"),
(35, 51, "STREET_ADDRESS"),
(52, 57, "ZIPCODE"),
(58, 65, "CITY"),
(66, 68, "STATE"),
]
}),
(
"3462 Vesta Drive Illinois 708-252-3497 IL Chicago 773-761-2359 60626"
, {
"entities":[
(0, 16, "STREET_ADDRESS"),
(17, 25, "STATE_FULL"),
(26, 38, "MOBILE_NUMBER"),
(39, 41, "STATE"),
(42, 49, "CITY"),
(50, 62, "TELEPHONE_NUMBER"),
(63, 68, "ZIPCODE"),
]
}),
(
"IL Illinois 3462 Vesta Drive 708-252-3497 773-761-2359 60626 Chicago"
, {
"entities":[
(0, 2, "STATE"),
(3, 11, "STATE_FULL"),
(12, 28, "STREET_ADDRESS"),
(29, 41, "MOBILE_NUMBER"),
(42, 54, "TELEPHONE_NUMBER"),
(55, 60, "ZIPCODE"),
(61, 68, "CITY"),
]
}),
(
"Hollywood 323-468-4429 CA 90028 4271 Red Maple Drive California 714-852-3285"
, {
"entities":[
(0, 9, "CITY"),
(10, 22, "TELEPHONE_NUMBER"),
(23, 25, "STATE"),
(26, 31, "ZIPCODE"),
(32, 52, "STREET_ADDRESS"),
(53, 63, "STATE_FULL"),
(64, 76, "MOBILE_NUMBER"),
]
}),
(
"California 90028 4271 Red Maple Drive 714-852-3285 Hollywood 323-468-4429 CA"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 16, "ZIPCODE"),
(17, 37, "STREET_ADDRESS"),
(38, 50, "MOBILE_NUMBER"),
(51, 60, "CITY"),
(61, 73, "TELEPHONE_NUMBER"),
(74, 76, "STATE"),
]
}),
(
"4271 Red Maple Drive 323-468-4429 90028 CA Hollywood California 714-852-3285"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 33, "TELEPHONE_NUMBER"),
(34, 39, "ZIPCODE"),
(40, 42, "STATE"),
(43, 52, "CITY"),
(53, 63, "STATE_FULL"),
(64, 76, "MOBILE_NUMBER"),
]
}),
(
"90028 323-468-4429 California CA 4271 Red Maple Drive 714-852-3285 Hollywood"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "TELEPHONE_NUMBER"),
(19, 29, "STATE_FULL"),
(30, 32, "STATE"),
(33, 53, "STREET_ADDRESS"),
(54, 66, "MOBILE_NUMBER"),
(67, 76, "CITY"),
]
}),
(
"90028 323-468-4429 714-852-3285 Hollywood California CA 4271 Red Maple Drive"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "TELEPHONE_NUMBER"),
(19, 31, "MOBILE_NUMBER"),
(32, 41, "CITY"),
(42, 52, "STATE_FULL"),
(53, 55, "STATE"),
(56, 76, "STREET_ADDRESS"),
]
}),
(
"California 4271 Red Maple Drive CA 90028 323-468-4429 714-852-3285 Hollywood"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 31, "STREET_ADDRESS"),
(32, 34, "STATE"),
(35, 40, "ZIPCODE"),
(41, 53, "TELEPHONE_NUMBER"),
(54, 66, "MOBILE_NUMBER"),
(67, 76, "CITY"),
]
}),
(
"323-468-4429 CA 90028 714-852-3285 Hollywood California 4271 Red Maple Drive"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 15, "STATE"),
(16, 21, "ZIPCODE"),
(22, 34, "MOBILE_NUMBER"),
(35, 44, "CITY"),
(45, 55, "STATE_FULL"),
(56, 76, "STREET_ADDRESS"),
]
}),
(
"323-468-4429 CA 714-852-3285 Hollywood California 4271 Red Maple Drive 90028"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 15, "STATE"),
(16, 28, "MOBILE_NUMBER"),
(29, 38, "CITY"),
(39, 49, "STATE_FULL"),
(50, 70, "STREET_ADDRESS"),
(71, 76, "ZIPCODE"),
]
}),
(
"714-852-3285 CA 90028 4271 Red Maple Drive California 323-468-4429 Hollywood"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 15, "STATE"),
(16, 21, "ZIPCODE"),
(22, 42, "STREET_ADDRESS"),
(43, 53, "STATE_FULL"),
(54, 66, "TELEPHONE_NUMBER"),
(67, 76, "CITY"),
]
}),
(
"714-852-3285 4271 Red Maple Drive CA 323-468-4429 California Hollywood 90028"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 33, "STREET_ADDRESS"),
(34, 36, "STATE"),
(37, 49, "TELEPHONE_NUMBER"),
(50, 60, "STATE_FULL"),
(61, 70, "CITY"),
(71, 76, "ZIPCODE"),
]
}),
(
"29424 SC 843-730-3828 843-577-7991 South Carolina Charleston free 4706 Khale Street"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 21, "MOBILE_NUMBER"),
(22, 34, "TELEPHONE_NUMBER"),
(35, 49, "STATE_FULL"),
(50, 60, "CITY"),
(66, 83, "STREET_ADDRESS"),
]
}),
(
"Charleston 843-577-7991 free SC 29424 4706 Khale Street South Carolina 843-730-3828"
, {
"entities":[
(0, 10, "CITY"),
(11, 23, "TELEPHONE_NUMBER"),
(29, 31, "STATE"),
(32, 37, "ZIPCODE"),
(38, 55, "STREET_ADDRESS"),
(56, 70, "STATE_FULL"),
(71, 83, "MOBILE_NUMBER"),
]
}),
(
"free Charleston SC 4706 Khale Street 29424 843-577-7991 South Carolina 843-730-3828"
, {
"entities":[
(5, 15, "CITY"),
(16, 18, "STATE"),
(19, 36, "STREET_ADDRESS"),
(37, 42, "ZIPCODE"),
(43, 55, "TELEPHONE_NUMBER"),
(56, 70, "STATE_FULL"),
(71, 83, "MOBILE_NUMBER"),
]
}),
(
"Charleston free 843-577-7991 SC South Carolina 843-730-3828 4706 Khale Street 29424"
, {
"entities":[
(0, 10, "CITY"),
(16, 28, "TELEPHONE_NUMBER"),
(29, 31, "STATE"),
(32, 46, "STATE_FULL"),
(47, 59, "MOBILE_NUMBER"),
(60, 77, "STREET_ADDRESS"),
(78, 83, "ZIPCODE"),
]
}),
(
"843-730-3828 Charleston 4706 Khale Street 843-577-7991 free SC South Carolina 29424"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 23, "CITY"),
(24, 41, "STREET_ADDRESS"),
(42, 54, "TELEPHONE_NUMBER"),
(60, 62, "STATE"),
(63, 77, "STATE_FULL"),
(78, 83, "ZIPCODE"),
]
}),
(
"4706 Khale Street 29424 SC South Carolina 843-577-7991 843-730-3828 Charleston free"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 23, "ZIPCODE"),
(24, 26, "STATE"),
(27, 41, "STATE_FULL"),
(42, 54, "TELEPHONE_NUMBER"),
(55, 67, "MOBILE_NUMBER"),
(68, 78, "CITY"),
]
}),
(
"South Carolina free Charleston SC 843-577-7991 4706 Khale Street 29424 843-730-3828"
, {
"entities":[
(0, 14, "STATE_FULL"),
(20, 30, "CITY"),
(31, 33, "STATE"),
(34, 46, "TELEPHONE_NUMBER"),
(47, 64, "STREET_ADDRESS"),
(65, 70, "ZIPCODE"),
(71, 83, "MOBILE_NUMBER"),
]
}),
(
"Charleston SC free 29424 843-577-7991 South Carolina 843-730-3828 4706 Khale Street"
, {
"entities":[
(0, 10, "CITY"),
(11, 13, "STATE"),
(19, 24, "ZIPCODE"),
(25, 37, "TELEPHONE_NUMBER"),
(38, 52, "STATE_FULL"),
(53, 65, "MOBILE_NUMBER"),
(66, 83, "STREET_ADDRESS"),
]
}),
(
"South Carolina Charleston free 29424 4706 Khale Street 843-730-3828 843-577-7991 SC"
, {
"entities":[
(0, 14, "STATE_FULL"),
(15, 25, "CITY"),
(31, 36, "ZIPCODE"),
(37, 54, "STREET_ADDRESS"),
(55, 67, "MOBILE_NUMBER"),
(68, 80, "TELEPHONE_NUMBER"),
(81, 83, "STATE"),
]
}),
(
"SC 29424 Charleston 4706 Khale Street South Carolina free 843-577-7991 843-730-3828"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 19, "CITY"),
(20, 37, "STREET_ADDRESS"),
(38, 52, "STATE_FULL"),
(58, 70, "TELEPHONE_NUMBER"),
(71, 83, "MOBILE_NUMBER"),
]
}),
(
"216-816-5957 Independence 440-490-6570 44131 Ohio 1092 Bingamon Road OH"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 25, "CITY"),
(26, 38, "TELEPHONE_NUMBER"),
(39, 44, "ZIPCODE"),
(45, 49, "STATE_FULL"),
(50, 68, "STREET_ADDRESS"),
(69, 71, "STATE"),
]
}),
(
"Independence 216-816-5957 44131 Ohio 1092 Bingamon Road OH 440-490-6570"
, {
"entities":[
(0, 12, "CITY"),
(13, 25, "MOBILE_NUMBER"),
(26, 31, "ZIPCODE"),
(32, 36, "STATE_FULL"),
(37, 55, "STREET_ADDRESS"),
(56, 58, "STATE"),
(59, 71, "TELEPHONE_NUMBER"),
]
}),
(
"44131 OH 1092 Bingamon Road Independence Ohio 440-490-6570 216-816-5957"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 27, "STREET_ADDRESS"),
(28, 40, "CITY"),
(41, 45, "STATE_FULL"),
(46, 58, "TELEPHONE_NUMBER"),
(59, 71, "MOBILE_NUMBER"),
]
}),
(
"1092 Bingamon Road OH 44131 Independence 440-490-6570 216-816-5957 Ohio"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 21, "STATE"),
(22, 27, "ZIPCODE"),
(28, 40, "CITY"),
(41, 53, "TELEPHONE_NUMBER"),
(54, 66, "MOBILE_NUMBER"),
(67, 71, "STATE_FULL"),
]
}),
(
"44131 216-816-5957 OH Ohio Independence 1092 Bingamon Road 440-490-6570"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "MOBILE_NUMBER"),
(19, 21, "STATE"),
(22, 26, "STATE_FULL"),
(27, 39, "CITY"),
(40, 58, "STREET_ADDRESS"),
(59, 71, "TELEPHONE_NUMBER"),
]
}),
(
"216-816-5957 Independence OH 44131 1092 Bingamon Road 440-490-6570 Ohio"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 25, "CITY"),
(26, 28, "STATE"),
(29, 34, "ZIPCODE"),
(35, 53, "STREET_ADDRESS"),
(54, 66, "TELEPHONE_NUMBER"),
(67, 71, "STATE_FULL"),
]
}),
(
"44131 1092 Bingamon Road Ohio 440-490-6570 OH 216-816-5957 Independence"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 24, "STREET_ADDRESS"),
(25, 29, "STATE_FULL"),
(30, 42, "TELEPHONE_NUMBER"),
(43, 45, "STATE"),
(46, 58, "MOBILE_NUMBER"),
(59, 71, "CITY"),
]
}),
(
"216-816-5957 44131 440-490-6570 1092 Bingamon Road OH Ohio Independence"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 31, "TELEPHONE_NUMBER"),
(32, 50, "STREET_ADDRESS"),
(51, 53, "STATE"),
(54, 58, "STATE_FULL"),
(59, 71, "CITY"),
]
}),
(
"1092 Bingamon Road Ohio Independence OH 216-816-5957 44131 440-490-6570"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 23, "STATE_FULL"),
(24, 36, "CITY"),
(37, 39, "STATE"),
(40, 52, "MOBILE_NUMBER"),
(53, 58, "ZIPCODE"),
(59, 71, "TELEPHONE_NUMBER"),
]
}),
(
"OH 1092 Bingamon Road 216-816-5957 Ohio Independence 440-490-6570 44131"
, {
"entities":[
(0, 2, "STATE"),
(3, 21, "STREET_ADDRESS"),
(22, 34, "MOBILE_NUMBER"),
(35, 39, "STATE_FULL"),
(40, 52, "CITY"),
(53, 65, "TELEPHONE_NUMBER"),
(66, 71, "ZIPCODE"),
]
}),
(
"GA Georgia 229-296-8655 31707 2255 Private Lane Albany 229-603-5152"
, {
"entities":[
(0, 2, "STATE"),
(3, 10, "STATE_FULL"),
(11, 23, "TELEPHONE_NUMBER"),
(24, 29, "ZIPCODE"),
(30, 47, "STREET_ADDRESS"),
(48, 54, "CITY"),
(55, 67, "MOBILE_NUMBER"),
]
}),
(
"229-603-5152 GA Georgia 229-296-8655 31707 Albany 2255 Private Lane"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 15, "STATE"),
(16, 23, "STATE_FULL"),
(24, 36, "TELEPHONE_NUMBER"),
(37, 42, "ZIPCODE"),
(43, 49, "CITY"),
(50, 67, "STREET_ADDRESS"),
]
}),
(
"Albany 31707 GA 229-296-8655 229-603-5152 Georgia 2255 Private Lane"
, {
"entities":[
(0, 6, "CITY"),
(7, 12, "ZIPCODE"),
(13, 15, "STATE"),
(16, 28, "TELEPHONE_NUMBER"),
(29, 41, "MOBILE_NUMBER"),
(42, 49, "STATE_FULL"),
(50, 67, "STREET_ADDRESS"),
]
}),
(
"Georgia 31707 229-296-8655 Albany GA 229-603-5152 2255 Private Lane"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 13, "ZIPCODE"),
(14, 26, "TELEPHONE_NUMBER"),
(27, 33, "CITY"),
(34, 36, "STATE"),
(37, 49, "MOBILE_NUMBER"),
(50, 67, "STREET_ADDRESS"),
]
}),
(
"31707 Albany 2255 Private Lane GA Georgia 229-603-5152 229-296-8655"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 12, "CITY"),
(13, 30, "STREET_ADDRESS"),
(31, 33, "STATE"),
(34, 41, "STATE_FULL"),
(42, 54, "MOBILE_NUMBER"),
(55, 67, "TELEPHONE_NUMBER"),
]
}),
(
"GA 2255 Private Lane 229-296-8655 Georgia 229-603-5152 Albany 31707"
, {
"entities":[
(0, 2, "STATE"),
(3, 20, "STREET_ADDRESS"),
(21, 33, "TELEPHONE_NUMBER"),
(34, 41, "STATE_FULL"),
(42, 54, "MOBILE_NUMBER"),
(55, 61, "CITY"),
(62, 67, "ZIPCODE"),
]
}),
(
"Georgia 2255 Private Lane GA 229-603-5152 229-296-8655 Albany 31707"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 25, "STREET_ADDRESS"),
(26, 28, "STATE"),
(29, 41, "MOBILE_NUMBER"),
(42, 54, "TELEPHONE_NUMBER"),
(55, 61, "CITY"),
(62, 67, "ZIPCODE"),
]
}),
(
"2255 Private Lane Georgia 229-603-5152 229-296-8655 GA 31707 Albany"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 25, "STATE_FULL"),
(26, 38, "MOBILE_NUMBER"),
(39, 51, "TELEPHONE_NUMBER"),
(52, 54, "STATE"),
(55, 60, "ZIPCODE"),
(61, 67, "CITY"),
]
}),
(
"31707 GA Albany 229-603-5152 2255 Private Lane Georgia 229-296-8655"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 15, "CITY"),
(16, 28, "MOBILE_NUMBER"),
(29, 46, "STREET_ADDRESS"),
(47, 54, "STATE_FULL"),
(55, 67, "TELEPHONE_NUMBER"),
]
}),
(
"229-296-8655 31707 229-603-5152 Georgia 2255 Private Lane GA Albany"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 31, "MOBILE_NUMBER"),
(32, 39, "STATE_FULL"),
(40, 57, "STREET_ADDRESS"),
(58, 60, "STATE"),
(61, 67, "CITY"),
]
}),
(
"Louisiana LA 985-300-1514 70001 2747 Bassel Street 504-408-6000 Metairie"
, {
"entities":[
(0, 9, "STATE_FULL"),
(10, 12, "STATE"),
(13, 25, "TELEPHONE_NUMBER"),
(26, 31, "ZIPCODE"),
(32, 50, "STREET_ADDRESS"),
(51, 63, "MOBILE_NUMBER"),
(64, 72, "CITY"),
]
}),
(
"2747 Bassel Street Metairie 504-408-6000 70001 LA 985-300-1514 Louisiana"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 27, "CITY"),
(28, 40, "MOBILE_NUMBER"),
(41, 46, "ZIPCODE"),
(47, 49, "STATE"),
(50, 62, "TELEPHONE_NUMBER"),
(63, 72, "STATE_FULL"),
]
}),
(
"LA 504-408-6000 Metairie Louisiana 70001 2747 Bassel Street 985-300-1514"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "MOBILE_NUMBER"),
(16, 24, "CITY"),
(25, 34, "STATE_FULL"),
(35, 40, "ZIPCODE"),
(41, 59, "STREET_ADDRESS"),
(60, 72, "TELEPHONE_NUMBER"),
]
}),
(
"Metairie Louisiana 985-300-1514 70001 LA 504-408-6000 2747 Bassel Street"
, {
"entities":[
(0, 8, "CITY"),
(9, 18, "STATE_FULL"),
(19, 31, "TELEPHONE_NUMBER"),
(32, 37, "ZIPCODE"),
(38, 40, "STATE"),
(41, 53, "MOBILE_NUMBER"),
(54, 72, "STREET_ADDRESS"),
]
}),
(
"Metairie 2747 Bassel Street Louisiana LA 985-300-1514 504-408-6000 70001"
, {
"entities":[
(0, 8, "CITY"),
(9, 27, "STREET_ADDRESS"),
(28, 37, "STATE_FULL"),
(38, 40, "STATE"),
(41, 53, "TELEPHONE_NUMBER"),
(54, 66, "MOBILE_NUMBER"),
(67, 72, "ZIPCODE"),
]
}),
(
"Metairie LA 70001 Louisiana 2747 Bassel Street 504-408-6000 985-300-1514"
, {
"entities":[
(0, 8, "CITY"),
(9, 11, "STATE"),
(12, 17, "ZIPCODE"),
(18, 27, "STATE_FULL"),
(28, 46, "STREET_ADDRESS"),
(47, 59, "MOBILE_NUMBER"),
(60, 72, "TELEPHONE_NUMBER"),
]
}),
(
"Metairie LA Louisiana 70001 2747 Bassel Street 985-300-1514 504-408-6000"
, {
"entities":[
(0, 8, "CITY"),
(9, 11, "STATE"),
(12, 21, "STATE_FULL"),
(22, 27, "ZIPCODE"),
(28, 46, "STREET_ADDRESS"),
(47, 59, "TELEPHONE_NUMBER"),
(60, 72, "MOBILE_NUMBER"),
]
}),
(
"Metairie LA 985-300-1514 Louisiana 70001 504-408-6000 2747 Bassel Street"
, {
"entities":[
(0, 8, "CITY"),
(9, 11, "STATE"),
(12, 24, "TELEPHONE_NUMBER"),
(25, 34, "STATE_FULL"),
(35, 40, "ZIPCODE"),
(41, 53, "MOBILE_NUMBER"),
(54, 72, "STREET_ADDRESS"),
]
}),
(
"LA Metairie 70001 Louisiana 985-300-1514 2747 Bassel Street 504-408-6000"
, {
"entities":[
(0, 2, "STATE"),
(3, 11, "CITY"),
(12, 17, "ZIPCODE"),
(18, 27, "STATE_FULL"),
(28, 40, "TELEPHONE_NUMBER"),
(41, 59, "STREET_ADDRESS"),
(60, 72, "MOBILE_NUMBER"),
]
}),
(
"LA Louisiana 985-300-1514 2747 Bassel Street 70001 Metairie 504-408-6000"
, {
"entities":[
(0, 2, "STATE"),
(3, 12, "STATE_FULL"),
(13, 25, "TELEPHONE_NUMBER"),
(26, 44, "STREET_ADDRESS"),
(45, 50, "ZIPCODE"),
(51, 59, "CITY"),
(60, 72, "MOBILE_NUMBER"),
]
}),
(
"1302 Haul Road California 94025 CA 619-361-8704 650-926-1286 Menlo Park"
, {
"entities":[
(0, 14, "STREET_ADDRESS"),
(15, 25, "STATE_FULL"),
(26, 31, "ZIPCODE"),
(32, 34, "STATE"),
(35, 47, "MOBILE_NUMBER"),
(48, 60, "TELEPHONE_NUMBER"),
(61, 71, "CITY"),
]
}),
(
"1302 Haul Road Menlo Park California 650-926-1286 94025 CA 619-361-8704"
, {
"entities":[
(0, 14, "STREET_ADDRESS"),
(15, 25, "CITY"),
(26, 36, "STATE_FULL"),
(37, 49, "TELEPHONE_NUMBER"),
(50, 55, "ZIPCODE"),
(56, 58, "STATE"),
(59, 71, "MOBILE_NUMBER"),
]
}),
(
"1302 Haul Road 650-926-1286 94025 619-361-8704 CA California Menlo Park"
, {
"entities":[
(0, 14, "STREET_ADDRESS"),
(15, 27, "TELEPHONE_NUMBER"),
(28, 33, "ZIPCODE"),
(34, 46, "MOBILE_NUMBER"),
(47, 49, "STATE"),
(50, 60, "STATE_FULL"),
(61, 71, "CITY"),
]
}),
(
"Menlo Park California CA 650-926-1286 619-361-8704 94025 1302 Haul Road"
, {
"entities":[
(0, 10, "CITY"),
(11, 21, "STATE_FULL"),
(22, 24, "STATE"),
(25, 37, "TELEPHONE_NUMBER"),
(38, 50, "MOBILE_NUMBER"),
(51, 56, "ZIPCODE"),
(57, 71, "STREET_ADDRESS"),
]
}),
(
"1302 Haul Road 94025 California 619-361-8704 650-926-1286 Menlo Park CA"
, {
"entities":[
(0, 14, "STREET_ADDRESS"),
(15, 20, "ZIPCODE"),
(21, 31, "STATE_FULL"),
(32, 44, "MOBILE_NUMBER"),
(45, 57, "TELEPHONE_NUMBER"),
(58, 68, "CITY"),
(69, 71, "STATE"),
]
}),
(
"CA Menlo Park 1302 Haul Road 94025 California 619-361-8704 650-926-1286"
, {
"entities":[
(0, 2, "STATE"),
(3, 13, "CITY"),
(14, 28, "STREET_ADDRESS"),
(29, 34, "ZIPCODE"),
(35, 45, "STATE_FULL"),
(46, 58, "MOBILE_NUMBER"),
(59, 71, "TELEPHONE_NUMBER"),
]
}),
(
"1302 Haul Road 650-926-1286 California CA 94025 Menlo Park 619-361-8704"
, {
"entities":[
(0, 14, "STREET_ADDRESS"),
(15, 27, "TELEPHONE_NUMBER"),
(28, 38, "STATE_FULL"),
(39, 41, "STATE"),
(42, 47, "ZIPCODE"),
(48, 58, "CITY"),
(59, 71, "MOBILE_NUMBER"),
]
}),
(
"Menlo Park 94025 1302 Haul Road CA California 619-361-8704 650-926-1286"
, {
"entities":[
(0, 10, "CITY"),
(11, 16, "ZIPCODE"),
(17, 31, "STREET_ADDRESS"),
(32, 34, "STATE"),
(35, 45, "STATE_FULL"),
(46, 58, "MOBILE_NUMBER"),
(59, 71, "TELEPHONE_NUMBER"),
]
}),
(
"650-926-1286 Menlo Park 619-361-8704 94025 CA California 1302 Haul Road"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 23, "CITY"),
(24, 36, "MOBILE_NUMBER"),
(37, 42, "ZIPCODE"),
(43, 45, "STATE"),
(46, 56, "STATE_FULL"),
(57, 71, "STREET_ADDRESS"),
]
}),
(
"1302 Haul Road 94025 Menlo Park 650-926-1286 California 619-361-8704 CA"
, {
"entities":[
(0, 14, "STREET_ADDRESS"),
(15, 20, "ZIPCODE"),
(21, 31, "CITY"),
(32, 44, "TELEPHONE_NUMBER"),
(45, 55, "STATE_FULL"),
(56, 68, "MOBILE_NUMBER"),
(69, 71, "STATE"),
]
}),
(
"MO estimate 573-819-4058 573-268-4423 65207 Missouri Columbia 2172 Mandan Road"
, {
"entities":[
(0, 2, "STATE"),
(12, 24, "TELEPHONE_NUMBER"),
(25, 37, "MOBILE_NUMBER"),
(38, 43, "ZIPCODE"),
(44, 52, "STATE_FULL"),
(53, 61, "CITY"),
(62, 78, "STREET_ADDRESS"),
]
}),
(
"65207 Missouri MO 573-268-4423 2172 Mandan Road estimate Columbia 573-819-4058"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 14, "STATE_FULL"),
(15, 17, "STATE"),
(18, 30, "MOBILE_NUMBER"),
(31, 47, "STREET_ADDRESS"),
(57, 65, "CITY"),
(66, 78, "TELEPHONE_NUMBER"),
]
}),
(
"65207 Missouri Columbia 2172 Mandan Road 573-819-4058 MO estimate 573-268-4423"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 14, "STATE_FULL"),
(15, 23, "CITY"),
(24, 40, "STREET_ADDRESS"),
(41, 53, "TELEPHONE_NUMBER"),
(54, 56, "STATE"),
(66, 78, "MOBILE_NUMBER"),
]
}),
(
"estimate 65207 573-819-4058 2172 Mandan Road MO Missouri Columbia 573-268-4423"
, {
"entities":[
(9, 14, "ZIPCODE"),
(15, 27, "TELEPHONE_NUMBER"),
(28, 44, "STREET_ADDRESS"),
(45, 47, "STATE"),
(48, 56, "STATE_FULL"),
(57, 65, "CITY"),
(66, 78, "MOBILE_NUMBER"),
]
}),
(
"Columbia 65207 Missouri estimate 573-819-4058 MO 573-268-4423 2172 Mandan Road"
, {
"entities":[
(0, 8, "CITY"),
(9, 14, "ZIPCODE"),
(15, 23, "STATE_FULL"),
(33, 45, "TELEPHONE_NUMBER"),
(46, 48, "STATE"),
(49, 61, "MOBILE_NUMBER"),
(62, 78, "STREET_ADDRESS"),
]
}),
(
"estimate 2172 Mandan Road 573-819-4058 MO 573-268-4423 65207 Columbia Missouri"
, {
"entities":[
(9, 25, "STREET_ADDRESS"),
(26, 38, "TELEPHONE_NUMBER"),
(39, 41, "STATE"),
(42, 54, "MOBILE_NUMBER"),
(55, 60, "ZIPCODE"),
(61, 69, "CITY"),
(70, 78, "STATE_FULL"),
]
}),
(
"Missouri 573-819-4058 573-268-4423 MO Columbia 65207 estimate 2172 Mandan Road"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 21, "TELEPHONE_NUMBER"),
(22, 34, "MOBILE_NUMBER"),
(35, 37, "STATE"),
(38, 46, "CITY"),
(47, 52, "ZIPCODE"),
(62, 78, "STREET_ADDRESS"),
]
}),
(
"estimate Columbia 2172 Mandan Road 65207 Missouri 573-819-4058 573-268-4423 MO"
, {
"entities":[
(9, 17, "CITY"),
(18, 34, "STREET_ADDRESS"),
(35, 40, "ZIPCODE"),
(41, 49, "STATE_FULL"),
(50, 62, "TELEPHONE_NUMBER"),
(63, 75, "MOBILE_NUMBER"),
(76, 78, "STATE"),
]
}),
(
"2172 Mandan Road 65207 MO 573-268-4423 estimate Columbia 573-819-4058 Missouri"
, {
"entities":[
(0, 16, "STREET_ADDRESS"),
(17, 22, "ZIPCODE"),
(23, 25, "STATE"),
(26, 38, "MOBILE_NUMBER"),
(48, 56, "CITY"),
(57, 69, "TELEPHONE_NUMBER"),
(70, 78, "STATE_FULL"),
]
}),
(
"65207 573-268-4423 Missouri Columbia MO 2172 Mandan Road 573-819-4058 estimate"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "MOBILE_NUMBER"),
(19, 27, "STATE_FULL"),
(28, 36, "CITY"),
(37, 39, "STATE"),
(40, 56, "STREET_ADDRESS"),
(57, 69, "TELEPHONE_NUMBER"),
]
}),
(
"Mississippi 228-313-7199 1507 Kelley Road 39507 MS Gulfport 601-201-2925"
, {
"entities":[
(0, 11, "STATE_FULL"),
(12, 24, "TELEPHONE_NUMBER"),
(25, 41, "STREET_ADDRESS"),
(42, 47, "ZIPCODE"),
(48, 50, "STATE"),
(51, 59, "CITY"),
(60, 72, "MOBILE_NUMBER"),
]
}),
(
"39507 MS Gulfport 228-313-7199 601-201-2925 1507 Kelley Road Mississippi"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 17, "CITY"),
(18, 30, "TELEPHONE_NUMBER"),
(31, 43, "MOBILE_NUMBER"),
(44, 60, "STREET_ADDRESS"),
(61, 72, "STATE_FULL"),
]
}),
(
"MS 601-201-2925 Gulfport 39507 Mississippi 1507 Kelley Road 228-313-7199"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "MOBILE_NUMBER"),
(16, 24, "CITY"),
(25, 30, "ZIPCODE"),
(31, 42, "STATE_FULL"),
(43, 59, "STREET_ADDRESS"),
(60, 72, "TELEPHONE_NUMBER"),
]
}),
(
"Gulfport 601-201-2925 MS 228-313-7199 Mississippi 39507 1507 Kelley Road"
, {
"entities":[
(0, 8, "CITY"),
(9, 21, "MOBILE_NUMBER"),
(22, 24, "STATE"),
(25, 37, "TELEPHONE_NUMBER"),
(38, 49, "STATE_FULL"),
(50, 55, "ZIPCODE"),
(56, 72, "STREET_ADDRESS"),
]
}),
(
"MS 1507 Kelley Road 228-313-7199 Mississippi Gulfport 39507 601-201-2925"
, {
"entities":[
(0, 2, "STATE"),
(3, 19, "STREET_ADDRESS"),
(20, 32, "TELEPHONE_NUMBER"),
(33, 44, "STATE_FULL"),
(45, 53, "CITY"),
(54, 59, "ZIPCODE"),
(60, 72, "MOBILE_NUMBER"),
]
}),
(
"MS Gulfport 39507 228-313-7199 Mississippi 601-201-2925 1507 Kelley Road"
, {
"entities":[
(0, 2, "STATE"),
(3, 11, "CITY"),
(12, 17, "ZIPCODE"),
(18, 30, "TELEPHONE_NUMBER"),
(31, 42, "STATE_FULL"),
(43, 55, "MOBILE_NUMBER"),
(56, 72, "STREET_ADDRESS"),
]
}),
(
"1507 Kelley Road 601-201-2925 228-313-7199 39507 Mississippi MS Gulfport"
, {
"entities":[
(0, 16, "STREET_ADDRESS"),
(17, 29, "MOBILE_NUMBER"),
(30, 42, "TELEPHONE_NUMBER"),
(43, 48, "ZIPCODE"),
(49, 60, "STATE_FULL"),
(61, 63, "STATE"),
(64, 72, "CITY"),
]
}),
(
"39507 MS Mississippi 601-201-2925 1507 Kelley Road 228-313-7199 Gulfport"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 20, "STATE_FULL"),
(21, 33, "MOBILE_NUMBER"),
(34, 50, "STREET_ADDRESS"),
(51, 63, "TELEPHONE_NUMBER"),
(64, 72, "CITY"),
]
}),
(
"601-201-2925 MS Gulfport 39507 1507 Kelley Road Mississippi 228-313-7199"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 15, "STATE"),
(16, 24, "CITY"),
(25, 30, "ZIPCODE"),
(31, 47, "STREET_ADDRESS"),
(48, 59, "STATE_FULL"),
(60, 72, "TELEPHONE_NUMBER"),
]
}),
(
"Gulfport 601-201-2925 MS 1507 Kelley Road 228-313-7199 Mississippi 39507"
, {
"entities":[
(0, 8, "CITY"),
(9, 21, "MOBILE_NUMBER"),
(22, 24, "STATE"),
(25, 41, "STREET_ADDRESS"),
(42, 54, "TELEPHONE_NUMBER"),
(55, 66, "STATE_FULL"),
(67, 72, "ZIPCODE"),
]
}),
(
"Golden Valley 55427 651-789-5305 that 586 Laurel Lee MN Minnesota 218-979-9495"
, {
"entities":[
(0, 13, "CITY"),
(14, 19, "ZIPCODE"),
(20, 32, "TELEPHONE_NUMBER"),
(38, 52, "STREET_ADDRESS"),
(53, 55, "STATE"),
(56, 65, "STATE_FULL"),
(66, 78, "MOBILE_NUMBER"),
]
}),
(
"55427 651-789-5305 Golden Valley MN that 218-979-9495 Minnesota 586 Laurel Lee"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "TELEPHONE_NUMBER"),
(19, 32, "CITY"),
(33, 35, "STATE"),
(41, 53, "MOBILE_NUMBER"),
(54, 63, "STATE_FULL"),
(64, 78, "STREET_ADDRESS"),
]
}),
(
"651-789-5305 586 Laurel Lee 218-979-9495 55427 Minnesota Golden Valley that MN"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 27, "STREET_ADDRESS"),
(28, 40, "MOBILE_NUMBER"),
(41, 46, "ZIPCODE"),
(47, 56, "STATE_FULL"),
(57, 70, "CITY"),
(76, 78, "STATE"),
]
}),
(
"MN 651-789-5305 586 Laurel Lee Golden Valley Minnesota 218-979-9495 55427 that"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "TELEPHONE_NUMBER"),
(16, 30, "STREET_ADDRESS"),
(31, 44, "CITY"),
(45, 54, "STATE_FULL"),
(55, 67, "MOBILE_NUMBER"),
(68, 73, "ZIPCODE"),
]
}),
(
"Golden Valley 55427 Minnesota 218-979-9495 586 Laurel Lee MN 651-789-5305 that"
, {
"entities":[
(0, 13, "CITY"),
(14, 19, "ZIPCODE"),
(20, 29, "STATE_FULL"),
(30, 42, "MOBILE_NUMBER"),
(43, 57, "STREET_ADDRESS"),
(58, 60, "STATE"),
(61, 73, "TELEPHONE_NUMBER"),
]
}),
(
"55427 that 586 Laurel Lee 218-979-9495 MN Minnesota 651-789-5305 Golden Valley"
, {
"entities":[
(0, 5, "ZIPCODE"),
(11, 25, "STREET_ADDRESS"),
(26, 38, "MOBILE_NUMBER"),
(39, 41, "STATE"),
(42, 51, "STATE_FULL"),
(52, 64, "TELEPHONE_NUMBER"),
(65, 78, "CITY"),
]
}),
(
"MN 651-789-5305 218-979-9495 55427 Minnesota Golden Valley 586 Laurel Lee that"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "TELEPHONE_NUMBER"),
(16, 28, "MOBILE_NUMBER"),
(29, 34, "ZIPCODE"),
(35, 44, "STATE_FULL"),
(45, 58, "CITY"),
(59, 73, "STREET_ADDRESS"),
]
}),
(
"Golden Valley 218-979-9495 Minnesota that MN 586 Laurel Lee 651-789-5305 55427"
, {
"entities":[
(0, 13, "CITY"),
(14, 26, "MOBILE_NUMBER"),
(27, 36, "STATE_FULL"),
(42, 44, "STATE"),
(45, 59, "STREET_ADDRESS"),
(60, 72, "TELEPHONE_NUMBER"),
(73, 78, "ZIPCODE"),
]
}),
(
"586 Laurel Lee Minnesota 55427 218-979-9495 651-789-5305 MN Golden Valley that"
, {
"entities":[
(0, 14, "STREET_ADDRESS"),
(15, 24, "STATE_FULL"),
(25, 30, "ZIPCODE"),
(31, 43, "MOBILE_NUMBER"),
(44, 56, "TELEPHONE_NUMBER"),
(57, 59, "STATE"),
(60, 73, "CITY"),
]
}),
(
"586 Laurel Lee Minnesota 55427 651-789-5305 Golden Valley 218-979-9495 MN that"
, {
"entities":[
(0, 14, "STREET_ADDRESS"),
(15, 24, "STATE_FULL"),
(25, 30, "ZIPCODE"),
(31, 43, "TELEPHONE_NUMBER"),
(44, 57, "CITY"),
(58, 70, "MOBILE_NUMBER"),
(71, 73, "STATE"),
]
}),
(
"510-507-8694 4975 Clifford Street Oakland 94609 California 510-654-6444 CA"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 33, "STREET_ADDRESS"),
(34, 41, "CITY"),
(42, 47, "ZIPCODE"),
(48, 58, "STATE_FULL"),
(59, 71, "TELEPHONE_NUMBER"),
(72, 74, "STATE"),
]
}),
(
"CA Oakland 510-507-8694 4975 Clifford Street 510-654-6444 94609 California"
, {
"entities":[
(0, 2, "STATE"),
(3, 10, "CITY"),
(11, 23, "MOBILE_NUMBER"),
(24, 44, "STREET_ADDRESS"),
(45, 57, "TELEPHONE_NUMBER"),
(58, 63, "ZIPCODE"),
(64, 74, "STATE_FULL"),
]
}),
(
"Oakland 4975 Clifford Street CA 510-654-6444 510-507-8694 94609 California"
, {
"entities":[
(0, 7, "CITY"),
(8, 28, "STREET_ADDRESS"),
(29, 31, "STATE"),
(32, 44, "TELEPHONE_NUMBER"),
(45, 57, "MOBILE_NUMBER"),
(58, 63, "ZIPCODE"),
(64, 74, "STATE_FULL"),
]
}),
(
"94609 510-507-8694 4975 Clifford Street CA Oakland 510-654-6444 California"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "MOBILE_NUMBER"),
(19, 39, "STREET_ADDRESS"),
(40, 42, "STATE"),
(43, 50, "CITY"),
(51, 63, "TELEPHONE_NUMBER"),
(64, 74, "STATE_FULL"),
]
}),
(
"California 4975 Clifford Street 510-507-8694 Oakland 94609 CA 510-654-6444"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 31, "STREET_ADDRESS"),
(32, 44, "MOBILE_NUMBER"),
(45, 52, "CITY"),
(53, 58, "ZIPCODE"),
(59, 61, "STATE"),
(62, 74, "TELEPHONE_NUMBER"),
]
}),
(
"California 510-654-6444 CA 510-507-8694 4975 Clifford Street 94609 Oakland"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 23, "TELEPHONE_NUMBER"),
(24, 26, "STATE"),
(27, 39, "MOBILE_NUMBER"),
(40, 60, "STREET_ADDRESS"),
(61, 66, "ZIPCODE"),
(67, 74, "CITY"),
]
}),
(
"4975 Clifford Street CA 510-654-6444 California Oakland 94609 510-507-8694"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 23, "STATE"),
(24, 36, "TELEPHONE_NUMBER"),
(37, 47, "STATE_FULL"),
(48, 55, "CITY"),
(56, 61, "ZIPCODE"),
(62, 74, "MOBILE_NUMBER"),
]
}),
(
"CA 510-654-6444 4975 Clifford Street 510-507-8694 California Oakland 94609"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "TELEPHONE_NUMBER"),
(16, 36, "STREET_ADDRESS"),
(37, 49, "MOBILE_NUMBER"),
(50, 60, "STATE_FULL"),
(61, 68, "CITY"),
(69, 74, "ZIPCODE"),
]
}),
(
"510-654-6444 Oakland 4975 Clifford Street CA California 510-507-8694 94609"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 20, "CITY"),
(21, 41, "STREET_ADDRESS"),
(42, 44, "STATE"),
(45, 55, "STATE_FULL"),
(56, 68, "MOBILE_NUMBER"),
(69, 74, "ZIPCODE"),
]
}),
(
"510-507-8694 Oakland CA 510-654-6444 4975 Clifford Street California 94609"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 20, "CITY"),
(21, 23, "STATE"),
(24, 36, "TELEPHONE_NUMBER"),
(37, 57, "STREET_ADDRESS"),
(58, 68, "STATE_FULL"),
(69, 74, "ZIPCODE"),
]
}),
(
"We 1831 Stoney Lane 75051 Texas Grand Prairie 972-933-6296 TX 214-314-8047"
, {
"entities":[
(3, 19, "STREET_ADDRESS"),
(20, 25, "ZIPCODE"),
(26, 31, "STATE_FULL"),
(32, 45, "CITY"),
(46, 58, "TELEPHONE_NUMBER"),
(59, 61, "STATE"),
(62, 74, "MOBILE_NUMBER"),
]
}),
(
"TX 1831 Stoney Lane Grand Prairie 75051 We 214-314-8047 Texas 972-933-6296"
, {
"entities":[
(0, 2, "STATE"),
(3, 19, "STREET_ADDRESS"),
(20, 33, "CITY"),
(34, 39, "ZIPCODE"),
(43, 55, "MOBILE_NUMBER"),
(56, 61, "STATE_FULL"),
(62, 74, "TELEPHONE_NUMBER"),
]
}),
(
"TX Texas 214-314-8047 75051 Grand Prairie 972-933-6296 We 1831 Stoney Lane"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "STATE_FULL"),
(9, 21, "MOBILE_NUMBER"),
(22, 27, "ZIPCODE"),
(28, 41, "CITY"),
(42, 54, "TELEPHONE_NUMBER"),
(58, 74, "STREET_ADDRESS"),
]
}),
(
"Grand Prairie 1831 Stoney Lane 214-314-8047 We 75051 TX 972-933-6296 Texas"
, {
"entities":[
(0, 13, "CITY"),
(14, 30, "STREET_ADDRESS"),
(31, 43, "MOBILE_NUMBER"),
(47, 52, "ZIPCODE"),
(53, 55, "STATE"),
(56, 68, "TELEPHONE_NUMBER"),
(69, 74, "STATE_FULL"),
]
}),
(
"972-933-6296 1831 Stoney Lane Texas We Grand Prairie 75051 214-314-8047 TX"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 29, "STREET_ADDRESS"),
(30, 35, "STATE_FULL"),
(39, 52, "CITY"),
(53, 58, "ZIPCODE"),
(59, 71, "MOBILE_NUMBER"),
(72, 74, "STATE"),
]
}),
(
"Grand Prairie TX 75051 We 214-314-8047 Texas 1831 Stoney Lane 972-933-6296"
, {
"entities":[
(0, 13, "CITY"),
(14, 16, "STATE"),
(17, 22, "ZIPCODE"),
(26, 38, "MOBILE_NUMBER"),
(39, 44, "STATE_FULL"),
(45, 61, "STREET_ADDRESS"),
(62, 74, "TELEPHONE_NUMBER"),
]
}),
(
"972-933-6296 1831 Stoney Lane We TX Grand Prairie Texas 75051 214-314-8047"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 29, "STREET_ADDRESS"),
(33, 35, "STATE"),
(36, 49, "CITY"),
(50, 55, "STATE_FULL"),
(56, 61, "ZIPCODE"),
(62, 74, "MOBILE_NUMBER"),
]
}),
(
"75051 TX Grand Prairie 972-933-6296 Texas 214-314-8047 We 1831 Stoney Lane"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 22, "CITY"),
(23, 35, "TELEPHONE_NUMBER"),
(36, 41, "STATE_FULL"),
(42, 54, "MOBILE_NUMBER"),
(58, 74, "STREET_ADDRESS"),
]
}),
(
"214-314-8047 We Texas 1831 Stoney Lane TX 972-933-6296 75051 Grand Prairie"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(16, 21, "STATE_FULL"),
(22, 38, "STREET_ADDRESS"),
(39, 41, "STATE"),
(42, 54, "TELEPHONE_NUMBER"),
(55, 60, "ZIPCODE"),
(61, 74, "CITY"),
]
}),
(
"1831 Stoney Lane 75051 972-933-6296 Grand Prairie 214-314-8047 Texas We TX"
, {
"entities":[
(0, 16, "STREET_ADDRESS"),
(17, 22, "ZIPCODE"),
(23, 35, "TELEPHONE_NUMBER"),
(36, 49, "CITY"),
(50, 62, "MOBILE_NUMBER"),
(63, 68, "STATE_FULL"),
(72, 74, "STATE"),
]
}),
(
"USE address Virginia 434-305-1345 22980 VA with Waynesboro 276-685-1931 1807 Worley Avenue"
, {
"entities":[
(12, 20, "STATE_FULL"),
(21, 33, "TELEPHONE_NUMBER"),
(34, 39, "ZIPCODE"),
(40, 42, "STATE"),
(48, 58, "CITY"),
(59, 71, "MOBILE_NUMBER"),
(72, 90, "STREET_ADDRESS"),
]
}),
(
"22980 VA Virginia USE 276-685-1931 with 434-305-1345 1807 Worley Avenue address Waynesboro"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 17, "STATE_FULL"),
(22, 34, "MOBILE_NUMBER"),
(40, 52, "TELEPHONE_NUMBER"),
(53, 71, "STREET_ADDRESS"),
(80, 90, "CITY"),
]
}),
(
"VA address Waynesboro Virginia 22980 276-685-1931 1807 Worley Avenue USE 434-305-1345 with"
, {
"entities":[
(0, 2, "STATE"),
(11, 21, "CITY"),
(22, 30, "STATE_FULL"),
(31, 36, "ZIPCODE"),
(37, 49, "MOBILE_NUMBER"),
(50, 68, "STREET_ADDRESS"),
(73, 85, "TELEPHONE_NUMBER"),
]
}),
(
"Virginia USE 22980 434-305-1345 VA 1807 Worley Avenue Waynesboro 276-685-1931 with address"
, {
"entities":[
(0, 8, "STATE_FULL"),
(13, 18, "ZIPCODE"),
(19, 31, "TELEPHONE_NUMBER"),
(32, 34, "STATE"),
(35, 53, "STREET_ADDRESS"),
(54, 64, "CITY"),
(65, 77, "MOBILE_NUMBER"),
]
}),
(
"address with 276-685-1931 VA 1807 Worley Avenue 434-305-1345 22980 Waynesboro USE Virginia"
, {
"entities":[
(13, 25, "MOBILE_NUMBER"),
(26, 28, "STATE"),
(29, 47, "STREET_ADDRESS"),
(48, 60, "TELEPHONE_NUMBER"),
(61, 66, "ZIPCODE"),
(67, 77, "CITY"),
(82, 90, "STATE_FULL"),
]
}),
(
"VA Waynesboro Virginia address with 1807 Worley Avenue 22980 USE 434-305-1345 276-685-1931"
, {
"entities":[
(0, 2, "STATE"),
(3, 13, "CITY"),
(14, 22, "STATE_FULL"),
(36, 54, "STREET_ADDRESS"),
(55, 60, "ZIPCODE"),
(65, 77, "TELEPHONE_NUMBER"),
(78, 90, "MOBILE_NUMBER"),
]
}),
(
"Virginia with 22980 276-685-1931 Waynesboro 434-305-1345 address 1807 Worley Avenue VA USE"
, {
"entities":[
(0, 8, "STATE_FULL"),
(14, 19, "ZIPCODE"),
(20, 32, "MOBILE_NUMBER"),
(33, 43, "CITY"),
(44, 56, "TELEPHONE_NUMBER"),
(65, 83, "STREET_ADDRESS"),
(84, 86, "STATE"),
]
}),
(
"Waynesboro address Virginia 276-685-1931 434-305-1345 22980 1807 Worley Avenue USE VA with"
, {
"entities":[
(0, 10, "CITY"),
(19, 27, "STATE_FULL"),
(28, 40, "MOBILE_NUMBER"),
(41, 53, "TELEPHONE_NUMBER"),
(54, 59, "ZIPCODE"),
(60, 78, "STREET_ADDRESS"),
(83, 85, "STATE"),
]
}),
(
"1807 Worley Avenue 22980 276-685-1931 with 434-305-1345 Virginia USE VA Waynesboro address"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 24, "ZIPCODE"),
(25, 37, "MOBILE_NUMBER"),
(43, 55, "TELEPHONE_NUMBER"),
(56, 64, "STATE_FULL"),
(69, 71, "STATE"),
(72, 82, "CITY"),
]
}),
(
"address with Waynesboro 22980 434-305-1345 VA 276-685-1931 Virginia USE 1807 Worley Avenue"
, {
"entities":[
(13, 23, "CITY"),
(24, 29, "ZIPCODE"),
(30, 42, "TELEPHONE_NUMBER"),
(43, 45, "STATE"),
(46, 58, "MOBILE_NUMBER"),
(59, 67, "STATE_FULL"),
(72, 90, "STREET_ADDRESS"),
]
}),
(
"Monterey 2880 Black Oak Hollow Road 95940 408-810-0168 CA 831-236-1907 California"
, {
"entities":[
(0, 8, "CITY"),
(9, 35, "STREET_ADDRESS"),
(36, 41, "ZIPCODE"),
(42, 54, "TELEPHONE_NUMBER"),
(55, 57, "STATE"),
(58, 70, "MOBILE_NUMBER"),
(71, 81, "STATE_FULL"),
]
}),
(
"Monterey CA 95940 408-810-0168 California 2880 Black Oak Hollow Road 831-236-1907"
, {
"entities":[
(0, 8, "CITY"),
(9, 11, "STATE"),
(12, 17, "ZIPCODE"),
(18, 30, "TELEPHONE_NUMBER"),
(31, 41, "STATE_FULL"),
(42, 68, "STREET_ADDRESS"),
(69, 81, "MOBILE_NUMBER"),
]
}),
(
"2880 Black Oak Hollow Road 831-236-1907 95940 408-810-0168 California CA Monterey"
, {
"entities":[
(0, 26, "STREET_ADDRESS"),
(27, 39, "MOBILE_NUMBER"),
(40, 45, "ZIPCODE"),
(46, 58, "TELEPHONE_NUMBER"),
(59, 69, "STATE_FULL"),
(70, 72, "STATE"),
(73, 81, "CITY"),
]
}),
(
"831-236-1907 California 408-810-0168 95940 2880 Black Oak Hollow Road Monterey CA"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 23, "STATE_FULL"),
(24, 36, "TELEPHONE_NUMBER"),
(37, 42, "ZIPCODE"),
(43, 69, "STREET_ADDRESS"),
(70, 78, "CITY"),
(79, 81, "STATE"),
]
}),
(
"408-810-0168 California 95940 CA 2880 Black Oak Hollow Road 831-236-1907 Monterey"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 23, "STATE_FULL"),
(24, 29, "ZIPCODE"),
(30, 32, "STATE"),
(33, 59, "STREET_ADDRESS"),
(60, 72, "MOBILE_NUMBER"),
(73, 81, "CITY"),
]
}),
(
"408-810-0168 CA Monterey 831-236-1907 2880 Black Oak Hollow Road California 95940"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 15, "STATE"),
(16, 24, "CITY"),
(25, 37, "MOBILE_NUMBER"),
(38, 64, "STREET_ADDRESS"),
(65, 75, "STATE_FULL"),
(76, 81, "ZIPCODE"),
]
}),
(
"831-236-1907 CA 95940 2880 Black Oak Hollow Road Monterey 408-810-0168 California"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 15, "STATE"),
(16, 21, "ZIPCODE"),
(22, 48, "STREET_ADDRESS"),
(49, 57, "CITY"),
(58, 70, "TELEPHONE_NUMBER"),
(71, 81, "STATE_FULL"),
]
}),
(
"408-810-0168 CA 2880 Black Oak Hollow Road Monterey California 831-236-1907 95940"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 15, "STATE"),
(16, 42, "STREET_ADDRESS"),
(43, 51, "CITY"),
(52, 62, "STATE_FULL"),
(63, 75, "MOBILE_NUMBER"),
(76, 81, "ZIPCODE"),
]
}),
(
"831-236-1907 2880 Black Oak Hollow Road 95940 CA 408-810-0168 Monterey California"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 39, "STREET_ADDRESS"),
(40, 45, "ZIPCODE"),
(46, 48, "STATE"),
(49, 61, "TELEPHONE_NUMBER"),
(62, 70, "CITY"),
(71, 81, "STATE_FULL"),
]
}),
(
"408-810-0168 2880 Black Oak Hollow Road 95940 California 831-236-1907 Monterey CA"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 39, "STREET_ADDRESS"),
(40, 45, "ZIPCODE"),
(46, 56, "STATE_FULL"),
(57, 69, "MOBILE_NUMBER"),
(70, 78, "CITY"),
(79, 81, "STATE"),
]
}),
(
"95113 707-797-1981 CA 1049 Pretty View Lane San Jose with California 408-429-4770"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "TELEPHONE_NUMBER"),
(19, 21, "STATE"),
(22, 43, "STREET_ADDRESS"),
(44, 52, "CITY"),
(58, 68, "STATE_FULL"),
(69, 81, "MOBILE_NUMBER"),
]
}),
(
"1049 Pretty View Lane with 95113 707-797-1981 California CA 408-429-4770 San Jose"
, {
"entities":[
(0, 21, "STREET_ADDRESS"),
(27, 32, "ZIPCODE"),
(33, 45, "TELEPHONE_NUMBER"),
(46, 56, "STATE_FULL"),
(57, 59, "STATE"),
(60, 72, "MOBILE_NUMBER"),
(73, 81, "CITY"),
]
}),
(
"408-429-4770 707-797-1981 California San Jose CA 95113 with 1049 Pretty View Lane"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 25, "TELEPHONE_NUMBER"),
(26, 36, "STATE_FULL"),
(37, 45, "CITY"),
(46, 48, "STATE"),
(49, 54, "ZIPCODE"),
(60, 81, "STREET_ADDRESS"),
]
}),
(
"95113 CA 408-429-4770 with 707-797-1981 San Jose California 1049 Pretty View Lane"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 21, "MOBILE_NUMBER"),
(27, 39, "TELEPHONE_NUMBER"),
(40, 48, "CITY"),
(49, 59, "STATE_FULL"),
(60, 81, "STREET_ADDRESS"),
]
}),
(
"1049 Pretty View Lane 408-429-4770 CA California with San Jose 707-797-1981 95113"
, {
"entities":[
(0, 21, "STREET_ADDRESS"),
(22, 34, "MOBILE_NUMBER"),
(35, 37, "STATE"),
(38, 48, "STATE_FULL"),
(54, 62, "CITY"),
(63, 75, "TELEPHONE_NUMBER"),
(76, 81, "ZIPCODE"),
]
}),
(
"95113 1049 Pretty View Lane California 408-429-4770 San Jose 707-797-1981 with CA"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 27, "STREET_ADDRESS"),
(28, 38, "STATE_FULL"),
(39, 51, "MOBILE_NUMBER"),
(52, 60, "CITY"),
(61, 73, "TELEPHONE_NUMBER"),
(79, 81, "STATE"),
]
}),
(
"California San Jose 408-429-4770 1049 Pretty View Lane 95113 CA with 707-797-1981"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 19, "CITY"),
(20, 32, "MOBILE_NUMBER"),
(33, 54, "STREET_ADDRESS"),
(55, 60, "ZIPCODE"),
(61, 63, "STATE"),
(69, 81, "TELEPHONE_NUMBER"),
]
}),
(
"95113 CA with California San Jose 1049 Pretty View Lane 408-429-4770 707-797-1981"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(14, 24, "STATE_FULL"),
(25, 33, "CITY"),
(34, 55, "STREET_ADDRESS"),
(56, 68, "MOBILE_NUMBER"),
(69, 81, "TELEPHONE_NUMBER"),
]
}),
(
"with 408-429-4770 707-797-1981 1049 Pretty View Lane CA California 95113 San Jose"
, {
"entities":[
(5, 17, "MOBILE_NUMBER"),
(18, 30, "TELEPHONE_NUMBER"),
(31, 52, "STREET_ADDRESS"),
(53, 55, "STATE"),
(56, 66, "STATE_FULL"),
(67, 72, "ZIPCODE"),
(73, 81, "CITY"),
]
}),
(
"95113 with 408-429-4770 CA California San Jose 1049 Pretty View Lane 707-797-1981"
, {
"entities":[
(0, 5, "ZIPCODE"),
(11, 23, "MOBILE_NUMBER"),
(24, 26, "STATE"),
(27, 37, "STATE_FULL"),
(38, 46, "CITY"),
(47, 68, "STREET_ADDRESS"),
(69, 81, "TELEPHONE_NUMBER"),
]
}),
(
"Massachusetts Boston MA 617-457-2442 that 617-908-8320 4775 Hinkle Lake Road 02109"
, {
"entities":[
(0, 13, "STATE_FULL"),
(14, 20, "CITY"),
(21, 23, "STATE"),
(24, 36, "TELEPHONE_NUMBER"),
(42, 54, "MOBILE_NUMBER"),
(55, 76, "STREET_ADDRESS"),
(77, 82, "ZIPCODE"),
]
}),
(
"02109 Massachusetts MA that 4775 Hinkle Lake Road 617-908-8320 Boston 617-457-2442"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 19, "STATE_FULL"),
(20, 22, "STATE"),
(28, 49, "STREET_ADDRESS"),
(50, 62, "MOBILE_NUMBER"),
(63, 69, "CITY"),
(70, 82, "TELEPHONE_NUMBER"),
]
}),
(
"02109 MA Boston 617-457-2442 Massachusetts 4775 Hinkle Lake Road that 617-908-8320"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 15, "CITY"),
(16, 28, "TELEPHONE_NUMBER"),
(29, 42, "STATE_FULL"),
(43, 64, "STREET_ADDRESS"),
(70, 82, "MOBILE_NUMBER"),
]
}),
(
"that 617-908-8320 Boston 02109 Massachusetts 4775 Hinkle Lake Road MA 617-457-2442"
, {
"entities":[
(5, 17, "MOBILE_NUMBER"),
(18, 24, "CITY"),
(25, 30, "ZIPCODE"),
(31, 44, "STATE_FULL"),
(45, 66, "STREET_ADDRESS"),
(67, 69, "STATE"),
(70, 82, "TELEPHONE_NUMBER"),
]
}),
(
"02109 4775 Hinkle Lake Road MA 617-908-8320 that Boston 617-457-2442 Massachusetts"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 27, "STREET_ADDRESS"),
(28, 30, "STATE"),
(31, 43, "MOBILE_NUMBER"),
(49, 55, "CITY"),
(56, 68, "TELEPHONE_NUMBER"),
(69, 82, "STATE_FULL"),
]
}),
(
"Boston that 02109 617-908-8320 4775 Hinkle Lake Road MA Massachusetts 617-457-2442"
, {
"entities":[
(0, 6, "CITY"),
(12, 17, "ZIPCODE"),
(18, 30, "MOBILE_NUMBER"),
(31, 52, "STREET_ADDRESS"),
(53, 55, "STATE"),
(56, 69, "STATE_FULL"),
(70, 82, "TELEPHONE_NUMBER"),
]
}),
(
"617-457-2442 MA 617-908-8320 Boston 4775 Hinkle Lake Road 02109 that Massachusetts"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 15, "STATE"),
(16, 28, "MOBILE_NUMBER"),
(29, 35, "CITY"),
(36, 57, "STREET_ADDRESS"),
(58, 63, "ZIPCODE"),
(69, 82, "STATE_FULL"),
]
}),
(
"that 02109 Boston 4775 Hinkle Lake Road 617-457-2442 617-908-8320 MA Massachusetts"
, {
"entities":[
(5, 10, "ZIPCODE"),
(11, 17, "CITY"),
(18, 39, "STREET_ADDRESS"),
(40, 52, "TELEPHONE_NUMBER"),
(53, 65, "MOBILE_NUMBER"),
(66, 68, "STATE"),
(69, 82, "STATE_FULL"),
]
}),
(
"MA Boston Massachusetts 617-457-2442 02109 4775 Hinkle Lake Road 617-908-8320 that"
, {
"entities":[
(0, 2, "STATE"),
(3, 9, "CITY"),
(10, 23, "STATE_FULL"),
(24, 36, "TELEPHONE_NUMBER"),
(37, 42, "ZIPCODE"),
(43, 64, "STREET_ADDRESS"),
(65, 77, "MOBILE_NUMBER"),
]
}),
(
"MA that 4775 Hinkle Lake Road 617-457-2442 Boston 617-908-8320 02109 Massachusetts"
, {
"entities":[
(0, 2, "STATE"),
(8, 29, "STREET_ADDRESS"),
(30, 42, "TELEPHONE_NUMBER"),
(43, 49, "CITY"),
(50, 62, "MOBILE_NUMBER"),
(63, 68, "ZIPCODE"),
(69, 82, "STATE_FULL"),
]
}),
(
"419-367-7643 address 419-735-0899 Ohio Toledo 2319 Hill Street 43615 OH"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(21, 33, "TELEPHONE_NUMBER"),
(34, 38, "STATE_FULL"),
(39, 45, "CITY"),
(46, 62, "STREET_ADDRESS"),
(63, 68, "ZIPCODE"),
(69, 71, "STATE"),
]
}),
(
"Toledo 419-367-7643 address OH 2319 Hill Street 419-735-0899 43615 Ohio"
, {
"entities":[
(0, 6, "CITY"),
(7, 19, "MOBILE_NUMBER"),
(28, 30, "STATE"),
(31, 47, "STREET_ADDRESS"),
(48, 60, "TELEPHONE_NUMBER"),
(61, 66, "ZIPCODE"),
(67, 71, "STATE_FULL"),
]
}),
(
"2319 Hill Street 419-735-0899 address 419-367-7643 Ohio 43615 OH Toledo"
, {
"entities":[
(0, 16, "STREET_ADDRESS"),
(17, 29, "TELEPHONE_NUMBER"),
(38, 50, "MOBILE_NUMBER"),
(51, 55, "STATE_FULL"),
(56, 61, "ZIPCODE"),
(62, 64, "STATE"),
(65, 71, "CITY"),
]
}),
(
"43615 address 419-367-7643 OH Ohio 2319 Hill Street Toledo 419-735-0899"
, {
"entities":[
(0, 5, "ZIPCODE"),
(14, 26, "MOBILE_NUMBER"),
(27, 29, "STATE"),
(30, 34, "STATE_FULL"),
(35, 51, "STREET_ADDRESS"),
(52, 58, "CITY"),
(59, 71, "TELEPHONE_NUMBER"),
]
}),
(
"address OH 419-367-7643 2319 Hill Street Ohio Toledo 419-735-0899 43615"
, {
"entities":[
(8, 10, "STATE"),
(11, 23, "MOBILE_NUMBER"),
(24, 40, "STREET_ADDRESS"),
(41, 45, "STATE_FULL"),
(46, 52, "CITY"),
(53, 65, "TELEPHONE_NUMBER"),
(66, 71, "ZIPCODE"),
]
}),
(
"OH 43615 address 419-735-0899 Ohio Toledo 2319 Hill Street 419-367-7643"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(17, 29, "TELEPHONE_NUMBER"),
(30, 34, "STATE_FULL"),
(35, 41, "CITY"),
(42, 58, "STREET_ADDRESS"),
(59, 71, "MOBILE_NUMBER"),
]
}),
(
"419-735-0899 Ohio address 43615 Toledo 2319 Hill Street 419-367-7643 OH"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 17, "STATE_FULL"),
(26, 31, "ZIPCODE"),
(32, 38, "CITY"),
(39, 55, "STREET_ADDRESS"),
(56, 68, "MOBILE_NUMBER"),
(69, 71, "STATE"),
]
}),
(
"OH 419-735-0899 address 419-367-7643 Ohio 43615 2319 Hill Street Toledo"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "TELEPHONE_NUMBER"),
(24, 36, "MOBILE_NUMBER"),
(37, 41, "STATE_FULL"),
(42, 47, "ZIPCODE"),
(48, 64, "STREET_ADDRESS"),
(65, 71, "CITY"),
]
}),
(
"419-367-7643 Toledo 2319 Hill Street address 419-735-0899 OH Ohio 43615"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 19, "CITY"),
(20, 36, "STREET_ADDRESS"),
(45, 57, "TELEPHONE_NUMBER"),
(58, 60, "STATE"),
(61, 65, "STATE_FULL"),
(66, 71, "ZIPCODE"),
]
}),
(
"Ohio Toledo 43615 419-367-7643 OH 2319 Hill Street address 419-735-0899"
, {
"entities":[
(0, 4, "STATE_FULL"),
(5, 11, "CITY"),
(12, 17, "ZIPCODE"),
(18, 30, "MOBILE_NUMBER"),
(31, 33, "STATE"),
(34, 50, "STREET_ADDRESS"),
(59, 71, "TELEPHONE_NUMBER"),
]
}),
(
"33830 305-479-4239 813-267-4312 651 Bernardo Street FL Winter Haven Florida"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "MOBILE_NUMBER"),
(19, 31, "TELEPHONE_NUMBER"),
(32, 51, "STREET_ADDRESS"),
(52, 54, "STATE"),
(55, 67, "CITY"),
(68, 75, "STATE_FULL"),
]
}),
(
"Winter Haven 651 Bernardo Street FL 305-479-4239 813-267-4312 Florida 33830"
, {
"entities":[
(0, 12, "CITY"),
(13, 32, "STREET_ADDRESS"),
(33, 35, "STATE"),
(36, 48, "MOBILE_NUMBER"),
(49, 61, "TELEPHONE_NUMBER"),
(62, 69, "STATE_FULL"),
(70, 75, "ZIPCODE"),
]
}),
(
"651 Bernardo Street 813-267-4312 Winter Haven 33830 FL Florida 305-479-4239"
, {
"entities":[
(0, 19, "STREET_ADDRESS"),
(20, 32, "TELEPHONE_NUMBER"),
(33, 45, "CITY"),
(46, 51, "ZIPCODE"),
(52, 54, "STATE"),
(55, 62, "STATE_FULL"),
(63, 75, "MOBILE_NUMBER"),
]
}),
(
"305-479-4239 651 Bernardo Street 813-267-4312 Winter Haven Florida FL 33830"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 32, "STREET_ADDRESS"),
(33, 45, "TELEPHONE_NUMBER"),
(46, 58, "CITY"),
(59, 66, "STATE_FULL"),
(67, 69, "STATE"),
(70, 75, "ZIPCODE"),
]
}),
(
"FL 813-267-4312 Florida Winter Haven 305-479-4239 33830 651 Bernardo Street"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "TELEPHONE_NUMBER"),
(16, 23, "STATE_FULL"),
(24, 36, "CITY"),
(37, 49, "MOBILE_NUMBER"),
(50, 55, "ZIPCODE"),
(56, 75, "STREET_ADDRESS"),
]
}),
(
"33830 813-267-4312 Winter Haven 651 Bernardo Street Florida FL 305-479-4239"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "TELEPHONE_NUMBER"),
(19, 31, "CITY"),
(32, 51, "STREET_ADDRESS"),
(52, 59, "STATE_FULL"),
(60, 62, "STATE"),
(63, 75, "MOBILE_NUMBER"),
]
}),
(
"813-267-4312 305-479-4239 Winter Haven Florida 33830 FL 651 Bernardo Street"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 25, "MOBILE_NUMBER"),
(26, 38, "CITY"),
(39, 46, "STATE_FULL"),
(47, 52, "ZIPCODE"),
(53, 55, "STATE"),
(56, 75, "STREET_ADDRESS"),
]
}),
(
"Florida FL 305-479-4239 33830 Winter Haven 813-267-4312 651 Bernardo Street"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 10, "STATE"),
(11, 23, "MOBILE_NUMBER"),
(24, 29, "ZIPCODE"),
(30, 42, "CITY"),
(43, 55, "TELEPHONE_NUMBER"),
(56, 75, "STREET_ADDRESS"),
]
}),
(
"305-479-4239 33830 Winter Haven 813-267-4312 Florida FL 651 Bernardo Street"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 31, "CITY"),
(32, 44, "TELEPHONE_NUMBER"),
(45, 52, "STATE_FULL"),
(53, 55, "STATE"),
(56, 75, "STREET_ADDRESS"),
]
}),
(
"Florida 305-479-4239 FL 33830 Winter Haven 813-267-4312 651 Bernardo Street"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 20, "MOBILE_NUMBER"),
(21, 23, "STATE"),
(24, 29, "ZIPCODE"),
(30, 42, "CITY"),
(43, 55, "TELEPHONE_NUMBER"),
(56, 75, "STREET_ADDRESS"),
]
}),
(
"155 Daylene Drive MI 313-570-4492 Detroit 48226 Michigan 734-652-7052"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 20, "STATE"),
(21, 33, "MOBILE_NUMBER"),
(34, 41, "CITY"),
(42, 47, "ZIPCODE"),
(48, 56, "STATE_FULL"),
(57, 69, "TELEPHONE_NUMBER"),
]
}),
(
"734-652-7052 Detroit 155 Daylene Drive Michigan 313-570-4492 MI 48226"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 20, "CITY"),
(21, 38, "STREET_ADDRESS"),
(39, 47, "STATE_FULL"),
(48, 60, "MOBILE_NUMBER"),
(61, 63, "STATE"),
(64, 69, "ZIPCODE"),
]
}),
(
"734-652-7052 313-570-4492 Michigan Detroit 155 Daylene Drive 48226 MI"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 25, "MOBILE_NUMBER"),
(26, 34, "STATE_FULL"),
(35, 42, "CITY"),
(43, 60, "STREET_ADDRESS"),
(61, 66, "ZIPCODE"),
(67, 69, "STATE"),
]
}),
(
"Detroit Michigan 313-570-4492 734-652-7052 155 Daylene Drive MI 48226"
, {
"entities":[
(0, 7, "CITY"),
(8, 16, "STATE_FULL"),
(17, 29, "MOBILE_NUMBER"),
(30, 42, "TELEPHONE_NUMBER"),
(43, 60, "STREET_ADDRESS"),
(61, 63, "STATE"),
(64, 69, "ZIPCODE"),
]
}),
(
"734-652-7052 MI 48226 Detroit Michigan 155 Daylene Drive 313-570-4492"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 15, "STATE"),
(16, 21, "ZIPCODE"),
(22, 29, "CITY"),
(30, 38, "STATE_FULL"),
(39, 56, "STREET_ADDRESS"),
(57, 69, "MOBILE_NUMBER"),
]
}),
(
"313-570-4492 734-652-7052 MI 155 Daylene Drive Michigan 48226 Detroit"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 25, "TELEPHONE_NUMBER"),
(26, 28, "STATE"),
(29, 46, "STREET_ADDRESS"),
(47, 55, "STATE_FULL"),
(56, 61, "ZIPCODE"),
(62, 69, "CITY"),
]
}),
(
"155 Daylene Drive MI Michigan 313-570-4492 734-652-7052 Detroit 48226"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 20, "STATE"),
(21, 29, "STATE_FULL"),
(30, 42, "MOBILE_NUMBER"),
(43, 55, "TELEPHONE_NUMBER"),
(56, 63, "CITY"),
(64, 69, "ZIPCODE"),
]
}),
(
"48226 155 Daylene Drive MI Detroit 734-652-7052 313-570-4492 Michigan"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 23, "STREET_ADDRESS"),
(24, 26, "STATE"),
(27, 34, "CITY"),
(35, 47, "TELEPHONE_NUMBER"),
(48, 60, "MOBILE_NUMBER"),
(61, 69, "STATE_FULL"),
]
}),
(
"734-652-7052 313-570-4492 48226 Michigan 155 Daylene Drive Detroit MI"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 25, "MOBILE_NUMBER"),
(26, 31, "ZIPCODE"),
(32, 40, "STATE_FULL"),
(41, 58, "STREET_ADDRESS"),
(59, 66, "CITY"),
(67, 69, "STATE"),
]
}),
(
"734-652-7052 Michigan 155 Daylene Drive MI Detroit 48226 313-570-4492"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 21, "STATE_FULL"),
(22, 39, "STREET_ADDRESS"),
(40, 42, "STATE"),
(43, 50, "CITY"),
(51, 56, "ZIPCODE"),
(57, 69, "MOBILE_NUMBER"),
]
}),
(
"Heidelberg 601-787-0545 601-935-0840 USE 39439 MS 1043 School House Road Mississippi"
, {
"entities":[
(0, 10, "CITY"),
(11, 23, "TELEPHONE_NUMBER"),
(24, 36, "MOBILE_NUMBER"),
(41, 46, "ZIPCODE"),
(47, 49, "STATE"),
(50, 72, "STREET_ADDRESS"),
(73, 84, "STATE_FULL"),
]
}),
(
"MS 1043 School House Road Heidelberg USE 39439 601-787-0545 Mississippi 601-935-0840"
, {
"entities":[
(0, 2, "STATE"),
(3, 25, "STREET_ADDRESS"),
(26, 36, "CITY"),
(41, 46, "ZIPCODE"),
(47, 59, "TELEPHONE_NUMBER"),
(60, 71, "STATE_FULL"),
(72, 84, "MOBILE_NUMBER"),
]
}),
(
"39439 601-787-0545 USE 601-935-0840 MS Mississippi Heidelberg 1043 School House Road"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "TELEPHONE_NUMBER"),
(23, 35, "MOBILE_NUMBER"),
(36, 38, "STATE"),
(39, 50, "STATE_FULL"),
(51, 61, "CITY"),
(62, 84, "STREET_ADDRESS"),
]
}),
(
"USE Heidelberg 601-935-0840 Mississippi 601-787-0545 39439 MS 1043 School House Road"
, {
"entities":[
(4, 14, "CITY"),
(15, 27, "MOBILE_NUMBER"),
(28, 39, "STATE_FULL"),
(40, 52, "TELEPHONE_NUMBER"),
(53, 58, "ZIPCODE"),
(59, 61, "STATE"),
(62, 84, "STREET_ADDRESS"),
]
}),
(
"39439 MS Heidelberg 1043 School House Road 601-787-0545 601-935-0840 Mississippi USE"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 19, "CITY"),
(20, 42, "STREET_ADDRESS"),
(43, 55, "TELEPHONE_NUMBER"),
(56, 68, "MOBILE_NUMBER"),
(69, 80, "STATE_FULL"),
]
}),
(
"601-935-0840 Heidelberg 39439 MS 1043 School House Road 601-787-0545 USE Mississippi"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 23, "CITY"),
(24, 29, "ZIPCODE"),
(30, 32, "STATE"),
(33, 55, "STREET_ADDRESS"),
(56, 68, "TELEPHONE_NUMBER"),
(73, 84, "STATE_FULL"),
]
}),
(
"Mississippi MS 601-787-0545 39439 USE 1043 School House Road 601-935-0840 Heidelberg"
, {
"entities":[
(0, 11, "STATE_FULL"),
(12, 14, "STATE"),
(15, 27, "TELEPHONE_NUMBER"),
(28, 33, "ZIPCODE"),
(38, 60, "STREET_ADDRESS"),
(61, 73, "MOBILE_NUMBER"),
(74, 84, "CITY"),
]
}),
(
"USE Heidelberg MS 39439 Mississippi 601-787-0545 1043 School House Road 601-935-0840"
, {
"entities":[
(4, 14, "CITY"),
(15, 17, "STATE"),
(18, 23, "ZIPCODE"),
(24, 35, "STATE_FULL"),
(36, 48, "TELEPHONE_NUMBER"),
(49, 71, "STREET_ADDRESS"),
(72, 84, "MOBILE_NUMBER"),
]
}),
(
"MS 39439 Mississippi 1043 School House Road USE 601-787-0545 601-935-0840 Heidelberg"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 20, "STATE_FULL"),
(21, 43, "STREET_ADDRESS"),
(48, 60, "TELEPHONE_NUMBER"),
(61, 73, "MOBILE_NUMBER"),
(74, 84, "CITY"),
]
}),
(
"Mississippi MS USE 601-787-0545 1043 School House Road Heidelberg 39439 601-935-0840"
, {
"entities":[
(0, 11, "STATE_FULL"),
(12, 14, "STATE"),
(19, 31, "TELEPHONE_NUMBER"),
(32, 54, "STREET_ADDRESS"),
(55, 65, "CITY"),
(66, 71, "ZIPCODE"),
(72, 84, "MOBILE_NUMBER"),
]
}),
(
"OH 44512 2884 Rivendell Drive Ohio 330-347-5089 330-770-3466 Boardman"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 29, "STREET_ADDRESS"),
(30, 34, "STATE_FULL"),
(35, 47, "MOBILE_NUMBER"),
(48, 60, "TELEPHONE_NUMBER"),
(61, 69, "CITY"),
]
}),
(
"330-347-5089 330-770-3466 2884 Rivendell Drive Boardman 44512 Ohio OH"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 25, "TELEPHONE_NUMBER"),
(26, 46, "STREET_ADDRESS"),
(47, 55, "CITY"),
(56, 61, "ZIPCODE"),
(62, 66, "STATE_FULL"),
(67, 69, "STATE"),
]
}),
(
"44512 330-347-5089 OH Boardman 2884 Rivendell Drive 330-770-3466 Ohio"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "MOBILE_NUMBER"),
(19, 21, "STATE"),
(22, 30, "CITY"),
(31, 51, "STREET_ADDRESS"),
(52, 64, "TELEPHONE_NUMBER"),
(65, 69, "STATE_FULL"),
]
}),
(
"Boardman 2884 Rivendell Drive 44512 Ohio 330-770-3466 330-347-5089 OH"
, {
"entities":[
(0, 8, "CITY"),
(9, 29, "STREET_ADDRESS"),
(30, 35, "ZIPCODE"),
(36, 40, "STATE_FULL"),
(41, 53, "TELEPHONE_NUMBER"),
(54, 66, "MOBILE_NUMBER"),
(67, 69, "STATE"),
]
}),
(
"Boardman 2884 Rivendell Drive 330-770-3466 330-347-5089 44512 Ohio OH"
, {
"entities":[
(0, 8, "CITY"),
(9, 29, "STREET_ADDRESS"),
(30, 42, "TELEPHONE_NUMBER"),
(43, 55, "MOBILE_NUMBER"),
(56, 61, "ZIPCODE"),
(62, 66, "STATE_FULL"),
(67, 69, "STATE"),
]
}),
(
"44512 Boardman 330-770-3466 OH 2884 Rivendell Drive Ohio 330-347-5089"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 14, "CITY"),
(15, 27, "TELEPHONE_NUMBER"),
(28, 30, "STATE"),
(31, 51, "STREET_ADDRESS"),
(52, 56, "STATE_FULL"),
(57, 69, "MOBILE_NUMBER"),
]
}),
(
"Ohio 44512 OH 2884 Rivendell Drive 330-347-5089 Boardman 330-770-3466"
, {
"entities":[
(0, 4, "STATE_FULL"),
(5, 10, "ZIPCODE"),
(11, 13, "STATE"),
(14, 34, "STREET_ADDRESS"),
(35, 47, "MOBILE_NUMBER"),
(48, 56, "CITY"),
(57, 69, "TELEPHONE_NUMBER"),
]
}),
(
"44512 2884 Rivendell Drive 330-347-5089 330-770-3466 Boardman OH Ohio"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 26, "STREET_ADDRESS"),
(27, 39, "MOBILE_NUMBER"),
(40, 52, "TELEPHONE_NUMBER"),
(53, 61, "CITY"),
(62, 64, "STATE"),
(65, 69, "STATE_FULL"),
]
}),
(
"Boardman OH Ohio 330-347-5089 330-770-3466 2884 Rivendell Drive 44512"
, {
"entities":[
(0, 8, "CITY"),
(9, 11, "STATE"),
(12, 16, "STATE_FULL"),
(17, 29, "MOBILE_NUMBER"),
(30, 42, "TELEPHONE_NUMBER"),
(43, 63, "STREET_ADDRESS"),
(64, 69, "ZIPCODE"),
]
}),
(
"Ohio Boardman 2884 Rivendell Drive OH 330-770-3466 330-347-5089 44512"
, {
"entities":[
(0, 4, "STATE_FULL"),
(5, 13, "CITY"),
(14, 34, "STREET_ADDRESS"),
(35, 37, "STATE"),
(38, 50, "TELEPHONE_NUMBER"),
(51, 63, "MOBILE_NUMBER"),
(64, 69, "ZIPCODE"),
]
}),
(
"Chester Springs 3813 Filbert Street Pennsylvania 19425 717-507-1685 610-827-7661 that PA"
, {
"entities":[
(0, 15, "CITY"),
(16, 35, "STREET_ADDRESS"),
(36, 48, "STATE_FULL"),
(49, 54, "ZIPCODE"),
(55, 67, "MOBILE_NUMBER"),
(68, 80, "TELEPHONE_NUMBER"),
(86, 88, "STATE"),
]
}),
(
"19425 that Pennsylvania Chester Springs 610-827-7661 3813 Filbert Street 717-507-1685 PA"
, {
"entities":[
(0, 5, "ZIPCODE"),
(11, 23, "STATE_FULL"),
(24, 39, "CITY"),
(40, 52, "TELEPHONE_NUMBER"),
(53, 72, "STREET_ADDRESS"),
(73, 85, "MOBILE_NUMBER"),
(86, 88, "STATE"),
]
}),
(
"3813 Filbert Street Chester Springs PA 19425 that 610-827-7661 Pennsylvania 717-507-1685"
, {
"entities":[
(0, 19, "STREET_ADDRESS"),
(20, 35, "CITY"),
(36, 38, "STATE"),
(39, 44, "ZIPCODE"),
(50, 62, "TELEPHONE_NUMBER"),
(63, 75, "STATE_FULL"),
(76, 88, "MOBILE_NUMBER"),
]
}),
(
"19425 610-827-7661 717-507-1685 Pennsylvania Chester Springs that PA 3813 Filbert Street"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "TELEPHONE_NUMBER"),
(19, 31, "MOBILE_NUMBER"),
(32, 44, "STATE_FULL"),
(45, 60, "CITY"),
(66, 68, "STATE"),
(69, 88, "STREET_ADDRESS"),
]
}),
(
"PA 19425 that Chester Springs Pennsylvania 3813 Filbert Street 717-507-1685 610-827-7661"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(14, 29, "CITY"),
(30, 42, "STATE_FULL"),
(43, 62, "STREET_ADDRESS"),
(63, 75, "MOBILE_NUMBER"),
(76, 88, "TELEPHONE_NUMBER"),
]
}),
(
"PA 717-507-1685 19425 Pennsylvania Chester Springs 3813 Filbert Street 610-827-7661 that"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "MOBILE_NUMBER"),
(16, 21, "ZIPCODE"),
(22, 34, "STATE_FULL"),
(35, 50, "CITY"),
(51, 70, "STREET_ADDRESS"),
(71, 83, "TELEPHONE_NUMBER"),
]
}),
(
"Pennsylvania PA 3813 Filbert Street that 717-507-1685 19425 Chester Springs 610-827-7661"
, {
"entities":[
(0, 12, "STATE_FULL"),
(13, 15, "STATE"),
(16, 35, "STREET_ADDRESS"),
(41, 53, "MOBILE_NUMBER"),
(54, 59, "ZIPCODE"),
(60, 75, "CITY"),
(76, 88, "TELEPHONE_NUMBER"),
]
}),
(
"19425 PA 717-507-1685 Pennsylvania Chester Springs 610-827-7661 3813 Filbert Street that"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 21, "MOBILE_NUMBER"),
(22, 34, "STATE_FULL"),
(35, 50, "CITY"),
(51, 63, "TELEPHONE_NUMBER"),
(64, 83, "STREET_ADDRESS"),
]
}),
(
"3813 Filbert Street 19425 Pennsylvania 610-827-7661 that Chester Springs PA 717-507-1685"
, {
"entities":[
(0, 19, "STREET_ADDRESS"),
(20, 25, "ZIPCODE"),
(26, 38, "STATE_FULL"),
(39, 51, "TELEPHONE_NUMBER"),
(57, 72, "CITY"),
(73, 75, "STATE"),
(76, 88, "MOBILE_NUMBER"),
]
}),
(
"that Pennsylvania PA 19425 Chester Springs 610-827-7661 3813 Filbert Street 717-507-1685"
, {
"entities":[
(5, 17, "STATE_FULL"),
(18, 20, "STATE"),
(21, 26, "ZIPCODE"),
(27, 42, "CITY"),
(43, 55, "TELEPHONE_NUMBER"),
(56, 75, "STREET_ADDRESS"),
(76, 88, "MOBILE_NUMBER"),
]
}),
(
"978-424-1036 Massachusetts Marlboro 2816 Joanne Lane MA 508-726-0402 01752"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 26, "STATE_FULL"),
(27, 35, "CITY"),
(36, 52, "STREET_ADDRESS"),
(53, 55, "STATE"),
(56, 68, "MOBILE_NUMBER"),
(69, 74, "ZIPCODE"),
]
}),
(
"Marlboro Massachusetts 01752 2816 Joanne Lane 508-726-0402 978-424-1036 MA"
, {
"entities":[
(0, 8, "CITY"),
(9, 22, "STATE_FULL"),
(23, 28, "ZIPCODE"),
(29, 45, "STREET_ADDRESS"),
(46, 58, "MOBILE_NUMBER"),
(59, 71, "TELEPHONE_NUMBER"),
(72, 74, "STATE"),
]
}),
(
"2816 Joanne Lane 978-424-1036 Marlboro Massachusetts 01752 508-726-0402 MA"
, {
"entities":[
(0, 16, "STREET_ADDRESS"),
(17, 29, "TELEPHONE_NUMBER"),
(30, 38, "CITY"),
(39, 52, "STATE_FULL"),
(53, 58, "ZIPCODE"),
(59, 71, "MOBILE_NUMBER"),
(72, 74, "STATE"),
]
}),
(
"2816 Joanne Lane 508-726-0402 Massachusetts MA 978-424-1036 Marlboro 01752"
, {
"entities":[
(0, 16, "STREET_ADDRESS"),
(17, 29, "MOBILE_NUMBER"),
(30, 43, "STATE_FULL"),
(44, 46, "STATE"),
(47, 59, "TELEPHONE_NUMBER"),
(60, 68, "CITY"),
(69, 74, "ZIPCODE"),
]
}),
(
"2816 Joanne Lane Marlboro 508-726-0402 978-424-1036 MA 01752 Massachusetts"
, {
"entities":[
(0, 16, "STREET_ADDRESS"),
(17, 25, "CITY"),
(26, 38, "MOBILE_NUMBER"),
(39, 51, "TELEPHONE_NUMBER"),
(52, 54, "STATE"),
(55, 60, "ZIPCODE"),
(61, 74, "STATE_FULL"),
]
}),
(
"2816 Joanne Lane MA Marlboro Massachusetts 01752 978-424-1036 508-726-0402"
, {
"entities":[
(0, 16, "STREET_ADDRESS"),
(17, 19, "STATE"),
(20, 28, "CITY"),
(29, 42, "STATE_FULL"),
(43, 48, "ZIPCODE"),
(49, 61, "TELEPHONE_NUMBER"),
(62, 74, "MOBILE_NUMBER"),
]
}),
(
"Marlboro 978-424-1036 MA Massachusetts 2816 Joanne Lane 508-726-0402 01752"
, {
"entities":[
(0, 8, "CITY"),
(9, 21, "TELEPHONE_NUMBER"),
(22, 24, "STATE"),
(25, 38, "STATE_FULL"),
(39, 55, "STREET_ADDRESS"),
(56, 68, "MOBILE_NUMBER"),
(69, 74, "ZIPCODE"),
]
}),
(
"2816 Joanne Lane MA 01752 978-424-1036 Massachusetts 508-726-0402 Marlboro"
, {
"entities":[
(0, 16, "STREET_ADDRESS"),
(17, 19, "STATE"),
(20, 25, "ZIPCODE"),
(26, 38, "TELEPHONE_NUMBER"),
(39, 52, "STATE_FULL"),
(53, 65, "MOBILE_NUMBER"),
(66, 74, "CITY"),
]
}),
(
"01752 Massachusetts Marlboro 508-726-0402 MA 2816 Joanne Lane 978-424-1036"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 19, "STATE_FULL"),
(20, 28, "CITY"),
(29, 41, "MOBILE_NUMBER"),
(42, 44, "STATE"),
(45, 61, "STREET_ADDRESS"),
(62, 74, "TELEPHONE_NUMBER"),
]
}),
(
"2816 Joanne Lane Massachusetts Marlboro 508-726-0402 MA 01752 978-424-1036"
, {
"entities":[
(0, 16, "STREET_ADDRESS"),
(17, 30, "STATE_FULL"),
(31, 39, "CITY"),
(40, 52, "MOBILE_NUMBER"),
(53, 55, "STATE"),
(56, 61, "ZIPCODE"),
(62, 74, "TELEPHONE_NUMBER"),
]
}),
(
"Concord CA 510-289-0776 94520 3990 Wayside Lane 714-298-8577 California"
, {
"entities":[
(0, 7, "CITY"),
(8, 10, "STATE"),
(11, 23, "TELEPHONE_NUMBER"),
(24, 29, "ZIPCODE"),
(30, 47, "STREET_ADDRESS"),
(48, 60, "MOBILE_NUMBER"),
(61, 71, "STATE_FULL"),
]
}),
(
"510-289-0776 94520 Concord California CA 714-298-8577 3990 Wayside Lane"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 26, "CITY"),
(27, 37, "STATE_FULL"),
(38, 40, "STATE"),
(41, 53, "MOBILE_NUMBER"),
(54, 71, "STREET_ADDRESS"),
]
}),
(
"510-289-0776 3990 Wayside Lane 714-298-8577 Concord CA California 94520"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 30, "STREET_ADDRESS"),
(31, 43, "MOBILE_NUMBER"),
(44, 51, "CITY"),
(52, 54, "STATE"),
(55, 65, "STATE_FULL"),
(66, 71, "ZIPCODE"),
]
}),
(
"CA California 3990 Wayside Lane 714-298-8577 94520 510-289-0776 Concord"
, {
"entities":[
(0, 2, "STATE"),
(3, 13, "STATE_FULL"),
(14, 31, "STREET_ADDRESS"),
(32, 44, "MOBILE_NUMBER"),
(45, 50, "ZIPCODE"),
(51, 63, "TELEPHONE_NUMBER"),
(64, 71, "CITY"),
]
}),
(
"94520 510-289-0776 California 714-298-8577 Concord CA 3990 Wayside Lane"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "TELEPHONE_NUMBER"),
(19, 29, "STATE_FULL"),
(30, 42, "MOBILE_NUMBER"),
(43, 50, "CITY"),
(51, 53, "STATE"),
(54, 71, "STREET_ADDRESS"),
]
}),
(
"California Concord CA 714-298-8577 94520 510-289-0776 3990 Wayside Lane"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 18, "CITY"),
(19, 21, "STATE"),
(22, 34, "MOBILE_NUMBER"),
(35, 40, "ZIPCODE"),
(41, 53, "TELEPHONE_NUMBER"),
(54, 71, "STREET_ADDRESS"),
]
}),
(
"94520 CA 714-298-8577 510-289-0776 Concord California 3990 Wayside Lane"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 21, "MOBILE_NUMBER"),
(22, 34, "TELEPHONE_NUMBER"),
(35, 42, "CITY"),
(43, 53, "STATE_FULL"),
(54, 71, "STREET_ADDRESS"),
]
}),
(
"3990 Wayside Lane 714-298-8577 510-289-0776 California CA Concord 94520"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 30, "MOBILE_NUMBER"),
(31, 43, "TELEPHONE_NUMBER"),
(44, 54, "STATE_FULL"),
(55, 57, "STATE"),
(58, 65, "CITY"),
(66, 71, "ZIPCODE"),
]
}),
(
"CA 94520 3990 Wayside Lane California 510-289-0776 Concord 714-298-8577"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 26, "STREET_ADDRESS"),
(27, 37, "STATE_FULL"),
(38, 50, "TELEPHONE_NUMBER"),
(51, 58, "CITY"),
(59, 71, "MOBILE_NUMBER"),
]
}),
(
"Concord 94520 510-289-0776 California CA 714-298-8577 3990 Wayside Lane"
, {
"entities":[
(0, 7, "CITY"),
(8, 13, "ZIPCODE"),
(14, 26, "TELEPHONE_NUMBER"),
(27, 37, "STATE_FULL"),
(38, 40, "STATE"),
(41, 53, "MOBILE_NUMBER"),
(54, 71, "STREET_ADDRESS"),
]
}),
(
"76225 Alvord 940-427-0166 TX 830-352-6679 Texas 3449 Alexander Drive"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 12, "CITY"),
(13, 25, "TELEPHONE_NUMBER"),
(26, 28, "STATE"),
(29, 41, "MOBILE_NUMBER"),
(42, 47, "STATE_FULL"),
(48, 68, "STREET_ADDRESS"),
]
}),
(
"Alvord Texas 76225 940-427-0166 TX 830-352-6679 3449 Alexander Drive"
, {
"entities":[
(0, 6, "CITY"),
(7, 12, "STATE_FULL"),
(13, 18, "ZIPCODE"),
(19, 31, "TELEPHONE_NUMBER"),
(32, 34, "STATE"),
(35, 47, "MOBILE_NUMBER"),
(48, 68, "STREET_ADDRESS"),
]
}),
(
"Alvord TX Texas 940-427-0166 830-352-6679 76225 3449 Alexander Drive"
, {
"entities":[
(0, 6, "CITY"),
(7, 9, "STATE"),
(10, 15, "STATE_FULL"),
(16, 28, "TELEPHONE_NUMBER"),
(29, 41, "MOBILE_NUMBER"),
(42, 47, "ZIPCODE"),
(48, 68, "STREET_ADDRESS"),
]
}),
(
"940-427-0166 Texas 3449 Alexander Drive TX 830-352-6679 76225 Alvord"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 18, "STATE_FULL"),
(19, 39, "STREET_ADDRESS"),
(40, 42, "STATE"),
(43, 55, "MOBILE_NUMBER"),
(56, 61, "ZIPCODE"),
(62, 68, "CITY"),
]
}),
(
"TX 3449 Alexander Drive Alvord 940-427-0166 Texas 76225 830-352-6679"
, {
"entities":[
(0, 2, "STATE"),
(3, 23, "STREET_ADDRESS"),
(24, 30, "CITY"),
(31, 43, "TELEPHONE_NUMBER"),
(44, 49, "STATE_FULL"),
(50, 55, "ZIPCODE"),
(56, 68, "MOBILE_NUMBER"),
]
}),
(
"Alvord Texas 3449 Alexander Drive 940-427-0166 TX 76225 830-352-6679"
, {
"entities":[
(0, 6, "CITY"),
(7, 12, "STATE_FULL"),
(13, 33, "STREET_ADDRESS"),
(34, 46, "TELEPHONE_NUMBER"),
(47, 49, "STATE"),
(50, 55, "ZIPCODE"),
(56, 68, "MOBILE_NUMBER"),
]
}),
(
"3449 Alexander Drive TX 76225 Texas 940-427-0166 Alvord 830-352-6679"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 23, "STATE"),
(24, 29, "ZIPCODE"),
(30, 35, "STATE_FULL"),
(36, 48, "TELEPHONE_NUMBER"),
(49, 55, "CITY"),
(56, 68, "MOBILE_NUMBER"),
]
}),
(
"Texas 76225 3449 Alexander Drive Alvord 830-352-6679 940-427-0166 TX"
, {
"entities":[
(0, 5, "STATE_FULL"),
(6, 11, "ZIPCODE"),
(12, 32, "STREET_ADDRESS"),
(33, 39, "CITY"),
(40, 52, "MOBILE_NUMBER"),
(53, 65, "TELEPHONE_NUMBER"),
(66, 68, "STATE"),
]
}),
(
"830-352-6679 76225 Alvord TX 940-427-0166 3449 Alexander Drive Texas"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 25, "CITY"),
(26, 28, "STATE"),
(29, 41, "TELEPHONE_NUMBER"),
(42, 62, "STREET_ADDRESS"),
(63, 68, "STATE_FULL"),
]
}),
(
"3449 Alexander Drive Texas 76225 TX 830-352-6679 Alvord 940-427-0166"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 26, "STATE_FULL"),
(27, 32, "ZIPCODE"),
(33, 35, "STATE"),
(36, 48, "MOBILE_NUMBER"),
(49, 55, "CITY"),
(56, 68, "TELEPHONE_NUMBER"),
]
}),
(
"404-786-8553 30303 904 Stroop Hill Road GA 770-256-7835 Atlanta Georgia that"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 39, "STREET_ADDRESS"),
(40, 42, "STATE"),
(43, 55, "MOBILE_NUMBER"),
(56, 63, "CITY"),
(64, 71, "STATE_FULL"),
]
}),
(
"770-256-7835 Atlanta 904 Stroop Hill Road GA 404-786-8553 that Georgia 30303"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 20, "CITY"),
(21, 41, "STREET_ADDRESS"),
(42, 44, "STATE"),
(45, 57, "TELEPHONE_NUMBER"),
(63, 70, "STATE_FULL"),
(71, 76, "ZIPCODE"),
]
}),
(
"404-786-8553 30303 770-256-7835 Atlanta 904 Stroop Hill Road GA Georgia that"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 31, "MOBILE_NUMBER"),
(32, 39, "CITY"),
(40, 60, "STREET_ADDRESS"),
(61, 63, "STATE"),
(64, 71, "STATE_FULL"),
]
}),
(
"770-256-7835 GA Georgia Atlanta that 404-786-8553 904 Stroop Hill Road 30303"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 15, "STATE"),
(16, 23, "STATE_FULL"),
(24, 31, "CITY"),
(37, 49, "TELEPHONE_NUMBER"),
(50, 70, "STREET_ADDRESS"),
(71, 76, "ZIPCODE"),
]
}),
(
"that 904 Stroop Hill Road Atlanta GA 770-256-7835 Georgia 404-786-8553 30303"
, {
"entities":[
(5, 25, "STREET_ADDRESS"),
(26, 33, "CITY"),
(34, 36, "STATE"),
(37, 49, "MOBILE_NUMBER"),
(50, 57, "STATE_FULL"),
(58, 70, "TELEPHONE_NUMBER"),
(71, 76, "ZIPCODE"),
]
}),
(
"30303 404-786-8553 Atlanta Georgia that 904 Stroop Hill Road GA 770-256-7835"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "TELEPHONE_NUMBER"),
(19, 26, "CITY"),
(27, 34, "STATE_FULL"),
(40, 60, "STREET_ADDRESS"),
(61, 63, "STATE"),
(64, 76, "MOBILE_NUMBER"),
]
}),
(
"904 Stroop Hill Road 404-786-8553 that Atlanta 770-256-7835 Georgia 30303 GA"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 33, "TELEPHONE_NUMBER"),
(39, 46, "CITY"),
(47, 59, "MOBILE_NUMBER"),
(60, 67, "STATE_FULL"),
(68, 73, "ZIPCODE"),
(74, 76, "STATE"),
]
}),
(
"that 30303 Atlanta 904 Stroop Hill Road 404-786-8553 Georgia 770-256-7835 GA"
, {
"entities":[
(5, 10, "ZIPCODE"),
(11, 18, "CITY"),
(19, 39, "STREET_ADDRESS"),
(40, 52, "TELEPHONE_NUMBER"),
(53, 60, "STATE_FULL"),
(61, 73, "MOBILE_NUMBER"),
(74, 76, "STATE"),
]
}),
(
"that 404-786-8553 904 Stroop Hill Road 30303 Atlanta GA 770-256-7835 Georgia"
, {
"entities":[
(5, 17, "TELEPHONE_NUMBER"),
(18, 38, "STREET_ADDRESS"),
(39, 44, "ZIPCODE"),
(45, 52, "CITY"),
(53, 55, "STATE"),
(56, 68, "MOBILE_NUMBER"),
(69, 76, "STATE_FULL"),
]
}),
(
"30303 that GA 904 Stroop Hill Road Atlanta 404-786-8553 Georgia 770-256-7835"
, {
"entities":[
(0, 5, "ZIPCODE"),
(11, 13, "STATE"),
(14, 34, "STREET_ADDRESS"),
(35, 42, "CITY"),
(43, 55, "TELEPHONE_NUMBER"),
(56, 63, "STATE_FULL"),
(64, 76, "MOBILE_NUMBER"),
]
}),
(
"305-972-5759 33157 Perrine Florida 627 Ridenour Street 786-291-3876 FL"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 26, "CITY"),
(27, 34, "STATE_FULL"),
(35, 54, "STREET_ADDRESS"),
(55, 67, "TELEPHONE_NUMBER"),
(68, 70, "STATE"),
]
}),
(
"Perrine 33157 627 Ridenour Street FL 305-972-5759 Florida 786-291-3876"
, {
"entities":[
(0, 7, "CITY"),
(8, 13, "ZIPCODE"),
(14, 33, "STREET_ADDRESS"),
(34, 36, "STATE"),
(37, 49, "MOBILE_NUMBER"),
(50, 57, "STATE_FULL"),
(58, 70, "TELEPHONE_NUMBER"),
]
}),
(
"786-291-3876 Perrine 33157 FL Florida 627 Ridenour Street 305-972-5759"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 20, "CITY"),
(21, 26, "ZIPCODE"),
(27, 29, "STATE"),
(30, 37, "STATE_FULL"),
(38, 57, "STREET_ADDRESS"),
(58, 70, "MOBILE_NUMBER"),
]
}),
(
"Florida 627 Ridenour Street 786-291-3876 FL 305-972-5759 33157 Perrine"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 27, "STREET_ADDRESS"),
(28, 40, "TELEPHONE_NUMBER"),
(41, 43, "STATE"),
(44, 56, "MOBILE_NUMBER"),
(57, 62, "ZIPCODE"),
(63, 70, "CITY"),
]
}),
(
"FL 33157 305-972-5759 786-291-3876 Florida Perrine 627 Ridenour Street"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 21, "MOBILE_NUMBER"),
(22, 34, "TELEPHONE_NUMBER"),
(35, 42, "STATE_FULL"),
(43, 50, "CITY"),
(51, 70, "STREET_ADDRESS"),
]
}),
(
"627 Ridenour Street 786-291-3876 305-972-5759 Florida FL 33157 Perrine"
, {
"entities":[
(0, 19, "STREET_ADDRESS"),
(20, 32, "TELEPHONE_NUMBER"),
(33, 45, "MOBILE_NUMBER"),
(46, 53, "STATE_FULL"),
(54, 56, "STATE"),
(57, 62, "ZIPCODE"),
(63, 70, "CITY"),
]
}),
(
"FL Florida 33157 786-291-3876 305-972-5759 Perrine 627 Ridenour Street"
, {
"entities":[
(0, 2, "STATE"),
(3, 10, "STATE_FULL"),
(11, 16, "ZIPCODE"),
(17, 29, "TELEPHONE_NUMBER"),
(30, 42, "MOBILE_NUMBER"),
(43, 50, "CITY"),
(51, 70, "STREET_ADDRESS"),
]
}),
(
"305-972-5759 33157 Florida 786-291-3876 Perrine FL 627 Ridenour Street"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 26, "STATE_FULL"),
(27, 39, "TELEPHONE_NUMBER"),
(40, 47, "CITY"),
(48, 50, "STATE"),
(51, 70, "STREET_ADDRESS"),
]
}),
(
"305-972-5759 627 Ridenour Street Perrine 786-291-3876 33157 FL Florida"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 32, "STREET_ADDRESS"),
(33, 40, "CITY"),
(41, 53, "TELEPHONE_NUMBER"),
(54, 59, "ZIPCODE"),
(60, 62, "STATE"),
(63, 70, "STATE_FULL"),
]
}),
(
"Perrine 33157 305-972-5759 Florida FL 786-291-3876 627 Ridenour Street"
, {
"entities":[
(0, 7, "CITY"),
(8, 13, "ZIPCODE"),
(14, 26, "MOBILE_NUMBER"),
(27, 34, "STATE_FULL"),
(35, 37, "STATE"),
(38, 50, "TELEPHONE_NUMBER"),
(51, 70, "STREET_ADDRESS"),
]
}),
(
"4105 George Street free 305-201-0087 FL 32607 352-477-1594 Gainesville free address Florida"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(24, 36, "MOBILE_NUMBER"),
(37, 39, "STATE"),
(40, 45, "ZIPCODE"),
(46, 58, "TELEPHONE_NUMBER"),
(59, 70, "CITY"),
(84, 91, "STATE_FULL"),
]
}),
(
"32607 Florida free FL 352-477-1594 4105 George Street address free 305-201-0087 Gainesville"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 13, "STATE_FULL"),
(19, 21, "STATE"),
(22, 34, "TELEPHONE_NUMBER"),
(35, 53, "STREET_ADDRESS"),
(67, 79, "MOBILE_NUMBER"),
(80, 91, "CITY"),
]
}),
(
"free free Gainesville FL 32607 352-477-1594 Florida 305-201-0087 4105 George Street address"
, {
"entities":[
(10, 21, "CITY"),
(22, 24, "STATE"),
(25, 30, "ZIPCODE"),
(31, 43, "TELEPHONE_NUMBER"),
(44, 51, "STATE_FULL"),
(52, 64, "MOBILE_NUMBER"),
(65, 83, "STREET_ADDRESS"),
]
}),
(
"352-477-1594 32607 Florida FL free address 305-201-0087 Gainesville free 4105 George Street"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 26, "STATE_FULL"),
(27, 29, "STATE"),
(43, 55, "MOBILE_NUMBER"),
(56, 67, "CITY"),
(73, 91, "STREET_ADDRESS"),
]
}),
(
"free address 4105 George Street free FL Gainesville Florida 32607 352-477-1594 305-201-0087"
, {
"entities":[
(13, 31, "STREET_ADDRESS"),
(37, 39, "STATE"),
(40, 51, "CITY"),
(52, 59, "STATE_FULL"),
(60, 65, "ZIPCODE"),
(66, 78, "TELEPHONE_NUMBER"),
(79, 91, "MOBILE_NUMBER"),
]
}),
(
"FL free Florida 352-477-1594 32607 4105 George Street free 305-201-0087 Gainesville address"
, {
"entities":[
(0, 2, "STATE"),
(8, 15, "STATE_FULL"),
(16, 28, "TELEPHONE_NUMBER"),
(29, 34, "ZIPCODE"),
(35, 53, "STREET_ADDRESS"),
(59, 71, "MOBILE_NUMBER"),
(72, 83, "CITY"),
]
}),
(
"address Florida free Gainesville free 32607 352-477-1594 305-201-0087 4105 George Street FL"
, {
"entities":[
(8, 15, "STATE_FULL"),
(21, 32, "CITY"),
(38, 43, "ZIPCODE"),
(44, 56, "TELEPHONE_NUMBER"),
(57, 69, "MOBILE_NUMBER"),
(70, 88, "STREET_ADDRESS"),
(89, 91, "STATE"),
]
}),
(
"free 305-201-0087 address FL 4105 George Street 32607 Gainesville 352-477-1594 Florida free"
, {
"entities":[
(5, 17, "MOBILE_NUMBER"),
(26, 28, "STATE"),
(29, 47, "STREET_ADDRESS"),
(48, 53, "ZIPCODE"),
(54, 65, "CITY"),
(66, 78, "TELEPHONE_NUMBER"),
(79, 86, "STATE_FULL"),
]
}),
(
"free address free 32607 FL 352-477-1594 Florida 305-201-0087 Gainesville 4105 George Street"
, {
"entities":[
(18, 23, "ZIPCODE"),
(24, 26, "STATE"),
(27, 39, "TELEPHONE_NUMBER"),
(40, 47, "STATE_FULL"),
(48, 60, "MOBILE_NUMBER"),
(61, 72, "CITY"),
(73, 91, "STREET_ADDRESS"),
]
}),
(
"free 305-201-0087 FL 32607 352-477-1594 4105 George Street Gainesville Florida free address"
, {
"entities":[
(5, 17, "MOBILE_NUMBER"),
(18, 20, "STATE"),
(21, 26, "ZIPCODE"),
(27, 39, "TELEPHONE_NUMBER"),
(40, 58, "STREET_ADDRESS"),
(59, 70, "CITY"),
(71, 78, "STATE_FULL"),
]
}),
(
"904-335-5946 3910 Cherry Tree Drive Jacksonville FL 32216 Florida 904-618-4434"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 35, "STREET_ADDRESS"),
(36, 48, "CITY"),
(49, 51, "STATE"),
(52, 57, "ZIPCODE"),
(58, 65, "STATE_FULL"),
(66, 78, "MOBILE_NUMBER"),
]
}),
(
"Florida FL Jacksonville 904-335-5946 3910 Cherry Tree Drive 904-618-4434 32216"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 10, "STATE"),
(11, 23, "CITY"),
(24, 36, "TELEPHONE_NUMBER"),
(37, 59, "STREET_ADDRESS"),
(60, 72, "MOBILE_NUMBER"),
(73, 78, "ZIPCODE"),
]
}),
(
"Jacksonville 3910 Cherry Tree Drive FL 904-335-5946 32216 Florida 904-618-4434"
, {
"entities":[
(0, 12, "CITY"),
(13, 35, "STREET_ADDRESS"),
(36, 38, "STATE"),
(39, 51, "TELEPHONE_NUMBER"),
(52, 57, "ZIPCODE"),
(58, 65, "STATE_FULL"),
(66, 78, "MOBILE_NUMBER"),
]
}),
(
"Jacksonville FL Florida 904-618-4434 3910 Cherry Tree Drive 904-335-5946 32216"
, {
"entities":[
(0, 12, "CITY"),
(13, 15, "STATE"),
(16, 23, "STATE_FULL"),
(24, 36, "MOBILE_NUMBER"),
(37, 59, "STREET_ADDRESS"),
(60, 72, "TELEPHONE_NUMBER"),
(73, 78, "ZIPCODE"),
]
}),
(
"3910 Cherry Tree Drive Jacksonville FL Florida 904-618-4434 904-335-5946 32216"
, {
"entities":[
(0, 22, "STREET_ADDRESS"),
(23, 35, "CITY"),
(36, 38, "STATE"),
(39, 46, "STATE_FULL"),
(47, 59, "MOBILE_NUMBER"),
(60, 72, "TELEPHONE_NUMBER"),
(73, 78, "ZIPCODE"),
]
}),
(
"904-335-5946 FL 3910 Cherry Tree Drive Florida 32216 904-618-4434 Jacksonville"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 15, "STATE"),
(16, 38, "STREET_ADDRESS"),
(39, 46, "STATE_FULL"),
(47, 52, "ZIPCODE"),
(53, 65, "MOBILE_NUMBER"),
(66, 78, "CITY"),
]
}),
(
"3910 Cherry Tree Drive 32216 904-618-4434 Jacksonville Florida FL 904-335-5946"
, {
"entities":[
(0, 22, "STREET_ADDRESS"),
(23, 28, "ZIPCODE"),
(29, 41, "MOBILE_NUMBER"),
(42, 54, "CITY"),
(55, 62, "STATE_FULL"),
(63, 65, "STATE"),
(66, 78, "TELEPHONE_NUMBER"),
]
}),
(
"FL 904-618-4434 Jacksonville 3910 Cherry Tree Drive 904-335-5946 32216 Florida"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "MOBILE_NUMBER"),
(16, 28, "CITY"),
(29, 51, "STREET_ADDRESS"),
(52, 64, "TELEPHONE_NUMBER"),
(65, 70, "ZIPCODE"),
(71, 78, "STATE_FULL"),
]
}),
(
"32216 Jacksonville 904-335-5946 3910 Cherry Tree Drive Florida FL 904-618-4434"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "CITY"),
(19, 31, "TELEPHONE_NUMBER"),
(32, 54, "STREET_ADDRESS"),
(55, 62, "STATE_FULL"),
(63, 65, "STATE"),
(66, 78, "MOBILE_NUMBER"),
]
}),
(
"Jacksonville 32216 3910 Cherry Tree Drive FL 904-618-4434 Florida 904-335-5946"
, {
"entities":[
(0, 12, "CITY"),
(13, 18, "ZIPCODE"),
(19, 41, "STREET_ADDRESS"),
(42, 44, "STATE"),
(45, 57, "MOBILE_NUMBER"),
(58, 65, "STATE_FULL"),
(66, 78, "TELEPHONE_NUMBER"),
]
}),
(
"765-357-7190 IN Indiana 46225 2--3275 767 Overlook Drive Indianapolis"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 15, "STATE"),
(16, 23, "STATE_FULL"),
(24, 29, "ZIPCODE"),
(30, 37, "MOBILE_NUMBER"),
(38, 56, "STREET_ADDRESS"),
(57, 69, "CITY"),
]
}),
(
"765-357-7190 IN Indianapolis 2--3275 767 Overlook Drive Indiana 46225"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 15, "STATE"),
(16, 28, "CITY"),
(29, 36, "MOBILE_NUMBER"),
(37, 55, "STREET_ADDRESS"),
(56, 63, "STATE_FULL"),
(64, 69, "ZIPCODE"),
]
}),
(
"46225 IN 765-357-7190 2--3275 Indianapolis Indiana 767 Overlook Drive"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 21, "TELEPHONE_NUMBER"),
(22, 29, "MOBILE_NUMBER"),
(30, 42, "CITY"),
(43, 50, "STATE_FULL"),
(51, 69, "STREET_ADDRESS"),
]
}),
(
"Indiana 46225 767 Overlook Drive Indianapolis IN 2--3275 765-357-7190"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 13, "ZIPCODE"),
(14, 32, "STREET_ADDRESS"),
(33, 45, "CITY"),
(46, 48, "STATE"),
(49, 56, "MOBILE_NUMBER"),
(57, 69, "TELEPHONE_NUMBER"),
]
}),
(
"IN Indianapolis Indiana 2--3275 765-357-7190 767 Overlook Drive 46225"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "CITY"),
(16, 23, "STATE_FULL"),
(24, 31, "MOBILE_NUMBER"),
(32, 44, "TELEPHONE_NUMBER"),
(45, 63, "STREET_ADDRESS"),
(64, 69, "ZIPCODE"),
]
}),
(
"765-357-7190 Indianapolis 2--3275 767 Overlook Drive Indiana 46225 IN"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 25, "CITY"),
(26, 33, "MOBILE_NUMBER"),
(34, 52, "STREET_ADDRESS"),
(53, 60, "STATE_FULL"),
(61, 66, "ZIPCODE"),
(67, 69, "STATE"),
]
}),
(
"765-357-7190 46225 767 Overlook Drive Indianapolis Indiana IN 2--3275"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 37, "STREET_ADDRESS"),
(38, 50, "CITY"),
(51, 58, "STATE_FULL"),
(59, 61, "STATE"),
(62, 69, "MOBILE_NUMBER"),
]
}),
(
"46225 767 Overlook Drive 765-357-7190 2--3275 Indianapolis IN Indiana"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 24, "STREET_ADDRESS"),
(25, 37, "TELEPHONE_NUMBER"),
(38, 45, "MOBILE_NUMBER"),
(46, 58, "CITY"),
(59, 61, "STATE"),
(62, 69, "STATE_FULL"),
]
}),
(
"767 Overlook Drive 765-357-7190 46225 Indiana Indianapolis IN 2--3275"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 31, "TELEPHONE_NUMBER"),
(32, 37, "ZIPCODE"),
(38, 45, "STATE_FULL"),
(46, 58, "CITY"),
(59, 61, "STATE"),
(62, 69, "MOBILE_NUMBER"),
]
}),
(
"46225 IN 765-357-7190 Indianapolis Indiana 2--3275 767 Overlook Drive"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 21, "TELEPHONE_NUMBER"),
(22, 34, "CITY"),
(35, 42, "STATE_FULL"),
(43, 50, "MOBILE_NUMBER"),
(51, 69, "STREET_ADDRESS"),
]
}),
(
"91104 Pasadena 626-345-9873 CA 48 Middleville Road California 626-840-2637"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 14, "CITY"),
(15, 27, "TELEPHONE_NUMBER"),
(28, 30, "STATE"),
(31, 50, "STREET_ADDRESS"),
(51, 61, "STATE_FULL"),
(62, 74, "MOBILE_NUMBER"),
]
}),
(
"CA 48 Middleville Road 626-840-2637 91104 California Pasadena 626-345-9873"
, {
"entities":[
(0, 2, "STATE"),
(3, 22, "STREET_ADDRESS"),
(23, 35, "MOBILE_NUMBER"),
(36, 41, "ZIPCODE"),
(42, 52, "STATE_FULL"),
(53, 61, "CITY"),
(62, 74, "TELEPHONE_NUMBER"),
]
}),
(
"CA 91104 California 48 Middleville Road 626-345-9873 Pasadena 626-840-2637"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 19, "STATE_FULL"),
(20, 39, "STREET_ADDRESS"),
(40, 52, "TELEPHONE_NUMBER"),
(53, 61, "CITY"),
(62, 74, "MOBILE_NUMBER"),
]
}),
(
"91104 48 Middleville Road California CA 626-840-2637 Pasadena 626-345-9873"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 25, "STREET_ADDRESS"),
(26, 36, "STATE_FULL"),
(37, 39, "STATE"),
(40, 52, "MOBILE_NUMBER"),
(53, 61, "CITY"),
(62, 74, "TELEPHONE_NUMBER"),
]
}),
(
"626-345-9873 California 626-840-2637 91104 CA Pasadena 48 Middleville Road"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 23, "STATE_FULL"),
(24, 36, "MOBILE_NUMBER"),
(37, 42, "ZIPCODE"),
(43, 45, "STATE"),
(46, 54, "CITY"),
(55, 74, "STREET_ADDRESS"),
]
}),
(
"626-840-2637 CA 48 Middleville Road California 91104 626-345-9873 Pasadena"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 15, "STATE"),
(16, 35, "STREET_ADDRESS"),
(36, 46, "STATE_FULL"),
(47, 52, "ZIPCODE"),
(53, 65, "TELEPHONE_NUMBER"),
(66, 74, "CITY"),
]
}),
(
"CA 626-840-2637 626-345-9873 Pasadena 91104 48 Middleville Road California"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "MOBILE_NUMBER"),
(16, 28, "TELEPHONE_NUMBER"),
(29, 37, "CITY"),
(38, 43, "ZIPCODE"),
(44, 63, "STREET_ADDRESS"),
(64, 74, "STATE_FULL"),
]
}),
(
"48 Middleville Road California 626-840-2637 91104 Pasadena 626-345-9873 CA"
, {
"entities":[
(0, 19, "STREET_ADDRESS"),
(20, 30, "STATE_FULL"),
(31, 43, "MOBILE_NUMBER"),
(44, 49, "ZIPCODE"),
(50, 58, "CITY"),
(59, 71, "TELEPHONE_NUMBER"),
(72, 74, "STATE"),
]
}),
(
"91104 48 Middleville Road CA California Pasadena 626-840-2637 626-345-9873"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 25, "STREET_ADDRESS"),
(26, 28, "STATE"),
(29, 39, "STATE_FULL"),
(40, 48, "CITY"),
(49, 61, "MOBILE_NUMBER"),
(62, 74, "TELEPHONE_NUMBER"),
]
}),
(
"California CA 626-840-2637 Pasadena 626-345-9873 48 Middleville Road 91104"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 13, "STATE"),
(14, 26, "MOBILE_NUMBER"),
(27, 35, "CITY"),
(36, 48, "TELEPHONE_NUMBER"),
(49, 68, "STREET_ADDRESS"),
(69, 74, "ZIPCODE"),
]
}),
(
"MN 320-356-5047 in 4562 Newton Street Avon Minnesota 56310 320-844-0185"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "TELEPHONE_NUMBER"),
(19, 37, "STREET_ADDRESS"),
(38, 42, "CITY"),
(43, 52, "STATE_FULL"),
(53, 58, "ZIPCODE"),
(59, 71, "MOBILE_NUMBER"),
]
}),
(
"320-356-5047 Minnesota in Avon 320-844-0185 MN 4562 Newton Street 56310"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 22, "STATE_FULL"),
(26, 30, "CITY"),
(31, 43, "MOBILE_NUMBER"),
(44, 46, "STATE"),
(47, 65, "STREET_ADDRESS"),
(66, 71, "ZIPCODE"),
]
}),
(
"Minnesota in Avon 4562 Newton Street 320-844-0185 56310 MN 320-356-5047"
, {
"entities":[
(0, 9, "STATE_FULL"),
(13, 17, "CITY"),
(18, 36, "STREET_ADDRESS"),
(37, 49, "MOBILE_NUMBER"),
(50, 55, "ZIPCODE"),
(56, 58, "STATE"),
(59, 71, "TELEPHONE_NUMBER"),
]
}),
(
"320-356-5047 MN Minnesota 56310 in 4562 Newton Street 320-844-0185 Avon"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 15, "STATE"),
(16, 25, "STATE_FULL"),
(26, 31, "ZIPCODE"),
(35, 53, "STREET_ADDRESS"),
(54, 66, "MOBILE_NUMBER"),
(67, 71, "CITY"),
]
}),
(
"in Avon MN 320-844-0185 56310 4562 Newton Street Minnesota 320-356-5047"
, {
"entities":[
(3, 7, "CITY"),
(8, 10, "STATE"),
(11, 23, "MOBILE_NUMBER"),
(24, 29, "ZIPCODE"),
(30, 48, "STREET_ADDRESS"),
(49, 58, "STATE_FULL"),
(59, 71, "TELEPHONE_NUMBER"),
]
}),
(
"in 56310 4562 Newton Street Minnesota 320-844-0185 Avon MN 320-356-5047"
, {
"entities":[
(3, 8, "ZIPCODE"),
(9, 27, "STREET_ADDRESS"),
(28, 37, "STATE_FULL"),
(38, 50, "MOBILE_NUMBER"),
(51, 55, "CITY"),
(56, 58, "STATE"),
(59, 71, "TELEPHONE_NUMBER"),
]
}),
(
"320-844-0185 in 56310 320-356-5047 MN Minnesota Avon 4562 Newton Street"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(16, 21, "ZIPCODE"),
(22, 34, "TELEPHONE_NUMBER"),
(35, 37, "STATE"),
(38, 47, "STATE_FULL"),
(48, 52, "CITY"),
(53, 71, "STREET_ADDRESS"),
]
}),
(
"4562 Newton Street in 320-844-0185 Avon 320-356-5047 56310 Minnesota MN"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(22, 34, "MOBILE_NUMBER"),
(35, 39, "CITY"),
(40, 52, "TELEPHONE_NUMBER"),
(53, 58, "ZIPCODE"),
(59, 68, "STATE_FULL"),
(69, 71, "STATE"),
]
}),
(
"Avon 56310 MN Minnesota 320-844-0185 in 4562 Newton Street 320-356-5047"
, {
"entities":[
(0, 4, "CITY"),
(5, 10, "ZIPCODE"),
(11, 13, "STATE"),
(14, 23, "STATE_FULL"),
(24, 36, "MOBILE_NUMBER"),
(40, 58, "STREET_ADDRESS"),
(59, 71, "TELEPHONE_NUMBER"),
]
}),
(
"56310 in Avon 320-356-5047 MN 4562 Newton Street 320-844-0185 Minnesota"
, {
"entities":[
(0, 5, "ZIPCODE"),
(9, 13, "CITY"),
(14, 26, "TELEPHONE_NUMBER"),
(27, 29, "STATE"),
(30, 48, "STREET_ADDRESS"),
(49, 61, "MOBILE_NUMBER"),
(62, 71, "STATE_FULL"),
]
}),
(
"75501 We address TX Texas 903-831-6828 estimate Texarkana 903-276-9534 2520 Grant Street"
, {
"entities":[
(0, 5, "ZIPCODE"),
(17, 19, "STATE"),
(20, 25, "STATE_FULL"),
(26, 38, "TELEPHONE_NUMBER"),
(48, 57, "CITY"),
(58, 70, "MOBILE_NUMBER"),
(71, 88, "STREET_ADDRESS"),
]
}),
(
"903-831-6828 Texarkana 903-276-9534 75501 2520 Grant Street estimate TX Texas address We"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 22, "CITY"),
(23, 35, "MOBILE_NUMBER"),
(36, 41, "ZIPCODE"),
(42, 59, "STREET_ADDRESS"),
(69, 71, "STATE"),
(72, 77, "STATE_FULL"),
]
}),
(
"Texarkana 903-276-9534 estimate 2520 Grant Street 75501 We Texas 903-831-6828 TX address"
, {
"entities":[
(0, 9, "CITY"),
(10, 22, "MOBILE_NUMBER"),
(32, 49, "STREET_ADDRESS"),
(50, 55, "ZIPCODE"),
(59, 64, "STATE_FULL"),
(65, 77, "TELEPHONE_NUMBER"),
(78, 80, "STATE"),
]
}),
(
"Texas address TX 903-831-6828 We 75501 estimate 903-276-9534 Texarkana 2520 Grant Street"
, {
"entities":[
(0, 5, "STATE_FULL"),
(14, 16, "STATE"),
(17, 29, "TELEPHONE_NUMBER"),
(33, 38, "ZIPCODE"),
(48, 60, "MOBILE_NUMBER"),
(61, 70, "CITY"),
(71, 88, "STREET_ADDRESS"),
]
}),
(
"2520 Grant Street estimate 903-276-9534 TX Texarkana address Texas 903-831-6828 75501 We"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(27, 39, "MOBILE_NUMBER"),
(40, 42, "STATE"),
(43, 52, "CITY"),
(61, 66, "STATE_FULL"),
(67, 79, "TELEPHONE_NUMBER"),
(80, 85, "ZIPCODE"),
]
}),
(
"address TX Texas estimate 75501 2520 Grant Street We 903-831-6828 Texarkana 903-276-9534"
, {
"entities":[
(8, 10, "STATE"),
(11, 16, "STATE_FULL"),
(26, 31, "ZIPCODE"),
(32, 49, "STREET_ADDRESS"),
(53, 65, "TELEPHONE_NUMBER"),
(66, 75, "CITY"),
(76, 88, "MOBILE_NUMBER"),
]
}),
(
"TX Texarkana 903-276-9534 address 2520 Grant Street Texas estimate We 75501 903-831-6828"
, {
"entities":[
(0, 2, "STATE"),
(3, 12, "CITY"),
(13, 25, "MOBILE_NUMBER"),
(34, 51, "STREET_ADDRESS"),
(52, 57, "STATE_FULL"),
(70, 75, "ZIPCODE"),
(76, 88, "TELEPHONE_NUMBER"),
]
}),
(
"We 903-831-6828 75501 TX address Texas 2520 Grant Street estimate Texarkana 903-276-9534"
, {
"entities":[
(3, 15, "TELEPHONE_NUMBER"),
(16, 21, "ZIPCODE"),
(22, 24, "STATE"),
(33, 38, "STATE_FULL"),
(39, 56, "STREET_ADDRESS"),
(66, 75, "CITY"),
(76, 88, "MOBILE_NUMBER"),
]
}),
(
"estimate 903-276-9534 Texarkana 75501 903-831-6828 We address 2520 Grant Street TX Texas"
, {
"entities":[
(9, 21, "MOBILE_NUMBER"),
(22, 31, "CITY"),
(32, 37, "ZIPCODE"),
(38, 50, "TELEPHONE_NUMBER"),
(62, 79, "STREET_ADDRESS"),
(80, 82, "STATE"),
(83, 88, "STATE_FULL"),
]
}),
(
"TX Texas 903-831-6828 Texarkana estimate 903-276-9534 75501 2520 Grant Street We address"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "STATE_FULL"),
(9, 21, "TELEPHONE_NUMBER"),
(22, 31, "CITY"),
(41, 53, "MOBILE_NUMBER"),
(54, 59, "ZIPCODE"),
(60, 77, "STREET_ADDRESS"),
]
}),
(
"Nebraska 402-963-3865 Omaha NE 3353 Bungalow Road 402-215-6786 68164"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 21, "TELEPHONE_NUMBER"),
(22, 27, "CITY"),
(28, 30, "STATE"),
(31, 49, "STREET_ADDRESS"),
(50, 62, "MOBILE_NUMBER"),
(63, 68, "ZIPCODE"),
]
}),
(
"68164 402-963-3865 NE Omaha Nebraska 3353 Bungalow Road 402-215-6786"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "TELEPHONE_NUMBER"),
(19, 21, "STATE"),
(22, 27, "CITY"),
(28, 36, "STATE_FULL"),
(37, 55, "STREET_ADDRESS"),
(56, 68, "MOBILE_NUMBER"),
]
}),
(
"Nebraska 402-963-3865 Omaha 3353 Bungalow Road 68164 NE 402-215-6786"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 21, "TELEPHONE_NUMBER"),
(22, 27, "CITY"),
(28, 46, "STREET_ADDRESS"),
(47, 52, "ZIPCODE"),
(53, 55, "STATE"),
(56, 68, "MOBILE_NUMBER"),
]
}),
(
"402-963-3865 NE Nebraska 3353 Bungalow Road Omaha 68164 402-215-6786"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 15, "STATE"),
(16, 24, "STATE_FULL"),
(25, 43, "STREET_ADDRESS"),
(44, 49, "CITY"),
(50, 55, "ZIPCODE"),
(56, 68, "MOBILE_NUMBER"),
]
}),
(
"Nebraska 402-963-3865 Omaha 68164 402-215-6786 NE 3353 Bungalow Road"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 21, "TELEPHONE_NUMBER"),
(22, 27, "CITY"),
(28, 33, "ZIPCODE"),
(34, 46, "MOBILE_NUMBER"),
(47, 49, "STATE"),
(50, 68, "STREET_ADDRESS"),
]
}),
(
"402-963-3865 NE Nebraska Omaha 68164 3353 Bungalow Road 402-215-6786"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 15, "STATE"),
(16, 24, "STATE_FULL"),
(25, 30, "CITY"),
(31, 36, "ZIPCODE"),
(37, 55, "STREET_ADDRESS"),
(56, 68, "MOBILE_NUMBER"),
]
}),
(
"402-215-6786 NE Nebraska Omaha 3353 Bungalow Road 402-963-3865 68164"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 15, "STATE"),
(16, 24, "STATE_FULL"),
(25, 30, "CITY"),
(31, 49, "STREET_ADDRESS"),
(50, 62, "TELEPHONE_NUMBER"),
(63, 68, "ZIPCODE"),
]
}),
(
"Nebraska 402-963-3865 68164 402-215-6786 3353 Bungalow Road NE Omaha"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 21, "TELEPHONE_NUMBER"),
(22, 27, "ZIPCODE"),
(28, 40, "MOBILE_NUMBER"),
(41, 59, "STREET_ADDRESS"),
(60, 62, "STATE"),
(63, 68, "CITY"),
]
}),
(
"68164 NE Nebraska Omaha 402-963-3865 402-215-6786 3353 Bungalow Road"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 17, "STATE_FULL"),
(18, 23, "CITY"),
(24, 36, "TELEPHONE_NUMBER"),
(37, 49, "MOBILE_NUMBER"),
(50, 68, "STREET_ADDRESS"),
]
}),
(
"402-963-3865 3353 Bungalow Road NE 68164 402-215-6786 Omaha Nebraska"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 31, "STREET_ADDRESS"),
(32, 34, "STATE"),
(35, 40, "ZIPCODE"),
(41, 53, "MOBILE_NUMBER"),
(54, 59, "CITY"),
(60, 68, "STATE_FULL"),
]
}),
(
"708-833-7098 2667 Lowland Drive 60606 Chicago IL with Illinois 815-401-2085"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 31, "STREET_ADDRESS"),
(32, 37, "ZIPCODE"),
(38, 45, "CITY"),
(46, 48, "STATE"),
(54, 62, "STATE_FULL"),
(63, 75, "TELEPHONE_NUMBER"),
]
}),
(
"815-401-2085 Illinois 708-833-7098 with 2667 Lowland Drive Chicago IL 60606"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 21, "STATE_FULL"),
(22, 34, "MOBILE_NUMBER"),
(40, 58, "STREET_ADDRESS"),
(59, 66, "CITY"),
(67, 69, "STATE"),
(70, 75, "ZIPCODE"),
]
}),
(
"IL 708-833-7098 with 815-401-2085 Chicago 60606 2667 Lowland Drive Illinois"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "MOBILE_NUMBER"),
(21, 33, "TELEPHONE_NUMBER"),
(34, 41, "CITY"),
(42, 47, "ZIPCODE"),
(48, 66, "STREET_ADDRESS"),
(67, 75, "STATE_FULL"),
]
}),
(
"Chicago 815-401-2085 708-833-7098 60606 Illinois with IL 2667 Lowland Drive"
, {
"entities":[
(0, 7, "CITY"),
(8, 20, "TELEPHONE_NUMBER"),
(21, 33, "MOBILE_NUMBER"),
(34, 39, "ZIPCODE"),
(40, 48, "STATE_FULL"),
(54, 56, "STATE"),
(57, 75, "STREET_ADDRESS"),
]
}),
(
"708-833-7098 with IL Chicago Illinois 60606 2667 Lowland Drive 815-401-2085"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(18, 20, "STATE"),
(21, 28, "CITY"),
(29, 37, "STATE_FULL"),
(38, 43, "ZIPCODE"),
(44, 62, "STREET_ADDRESS"),
(63, 75, "TELEPHONE_NUMBER"),
]
}),
(
"2667 Lowland Drive IL 60606 815-401-2085 Chicago Illinois with 708-833-7098"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 21, "STATE"),
(22, 27, "ZIPCODE"),
(28, 40, "TELEPHONE_NUMBER"),
(41, 48, "CITY"),
(49, 57, "STATE_FULL"),
(63, 75, "MOBILE_NUMBER"),
]
}),
(
"IL Illinois 815-401-2085 2667 Lowland Drive 708-833-7098 Chicago with 60606"
, {
"entities":[
(0, 2, "STATE"),
(3, 11, "STATE_FULL"),
(12, 24, "TELEPHONE_NUMBER"),
(25, 43, "STREET_ADDRESS"),
(44, 56, "MOBILE_NUMBER"),
(57, 64, "CITY"),
(70, 75, "ZIPCODE"),
]
}),
(
"708-833-7098 IL 60606 with Illinois 815-401-2085 Chicago 2667 Lowland Drive"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 15, "STATE"),
(16, 21, "ZIPCODE"),
(27, 35, "STATE_FULL"),
(36, 48, "TELEPHONE_NUMBER"),
(49, 56, "CITY"),
(57, 75, "STREET_ADDRESS"),
]
}),
(
"2667 Lowland Drive Chicago with IL Illinois 815-401-2085 708-833-7098 60606"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 26, "CITY"),
(32, 34, "STATE"),
(35, 43, "STATE_FULL"),
(44, 56, "TELEPHONE_NUMBER"),
(57, 69, "MOBILE_NUMBER"),
(70, 75, "ZIPCODE"),
]
}),
(
"815-401-2085 2667 Lowland Drive 708-833-7098 60606 Chicago IL Illinois with"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 31, "STREET_ADDRESS"),
(32, 44, "MOBILE_NUMBER"),
(45, 50, "ZIPCODE"),
(51, 58, "CITY"),
(59, 61, "STATE"),
(62, 70, "STATE_FULL"),
]
}),
(
"Sacramento California 95817 CA 916-451-2903 916-202-2541 address 67 Park Avenue"
, {
"entities":[
(0, 10, "CITY"),
(11, 21, "STATE_FULL"),
(22, 27, "ZIPCODE"),
(28, 30, "STATE"),
(31, 43, "TELEPHONE_NUMBER"),
(44, 56, "MOBILE_NUMBER"),
(65, 79, "STREET_ADDRESS"),
]
}),
(
"California address 916-451-2903 CA 67 Park Avenue 916-202-2541 95817 Sacramento"
, {
"entities":[
(0, 10, "STATE_FULL"),
(19, 31, "TELEPHONE_NUMBER"),
(32, 34, "STATE"),
(35, 49, "STREET_ADDRESS"),
(50, 62, "MOBILE_NUMBER"),
(63, 68, "ZIPCODE"),
(69, 79, "CITY"),
]
}),
(
"California Sacramento 916-451-2903 address CA 916-202-2541 95817 67 Park Avenue"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 21, "CITY"),
(22, 34, "TELEPHONE_NUMBER"),
(43, 45, "STATE"),
(46, 58, "MOBILE_NUMBER"),
(59, 64, "ZIPCODE"),
(65, 79, "STREET_ADDRESS"),
]
}),
(
"916-451-2903 California 67 Park Avenue address 95817 916-202-2541 Sacramento CA"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 23, "STATE_FULL"),
(24, 38, "STREET_ADDRESS"),
(47, 52, "ZIPCODE"),
(53, 65, "MOBILE_NUMBER"),
(66, 76, "CITY"),
(77, 79, "STATE"),
]
}),
(
"916-451-2903 CA California address 67 Park Avenue Sacramento 916-202-2541 95817"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 15, "STATE"),
(16, 26, "STATE_FULL"),
(35, 49, "STREET_ADDRESS"),
(50, 60, "CITY"),
(61, 73, "MOBILE_NUMBER"),
(74, 79, "ZIPCODE"),
]
}),
(
"CA 916-451-2903 95817 67 Park Avenue California Sacramento 916-202-2541 address"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "TELEPHONE_NUMBER"),
(16, 21, "ZIPCODE"),
(22, 36, "STREET_ADDRESS"),
(37, 47, "STATE_FULL"),
(48, 58, "CITY"),
(59, 71, "MOBILE_NUMBER"),
]
}),
(
"California 916-202-2541 address 95817 CA 67 Park Avenue 916-451-2903 Sacramento"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 23, "MOBILE_NUMBER"),
(32, 37, "ZIPCODE"),
(38, 40, "STATE"),
(41, 55, "STREET_ADDRESS"),
(56, 68, "TELEPHONE_NUMBER"),
(69, 79, "CITY"),
]
}),
(
"California address 916-451-2903 CA Sacramento 916-202-2541 95817 67 Park Avenue"
, {
"entities":[
(0, 10, "STATE_FULL"),
(19, 31, "TELEPHONE_NUMBER"),
(32, 34, "STATE"),
(35, 45, "CITY"),
(46, 58, "MOBILE_NUMBER"),
(59, 64, "ZIPCODE"),
(65, 79, "STREET_ADDRESS"),
]
}),
(
"916-202-2541 916-451-2903 California CA 67 Park Avenue 95817 address Sacramento"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 25, "TELEPHONE_NUMBER"),
(26, 36, "STATE_FULL"),
(37, 39, "STATE"),
(40, 54, "STREET_ADDRESS"),
(55, 60, "ZIPCODE"),
(69, 79, "CITY"),
]
}),
(
"California 916-202-2541 916-451-2903 address CA 67 Park Avenue Sacramento 95817"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 23, "MOBILE_NUMBER"),
(24, 36, "TELEPHONE_NUMBER"),
(45, 47, "STATE"),
(48, 62, "STREET_ADDRESS"),
(63, 73, "CITY"),
(74, 79, "ZIPCODE"),
]
}),
(
"Wisconsin 53202 3152 Oakridge Farm Lane WI 262-299-4045 Milwaukee 414-222-6410"
, {
"entities":[
(0, 9, "STATE_FULL"),
(10, 15, "ZIPCODE"),
(16, 39, "STREET_ADDRESS"),
(40, 42, "STATE"),
(43, 55, "TELEPHONE_NUMBER"),
(56, 65, "CITY"),
(66, 78, "MOBILE_NUMBER"),
]
}),
(
"WI 262-299-4045 414-222-6410 53202 Milwaukee 3152 Oakridge Farm Lane Wisconsin"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "TELEPHONE_NUMBER"),
(16, 28, "MOBILE_NUMBER"),
(29, 34, "ZIPCODE"),
(35, 44, "CITY"),
(45, 68, "STREET_ADDRESS"),
(69, 78, "STATE_FULL"),
]
}),
(
"262-299-4045 WI Milwaukee 414-222-6410 53202 3152 Oakridge Farm Lane Wisconsin"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 15, "STATE"),
(16, 25, "CITY"),
(26, 38, "MOBILE_NUMBER"),
(39, 44, "ZIPCODE"),
(45, 68, "STREET_ADDRESS"),
(69, 78, "STATE_FULL"),
]
}),
(
"53202 WI 414-222-6410 Milwaukee Wisconsin 3152 Oakridge Farm Lane 262-299-4045"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 21, "MOBILE_NUMBER"),
(22, 31, "CITY"),
(32, 41, "STATE_FULL"),
(42, 65, "STREET_ADDRESS"),
(66, 78, "TELEPHONE_NUMBER"),
]
}),
(
"Wisconsin 53202 Milwaukee 414-222-6410 262-299-4045 3152 Oakridge Farm Lane WI"
, {
"entities":[
(0, 9, "STATE_FULL"),
(10, 15, "ZIPCODE"),
(16, 25, "CITY"),
(26, 38, "MOBILE_NUMBER"),
(39, 51, "TELEPHONE_NUMBER"),
(52, 75, "STREET_ADDRESS"),
(76, 78, "STATE"),
]
}),
(
"53202 3152 Oakridge Farm Lane WI Milwaukee Wisconsin 262-299-4045 414-222-6410"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 29, "STREET_ADDRESS"),
(30, 32, "STATE"),
(33, 42, "CITY"),
(43, 52, "STATE_FULL"),
(53, 65, "TELEPHONE_NUMBER"),
(66, 78, "MOBILE_NUMBER"),
]
}),
(
"262-299-4045 414-222-6410 3152 Oakridge Farm Lane WI 53202 Wisconsin Milwaukee"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 25, "MOBILE_NUMBER"),
(26, 49, "STREET_ADDRESS"),
(50, 52, "STATE"),
(53, 58, "ZIPCODE"),
(59, 68, "STATE_FULL"),
(69, 78, "CITY"),
]
}),
(
"53202 Wisconsin 262-299-4045 414-222-6410 3152 Oakridge Farm Lane WI Milwaukee"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 15, "STATE_FULL"),
(16, 28, "TELEPHONE_NUMBER"),
(29, 41, "MOBILE_NUMBER"),
(42, 65, "STREET_ADDRESS"),
(66, 68, "STATE"),
(69, 78, "CITY"),
]
}),
(
"414-222-6410 Milwaukee 53202 Wisconsin 262-299-4045 3152 Oakridge Farm Lane WI"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 22, "CITY"),
(23, 28, "ZIPCODE"),
(29, 38, "STATE_FULL"),
(39, 51, "TELEPHONE_NUMBER"),
(52, 75, "STREET_ADDRESS"),
(76, 78, "STATE"),
]
}),
(
"53202 262-299-4045 WI Milwaukee Wisconsin 414-222-6410 3152 Oakridge Farm Lane"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "TELEPHONE_NUMBER"),
(19, 21, "STATE"),
(22, 31, "CITY"),
(32, 41, "STATE_FULL"),
(42, 54, "MOBILE_NUMBER"),
(55, 78, "STREET_ADDRESS"),
]
}),
(
"NV 702-533-3781 Nevada Las Vegas 89101 4167 Hickory Ridge Drive 702-686-9232"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "MOBILE_NUMBER"),
(16, 22, "STATE_FULL"),
(23, 32, "CITY"),
(33, 38, "ZIPCODE"),
(39, 63, "STREET_ADDRESS"),
(64, 76, "TELEPHONE_NUMBER"),
]
}),
(
"89101 702-533-3781 4167 Hickory Ridge Drive 702-686-9232 Las Vegas NV Nevada"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "MOBILE_NUMBER"),
(19, 43, "STREET_ADDRESS"),
(44, 56, "TELEPHONE_NUMBER"),
(57, 66, "CITY"),
(67, 69, "STATE"),
(70, 76, "STATE_FULL"),
]
}),
(
"NV 89101 Nevada 4167 Hickory Ridge Drive 702-686-9232 Las Vegas 702-533-3781"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 15, "STATE_FULL"),
(16, 40, "STREET_ADDRESS"),
(41, 53, "TELEPHONE_NUMBER"),
(54, 63, "CITY"),
(64, 76, "MOBILE_NUMBER"),
]
}),
(
"702-533-3781 702-686-9232 4167 Hickory Ridge Drive 89101 NV Nevada Las Vegas"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 25, "TELEPHONE_NUMBER"),
(26, 50, "STREET_ADDRESS"),
(51, 56, "ZIPCODE"),
(57, 59, "STATE"),
(60, 66, "STATE_FULL"),
(67, 76, "CITY"),
]
}),
(
"89101 NV 702-533-3781 Las Vegas 4167 Hickory Ridge Drive Nevada 702-686-9232"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 21, "MOBILE_NUMBER"),
(22, 31, "CITY"),
(32, 56, "STREET_ADDRESS"),
(57, 63, "STATE_FULL"),
(64, 76, "TELEPHONE_NUMBER"),
]
}),
(
"702-533-3781 Nevada NV 89101 702-686-9232 4167 Hickory Ridge Drive Las Vegas"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 19, "STATE_FULL"),
(20, 22, "STATE"),
(23, 28, "ZIPCODE"),
(29, 41, "TELEPHONE_NUMBER"),
(42, 66, "STREET_ADDRESS"),
(67, 76, "CITY"),
]
}),
(
"702-686-9232 NV Nevada 702-533-3781 4167 Hickory Ridge Drive Las Vegas 89101"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 15, "STATE"),
(16, 22, "STATE_FULL"),
(23, 35, "MOBILE_NUMBER"),
(36, 60, "STREET_ADDRESS"),
(61, 70, "CITY"),
(71, 76, "ZIPCODE"),
]
}),
(
"89101 4167 Hickory Ridge Drive Nevada 702-686-9232 Las Vegas NV 702-533-3781"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 30, "STREET_ADDRESS"),
(31, 37, "STATE_FULL"),
(38, 50, "TELEPHONE_NUMBER"),
(51, 60, "CITY"),
(61, 63, "STATE"),
(64, 76, "MOBILE_NUMBER"),
]
}),
(
"89101 4167 Hickory Ridge Drive 702-533-3781 NV Las Vegas Nevada 702-686-9232"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 30, "STREET_ADDRESS"),
(31, 43, "MOBILE_NUMBER"),
(44, 46, "STATE"),
(47, 56, "CITY"),
(57, 63, "STATE_FULL"),
(64, 76, "TELEPHONE_NUMBER"),
]
}),
(
"NV 702-533-3781 Las Vegas 4167 Hickory Ridge Drive Nevada 702-686-9232 89101"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "MOBILE_NUMBER"),
(16, 25, "CITY"),
(26, 50, "STREET_ADDRESS"),
(51, 57, "STATE_FULL"),
(58, 70, "TELEPHONE_NUMBER"),
(71, 76, "ZIPCODE"),
]
}),
(
"Michigan 1905 Perry Street MI 810-588-6709 48185 that 989-598-3163 Westland"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 26, "STREET_ADDRESS"),
(27, 29, "STATE"),
(30, 42, "TELEPHONE_NUMBER"),
(43, 48, "ZIPCODE"),
(54, 66, "MOBILE_NUMBER"),
(67, 75, "CITY"),
]
}),
(
"Michigan 1905 Perry Street that 48185 Westland MI 810-588-6709 989-598-3163"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 26, "STREET_ADDRESS"),
(32, 37, "ZIPCODE"),
(38, 46, "CITY"),
(47, 49, "STATE"),
(50, 62, "TELEPHONE_NUMBER"),
(63, 75, "MOBILE_NUMBER"),
]
}),
(
"989-598-3163 1905 Perry Street MI 48185 Michigan that 810-588-6709 Westland"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 30, "STREET_ADDRESS"),
(31, 33, "STATE"),
(34, 39, "ZIPCODE"),
(40, 48, "STATE_FULL"),
(54, 66, "TELEPHONE_NUMBER"),
(67, 75, "CITY"),
]
}),
(
"Michigan 1905 Perry Street MI Westland 48185 810-588-6709 that 989-598-3163"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 26, "STREET_ADDRESS"),
(27, 29, "STATE"),
(30, 38, "CITY"),
(39, 44, "ZIPCODE"),
(45, 57, "TELEPHONE_NUMBER"),
(63, 75, "MOBILE_NUMBER"),
]
}),
(
"Westland MI that 1905 Perry Street Michigan 810-588-6709 989-598-3163 48185"
, {
"entities":[
(0, 8, "CITY"),
(9, 11, "STATE"),
(17, 34, "STREET_ADDRESS"),
(35, 43, "STATE_FULL"),
(44, 56, "TELEPHONE_NUMBER"),
(57, 69, "MOBILE_NUMBER"),
(70, 75, "ZIPCODE"),
]
}),
(
"810-588-6709 Michigan 48185 Westland 989-598-3163 1905 Perry Street that MI"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 21, "STATE_FULL"),
(22, 27, "ZIPCODE"),
(28, 36, "CITY"),
(37, 49, "MOBILE_NUMBER"),
(50, 67, "STREET_ADDRESS"),
(73, 75, "STATE"),
]
}),
(
"48185 Michigan Westland 989-598-3163 810-588-6709 1905 Perry Street MI that"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 14, "STATE_FULL"),
(15, 23, "CITY"),
(24, 36, "MOBILE_NUMBER"),
(37, 49, "TELEPHONE_NUMBER"),
(50, 67, "STREET_ADDRESS"),
(68, 70, "STATE"),
]
}),
(
"989-598-3163 48185 MI 810-588-6709 1905 Perry Street that Michigan Westland"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 21, "STATE"),
(22, 34, "TELEPHONE_NUMBER"),
(35, 52, "STREET_ADDRESS"),
(58, 66, "STATE_FULL"),
(67, 75, "CITY"),
]
}),
(
"989-598-3163 810-588-6709 48185 Michigan that Westland 1905 Perry Street MI"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 25, "TELEPHONE_NUMBER"),
(26, 31, "ZIPCODE"),
(32, 40, "STATE_FULL"),
(46, 54, "CITY"),
(55, 72, "STREET_ADDRESS"),
(73, 75, "STATE"),
]
}),
(
"989-598-3163 1905 Perry Street MI Westland 810-588-6709 48185 that Michigan"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 30, "STREET_ADDRESS"),
(31, 33, "STATE"),
(34, 42, "CITY"),
(43, 55, "TELEPHONE_NUMBER"),
(56, 61, "ZIPCODE"),
(67, 75, "STATE_FULL"),
]
}),
(
"903-203-4211 832-725-2095 3268 Werninger Street Houston Texas TX 77032"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 25, "TELEPHONE_NUMBER"),
(26, 47, "STREET_ADDRESS"),
(48, 55, "CITY"),
(56, 61, "STATE_FULL"),
(62, 64, "STATE"),
(65, 70, "ZIPCODE"),
]
}),
(
"77032 Texas 832-725-2095 Houston 903-203-4211 TX 3268 Werninger Street"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 11, "STATE_FULL"),
(12, 24, "TELEPHONE_NUMBER"),
(25, 32, "CITY"),
(33, 45, "MOBILE_NUMBER"),
(46, 48, "STATE"),
(49, 70, "STREET_ADDRESS"),
]
}),
(
"77032 Houston 3268 Werninger Street TX Texas 832-725-2095 903-203-4211"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 13, "CITY"),
(14, 35, "STREET_ADDRESS"),
(36, 38, "STATE"),
(39, 44, "STATE_FULL"),
(45, 57, "TELEPHONE_NUMBER"),
(58, 70, "MOBILE_NUMBER"),
]
}),
(
"3268 Werninger Street Texas 903-203-4211 Houston TX 832-725-2095 77032"
, {
"entities":[
(0, 21, "STREET_ADDRESS"),
(22, 27, "STATE_FULL"),
(28, 40, "MOBILE_NUMBER"),
(41, 48, "CITY"),
(49, 51, "STATE"),
(52, 64, "TELEPHONE_NUMBER"),
(65, 70, "ZIPCODE"),
]
}),
(
"3268 Werninger Street Houston TX 903-203-4211 Texas 77032 832-725-2095"
, {
"entities":[
(0, 21, "STREET_ADDRESS"),
(22, 29, "CITY"),
(30, 32, "STATE"),
(33, 45, "MOBILE_NUMBER"),
(46, 51, "STATE_FULL"),
(52, 57, "ZIPCODE"),
(58, 70, "TELEPHONE_NUMBER"),
]
}),
(
"832-725-2095 903-203-4211 TX 77032 Houston Texas 3268 Werninger Street"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 25, "MOBILE_NUMBER"),
(26, 28, "STATE"),
(29, 34, "ZIPCODE"),
(35, 42, "CITY"),
(43, 48, "STATE_FULL"),
(49, 70, "STREET_ADDRESS"),
]
}),
(
"77032 TX 3268 Werninger Street Houston 903-203-4211 832-725-2095 Texas"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 30, "STREET_ADDRESS"),
(31, 38, "CITY"),
(39, 51, "MOBILE_NUMBER"),
(52, 64, "TELEPHONE_NUMBER"),
(65, 70, "STATE_FULL"),
]
}),
(
"Houston 903-203-4211 832-725-2095 3268 Werninger Street 77032 TX Texas"
, {
"entities":[
(0, 7, "CITY"),
(8, 20, "MOBILE_NUMBER"),
(21, 33, "TELEPHONE_NUMBER"),
(34, 55, "STREET_ADDRESS"),
(56, 61, "ZIPCODE"),
(62, 64, "STATE"),
(65, 70, "STATE_FULL"),
]
}),
(
"TX 3268 Werninger Street Houston 832-725-2095 Texas 77032 903-203-4211"
, {
"entities":[
(0, 2, "STATE"),
(3, 24, "STREET_ADDRESS"),
(25, 32, "CITY"),
(33, 45, "TELEPHONE_NUMBER"),
(46, 51, "STATE_FULL"),
(52, 57, "ZIPCODE"),
(58, 70, "MOBILE_NUMBER"),
]
}),
(
"832-725-2095 3268 Werninger Street Texas 903-203-4211 TX Houston 77032"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 34, "STREET_ADDRESS"),
(35, 40, "STATE_FULL"),
(41, 53, "MOBILE_NUMBER"),
(54, 56, "STATE"),
(57, 64, "CITY"),
(65, 70, "ZIPCODE"),
]
}),
(
"28202 North Carolina Charlotte 704-346-2641 2343 Holly Street NC 704-990-4610"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 20, "STATE_FULL"),
(21, 30, "CITY"),
(31, 43, "MOBILE_NUMBER"),
(44, 61, "STREET_ADDRESS"),
(62, 64, "STATE"),
(65, 77, "TELEPHONE_NUMBER"),
]
}),
(
"28202 Charlotte 704-346-2641 NC 2343 Holly Street North Carolina 704-990-4610"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 15, "CITY"),
(16, 28, "MOBILE_NUMBER"),
(29, 31, "STATE"),
(32, 49, "STREET_ADDRESS"),
(50, 64, "STATE_FULL"),
(65, 77, "TELEPHONE_NUMBER"),
]
}),
(
"North Carolina 28202 NC 2343 Holly Street 704-990-4610 Charlotte 704-346-2641"
, {
"entities":[
(0, 14, "STATE_FULL"),
(15, 20, "ZIPCODE"),
(21, 23, "STATE"),
(24, 41, "STREET_ADDRESS"),
(42, 54, "TELEPHONE_NUMBER"),
(55, 64, "CITY"),
(65, 77, "MOBILE_NUMBER"),
]
}),
(
"704-346-2641 North Carolina Charlotte 704-990-4610 28202 NC 2343 Holly Street"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 27, "STATE_FULL"),
(28, 37, "CITY"),
(38, 50, "TELEPHONE_NUMBER"),
(51, 56, "ZIPCODE"),
(57, 59, "STATE"),
(60, 77, "STREET_ADDRESS"),
]
}),
(
"28202 2343 Holly Street 704-346-2641 704-990-4610 NC North Carolina Charlotte"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 23, "STREET_ADDRESS"),
(24, 36, "MOBILE_NUMBER"),
(37, 49, "TELEPHONE_NUMBER"),
(50, 52, "STATE"),
(53, 67, "STATE_FULL"),
(68, 77, "CITY"),
]
}),
(
"704-346-2641 28202 NC Charlotte 2343 Holly Street North Carolina 704-990-4610"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 21, "STATE"),
(22, 31, "CITY"),
(32, 49, "STREET_ADDRESS"),
(50, 64, "STATE_FULL"),
(65, 77, "TELEPHONE_NUMBER"),
]
}),
(
"28202 North Carolina 704-990-4610 704-346-2641 NC 2343 Holly Street Charlotte"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 20, "STATE_FULL"),
(21, 33, "TELEPHONE_NUMBER"),
(34, 46, "MOBILE_NUMBER"),
(47, 49, "STATE"),
(50, 67, "STREET_ADDRESS"),
(68, 77, "CITY"),
]
}),
(
"Charlotte 704-990-4610 704-346-2641 2343 Holly Street 28202 NC North Carolina"
, {
"entities":[
(0, 9, "CITY"),
(10, 22, "TELEPHONE_NUMBER"),
(23, 35, "MOBILE_NUMBER"),
(36, 53, "STREET_ADDRESS"),
(54, 59, "ZIPCODE"),
(60, 62, "STATE"),
(63, 77, "STATE_FULL"),
]
}),
(
"704-346-2641 North Carolina 2343 Holly Street 28202 Charlotte NC 704-990-4610"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 27, "STATE_FULL"),
(28, 45, "STREET_ADDRESS"),
(46, 51, "ZIPCODE"),
(52, 61, "CITY"),
(62, 64, "STATE"),
(65, 77, "TELEPHONE_NUMBER"),
]
}),
(
"704-346-2641 NC 704-990-4610 Charlotte 2343 Holly Street 28202 North Carolina"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 15, "STATE"),
(16, 28, "TELEPHONE_NUMBER"),
(29, 38, "CITY"),
(39, 56, "STREET_ADDRESS"),
(57, 62, "ZIPCODE"),
(63, 77, "STATE_FULL"),
]
}),
(
"California 95050 CA Santa Clara that 3595 Rardin Drive 650-683-7164 408-460-6741"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 16, "ZIPCODE"),
(17, 19, "STATE"),
(20, 31, "CITY"),
(37, 54, "STREET_ADDRESS"),
(55, 67, "TELEPHONE_NUMBER"),
(68, 80, "MOBILE_NUMBER"),
]
}),
(
"CA that 95050 408-460-6741 650-683-7164 California 3595 Rardin Drive Santa Clara"
, {
"entities":[
(0, 2, "STATE"),
(8, 13, "ZIPCODE"),
(14, 26, "MOBILE_NUMBER"),
(27, 39, "TELEPHONE_NUMBER"),
(40, 50, "STATE_FULL"),
(51, 68, "STREET_ADDRESS"),
(69, 80, "CITY"),
]
}),
(
"650-683-7164 408-460-6741 that CA 3595 Rardin Drive California 95050 Santa Clara"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 25, "MOBILE_NUMBER"),
(31, 33, "STATE"),
(34, 51, "STREET_ADDRESS"),
(52, 62, "STATE_FULL"),
(63, 68, "ZIPCODE"),
(69, 80, "CITY"),
]
}),
(
"650-683-7164 408-460-6741 CA Santa Clara California 3595 Rardin Drive that 95050"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 25, "MOBILE_NUMBER"),
(26, 28, "STATE"),
(29, 40, "CITY"),
(41, 51, "STATE_FULL"),
(52, 69, "STREET_ADDRESS"),
(75, 80, "ZIPCODE"),
]
}),
(
"California 3595 Rardin Drive 650-683-7164 95050 that Santa Clara 408-460-6741 CA"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 28, "STREET_ADDRESS"),
(29, 41, "TELEPHONE_NUMBER"),
(42, 47, "ZIPCODE"),
(53, 64, "CITY"),
(65, 77, "MOBILE_NUMBER"),
(78, 80, "STATE"),
]
}),
(
"3595 Rardin Drive 408-460-6741 California that 650-683-7164 CA Santa Clara 95050"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 30, "MOBILE_NUMBER"),
(31, 41, "STATE_FULL"),
(47, 59, "TELEPHONE_NUMBER"),
(60, 62, "STATE"),
(63, 74, "CITY"),
(75, 80, "ZIPCODE"),
]
}),
(
"650-683-7164 that 95050 408-460-6741 Santa Clara 3595 Rardin Drive California CA"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(18, 23, "ZIPCODE"),
(24, 36, "MOBILE_NUMBER"),
(37, 48, "CITY"),
(49, 66, "STREET_ADDRESS"),
(67, 77, "STATE_FULL"),
(78, 80, "STATE"),
]
}),
(
"650-683-7164 CA 95050 Santa Clara 408-460-6741 that California 3595 Rardin Drive"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 15, "STATE"),
(16, 21, "ZIPCODE"),
(22, 33, "CITY"),
(34, 46, "MOBILE_NUMBER"),
(52, 62, "STATE_FULL"),
(63, 80, "STREET_ADDRESS"),
]
}),
(
"CA 95050 3595 Rardin Drive 650-683-7164 408-460-6741 California Santa Clara that"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 26, "STREET_ADDRESS"),
(27, 39, "TELEPHONE_NUMBER"),
(40, 52, "MOBILE_NUMBER"),
(53, 63, "STATE_FULL"),
(64, 75, "CITY"),
]
}),
(
"3595 Rardin Drive 95050 California that 650-683-7164 Santa Clara 408-460-6741 CA"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 23, "ZIPCODE"),
(24, 34, "STATE_FULL"),
(40, 52, "TELEPHONE_NUMBER"),
(53, 64, "CITY"),
(65, 77, "MOBILE_NUMBER"),
(78, 80, "STATE"),
]
}),
(
"772-200-5771 address 3766 Long Street 34488 Florida Silver Springs FL 352-236-9627"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(21, 37, "STREET_ADDRESS"),
(38, 43, "ZIPCODE"),
(44, 51, "STATE_FULL"),
(52, 66, "CITY"),
(67, 69, "STATE"),
(70, 82, "TELEPHONE_NUMBER"),
]
}),
(
"Florida 3766 Long Street FL 772-200-5771 address 352-236-9627 34488 Silver Springs"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 24, "STREET_ADDRESS"),
(25, 27, "STATE"),
(28, 40, "MOBILE_NUMBER"),
(49, 61, "TELEPHONE_NUMBER"),
(62, 67, "ZIPCODE"),
(68, 82, "CITY"),
]
}),
(
"3766 Long Street 772-200-5771 34488 address FL 352-236-9627 Florida Silver Springs"
, {
"entities":[
(0, 16, "STREET_ADDRESS"),
(17, 29, "MOBILE_NUMBER"),
(30, 35, "ZIPCODE"),
(44, 46, "STATE"),
(47, 59, "TELEPHONE_NUMBER"),
(60, 67, "STATE_FULL"),
(68, 82, "CITY"),
]
}),
(
"352-236-9627 Florida address Silver Springs 772-200-5771 3766 Long Street 34488 FL"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 20, "STATE_FULL"),
(29, 43, "CITY"),
(44, 56, "MOBILE_NUMBER"),
(57, 73, "STREET_ADDRESS"),
(74, 79, "ZIPCODE"),
(80, 82, "STATE"),
]
}),
(
"3766 Long Street Florida address Silver Springs 772-200-5771 34488 352-236-9627 FL"
, {
"entities":[
(0, 16, "STREET_ADDRESS"),
(17, 24, "STATE_FULL"),
(33, 47, "CITY"),
(48, 60, "MOBILE_NUMBER"),
(61, 66, "ZIPCODE"),
(67, 79, "TELEPHONE_NUMBER"),
(80, 82, "STATE"),
]
}),
(
"34488 Florida 352-236-9627 address 772-200-5771 FL 3766 Long Street Silver Springs"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 13, "STATE_FULL"),
(14, 26, "TELEPHONE_NUMBER"),
(35, 47, "MOBILE_NUMBER"),
(48, 50, "STATE"),
(51, 67, "STREET_ADDRESS"),
(68, 82, "CITY"),
]
}),
(
"address Silver Springs 772-200-5771 3766 Long Street FL 352-236-9627 34488 Florida"
, {
"entities":[
(8, 22, "CITY"),
(23, 35, "MOBILE_NUMBER"),
(36, 52, "STREET_ADDRESS"),
(53, 55, "STATE"),
(56, 68, "TELEPHONE_NUMBER"),
(69, 74, "ZIPCODE"),
(75, 82, "STATE_FULL"),
]
}),
(
"FL 34488 352-236-9627 address 772-200-5771 3766 Long Street Silver Springs Florida"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 21, "TELEPHONE_NUMBER"),
(30, 42, "MOBILE_NUMBER"),
(43, 59, "STREET_ADDRESS"),
(60, 74, "CITY"),
(75, 82, "STATE_FULL"),
]
}),
(
"FL address Florida 352-236-9627 772-200-5771 3766 Long Street 34488 Silver Springs"
, {
"entities":[
(0, 2, "STATE"),
(11, 18, "STATE_FULL"),
(19, 31, "TELEPHONE_NUMBER"),
(32, 44, "MOBILE_NUMBER"),
(45, 61, "STREET_ADDRESS"),
(62, 67, "ZIPCODE"),
(68, 82, "CITY"),
]
}),
(
"772-200-5771 Silver Springs 352-236-9627 3766 Long Street Florida 34488 FL address"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 27, "CITY"),
(28, 40, "TELEPHONE_NUMBER"),
(41, 57, "STREET_ADDRESS"),
(58, 65, "STATE_FULL"),
(66, 71, "ZIPCODE"),
(72, 74, "STATE"),
]
}),
(
"2601 Fincham Road California 760-568-8192 CA We Palm Desert 760-229-3194 92260"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 28, "STATE_FULL"),
(29, 41, "TELEPHONE_NUMBER"),
(42, 44, "STATE"),
(48, 59, "CITY"),
(60, 72, "MOBILE_NUMBER"),
(73, 78, "ZIPCODE"),
]
}),
(
"Palm Desert 2601 Fincham Road 92260 760-568-8192 California CA We 760-229-3194"
, {
"entities":[
(0, 11, "CITY"),
(12, 29, "STREET_ADDRESS"),
(30, 35, "ZIPCODE"),
(36, 48, "TELEPHONE_NUMBER"),
(49, 59, "STATE_FULL"),
(60, 62, "STATE"),
(66, 78, "MOBILE_NUMBER"),
]
}),
(
"Palm Desert CA California 2601 Fincham Road 760-568-8192 92260 760-229-3194 We"
, {
"entities":[
(0, 11, "CITY"),
(12, 14, "STATE"),
(15, 25, "STATE_FULL"),
(26, 43, "STREET_ADDRESS"),
(44, 56, "TELEPHONE_NUMBER"),
(57, 62, "ZIPCODE"),
(63, 75, "MOBILE_NUMBER"),
]
}),
(
"760-229-3194 We California Palm Desert CA 760-568-8192 92260 2601 Fincham Road"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(16, 26, "STATE_FULL"),
(27, 38, "CITY"),
(39, 41, "STATE"),
(42, 54, "TELEPHONE_NUMBER"),
(55, 60, "ZIPCODE"),
(61, 78, "STREET_ADDRESS"),
]
}),
(
"760-229-3194 2601 Fincham Road 760-568-8192 92260 California CA Palm Desert We"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 30, "STREET_ADDRESS"),
(31, 43, "TELEPHONE_NUMBER"),
(44, 49, "ZIPCODE"),
(50, 60, "STATE_FULL"),
(61, 63, "STATE"),
(64, 75, "CITY"),
]
}),
(
"2601 Fincham Road California 92260 760-229-3194 760-568-8192 Palm Desert CA We"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 28, "STATE_FULL"),
(29, 34, "ZIPCODE"),
(35, 47, "MOBILE_NUMBER"),
(48, 60, "TELEPHONE_NUMBER"),
(61, 72, "CITY"),
(73, 75, "STATE"),
]
}),
(
"760-229-3194 CA 92260 2601 Fincham Road Palm Desert 760-568-8192 California We"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 15, "STATE"),
(16, 21, "ZIPCODE"),
(22, 39, "STREET_ADDRESS"),
(40, 51, "CITY"),
(52, 64, "TELEPHONE_NUMBER"),
(65, 75, "STATE_FULL"),
]
}),
(
"Palm Desert 760-229-3194 We 2601 Fincham Road California 760-568-8192 CA 92260"
, {
"entities":[
(0, 11, "CITY"),
(12, 24, "MOBILE_NUMBER"),
(28, 45, "STREET_ADDRESS"),
(46, 56, "STATE_FULL"),
(57, 69, "TELEPHONE_NUMBER"),
(70, 72, "STATE"),
(73, 78, "ZIPCODE"),
]
}),
(
"92260 Palm Desert 760-229-3194 We California 2601 Fincham Road CA 760-568-8192"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 17, "CITY"),
(18, 30, "MOBILE_NUMBER"),
(34, 44, "STATE_FULL"),
(45, 62, "STREET_ADDRESS"),
(63, 65, "STATE"),
(66, 78, "TELEPHONE_NUMBER"),
]
}),
(
"760-568-8192 California 760-229-3194 92260 CA 2601 Fincham Road Palm Desert We"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 23, "STATE_FULL"),
(24, 36, "MOBILE_NUMBER"),
(37, 42, "ZIPCODE"),
(43, 45, "STATE"),
(46, 63, "STREET_ADDRESS"),
(64, 75, "CITY"),
]
}),
(
"77478 1973 Gore Street Texas Sugar Land TX 832-988-1471 713-549-3994"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 22, "STREET_ADDRESS"),
(23, 28, "STATE_FULL"),
(29, 39, "CITY"),
(40, 42, "STATE"),
(43, 55, "MOBILE_NUMBER"),
(56, 68, "TELEPHONE_NUMBER"),
]
}),
(
"Texas 77478 1973 Gore Street 832-988-1471 Sugar Land 713-549-3994 TX"
, {
"entities":[
(0, 5, "STATE_FULL"),
(6, 11, "ZIPCODE"),
(12, 28, "STREET_ADDRESS"),
(29, 41, "MOBILE_NUMBER"),
(42, 52, "CITY"),
(53, 65, "TELEPHONE_NUMBER"),
(66, 68, "STATE"),
]
}),
(
"832-988-1471 1973 Gore Street TX Texas Sugar Land 77478 713-549-3994"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 29, "STREET_ADDRESS"),
(30, 32, "STATE"),
(33, 38, "STATE_FULL"),
(39, 49, "CITY"),
(50, 55, "ZIPCODE"),
(56, 68, "TELEPHONE_NUMBER"),
]
}),
(
"Sugar Land 77478 Texas 713-549-3994 TX 832-988-1471 1973 Gore Street"
, {
"entities":[
(0, 10, "CITY"),
(11, 16, "ZIPCODE"),
(17, 22, "STATE_FULL"),
(23, 35, "TELEPHONE_NUMBER"),
(36, 38, "STATE"),
(39, 51, "MOBILE_NUMBER"),
(52, 68, "STREET_ADDRESS"),
]
}),
(
"Texas 77478 713-549-3994 832-988-1471 Sugar Land 1973 Gore Street TX"
, {
"entities":[
(0, 5, "STATE_FULL"),
(6, 11, "ZIPCODE"),
(12, 24, "TELEPHONE_NUMBER"),
(25, 37, "MOBILE_NUMBER"),
(38, 48, "CITY"),
(49, 65, "STREET_ADDRESS"),
(66, 68, "STATE"),
]
}),
(
"1973 Gore Street 77478 713-549-3994 TX 832-988-1471 Sugar Land Texas"
, {
"entities":[
(0, 16, "STREET_ADDRESS"),
(17, 22, "ZIPCODE"),
(23, 35, "TELEPHONE_NUMBER"),
(36, 38, "STATE"),
(39, 51, "MOBILE_NUMBER"),
(52, 62, "CITY"),
(63, 68, "STATE_FULL"),
]
}),
(
"832-988-1471 Texas Sugar Land TX 77478 1973 Gore Street 713-549-3994"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 18, "STATE_FULL"),
(19, 29, "CITY"),
(30, 32, "STATE"),
(33, 38, "ZIPCODE"),
(39, 55, "STREET_ADDRESS"),
(56, 68, "TELEPHONE_NUMBER"),
]
}),
(
"Sugar Land 713-549-3994 TX 832-988-1471 1973 Gore Street 77478 Texas"
, {
"entities":[
(0, 10, "CITY"),
(11, 23, "TELEPHONE_NUMBER"),
(24, 26, "STATE"),
(27, 39, "MOBILE_NUMBER"),
(40, 56, "STREET_ADDRESS"),
(57, 62, "ZIPCODE"),
(63, 68, "STATE_FULL"),
]
}),
(
"Sugar Land TX 77478 713-549-3994 Texas 832-988-1471 1973 Gore Street"
, {
"entities":[
(0, 10, "CITY"),
(11, 13, "STATE"),
(14, 19, "ZIPCODE"),
(20, 32, "TELEPHONE_NUMBER"),
(33, 38, "STATE_FULL"),
(39, 51, "MOBILE_NUMBER"),
(52, 68, "STREET_ADDRESS"),
]
}),
(
"Texas 1973 Gore Street 77478 Sugar Land 832-988-1471 713-549-3994 TX"
, {
"entities":[
(0, 5, "STATE_FULL"),
(6, 22, "STREET_ADDRESS"),
(23, 28, "ZIPCODE"),
(29, 39, "CITY"),
(40, 52, "MOBILE_NUMBER"),
(53, 65, "TELEPHONE_NUMBER"),
(66, 68, "STATE"),
]
}),
(
"617-324-5274 Massachusetts Cambridge 617-230-8443 MA 888 Lynn Street 02141"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 26, "STATE_FULL"),
(27, 36, "CITY"),
(37, 49, "MOBILE_NUMBER"),
(50, 52, "STATE"),
(53, 68, "STREET_ADDRESS"),
(69, 74, "ZIPCODE"),
]
}),
(
"Massachusetts MA 617-230-8443 02141 888 Lynn Street Cambridge 617-324-5274"
, {
"entities":[
(0, 13, "STATE_FULL"),
(14, 16, "STATE"),
(17, 29, "MOBILE_NUMBER"),
(30, 35, "ZIPCODE"),
(36, 51, "STREET_ADDRESS"),
(52, 61, "CITY"),
(62, 74, "TELEPHONE_NUMBER"),
]
}),
(
"617-230-8443 02141 Massachusetts Cambridge 888 Lynn Street MA 617-324-5274"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 32, "STATE_FULL"),
(33, 42, "CITY"),
(43, 58, "STREET_ADDRESS"),
(59, 61, "STATE"),
(62, 74, "TELEPHONE_NUMBER"),
]
}),
(
"02141 Massachusetts 617-324-5274 MA Cambridge 888 Lynn Street 617-230-8443"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 19, "STATE_FULL"),
(20, 32, "TELEPHONE_NUMBER"),
(33, 35, "STATE"),
(36, 45, "CITY"),
(46, 61, "STREET_ADDRESS"),
(62, 74, "MOBILE_NUMBER"),
]
}),
(
"02141 617-324-5274 MA Massachusetts 617-230-8443 888 Lynn Street Cambridge"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "TELEPHONE_NUMBER"),
(19, 21, "STATE"),
(22, 35, "STATE_FULL"),
(36, 48, "MOBILE_NUMBER"),
(49, 64, "STREET_ADDRESS"),
(65, 74, "CITY"),
]
}),
(
"Massachusetts 02141 MA 617-230-8443 617-324-5274 888 Lynn Street Cambridge"
, {
"entities":[
(0, 13, "STATE_FULL"),
(14, 19, "ZIPCODE"),
(20, 22, "STATE"),
(23, 35, "MOBILE_NUMBER"),
(36, 48, "TELEPHONE_NUMBER"),
(49, 64, "STREET_ADDRESS"),
(65, 74, "CITY"),
]
}),
(
"02141 617-230-8443 MA Cambridge 888 Lynn Street 617-324-5274 Massachusetts"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "MOBILE_NUMBER"),
(19, 21, "STATE"),
(22, 31, "CITY"),
(32, 47, "STREET_ADDRESS"),
(48, 60, "TELEPHONE_NUMBER"),
(61, 74, "STATE_FULL"),
]
}),
(
"Cambridge MA 617-324-5274 Massachusetts 02141 617-230-8443 888 Lynn Street"
, {
"entities":[
(0, 9, "CITY"),
(10, 12, "STATE"),
(13, 25, "TELEPHONE_NUMBER"),
(26, 39, "STATE_FULL"),
(40, 45, "ZIPCODE"),
(46, 58, "MOBILE_NUMBER"),
(59, 74, "STREET_ADDRESS"),
]
}),
(
"Cambridge 617-324-5274 MA 888 Lynn Street Massachusetts 02141 617-230-8443"
, {
"entities":[
(0, 9, "CITY"),
(10, 22, "TELEPHONE_NUMBER"),
(23, 25, "STATE"),
(26, 41, "STREET_ADDRESS"),
(42, 55, "STATE_FULL"),
(56, 61, "ZIPCODE"),
(62, 74, "MOBILE_NUMBER"),
]
}),
(
"617-324-5274 MA 888 Lynn Street Cambridge Massachusetts 02141 617-230-8443"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 15, "STATE"),
(16, 31, "STREET_ADDRESS"),
(32, 41, "CITY"),
(42, 55, "STATE_FULL"),
(56, 61, "ZIPCODE"),
(62, 74, "MOBILE_NUMBER"),
]
}),
]
