TRAINING_DATA2 = [
(
"Phone estimate Ohio 3496 Bates Brothers Road 614-320-5836 Information OH 43085 Worthington 614-450-5895"
, {
"entities":[
(15, 19, "STATE_FULL"),
(20, 44, "STREET_ADDRESS"),
(45, 57, "TELEPHONE_NUMBER"),
(70, 72, "STATE"),
(73, 78, "ZIPCODE"),
(79, 90, "CITY"),
(91, 103, "MOBILE_NUMBER"),
]
}),
(
"Information Phone 614-450-5895 estimate OH 43085 614-320-5836 3496 Bates Brothers Road Ohio Worthington"
, {
"entities":[
(18, 30, "MOBILE_NUMBER"),
(40, 42, "STATE"),
(43, 48, "ZIPCODE"),
(49, 61, "TELEPHONE_NUMBER"),
(62, 86, "STREET_ADDRESS"),
(87, 91, "STATE_FULL"),
(92, 103, "CITY"),
]
}),
(
"OH 43085 Ohio Phone Worthington 614-320-5836 614-450-5895 Information estimate 3496 Bates Brothers Road"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 13, "STATE_FULL"),
(20, 31, "CITY"),
(32, 44, "TELEPHONE_NUMBER"),
(45, 57, "MOBILE_NUMBER"),
(79, 103, "STREET_ADDRESS"),
]
}),
(
"Information Ohio 43085 614-320-5836 Phone Worthington 3496 Bates Brothers Road OH estimate 614-450-5895"
, {
"entities":[
(12, 16, "STATE_FULL"),
(17, 22, "ZIPCODE"),
(23, 35, "TELEPHONE_NUMBER"),
(42, 53, "CITY"),
(54, 78, "STREET_ADDRESS"),
(79, 81, "STATE"),
(91, 103, "MOBILE_NUMBER"),
]
}),
(
"OH estimate 614-450-5895 43085 Information Worthington Phone Ohio 614-320-5836 3496 Bates Brothers Road"
, {
"entities":[
(0, 2, "STATE"),
(12, 24, "MOBILE_NUMBER"),
(25, 30, "ZIPCODE"),
(43, 54, "CITY"),
(61, 65, "STATE_FULL"),
(66, 78, "TELEPHONE_NUMBER"),
(79, 103, "STREET_ADDRESS"),
]
}),
(
"Phone Worthington Ohio estimate 43085 614-320-5836 Information OH 3496 Bates Brothers Road 614-450-5895"
, {
"entities":[
(6, 17, "CITY"),
(18, 22, "STATE_FULL"),
(32, 37, "ZIPCODE"),
(38, 50, "TELEPHONE_NUMBER"),
(63, 65, "STATE"),
(66, 90, "STREET_ADDRESS"),
(91, 103, "MOBILE_NUMBER"),
]
}),
(
"Phone Ohio OH estimate 43085 3496 Bates Brothers Road Information 614-450-5895 614-320-5836 Worthington"
, {
"entities":[
(6, 10, "STATE_FULL"),
(11, 13, "STATE"),
(23, 28, "ZIPCODE"),
(29, 53, "STREET_ADDRESS"),
(66, 78, "MOBILE_NUMBER"),
(79, 91, "TELEPHONE_NUMBER"),
(92, 103, "CITY"),
]
}),
(
"3496 Bates Brothers Road Phone OH 43085 estimate Information Ohio 614-450-5895 Worthington 614-320-5836"
, {
"entities":[
(0, 24, "STREET_ADDRESS"),
(31, 33, "STATE"),
(34, 39, "ZIPCODE"),
(61, 65, "STATE_FULL"),
(66, 78, "MOBILE_NUMBER"),
(79, 90, "CITY"),
(91, 103, "TELEPHONE_NUMBER"),
]
}),
(
"3496 Bates Brothers Road OH Phone Ohio Worthington Information estimate 614-450-5895 43085 614-320-5836"
, {
"entities":[
(0, 24, "STREET_ADDRESS"),
(25, 27, "STATE"),
(34, 38, "STATE_FULL"),
(39, 50, "CITY"),
(72, 84, "MOBILE_NUMBER"),
(85, 90, "ZIPCODE"),
(91, 103, "TELEPHONE_NUMBER"),
]
}),
(
"614-450-5895 OH Phone Ohio 43085 Worthington Information 3496 Bates Brothers Road 614-320-5836 estimate"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 15, "STATE"),
(22, 26, "STATE_FULL"),
(27, 32, "ZIPCODE"),
(33, 44, "CITY"),
(57, 81, "STREET_ADDRESS"),
(82, 94, "TELEPHONE_NUMBER"),
]
}),
(
"Elizabeth 908-659-7831 USE 4084 Hedge Street NJ 908-512-9007 Contact Information Number 07201 New Jersey"
, {
"entities":[
(0, 9, "CITY"),
(10, 22, "TELEPHONE_NUMBER"),
(27, 44, "STREET_ADDRESS"),
(45, 47, "STATE"),
(48, 60, "MOBILE_NUMBER"),
(88, 93, "ZIPCODE"),
(94, 104, "STATE_FULL"),
]
}),
(
"07201 908-659-7831 NJ 4084 Hedge Street 908-512-9007 Number Elizabeth New Jersey USE Contact Information"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "TELEPHONE_NUMBER"),
(19, 21, "STATE"),
(22, 39, "STREET_ADDRESS"),
(40, 52, "MOBILE_NUMBER"),
(60, 69, "CITY"),
(70, 80, "STATE_FULL"),
]
}),
(
"908-512-9007 New Jersey 4084 Hedge Street Contact Information USE NJ Elizabeth 908-659-7831 07201 Number"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 23, "STATE_FULL"),
(24, 41, "STREET_ADDRESS"),
(66, 68, "STATE"),
(69, 78, "CITY"),
(79, 91, "TELEPHONE_NUMBER"),
(92, 97, "ZIPCODE"),
]
}),
(
"Number 908-512-9007 Contact Information Elizabeth NJ 07201 USE New Jersey 4084 Hedge Street 908-659-7831"
, {
"entities":[
(7, 19, "MOBILE_NUMBER"),
(40, 49, "CITY"),
(50, 52, "STATE"),
(53, 58, "ZIPCODE"),
(63, 73, "STATE_FULL"),
(74, 91, "STREET_ADDRESS"),
(92, 104, "TELEPHONE_NUMBER"),
]
}),
(
"908-512-9007 4084 Hedge Street 908-659-7831 Elizabeth NJ Number USE 07201 New Jersey Contact Information"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 30, "STREET_ADDRESS"),
(31, 43, "TELEPHONE_NUMBER"),
(44, 53, "CITY"),
(54, 56, "STATE"),
(68, 73, "ZIPCODE"),
(74, 84, "STATE_FULL"),
]
}),
(
"NJ New Jersey Number USE Contact Information 4084 Hedge Street 908-659-7831 Elizabeth 07201 908-512-9007"
, {
"entities":[
(0, 2, "STATE"),
(3, 13, "STATE_FULL"),
(45, 62, "STREET_ADDRESS"),
(63, 75, "TELEPHONE_NUMBER"),
(76, 85, "CITY"),
(86, 91, "ZIPCODE"),
(92, 104, "MOBILE_NUMBER"),
]
}),
(
"908-659-7831 4084 Hedge Street New Jersey Contact Information 908-512-9007 07201 USE Elizabeth NJ Number"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 30, "STREET_ADDRESS"),
(31, 41, "STATE_FULL"),
(62, 74, "MOBILE_NUMBER"),
(75, 80, "ZIPCODE"),
(85, 94, "CITY"),
(95, 97, "STATE"),
]
}),
(
"NJ Elizabeth New Jersey 4084 Hedge Street Contact Information 908-512-9007 908-659-7831 Number USE 07201"
, {
"entities":[
(0, 2, "STATE"),
(3, 12, "CITY"),
(13, 23, "STATE_FULL"),
(24, 41, "STREET_ADDRESS"),
(62, 74, "MOBILE_NUMBER"),
(75, 87, "TELEPHONE_NUMBER"),
(99, 104, "ZIPCODE"),
]
}),
(
"07201 Number Elizabeth NJ USE Contact Information New Jersey 908-512-9007 908-659-7831 4084 Hedge Street"
, {
"entities":[
(0, 5, "ZIPCODE"),
(13, 22, "CITY"),
(23, 25, "STATE"),
(50, 60, "STATE_FULL"),
(61, 73, "MOBILE_NUMBER"),
(74, 86, "TELEPHONE_NUMBER"),
(87, 104, "STREET_ADDRESS"),
]
}),
(
"908-512-9007 07201 New Jersey 908-659-7831 NJ Elizabeth Contact Information USE Number 4084 Hedge Street"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 29, "STATE_FULL"),
(30, 42, "TELEPHONE_NUMBER"),
(43, 45, "STATE"),
(46, 55, "CITY"),
(87, 104, "STREET_ADDRESS"),
]
}),
(
"2854 Ray Court 910-200-4827 Wilmington 28403 910-360-5252 NC North Carolina"
, {
"entities":[
(0, 14, "STREET_ADDRESS"),
(15, 27, "MOBILE_NUMBER"),
(28, 38, "CITY"),
(39, 44, "ZIPCODE"),
(45, 57, "TELEPHONE_NUMBER"),
(58, 60, "STATE"),
(61, 75, "STATE_FULL"),
]
}),
(
"NC 910-200-4827 2854 Ray Court North Carolina 910-360-5252 Wilmington 28403"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "MOBILE_NUMBER"),
(16, 30, "STREET_ADDRESS"),
(31, 45, "STATE_FULL"),
(46, 58, "TELEPHONE_NUMBER"),
(59, 69, "CITY"),
(70, 75, "ZIPCODE"),
]
}),
(
"28403 2854 Ray Court 910-360-5252 910-200-4827 NC Wilmington North Carolina"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 20, "STREET_ADDRESS"),
(21, 33, "TELEPHONE_NUMBER"),
(34, 46, "MOBILE_NUMBER"),
(47, 49, "STATE"),
(50, 60, "CITY"),
(61, 75, "STATE_FULL"),
]
}),
(
"28403 2854 Ray Court 910-360-5252 North Carolina Wilmington 910-200-4827 NC"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 20, "STREET_ADDRESS"),
(21, 33, "TELEPHONE_NUMBER"),
(34, 48, "STATE_FULL"),
(49, 59, "CITY"),
(60, 72, "MOBILE_NUMBER"),
(73, 75, "STATE"),
]
}),
(
"28403 NC 910-360-5252 2854 Ray Court Wilmington North Carolina 910-200-4827"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 21, "TELEPHONE_NUMBER"),
(22, 36, "STREET_ADDRESS"),
(37, 47, "CITY"),
(48, 62, "STATE_FULL"),
(63, 75, "MOBILE_NUMBER"),
]
}),
(
"North Carolina 910-360-5252 Wilmington 28403 910-200-4827 2854 Ray Court NC"
, {
"entities":[
(0, 14, "STATE_FULL"),
(15, 27, "TELEPHONE_NUMBER"),
(28, 38, "CITY"),
(39, 44, "ZIPCODE"),
(45, 57, "MOBILE_NUMBER"),
(58, 72, "STREET_ADDRESS"),
(73, 75, "STATE"),
]
}),
(
"2854 Ray Court 910-200-4827 NC 910-360-5252 28403 Wilmington North Carolina"
, {
"entities":[
(0, 14, "STREET_ADDRESS"),
(15, 27, "MOBILE_NUMBER"),
(28, 30, "STATE"),
(31, 43, "TELEPHONE_NUMBER"),
(44, 49, "ZIPCODE"),
(50, 60, "CITY"),
(61, 75, "STATE_FULL"),
]
}),
(
"North Carolina 910-200-4827 Wilmington 2854 Ray Court NC 28403 910-360-5252"
, {
"entities":[
(0, 14, "STATE_FULL"),
(15, 27, "MOBILE_NUMBER"),
(28, 38, "CITY"),
(39, 53, "STREET_ADDRESS"),
(54, 56, "STATE"),
(57, 62, "ZIPCODE"),
(63, 75, "TELEPHONE_NUMBER"),
]
}),
(
"28403 910-200-4827 NC North Carolina 2854 Ray Court 910-360-5252 Wilmington"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "MOBILE_NUMBER"),
(19, 21, "STATE"),
(22, 36, "STATE_FULL"),
(37, 51, "STREET_ADDRESS"),
(52, 64, "TELEPHONE_NUMBER"),
(65, 75, "CITY"),
]
}),
(
"28403 910-360-5252 North Carolina NC Wilmington 2854 Ray Court 910-200-4827"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "TELEPHONE_NUMBER"),
(19, 33, "STATE_FULL"),
(34, 36, "STATE"),
(37, 47, "CITY"),
(48, 62, "STREET_ADDRESS"),
(63, 75, "MOBILE_NUMBER"),
]
}),
(
"4277 Buckhannan Avenue Mannsville 315-465-6016 New York 13661 NY 516-509-9328"
, {
"entities":[
(0, 22, "STREET_ADDRESS"),
(23, 33, "CITY"),
(34, 46, "TELEPHONE_NUMBER"),
(47, 55, "STATE_FULL"),
(56, 61, "ZIPCODE"),
(62, 64, "STATE"),
(65, 77, "MOBILE_NUMBER"),
]
}),
(
"New York 315-465-6016 4277 Buckhannan Avenue Mannsville 516-509-9328 NY 13661"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 21, "TELEPHONE_NUMBER"),
(22, 44, "STREET_ADDRESS"),
(45, 55, "CITY"),
(56, 68, "MOBILE_NUMBER"),
(69, 71, "STATE"),
(72, 77, "ZIPCODE"),
]
}),
(
"New York 516-509-9328 4277 Buckhannan Avenue 13661 NY Mannsville 315-465-6016"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 21, "MOBILE_NUMBER"),
(22, 44, "STREET_ADDRESS"),
(45, 50, "ZIPCODE"),
(51, 53, "STATE"),
(54, 64, "CITY"),
(65, 77, "TELEPHONE_NUMBER"),
]
}),
(
"516-509-9328 13661 315-465-6016 New York Mannsville 4277 Buckhannan Avenue NY"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 31, "TELEPHONE_NUMBER"),
(32, 40, "STATE_FULL"),
(41, 51, "CITY"),
(52, 74, "STREET_ADDRESS"),
(75, 77, "STATE"),
]
}),
(
"New York 516-509-9328 NY Mannsville 315-465-6016 4277 Buckhannan Avenue 13661"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 21, "MOBILE_NUMBER"),
(22, 24, "STATE"),
(25, 35, "CITY"),
(36, 48, "TELEPHONE_NUMBER"),
(49, 71, "STREET_ADDRESS"),
(72, 77, "ZIPCODE"),
]
}),
(
"4277 Buckhannan Avenue 13661 NY Mannsville New York 516-509-9328 315-465-6016"
, {
"entities":[
(0, 22, "STREET_ADDRESS"),
(23, 28, "ZIPCODE"),
(29, 31, "STATE"),
(32, 42, "CITY"),
(43, 51, "STATE_FULL"),
(52, 64, "MOBILE_NUMBER"),
(65, 77, "TELEPHONE_NUMBER"),
]
}),
(
"4277 Buckhannan Avenue 315-465-6016 New York NY 516-509-9328 13661 Mannsville"
, {
"entities":[
(0, 22, "STREET_ADDRESS"),
(23, 35, "TELEPHONE_NUMBER"),
(36, 44, "STATE_FULL"),
(45, 47, "STATE"),
(48, 60, "MOBILE_NUMBER"),
(61, 66, "ZIPCODE"),
(67, 77, "CITY"),
]
}),
(
"516-509-9328 4277 Buckhannan Avenue NY New York Mannsville 13661 315-465-6016"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 35, "STREET_ADDRESS"),
(36, 38, "STATE"),
(39, 47, "STATE_FULL"),
(48, 58, "CITY"),
(59, 64, "ZIPCODE"),
(65, 77, "TELEPHONE_NUMBER"),
]
}),
(
"4277 Buckhannan Avenue 13661 Mannsville 516-509-9328 New York NY 315-465-6016"
, {
"entities":[
(0, 22, "STREET_ADDRESS"),
(23, 28, "ZIPCODE"),
(29, 39, "CITY"),
(40, 52, "MOBILE_NUMBER"),
(53, 61, "STATE_FULL"),
(62, 64, "STATE"),
(65, 77, "TELEPHONE_NUMBER"),
]
}),
(
"New York 315-465-6016 516-509-9328 4277 Buckhannan Avenue Mannsville NY 13661"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 21, "TELEPHONE_NUMBER"),
(22, 34, "MOBILE_NUMBER"),
(35, 57, "STREET_ADDRESS"),
(58, 68, "CITY"),
(69, 71, "STATE"),
(72, 77, "ZIPCODE"),
]
}),
(
"816-448-6988 Kansas City 64106 Missouri 816-456-2216 320 Traders Alley MO"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 24, "CITY"),
(25, 30, "ZIPCODE"),
(31, 39, "STATE_FULL"),
(40, 52, "MOBILE_NUMBER"),
(53, 70, "STREET_ADDRESS"),
(71, 73, "STATE"),
]
}),
(
"Kansas City 320 Traders Alley 816-448-6988 816-456-2216 MO 64106 Missouri"
, {
"entities":[
(0, 11, "CITY"),
(12, 29, "STREET_ADDRESS"),
(30, 42, "TELEPHONE_NUMBER"),
(43, 55, "MOBILE_NUMBER"),
(56, 58, "STATE"),
(59, 64, "ZIPCODE"),
(65, 73, "STATE_FULL"),
]
}),
(
"MO 64106 816-448-6988 Missouri 320 Traders Alley 816-456-2216 Kansas City"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 21, "TELEPHONE_NUMBER"),
(22, 30, "STATE_FULL"),
(31, 48, "STREET_ADDRESS"),
(49, 61, "MOBILE_NUMBER"),
(62, 73, "CITY"),
]
}),
(
"816-456-2216 MO Missouri 64106 Kansas City 816-448-6988 320 Traders Alley"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 15, "STATE"),
(16, 24, "STATE_FULL"),
(25, 30, "ZIPCODE"),
(31, 42, "CITY"),
(43, 55, "TELEPHONE_NUMBER"),
(56, 73, "STREET_ADDRESS"),
]
}),
(
"Missouri 64106 320 Traders Alley Kansas City 816-448-6988 MO 816-456-2216"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 14, "ZIPCODE"),
(15, 32, "STREET_ADDRESS"),
(33, 44, "CITY"),
(45, 57, "TELEPHONE_NUMBER"),
(58, 60, "STATE"),
(61, 73, "MOBILE_NUMBER"),
]
}),
(
"Missouri 816-448-6988 320 Traders Alley 816-456-2216 64106 MO Kansas City"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 21, "TELEPHONE_NUMBER"),
(22, 39, "STREET_ADDRESS"),
(40, 52, "MOBILE_NUMBER"),
(53, 58, "ZIPCODE"),
(59, 61, "STATE"),
(62, 73, "CITY"),
]
}),
(
"Kansas City 816-456-2216 64106 Missouri MO 320 Traders Alley 816-448-6988"
, {
"entities":[
(0, 11, "CITY"),
(12, 24, "MOBILE_NUMBER"),
(25, 30, "ZIPCODE"),
(31, 39, "STATE_FULL"),
(40, 42, "STATE"),
(43, 60, "STREET_ADDRESS"),
(61, 73, "TELEPHONE_NUMBER"),
]
}),
(
"816-448-6988 816-456-2216 320 Traders Alley MO 64106 Kansas City Missouri"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 25, "MOBILE_NUMBER"),
(26, 43, "STREET_ADDRESS"),
(44, 46, "STATE"),
(47, 52, "ZIPCODE"),
(53, 64, "CITY"),
(65, 73, "STATE_FULL"),
]
}),
(
"MO Missouri Kansas City 64106 320 Traders Alley 816-456-2216 816-448-6988"
, {
"entities":[
(0, 2, "STATE"),
(3, 11, "STATE_FULL"),
(12, 23, "CITY"),
(24, 29, "ZIPCODE"),
(30, 47, "STREET_ADDRESS"),
(48, 60, "MOBILE_NUMBER"),
(61, 73, "TELEPHONE_NUMBER"),
]
}),
(
"320 Traders Alley Missouri MO Kansas City 64106 816-448-6988 816-456-2216"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 26, "STATE_FULL"),
(27, 29, "STATE"),
(30, 41, "CITY"),
(42, 47, "ZIPCODE"),
(48, 60, "TELEPHONE_NUMBER"),
(61, 73, "MOBILE_NUMBER"),
]
}),
(
"2400 Terra Street Washington Elma 360-470-6532 Contact Information 98541 WA 360-346-9410"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 28, "STATE_FULL"),
(29, 33, "CITY"),
(34, 46, "MOBILE_NUMBER"),
(67, 72, "ZIPCODE"),
(73, 75, "STATE"),
(76, 88, "TELEPHONE_NUMBER"),
]
}),
(
"98541 Elma 360-346-9410 WA Washington Contact Information 2400 Terra Street 360-470-6532"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 10, "CITY"),
(11, 23, "TELEPHONE_NUMBER"),
(24, 26, "STATE"),
(27, 37, "STATE_FULL"),
(58, 75, "STREET_ADDRESS"),
(76, 88, "MOBILE_NUMBER"),
]
}),
(
"360-346-9410 98541 Elma 2400 Terra Street 360-470-6532 Washington Contact Information WA"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 23, "CITY"),
(24, 41, "STREET_ADDRESS"),
(42, 54, "MOBILE_NUMBER"),
(55, 65, "STATE_FULL"),
(86, 88, "STATE"),
]
}),
(
"Washington 360-470-6532 360-346-9410 Elma 98541 Contact Information 2400 Terra Street WA"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 23, "MOBILE_NUMBER"),
(24, 36, "TELEPHONE_NUMBER"),
(37, 41, "CITY"),
(42, 47, "ZIPCODE"),
(68, 85, "STREET_ADDRESS"),
(86, 88, "STATE"),
]
}),
(
"360-470-6532 360-346-9410 Elma 2400 Terra Street Contact Information 98541 WA Washington"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 25, "TELEPHONE_NUMBER"),
(26, 30, "CITY"),
(31, 48, "STREET_ADDRESS"),
(69, 74, "ZIPCODE"),
(75, 77, "STATE"),
(78, 88, "STATE_FULL"),
]
}),
(
"Contact Information Washington 360-470-6532 360-346-9410 2400 Terra Street 98541 WA Elma"
, {
"entities":[
(20, 30, "STATE_FULL"),
(31, 43, "MOBILE_NUMBER"),
(44, 56, "TELEPHONE_NUMBER"),
(57, 74, "STREET_ADDRESS"),
(75, 80, "ZIPCODE"),
(81, 83, "STATE"),
(84, 88, "CITY"),
]
}),
(
"98541 Contact Information 360-346-9410 360-470-6532 Elma 2400 Terra Street Washington WA"
, {
"entities":[
(0, 5, "ZIPCODE"),
(26, 38, "TELEPHONE_NUMBER"),
(39, 51, "MOBILE_NUMBER"),
(52, 56, "CITY"),
(57, 74, "STREET_ADDRESS"),
(75, 85, "STATE_FULL"),
(86, 88, "STATE"),
]
}),
(
"98541 360-470-6532 Elma 2400 Terra Street Washington 360-346-9410 Contact Information WA"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "MOBILE_NUMBER"),
(19, 23, "CITY"),
(24, 41, "STREET_ADDRESS"),
(42, 52, "STATE_FULL"),
(53, 65, "TELEPHONE_NUMBER"),
(86, 88, "STATE"),
]
}),
(
"Contact Information 2400 Terra Street Washington Elma 360-346-9410 360-470-6532 98541 WA"
, {
"entities":[
(20, 37, "STREET_ADDRESS"),
(38, 48, "STATE_FULL"),
(49, 53, "CITY"),
(54, 66, "TELEPHONE_NUMBER"),
(67, 79, "MOBILE_NUMBER"),
(80, 85, "ZIPCODE"),
(86, 88, "STATE"),
]
}),
(
"Washington Contact Information 360-346-9410 WA 360-470-6532 98541 2400 Terra Street Elma"
, {
"entities":[
(0, 10, "STATE_FULL"),
(31, 43, "TELEPHONE_NUMBER"),
(44, 46, "STATE"),
(47, 59, "MOBILE_NUMBER"),
(60, 65, "ZIPCODE"),
(66, 83, "STREET_ADDRESS"),
(84, 88, "CITY"),
]
}),
(
"623-505-9901 4093 Cambridge Drive Arizona AZ 623-418-2864 85003 Phoenix"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 33, "STREET_ADDRESS"),
(34, 41, "STATE_FULL"),
(42, 44, "STATE"),
(45, 57, "MOBILE_NUMBER"),
(58, 63, "ZIPCODE"),
(64, 71, "CITY"),
]
}),
(
"623-418-2864 AZ 4093 Cambridge Drive 623-505-9901 85003 Arizona Phoenix"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 15, "STATE"),
(16, 36, "STREET_ADDRESS"),
(37, 49, "TELEPHONE_NUMBER"),
(50, 55, "ZIPCODE"),
(56, 63, "STATE_FULL"),
(64, 71, "CITY"),
]
}),
(
"623-418-2864 623-505-9901 4093 Cambridge Drive 85003 AZ Arizona Phoenix"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 25, "TELEPHONE_NUMBER"),
(26, 46, "STREET_ADDRESS"),
(47, 52, "ZIPCODE"),
(53, 55, "STATE"),
(56, 63, "STATE_FULL"),
(64, 71, "CITY"),
]
}),
(
"Arizona 85003 AZ 623-418-2864 623-505-9901 4093 Cambridge Drive Phoenix"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 13, "ZIPCODE"),
(14, 16, "STATE"),
(17, 29, "MOBILE_NUMBER"),
(30, 42, "TELEPHONE_NUMBER"),
(43, 63, "STREET_ADDRESS"),
(64, 71, "CITY"),
]
}),
(
"Arizona 623-418-2864 623-505-9901 85003 Phoenix 4093 Cambridge Drive AZ"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 20, "MOBILE_NUMBER"),
(21, 33, "TELEPHONE_NUMBER"),
(34, 39, "ZIPCODE"),
(40, 47, "CITY"),
(48, 68, "STREET_ADDRESS"),
(69, 71, "STATE"),
]
}),
(
"Arizona AZ 4093 Cambridge Drive Phoenix 85003 623-505-9901 623-418-2864"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 10, "STATE"),
(11, 31, "STREET_ADDRESS"),
(32, 39, "CITY"),
(40, 45, "ZIPCODE"),
(46, 58, "TELEPHONE_NUMBER"),
(59, 71, "MOBILE_NUMBER"),
]
}),
(
"623-505-9901 AZ 85003 4093 Cambridge Drive 623-418-2864 Arizona Phoenix"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 15, "STATE"),
(16, 21, "ZIPCODE"),
(22, 42, "STREET_ADDRESS"),
(43, 55, "MOBILE_NUMBER"),
(56, 63, "STATE_FULL"),
(64, 71, "CITY"),
]
}),
(
"AZ 4093 Cambridge Drive 85003 Arizona 623-418-2864 623-505-9901 Phoenix"
, {
"entities":[
(0, 2, "STATE"),
(3, 23, "STREET_ADDRESS"),
(24, 29, "ZIPCODE"),
(30, 37, "STATE_FULL"),
(38, 50, "MOBILE_NUMBER"),
(51, 63, "TELEPHONE_NUMBER"),
(64, 71, "CITY"),
]
}),
(
"AZ 623-505-9901 85003 Arizona Phoenix 623-418-2864 4093 Cambridge Drive"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "TELEPHONE_NUMBER"),
(16, 21, "ZIPCODE"),
(22, 29, "STATE_FULL"),
(30, 37, "CITY"),
(38, 50, "MOBILE_NUMBER"),
(51, 71, "STREET_ADDRESS"),
]
}),
(
"Arizona Phoenix AZ 85003 623-505-9901 623-418-2864 4093 Cambridge Drive"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 15, "CITY"),
(16, 18, "STATE"),
(19, 24, "ZIPCODE"),
(25, 37, "TELEPHONE_NUMBER"),
(38, 50, "MOBILE_NUMBER"),
(51, 71, "STREET_ADDRESS"),
]
}),
(
"3565 Eagle Lane 58271 MN 320-522-8479 Minnesota 218-823-1717 Pembina"
, {
"entities":[
(0, 15, "STREET_ADDRESS"),
(16, 21, "ZIPCODE"),
(22, 24, "STATE"),
(25, 37, "MOBILE_NUMBER"),
(38, 47, "STATE_FULL"),
(48, 60, "TELEPHONE_NUMBER"),
(61, 68, "CITY"),
]
}),
(
"3565 Eagle Lane 218-823-1717 58271 MN Pembina Minnesota 320-522-8479"
, {
"entities":[
(0, 15, "STREET_ADDRESS"),
(16, 28, "TELEPHONE_NUMBER"),
(29, 34, "ZIPCODE"),
(35, 37, "STATE"),
(38, 45, "CITY"),
(46, 55, "STATE_FULL"),
(56, 68, "MOBILE_NUMBER"),
]
}),
(
"3565 Eagle Lane Pembina MN 218-823-1717 320-522-8479 Minnesota 58271"
, {
"entities":[
(0, 15, "STREET_ADDRESS"),
(16, 23, "CITY"),
(24, 26, "STATE"),
(27, 39, "TELEPHONE_NUMBER"),
(40, 52, "MOBILE_NUMBER"),
(53, 62, "STATE_FULL"),
(63, 68, "ZIPCODE"),
]
}),
(
"Pembina Minnesota 58271 218-823-1717 MN 3565 Eagle Lane 320-522-8479"
, {
"entities":[
(0, 7, "CITY"),
(8, 17, "STATE_FULL"),
(18, 23, "ZIPCODE"),
(24, 36, "TELEPHONE_NUMBER"),
(37, 39, "STATE"),
(40, 55, "STREET_ADDRESS"),
(56, 68, "MOBILE_NUMBER"),
]
}),
(
"320-522-8479 218-823-1717 Pembina MN 3565 Eagle Lane Minnesota 58271"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 25, "TELEPHONE_NUMBER"),
(26, 33, "CITY"),
(34, 36, "STATE"),
(37, 52, "STREET_ADDRESS"),
(53, 62, "STATE_FULL"),
(63, 68, "ZIPCODE"),
]
}),
(
"MN Pembina 320-522-8479 58271 218-823-1717 Minnesota 3565 Eagle Lane"
, {
"entities":[
(0, 2, "STATE"),
(3, 10, "CITY"),
(11, 23, "MOBILE_NUMBER"),
(24, 29, "ZIPCODE"),
(30, 42, "TELEPHONE_NUMBER"),
(43, 52, "STATE_FULL"),
(53, 68, "STREET_ADDRESS"),
]
}),
(
"320-522-8479 MN 58271 Minnesota Pembina 3565 Eagle Lane 218-823-1717"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 15, "STATE"),
(16, 21, "ZIPCODE"),
(22, 31, "STATE_FULL"),
(32, 39, "CITY"),
(40, 55, "STREET_ADDRESS"),
(56, 68, "TELEPHONE_NUMBER"),
]
}),
(
"MN 3565 Eagle Lane 218-823-1717 Pembina 58271 320-522-8479 Minnesota"
, {
"entities":[
(0, 2, "STATE"),
(3, 18, "STREET_ADDRESS"),
(19, 31, "TELEPHONE_NUMBER"),
(32, 39, "CITY"),
(40, 45, "ZIPCODE"),
(46, 58, "MOBILE_NUMBER"),
(59, 68, "STATE_FULL"),
]
}),
(
"MN 3565 Eagle Lane 218-823-1717 Pembina 320-522-8479 Minnesota 58271"
, {
"entities":[
(0, 2, "STATE"),
(3, 18, "STREET_ADDRESS"),
(19, 31, "TELEPHONE_NUMBER"),
(32, 39, "CITY"),
(40, 52, "MOBILE_NUMBER"),
(53, 62, "STATE_FULL"),
(63, 68, "ZIPCODE"),
]
}),
(
"Pembina MN Minnesota 218-823-1717 3565 Eagle Lane 320-522-8479 58271"
, {
"entities":[
(0, 7, "CITY"),
(8, 10, "STATE"),
(11, 20, "STATE_FULL"),
(21, 33, "TELEPHONE_NUMBER"),
(34, 49, "STREET_ADDRESS"),
(50, 62, "MOBILE_NUMBER"),
(63, 68, "ZIPCODE"),
]
}),
(
"Camden 08102 NJ 609-636-3990 New Jersey 943 Valley Street 856-754-8023"
, {
"entities":[
(0, 6, "CITY"),
(7, 12, "ZIPCODE"),
(13, 15, "STATE"),
(16, 28, "MOBILE_NUMBER"),
(29, 39, "STATE_FULL"),
(40, 57, "STREET_ADDRESS"),
(58, 70, "TELEPHONE_NUMBER"),
]
}),
(
"08102 NJ New Jersey 856-754-8023 Camden 943 Valley Street 609-636-3990"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 19, "STATE_FULL"),
(20, 32, "TELEPHONE_NUMBER"),
(33, 39, "CITY"),
(40, 57, "STREET_ADDRESS"),
(58, 70, "MOBILE_NUMBER"),
]
}),
(
"Camden 856-754-8023 609-636-3990 NJ 08102 New Jersey 943 Valley Street"
, {
"entities":[
(0, 6, "CITY"),
(7, 19, "TELEPHONE_NUMBER"),
(20, 32, "MOBILE_NUMBER"),
(33, 35, "STATE"),
(36, 41, "ZIPCODE"),
(42, 52, "STATE_FULL"),
(53, 70, "STREET_ADDRESS"),
]
}),
(
"943 Valley Street 08102 609-636-3990 856-754-8023 Camden New Jersey NJ"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 23, "ZIPCODE"),
(24, 36, "MOBILE_NUMBER"),
(37, 49, "TELEPHONE_NUMBER"),
(50, 56, "CITY"),
(57, 67, "STATE_FULL"),
(68, 70, "STATE"),
]
}),
(
"Camden 609-636-3990 08102 856-754-8023 New Jersey 943 Valley Street NJ"
, {
"entities":[
(0, 6, "CITY"),
(7, 19, "MOBILE_NUMBER"),
(20, 25, "ZIPCODE"),
(26, 38, "TELEPHONE_NUMBER"),
(39, 49, "STATE_FULL"),
(50, 67, "STREET_ADDRESS"),
(68, 70, "STATE"),
]
}),
(
"Camden 609-636-3990 08102 NJ 856-754-8023 New Jersey 943 Valley Street"
, {
"entities":[
(0, 6, "CITY"),
(7, 19, "MOBILE_NUMBER"),
(20, 25, "ZIPCODE"),
(26, 28, "STATE"),
(29, 41, "TELEPHONE_NUMBER"),
(42, 52, "STATE_FULL"),
(53, 70, "STREET_ADDRESS"),
]
}),
(
"856-754-8023 Camden 943 Valley Street 08102 New Jersey 609-636-3990 NJ"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 19, "CITY"),
(20, 37, "STREET_ADDRESS"),
(38, 43, "ZIPCODE"),
(44, 54, "STATE_FULL"),
(55, 67, "MOBILE_NUMBER"),
(68, 70, "STATE"),
]
}),
(
"New Jersey Camden NJ 856-754-8023 943 Valley Street 08102 609-636-3990"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 17, "CITY"),
(18, 20, "STATE"),
(21, 33, "TELEPHONE_NUMBER"),
(34, 51, "STREET_ADDRESS"),
(52, 57, "ZIPCODE"),
(58, 70, "MOBILE_NUMBER"),
]
}),
(
"NJ New Jersey 08102 Camden 943 Valley Street 856-754-8023 609-636-3990"
, {
"entities":[
(0, 2, "STATE"),
(3, 13, "STATE_FULL"),
(14, 19, "ZIPCODE"),
(20, 26, "CITY"),
(27, 44, "STREET_ADDRESS"),
(45, 57, "TELEPHONE_NUMBER"),
(58, 70, "MOBILE_NUMBER"),
]
}),
(
"NJ 08102 856-754-8023 New Jersey 609-636-3990 943 Valley Street Camden"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 21, "TELEPHONE_NUMBER"),
(22, 32, "STATE_FULL"),
(33, 45, "MOBILE_NUMBER"),
(46, 63, "STREET_ADDRESS"),
(64, 70, "CITY"),
]
}),
(
"LA USE 504-342-0327 337-496-5586 2019 Rose Avenue Louisiana 70094 Avondale"
, {
"entities":[
(0, 2, "STATE"),
(7, 19, "TELEPHONE_NUMBER"),
(20, 32, "MOBILE_NUMBER"),
(33, 49, "STREET_ADDRESS"),
(50, 59, "STATE_FULL"),
(60, 65, "ZIPCODE"),
(66, 74, "CITY"),
]
}),
(
"Louisiana 504-342-0327 Avondale 2019 Rose Avenue USE LA 70094 337-496-5586"
, {
"entities":[
(0, 9, "STATE_FULL"),
(10, 22, "TELEPHONE_NUMBER"),
(23, 31, "CITY"),
(32, 48, "STREET_ADDRESS"),
(53, 55, "STATE"),
(56, 61, "ZIPCODE"),
(62, 74, "MOBILE_NUMBER"),
]
}),
(
"Avondale 70094 337-496-5586 2019 Rose Avenue 504-342-0327 Louisiana USE LA"
, {
"entities":[
(0, 8, "CITY"),
(9, 14, "ZIPCODE"),
(15, 27, "MOBILE_NUMBER"),
(28, 44, "STREET_ADDRESS"),
(45, 57, "TELEPHONE_NUMBER"),
(58, 67, "STATE_FULL"),
(72, 74, "STATE"),
]
}),
(
"Avondale USE 337-496-5586 504-342-0327 70094 LA 2019 Rose Avenue Louisiana"
, {
"entities":[
(0, 8, "CITY"),
(13, 25, "MOBILE_NUMBER"),
(26, 38, "TELEPHONE_NUMBER"),
(39, 44, "ZIPCODE"),
(45, 47, "STATE"),
(48, 64, "STREET_ADDRESS"),
(65, 74, "STATE_FULL"),
]
}),
(
"Avondale 2019 Rose Avenue LA 337-496-5586 USE 504-342-0327 70094 Louisiana"
, {
"entities":[
(0, 8, "CITY"),
(9, 25, "STREET_ADDRESS"),
(26, 28, "STATE"),
(29, 41, "MOBILE_NUMBER"),
(46, 58, "TELEPHONE_NUMBER"),
(59, 64, "ZIPCODE"),
(65, 74, "STATE_FULL"),
]
}),
(
"USE 504-342-0327 LA 337-496-5586 Louisiana Avondale 70094 2019 Rose Avenue"
, {
"entities":[
(4, 16, "TELEPHONE_NUMBER"),
(17, 19, "STATE"),
(20, 32, "MOBILE_NUMBER"),
(33, 42, "STATE_FULL"),
(43, 51, "CITY"),
(52, 57, "ZIPCODE"),
(58, 74, "STREET_ADDRESS"),
]
}),
(
"337-496-5586 Louisiana 2019 Rose Avenue USE LA 504-342-0327 70094 Avondale"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 22, "STATE_FULL"),
(23, 39, "STREET_ADDRESS"),
(44, 46, "STATE"),
(47, 59, "TELEPHONE_NUMBER"),
(60, 65, "ZIPCODE"),
(66, 74, "CITY"),
]
}),
(
"504-342-0327 2019 Rose Avenue 70094 Louisiana LA USE Avondale 337-496-5586"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 29, "STREET_ADDRESS"),
(30, 35, "ZIPCODE"),
(36, 45, "STATE_FULL"),
(46, 48, "STATE"),
(53, 61, "CITY"),
(62, 74, "MOBILE_NUMBER"),
]
}),
(
"Avondale 70094 USE Louisiana LA 504-342-0327 337-496-5586 2019 Rose Avenue"
, {
"entities":[
(0, 8, "CITY"),
(9, 14, "ZIPCODE"),
(19, 28, "STATE_FULL"),
(29, 31, "STATE"),
(32, 44, "TELEPHONE_NUMBER"),
(45, 57, "MOBILE_NUMBER"),
(58, 74, "STREET_ADDRESS"),
]
}),
(
"2019 Rose Avenue 70094 Avondale 337-496-5586 USE Louisiana 504-342-0327 LA"
, {
"entities":[
(0, 16, "STREET_ADDRESS"),
(17, 22, "ZIPCODE"),
(23, 31, "CITY"),
(32, 44, "MOBILE_NUMBER"),
(49, 58, "STATE_FULL"),
(59, 71, "TELEPHONE_NUMBER"),
(72, 74, "STATE"),
]
}),
(
"Phone Arizona 928-306-7425 2658 Brown Street 928-207-0898 85901 Show Low AZ"
, {
"entities":[
(6, 13, "STATE_FULL"),
(14, 26, "MOBILE_NUMBER"),
(27, 44, "STREET_ADDRESS"),
(45, 57, "TELEPHONE_NUMBER"),
(58, 63, "ZIPCODE"),
(64, 72, "CITY"),
(73, 75, "STATE"),
]
}),
(
"85901 928-306-7425 Show Low AZ Arizona 2658 Brown Street Phone 928-207-0898"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "MOBILE_NUMBER"),
(19, 27, "CITY"),
(28, 30, "STATE"),
(31, 38, "STATE_FULL"),
(39, 56, "STREET_ADDRESS"),
(63, 75, "TELEPHONE_NUMBER"),
]
}),
(
"85901 Arizona 928-306-7425 Phone 2658 Brown Street Show Low 928-207-0898 AZ"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 13, "STATE_FULL"),
(14, 26, "MOBILE_NUMBER"),
(33, 50, "STREET_ADDRESS"),
(51, 59, "CITY"),
(60, 72, "TELEPHONE_NUMBER"),
(73, 75, "STATE"),
]
}),
(
"928-207-0898 85901 928-306-7425 AZ Arizona Phone 2658 Brown Street Show Low"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 31, "MOBILE_NUMBER"),
(32, 34, "STATE"),
(35, 42, "STATE_FULL"),
(49, 66, "STREET_ADDRESS"),
(67, 75, "CITY"),
]
}),
(
"928-306-7425 Phone 85901 2658 Brown Street Show Low AZ Arizona 928-207-0898"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(19, 24, "ZIPCODE"),
(25, 42, "STREET_ADDRESS"),
(43, 51, "CITY"),
(52, 54, "STATE"),
(55, 62, "STATE_FULL"),
(63, 75, "TELEPHONE_NUMBER"),
]
}),
(
"85901 AZ 928-306-7425 Arizona 2658 Brown Street 928-207-0898 Show Low Phone"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 21, "MOBILE_NUMBER"),
(22, 29, "STATE_FULL"),
(30, 47, "STREET_ADDRESS"),
(48, 60, "TELEPHONE_NUMBER"),
(61, 69, "CITY"),
]
}),
(
"AZ 2658 Brown Street 928-207-0898 Show Low 928-306-7425 Phone 85901 Arizona"
, {
"entities":[
(0, 2, "STATE"),
(3, 20, "STREET_ADDRESS"),
(21, 33, "TELEPHONE_NUMBER"),
(34, 42, "CITY"),
(43, 55, "MOBILE_NUMBER"),
(62, 67, "ZIPCODE"),
(68, 75, "STATE_FULL"),
]
}),
(
"Show Low Phone 2658 Brown Street Arizona 928-306-7425 85901 AZ 928-207-0898"
, {
"entities":[
(0, 8, "CITY"),
(15, 32, "STREET_ADDRESS"),
(33, 40, "STATE_FULL"),
(41, 53, "MOBILE_NUMBER"),
(54, 59, "ZIPCODE"),
(60, 62, "STATE"),
(63, 75, "TELEPHONE_NUMBER"),
]
}),
(
"Phone 928-306-7425 Arizona 2658 Brown Street AZ 928-207-0898 85901 Show Low"
, {
"entities":[
(6, 18, "MOBILE_NUMBER"),
(19, 26, "STATE_FULL"),
(27, 44, "STREET_ADDRESS"),
(45, 47, "STATE"),
(48, 60, "TELEPHONE_NUMBER"),
(61, 66, "ZIPCODE"),
(67, 75, "CITY"),
]
}),
(
"85901 Show Low Arizona AZ 928-306-7425 2658 Brown Street Phone 928-207-0898"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 14, "CITY"),
(15, 22, "STATE_FULL"),
(23, 25, "STATE"),
(26, 38, "MOBILE_NUMBER"),
(39, 56, "STREET_ADDRESS"),
(63, 75, "TELEPHONE_NUMBER"),
]
}),
(
"Sherman Oaks 91403 California 4074 Quiet Valley Lane 818-944-7796 818-740-4239 CA"
, {
"entities":[
(0, 12, "CITY"),
(13, 18, "ZIPCODE"),
(19, 29, "STATE_FULL"),
(30, 52, "STREET_ADDRESS"),
(53, 65, "TELEPHONE_NUMBER"),
(66, 78, "MOBILE_NUMBER"),
(79, 81, "STATE"),
]
}),
(
"California 4074 Quiet Valley Lane 91403 CA 818-740-4239 Sherman Oaks 818-944-7796"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 33, "STREET_ADDRESS"),
(34, 39, "ZIPCODE"),
(40, 42, "STATE"),
(43, 55, "MOBILE_NUMBER"),
(56, 68, "CITY"),
(69, 81, "TELEPHONE_NUMBER"),
]
}),
(
"California 818-944-7796 Sherman Oaks 91403 4074 Quiet Valley Lane CA 818-740-4239"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 23, "TELEPHONE_NUMBER"),
(24, 36, "CITY"),
(37, 42, "ZIPCODE"),
(43, 65, "STREET_ADDRESS"),
(66, 68, "STATE"),
(69, 81, "MOBILE_NUMBER"),
]
}),
(
"California 91403 Sherman Oaks 818-740-4239 818-944-7796 4074 Quiet Valley Lane CA"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 16, "ZIPCODE"),
(17, 29, "CITY"),
(30, 42, "MOBILE_NUMBER"),
(43, 55, "TELEPHONE_NUMBER"),
(56, 78, "STREET_ADDRESS"),
(79, 81, "STATE"),
]
}),
(
"CA 91403 California 818-944-7796 818-740-4239 4074 Quiet Valley Lane Sherman Oaks"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 19, "STATE_FULL"),
(20, 32, "TELEPHONE_NUMBER"),
(33, 45, "MOBILE_NUMBER"),
(46, 68, "STREET_ADDRESS"),
(69, 81, "CITY"),
]
}),
(
"California 818-740-4239 91403 Sherman Oaks CA 818-944-7796 4074 Quiet Valley Lane"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 23, "MOBILE_NUMBER"),
(24, 29, "ZIPCODE"),
(30, 42, "CITY"),
(43, 45, "STATE"),
(46, 58, "TELEPHONE_NUMBER"),
(59, 81, "STREET_ADDRESS"),
]
}),
(
"818-944-7796 4074 Quiet Valley Lane California 91403 818-740-4239 Sherman Oaks CA"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 35, "STREET_ADDRESS"),
(36, 46, "STATE_FULL"),
(47, 52, "ZIPCODE"),
(53, 65, "MOBILE_NUMBER"),
(66, 78, "CITY"),
(79, 81, "STATE"),
]
}),
(
"818-740-4239 California CA 818-944-7796 4074 Quiet Valley Lane Sherman Oaks 91403"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 23, "STATE_FULL"),
(24, 26, "STATE"),
(27, 39, "TELEPHONE_NUMBER"),
(40, 62, "STREET_ADDRESS"),
(63, 75, "CITY"),
(76, 81, "ZIPCODE"),
]
}),
(
"4074 Quiet Valley Lane California CA Sherman Oaks 91403 818-944-7796 818-740-4239"
, {
"entities":[
(0, 22, "STREET_ADDRESS"),
(23, 33, "STATE_FULL"),
(34, 36, "STATE"),
(37, 49, "CITY"),
(50, 55, "ZIPCODE"),
(56, 68, "TELEPHONE_NUMBER"),
(69, 81, "MOBILE_NUMBER"),
]
}),
(
"818-944-7796 4074 Quiet Valley Lane Sherman Oaks CA 818-740-4239 California 91403"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 35, "STREET_ADDRESS"),
(36, 48, "CITY"),
(49, 51, "STATE"),
(52, 64, "MOBILE_NUMBER"),
(65, 75, "STATE_FULL"),
(76, 81, "ZIPCODE"),
]
}),
(
"2061 Simons Hollow Road 570-788-0529 Pennsylvania Conyngham PA 18219 412-352-9036"
, {
"entities":[
(0, 23, "STREET_ADDRESS"),
(24, 36, "TELEPHONE_NUMBER"),
(37, 49, "STATE_FULL"),
(50, 59, "CITY"),
(60, 62, "STATE"),
(63, 68, "ZIPCODE"),
(69, 81, "MOBILE_NUMBER"),
]
}),
(
"2061 Simons Hollow Road 570-788-0529 Conyngham 18219 PA Pennsylvania 412-352-9036"
, {
"entities":[
(0, 23, "STREET_ADDRESS"),
(24, 36, "TELEPHONE_NUMBER"),
(37, 46, "CITY"),
(47, 52, "ZIPCODE"),
(53, 55, "STATE"),
(56, 68, "STATE_FULL"),
(69, 81, "MOBILE_NUMBER"),
]
}),
(
"18219 PA 412-352-9036 Conyngham Pennsylvania 570-788-0529 2061 Simons Hollow Road"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 21, "MOBILE_NUMBER"),
(22, 31, "CITY"),
(32, 44, "STATE_FULL"),
(45, 57, "TELEPHONE_NUMBER"),
(58, 81, "STREET_ADDRESS"),
]
}),
(
"Pennsylvania Conyngham 18219 2061 Simons Hollow Road 570-788-0529 412-352-9036 PA"
, {
"entities":[
(0, 12, "STATE_FULL"),
(13, 22, "CITY"),
(23, 28, "ZIPCODE"),
(29, 52, "STREET_ADDRESS"),
(53, 65, "TELEPHONE_NUMBER"),
(66, 78, "MOBILE_NUMBER"),
(79, 81, "STATE"),
]
}),
(
"18219 Conyngham PA Pennsylvania 412-352-9036 2061 Simons Hollow Road 570-788-0529"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 15, "CITY"),
(16, 18, "STATE"),
(19, 31, "STATE_FULL"),
(32, 44, "MOBILE_NUMBER"),
(45, 68, "STREET_ADDRESS"),
(69, 81, "TELEPHONE_NUMBER"),
]
}),
(
"PA Conyngham 570-788-0529 18219 412-352-9036 2061 Simons Hollow Road Pennsylvania"
, {
"entities":[
(0, 2, "STATE"),
(3, 12, "CITY"),
(13, 25, "TELEPHONE_NUMBER"),
(26, 31, "ZIPCODE"),
(32, 44, "MOBILE_NUMBER"),
(45, 68, "STREET_ADDRESS"),
(69, 81, "STATE_FULL"),
]
}),
(
"PA 570-788-0529 18219 Pennsylvania 412-352-9036 2061 Simons Hollow Road Conyngham"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "TELEPHONE_NUMBER"),
(16, 21, "ZIPCODE"),
(22, 34, "STATE_FULL"),
(35, 47, "MOBILE_NUMBER"),
(48, 71, "STREET_ADDRESS"),
(72, 81, "CITY"),
]
}),
(
"Pennsylvania 18219 2061 Simons Hollow Road 412-352-9036 PA 570-788-0529 Conyngham"
, {
"entities":[
(0, 12, "STATE_FULL"),
(13, 18, "ZIPCODE"),
(19, 42, "STREET_ADDRESS"),
(43, 55, "MOBILE_NUMBER"),
(56, 58, "STATE"),
(59, 71, "TELEPHONE_NUMBER"),
(72, 81, "CITY"),
]
}),
(
"PA 570-788-0529 2061 Simons Hollow Road Pennsylvania 18219 Conyngham 412-352-9036"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "TELEPHONE_NUMBER"),
(16, 39, "STREET_ADDRESS"),
(40, 52, "STATE_FULL"),
(53, 58, "ZIPCODE"),
(59, 68, "CITY"),
(69, 81, "MOBILE_NUMBER"),
]
}),
(
"412-352-9036 PA Conyngham 570-788-0529 18219 2061 Simons Hollow Road Pennsylvania"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 15, "STATE"),
(16, 25, "CITY"),
(26, 38, "TELEPHONE_NUMBER"),
(39, 44, "ZIPCODE"),
(45, 68, "STREET_ADDRESS"),
(69, 81, "STATE_FULL"),
]
}),
(
"307-275-7775 Wyoming 3198 Arbor Court Cheyenne 307-630-9285 82001 WY"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 20, "STATE_FULL"),
(21, 37, "STREET_ADDRESS"),
(38, 46, "CITY"),
(47, 59, "MOBILE_NUMBER"),
(60, 65, "ZIPCODE"),
(66, 68, "STATE"),
]
}),
(
"WY 307-630-9285 82001 Cheyenne 307-275-7775 3198 Arbor Court Wyoming"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "MOBILE_NUMBER"),
(16, 21, "ZIPCODE"),
(22, 30, "CITY"),
(31, 43, "TELEPHONE_NUMBER"),
(44, 60, "STREET_ADDRESS"),
(61, 68, "STATE_FULL"),
]
}),
(
"Wyoming 3198 Arbor Court 82001 Cheyenne WY 307-630-9285 307-275-7775"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 24, "STREET_ADDRESS"),
(25, 30, "ZIPCODE"),
(31, 39, "CITY"),
(40, 42, "STATE"),
(43, 55, "MOBILE_NUMBER"),
(56, 68, "TELEPHONE_NUMBER"),
]
}),
(
"Cheyenne 307-630-9285 82001 3198 Arbor Court WY 307-275-7775 Wyoming"
, {
"entities":[
(0, 8, "CITY"),
(9, 21, "MOBILE_NUMBER"),
(22, 27, "ZIPCODE"),
(28, 44, "STREET_ADDRESS"),
(45, 47, "STATE"),
(48, 60, "TELEPHONE_NUMBER"),
(61, 68, "STATE_FULL"),
]
}),
(
"82001 3198 Arbor Court Cheyenne Wyoming 307-275-7775 WY 307-630-9285"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 22, "STREET_ADDRESS"),
(23, 31, "CITY"),
(32, 39, "STATE_FULL"),
(40, 52, "TELEPHONE_NUMBER"),
(53, 55, "STATE"),
(56, 68, "MOBILE_NUMBER"),
]
}),
(
"Wyoming 3198 Arbor Court WY 307-630-9285 Cheyenne 307-275-7775 82001"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 24, "STREET_ADDRESS"),
(25, 27, "STATE"),
(28, 40, "MOBILE_NUMBER"),
(41, 49, "CITY"),
(50, 62, "TELEPHONE_NUMBER"),
(63, 68, "ZIPCODE"),
]
}),
(
"Cheyenne 307-630-9285 WY 3198 Arbor Court 82001 Wyoming 307-275-7775"
, {
"entities":[
(0, 8, "CITY"),
(9, 21, "MOBILE_NUMBER"),
(22, 24, "STATE"),
(25, 41, "STREET_ADDRESS"),
(42, 47, "ZIPCODE"),
(48, 55, "STATE_FULL"),
(56, 68, "TELEPHONE_NUMBER"),
]
}),
(
"307-275-7775 307-630-9285 Wyoming Cheyenne WY 3198 Arbor Court 82001"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 25, "MOBILE_NUMBER"),
(26, 33, "STATE_FULL"),
(34, 42, "CITY"),
(43, 45, "STATE"),
(46, 62, "STREET_ADDRESS"),
(63, 68, "ZIPCODE"),
]
}),
(
"Wyoming 307-630-9285 3198 Arbor Court 82001 WY Cheyenne 307-275-7775"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 20, "MOBILE_NUMBER"),
(21, 37, "STREET_ADDRESS"),
(38, 43, "ZIPCODE"),
(44, 46, "STATE"),
(47, 55, "CITY"),
(56, 68, "TELEPHONE_NUMBER"),
]
}),
(
"Cheyenne 307-630-9285 WY 82001 3198 Arbor Court 307-275-7775 Wyoming"
, {
"entities":[
(0, 8, "CITY"),
(9, 21, "MOBILE_NUMBER"),
(22, 24, "STATE"),
(25, 30, "ZIPCODE"),
(31, 47, "STREET_ADDRESS"),
(48, 60, "TELEPHONE_NUMBER"),
(61, 68, "STATE_FULL"),
]
}),
(
"20009 Contact 650-948--9331 DC 4390 Massachusetts Avenue 202-667-7005 Washington Washington DC"
, {
"entities":[
(0, 5, "ZIPCODE"),
(14, 27, "MOBILE_NUMBER"),
(28, 30, "STATE"),
(31, 56, "STREET_ADDRESS"),
(57, 69, "TELEPHONE_NUMBER"),
(70, 80, "CITY"),
(81, 94, "STATE_FULL"),
]
}),
(
"Washington DC 20009 Contact 202-667-7005 4390 Massachusetts Avenue DC Washington 650-948--9331"
, {
"entities":[
(0, 13, "STATE_FULL"),
(14, 19, "ZIPCODE"),
(28, 40, "TELEPHONE_NUMBER"),
(41, 66, "STREET_ADDRESS"),
(67, 69, "STATE"),
(70, 80, "CITY"),
(81, 94, "MOBILE_NUMBER"),
]
}),
(
"4390 Massachusetts Avenue 650-948--9331 Washington Washington DC 202-667-7005 20009 DC Contact"
, {
"entities":[
(0, 25, "STREET_ADDRESS"),
(26, 39, "MOBILE_NUMBER"),
(40, 50, "CITY"),
(51, 64, "STATE_FULL"),
(65, 77, "TELEPHONE_NUMBER"),
(78, 83, "ZIPCODE"),
(84, 86, "STATE"),
]
}),
(
"202-667-7005 Contact Washington 650-948--9331 20009 DC Washington DC 4390 Massachusetts Avenue"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(21, 31, "CITY"),
(32, 45, "MOBILE_NUMBER"),
(46, 51, "ZIPCODE"),
(52, 54, "STATE"),
(55, 68, "STATE_FULL"),
(69, 94, "STREET_ADDRESS"),
]
}),
(
"20009 DC 650-948--9331 202-667-7005 Contact Washington DC Washington 4390 Massachusetts Avenue"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 22, "MOBILE_NUMBER"),
(23, 35, "TELEPHONE_NUMBER"),
(44, 57, "STATE_FULL"),
(58, 68, "CITY"),
(69, 94, "STREET_ADDRESS"),
]
}),
(
"650-948--9331 202-667-7005 DC Washington 20009 4390 Massachusetts Avenue Contact Washington DC"
, {
"entities":[
(0, 13, "MOBILE_NUMBER"),
(14, 26, "TELEPHONE_NUMBER"),
(27, 29, "STATE"),
(30, 40, "CITY"),
(41, 46, "ZIPCODE"),
(47, 72, "STREET_ADDRESS"),
(81, 94, "STATE_FULL"),
]
}),
(
"DC 4390 Massachusetts Avenue Washington DC 650-948--9331 Contact Washington 20009 202-667-7005"
, {
"entities":[
(0, 2, "STATE"),
(3, 28, "STREET_ADDRESS"),
(29, 42, "STATE_FULL"),
(43, 56, "MOBILE_NUMBER"),
(65, 75, "CITY"),
(76, 81, "ZIPCODE"),
(82, 94, "TELEPHONE_NUMBER"),
]
}),
(
"4390 Massachusetts Avenue 20009 Contact DC 202-667-7005 650-948--9331 Washington DC Washington"
, {
"entities":[
(0, 25, "STREET_ADDRESS"),
(26, 31, "ZIPCODE"),
(40, 42, "STATE"),
(43, 55, "TELEPHONE_NUMBER"),
(56, 69, "MOBILE_NUMBER"),
(70, 83, "STATE_FULL"),
(84, 94, "CITY"),
]
}),
(
"Washington DC DC 20009 650-948--9331 Washington 202-667-7005 4390 Massachusetts Avenue Contact"
, {
"entities":[
(0, 13, "STATE_FULL"),
(14, 16, "STATE"),
(17, 22, "ZIPCODE"),
(23, 36, "MOBILE_NUMBER"),
(37, 47, "CITY"),
(48, 60, "TELEPHONE_NUMBER"),
(61, 86, "STREET_ADDRESS"),
]
}),
(
"DC Washington Washington DC Contact 650-948--9331 4390 Massachusetts Avenue 20009 202-667-7005"
, {
"entities":[
(0, 2, "STATE"),
(3, 13, "CITY"),
(14, 27, "STATE_FULL"),
(36, 49, "MOBILE_NUMBER"),
(50, 75, "STREET_ADDRESS"),
(76, 81, "ZIPCODE"),
(82, 94, "TELEPHONE_NUMBER"),
]
}),
(
"3111 Freshour Circle San Antonio Texas TX 210-261-7437 Number 210-638-5347 78205"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 32, "CITY"),
(33, 38, "STATE_FULL"),
(39, 41, "STATE"),
(42, 54, "TELEPHONE_NUMBER"),
(62, 74, "MOBILE_NUMBER"),
(75, 80, "ZIPCODE"),
]
}),
(
"210-261-7437 Number 3111 Freshour Circle 78205 San Antonio Texas 210-638-5347 TX"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(20, 40, "STREET_ADDRESS"),
(41, 46, "ZIPCODE"),
(47, 58, "CITY"),
(59, 64, "STATE_FULL"),
(65, 77, "MOBILE_NUMBER"),
(78, 80, "STATE"),
]
}),
(
"San Antonio Texas Number TX 78205 210-261-7437 210-638-5347 3111 Freshour Circle"
, {
"entities":[
(0, 11, "CITY"),
(12, 17, "STATE_FULL"),
(25, 27, "STATE"),
(28, 33, "ZIPCODE"),
(34, 46, "TELEPHONE_NUMBER"),
(47, 59, "MOBILE_NUMBER"),
(60, 80, "STREET_ADDRESS"),
]
}),
(
"210-638-5347 TX San Antonio 210-261-7437 78205 3111 Freshour Circle Number Texas"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 15, "STATE"),
(16, 27, "CITY"),
(28, 40, "TELEPHONE_NUMBER"),
(41, 46, "ZIPCODE"),
(47, 67, "STREET_ADDRESS"),
(75, 80, "STATE_FULL"),
]
}),
(
"TX 3111 Freshour Circle 210-261-7437 210-638-5347 Texas 78205 San Antonio Number"
, {
"entities":[
(0, 2, "STATE"),
(3, 23, "STREET_ADDRESS"),
(24, 36, "TELEPHONE_NUMBER"),
(37, 49, "MOBILE_NUMBER"),
(50, 55, "STATE_FULL"),
(56, 61, "ZIPCODE"),
(62, 73, "CITY"),
]
}),
(
"TX Number 210-638-5347 San Antonio 210-261-7437 Texas 3111 Freshour Circle 78205"
, {
"entities":[
(0, 2, "STATE"),
(10, 22, "MOBILE_NUMBER"),
(23, 34, "CITY"),
(35, 47, "TELEPHONE_NUMBER"),
(48, 53, "STATE_FULL"),
(54, 74, "STREET_ADDRESS"),
(75, 80, "ZIPCODE"),
]
}),
(
"San Antonio TX Texas 210-261-7437 Number 210-638-5347 78205 3111 Freshour Circle"
, {
"entities":[
(0, 11, "CITY"),
(12, 14, "STATE"),
(15, 20, "STATE_FULL"),
(21, 33, "TELEPHONE_NUMBER"),
(41, 53, "MOBILE_NUMBER"),
(54, 59, "ZIPCODE"),
(60, 80, "STREET_ADDRESS"),
]
}),
(
"3111 Freshour Circle 78205 210-638-5347 Number TX Texas San Antonio 210-261-7437"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 26, "ZIPCODE"),
(27, 39, "MOBILE_NUMBER"),
(47, 49, "STATE"),
(50, 55, "STATE_FULL"),
(56, 67, "CITY"),
(68, 80, "TELEPHONE_NUMBER"),
]
}),
(
"Number 210-638-5347 78205 San Antonio TX Texas 3111 Freshour Circle 210-261-7437"
, {
"entities":[
(7, 19, "MOBILE_NUMBER"),
(20, 25, "ZIPCODE"),
(26, 37, "CITY"),
(38, 40, "STATE"),
(41, 46, "STATE_FULL"),
(47, 67, "STREET_ADDRESS"),
(68, 80, "TELEPHONE_NUMBER"),
]
}),
(
"Texas 210-638-5347 210-261-7437 Number 3111 Freshour Circle TX San Antonio 78205"
, {
"entities":[
(0, 5, "STATE_FULL"),
(6, 18, "MOBILE_NUMBER"),
(19, 31, "TELEPHONE_NUMBER"),
(39, 59, "STREET_ADDRESS"),
(60, 62, "STATE"),
(63, 74, "CITY"),
(75, 80, "ZIPCODE"),
]
}),
(
"281-414-3963 Texas 77021 713-749-2042 2547 Michael Street TX Houston"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 18, "STATE_FULL"),
(19, 24, "ZIPCODE"),
(25, 37, "TELEPHONE_NUMBER"),
(38, 57, "STREET_ADDRESS"),
(58, 60, "STATE"),
(61, 68, "CITY"),
]
}),
(
"TX 2547 Michael Street Texas 77021 281-414-3963 713-749-2042 Houston"
, {
"entities":[
(0, 2, "STATE"),
(3, 22, "STREET_ADDRESS"),
(23, 28, "STATE_FULL"),
(29, 34, "ZIPCODE"),
(35, 47, "MOBILE_NUMBER"),
(48, 60, "TELEPHONE_NUMBER"),
(61, 68, "CITY"),
]
}),
(
"Texas 77021 TX 2547 Michael Street 713-749-2042 Houston 281-414-3963"
, {
"entities":[
(0, 5, "STATE_FULL"),
(6, 11, "ZIPCODE"),
(12, 14, "STATE"),
(15, 34, "STREET_ADDRESS"),
(35, 47, "TELEPHONE_NUMBER"),
(48, 55, "CITY"),
(56, 68, "MOBILE_NUMBER"),
]
}),
(
"2547 Michael Street 281-414-3963 TX Texas Houston 713-749-2042 77021"
, {
"entities":[
(0, 19, "STREET_ADDRESS"),
(20, 32, "MOBILE_NUMBER"),
(33, 35, "STATE"),
(36, 41, "STATE_FULL"),
(42, 49, "CITY"),
(50, 62, "TELEPHONE_NUMBER"),
(63, 68, "ZIPCODE"),
]
}),
(
"713-749-2042 281-414-3963 TX Houston 2547 Michael Street Texas 77021"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 25, "MOBILE_NUMBER"),
(26, 28, "STATE"),
(29, 36, "CITY"),
(37, 56, "STREET_ADDRESS"),
(57, 62, "STATE_FULL"),
(63, 68, "ZIPCODE"),
]
}),
(
"TX 2547 Michael Street 713-749-2042 Texas 77021 Houston 281-414-3963"
, {
"entities":[
(0, 2, "STATE"),
(3, 22, "STREET_ADDRESS"),
(23, 35, "TELEPHONE_NUMBER"),
(36, 41, "STATE_FULL"),
(42, 47, "ZIPCODE"),
(48, 55, "CITY"),
(56, 68, "MOBILE_NUMBER"),
]
}),
(
"TX 713-749-2042 281-414-3963 Houston 77021 2547 Michael Street Texas"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "TELEPHONE_NUMBER"),
(16, 28, "MOBILE_NUMBER"),
(29, 36, "CITY"),
(37, 42, "ZIPCODE"),
(43, 62, "STREET_ADDRESS"),
(63, 68, "STATE_FULL"),
]
}),
(
"Houston 281-414-3963 713-749-2042 77021 TX Texas 2547 Michael Street"
, {
"entities":[
(0, 7, "CITY"),
(8, 20, "MOBILE_NUMBER"),
(21, 33, "TELEPHONE_NUMBER"),
(34, 39, "ZIPCODE"),
(40, 42, "STATE"),
(43, 48, "STATE_FULL"),
(49, 68, "STREET_ADDRESS"),
]
}),
(
"Houston 2547 Michael Street 713-749-2042 281-414-3963 TX 77021 Texas"
, {
"entities":[
(0, 7, "CITY"),
(8, 27, "STREET_ADDRESS"),
(28, 40, "TELEPHONE_NUMBER"),
(41, 53, "MOBILE_NUMBER"),
(54, 56, "STATE"),
(57, 62, "ZIPCODE"),
(63, 68, "STATE_FULL"),
]
}),
(
"TX 281-414-3963 Texas 77021 2547 Michael Street Houston 713-749-2042"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "MOBILE_NUMBER"),
(16, 21, "STATE_FULL"),
(22, 27, "ZIPCODE"),
(28, 47, "STREET_ADDRESS"),
(48, 55, "CITY"),
(56, 68, "TELEPHONE_NUMBER"),
]
}),
(
"21061 MD 443-618-6351 Maryland 410-508-1550 number Glen Burnie 450 Columbia Boulevard"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 21, "MOBILE_NUMBER"),
(22, 30, "STATE_FULL"),
(31, 43, "TELEPHONE_NUMBER"),
(51, 62, "CITY"),
(63, 85, "STREET_ADDRESS"),
]
}),
(
"450 Columbia Boulevard Maryland 21061 410-508-1550 443-618-6351 MD Glen Burnie number"
, {
"entities":[
(0, 22, "STREET_ADDRESS"),
(23, 31, "STATE_FULL"),
(32, 37, "ZIPCODE"),
(38, 50, "TELEPHONE_NUMBER"),
(51, 63, "MOBILE_NUMBER"),
(64, 66, "STATE"),
(67, 78, "CITY"),
]
}),
(
"number Maryland 450 Columbia Boulevard 443-618-6351 410-508-1550 MD 21061 Glen Burnie"
, {
"entities":[
(7, 15, "STATE_FULL"),
(16, 38, "STREET_ADDRESS"),
(39, 51, "MOBILE_NUMBER"),
(52, 64, "TELEPHONE_NUMBER"),
(65, 67, "STATE"),
(68, 73, "ZIPCODE"),
(74, 85, "CITY"),
]
}),
(
"21061 410-508-1550 MD Maryland number Glen Burnie 450 Columbia Boulevard 443-618-6351"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "TELEPHONE_NUMBER"),
(19, 21, "STATE"),
(22, 30, "STATE_FULL"),
(38, 49, "CITY"),
(50, 72, "STREET_ADDRESS"),
(73, 85, "MOBILE_NUMBER"),
]
}),
(
"MD Maryland number 450 Columbia Boulevard 410-508-1550 Glen Burnie 21061 443-618-6351"
, {
"entities":[
(0, 2, "STATE"),
(3, 11, "STATE_FULL"),
(19, 41, "STREET_ADDRESS"),
(42, 54, "TELEPHONE_NUMBER"),
(55, 66, "CITY"),
(67, 72, "ZIPCODE"),
(73, 85, "MOBILE_NUMBER"),
]
}),
(
"Glen Burnie MD number 410-508-1550 Maryland 450 Columbia Boulevard 443-618-6351 21061"
, {
"entities":[
(0, 11, "CITY"),
(12, 14, "STATE"),
(22, 34, "TELEPHONE_NUMBER"),
(35, 43, "STATE_FULL"),
(44, 66, "STREET_ADDRESS"),
(67, 79, "MOBILE_NUMBER"),
(80, 85, "ZIPCODE"),
]
}),
(
"21061 number MD 443-618-6351 450 Columbia Boulevard Glen Burnie 410-508-1550 Maryland"
, {
"entities":[
(0, 5, "ZIPCODE"),
(13, 15, "STATE"),
(16, 28, "MOBILE_NUMBER"),
(29, 51, "STREET_ADDRESS"),
(52, 63, "CITY"),
(64, 76, "TELEPHONE_NUMBER"),
(77, 85, "STATE_FULL"),
]
}),
(
"410-508-1550 MD Maryland 21061 443-618-6351 Glen Burnie 450 Columbia Boulevard number"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 15, "STATE"),
(16, 24, "STATE_FULL"),
(25, 30, "ZIPCODE"),
(31, 43, "MOBILE_NUMBER"),
(44, 55, "CITY"),
(56, 78, "STREET_ADDRESS"),
]
}),
(
"Maryland number Glen Burnie 21061 MD 410-508-1550 443-618-6351 450 Columbia Boulevard"
, {
"entities":[
(0, 8, "STATE_FULL"),
(16, 27, "CITY"),
(28, 33, "ZIPCODE"),
(34, 36, "STATE"),
(37, 49, "TELEPHONE_NUMBER"),
(50, 62, "MOBILE_NUMBER"),
(63, 85, "STREET_ADDRESS"),
]
}),
(
"21061 number Maryland 450 Columbia Boulevard 443-618-6351 Glen Burnie 410-508-1550 MD"
, {
"entities":[
(0, 5, "ZIPCODE"),
(13, 21, "STATE_FULL"),
(22, 44, "STREET_ADDRESS"),
(45, 57, "MOBILE_NUMBER"),
(58, 69, "CITY"),
(70, 82, "TELEPHONE_NUMBER"),
(83, 85, "STATE"),
]
}),
(
"714-845-2383 90017 Los Angeles CA 2664 Sunny Day Drive 323-542-3993 California"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 30, "CITY"),
(31, 33, "STATE"),
(34, 54, "STREET_ADDRESS"),
(55, 67, "MOBILE_NUMBER"),
(68, 78, "STATE_FULL"),
]
}),
(
"CA Los Angeles 323-542-3993 714-845-2383 2664 Sunny Day Drive California 90017"
, {
"entities":[
(0, 2, "STATE"),
(3, 14, "CITY"),
(15, 27, "MOBILE_NUMBER"),
(28, 40, "TELEPHONE_NUMBER"),
(41, 61, "STREET_ADDRESS"),
(62, 72, "STATE_FULL"),
(73, 78, "ZIPCODE"),
]
}),
(
"California CA 90017 Los Angeles 323-542-3993 714-845-2383 2664 Sunny Day Drive"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 13, "STATE"),
(14, 19, "ZIPCODE"),
(20, 31, "CITY"),
(32, 44, "MOBILE_NUMBER"),
(45, 57, "TELEPHONE_NUMBER"),
(58, 78, "STREET_ADDRESS"),
]
}),
(
"2664 Sunny Day Drive CA Los Angeles 323-542-3993 714-845-2383 90017 California"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 23, "STATE"),
(24, 35, "CITY"),
(36, 48, "MOBILE_NUMBER"),
(49, 61, "TELEPHONE_NUMBER"),
(62, 67, "ZIPCODE"),
(68, 78, "STATE_FULL"),
]
}),
(
"2664 Sunny Day Drive CA California Los Angeles 714-845-2383 90017 323-542-3993"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 23, "STATE"),
(24, 34, "STATE_FULL"),
(35, 46, "CITY"),
(47, 59, "TELEPHONE_NUMBER"),
(60, 65, "ZIPCODE"),
(66, 78, "MOBILE_NUMBER"),
]
}),
(
"2664 Sunny Day Drive Los Angeles CA 323-542-3993 714-845-2383 California 90017"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 32, "CITY"),
(33, 35, "STATE"),
(36, 48, "MOBILE_NUMBER"),
(49, 61, "TELEPHONE_NUMBER"),
(62, 72, "STATE_FULL"),
(73, 78, "ZIPCODE"),
]
}),
(
"323-542-3993 CA 90017 714-845-2383 Los Angeles 2664 Sunny Day Drive California"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 15, "STATE"),
(16, 21, "ZIPCODE"),
(22, 34, "TELEPHONE_NUMBER"),
(35, 46, "CITY"),
(47, 67, "STREET_ADDRESS"),
(68, 78, "STATE_FULL"),
]
}),
(
"CA 90017 323-542-3993 714-845-2383 Los Angeles California 2664 Sunny Day Drive"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 21, "MOBILE_NUMBER"),
(22, 34, "TELEPHONE_NUMBER"),
(35, 46, "CITY"),
(47, 57, "STATE_FULL"),
(58, 78, "STREET_ADDRESS"),
]
}),
(
"714-845-2383 90017 2664 Sunny Day Drive California 323-542-3993 CA Los Angeles"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 39, "STREET_ADDRESS"),
(40, 50, "STATE_FULL"),
(51, 63, "MOBILE_NUMBER"),
(64, 66, "STATE"),
(67, 78, "CITY"),
]
}),
(
"90017 California 2664 Sunny Day Drive CA 323-542-3993 714-845-2383 Los Angeles"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 16, "STATE_FULL"),
(17, 37, "STREET_ADDRESS"),
(38, 40, "STATE"),
(41, 53, "MOBILE_NUMBER"),
(54, 66, "TELEPHONE_NUMBER"),
(67, 78, "CITY"),
]
}),
(
"Oklahoma Oklahoma City 4105 Ottis Street free 405-476-0219 73129 OK 405-334-2145"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 22, "CITY"),
(23, 40, "STREET_ADDRESS"),
(46, 58, "MOBILE_NUMBER"),
(59, 64, "ZIPCODE"),
(65, 67, "STATE"),
(68, 80, "TELEPHONE_NUMBER"),
]
}),
(
"free Oklahoma 73129 Oklahoma City 405-334-2145 4105 Ottis Street OK 405-476-0219"
, {
"entities":[
(5, 13, "STATE_FULL"),
(14, 19, "ZIPCODE"),
(20, 33, "CITY"),
(34, 46, "TELEPHONE_NUMBER"),
(47, 64, "STREET_ADDRESS"),
(65, 67, "STATE"),
(68, 80, "MOBILE_NUMBER"),
]
}),
(
"free Oklahoma OK 405-476-0219 405-334-2145 73129 Oklahoma City 4105 Ottis Street"
, {
"entities":[
(5, 13, "STATE_FULL"),
(14, 16, "STATE"),
(17, 29, "MOBILE_NUMBER"),
(30, 42, "TELEPHONE_NUMBER"),
(43, 48, "ZIPCODE"),
(49, 62, "CITY"),
(63, 80, "STREET_ADDRESS"),
]
}),
(
"Oklahoma City OK Oklahoma 73129 405-476-0219 free 4105 Ottis Street 405-334-2145"
, {
"entities":[
(0, 13, "CITY"),
(14, 16, "STATE"),
(17, 25, "STATE_FULL"),
(26, 31, "ZIPCODE"),
(32, 44, "MOBILE_NUMBER"),
(50, 67, "STREET_ADDRESS"),
(68, 80, "TELEPHONE_NUMBER"),
]
}),
(
"405-334-2145 405-476-0219 free Oklahoma City 73129 Oklahoma 4105 Ottis Street OK"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 25, "MOBILE_NUMBER"),
(31, 44, "CITY"),
(45, 50, "ZIPCODE"),
(51, 59, "STATE_FULL"),
(60, 77, "STREET_ADDRESS"),
(78, 80, "STATE"),
]
}),
(
"Oklahoma free 405-476-0219 405-334-2145 73129 Oklahoma City 4105 Ottis Street OK"
, {
"entities":[
(0, 8, "STATE_FULL"),
(14, 26, "MOBILE_NUMBER"),
(27, 39, "TELEPHONE_NUMBER"),
(40, 45, "ZIPCODE"),
(46, 59, "CITY"),
(60, 77, "STREET_ADDRESS"),
(78, 80, "STATE"),
]
}),
(
"73129 405-476-0219 405-334-2145 free Oklahoma 4105 Ottis Street Oklahoma City OK"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "MOBILE_NUMBER"),
(19, 31, "TELEPHONE_NUMBER"),
(37, 45, "STATE_FULL"),
(46, 63, "STREET_ADDRESS"),
(64, 77, "CITY"),
(78, 80, "STATE"),
]
}),
(
"73129 OK 405-334-2145 4105 Ottis Street Oklahoma free 405-476-0219 Oklahoma City"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 21, "TELEPHONE_NUMBER"),
(22, 39, "STREET_ADDRESS"),
(40, 48, "STATE_FULL"),
(54, 66, "MOBILE_NUMBER"),
(67, 80, "CITY"),
]
}),
(
"4105 Ottis Street 73129 free Oklahoma City OK 405-334-2145 405-476-0219 Oklahoma"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 23, "ZIPCODE"),
(29, 42, "CITY"),
(43, 45, "STATE"),
(46, 58, "TELEPHONE_NUMBER"),
(59, 71, "MOBILE_NUMBER"),
(72, 80, "STATE_FULL"),
]
}),
(
"free 4105 Ottis Street Oklahoma City OK Oklahoma 405-334-2145 405-476-0219 73129"
, {
"entities":[
(5, 22, "STREET_ADDRESS"),
(23, 36, "CITY"),
(37, 39, "STATE"),
(40, 48, "STATE_FULL"),
(49, 61, "TELEPHONE_NUMBER"),
(62, 74, "MOBILE_NUMBER"),
(75, 80, "ZIPCODE"),
]
}),
(
"Bothell Phone Washington WA 425-471-1027 474 Stockert Hollow Road 98021 425-899-5080"
, {
"entities":[
(0, 7, "CITY"),
(14, 24, "STATE_FULL"),
(25, 27, "STATE"),
(28, 40, "MOBILE_NUMBER"),
(41, 65, "STREET_ADDRESS"),
(66, 71, "ZIPCODE"),
(72, 84, "TELEPHONE_NUMBER"),
]
}),
(
"Phone 98021 425-471-1027 WA Bothell Washington 425-899-5080 474 Stockert Hollow Road"
, {
"entities":[
(6, 11, "ZIPCODE"),
(12, 24, "MOBILE_NUMBER"),
(25, 27, "STATE"),
(28, 35, "CITY"),
(36, 46, "STATE_FULL"),
(47, 59, "TELEPHONE_NUMBER"),
(60, 84, "STREET_ADDRESS"),
]
}),
(
"98021 474 Stockert Hollow Road 425-899-5080 Bothell 425-471-1027 Phone Washington WA"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 30, "STREET_ADDRESS"),
(31, 43, "TELEPHONE_NUMBER"),
(44, 51, "CITY"),
(52, 64, "MOBILE_NUMBER"),
(71, 81, "STATE_FULL"),
(82, 84, "STATE"),
]
}),
(
"425-899-5080 98021 425-471-1027 Washington Phone WA 474 Stockert Hollow Road Bothell"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 31, "MOBILE_NUMBER"),
(32, 42, "STATE_FULL"),
(49, 51, "STATE"),
(52, 76, "STREET_ADDRESS"),
(77, 84, "CITY"),
]
}),
(
"98021 Washington 474 Stockert Hollow Road Phone 425-471-1027 425-899-5080 Bothell WA"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 16, "STATE_FULL"),
(17, 41, "STREET_ADDRESS"),
(48, 60, "MOBILE_NUMBER"),
(61, 73, "TELEPHONE_NUMBER"),
(74, 81, "CITY"),
(82, 84, "STATE"),
]
}),
(
"Washington 425-471-1027 Bothell 474 Stockert Hollow Road WA 98021 Phone 425-899-5080"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 23, "MOBILE_NUMBER"),
(24, 31, "CITY"),
(32, 56, "STREET_ADDRESS"),
(57, 59, "STATE"),
(60, 65, "ZIPCODE"),
(72, 84, "TELEPHONE_NUMBER"),
]
}),
(
"425-471-1027 474 Stockert Hollow Road Bothell WA 425-899-5080 Washington 98021 Phone"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 37, "STREET_ADDRESS"),
(38, 45, "CITY"),
(46, 48, "STATE"),
(49, 61, "TELEPHONE_NUMBER"),
(62, 72, "STATE_FULL"),
(73, 78, "ZIPCODE"),
]
}),
(
"425-471-1027 98021 Phone Bothell Washington 425-899-5080 WA 474 Stockert Hollow Road"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 18, "ZIPCODE"),
(25, 32, "CITY"),
(33, 43, "STATE_FULL"),
(44, 56, "TELEPHONE_NUMBER"),
(57, 59, "STATE"),
(60, 84, "STREET_ADDRESS"),
]
}),
(
"Bothell 425-899-5080 Washington 425-471-1027 WA 98021 474 Stockert Hollow Road Phone"
, {
"entities":[
(0, 7, "CITY"),
(8, 20, "TELEPHONE_NUMBER"),
(21, 31, "STATE_FULL"),
(32, 44, "MOBILE_NUMBER"),
(45, 47, "STATE"),
(48, 53, "ZIPCODE"),
(54, 78, "STREET_ADDRESS"),
]
}),
(
"Phone 98021 WA 425-899-5080 474 Stockert Hollow Road Washington Bothell 425-471-1027"
, {
"entities":[
(6, 11, "ZIPCODE"),
(12, 14, "STATE"),
(15, 27, "TELEPHONE_NUMBER"),
(28, 52, "STREET_ADDRESS"),
(53, 63, "STATE_FULL"),
(64, 71, "CITY"),
(72, 84, "MOBILE_NUMBER"),
]
}),
(
"940-580-8085 214-263-2292 75247 Dallas TX Texas 3108 Olen Thomas Drive"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 25, "MOBILE_NUMBER"),
(26, 31, "ZIPCODE"),
(32, 38, "CITY"),
(39, 41, "STATE"),
(42, 47, "STATE_FULL"),
(48, 70, "STREET_ADDRESS"),
]
}),
(
"Dallas TX 75247 Texas 214-263-2292 940-580-8085 3108 Olen Thomas Drive"
, {
"entities":[
(0, 6, "CITY"),
(7, 9, "STATE"),
(10, 15, "ZIPCODE"),
(16, 21, "STATE_FULL"),
(22, 34, "MOBILE_NUMBER"),
(35, 47, "TELEPHONE_NUMBER"),
(48, 70, "STREET_ADDRESS"),
]
}),
(
"214-263-2292 TX 940-580-8085 75247 Texas 3108 Olen Thomas Drive Dallas"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 15, "STATE"),
(16, 28, "TELEPHONE_NUMBER"),
(29, 34, "ZIPCODE"),
(35, 40, "STATE_FULL"),
(41, 63, "STREET_ADDRESS"),
(64, 70, "CITY"),
]
}),
(
"3108 Olen Thomas Drive 214-263-2292 Texas TX 75247 940-580-8085 Dallas"
, {
"entities":[
(0, 22, "STREET_ADDRESS"),
(23, 35, "MOBILE_NUMBER"),
(36, 41, "STATE_FULL"),
(42, 44, "STATE"),
(45, 50, "ZIPCODE"),
(51, 63, "TELEPHONE_NUMBER"),
(64, 70, "CITY"),
]
}),
(
"Texas 75247 3108 Olen Thomas Drive Dallas TX 214-263-2292 940-580-8085"
, {
"entities":[
(0, 5, "STATE_FULL"),
(6, 11, "ZIPCODE"),
(12, 34, "STREET_ADDRESS"),
(35, 41, "CITY"),
(42, 44, "STATE"),
(45, 57, "MOBILE_NUMBER"),
(58, 70, "TELEPHONE_NUMBER"),
]
}),
(
"75247 TX 940-580-8085 3108 Olen Thomas Drive Dallas Texas 214-263-2292"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 21, "TELEPHONE_NUMBER"),
(22, 44, "STREET_ADDRESS"),
(45, 51, "CITY"),
(52, 57, "STATE_FULL"),
(58, 70, "MOBILE_NUMBER"),
]
}),
(
"75247 3108 Olen Thomas Drive Dallas 214-263-2292 TX Texas 940-580-8085"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 28, "STREET_ADDRESS"),
(29, 35, "CITY"),
(36, 48, "MOBILE_NUMBER"),
(49, 51, "STATE"),
(52, 57, "STATE_FULL"),
(58, 70, "TELEPHONE_NUMBER"),
]
}),
(
"940-580-8085 75247 TX Dallas 3108 Olen Thomas Drive Texas 214-263-2292"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 21, "STATE"),
(22, 28, "CITY"),
(29, 51, "STREET_ADDRESS"),
(52, 57, "STATE_FULL"),
(58, 70, "MOBILE_NUMBER"),
]
}),
(
"3108 Olen Thomas Drive Texas 214-263-2292 75247 940-580-8085 TX Dallas"
, {
"entities":[
(0, 22, "STREET_ADDRESS"),
(23, 28, "STATE_FULL"),
(29, 41, "MOBILE_NUMBER"),
(42, 47, "ZIPCODE"),
(48, 60, "TELEPHONE_NUMBER"),
(61, 63, "STATE"),
(64, 70, "CITY"),
]
}),
(
"Texas Dallas TX 214-263-2292 75247 940-580-8085 3108 Olen Thomas Drive"
, {
"entities":[
(0, 5, "STATE_FULL"),
(6, 12, "CITY"),
(13, 15, "STATE"),
(16, 28, "MOBILE_NUMBER"),
(29, 34, "ZIPCODE"),
(35, 47, "TELEPHONE_NUMBER"),
(48, 70, "STREET_ADDRESS"),
]
}),
(
"4391 Horner Street 334-206-7595 Montgomery 3--5984 AL Alabama 36104 location"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 31, "TELEPHONE_NUMBER"),
(32, 42, "CITY"),
(43, 50, "MOBILE_NUMBER"),
(51, 53, "STATE"),
(54, 61, "STATE_FULL"),
(62, 67, "ZIPCODE"),
]
}),
(
"3--5984 location 36104 334-206-7595 Alabama Montgomery 4391 Horner Street AL"
, {
"entities":[
(0, 7, "MOBILE_NUMBER"),
(17, 22, "ZIPCODE"),
(23, 35, "TELEPHONE_NUMBER"),
(36, 43, "STATE_FULL"),
(44, 54, "CITY"),
(55, 73, "STREET_ADDRESS"),
(74, 76, "STATE"),
]
}),
(
"4391 Horner Street 3--5984 Montgomery Alabama 334-206-7595 AL 36104 location"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 26, "MOBILE_NUMBER"),
(27, 37, "CITY"),
(38, 45, "STATE_FULL"),
(46, 58, "TELEPHONE_NUMBER"),
(59, 61, "STATE"),
(62, 67, "ZIPCODE"),
]
}),
(
"3--5984 4391 Horner Street location 36104 Montgomery 334-206-7595 AL Alabama"
, {
"entities":[
(0, 7, "MOBILE_NUMBER"),
(8, 26, "STREET_ADDRESS"),
(36, 41, "ZIPCODE"),
(42, 52, "CITY"),
(53, 65, "TELEPHONE_NUMBER"),
(66, 68, "STATE"),
(69, 76, "STATE_FULL"),
]
}),
(
"36104 Alabama AL location 334-206-7595 4391 Horner Street 3--5984 Montgomery"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 13, "STATE_FULL"),
(14, 16, "STATE"),
(26, 38, "TELEPHONE_NUMBER"),
(39, 57, "STREET_ADDRESS"),
(58, 65, "MOBILE_NUMBER"),
(66, 76, "CITY"),
]
}),
(
"334-206-7595 Alabama 36104 Montgomery AL 4391 Horner Street location 3--5984"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 20, "STATE_FULL"),
(21, 26, "ZIPCODE"),
(27, 37, "CITY"),
(38, 40, "STATE"),
(41, 59, "STREET_ADDRESS"),
(69, 76, "MOBILE_NUMBER"),
]
}),
(
"location 334-206-7595 AL Alabama Montgomery 36104 4391 Horner Street 3--5984"
, {
"entities":[
(9, 21, "TELEPHONE_NUMBER"),
(22, 24, "STATE"),
(25, 32, "STATE_FULL"),
(33, 43, "CITY"),
(44, 49, "ZIPCODE"),
(50, 68, "STREET_ADDRESS"),
(69, 76, "MOBILE_NUMBER"),
]
}),
(
"AL 4391 Horner Street Montgomery 36104 Alabama location 334-206-7595 3--5984"
, {
"entities":[
(0, 2, "STATE"),
(3, 21, "STREET_ADDRESS"),
(22, 32, "CITY"),
(33, 38, "ZIPCODE"),
(39, 46, "STATE_FULL"),
(56, 68, "TELEPHONE_NUMBER"),
(69, 76, "MOBILE_NUMBER"),
]
}),
(
"location 36104 Montgomery AL 4391 Horner Street 334-206-7595 Alabama 3--5984"
, {
"entities":[
(9, 14, "ZIPCODE"),
(15, 25, "CITY"),
(26, 28, "STATE"),
(29, 47, "STREET_ADDRESS"),
(48, 60, "TELEPHONE_NUMBER"),
(61, 68, "STATE_FULL"),
(69, 76, "MOBILE_NUMBER"),
]
}),
(
"36104 Alabama Montgomery 4391 Horner Street 3--5984 location 334-206-7595 AL"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 13, "STATE_FULL"),
(14, 24, "CITY"),
(25, 43, "STREET_ADDRESS"),
(44, 51, "MOBILE_NUMBER"),
(61, 73, "TELEPHONE_NUMBER"),
(74, 76, "STATE"),
]
}),
(
"OH Toledo 419-304-5875 43604 419-572-4158 Ohio Phone 1338 Stonecoal Road"
, {
"entities":[
(0, 2, "STATE"),
(3, 9, "CITY"),
(10, 22, "MOBILE_NUMBER"),
(23, 28, "ZIPCODE"),
(29, 41, "TELEPHONE_NUMBER"),
(42, 46, "STATE_FULL"),
(53, 72, "STREET_ADDRESS"),
]
}),
(
"419-304-5875 OH 419-572-4158 Phone Ohio 43604 Toledo 1338 Stonecoal Road"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 15, "STATE"),
(16, 28, "TELEPHONE_NUMBER"),
(35, 39, "STATE_FULL"),
(40, 45, "ZIPCODE"),
(46, 52, "CITY"),
(53, 72, "STREET_ADDRESS"),
]
}),
(
"419-572-4158 Phone 419-304-5875 1338 Stonecoal Road OH Toledo Ohio 43604"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(19, 31, "MOBILE_NUMBER"),
(32, 51, "STREET_ADDRESS"),
(52, 54, "STATE"),
(55, 61, "CITY"),
(62, 66, "STATE_FULL"),
(67, 72, "ZIPCODE"),
]
}),
(
"419-304-5875 Phone OH 1338 Stonecoal Road 43604 Ohio 419-572-4158 Toledo"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(19, 21, "STATE"),
(22, 41, "STREET_ADDRESS"),
(42, 47, "ZIPCODE"),
(48, 52, "STATE_FULL"),
(53, 65, "TELEPHONE_NUMBER"),
(66, 72, "CITY"),
]
}),
(
"1338 Stonecoal Road Toledo 419-572-4158 419-304-5875 Ohio 43604 OH Phone"
, {
"entities":[
(0, 19, "STREET_ADDRESS"),
(20, 26, "CITY"),
(27, 39, "TELEPHONE_NUMBER"),
(40, 52, "MOBILE_NUMBER"),
(53, 57, "STATE_FULL"),
(58, 63, "ZIPCODE"),
(64, 66, "STATE"),
]
}),
(
"419-572-4158 Phone Ohio 419-304-5875 Toledo 43604 OH 1338 Stonecoal Road"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(19, 23, "STATE_FULL"),
(24, 36, "MOBILE_NUMBER"),
(37, 43, "CITY"),
(44, 49, "ZIPCODE"),
(50, 52, "STATE"),
(53, 72, "STREET_ADDRESS"),
]
}),
(
"OH 419-572-4158 419-304-5875 Ohio Toledo 1338 Stonecoal Road 43604 Phone"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "TELEPHONE_NUMBER"),
(16, 28, "MOBILE_NUMBER"),
(29, 33, "STATE_FULL"),
(34, 40, "CITY"),
(41, 60, "STREET_ADDRESS"),
(61, 66, "ZIPCODE"),
]
}),
(
"1338 Stonecoal Road 419-304-5875 Phone Toledo Ohio OH 419-572-4158 43604"
, {
"entities":[
(0, 19, "STREET_ADDRESS"),
(20, 32, "MOBILE_NUMBER"),
(39, 45, "CITY"),
(46, 50, "STATE_FULL"),
(51, 53, "STATE"),
(54, 66, "TELEPHONE_NUMBER"),
(67, 72, "ZIPCODE"),
]
}),
(
"OH 1338 Stonecoal Road 419-572-4158 Ohio Toledo 419-304-5875 Phone 43604"
, {
"entities":[
(0, 2, "STATE"),
(3, 22, "STREET_ADDRESS"),
(23, 35, "TELEPHONE_NUMBER"),
(36, 40, "STATE_FULL"),
(41, 47, "CITY"),
(48, 60, "MOBILE_NUMBER"),
(67, 72, "ZIPCODE"),
]
}),
(
"Phone 419-572-4158 419-304-5875 43604 1338 Stonecoal Road Ohio OH Toledo"
, {
"entities":[
(6, 18, "TELEPHONE_NUMBER"),
(19, 31, "MOBILE_NUMBER"),
(32, 37, "ZIPCODE"),
(38, 57, "STREET_ADDRESS"),
(58, 62, "STATE_FULL"),
(63, 65, "STATE"),
(66, 72, "CITY"),
]
}),
(
"Los Angeles California 90017 CA 626-605-6718 3968 Nickel Road phone 213-798-0366"
, {
"entities":[
(0, 11, "CITY"),
(12, 22, "STATE_FULL"),
(23, 28, "ZIPCODE"),
(29, 31, "STATE"),
(32, 44, "TELEPHONE_NUMBER"),
(45, 61, "STREET_ADDRESS"),
(68, 80, "MOBILE_NUMBER"),
]
}),
(
"213-798-0366 phone 626-605-6718 California 90017 CA Los Angeles 3968 Nickel Road"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(19, 31, "TELEPHONE_NUMBER"),
(32, 42, "STATE_FULL"),
(43, 48, "ZIPCODE"),
(49, 51, "STATE"),
(52, 63, "CITY"),
(64, 80, "STREET_ADDRESS"),
]
}),
(
"CA 3968 Nickel Road 626-605-6718 90017 California Los Angeles 213-798-0366 phone"
, {
"entities":[
(0, 2, "STATE"),
(3, 19, "STREET_ADDRESS"),
(20, 32, "TELEPHONE_NUMBER"),
(33, 38, "ZIPCODE"),
(39, 49, "STATE_FULL"),
(50, 61, "CITY"),
(62, 74, "MOBILE_NUMBER"),
]
}),
(
"3968 Nickel Road phone California Los Angeles CA 213-798-0366 90017 626-605-6718"
, {
"entities":[
(0, 16, "STREET_ADDRESS"),
(23, 33, "STATE_FULL"),
(34, 45, "CITY"),
(46, 48, "STATE"),
(49, 61, "MOBILE_NUMBER"),
(62, 67, "ZIPCODE"),
(68, 80, "TELEPHONE_NUMBER"),
]
}),
(
"California phone 213-798-0366 626-605-6718 90017 CA 3968 Nickel Road Los Angeles"
, {
"entities":[
(0, 10, "STATE_FULL"),
(17, 29, "MOBILE_NUMBER"),
(30, 42, "TELEPHONE_NUMBER"),
(43, 48, "ZIPCODE"),
(49, 51, "STATE"),
(52, 68, "STREET_ADDRESS"),
(69, 80, "CITY"),
]
}),
(
"California Los Angeles 213-798-0366 CA phone 90017 3968 Nickel Road 626-605-6718"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 22, "CITY"),
(23, 35, "MOBILE_NUMBER"),
(36, 38, "STATE"),
(45, 50, "ZIPCODE"),
(51, 67, "STREET_ADDRESS"),
(68, 80, "TELEPHONE_NUMBER"),
]
}),
(
"phone 213-798-0366 90017 CA 3968 Nickel Road 626-605-6718 California Los Angeles"
, {
"entities":[
(6, 18, "MOBILE_NUMBER"),
(19, 24, "ZIPCODE"),
(25, 27, "STATE"),
(28, 44, "STREET_ADDRESS"),
(45, 57, "TELEPHONE_NUMBER"),
(58, 68, "STATE_FULL"),
(69, 80, "CITY"),
]
}),
(
"California CA 626-605-6718 3968 Nickel Road 213-798-0366 phone Los Angeles 90017"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 13, "STATE"),
(14, 26, "TELEPHONE_NUMBER"),
(27, 43, "STREET_ADDRESS"),
(44, 56, "MOBILE_NUMBER"),
(63, 74, "CITY"),
(75, 80, "ZIPCODE"),
]
}),
(
"phone Los Angeles California 213-798-0366 CA 626-605-6718 3968 Nickel Road 90017"
, {
"entities":[
(6, 17, "CITY"),
(18, 28, "STATE_FULL"),
(29, 41, "MOBILE_NUMBER"),
(42, 44, "STATE"),
(45, 57, "TELEPHONE_NUMBER"),
(58, 74, "STREET_ADDRESS"),
(75, 80, "ZIPCODE"),
]
}),
(
"CA 213-798-0366 3968 Nickel Road 90017 California Los Angeles 626-605-6718 phone"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "MOBILE_NUMBER"),
(16, 32, "STREET_ADDRESS"),
(33, 38, "ZIPCODE"),
(39, 49, "STATE_FULL"),
(50, 61, "CITY"),
(62, 74, "TELEPHONE_NUMBER"),
]
}),
]
