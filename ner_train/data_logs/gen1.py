TRAINING_DATA2 = [
(
"361-645-1378 214-202-6951 77963 TX Goliad Texas 3551 White Avenue"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 25, "MOBILE_NUMBER"),
(26, 31, "ZIPCODE"),
(32, 34, "STATE"),
(35, 41, "CITY"),
(42, 47, "STATE_FULL"),
(48, 65, "STREET_ADDRESS"),
]
}),
(
"TX 361-645-1378 214-202-6951 Goliad Texas 77963 3551 White Avenue"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "TELEPHONE_NUMBER"),
(16, 28, "MOBILE_NUMBER"),
(29, 35, "CITY"),
(36, 41, "STATE_FULL"),
(42, 47, "ZIPCODE"),
(48, 65, "STREET_ADDRESS"),
]
}),
(
"77963 361-645-1378 Texas Goliad 3551 White Avenue 214-202-6951 TX"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "TELEPHONE_NUMBER"),
(19, 24, "STATE_FULL"),
(25, 31, "CITY"),
(32, 49, "STREET_ADDRESS"),
(50, 62, "MOBILE_NUMBER"),
(63, 65, "STATE"),
]
}),
(
"Goliad 3551 White Avenue 214-202-6951 77963 Texas 361-645-1378 TX"
, {
"entities":[
(0, 6, "CITY"),
(7, 24, "STREET_ADDRESS"),
(25, 37, "MOBILE_NUMBER"),
(38, 43, "ZIPCODE"),
(44, 49, "STATE_FULL"),
(50, 62, "TELEPHONE_NUMBER"),
(63, 65, "STATE"),
]
}),
(
"TX Texas Goliad 214-202-6951 77963 3551 White Avenue 361-645-1378"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "STATE_FULL"),
(9, 15, "CITY"),
(16, 28, "MOBILE_NUMBER"),
(29, 34, "ZIPCODE"),
(35, 52, "STREET_ADDRESS"),
(53, 65, "TELEPHONE_NUMBER"),
]
}),
(
"361-645-1378 214-202-6951 Goliad 3551 White Avenue Texas TX 77963"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 25, "MOBILE_NUMBER"),
(26, 32, "CITY"),
(33, 50, "STREET_ADDRESS"),
(51, 56, "STATE_FULL"),
(57, 59, "STATE"),
(60, 65, "ZIPCODE"),
]
}),
(
"77963 Goliad TX Texas 214-202-6951 3551 White Avenue 361-645-1378"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 12, "CITY"),
(13, 15, "STATE"),
(16, 21, "STATE_FULL"),
(22, 34, "MOBILE_NUMBER"),
(35, 52, "STREET_ADDRESS"),
(53, 65, "TELEPHONE_NUMBER"),
]
}),
(
"77963 214-202-6951 TX Goliad Texas 3551 White Avenue 361-645-1378"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "MOBILE_NUMBER"),
(19, 21, "STATE"),
(22, 28, "CITY"),
(29, 34, "STATE_FULL"),
(35, 52, "STREET_ADDRESS"),
(53, 65, "TELEPHONE_NUMBER"),
]
}),
(
"214-202-6951 TX Texas 77963 361-645-1378 Goliad 3551 White Avenue"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 15, "STATE"),
(16, 21, "STATE_FULL"),
(22, 27, "ZIPCODE"),
(28, 40, "TELEPHONE_NUMBER"),
(41, 47, "CITY"),
(48, 65, "STREET_ADDRESS"),
]
}),
(
"TX 361-645-1378 77963 Texas 214-202-6951 3551 White Avenue Goliad"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "TELEPHONE_NUMBER"),
(16, 21, "ZIPCODE"),
(22, 27, "STATE_FULL"),
(28, 40, "MOBILE_NUMBER"),
(41, 58, "STREET_ADDRESS"),
(59, 65, "CITY"),
]
}),
(
"Monroe LA Louisiana 2721 Norma Lane 318-488-2527 318-331-7187 71201"
, {
"entities":[
(0, 6, "CITY"),
(7, 9, "STATE"),
(10, 19, "STATE_FULL"),
(20, 35, "STREET_ADDRESS"),
(36, 48, "TELEPHONE_NUMBER"),
(49, 61, "MOBILE_NUMBER"),
(62, 67, "ZIPCODE"),
]
}),
(
"Louisiana 318-488-2527 LA 71201 318-331-7187 2721 Norma Lane Monroe"
, {
"entities":[
(0, 9, "STATE_FULL"),
(10, 22, "TELEPHONE_NUMBER"),
(23, 25, "STATE"),
(26, 31, "ZIPCODE"),
(32, 44, "MOBILE_NUMBER"),
(45, 60, "STREET_ADDRESS"),
(61, 67, "CITY"),
]
}),
(
"Louisiana 71201 318-488-2527 Monroe LA 318-331-7187 2721 Norma Lane"
, {
"entities":[
(0, 9, "STATE_FULL"),
(10, 15, "ZIPCODE"),
(16, 28, "TELEPHONE_NUMBER"),
(29, 35, "CITY"),
(36, 38, "STATE"),
(39, 51, "MOBILE_NUMBER"),
(52, 67, "STREET_ADDRESS"),
]
}),
(
"Louisiana 318-331-7187 LA 2721 Norma Lane 318-488-2527 71201 Monroe"
, {
"entities":[
(0, 9, "STATE_FULL"),
(10, 22, "MOBILE_NUMBER"),
(23, 25, "STATE"),
(26, 41, "STREET_ADDRESS"),
(42, 54, "TELEPHONE_NUMBER"),
(55, 60, "ZIPCODE"),
(61, 67, "CITY"),
]
}),
(
"Louisiana LA 318-331-7187 2721 Norma Lane 71201 318-488-2527 Monroe"
, {
"entities":[
(0, 9, "STATE_FULL"),
(10, 12, "STATE"),
(13, 25, "MOBILE_NUMBER"),
(26, 41, "STREET_ADDRESS"),
(42, 47, "ZIPCODE"),
(48, 60, "TELEPHONE_NUMBER"),
(61, 67, "CITY"),
]
}),
(
"LA 2721 Norma Lane 318-331-7187 Monroe 71201 318-488-2527 Louisiana"
, {
"entities":[
(0, 2, "STATE"),
(3, 18, "STREET_ADDRESS"),
(19, 31, "MOBILE_NUMBER"),
(32, 38, "CITY"),
(39, 44, "ZIPCODE"),
(45, 57, "TELEPHONE_NUMBER"),
(58, 67, "STATE_FULL"),
]
}),
(
"318-331-7187 71201 Louisiana Monroe 2721 Norma Lane 318-488-2527 LA"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 28, "STATE_FULL"),
(29, 35, "CITY"),
(36, 51, "STREET_ADDRESS"),
(52, 64, "TELEPHONE_NUMBER"),
(65, 67, "STATE"),
]
}),
(
"318-331-7187 LA 318-488-2527 Louisiana 71201 Monroe 2721 Norma Lane"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 15, "STATE"),
(16, 28, "TELEPHONE_NUMBER"),
(29, 38, "STATE_FULL"),
(39, 44, "ZIPCODE"),
(45, 51, "CITY"),
(52, 67, "STREET_ADDRESS"),
]
}),
(
"Monroe 71201 318-488-2527 2721 Norma Lane Louisiana 318-331-7187 LA"
, {
"entities":[
(0, 6, "CITY"),
(7, 12, "ZIPCODE"),
(13, 25, "TELEPHONE_NUMBER"),
(26, 41, "STREET_ADDRESS"),
(42, 51, "STATE_FULL"),
(52, 64, "MOBILE_NUMBER"),
(65, 67, "STATE"),
]
}),
(
"318-331-7187 71201 2721 Norma Lane 318-488-2527 Louisiana LA Monroe"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 34, "STREET_ADDRESS"),
(35, 47, "TELEPHONE_NUMBER"),
(48, 57, "STATE_FULL"),
(58, 60, "STATE"),
(61, 67, "CITY"),
]
}),
(
"308-425-0717 308-470-6085 Franklin 995 Kyle Street 68939 Nebraska NE"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 25, "MOBILE_NUMBER"),
(26, 34, "CITY"),
(35, 50, "STREET_ADDRESS"),
(51, 56, "ZIPCODE"),
(57, 65, "STATE_FULL"),
(66, 68, "STATE"),
]
}),
(
"308-425-0717 Nebraska 308-470-6085 995 Kyle Street 68939 NE Franklin"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 21, "STATE_FULL"),
(22, 34, "MOBILE_NUMBER"),
(35, 50, "STREET_ADDRESS"),
(51, 56, "ZIPCODE"),
(57, 59, "STATE"),
(60, 68, "CITY"),
]
}),
(
"Franklin 68939 Nebraska NE 308-470-6085 308-425-0717 995 Kyle Street"
, {
"entities":[
(0, 8, "CITY"),
(9, 14, "ZIPCODE"),
(15, 23, "STATE_FULL"),
(24, 26, "STATE"),
(27, 39, "MOBILE_NUMBER"),
(40, 52, "TELEPHONE_NUMBER"),
(53, 68, "STREET_ADDRESS"),
]
}),
(
"Nebraska 308-425-0717 Franklin NE 308-470-6085 995 Kyle Street 68939"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 21, "TELEPHONE_NUMBER"),
(22, 30, "CITY"),
(31, 33, "STATE"),
(34, 46, "MOBILE_NUMBER"),
(47, 62, "STREET_ADDRESS"),
(63, 68, "ZIPCODE"),
]
}),
(
"995 Kyle Street Franklin 68939 NE 308-470-6085 Nebraska 308-425-0717"
, {
"entities":[
(0, 15, "STREET_ADDRESS"),
(16, 24, "CITY"),
(25, 30, "ZIPCODE"),
(31, 33, "STATE"),
(34, 46, "MOBILE_NUMBER"),
(47, 55, "STATE_FULL"),
(56, 68, "TELEPHONE_NUMBER"),
]
}),
(
"Franklin 995 Kyle Street Nebraska 308-425-0717 68939 NE 308-470-6085"
, {
"entities":[
(0, 8, "CITY"),
(9, 24, "STREET_ADDRESS"),
(25, 33, "STATE_FULL"),
(34, 46, "TELEPHONE_NUMBER"),
(47, 52, "ZIPCODE"),
(53, 55, "STATE"),
(56, 68, "MOBILE_NUMBER"),
]
}),
(
"308-425-0717 Franklin 995 Kyle Street 308-470-6085 68939 Nebraska NE"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 21, "CITY"),
(22, 37, "STREET_ADDRESS"),
(38, 50, "MOBILE_NUMBER"),
(51, 56, "ZIPCODE"),
(57, 65, "STATE_FULL"),
(66, 68, "STATE"),
]
}),
(
"995 Kyle Street NE Franklin Nebraska 308-425-0717 68939 308-470-6085"
, {
"entities":[
(0, 15, "STREET_ADDRESS"),
(16, 18, "STATE"),
(19, 27, "CITY"),
(28, 36, "STATE_FULL"),
(37, 49, "TELEPHONE_NUMBER"),
(50, 55, "ZIPCODE"),
(56, 68, "MOBILE_NUMBER"),
]
}),
(
"308-425-0717 Franklin 68939 995 Kyle Street NE 308-470-6085 Nebraska"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 21, "CITY"),
(22, 27, "ZIPCODE"),
(28, 43, "STREET_ADDRESS"),
(44, 46, "STATE"),
(47, 59, "MOBILE_NUMBER"),
(60, 68, "STATE_FULL"),
]
}),
(
"Nebraska Franklin 308-425-0717 308-470-6085 68939 NE 995 Kyle Street"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 17, "CITY"),
(18, 30, "TELEPHONE_NUMBER"),
(31, 43, "MOBILE_NUMBER"),
(44, 49, "ZIPCODE"),
(50, 52, "STATE"),
(53, 68, "STREET_ADDRESS"),
]
}),
(
"774-245-5698 4198 Huntz Lane Massachusetts MA Marlboro 01752 978-570-0889"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 28, "STREET_ADDRESS"),
(29, 42, "STATE_FULL"),
(43, 45, "STATE"),
(46, 54, "CITY"),
(55, 60, "ZIPCODE"),
(61, 73, "TELEPHONE_NUMBER"),
]
}),
(
"MA 01752 Massachusetts Marlboro 978-570-0889 774-245-5698 4198 Huntz Lane"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 22, "STATE_FULL"),
(23, 31, "CITY"),
(32, 44, "TELEPHONE_NUMBER"),
(45, 57, "MOBILE_NUMBER"),
(58, 73, "STREET_ADDRESS"),
]
}),
(
"978-570-0889 Massachusetts Marlboro MA 01752 4198 Huntz Lane 774-245-5698"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 26, "STATE_FULL"),
(27, 35, "CITY"),
(36, 38, "STATE"),
(39, 44, "ZIPCODE"),
(45, 60, "STREET_ADDRESS"),
(61, 73, "MOBILE_NUMBER"),
]
}),
(
"4198 Huntz Lane Massachusetts 01752 MA 978-570-0889 774-245-5698 Marlboro"
, {
"entities":[
(0, 15, "STREET_ADDRESS"),
(16, 29, "STATE_FULL"),
(30, 35, "ZIPCODE"),
(36, 38, "STATE"),
(39, 51, "TELEPHONE_NUMBER"),
(52, 64, "MOBILE_NUMBER"),
(65, 73, "CITY"),
]
}),
(
"Marlboro MA Massachusetts 978-570-0889 774-245-5698 01752 4198 Huntz Lane"
, {
"entities":[
(0, 8, "CITY"),
(9, 11, "STATE"),
(12, 25, "STATE_FULL"),
(26, 38, "TELEPHONE_NUMBER"),
(39, 51, "MOBILE_NUMBER"),
(52, 57, "ZIPCODE"),
(58, 73, "STREET_ADDRESS"),
]
}),
(
"978-570-0889 774-245-5698 Massachusetts 01752 4198 Huntz Lane MA Marlboro"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 25, "MOBILE_NUMBER"),
(26, 39, "STATE_FULL"),
(40, 45, "ZIPCODE"),
(46, 61, "STREET_ADDRESS"),
(62, 64, "STATE"),
(65, 73, "CITY"),
]
}),
(
"4198 Huntz Lane MA Marlboro 01752 Massachusetts 774-245-5698 978-570-0889"
, {
"entities":[
(0, 15, "STREET_ADDRESS"),
(16, 18, "STATE"),
(19, 27, "CITY"),
(28, 33, "ZIPCODE"),
(34, 47, "STATE_FULL"),
(48, 60, "MOBILE_NUMBER"),
(61, 73, "TELEPHONE_NUMBER"),
]
}),
(
"774-245-5698 Marlboro 978-570-0889 Massachusetts 4198 Huntz Lane 01752 MA"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 21, "CITY"),
(22, 34, "TELEPHONE_NUMBER"),
(35, 48, "STATE_FULL"),
(49, 64, "STREET_ADDRESS"),
(65, 70, "ZIPCODE"),
(71, 73, "STATE"),
]
}),
(
"774-245-5698 Massachusetts Marlboro 4198 Huntz Lane 01752 978-570-0889 MA"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 26, "STATE_FULL"),
(27, 35, "CITY"),
(36, 51, "STREET_ADDRESS"),
(52, 57, "ZIPCODE"),
(58, 70, "TELEPHONE_NUMBER"),
(71, 73, "STATE"),
]
}),
(
"978-570-0889 Massachusetts 01752 Marlboro MA 774-245-5698 4198 Huntz Lane"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 26, "STATE_FULL"),
(27, 32, "ZIPCODE"),
(33, 41, "CITY"),
(42, 44, "STATE"),
(45, 57, "MOBILE_NUMBER"),
(58, 73, "STREET_ADDRESS"),
]
}),
(
"32810 FL Florida Orlando 4478 Barnes Street 407-287-3751 407-256-1051"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 16, "STATE_FULL"),
(17, 24, "CITY"),
(25, 43, "STREET_ADDRESS"),
(44, 56, "TELEPHONE_NUMBER"),
(57, 69, "MOBILE_NUMBER"),
]
}),
(
"32810 FL 4478 Barnes Street 407-287-3751 407-256-1051 Florida Orlando"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 27, "STREET_ADDRESS"),
(28, 40, "TELEPHONE_NUMBER"),
(41, 53, "MOBILE_NUMBER"),
(54, 61, "STATE_FULL"),
(62, 69, "CITY"),
]
}),
(
"Florida Orlando 407-287-3751 4478 Barnes Street 407-256-1051 FL 32810"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 15, "CITY"),
(16, 28, "TELEPHONE_NUMBER"),
(29, 47, "STREET_ADDRESS"),
(48, 60, "MOBILE_NUMBER"),
(61, 63, "STATE"),
(64, 69, "ZIPCODE"),
]
}),
(
"Orlando 4478 Barnes Street FL Florida 407-287-3751 407-256-1051 32810"
, {
"entities":[
(0, 7, "CITY"),
(8, 26, "STREET_ADDRESS"),
(27, 29, "STATE"),
(30, 37, "STATE_FULL"),
(38, 50, "TELEPHONE_NUMBER"),
(51, 63, "MOBILE_NUMBER"),
(64, 69, "ZIPCODE"),
]
}),
(
"4478 Barnes Street 407-256-1051 FL Florida 407-287-3751 32810 Orlando"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 31, "MOBILE_NUMBER"),
(32, 34, "STATE"),
(35, 42, "STATE_FULL"),
(43, 55, "TELEPHONE_NUMBER"),
(56, 61, "ZIPCODE"),
(62, 69, "CITY"),
]
}),
(
"32810 Orlando FL Florida 407-256-1051 407-287-3751 4478 Barnes Street"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 13, "CITY"),
(14, 16, "STATE"),
(17, 24, "STATE_FULL"),
(25, 37, "MOBILE_NUMBER"),
(38, 50, "TELEPHONE_NUMBER"),
(51, 69, "STREET_ADDRESS"),
]
}),
(
"407-287-3751 Orlando 407-256-1051 32810 FL Florida 4478 Barnes Street"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 20, "CITY"),
(21, 33, "MOBILE_NUMBER"),
(34, 39, "ZIPCODE"),
(40, 42, "STATE"),
(43, 50, "STATE_FULL"),
(51, 69, "STREET_ADDRESS"),
]
}),
(
"Orlando 4478 Barnes Street 407-287-3751 32810 407-256-1051 FL Florida"
, {
"entities":[
(0, 7, "CITY"),
(8, 26, "STREET_ADDRESS"),
(27, 39, "TELEPHONE_NUMBER"),
(40, 45, "ZIPCODE"),
(46, 58, "MOBILE_NUMBER"),
(59, 61, "STATE"),
(62, 69, "STATE_FULL"),
]
}),
(
"FL 32810 407-256-1051 4478 Barnes Street Orlando 407-287-3751 Florida"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 21, "MOBILE_NUMBER"),
(22, 40, "STREET_ADDRESS"),
(41, 48, "CITY"),
(49, 61, "TELEPHONE_NUMBER"),
(62, 69, "STATE_FULL"),
]
}),
(
"32810 407-256-1051 Orlando 4478 Barnes Street Florida FL 407-287-3751"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "MOBILE_NUMBER"),
(19, 26, "CITY"),
(27, 45, "STREET_ADDRESS"),
(46, 53, "STATE_FULL"),
(54, 56, "STATE"),
(57, 69, "TELEPHONE_NUMBER"),
]
}),
(
"64747 MO 660-349-7819 Missouri 816-862-5323 3475 Big Elm Garden City"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 21, "MOBILE_NUMBER"),
(22, 30, "STATE_FULL"),
(31, 43, "TELEPHONE_NUMBER"),
(44, 56, "STREET_ADDRESS"),
(57, 68, "CITY"),
]
}),
(
"3475 Big Elm Missouri 816-862-5323 64747 MO 660-349-7819 Garden City"
, {
"entities":[
(0, 12, "STREET_ADDRESS"),
(13, 21, "STATE_FULL"),
(22, 34, "TELEPHONE_NUMBER"),
(35, 40, "ZIPCODE"),
(41, 43, "STATE"),
(44, 56, "MOBILE_NUMBER"),
(57, 68, "CITY"),
]
}),
(
"816-862-5323 Missouri Garden City 64747 MO 660-349-7819 3475 Big Elm"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 21, "STATE_FULL"),
(22, 33, "CITY"),
(34, 39, "ZIPCODE"),
(40, 42, "STATE"),
(43, 55, "MOBILE_NUMBER"),
(56, 68, "STREET_ADDRESS"),
]
}),
(
"64747 660-349-7819 3475 Big Elm MO Missouri Garden City 816-862-5323"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "MOBILE_NUMBER"),
(19, 31, "STREET_ADDRESS"),
(32, 34, "STATE"),
(35, 43, "STATE_FULL"),
(44, 55, "CITY"),
(56, 68, "TELEPHONE_NUMBER"),
]
}),
(
"660-349-7819 64747 3475 Big Elm Missouri MO 816-862-5323 Garden City"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 31, "STREET_ADDRESS"),
(32, 40, "STATE_FULL"),
(41, 43, "STATE"),
(44, 56, "TELEPHONE_NUMBER"),
(57, 68, "CITY"),
]
}),
(
"64747 Garden City 816-862-5323 660-349-7819 MO Missouri 3475 Big Elm"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 17, "CITY"),
(18, 30, "TELEPHONE_NUMBER"),
(31, 43, "MOBILE_NUMBER"),
(44, 46, "STATE"),
(47, 55, "STATE_FULL"),
(56, 68, "STREET_ADDRESS"),
]
}),
(
"MO 660-349-7819 Garden City 64747 Missouri 3475 Big Elm 816-862-5323"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "MOBILE_NUMBER"),
(16, 27, "CITY"),
(28, 33, "ZIPCODE"),
(34, 42, "STATE_FULL"),
(43, 55, "STREET_ADDRESS"),
(56, 68, "TELEPHONE_NUMBER"),
]
}),
(
"3475 Big Elm Missouri 64747 Garden City MO 660-349-7819 816-862-5323"
, {
"entities":[
(0, 12, "STREET_ADDRESS"),
(13, 21, "STATE_FULL"),
(22, 27, "ZIPCODE"),
(28, 39, "CITY"),
(40, 42, "STATE"),
(43, 55, "MOBILE_NUMBER"),
(56, 68, "TELEPHONE_NUMBER"),
]
}),
(
"816-862-5323 Garden City Missouri 660-349-7819 MO 3475 Big Elm 64747"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 24, "CITY"),
(25, 33, "STATE_FULL"),
(34, 46, "MOBILE_NUMBER"),
(47, 49, "STATE"),
(50, 62, "STREET_ADDRESS"),
(63, 68, "ZIPCODE"),
]
}),
(
"Garden City 64747 Missouri 660-349-7819 3475 Big Elm MO 816-862-5323"
, {
"entities":[
(0, 11, "CITY"),
(12, 17, "ZIPCODE"),
(18, 26, "STATE_FULL"),
(27, 39, "MOBILE_NUMBER"),
(40, 52, "STREET_ADDRESS"),
(53, 55, "STATE"),
(56, 68, "TELEPHONE_NUMBER"),
]
}),
(
"Indiana 4495 Barfield Lane 317-552-1216 46254 IN 317-294-1675 Indianapolis"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 26, "STREET_ADDRESS"),
(27, 39, "TELEPHONE_NUMBER"),
(40, 45, "ZIPCODE"),
(46, 48, "STATE"),
(49, 61, "MOBILE_NUMBER"),
(62, 74, "CITY"),
]
}),
(
"Indiana Indianapolis IN 317-552-1216 317-294-1675 46254 4495 Barfield Lane"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 20, "CITY"),
(21, 23, "STATE"),
(24, 36, "TELEPHONE_NUMBER"),
(37, 49, "MOBILE_NUMBER"),
(50, 55, "ZIPCODE"),
(56, 74, "STREET_ADDRESS"),
]
}),
(
"IN 317-294-1675 4495 Barfield Lane 317-552-1216 46254 Indiana Indianapolis"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "MOBILE_NUMBER"),
(16, 34, "STREET_ADDRESS"),
(35, 47, "TELEPHONE_NUMBER"),
(48, 53, "ZIPCODE"),
(54, 61, "STATE_FULL"),
(62, 74, "CITY"),
]
}),
(
"Indiana IN 4495 Barfield Lane 46254 317-294-1675 Indianapolis 317-552-1216"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 10, "STATE"),
(11, 29, "STREET_ADDRESS"),
(30, 35, "ZIPCODE"),
(36, 48, "MOBILE_NUMBER"),
(49, 61, "CITY"),
(62, 74, "TELEPHONE_NUMBER"),
]
}),
(
"317-294-1675 Indiana 4495 Barfield Lane IN 46254 317-552-1216 Indianapolis"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 20, "STATE_FULL"),
(21, 39, "STREET_ADDRESS"),
(40, 42, "STATE"),
(43, 48, "ZIPCODE"),
(49, 61, "TELEPHONE_NUMBER"),
(62, 74, "CITY"),
]
}),
(
"IN 317-294-1675 317-552-1216 Indiana 46254 Indianapolis 4495 Barfield Lane"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "MOBILE_NUMBER"),
(16, 28, "TELEPHONE_NUMBER"),
(29, 36, "STATE_FULL"),
(37, 42, "ZIPCODE"),
(43, 55, "CITY"),
(56, 74, "STREET_ADDRESS"),
]
}),
(
"46254 IN 317-552-1216 Indianapolis 4495 Barfield Lane 317-294-1675 Indiana"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 21, "TELEPHONE_NUMBER"),
(22, 34, "CITY"),
(35, 53, "STREET_ADDRESS"),
(54, 66, "MOBILE_NUMBER"),
(67, 74, "STATE_FULL"),
]
}),
(
"IN 4495 Barfield Lane 317-552-1216 317-294-1675 46254 Indiana Indianapolis"
, {
"entities":[
(0, 2, "STATE"),
(3, 21, "STREET_ADDRESS"),
(22, 34, "TELEPHONE_NUMBER"),
(35, 47, "MOBILE_NUMBER"),
(48, 53, "ZIPCODE"),
(54, 61, "STATE_FULL"),
(62, 74, "CITY"),
]
}),
(
"IN 317-294-1675 317-552-1216 Indianapolis Indiana 4495 Barfield Lane 46254"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "MOBILE_NUMBER"),
(16, 28, "TELEPHONE_NUMBER"),
(29, 41, "CITY"),
(42, 49, "STATE_FULL"),
(50, 68, "STREET_ADDRESS"),
(69, 74, "ZIPCODE"),
]
}),
(
"Indianapolis IN 317-294-1675 317-552-1216 46254 Indiana 4495 Barfield Lane"
, {
"entities":[
(0, 12, "CITY"),
(13, 15, "STATE"),
(16, 28, "MOBILE_NUMBER"),
(29, 41, "TELEPHONE_NUMBER"),
(42, 47, "ZIPCODE"),
(48, 55, "STATE_FULL"),
(56, 74, "STREET_ADDRESS"),
]
}),
(
"308-390-8879 4499 Kyle Street Nebraska NE 68803 Grand Island 308-391-5955"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 29, "STREET_ADDRESS"),
(30, 38, "STATE_FULL"),
(39, 41, "STATE"),
(42, 47, "ZIPCODE"),
(48, 60, "CITY"),
(61, 73, "TELEPHONE_NUMBER"),
]
}),
(
"NE 4499 Kyle Street Nebraska Grand Island 308-391-5955 308-390-8879 68803"
, {
"entities":[
(0, 2, "STATE"),
(3, 19, "STREET_ADDRESS"),
(20, 28, "STATE_FULL"),
(29, 41, "CITY"),
(42, 54, "TELEPHONE_NUMBER"),
(55, 67, "MOBILE_NUMBER"),
(68, 73, "ZIPCODE"),
]
}),
(
"4499 Kyle Street Nebraska 308-390-8879 Grand Island 68803 308-391-5955 NE"
, {
"entities":[
(0, 16, "STREET_ADDRESS"),
(17, 25, "STATE_FULL"),
(26, 38, "MOBILE_NUMBER"),
(39, 51, "CITY"),
(52, 57, "ZIPCODE"),
(58, 70, "TELEPHONE_NUMBER"),
(71, 73, "STATE"),
]
}),
(
"308-391-5955 Grand Island 4499 Kyle Street 68803 NE Nebraska 308-390-8879"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 25, "CITY"),
(26, 42, "STREET_ADDRESS"),
(43, 48, "ZIPCODE"),
(49, 51, "STATE"),
(52, 60, "STATE_FULL"),
(61, 73, "MOBILE_NUMBER"),
]
}),
(
"Nebraska 308-390-8879 Grand Island 68803 4499 Kyle Street NE 308-391-5955"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 21, "MOBILE_NUMBER"),
(22, 34, "CITY"),
(35, 40, "ZIPCODE"),
(41, 57, "STREET_ADDRESS"),
(58, 60, "STATE"),
(61, 73, "TELEPHONE_NUMBER"),
]
}),
(
"NE Nebraska 68803 4499 Kyle Street Grand Island 308-390-8879 308-391-5955"
, {
"entities":[
(0, 2, "STATE"),
(3, 11, "STATE_FULL"),
(12, 17, "ZIPCODE"),
(18, 34, "STREET_ADDRESS"),
(35, 47, "CITY"),
(48, 60, "MOBILE_NUMBER"),
(61, 73, "TELEPHONE_NUMBER"),
]
}),
(
"Grand Island NE 68803 308-390-8879 Nebraska 308-391-5955 4499 Kyle Street"
, {
"entities":[
(0, 12, "CITY"),
(13, 15, "STATE"),
(16, 21, "ZIPCODE"),
(22, 34, "MOBILE_NUMBER"),
(35, 43, "STATE_FULL"),
(44, 56, "TELEPHONE_NUMBER"),
(57, 73, "STREET_ADDRESS"),
]
}),
(
"308-390-8879 NE 308-391-5955 4499 Kyle Street Nebraska 68803 Grand Island"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 15, "STATE"),
(16, 28, "TELEPHONE_NUMBER"),
(29, 45, "STREET_ADDRESS"),
(46, 54, "STATE_FULL"),
(55, 60, "ZIPCODE"),
(61, 73, "CITY"),
]
}),
(
"308-390-8879 4499 Kyle Street Grand Island NE Nebraska 68803 308-391-5955"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 29, "STREET_ADDRESS"),
(30, 42, "CITY"),
(43, 45, "STATE"),
(46, 54, "STATE_FULL"),
(55, 60, "ZIPCODE"),
(61, 73, "TELEPHONE_NUMBER"),
]
}),
(
"308-391-5955 308-390-8879 4499 Kyle Street Grand Island 68803 NE Nebraska"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 25, "MOBILE_NUMBER"),
(26, 42, "STREET_ADDRESS"),
(43, 55, "CITY"),
(56, 61, "ZIPCODE"),
(62, 64, "STATE"),
(65, 73, "STATE_FULL"),
]
}),
(
"918-513-8561 2150 Philli Lane Tulsa 918-607-6167 OK Oklahoma 74103"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 29, "STREET_ADDRESS"),
(30, 35, "CITY"),
(36, 48, "MOBILE_NUMBER"),
(49, 51, "STATE"),
(52, 60, "STATE_FULL"),
(61, 66, "ZIPCODE"),
]
}),
(
"918-513-8561 74103 Oklahoma OK 918-607-6167 Tulsa 2150 Philli Lane"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 27, "STATE_FULL"),
(28, 30, "STATE"),
(31, 43, "MOBILE_NUMBER"),
(44, 49, "CITY"),
(50, 66, "STREET_ADDRESS"),
]
}),
(
"918-513-8561 2150 Philli Lane Tulsa OK 74103 918-607-6167 Oklahoma"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 29, "STREET_ADDRESS"),
(30, 35, "CITY"),
(36, 38, "STATE"),
(39, 44, "ZIPCODE"),
(45, 57, "MOBILE_NUMBER"),
(58, 66, "STATE_FULL"),
]
}),
(
"Tulsa 918-513-8561 918-607-6167 Oklahoma 74103 OK 2150 Philli Lane"
, {
"entities":[
(0, 5, "CITY"),
(6, 18, "TELEPHONE_NUMBER"),
(19, 31, "MOBILE_NUMBER"),
(32, 40, "STATE_FULL"),
(41, 46, "ZIPCODE"),
(47, 49, "STATE"),
(50, 66, "STREET_ADDRESS"),
]
}),
(
"Tulsa Oklahoma 918-513-8561 74103 2150 Philli Lane OK 918-607-6167"
, {
"entities":[
(0, 5, "CITY"),
(6, 14, "STATE_FULL"),
(15, 27, "TELEPHONE_NUMBER"),
(28, 33, "ZIPCODE"),
(34, 50, "STREET_ADDRESS"),
(51, 53, "STATE"),
(54, 66, "MOBILE_NUMBER"),
]
}),
(
"2150 Philli Lane 74103 918-513-8561 Tulsa Oklahoma OK 918-607-6167"
, {
"entities":[
(0, 16, "STREET_ADDRESS"),
(17, 22, "ZIPCODE"),
(23, 35, "TELEPHONE_NUMBER"),
(36, 41, "CITY"),
(42, 50, "STATE_FULL"),
(51, 53, "STATE"),
(54, 66, "MOBILE_NUMBER"),
]
}),
(
"2150 Philli Lane 918-513-8561 OK 74103 Oklahoma Tulsa 918-607-6167"
, {
"entities":[
(0, 16, "STREET_ADDRESS"),
(17, 29, "TELEPHONE_NUMBER"),
(30, 32, "STATE"),
(33, 38, "ZIPCODE"),
(39, 47, "STATE_FULL"),
(48, 53, "CITY"),
(54, 66, "MOBILE_NUMBER"),
]
}),
(
"918-513-8561 OK 918-607-6167 74103 Oklahoma 2150 Philli Lane Tulsa"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 15, "STATE"),
(16, 28, "MOBILE_NUMBER"),
(29, 34, "ZIPCODE"),
(35, 43, "STATE_FULL"),
(44, 60, "STREET_ADDRESS"),
(61, 66, "CITY"),
]
}),
(
"Oklahoma 918-607-6167 2150 Philli Lane 918-513-8561 74103 Tulsa OK"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 21, "MOBILE_NUMBER"),
(22, 38, "STREET_ADDRESS"),
(39, 51, "TELEPHONE_NUMBER"),
(52, 57, "ZIPCODE"),
(58, 63, "CITY"),
(64, 66, "STATE"),
]
}),
(
"918-513-8561 918-607-6167 OK 74103 Tulsa Oklahoma 2150 Philli Lane"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 25, "MOBILE_NUMBER"),
(26, 28, "STATE"),
(29, 34, "ZIPCODE"),
(35, 40, "CITY"),
(41, 49, "STATE_FULL"),
(50, 66, "STREET_ADDRESS"),
]
}),
(
"2343 Courtright Street 701-491-7220 Fargo North Dakota 701-361-2883 58102 ND"
, {
"entities":[
(0, 22, "STREET_ADDRESS"),
(23, 35, "TELEPHONE_NUMBER"),
(36, 41, "CITY"),
(42, 54, "STATE_FULL"),
(55, 67, "MOBILE_NUMBER"),
(68, 73, "ZIPCODE"),
(74, 76, "STATE"),
]
}),
(
"701-361-2883 2343 Courtright Street 58102 North Dakota ND 701-491-7220 Fargo"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 35, "STREET_ADDRESS"),
(36, 41, "ZIPCODE"),
(42, 54, "STATE_FULL"),
(55, 57, "STATE"),
(58, 70, "TELEPHONE_NUMBER"),
(71, 76, "CITY"),
]
}),
(
"North Dakota ND 58102 Fargo 701-361-2883 701-491-7220 2343 Courtright Street"
, {
"entities":[
(0, 12, "STATE_FULL"),
(13, 15, "STATE"),
(16, 21, "ZIPCODE"),
(22, 27, "CITY"),
(28, 40, "MOBILE_NUMBER"),
(41, 53, "TELEPHONE_NUMBER"),
(54, 76, "STREET_ADDRESS"),
]
}),
(
"701-361-2883 58102 North Dakota 701-491-7220 2343 Courtright Street Fargo ND"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 31, "STATE_FULL"),
(32, 44, "TELEPHONE_NUMBER"),
(45, 67, "STREET_ADDRESS"),
(68, 73, "CITY"),
(74, 76, "STATE"),
]
}),
(
"2343 Courtright Street 701-491-7220 701-361-2883 ND North Dakota Fargo 58102"
, {
"entities":[
(0, 22, "STREET_ADDRESS"),
(23, 35, "TELEPHONE_NUMBER"),
(36, 48, "MOBILE_NUMBER"),
(49, 51, "STATE"),
(52, 64, "STATE_FULL"),
(65, 70, "CITY"),
(71, 76, "ZIPCODE"),
]
}),
(
"701-361-2883 Fargo ND 58102 North Dakota 2343 Courtright Street 701-491-7220"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 18, "CITY"),
(19, 21, "STATE"),
(22, 27, "ZIPCODE"),
(28, 40, "STATE_FULL"),
(41, 63, "STREET_ADDRESS"),
(64, 76, "TELEPHONE_NUMBER"),
]
}),
(
"ND 701-491-7220 North Dakota 58102 2343 Courtright Street Fargo 701-361-2883"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "TELEPHONE_NUMBER"),
(16, 28, "STATE_FULL"),
(29, 34, "ZIPCODE"),
(35, 57, "STREET_ADDRESS"),
(58, 63, "CITY"),
(64, 76, "MOBILE_NUMBER"),
]
}),
(
"701-491-7220 2343 Courtright Street North Dakota 58102 Fargo ND 701-361-2883"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 35, "STREET_ADDRESS"),
(36, 48, "STATE_FULL"),
(49, 54, "ZIPCODE"),
(55, 60, "CITY"),
(61, 63, "STATE"),
(64, 76, "MOBILE_NUMBER"),
]
}),
(
"North Dakota ND 701-491-7220 701-361-2883 58102 2343 Courtright Street Fargo"
, {
"entities":[
(0, 12, "STATE_FULL"),
(13, 15, "STATE"),
(16, 28, "TELEPHONE_NUMBER"),
(29, 41, "MOBILE_NUMBER"),
(42, 47, "ZIPCODE"),
(48, 70, "STREET_ADDRESS"),
(71, 76, "CITY"),
]
}),
(
"701-361-2883 North Dakota 2343 Courtright Street 701-491-7220 Fargo 58102 ND"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 25, "STATE_FULL"),
(26, 48, "STREET_ADDRESS"),
(49, 61, "TELEPHONE_NUMBER"),
(62, 67, "CITY"),
(68, 73, "ZIPCODE"),
(74, 76, "STATE"),
]
}),
(
"LA 70171 Louisiana New Orleans 2517 Rose Avenue 3--5740 504-275-6637"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 18, "STATE_FULL"),
(19, 30, "CITY"),
(31, 47, "STREET_ADDRESS"),
(48, 55, "MOBILE_NUMBER"),
(56, 68, "TELEPHONE_NUMBER"),
]
}),
(
"3--5740 504-275-6637 70171 LA Louisiana New Orleans 2517 Rose Avenue"
, {
"entities":[
(0, 7, "MOBILE_NUMBER"),
(8, 20, "TELEPHONE_NUMBER"),
(21, 26, "ZIPCODE"),
(27, 29, "STATE"),
(30, 39, "STATE_FULL"),
(40, 51, "CITY"),
(52, 68, "STREET_ADDRESS"),
]
}),
(
"3--5740 504-275-6637 LA 70171 New Orleans 2517 Rose Avenue Louisiana"
, {
"entities":[
(0, 7, "MOBILE_NUMBER"),
(8, 20, "TELEPHONE_NUMBER"),
(21, 23, "STATE"),
(24, 29, "ZIPCODE"),
(30, 41, "CITY"),
(42, 58, "STREET_ADDRESS"),
(59, 68, "STATE_FULL"),
]
}),
(
"3--5740 2517 Rose Avenue New Orleans 70171 504-275-6637 Louisiana LA"
, {
"entities":[
(0, 7, "MOBILE_NUMBER"),
(8, 24, "STREET_ADDRESS"),
(25, 36, "CITY"),
(37, 42, "ZIPCODE"),
(43, 55, "TELEPHONE_NUMBER"),
(56, 65, "STATE_FULL"),
(66, 68, "STATE"),
]
}),
(
"70171 Louisiana 2517 Rose Avenue LA 3--5740 504-275-6637 New Orleans"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 15, "STATE_FULL"),
(16, 32, "STREET_ADDRESS"),
(33, 35, "STATE"),
(36, 43, "MOBILE_NUMBER"),
(44, 56, "TELEPHONE_NUMBER"),
(57, 68, "CITY"),
]
}),
(
"3--5740 2517 Rose Avenue 504-275-6637 LA Louisiana 70171 New Orleans"
, {
"entities":[
(0, 7, "MOBILE_NUMBER"),
(8, 24, "STREET_ADDRESS"),
(25, 37, "TELEPHONE_NUMBER"),
(38, 40, "STATE"),
(41, 50, "STATE_FULL"),
(51, 56, "ZIPCODE"),
(57, 68, "CITY"),
]
}),
(
"3--5740 70171 504-275-6637 Louisiana 2517 Rose Avenue LA New Orleans"
, {
"entities":[
(0, 7, "MOBILE_NUMBER"),
(8, 13, "ZIPCODE"),
(14, 26, "TELEPHONE_NUMBER"),
(27, 36, "STATE_FULL"),
(37, 53, "STREET_ADDRESS"),
(54, 56, "STATE"),
(57, 68, "CITY"),
]
}),
(
"Louisiana 3--5740 New Orleans 70171 2517 Rose Avenue 504-275-6637 LA"
, {
"entities":[
(0, 9, "STATE_FULL"),
(10, 17, "MOBILE_NUMBER"),
(18, 29, "CITY"),
(30, 35, "ZIPCODE"),
(36, 52, "STREET_ADDRESS"),
(53, 65, "TELEPHONE_NUMBER"),
(66, 68, "STATE"),
]
}),
(
"LA 70171 New Orleans 3--5740 504-275-6637 Louisiana 2517 Rose Avenue"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 20, "CITY"),
(21, 28, "MOBILE_NUMBER"),
(29, 41, "TELEPHONE_NUMBER"),
(42, 51, "STATE_FULL"),
(52, 68, "STREET_ADDRESS"),
]
}),
(
"Louisiana New Orleans 2517 Rose Avenue 3--5740 70171 LA 504-275-6637"
, {
"entities":[
(0, 9, "STATE_FULL"),
(10, 21, "CITY"),
(22, 38, "STREET_ADDRESS"),
(39, 46, "MOBILE_NUMBER"),
(47, 52, "ZIPCODE"),
(53, 55, "STATE"),
(56, 68, "TELEPHONE_NUMBER"),
]
}),
(
"1045 Lindale Avenue 510-912-6263 Oakland 510-530-1437 California CA 94602"
, {
"entities":[
(0, 19, "STREET_ADDRESS"),
(20, 32, "MOBILE_NUMBER"),
(33, 40, "CITY"),
(41, 53, "TELEPHONE_NUMBER"),
(54, 64, "STATE_FULL"),
(65, 67, "STATE"),
(68, 73, "ZIPCODE"),
]
}),
(
"California 510-912-6263 Oakland 94602 510-530-1437 CA 1045 Lindale Avenue"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 23, "MOBILE_NUMBER"),
(24, 31, "CITY"),
(32, 37, "ZIPCODE"),
(38, 50, "TELEPHONE_NUMBER"),
(51, 53, "STATE"),
(54, 73, "STREET_ADDRESS"),
]
}),
(
"510-530-1437 94602 California Oakland 1045 Lindale Avenue 510-912-6263 CA"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 29, "STATE_FULL"),
(30, 37, "CITY"),
(38, 57, "STREET_ADDRESS"),
(58, 70, "MOBILE_NUMBER"),
(71, 73, "STATE"),
]
}),
(
"1045 Lindale Avenue 94602 Oakland California 510-912-6263 CA 510-530-1437"
, {
"entities":[
(0, 19, "STREET_ADDRESS"),
(20, 25, "ZIPCODE"),
(26, 33, "CITY"),
(34, 44, "STATE_FULL"),
(45, 57, "MOBILE_NUMBER"),
(58, 60, "STATE"),
(61, 73, "TELEPHONE_NUMBER"),
]
}),
(
"1045 Lindale Avenue Oakland 510-530-1437 California 94602 510-912-6263 CA"
, {
"entities":[
(0, 19, "STREET_ADDRESS"),
(20, 27, "CITY"),
(28, 40, "TELEPHONE_NUMBER"),
(41, 51, "STATE_FULL"),
(52, 57, "ZIPCODE"),
(58, 70, "MOBILE_NUMBER"),
(71, 73, "STATE"),
]
}),
(
"1045 Lindale Avenue 94602 California 510-530-1437 CA 510-912-6263 Oakland"
, {
"entities":[
(0, 19, "STREET_ADDRESS"),
(20, 25, "ZIPCODE"),
(26, 36, "STATE_FULL"),
(37, 49, "TELEPHONE_NUMBER"),
(50, 52, "STATE"),
(53, 65, "MOBILE_NUMBER"),
(66, 73, "CITY"),
]
}),
(
"CA Oakland 1045 Lindale Avenue 94602 California 510-912-6263 510-530-1437"
, {
"entities":[
(0, 2, "STATE"),
(3, 10, "CITY"),
(11, 30, "STREET_ADDRESS"),
(31, 36, "ZIPCODE"),
(37, 47, "STATE_FULL"),
(48, 60, "MOBILE_NUMBER"),
(61, 73, "TELEPHONE_NUMBER"),
]
}),
(
"CA 510-530-1437 California 1045 Lindale Avenue Oakland 510-912-6263 94602"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "TELEPHONE_NUMBER"),
(16, 26, "STATE_FULL"),
(27, 46, "STREET_ADDRESS"),
(47, 54, "CITY"),
(55, 67, "MOBILE_NUMBER"),
(68, 73, "ZIPCODE"),
]
}),
(
"510-912-6263 Oakland 94602 510-530-1437 California CA 1045 Lindale Avenue"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 20, "CITY"),
(21, 26, "ZIPCODE"),
(27, 39, "TELEPHONE_NUMBER"),
(40, 50, "STATE_FULL"),
(51, 53, "STATE"),
(54, 73, "STREET_ADDRESS"),
]
}),
(
"510-530-1437 94602 Oakland California 1045 Lindale Avenue 510-912-6263 CA"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 26, "CITY"),
(27, 37, "STATE_FULL"),
(38, 57, "STREET_ADDRESS"),
(58, 70, "MOBILE_NUMBER"),
(71, 73, "STATE"),
]
}),
(
"619-318-4246 92123 112 Vernon Street California 760-712-2155 San Diego CA"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 36, "STREET_ADDRESS"),
(37, 47, "STATE_FULL"),
(48, 60, "TELEPHONE_NUMBER"),
(61, 70, "CITY"),
(71, 73, "STATE"),
]
}),
(
"CA 112 Vernon Street 619-318-4246 San Diego California 92123 760-712-2155"
, {
"entities":[
(0, 2, "STATE"),
(3, 20, "STREET_ADDRESS"),
(21, 33, "MOBILE_NUMBER"),
(34, 43, "CITY"),
(44, 54, "STATE_FULL"),
(55, 60, "ZIPCODE"),
(61, 73, "TELEPHONE_NUMBER"),
]
}),
(
"619-318-4246 760-712-2155 California CA 112 Vernon Street San Diego 92123"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 25, "TELEPHONE_NUMBER"),
(26, 36, "STATE_FULL"),
(37, 39, "STATE"),
(40, 57, "STREET_ADDRESS"),
(58, 67, "CITY"),
(68, 73, "ZIPCODE"),
]
}),
(
"92123 San Diego CA 112 Vernon Street 619-318-4246 California 760-712-2155"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 15, "CITY"),
(16, 18, "STATE"),
(19, 36, "STREET_ADDRESS"),
(37, 49, "MOBILE_NUMBER"),
(50, 60, "STATE_FULL"),
(61, 73, "TELEPHONE_NUMBER"),
]
}),
(
"San Diego 92123 California 112 Vernon Street CA 619-318-4246 760-712-2155"
, {
"entities":[
(0, 9, "CITY"),
(10, 15, "ZIPCODE"),
(16, 26, "STATE_FULL"),
(27, 44, "STREET_ADDRESS"),
(45, 47, "STATE"),
(48, 60, "MOBILE_NUMBER"),
(61, 73, "TELEPHONE_NUMBER"),
]
}),
(
"California San Diego 760-712-2155 92123 619-318-4246 CA 112 Vernon Street"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 20, "CITY"),
(21, 33, "TELEPHONE_NUMBER"),
(34, 39, "ZIPCODE"),
(40, 52, "MOBILE_NUMBER"),
(53, 55, "STATE"),
(56, 73, "STREET_ADDRESS"),
]
}),
(
"San Diego California 760-712-2155 112 Vernon Street 92123 619-318-4246 CA"
, {
"entities":[
(0, 9, "CITY"),
(10, 20, "STATE_FULL"),
(21, 33, "TELEPHONE_NUMBER"),
(34, 51, "STREET_ADDRESS"),
(52, 57, "ZIPCODE"),
(58, 70, "MOBILE_NUMBER"),
(71, 73, "STATE"),
]
}),
(
"112 Vernon Street 92123 619-318-4246 760-712-2155 San Diego California CA"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 23, "ZIPCODE"),
(24, 36, "MOBILE_NUMBER"),
(37, 49, "TELEPHONE_NUMBER"),
(50, 59, "CITY"),
(60, 70, "STATE_FULL"),
(71, 73, "STATE"),
]
}),
(
"San Diego 112 Vernon Street California 92123 760-712-2155 CA 619-318-4246"
, {
"entities":[
(0, 9, "CITY"),
(10, 27, "STREET_ADDRESS"),
(28, 38, "STATE_FULL"),
(39, 44, "ZIPCODE"),
(45, 57, "TELEPHONE_NUMBER"),
(58, 60, "STATE"),
(61, 73, "MOBILE_NUMBER"),
]
}),
(
"CA California San Diego 112 Vernon Street 760-712-2155 619-318-4246 92123"
, {
"entities":[
(0, 2, "STATE"),
(3, 13, "STATE_FULL"),
(14, 23, "CITY"),
(24, 41, "STREET_ADDRESS"),
(42, 54, "TELEPHONE_NUMBER"),
(55, 67, "MOBILE_NUMBER"),
(68, 73, "ZIPCODE"),
]
}),
(
"401-567-5514 02859 RI Rhode Island 401-678-2227 Pascoag 1855 Myra Street"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 21, "STATE"),
(22, 34, "STATE_FULL"),
(35, 47, "MOBILE_NUMBER"),
(48, 55, "CITY"),
(56, 72, "STREET_ADDRESS"),
]
}),
(
"401-567-5514 Rhode Island RI 02859 Pascoag 401-678-2227 1855 Myra Street"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 25, "STATE_FULL"),
(26, 28, "STATE"),
(29, 34, "ZIPCODE"),
(35, 42, "CITY"),
(43, 55, "MOBILE_NUMBER"),
(56, 72, "STREET_ADDRESS"),
]
}),
(
"1855 Myra Street 401-678-2227 RI 02859 Pascoag Rhode Island 401-567-5514"
, {
"entities":[
(0, 16, "STREET_ADDRESS"),
(17, 29, "MOBILE_NUMBER"),
(30, 32, "STATE"),
(33, 38, "ZIPCODE"),
(39, 46, "CITY"),
(47, 59, "STATE_FULL"),
(60, 72, "TELEPHONE_NUMBER"),
]
}),
(
"401-678-2227 Rhode Island 02859 401-567-5514 RI Pascoag 1855 Myra Street"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 25, "STATE_FULL"),
(26, 31, "ZIPCODE"),
(32, 44, "TELEPHONE_NUMBER"),
(45, 47, "STATE"),
(48, 55, "CITY"),
(56, 72, "STREET_ADDRESS"),
]
}),
(
"401-567-5514 401-678-2227 Rhode Island RI Pascoag 02859 1855 Myra Street"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 25, "MOBILE_NUMBER"),
(26, 38, "STATE_FULL"),
(39, 41, "STATE"),
(42, 49, "CITY"),
(50, 55, "ZIPCODE"),
(56, 72, "STREET_ADDRESS"),
]
}),
(
"1855 Myra Street 401-678-2227 RI 401-567-5514 Rhode Island 02859 Pascoag"
, {
"entities":[
(0, 16, "STREET_ADDRESS"),
(17, 29, "MOBILE_NUMBER"),
(30, 32, "STATE"),
(33, 45, "TELEPHONE_NUMBER"),
(46, 58, "STATE_FULL"),
(59, 64, "ZIPCODE"),
(65, 72, "CITY"),
]
}),
(
"401-567-5514 02859 401-678-2227 Pascoag RI Rhode Island 1855 Myra Street"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 31, "MOBILE_NUMBER"),
(32, 39, "CITY"),
(40, 42, "STATE"),
(43, 55, "STATE_FULL"),
(56, 72, "STREET_ADDRESS"),
]
}),
(
"RI 1855 Myra Street 02859 Pascoag Rhode Island 401-678-2227 401-567-5514"
, {
"entities":[
(0, 2, "STATE"),
(3, 19, "STREET_ADDRESS"),
(20, 25, "ZIPCODE"),
(26, 33, "CITY"),
(34, 46, "STATE_FULL"),
(47, 59, "MOBILE_NUMBER"),
(60, 72, "TELEPHONE_NUMBER"),
]
}),
(
"RI Rhode Island 1855 Myra Street 02859 401-567-5514 401-678-2227 Pascoag"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "STATE_FULL"),
(16, 32, "STREET_ADDRESS"),
(33, 38, "ZIPCODE"),
(39, 51, "TELEPHONE_NUMBER"),
(52, 64, "MOBILE_NUMBER"),
(65, 72, "CITY"),
]
}),
(
"401-567-5514 Rhode Island 1855 Myra Street RI 401-678-2227 Pascoag 02859"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 25, "STATE_FULL"),
(26, 42, "STREET_ADDRESS"),
(43, 45, "STATE"),
(46, 58, "MOBILE_NUMBER"),
(59, 66, "CITY"),
(67, 72, "ZIPCODE"),
]
}),
(
"Savannah 2859 Layman Avenue GA 912-667-4556 Georgia 31401 912-231-3111"
, {
"entities":[
(0, 8, "CITY"),
(9, 27, "STREET_ADDRESS"),
(28, 30, "STATE"),
(31, 43, "MOBILE_NUMBER"),
(44, 51, "STATE_FULL"),
(52, 57, "ZIPCODE"),
(58, 70, "TELEPHONE_NUMBER"),
]
}),
(
"2859 Layman Avenue 31401 912-231-3111 GA 912-667-4556 Savannah Georgia"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 24, "ZIPCODE"),
(25, 37, "TELEPHONE_NUMBER"),
(38, 40, "STATE"),
(41, 53, "MOBILE_NUMBER"),
(54, 62, "CITY"),
(63, 70, "STATE_FULL"),
]
}),
(
"GA 912-667-4556 2859 Layman Avenue Savannah 31401 912-231-3111 Georgia"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "MOBILE_NUMBER"),
(16, 34, "STREET_ADDRESS"),
(35, 43, "CITY"),
(44, 49, "ZIPCODE"),
(50, 62, "TELEPHONE_NUMBER"),
(63, 70, "STATE_FULL"),
]
}),
(
"Georgia 31401 GA Savannah 912-231-3111 912-667-4556 2859 Layman Avenue"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 13, "ZIPCODE"),
(14, 16, "STATE"),
(17, 25, "CITY"),
(26, 38, "TELEPHONE_NUMBER"),
(39, 51, "MOBILE_NUMBER"),
(52, 70, "STREET_ADDRESS"),
]
}),
(
"31401 912-231-3111 2859 Layman Avenue Savannah Georgia GA 912-667-4556"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "TELEPHONE_NUMBER"),
(19, 37, "STREET_ADDRESS"),
(38, 46, "CITY"),
(47, 54, "STATE_FULL"),
(55, 57, "STATE"),
(58, 70, "MOBILE_NUMBER"),
]
}),
(
"Georgia GA Savannah 2859 Layman Avenue 912-231-3111 31401 912-667-4556"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 10, "STATE"),
(11, 19, "CITY"),
(20, 38, "STREET_ADDRESS"),
(39, 51, "TELEPHONE_NUMBER"),
(52, 57, "ZIPCODE"),
(58, 70, "MOBILE_NUMBER"),
]
}),
(
"GA Savannah 2859 Layman Avenue 912-231-3111 31401 912-667-4556 Georgia"
, {
"entities":[
(0, 2, "STATE"),
(3, 11, "CITY"),
(12, 30, "STREET_ADDRESS"),
(31, 43, "TELEPHONE_NUMBER"),
(44, 49, "ZIPCODE"),
(50, 62, "MOBILE_NUMBER"),
(63, 70, "STATE_FULL"),
]
}),
(
"GA Georgia 912-231-3111 912-667-4556 31401 2859 Layman Avenue Savannah"
, {
"entities":[
(0, 2, "STATE"),
(3, 10, "STATE_FULL"),
(11, 23, "TELEPHONE_NUMBER"),
(24, 36, "MOBILE_NUMBER"),
(37, 42, "ZIPCODE"),
(43, 61, "STREET_ADDRESS"),
(62, 70, "CITY"),
]
}),
(
"Georgia 31401 912-667-4556 2859 Layman Avenue Savannah GA 912-231-3111"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 13, "ZIPCODE"),
(14, 26, "MOBILE_NUMBER"),
(27, 45, "STREET_ADDRESS"),
(46, 54, "CITY"),
(55, 57, "STATE"),
(58, 70, "TELEPHONE_NUMBER"),
]
}),
(
"2859 Layman Avenue 912-231-3111 31401 912-667-4556 Georgia Savannah GA"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 31, "TELEPHONE_NUMBER"),
(32, 37, "ZIPCODE"),
(38, 50, "MOBILE_NUMBER"),
(51, 58, "STATE_FULL"),
(59, 67, "CITY"),
(68, 70, "STATE"),
]
}),
(
"330-389-5855 43736 740-489-6053 4264 Irving Road Ohio Fairviwew OH"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 31, "TELEPHONE_NUMBER"),
(32, 48, "STREET_ADDRESS"),
(49, 53, "STATE_FULL"),
(54, 63, "CITY"),
(64, 66, "STATE"),
]
}),
(
"Fairviwew 43736 740-489-6053 4264 Irving Road 330-389-5855 OH Ohio"
, {
"entities":[
(0, 9, "CITY"),
(10, 15, "ZIPCODE"),
(16, 28, "TELEPHONE_NUMBER"),
(29, 45, "STREET_ADDRESS"),
(46, 58, "MOBILE_NUMBER"),
(59, 61, "STATE"),
(62, 66, "STATE_FULL"),
]
}),
(
"Fairviwew 330-389-5855 740-489-6053 Ohio 4264 Irving Road OH 43736"
, {
"entities":[
(0, 9, "CITY"),
(10, 22, "MOBILE_NUMBER"),
(23, 35, "TELEPHONE_NUMBER"),
(36, 40, "STATE_FULL"),
(41, 57, "STREET_ADDRESS"),
(58, 60, "STATE"),
(61, 66, "ZIPCODE"),
]
}),
(
"OH 740-489-6053 Fairviwew Ohio 43736 330-389-5855 4264 Irving Road"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "TELEPHONE_NUMBER"),
(16, 25, "CITY"),
(26, 30, "STATE_FULL"),
(31, 36, "ZIPCODE"),
(37, 49, "MOBILE_NUMBER"),
(50, 66, "STREET_ADDRESS"),
]
}),
(
"OH 330-389-5855 4264 Irving Road 43736 Ohio Fairviwew 740-489-6053"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "MOBILE_NUMBER"),
(16, 32, "STREET_ADDRESS"),
(33, 38, "ZIPCODE"),
(39, 43, "STATE_FULL"),
(44, 53, "CITY"),
(54, 66, "TELEPHONE_NUMBER"),
]
}),
(
"Ohio 4264 Irving Road Fairviwew 43736 330-389-5855 740-489-6053 OH"
, {
"entities":[
(0, 4, "STATE_FULL"),
(5, 21, "STREET_ADDRESS"),
(22, 31, "CITY"),
(32, 37, "ZIPCODE"),
(38, 50, "MOBILE_NUMBER"),
(51, 63, "TELEPHONE_NUMBER"),
(64, 66, "STATE"),
]
}),
(
"Fairviwew OH 43736 4264 Irving Road 330-389-5855 Ohio 740-489-6053"
, {
"entities":[
(0, 9, "CITY"),
(10, 12, "STATE"),
(13, 18, "ZIPCODE"),
(19, 35, "STREET_ADDRESS"),
(36, 48, "MOBILE_NUMBER"),
(49, 53, "STATE_FULL"),
(54, 66, "TELEPHONE_NUMBER"),
]
}),
(
"330-389-5855 740-489-6053 4264 Irving Road OH 43736 Fairviwew Ohio"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 25, "TELEPHONE_NUMBER"),
(26, 42, "STREET_ADDRESS"),
(43, 45, "STATE"),
(46, 51, "ZIPCODE"),
(52, 61, "CITY"),
(62, 66, "STATE_FULL"),
]
}),
(
"43736 740-489-6053 330-389-5855 Fairviwew 4264 Irving Road OH Ohio"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "TELEPHONE_NUMBER"),
(19, 31, "MOBILE_NUMBER"),
(32, 41, "CITY"),
(42, 58, "STREET_ADDRESS"),
(59, 61, "STATE"),
(62, 66, "STATE_FULL"),
]
}),
(
"OH 330-389-5855 740-489-6053 Ohio Fairviwew 4264 Irving Road 43736"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "MOBILE_NUMBER"),
(16, 28, "TELEPHONE_NUMBER"),
(29, 33, "STATE_FULL"),
(34, 43, "CITY"),
(44, 60, "STREET_ADDRESS"),
(61, 66, "ZIPCODE"),
]
}),
(
"Florida Miami 368 Agriculture Lane 33145 786-543-8081 FL 305-250-6700"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 13, "CITY"),
(14, 34, "STREET_ADDRESS"),
(35, 40, "ZIPCODE"),
(41, 53, "MOBILE_NUMBER"),
(54, 56, "STATE"),
(57, 69, "TELEPHONE_NUMBER"),
]
}),
(
"33145 368 Agriculture Lane 786-543-8081 Miami FL Florida 305-250-6700"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 26, "STREET_ADDRESS"),
(27, 39, "MOBILE_NUMBER"),
(40, 45, "CITY"),
(46, 48, "STATE"),
(49, 56, "STATE_FULL"),
(57, 69, "TELEPHONE_NUMBER"),
]
}),
(
"Florida 305-250-6700 33145 786-543-8081 FL 368 Agriculture Lane Miami"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 20, "TELEPHONE_NUMBER"),
(21, 26, "ZIPCODE"),
(27, 39, "MOBILE_NUMBER"),
(40, 42, "STATE"),
(43, 63, "STREET_ADDRESS"),
(64, 69, "CITY"),
]
}),
(
"Florida Miami 305-250-6700 33145 786-543-8081 FL 368 Agriculture Lane"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 13, "CITY"),
(14, 26, "TELEPHONE_NUMBER"),
(27, 32, "ZIPCODE"),
(33, 45, "MOBILE_NUMBER"),
(46, 48, "STATE"),
(49, 69, "STREET_ADDRESS"),
]
}),
(
"Miami 368 Agriculture Lane 33145 786-543-8081 Florida 305-250-6700 FL"
, {
"entities":[
(0, 5, "CITY"),
(6, 26, "STREET_ADDRESS"),
(27, 32, "ZIPCODE"),
(33, 45, "MOBILE_NUMBER"),
(46, 53, "STATE_FULL"),
(54, 66, "TELEPHONE_NUMBER"),
(67, 69, "STATE"),
]
}),
(
"Florida FL 786-543-8081 Miami 33145 305-250-6700 368 Agriculture Lane"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 10, "STATE"),
(11, 23, "MOBILE_NUMBER"),
(24, 29, "CITY"),
(30, 35, "ZIPCODE"),
(36, 48, "TELEPHONE_NUMBER"),
(49, 69, "STREET_ADDRESS"),
]
}),
(
"305-250-6700 FL Florida Miami 33145 786-543-8081 368 Agriculture Lane"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 15, "STATE"),
(16, 23, "STATE_FULL"),
(24, 29, "CITY"),
(30, 35, "ZIPCODE"),
(36, 48, "MOBILE_NUMBER"),
(49, 69, "STREET_ADDRESS"),
]
}),
(
"Miami FL 33145 305-250-6700 368 Agriculture Lane 786-543-8081 Florida"
, {
"entities":[
(0, 5, "CITY"),
(6, 8, "STATE"),
(9, 14, "ZIPCODE"),
(15, 27, "TELEPHONE_NUMBER"),
(28, 48, "STREET_ADDRESS"),
(49, 61, "MOBILE_NUMBER"),
(62, 69, "STATE_FULL"),
]
}),
(
"368 Agriculture Lane 33145 Miami 305-250-6700 Florida 786-543-8081 FL"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 26, "ZIPCODE"),
(27, 32, "CITY"),
(33, 45, "TELEPHONE_NUMBER"),
(46, 53, "STATE_FULL"),
(54, 66, "MOBILE_NUMBER"),
(67, 69, "STATE"),
]
}),
(
"33145 368 Agriculture Lane 305-250-6700 Miami FL 786-543-8081 Florida"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 26, "STREET_ADDRESS"),
(27, 39, "TELEPHONE_NUMBER"),
(40, 45, "CITY"),
(46, 48, "STATE"),
(49, 61, "MOBILE_NUMBER"),
(62, 69, "STATE_FULL"),
]
}),
(
"Michigan 734-717-7337 49801 MI 2629 Wood Duck Drive 906-370-7953 Iron Mountain"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 21, "MOBILE_NUMBER"),
(22, 27, "ZIPCODE"),
(28, 30, "STATE"),
(31, 51, "STREET_ADDRESS"),
(52, 64, "TELEPHONE_NUMBER"),
(65, 78, "CITY"),
]
}),
(
"Michigan 906-370-7953 MI 734-717-7337 2629 Wood Duck Drive 49801 Iron Mountain"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 21, "TELEPHONE_NUMBER"),
(22, 24, "STATE"),
(25, 37, "MOBILE_NUMBER"),
(38, 58, "STREET_ADDRESS"),
(59, 64, "ZIPCODE"),
(65, 78, "CITY"),
]
}),
(
"2629 Wood Duck Drive Iron Mountain MI 734-717-7337 49801 906-370-7953 Michigan"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 34, "CITY"),
(35, 37, "STATE"),
(38, 50, "MOBILE_NUMBER"),
(51, 56, "ZIPCODE"),
(57, 69, "TELEPHONE_NUMBER"),
(70, 78, "STATE_FULL"),
]
}),
(
"MI 734-717-7337 Michigan Iron Mountain 906-370-7953 49801 2629 Wood Duck Drive"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "MOBILE_NUMBER"),
(16, 24, "STATE_FULL"),
(25, 38, "CITY"),
(39, 51, "TELEPHONE_NUMBER"),
(52, 57, "ZIPCODE"),
(58, 78, "STREET_ADDRESS"),
]
}),
(
"49801 734-717-7337 MI 2629 Wood Duck Drive Michigan 906-370-7953 Iron Mountain"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "MOBILE_NUMBER"),
(19, 21, "STATE"),
(22, 42, "STREET_ADDRESS"),
(43, 51, "STATE_FULL"),
(52, 64, "TELEPHONE_NUMBER"),
(65, 78, "CITY"),
]
}),
(
"734-717-7337 2629 Wood Duck Drive Iron Mountain 49801 906-370-7953 Michigan MI"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 33, "STREET_ADDRESS"),
(34, 47, "CITY"),
(48, 53, "ZIPCODE"),
(54, 66, "TELEPHONE_NUMBER"),
(67, 75, "STATE_FULL"),
(76, 78, "STATE"),
]
}),
(
"2629 Wood Duck Drive 906-370-7953 MI 49801 Michigan 734-717-7337 Iron Mountain"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 33, "TELEPHONE_NUMBER"),
(34, 36, "STATE"),
(37, 42, "ZIPCODE"),
(43, 51, "STATE_FULL"),
(52, 64, "MOBILE_NUMBER"),
(65, 78, "CITY"),
]
}),
(
"49801 906-370-7953 2629 Wood Duck Drive Iron Mountain Michigan 734-717-7337 MI"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "TELEPHONE_NUMBER"),
(19, 39, "STREET_ADDRESS"),
(40, 53, "CITY"),
(54, 62, "STATE_FULL"),
(63, 75, "MOBILE_NUMBER"),
(76, 78, "STATE"),
]
}),
(
"2629 Wood Duck Drive 49801 734-717-7337 906-370-7953 MI Michigan Iron Mountain"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 26, "ZIPCODE"),
(27, 39, "MOBILE_NUMBER"),
(40, 52, "TELEPHONE_NUMBER"),
(53, 55, "STATE"),
(56, 64, "STATE_FULL"),
(65, 78, "CITY"),
]
}),
(
"Michigan 734-717-7337 2629 Wood Duck Drive Iron Mountain 49801 906-370-7953 MI"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 21, "MOBILE_NUMBER"),
(22, 42, "STREET_ADDRESS"),
(43, 56, "CITY"),
(57, 62, "ZIPCODE"),
(63, 75, "TELEPHONE_NUMBER"),
(76, 78, "STATE"),
]
}),
(
"Alabama 256-776-6104 AL Gurley 205-732-4555 35748 4435 Ferry Street"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 20, "TELEPHONE_NUMBER"),
(21, 23, "STATE"),
(24, 30, "CITY"),
(31, 43, "MOBILE_NUMBER"),
(44, 49, "ZIPCODE"),
(50, 67, "STREET_ADDRESS"),
]
}),
(
"256-776-6104 205-732-4555 Gurley AL Alabama 4435 Ferry Street 35748"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 25, "MOBILE_NUMBER"),
(26, 32, "CITY"),
(33, 35, "STATE"),
(36, 43, "STATE_FULL"),
(44, 61, "STREET_ADDRESS"),
(62, 67, "ZIPCODE"),
]
}),
(
"Alabama AL 256-776-6104 35748 Gurley 4435 Ferry Street 205-732-4555"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 10, "STATE"),
(11, 23, "TELEPHONE_NUMBER"),
(24, 29, "ZIPCODE"),
(30, 36, "CITY"),
(37, 54, "STREET_ADDRESS"),
(55, 67, "MOBILE_NUMBER"),
]
}),
(
"AL Gurley 4435 Ferry Street 256-776-6104 35748 205-732-4555 Alabama"
, {
"entities":[
(0, 2, "STATE"),
(3, 9, "CITY"),
(10, 27, "STREET_ADDRESS"),
(28, 40, "TELEPHONE_NUMBER"),
(41, 46, "ZIPCODE"),
(47, 59, "MOBILE_NUMBER"),
(60, 67, "STATE_FULL"),
]
}),
(
"4435 Ferry Street AL Gurley 35748 256-776-6104 Alabama 205-732-4555"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 20, "STATE"),
(21, 27, "CITY"),
(28, 33, "ZIPCODE"),
(34, 46, "TELEPHONE_NUMBER"),
(47, 54, "STATE_FULL"),
(55, 67, "MOBILE_NUMBER"),
]
}),
(
"Alabama 205-732-4555 Gurley 4435 Ferry Street 256-776-6104 AL 35748"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 20, "MOBILE_NUMBER"),
(21, 27, "CITY"),
(28, 45, "STREET_ADDRESS"),
(46, 58, "TELEPHONE_NUMBER"),
(59, 61, "STATE"),
(62, 67, "ZIPCODE"),
]
}),
(
"Alabama Gurley AL 205-732-4555 4435 Ferry Street 35748 256-776-6104"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 14, "CITY"),
(15, 17, "STATE"),
(18, 30, "MOBILE_NUMBER"),
(31, 48, "STREET_ADDRESS"),
(49, 54, "ZIPCODE"),
(55, 67, "TELEPHONE_NUMBER"),
]
}),
(
"4435 Ferry Street 35748 Gurley AL Alabama 256-776-6104 205-732-4555"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 23, "ZIPCODE"),
(24, 30, "CITY"),
(31, 33, "STATE"),
(34, 41, "STATE_FULL"),
(42, 54, "TELEPHONE_NUMBER"),
(55, 67, "MOBILE_NUMBER"),
]
}),
(
"256-776-6104 Gurley Alabama AL 4435 Ferry Street 35748 205-732-4555"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 19, "CITY"),
(20, 27, "STATE_FULL"),
(28, 30, "STATE"),
(31, 48, "STREET_ADDRESS"),
(49, 54, "ZIPCODE"),
(55, 67, "MOBILE_NUMBER"),
]
}),
(
"AL 35748 4435 Ferry Street Gurley Alabama 205-732-4555 256-776-6104"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 26, "STREET_ADDRESS"),
(27, 33, "CITY"),
(34, 41, "STATE_FULL"),
(42, 54, "MOBILE_NUMBER"),
(55, 67, "TELEPHONE_NUMBER"),
]
}),
(
"773-936-7601 Illinois 4890 Oak Avenue Chicago 847-932-5806 IL 60606"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 21, "STATE_FULL"),
(22, 37, "STREET_ADDRESS"),
(38, 45, "CITY"),
(46, 58, "TELEPHONE_NUMBER"),
(59, 61, "STATE"),
(62, 67, "ZIPCODE"),
]
}),
(
"IL 4890 Oak Avenue 773-936-7601 Illinois 60606 Chicago 847-932-5806"
, {
"entities":[
(0, 2, "STATE"),
(3, 18, "STREET_ADDRESS"),
(19, 31, "MOBILE_NUMBER"),
(32, 40, "STATE_FULL"),
(41, 46, "ZIPCODE"),
(47, 54, "CITY"),
(55, 67, "TELEPHONE_NUMBER"),
]
}),
(
"4890 Oak Avenue 60606 Illinois Chicago 773-936-7601 847-932-5806 IL"
, {
"entities":[
(0, 15, "STREET_ADDRESS"),
(16, 21, "ZIPCODE"),
(22, 30, "STATE_FULL"),
(31, 38, "CITY"),
(39, 51, "MOBILE_NUMBER"),
(52, 64, "TELEPHONE_NUMBER"),
(65, 67, "STATE"),
]
}),
(
"IL 773-936-7601 4890 Oak Avenue Illinois Chicago 847-932-5806 60606"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "MOBILE_NUMBER"),
(16, 31, "STREET_ADDRESS"),
(32, 40, "STATE_FULL"),
(41, 48, "CITY"),
(49, 61, "TELEPHONE_NUMBER"),
(62, 67, "ZIPCODE"),
]
}),
(
"60606 773-936-7601 Chicago Illinois 847-932-5806 4890 Oak Avenue IL"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "MOBILE_NUMBER"),
(19, 26, "CITY"),
(27, 35, "STATE_FULL"),
(36, 48, "TELEPHONE_NUMBER"),
(49, 64, "STREET_ADDRESS"),
(65, 67, "STATE"),
]
}),
(
"847-932-5806 773-936-7601 4890 Oak Avenue Illinois 60606 IL Chicago"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 25, "MOBILE_NUMBER"),
(26, 41, "STREET_ADDRESS"),
(42, 50, "STATE_FULL"),
(51, 56, "ZIPCODE"),
(57, 59, "STATE"),
(60, 67, "CITY"),
]
}),
(
"Illinois 4890 Oak Avenue 60606 IL Chicago 847-932-5806 773-936-7601"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 24, "STREET_ADDRESS"),
(25, 30, "ZIPCODE"),
(31, 33, "STATE"),
(34, 41, "CITY"),
(42, 54, "TELEPHONE_NUMBER"),
(55, 67, "MOBILE_NUMBER"),
]
}),
(
"847-932-5806 773-936-7601 Illinois 60606 4890 Oak Avenue Chicago IL"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 25, "MOBILE_NUMBER"),
(26, 34, "STATE_FULL"),
(35, 40, "ZIPCODE"),
(41, 56, "STREET_ADDRESS"),
(57, 64, "CITY"),
(65, 67, "STATE"),
]
}),
(
"Chicago 4890 Oak Avenue 847-932-5806 Illinois IL 773-936-7601 60606"
, {
"entities":[
(0, 7, "CITY"),
(8, 23, "STREET_ADDRESS"),
(24, 36, "TELEPHONE_NUMBER"),
(37, 45, "STATE_FULL"),
(46, 48, "STATE"),
(49, 61, "MOBILE_NUMBER"),
(62, 67, "ZIPCODE"),
]
}),
(
"Chicago IL 4890 Oak Avenue 847-932-5806 773-936-7601 60606 Illinois"
, {
"entities":[
(0, 7, "CITY"),
(8, 10, "STATE"),
(11, 26, "STREET_ADDRESS"),
(27, 39, "TELEPHONE_NUMBER"),
(40, 52, "MOBILE_NUMBER"),
(53, 58, "ZIPCODE"),
(59, 67, "STATE_FULL"),
]
}),
(
"480-229-0878 Arizona Salome AZ 85348 928-859-6486 581 Farm Meadow Drive"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 20, "STATE_FULL"),
(21, 27, "CITY"),
(28, 30, "STATE"),
(31, 36, "ZIPCODE"),
(37, 49, "TELEPHONE_NUMBER"),
(50, 71, "STREET_ADDRESS"),
]
}),
(
"85348 480-229-0878 581 Farm Meadow Drive Arizona 928-859-6486 Salome AZ"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "MOBILE_NUMBER"),
(19, 40, "STREET_ADDRESS"),
(41, 48, "STATE_FULL"),
(49, 61, "TELEPHONE_NUMBER"),
(62, 68, "CITY"),
(69, 71, "STATE"),
]
}),
(
"Arizona Salome 581 Farm Meadow Drive AZ 480-229-0878 85348 928-859-6486"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 14, "CITY"),
(15, 36, "STREET_ADDRESS"),
(37, 39, "STATE"),
(40, 52, "MOBILE_NUMBER"),
(53, 58, "ZIPCODE"),
(59, 71, "TELEPHONE_NUMBER"),
]
}),
(
"85348 928-859-6486 581 Farm Meadow Drive 480-229-0878 Salome AZ Arizona"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "TELEPHONE_NUMBER"),
(19, 40, "STREET_ADDRESS"),
(41, 53, "MOBILE_NUMBER"),
(54, 60, "CITY"),
(61, 63, "STATE"),
(64, 71, "STATE_FULL"),
]
}),
(
"Salome 928-859-6486 480-229-0878 AZ 581 Farm Meadow Drive 85348 Arizona"
, {
"entities":[
(0, 6, "CITY"),
(7, 19, "TELEPHONE_NUMBER"),
(20, 32, "MOBILE_NUMBER"),
(33, 35, "STATE"),
(36, 57, "STREET_ADDRESS"),
(58, 63, "ZIPCODE"),
(64, 71, "STATE_FULL"),
]
}),
(
"AZ 928-859-6486 480-229-0878 Salome 85348 581 Farm Meadow Drive Arizona"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "TELEPHONE_NUMBER"),
(16, 28, "MOBILE_NUMBER"),
(29, 35, "CITY"),
(36, 41, "ZIPCODE"),
(42, 63, "STREET_ADDRESS"),
(64, 71, "STATE_FULL"),
]
}),
(
"581 Farm Meadow Drive Salome AZ Arizona 480-229-0878 85348 928-859-6486"
, {
"entities":[
(0, 21, "STREET_ADDRESS"),
(22, 28, "CITY"),
(29, 31, "STATE"),
(32, 39, "STATE_FULL"),
(40, 52, "MOBILE_NUMBER"),
(53, 58, "ZIPCODE"),
(59, 71, "TELEPHONE_NUMBER"),
]
}),
(
"85348 Salome AZ 928-859-6486 581 Farm Meadow Drive 480-229-0878 Arizona"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 12, "CITY"),
(13, 15, "STATE"),
(16, 28, "TELEPHONE_NUMBER"),
(29, 50, "STREET_ADDRESS"),
(51, 63, "MOBILE_NUMBER"),
(64, 71, "STATE_FULL"),
]
}),
(
"85348 480-229-0878 928-859-6486 AZ Arizona Salome 581 Farm Meadow Drive"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "MOBILE_NUMBER"),
(19, 31, "TELEPHONE_NUMBER"),
(32, 34, "STATE"),
(35, 42, "STATE_FULL"),
(43, 49, "CITY"),
(50, 71, "STREET_ADDRESS"),
]
}),
(
"Salome 85348 Arizona 480-229-0878 AZ 581 Farm Meadow Drive 928-859-6486"
, {
"entities":[
(0, 6, "CITY"),
(7, 12, "ZIPCODE"),
(13, 20, "STATE_FULL"),
(21, 33, "MOBILE_NUMBER"),
(34, 36, "STATE"),
(37, 58, "STREET_ADDRESS"),
(59, 71, "TELEPHONE_NUMBER"),
]
}),
(
"Pennsylvania 17320 513 Lincoln Drive PA Fairfield (Adams) 610-804-7644 717-642-2172"
, {
"entities":[
(0, 12, "STATE_FULL"),
(13, 18, "ZIPCODE"),
(19, 36, "STREET_ADDRESS"),
(37, 39, "STATE"),
(40, 57, "CITY"),
(58, 70, "MOBILE_NUMBER"),
(71, 83, "TELEPHONE_NUMBER"),
]
}),
(
"513 Lincoln Drive 17320 Pennsylvania Fairfield (Adams) 610-804-7644 PA 717-642-2172"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 23, "ZIPCODE"),
(24, 36, "STATE_FULL"),
(37, 54, "CITY"),
(55, 67, "MOBILE_NUMBER"),
(68, 70, "STATE"),
(71, 83, "TELEPHONE_NUMBER"),
]
}),
(
"PA Pennsylvania 610-804-7644 717-642-2172 17320 Fairfield (Adams) 513 Lincoln Drive"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "STATE_FULL"),
(16, 28, "MOBILE_NUMBER"),
(29, 41, "TELEPHONE_NUMBER"),
(42, 47, "ZIPCODE"),
(48, 65, "CITY"),
(66, 83, "STREET_ADDRESS"),
]
}),
(
"Fairfield (Adams) 717-642-2172 610-804-7644 Pennsylvania 513 Lincoln Drive 17320 PA"
, {
"entities":[
(0, 17, "CITY"),
(18, 30, "TELEPHONE_NUMBER"),
(31, 43, "MOBILE_NUMBER"),
(44, 56, "STATE_FULL"),
(57, 74, "STREET_ADDRESS"),
(75, 80, "ZIPCODE"),
(81, 83, "STATE"),
]
}),
(
"Pennsylvania 17320 PA 717-642-2172 610-804-7644 Fairfield (Adams) 513 Lincoln Drive"
, {
"entities":[
(0, 12, "STATE_FULL"),
(13, 18, "ZIPCODE"),
(19, 21, "STATE"),
(22, 34, "TELEPHONE_NUMBER"),
(35, 47, "MOBILE_NUMBER"),
(48, 65, "CITY"),
(66, 83, "STREET_ADDRESS"),
]
}),
(
"513 Lincoln Drive 717-642-2172 Pennsylvania 610-804-7644 Fairfield (Adams) 17320 PA"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 30, "TELEPHONE_NUMBER"),
(31, 43, "STATE_FULL"),
(44, 56, "MOBILE_NUMBER"),
(57, 74, "CITY"),
(75, 80, "ZIPCODE"),
(81, 83, "STATE"),
]
}),
(
"513 Lincoln Drive 17320 717-642-2172 Fairfield (Adams) Pennsylvania PA 610-804-7644"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 23, "ZIPCODE"),
(24, 36, "TELEPHONE_NUMBER"),
(37, 54, "CITY"),
(55, 67, "STATE_FULL"),
(68, 70, "STATE"),
(71, 83, "MOBILE_NUMBER"),
]
}),
(
"PA 17320 717-642-2172 Pennsylvania 513 Lincoln Drive Fairfield (Adams) 610-804-7644"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 21, "TELEPHONE_NUMBER"),
(22, 34, "STATE_FULL"),
(35, 52, "STREET_ADDRESS"),
(53, 70, "CITY"),
(71, 83, "MOBILE_NUMBER"),
]
}),
(
"17320 Fairfield (Adams) 513 Lincoln Drive Pennsylvania PA 610-804-7644 717-642-2172"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 23, "CITY"),
(24, 41, "STREET_ADDRESS"),
(42, 54, "STATE_FULL"),
(55, 57, "STATE"),
(58, 70, "MOBILE_NUMBER"),
(71, 83, "TELEPHONE_NUMBER"),
]
}),
(
"610-804-7644 717-642-2172 513 Lincoln Drive Fairfield (Adams) 17320 Pennsylvania PA"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 25, "TELEPHONE_NUMBER"),
(26, 43, "STREET_ADDRESS"),
(44, 61, "CITY"),
(62, 67, "ZIPCODE"),
(68, 80, "STATE_FULL"),
(81, 83, "STATE"),
]
}),
(
"434-825-5724 Troutville Virginia VA 24175 2140 Maxwell Farm Road 540-260-0797"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 23, "CITY"),
(24, 32, "STATE_FULL"),
(33, 35, "STATE"),
(36, 41, "ZIPCODE"),
(42, 64, "STREET_ADDRESS"),
(65, 77, "TELEPHONE_NUMBER"),
]
}),
(
"24175 2140 Maxwell Farm Road VA 434-825-5724 Troutville 540-260-0797 Virginia"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 28, "STREET_ADDRESS"),
(29, 31, "STATE"),
(32, 44, "MOBILE_NUMBER"),
(45, 55, "CITY"),
(56, 68, "TELEPHONE_NUMBER"),
(69, 77, "STATE_FULL"),
]
}),
(
"540-260-0797 24175 434-825-5724 VA 2140 Maxwell Farm Road Troutville Virginia"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 31, "MOBILE_NUMBER"),
(32, 34, "STATE"),
(35, 57, "STREET_ADDRESS"),
(58, 68, "CITY"),
(69, 77, "STATE_FULL"),
]
}),
(
"Virginia 434-825-5724 VA Troutville 24175 540-260-0797 2140 Maxwell Farm Road"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 21, "MOBILE_NUMBER"),
(22, 24, "STATE"),
(25, 35, "CITY"),
(36, 41, "ZIPCODE"),
(42, 54, "TELEPHONE_NUMBER"),
(55, 77, "STREET_ADDRESS"),
]
}),
(
"VA Troutville Virginia 434-825-5724 540-260-0797 24175 2140 Maxwell Farm Road"
, {
"entities":[
(0, 2, "STATE"),
(3, 13, "CITY"),
(14, 22, "STATE_FULL"),
(23, 35, "MOBILE_NUMBER"),
(36, 48, "TELEPHONE_NUMBER"),
(49, 54, "ZIPCODE"),
(55, 77, "STREET_ADDRESS"),
]
}),
(
"Troutville 24175 540-260-0797 2140 Maxwell Farm Road VA Virginia 434-825-5724"
, {
"entities":[
(0, 10, "CITY"),
(11, 16, "ZIPCODE"),
(17, 29, "TELEPHONE_NUMBER"),
(30, 52, "STREET_ADDRESS"),
(53, 55, "STATE"),
(56, 64, "STATE_FULL"),
(65, 77, "MOBILE_NUMBER"),
]
}),
(
"434-825-5724 24175 2140 Maxwell Farm Road Troutville VA Virginia 540-260-0797"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 41, "STREET_ADDRESS"),
(42, 52, "CITY"),
(53, 55, "STATE"),
(56, 64, "STATE_FULL"),
(65, 77, "TELEPHONE_NUMBER"),
]
}),
(
"VA Virginia 434-825-5724 Troutville 24175 2140 Maxwell Farm Road 540-260-0797"
, {
"entities":[
(0, 2, "STATE"),
(3, 11, "STATE_FULL"),
(12, 24, "MOBILE_NUMBER"),
(25, 35, "CITY"),
(36, 41, "ZIPCODE"),
(42, 64, "STREET_ADDRESS"),
(65, 77, "TELEPHONE_NUMBER"),
]
}),
(
"Troutville Virginia 2140 Maxwell Farm Road 434-825-5724 VA 24175 540-260-0797"
, {
"entities":[
(0, 10, "CITY"),
(11, 19, "STATE_FULL"),
(20, 42, "STREET_ADDRESS"),
(43, 55, "MOBILE_NUMBER"),
(56, 58, "STATE"),
(59, 64, "ZIPCODE"),
(65, 77, "TELEPHONE_NUMBER"),
]
}),
(
"24175 Troutville 540-260-0797 2140 Maxwell Farm Road VA 434-825-5724 Virginia"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 16, "CITY"),
(17, 29, "TELEPHONE_NUMBER"),
(30, 52, "STREET_ADDRESS"),
(53, 55, "STATE"),
(56, 68, "MOBILE_NUMBER"),
(69, 77, "STATE_FULL"),
]
}),
(
"West Virginia 2115 Kelly Drive WV 24701 304-922-1856 304-921-1549 Bluefield"
, {
"entities":[
(0, 13, "STATE_FULL"),
(14, 30, "STREET_ADDRESS"),
(31, 33, "STATE"),
(34, 39, "ZIPCODE"),
(40, 52, "TELEPHONE_NUMBER"),
(53, 65, "MOBILE_NUMBER"),
(66, 75, "CITY"),
]
}),
(
"304-922-1856 WV 24701 Bluefield 2115 Kelly Drive West Virginia 304-921-1549"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 15, "STATE"),
(16, 21, "ZIPCODE"),
(22, 31, "CITY"),
(32, 48, "STREET_ADDRESS"),
(49, 62, "STATE_FULL"),
(63, 75, "MOBILE_NUMBER"),
]
}),
(
"304-921-1549 Bluefield 2115 Kelly Drive 304-922-1856 24701 WV West Virginia"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 22, "CITY"),
(23, 39, "STREET_ADDRESS"),
(40, 52, "TELEPHONE_NUMBER"),
(53, 58, "ZIPCODE"),
(59, 61, "STATE"),
(62, 75, "STATE_FULL"),
]
}),
(
"West Virginia WV Bluefield 24701 304-922-1856 2115 Kelly Drive 304-921-1549"
, {
"entities":[
(0, 13, "STATE_FULL"),
(14, 16, "STATE"),
(17, 26, "CITY"),
(27, 32, "ZIPCODE"),
(33, 45, "TELEPHONE_NUMBER"),
(46, 62, "STREET_ADDRESS"),
(63, 75, "MOBILE_NUMBER"),
]
}),
(
"304-921-1549 2115 Kelly Drive 304-922-1856 WV West Virginia Bluefield 24701"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 29, "STREET_ADDRESS"),
(30, 42, "TELEPHONE_NUMBER"),
(43, 45, "STATE"),
(46, 59, "STATE_FULL"),
(60, 69, "CITY"),
(70, 75, "ZIPCODE"),
]
}),
(
"WV 2115 Kelly Drive Bluefield West Virginia 24701 304-922-1856 304-921-1549"
, {
"entities":[
(0, 2, "STATE"),
(3, 19, "STREET_ADDRESS"),
(20, 29, "CITY"),
(30, 43, "STATE_FULL"),
(44, 49, "ZIPCODE"),
(50, 62, "TELEPHONE_NUMBER"),
(63, 75, "MOBILE_NUMBER"),
]
}),
(
"24701 304-922-1856 Bluefield WV West Virginia 2115 Kelly Drive 304-921-1549"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "TELEPHONE_NUMBER"),
(19, 28, "CITY"),
(29, 31, "STATE"),
(32, 45, "STATE_FULL"),
(46, 62, "STREET_ADDRESS"),
(63, 75, "MOBILE_NUMBER"),
]
}),
(
"WV 2115 Kelly Drive Bluefield 304-921-1549 24701 304-922-1856 West Virginia"
, {
"entities":[
(0, 2, "STATE"),
(3, 19, "STREET_ADDRESS"),
(20, 29, "CITY"),
(30, 42, "MOBILE_NUMBER"),
(43, 48, "ZIPCODE"),
(49, 61, "TELEPHONE_NUMBER"),
(62, 75, "STATE_FULL"),
]
}),
(
"2115 Kelly Drive Bluefield 24701 WV West Virginia 304-921-1549 304-922-1856"
, {
"entities":[
(0, 16, "STREET_ADDRESS"),
(17, 26, "CITY"),
(27, 32, "ZIPCODE"),
(33, 35, "STATE"),
(36, 49, "STATE_FULL"),
(50, 62, "MOBILE_NUMBER"),
(63, 75, "TELEPHONE_NUMBER"),
]
}),
(
"Bluefield 2115 Kelly Drive 304-922-1856 304-921-1549 West Virginia WV 24701"
, {
"entities":[
(0, 9, "CITY"),
(10, 26, "STREET_ADDRESS"),
(27, 39, "TELEPHONE_NUMBER"),
(40, 52, "MOBILE_NUMBER"),
(53, 66, "STATE_FULL"),
(67, 69, "STATE"),
(70, 75, "ZIPCODE"),
]
}),
(
"1287 White Oak Drive Kansas City 816-678-1070 64108 816-682-9653 Missouri MO"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 32, "CITY"),
(33, 45, "MOBILE_NUMBER"),
(46, 51, "ZIPCODE"),
(52, 64, "TELEPHONE_NUMBER"),
(65, 73, "STATE_FULL"),
(74, 76, "STATE"),
]
}),
(
"Missouri 64108 816-678-1070 1287 White Oak Drive MO 816-682-9653 Kansas City"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 14, "ZIPCODE"),
(15, 27, "MOBILE_NUMBER"),
(28, 48, "STREET_ADDRESS"),
(49, 51, "STATE"),
(52, 64, "TELEPHONE_NUMBER"),
(65, 76, "CITY"),
]
}),
(
"816-682-9653 Kansas City 64108 Missouri 1287 White Oak Drive MO 816-678-1070"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 24, "CITY"),
(25, 30, "ZIPCODE"),
(31, 39, "STATE_FULL"),
(40, 60, "STREET_ADDRESS"),
(61, 63, "STATE"),
(64, 76, "MOBILE_NUMBER"),
]
}),
(
"64108 MO Kansas City 816-682-9653 Missouri 1287 White Oak Drive 816-678-1070"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 20, "CITY"),
(21, 33, "TELEPHONE_NUMBER"),
(34, 42, "STATE_FULL"),
(43, 63, "STREET_ADDRESS"),
(64, 76, "MOBILE_NUMBER"),
]
}),
(
"Kansas City 816-682-9653 MO 1287 White Oak Drive Missouri 64108 816-678-1070"
, {
"entities":[
(0, 11, "CITY"),
(12, 24, "TELEPHONE_NUMBER"),
(25, 27, "STATE"),
(28, 48, "STREET_ADDRESS"),
(49, 57, "STATE_FULL"),
(58, 63, "ZIPCODE"),
(64, 76, "MOBILE_NUMBER"),
]
}),
(
"Kansas City 64108 MO 1287 White Oak Drive 816-678-1070 Missouri 816-682-9653"
, {
"entities":[
(0, 11, "CITY"),
(12, 17, "ZIPCODE"),
(18, 20, "STATE"),
(21, 41, "STREET_ADDRESS"),
(42, 54, "MOBILE_NUMBER"),
(55, 63, "STATE_FULL"),
(64, 76, "TELEPHONE_NUMBER"),
]
}),
(
"Missouri 1287 White Oak Drive MO 816-678-1070 64108 816-682-9653 Kansas City"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 29, "STREET_ADDRESS"),
(30, 32, "STATE"),
(33, 45, "MOBILE_NUMBER"),
(46, 51, "ZIPCODE"),
(52, 64, "TELEPHONE_NUMBER"),
(65, 76, "CITY"),
]
}),
(
"816-678-1070 Missouri MO 64108 816-682-9653 Kansas City 1287 White Oak Drive"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 21, "STATE_FULL"),
(22, 24, "STATE"),
(25, 30, "ZIPCODE"),
(31, 43, "TELEPHONE_NUMBER"),
(44, 55, "CITY"),
(56, 76, "STREET_ADDRESS"),
]
}),
(
"Kansas City 816-678-1070 MO 816-682-9653 64108 Missouri 1287 White Oak Drive"
, {
"entities":[
(0, 11, "CITY"),
(12, 24, "MOBILE_NUMBER"),
(25, 27, "STATE"),
(28, 40, "TELEPHONE_NUMBER"),
(41, 46, "ZIPCODE"),
(47, 55, "STATE_FULL"),
(56, 76, "STREET_ADDRESS"),
]
}),
(
"MO Kansas City 64108 1287 White Oak Drive 816-678-1070 Missouri 816-682-9653"
, {
"entities":[
(0, 2, "STATE"),
(3, 14, "CITY"),
(15, 20, "ZIPCODE"),
(21, 41, "STREET_ADDRESS"),
(42, 54, "MOBILE_NUMBER"),
(55, 63, "STATE_FULL"),
(64, 76, "TELEPHONE_NUMBER"),
]
}),
(
"803-225-0342 Greenville SC South Carolina 29601 3740 Traction Street 864-538-3611"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 23, "CITY"),
(24, 26, "STATE"),
(27, 41, "STATE_FULL"),
(42, 47, "ZIPCODE"),
(48, 68, "STREET_ADDRESS"),
(69, 81, "TELEPHONE_NUMBER"),
]
}),
(
"South Carolina 3740 Traction Street 803-225-0342 SC 864-538-3611 29601 Greenville"
, {
"entities":[
(0, 14, "STATE_FULL"),
(15, 35, "STREET_ADDRESS"),
(36, 48, "MOBILE_NUMBER"),
(49, 51, "STATE"),
(52, 64, "TELEPHONE_NUMBER"),
(65, 70, "ZIPCODE"),
(71, 81, "CITY"),
]
}),
(
"Greenville 3740 Traction Street SC 29601 864-538-3611 South Carolina 803-225-0342"
, {
"entities":[
(0, 10, "CITY"),
(11, 31, "STREET_ADDRESS"),
(32, 34, "STATE"),
(35, 40, "ZIPCODE"),
(41, 53, "TELEPHONE_NUMBER"),
(54, 68, "STATE_FULL"),
(69, 81, "MOBILE_NUMBER"),
]
}),
(
"803-225-0342 3740 Traction Street 864-538-3611 Greenville SC 29601 South Carolina"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 33, "STREET_ADDRESS"),
(34, 46, "TELEPHONE_NUMBER"),
(47, 57, "CITY"),
(58, 60, "STATE"),
(61, 66, "ZIPCODE"),
(67, 81, "STATE_FULL"),
]
}),
(
"SC 29601 803-225-0342 South Carolina 3740 Traction Street Greenville 864-538-3611"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 21, "MOBILE_NUMBER"),
(22, 36, "STATE_FULL"),
(37, 57, "STREET_ADDRESS"),
(58, 68, "CITY"),
(69, 81, "TELEPHONE_NUMBER"),
]
}),
(
"3740 Traction Street SC 29601 803-225-0342 South Carolina Greenville 864-538-3611"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 23, "STATE"),
(24, 29, "ZIPCODE"),
(30, 42, "MOBILE_NUMBER"),
(43, 57, "STATE_FULL"),
(58, 68, "CITY"),
(69, 81, "TELEPHONE_NUMBER"),
]
}),
(
"3740 Traction Street South Carolina SC 864-538-3611 Greenville 29601 803-225-0342"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 35, "STATE_FULL"),
(36, 38, "STATE"),
(39, 51, "TELEPHONE_NUMBER"),
(52, 62, "CITY"),
(63, 68, "ZIPCODE"),
(69, 81, "MOBILE_NUMBER"),
]
}),
(
"864-538-3611 803-225-0342 SC 3740 Traction Street Greenville South Carolina 29601"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 25, "MOBILE_NUMBER"),
(26, 28, "STATE"),
(29, 49, "STREET_ADDRESS"),
(50, 60, "CITY"),
(61, 75, "STATE_FULL"),
(76, 81, "ZIPCODE"),
]
}),
(
"Greenville 864-538-3611 29601 3740 Traction Street SC South Carolina 803-225-0342"
, {
"entities":[
(0, 10, "CITY"),
(11, 23, "TELEPHONE_NUMBER"),
(24, 29, "ZIPCODE"),
(30, 50, "STREET_ADDRESS"),
(51, 53, "STATE"),
(54, 68, "STATE_FULL"),
(69, 81, "MOBILE_NUMBER"),
]
}),
(
"Greenville 864-538-3611 SC 29601 South Carolina 3740 Traction Street 803-225-0342"
, {
"entities":[
(0, 10, "CITY"),
(11, 23, "TELEPHONE_NUMBER"),
(24, 26, "STATE"),
(27, 32, "ZIPCODE"),
(33, 47, "STATE_FULL"),
(48, 68, "STREET_ADDRESS"),
(69, 81, "MOBILE_NUMBER"),
]
}),
(
"WV 304-389-9980 West Virginia Mannington 26582 304-986-3045 768 Agriculture Lane"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "MOBILE_NUMBER"),
(16, 29, "STATE_FULL"),
(30, 40, "CITY"),
(41, 46, "ZIPCODE"),
(47, 59, "TELEPHONE_NUMBER"),
(60, 80, "STREET_ADDRESS"),
]
}),
(
"768 Agriculture Lane WV 304-389-9980 West Virginia 26582 Mannington 304-986-3045"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 23, "STATE"),
(24, 36, "MOBILE_NUMBER"),
(37, 50, "STATE_FULL"),
(51, 56, "ZIPCODE"),
(57, 67, "CITY"),
(68, 80, "TELEPHONE_NUMBER"),
]
}),
(
"304-986-3045 304-389-9980 Mannington 768 Agriculture Lane West Virginia 26582 WV"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 25, "MOBILE_NUMBER"),
(26, 36, "CITY"),
(37, 57, "STREET_ADDRESS"),
(58, 71, "STATE_FULL"),
(72, 77, "ZIPCODE"),
(78, 80, "STATE"),
]
}),
(
"26582 Mannington WV West Virginia 304-986-3045 304-389-9980 768 Agriculture Lane"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 16, "CITY"),
(17, 19, "STATE"),
(20, 33, "STATE_FULL"),
(34, 46, "TELEPHONE_NUMBER"),
(47, 59, "MOBILE_NUMBER"),
(60, 80, "STREET_ADDRESS"),
]
}),
(
"768 Agriculture Lane 304-986-3045 West Virginia WV 304-389-9980 26582 Mannington"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 33, "TELEPHONE_NUMBER"),
(34, 47, "STATE_FULL"),
(48, 50, "STATE"),
(51, 63, "MOBILE_NUMBER"),
(64, 69, "ZIPCODE"),
(70, 80, "CITY"),
]
}),
(
"West Virginia 26582 768 Agriculture Lane WV 304-986-3045 304-389-9980 Mannington"
, {
"entities":[
(0, 13, "STATE_FULL"),
(14, 19, "ZIPCODE"),
(20, 40, "STREET_ADDRESS"),
(41, 43, "STATE"),
(44, 56, "TELEPHONE_NUMBER"),
(57, 69, "MOBILE_NUMBER"),
(70, 80, "CITY"),
]
}),
(
"304-986-3045 304-389-9980 WV West Virginia Mannington 26582 768 Agriculture Lane"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 25, "MOBILE_NUMBER"),
(26, 28, "STATE"),
(29, 42, "STATE_FULL"),
(43, 53, "CITY"),
(54, 59, "ZIPCODE"),
(60, 80, "STREET_ADDRESS"),
]
}),
(
"304-986-3045 304-389-9980 26582 Mannington West Virginia WV 768 Agriculture Lane"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 25, "MOBILE_NUMBER"),
(26, 31, "ZIPCODE"),
(32, 42, "CITY"),
(43, 56, "STATE_FULL"),
(57, 59, "STATE"),
(60, 80, "STREET_ADDRESS"),
]
}),
(
"768 Agriculture Lane 304-986-3045 WV Mannington West Virginia 26582 304-389-9980"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 33, "TELEPHONE_NUMBER"),
(34, 36, "STATE"),
(37, 47, "CITY"),
(48, 61, "STATE_FULL"),
(62, 67, "ZIPCODE"),
(68, 80, "MOBILE_NUMBER"),
]
}),
(
"304-986-3045 304-389-9980 26582 768 Agriculture Lane Mannington WV West Virginia"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 25, "MOBILE_NUMBER"),
(26, 31, "ZIPCODE"),
(32, 52, "STREET_ADDRESS"),
(53, 63, "CITY"),
(64, 66, "STATE"),
(67, 80, "STATE_FULL"),
]
}),
(
"4431 Waterview Lane 505-428-6408 505-230-9911 New Mexico Santa Fe NM 87501"
, {
"entities":[
(0, 19, "STREET_ADDRESS"),
(20, 32, "TELEPHONE_NUMBER"),
(33, 45, "MOBILE_NUMBER"),
(46, 56, "STATE_FULL"),
(57, 65, "CITY"),
(66, 68, "STATE"),
(69, 74, "ZIPCODE"),
]
}),
(
"NM 4431 Waterview Lane New Mexico 505-428-6408 Santa Fe 87501 505-230-9911"
, {
"entities":[
(0, 2, "STATE"),
(3, 22, "STREET_ADDRESS"),
(23, 33, "STATE_FULL"),
(34, 46, "TELEPHONE_NUMBER"),
(47, 55, "CITY"),
(56, 61, "ZIPCODE"),
(62, 74, "MOBILE_NUMBER"),
]
}),
(
"87501 NM 4431 Waterview Lane 505-230-9911 New Mexico 505-428-6408 Santa Fe"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 28, "STREET_ADDRESS"),
(29, 41, "MOBILE_NUMBER"),
(42, 52, "STATE_FULL"),
(53, 65, "TELEPHONE_NUMBER"),
(66, 74, "CITY"),
]
}),
(
"505-428-6408 4431 Waterview Lane 505-230-9911 New Mexico Santa Fe 87501 NM"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 32, "STREET_ADDRESS"),
(33, 45, "MOBILE_NUMBER"),
(46, 56, "STATE_FULL"),
(57, 65, "CITY"),
(66, 71, "ZIPCODE"),
(72, 74, "STATE"),
]
}),
(
"505-428-6408 87501 4431 Waterview Lane 505-230-9911 New Mexico Santa Fe NM"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 38, "STREET_ADDRESS"),
(39, 51, "MOBILE_NUMBER"),
(52, 62, "STATE_FULL"),
(63, 71, "CITY"),
(72, 74, "STATE"),
]
}),
(
"505-428-6408 4431 Waterview Lane 87501 New Mexico NM Santa Fe 505-230-9911"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 32, "STREET_ADDRESS"),
(33, 38, "ZIPCODE"),
(39, 49, "STATE_FULL"),
(50, 52, "STATE"),
(53, 61, "CITY"),
(62, 74, "MOBILE_NUMBER"),
]
}),
(
"505-230-9911 87501 Santa Fe 4431 Waterview Lane 505-428-6408 New Mexico NM"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 27, "CITY"),
(28, 47, "STREET_ADDRESS"),
(48, 60, "TELEPHONE_NUMBER"),
(61, 71, "STATE_FULL"),
(72, 74, "STATE"),
]
}),
(
"505-230-9911 NM 87501 New Mexico 505-428-6408 Santa Fe 4431 Waterview Lane"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 15, "STATE"),
(16, 21, "ZIPCODE"),
(22, 32, "STATE_FULL"),
(33, 45, "TELEPHONE_NUMBER"),
(46, 54, "CITY"),
(55, 74, "STREET_ADDRESS"),
]
}),
(
"NM Santa Fe 505-230-9911 New Mexico 87501 4431 Waterview Lane 505-428-6408"
, {
"entities":[
(0, 2, "STATE"),
(3, 11, "CITY"),
(12, 24, "MOBILE_NUMBER"),
(25, 35, "STATE_FULL"),
(36, 41, "ZIPCODE"),
(42, 61, "STREET_ADDRESS"),
(62, 74, "TELEPHONE_NUMBER"),
]
}),
(
"4431 Waterview Lane New Mexico 505-230-9911 Santa Fe 505-428-6408 87501 NM"
, {
"entities":[
(0, 19, "STREET_ADDRESS"),
(20, 30, "STATE_FULL"),
(31, 43, "MOBILE_NUMBER"),
(44, 52, "CITY"),
(53, 65, "TELEPHONE_NUMBER"),
(66, 71, "ZIPCODE"),
(72, 74, "STATE"),
]
}),
(
"15201 PA Pittsburgh Pennsylvania 412-529-5421 4056 Chandler Hollow Road 412-426-5109"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 19, "CITY"),
(20, 32, "STATE_FULL"),
(33, 45, "MOBILE_NUMBER"),
(46, 71, "STREET_ADDRESS"),
(72, 84, "TELEPHONE_NUMBER"),
]
}),
(
"4056 Chandler Hollow Road 412-529-5421 PA Pittsburgh 15201 412-426-5109 Pennsylvania"
, {
"entities":[
(0, 25, "STREET_ADDRESS"),
(26, 38, "MOBILE_NUMBER"),
(39, 41, "STATE"),
(42, 52, "CITY"),
(53, 58, "ZIPCODE"),
(59, 71, "TELEPHONE_NUMBER"),
(72, 84, "STATE_FULL"),
]
}),
(
"15201 Pittsburgh PA 412-426-5109 Pennsylvania 4056 Chandler Hollow Road 412-529-5421"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 16, "CITY"),
(17, 19, "STATE"),
(20, 32, "TELEPHONE_NUMBER"),
(33, 45, "STATE_FULL"),
(46, 71, "STREET_ADDRESS"),
(72, 84, "MOBILE_NUMBER"),
]
}),
(
"412-426-5109 15201 Pittsburgh 4056 Chandler Hollow Road PA 412-529-5421 Pennsylvania"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 29, "CITY"),
(30, 55, "STREET_ADDRESS"),
(56, 58, "STATE"),
(59, 71, "MOBILE_NUMBER"),
(72, 84, "STATE_FULL"),
]
}),
(
"Pittsburgh 4056 Chandler Hollow Road 412-426-5109 Pennsylvania PA 15201 412-529-5421"
, {
"entities":[
(0, 10, "CITY"),
(11, 36, "STREET_ADDRESS"),
(37, 49, "TELEPHONE_NUMBER"),
(50, 62, "STATE_FULL"),
(63, 65, "STATE"),
(66, 71, "ZIPCODE"),
(72, 84, "MOBILE_NUMBER"),
]
}),
(
"Pennsylvania Pittsburgh 412-426-5109 PA 4056 Chandler Hollow Road 412-529-5421 15201"
, {
"entities":[
(0, 12, "STATE_FULL"),
(13, 23, "CITY"),
(24, 36, "TELEPHONE_NUMBER"),
(37, 39, "STATE"),
(40, 65, "STREET_ADDRESS"),
(66, 78, "MOBILE_NUMBER"),
(79, 84, "ZIPCODE"),
]
}),
(
"412-529-5421 Pittsburgh 412-426-5109 4056 Chandler Hollow Road PA Pennsylvania 15201"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 23, "CITY"),
(24, 36, "TELEPHONE_NUMBER"),
(37, 62, "STREET_ADDRESS"),
(63, 65, "STATE"),
(66, 78, "STATE_FULL"),
(79, 84, "ZIPCODE"),
]
}),
(
"412-529-5421 4056 Chandler Hollow Road 412-426-5109 15201 PA Pennsylvania Pittsburgh"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 38, "STREET_ADDRESS"),
(39, 51, "TELEPHONE_NUMBER"),
(52, 57, "ZIPCODE"),
(58, 60, "STATE"),
(61, 73, "STATE_FULL"),
(74, 84, "CITY"),
]
}),
(
"4056 Chandler Hollow Road 15201 Pittsburgh PA 412-426-5109 412-529-5421 Pennsylvania"
, {
"entities":[
(0, 25, "STREET_ADDRESS"),
(26, 31, "ZIPCODE"),
(32, 42, "CITY"),
(43, 45, "STATE"),
(46, 58, "TELEPHONE_NUMBER"),
(59, 71, "MOBILE_NUMBER"),
(72, 84, "STATE_FULL"),
]
}),
(
"PA 412-426-5109 4056 Chandler Hollow Road 15201 Pittsburgh Pennsylvania 412-529-5421"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "TELEPHONE_NUMBER"),
(16, 41, "STREET_ADDRESS"),
(42, 47, "ZIPCODE"),
(48, 58, "CITY"),
(59, 71, "STATE_FULL"),
(72, 84, "MOBILE_NUMBER"),
]
}),
(
"Knoxville 865-675-0184 865-300-2343 Tennessee 1290 Berkshire Circle TN 37933"
, {
"entities":[
(0, 9, "CITY"),
(10, 22, "TELEPHONE_NUMBER"),
(23, 35, "MOBILE_NUMBER"),
(36, 45, "STATE_FULL"),
(46, 67, "STREET_ADDRESS"),
(68, 70, "STATE"),
(71, 76, "ZIPCODE"),
]
}),
(
"865-675-0184 TN Knoxville 37933 1290 Berkshire Circle 865-300-2343 Tennessee"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 15, "STATE"),
(16, 25, "CITY"),
(26, 31, "ZIPCODE"),
(32, 53, "STREET_ADDRESS"),
(54, 66, "MOBILE_NUMBER"),
(67, 76, "STATE_FULL"),
]
}),
(
"Knoxville Tennessee 1290 Berkshire Circle 865-300-2343 TN 37933 865-675-0184"
, {
"entities":[
(0, 9, "CITY"),
(10, 19, "STATE_FULL"),
(20, 41, "STREET_ADDRESS"),
(42, 54, "MOBILE_NUMBER"),
(55, 57, "STATE"),
(58, 63, "ZIPCODE"),
(64, 76, "TELEPHONE_NUMBER"),
]
}),
(
"37933 Tennessee 865-675-0184 Knoxville 865-300-2343 TN 1290 Berkshire Circle"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 15, "STATE_FULL"),
(16, 28, "TELEPHONE_NUMBER"),
(29, 38, "CITY"),
(39, 51, "MOBILE_NUMBER"),
(52, 54, "STATE"),
(55, 76, "STREET_ADDRESS"),
]
}),
(
"865-675-0184 37933 Tennessee Knoxville 1290 Berkshire Circle 865-300-2343 TN"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 28, "STATE_FULL"),
(29, 38, "CITY"),
(39, 60, "STREET_ADDRESS"),
(61, 73, "MOBILE_NUMBER"),
(74, 76, "STATE"),
]
}),
(
"TN Knoxville Tennessee 1290 Berkshire Circle 865-300-2343 37933 865-675-0184"
, {
"entities":[
(0, 2, "STATE"),
(3, 12, "CITY"),
(13, 22, "STATE_FULL"),
(23, 44, "STREET_ADDRESS"),
(45, 57, "MOBILE_NUMBER"),
(58, 63, "ZIPCODE"),
(64, 76, "TELEPHONE_NUMBER"),
]
}),
(
"37933 865-675-0184 Knoxville TN 1290 Berkshire Circle 865-300-2343 Tennessee"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "TELEPHONE_NUMBER"),
(19, 28, "CITY"),
(29, 31, "STATE"),
(32, 53, "STREET_ADDRESS"),
(54, 66, "MOBILE_NUMBER"),
(67, 76, "STATE_FULL"),
]
}),
(
"Tennessee 1290 Berkshire Circle 37933 Knoxville TN 865-300-2343 865-675-0184"
, {
"entities":[
(0, 9, "STATE_FULL"),
(10, 31, "STREET_ADDRESS"),
(32, 37, "ZIPCODE"),
(38, 47, "CITY"),
(48, 50, "STATE"),
(51, 63, "MOBILE_NUMBER"),
(64, 76, "TELEPHONE_NUMBER"),
]
}),
(
"865-675-0184 1290 Berkshire Circle Tennessee Knoxville TN 865-300-2343 37933"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 34, "STREET_ADDRESS"),
(35, 44, "STATE_FULL"),
(45, 54, "CITY"),
(55, 57, "STATE"),
(58, 70, "MOBILE_NUMBER"),
(71, 76, "ZIPCODE"),
]
}),
(
"865-675-0184 1290 Berkshire Circle TN Knoxville 37933 865-300-2343 Tennessee"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 34, "STREET_ADDRESS"),
(35, 37, "STATE"),
(38, 47, "CITY"),
(48, 53, "ZIPCODE"),
(54, 66, "MOBILE_NUMBER"),
(67, 76, "STATE_FULL"),
]
}),
(
"503-823-7507 Portland 503-730-4260 611 Heron Way OR Oregon 97205"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 21, "CITY"),
(22, 34, "MOBILE_NUMBER"),
(35, 48, "STREET_ADDRESS"),
(49, 51, "STATE"),
(52, 58, "STATE_FULL"),
(59, 64, "ZIPCODE"),
]
}),
(
"97205 503-823-7507 503-730-4260 Portland OR 611 Heron Way Oregon"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "TELEPHONE_NUMBER"),
(19, 31, "MOBILE_NUMBER"),
(32, 40, "CITY"),
(41, 43, "STATE"),
(44, 57, "STREET_ADDRESS"),
(58, 64, "STATE_FULL"),
]
}),
(
"Portland 97205 503-730-4260 503-823-7507 OR 611 Heron Way Oregon"
, {
"entities":[
(0, 8, "CITY"),
(9, 14, "ZIPCODE"),
(15, 27, "MOBILE_NUMBER"),
(28, 40, "TELEPHONE_NUMBER"),
(41, 43, "STATE"),
(44, 57, "STREET_ADDRESS"),
(58, 64, "STATE_FULL"),
]
}),
(
"Portland Oregon 503-730-4260 OR 97205 503-823-7507 611 Heron Way"
, {
"entities":[
(0, 8, "CITY"),
(9, 15, "STATE_FULL"),
(16, 28, "MOBILE_NUMBER"),
(29, 31, "STATE"),
(32, 37, "ZIPCODE"),
(38, 50, "TELEPHONE_NUMBER"),
(51, 64, "STREET_ADDRESS"),
]
}),
(
"Portland 503-730-4260 OR Oregon 611 Heron Way 97205 503-823-7507"
, {
"entities":[
(0, 8, "CITY"),
(9, 21, "MOBILE_NUMBER"),
(22, 24, "STATE"),
(25, 31, "STATE_FULL"),
(32, 45, "STREET_ADDRESS"),
(46, 51, "ZIPCODE"),
(52, 64, "TELEPHONE_NUMBER"),
]
}),
(
"503-730-4260 OR Portland 611 Heron Way 503-823-7507 Oregon 97205"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 15, "STATE"),
(16, 24, "CITY"),
(25, 38, "STREET_ADDRESS"),
(39, 51, "TELEPHONE_NUMBER"),
(52, 58, "STATE_FULL"),
(59, 64, "ZIPCODE"),
]
}),
(
"97205 503-730-4260 Oregon 611 Heron Way 503-823-7507 Portland OR"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "MOBILE_NUMBER"),
(19, 25, "STATE_FULL"),
(26, 39, "STREET_ADDRESS"),
(40, 52, "TELEPHONE_NUMBER"),
(53, 61, "CITY"),
(62, 64, "STATE"),
]
}),
(
"97205 611 Heron Way Oregon 503-730-4260 Portland 503-823-7507 OR"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 19, "STREET_ADDRESS"),
(20, 26, "STATE_FULL"),
(27, 39, "MOBILE_NUMBER"),
(40, 48, "CITY"),
(49, 61, "TELEPHONE_NUMBER"),
(62, 64, "STATE"),
]
}),
(
"Oregon 503-823-7507 611 Heron Way OR 97205 503-730-4260 Portland"
, {
"entities":[
(0, 6, "STATE_FULL"),
(7, 19, "TELEPHONE_NUMBER"),
(20, 33, "STREET_ADDRESS"),
(34, 36, "STATE"),
(37, 42, "ZIPCODE"),
(43, 55, "MOBILE_NUMBER"),
(56, 64, "CITY"),
]
}),
(
"97205 503-823-7507 OR 611 Heron Way 503-730-4260 Portland Oregon"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "TELEPHONE_NUMBER"),
(19, 21, "STATE"),
(22, 35, "STREET_ADDRESS"),
(36, 48, "MOBILE_NUMBER"),
(49, 57, "CITY"),
(58, 64, "STATE_FULL"),
]
}),
(
"New Hampshire 603-873-0791 Manchester 03103 1430 Peck Street NH 603-639-6382"
, {
"entities":[
(0, 13, "STATE_FULL"),
(14, 26, "TELEPHONE_NUMBER"),
(27, 37, "CITY"),
(38, 43, "ZIPCODE"),
(44, 60, "STREET_ADDRESS"),
(61, 63, "STATE"),
(64, 76, "MOBILE_NUMBER"),
]
}),
(
"1430 Peck Street 603-639-6382 Manchester New Hampshire 03103 NH 603-873-0791"
, {
"entities":[
(0, 16, "STREET_ADDRESS"),
(17, 29, "MOBILE_NUMBER"),
(30, 40, "CITY"),
(41, 54, "STATE_FULL"),
(55, 60, "ZIPCODE"),
(61, 63, "STATE"),
(64, 76, "TELEPHONE_NUMBER"),
]
}),
(
"603-639-6382 603-873-0791 Manchester 03103 NH 1430 Peck Street New Hampshire"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 25, "TELEPHONE_NUMBER"),
(26, 36, "CITY"),
(37, 42, "ZIPCODE"),
(43, 45, "STATE"),
(46, 62, "STREET_ADDRESS"),
(63, 76, "STATE_FULL"),
]
}),
(
"603-873-0791 03103 Manchester New Hampshire 603-639-6382 1430 Peck Street NH"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 29, "CITY"),
(30, 43, "STATE_FULL"),
(44, 56, "MOBILE_NUMBER"),
(57, 73, "STREET_ADDRESS"),
(74, 76, "STATE"),
]
}),
(
"603-873-0791 New Hampshire 603-639-6382 Manchester NH 03103 1430 Peck Street"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 26, "STATE_FULL"),
(27, 39, "MOBILE_NUMBER"),
(40, 50, "CITY"),
(51, 53, "STATE"),
(54, 59, "ZIPCODE"),
(60, 76, "STREET_ADDRESS"),
]
}),
(
"03103 603-873-0791 603-639-6382 NH Manchester New Hampshire 1430 Peck Street"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "TELEPHONE_NUMBER"),
(19, 31, "MOBILE_NUMBER"),
(32, 34, "STATE"),
(35, 45, "CITY"),
(46, 59, "STATE_FULL"),
(60, 76, "STREET_ADDRESS"),
]
}),
(
"Manchester 603-639-6382 New Hampshire NH 603-873-0791 03103 1430 Peck Street"
, {
"entities":[
(0, 10, "CITY"),
(11, 23, "MOBILE_NUMBER"),
(24, 37, "STATE_FULL"),
(38, 40, "STATE"),
(41, 53, "TELEPHONE_NUMBER"),
(54, 59, "ZIPCODE"),
(60, 76, "STREET_ADDRESS"),
]
}),
(
"03103 New Hampshire 603-639-6382 1430 Peck Street 603-873-0791 Manchester NH"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 19, "STATE_FULL"),
(20, 32, "MOBILE_NUMBER"),
(33, 49, "STREET_ADDRESS"),
(50, 62, "TELEPHONE_NUMBER"),
(63, 73, "CITY"),
(74, 76, "STATE"),
]
}),
(
"603-639-6382 Manchester 1430 Peck Street 603-873-0791 New Hampshire NH 03103"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 23, "CITY"),
(24, 40, "STREET_ADDRESS"),
(41, 53, "TELEPHONE_NUMBER"),
(54, 67, "STATE_FULL"),
(68, 70, "STATE"),
(71, 76, "ZIPCODE"),
]
}),
(
"New Hampshire 03103 1430 Peck Street 603-639-6382 NH Manchester 603-873-0791"
, {
"entities":[
(0, 13, "STATE_FULL"),
(14, 19, "ZIPCODE"),
(20, 36, "STREET_ADDRESS"),
(37, 49, "MOBILE_NUMBER"),
(50, 52, "STATE"),
(53, 63, "CITY"),
(64, 76, "TELEPHONE_NUMBER"),
]
}),
(
"808-273-6428 808-668-5836 Waianae 96792 2280 Indiana Avenue Hawaii HI"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 25, "TELEPHONE_NUMBER"),
(26, 33, "CITY"),
(34, 39, "ZIPCODE"),
(40, 59, "STREET_ADDRESS"),
(60, 66, "STATE_FULL"),
(67, 69, "STATE"),
]
}),
(
"HI Hawaii 2280 Indiana Avenue 808-273-6428 96792 Waianae 808-668-5836"
, {
"entities":[
(0, 2, "STATE"),
(3, 9, "STATE_FULL"),
(10, 29, "STREET_ADDRESS"),
(30, 42, "MOBILE_NUMBER"),
(43, 48, "ZIPCODE"),
(49, 56, "CITY"),
(57, 69, "TELEPHONE_NUMBER"),
]
}),
(
"Waianae 808-273-6428 96792 2280 Indiana Avenue 808-668-5836 HI Hawaii"
, {
"entities":[
(0, 7, "CITY"),
(8, 20, "MOBILE_NUMBER"),
(21, 26, "ZIPCODE"),
(27, 46, "STREET_ADDRESS"),
(47, 59, "TELEPHONE_NUMBER"),
(60, 62, "STATE"),
(63, 69, "STATE_FULL"),
]
}),
(
"Waianae Hawaii 808-273-6428 HI 2280 Indiana Avenue 96792 808-668-5836"
, {
"entities":[
(0, 7, "CITY"),
(8, 14, "STATE_FULL"),
(15, 27, "MOBILE_NUMBER"),
(28, 30, "STATE"),
(31, 50, "STREET_ADDRESS"),
(51, 56, "ZIPCODE"),
(57, 69, "TELEPHONE_NUMBER"),
]
}),
(
"HI 96792 808-668-5836 Hawaii Waianae 2280 Indiana Avenue 808-273-6428"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 21, "TELEPHONE_NUMBER"),
(22, 28, "STATE_FULL"),
(29, 36, "CITY"),
(37, 56, "STREET_ADDRESS"),
(57, 69, "MOBILE_NUMBER"),
]
}),
(
"2280 Indiana Avenue Waianae 808-273-6428 96792 Hawaii 808-668-5836 HI"
, {
"entities":[
(0, 19, "STREET_ADDRESS"),
(20, 27, "CITY"),
(28, 40, "MOBILE_NUMBER"),
(41, 46, "ZIPCODE"),
(47, 53, "STATE_FULL"),
(54, 66, "TELEPHONE_NUMBER"),
(67, 69, "STATE"),
]
}),
(
"Waianae 96792 808-668-5836 Hawaii 2280 Indiana Avenue 808-273-6428 HI"
, {
"entities":[
(0, 7, "CITY"),
(8, 13, "ZIPCODE"),
(14, 26, "TELEPHONE_NUMBER"),
(27, 33, "STATE_FULL"),
(34, 53, "STREET_ADDRESS"),
(54, 66, "MOBILE_NUMBER"),
(67, 69, "STATE"),
]
}),
(
"808-273-6428 808-668-5836 Waianae Hawaii 2280 Indiana Avenue 96792 HI"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 25, "TELEPHONE_NUMBER"),
(26, 33, "CITY"),
(34, 40, "STATE_FULL"),
(41, 60, "STREET_ADDRESS"),
(61, 66, "ZIPCODE"),
(67, 69, "STATE"),
]
}),
(
"Hawaii 96792 808-668-5836 Waianae HI 2280 Indiana Avenue 808-273-6428"
, {
"entities":[
(0, 6, "STATE_FULL"),
(7, 12, "ZIPCODE"),
(13, 25, "TELEPHONE_NUMBER"),
(26, 33, "CITY"),
(34, 36, "STATE"),
(37, 56, "STREET_ADDRESS"),
(57, 69, "MOBILE_NUMBER"),
]
}),
(
"808-273-6428 Hawaii 808-668-5836 96792 HI Waianae 2280 Indiana Avenue"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 19, "STATE_FULL"),
(20, 32, "TELEPHONE_NUMBER"),
(33, 38, "ZIPCODE"),
(39, 41, "STATE"),
(42, 49, "CITY"),
(50, 69, "STREET_ADDRESS"),
]
}),
(
"231-592-3557 Michigan MI 49307 3074 Rubaiyat Road 989-203-9347 Big Rapids"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 21, "STATE_FULL"),
(22, 24, "STATE"),
(25, 30, "ZIPCODE"),
(31, 49, "STREET_ADDRESS"),
(50, 62, "MOBILE_NUMBER"),
(63, 73, "CITY"),
]
}),
(
"3074 Rubaiyat Road MI Big Rapids 231-592-3557 49307 989-203-9347 Michigan"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 21, "STATE"),
(22, 32, "CITY"),
(33, 45, "TELEPHONE_NUMBER"),
(46, 51, "ZIPCODE"),
(52, 64, "MOBILE_NUMBER"),
(65, 73, "STATE_FULL"),
]
}),
(
"Big Rapids Michigan 3074 Rubaiyat Road 231-592-3557 MI 49307 989-203-9347"
, {
"entities":[
(0, 10, "CITY"),
(11, 19, "STATE_FULL"),
(20, 38, "STREET_ADDRESS"),
(39, 51, "TELEPHONE_NUMBER"),
(52, 54, "STATE"),
(55, 60, "ZIPCODE"),
(61, 73, "MOBILE_NUMBER"),
]
}),
(
"989-203-9347 49307 MI Michigan 3074 Rubaiyat Road 231-592-3557 Big Rapids"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 21, "STATE"),
(22, 30, "STATE_FULL"),
(31, 49, "STREET_ADDRESS"),
(50, 62, "TELEPHONE_NUMBER"),
(63, 73, "CITY"),
]
}),
(
"MI 3074 Rubaiyat Road Michigan 989-203-9347 231-592-3557 49307 Big Rapids"
, {
"entities":[
(0, 2, "STATE"),
(3, 21, "STREET_ADDRESS"),
(22, 30, "STATE_FULL"),
(31, 43, "MOBILE_NUMBER"),
(44, 56, "TELEPHONE_NUMBER"),
(57, 62, "ZIPCODE"),
(63, 73, "CITY"),
]
}),
(
"989-203-9347 Big Rapids 3074 Rubaiyat Road 231-592-3557 49307 MI Michigan"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 23, "CITY"),
(24, 42, "STREET_ADDRESS"),
(43, 55, "TELEPHONE_NUMBER"),
(56, 61, "ZIPCODE"),
(62, 64, "STATE"),
(65, 73, "STATE_FULL"),
]
}),
(
"3074 Rubaiyat Road MI 49307 Michigan 231-592-3557 Big Rapids 989-203-9347"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 21, "STATE"),
(22, 27, "ZIPCODE"),
(28, 36, "STATE_FULL"),
(37, 49, "TELEPHONE_NUMBER"),
(50, 60, "CITY"),
(61, 73, "MOBILE_NUMBER"),
]
}),
(
"Big Rapids 231-592-3557 MI 49307 989-203-9347 3074 Rubaiyat Road Michigan"
, {
"entities":[
(0, 10, "CITY"),
(11, 23, "TELEPHONE_NUMBER"),
(24, 26, "STATE"),
(27, 32, "ZIPCODE"),
(33, 45, "MOBILE_NUMBER"),
(46, 64, "STREET_ADDRESS"),
(65, 73, "STATE_FULL"),
]
}),
(
"MI 231-592-3557 Big Rapids 989-203-9347 49307 3074 Rubaiyat Road Michigan"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "TELEPHONE_NUMBER"),
(16, 26, "CITY"),
(27, 39, "MOBILE_NUMBER"),
(40, 45, "ZIPCODE"),
(46, 64, "STREET_ADDRESS"),
(65, 73, "STATE_FULL"),
]
}),
(
"3074 Rubaiyat Road Michigan 49307 231-592-3557 Big Rapids 989-203-9347 MI"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 27, "STATE_FULL"),
(28, 33, "ZIPCODE"),
(34, 46, "TELEPHONE_NUMBER"),
(47, 57, "CITY"),
(58, 70, "MOBILE_NUMBER"),
(71, 73, "STATE"),
]
}),
(
"39213 MS Mississippi 662-213-6621 2904 Oxford Court 601-201-8443 Jackson"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 20, "STATE_FULL"),
(21, 33, "TELEPHONE_NUMBER"),
(34, 51, "STREET_ADDRESS"),
(52, 64, "MOBILE_NUMBER"),
(65, 72, "CITY"),
]
}),
(
"601-201-8443 MS 39213 2904 Oxford Court Jackson Mississippi 662-213-6621"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 15, "STATE"),
(16, 21, "ZIPCODE"),
(22, 39, "STREET_ADDRESS"),
(40, 47, "CITY"),
(48, 59, "STATE_FULL"),
(60, 72, "TELEPHONE_NUMBER"),
]
}),
(
"39213 Mississippi Jackson MS 662-213-6621 2904 Oxford Court 601-201-8443"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 17, "STATE_FULL"),
(18, 25, "CITY"),
(26, 28, "STATE"),
(29, 41, "TELEPHONE_NUMBER"),
(42, 59, "STREET_ADDRESS"),
(60, 72, "MOBILE_NUMBER"),
]
}),
(
"MS Mississippi 662-213-6621 Jackson 39213 2904 Oxford Court 601-201-8443"
, {
"entities":[
(0, 2, "STATE"),
(3, 14, "STATE_FULL"),
(15, 27, "TELEPHONE_NUMBER"),
(28, 35, "CITY"),
(36, 41, "ZIPCODE"),
(42, 59, "STREET_ADDRESS"),
(60, 72, "MOBILE_NUMBER"),
]
}),
(
"Mississippi 662-213-6621 39213 Jackson 2904 Oxford Court 601-201-8443 MS"
, {
"entities":[
(0, 11, "STATE_FULL"),
(12, 24, "TELEPHONE_NUMBER"),
(25, 30, "ZIPCODE"),
(31, 38, "CITY"),
(39, 56, "STREET_ADDRESS"),
(57, 69, "MOBILE_NUMBER"),
(70, 72, "STATE"),
]
}),
(
"MS 2904 Oxford Court 601-201-8443 Mississippi Jackson 39213 662-213-6621"
, {
"entities":[
(0, 2, "STATE"),
(3, 20, "STREET_ADDRESS"),
(21, 33, "MOBILE_NUMBER"),
(34, 45, "STATE_FULL"),
(46, 53, "CITY"),
(54, 59, "ZIPCODE"),
(60, 72, "TELEPHONE_NUMBER"),
]
}),
(
"Jackson 601-201-8443 2904 Oxford Court MS 39213 662-213-6621 Mississippi"
, {
"entities":[
(0, 7, "CITY"),
(8, 20, "MOBILE_NUMBER"),
(21, 38, "STREET_ADDRESS"),
(39, 41, "STATE"),
(42, 47, "ZIPCODE"),
(48, 60, "TELEPHONE_NUMBER"),
(61, 72, "STATE_FULL"),
]
}),
(
"662-213-6621 601-201-8443 2904 Oxford Court MS 39213 Mississippi Jackson"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 25, "MOBILE_NUMBER"),
(26, 43, "STREET_ADDRESS"),
(44, 46, "STATE"),
(47, 52, "ZIPCODE"),
(53, 64, "STATE_FULL"),
(65, 72, "CITY"),
]
}),
(
"601-201-8443 39213 Mississippi 2904 Oxford Court 662-213-6621 MS Jackson"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 30, "STATE_FULL"),
(31, 48, "STREET_ADDRESS"),
(49, 61, "TELEPHONE_NUMBER"),
(62, 64, "STATE"),
(65, 72, "CITY"),
]
}),
(
"601-201-8443 Jackson 39213 662-213-6621 Mississippi 2904 Oxford Court MS"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 20, "CITY"),
(21, 26, "ZIPCODE"),
(27, 39, "TELEPHONE_NUMBER"),
(40, 51, "STATE_FULL"),
(52, 69, "STREET_ADDRESS"),
(70, 72, "STATE"),
]
}),
(
"MT Gardiner 406-848-3131 59030 Montana 4839 Coolidge Street 406-230-2290"
, {
"entities":[
(0, 2, "STATE"),
(3, 11, "CITY"),
(12, 24, "TELEPHONE_NUMBER"),
(25, 30, "ZIPCODE"),
(31, 38, "STATE_FULL"),
(39, 59, "STREET_ADDRESS"),
(60, 72, "MOBILE_NUMBER"),
]
}),
(
"59030 Montana MT 406-230-2290 406-848-3131 4839 Coolidge Street Gardiner"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 13, "STATE_FULL"),
(14, 16, "STATE"),
(17, 29, "MOBILE_NUMBER"),
(30, 42, "TELEPHONE_NUMBER"),
(43, 63, "STREET_ADDRESS"),
(64, 72, "CITY"),
]
}),
(
"Gardiner Montana 59030 406-848-3131 4839 Coolidge Street 406-230-2290 MT"
, {
"entities":[
(0, 8, "CITY"),
(9, 16, "STATE_FULL"),
(17, 22, "ZIPCODE"),
(23, 35, "TELEPHONE_NUMBER"),
(36, 56, "STREET_ADDRESS"),
(57, 69, "MOBILE_NUMBER"),
(70, 72, "STATE"),
]
}),
(
"MT 4839 Coolidge Street Gardiner 59030 406-230-2290 406-848-3131 Montana"
, {
"entities":[
(0, 2, "STATE"),
(3, 23, "STREET_ADDRESS"),
(24, 32, "CITY"),
(33, 38, "ZIPCODE"),
(39, 51, "MOBILE_NUMBER"),
(52, 64, "TELEPHONE_NUMBER"),
(65, 72, "STATE_FULL"),
]
}),
(
"MT 4839 Coolidge Street Montana 406-230-2290 Gardiner 59030 406-848-3131"
, {
"entities":[
(0, 2, "STATE"),
(3, 23, "STREET_ADDRESS"),
(24, 31, "STATE_FULL"),
(32, 44, "MOBILE_NUMBER"),
(45, 53, "CITY"),
(54, 59, "ZIPCODE"),
(60, 72, "TELEPHONE_NUMBER"),
]
}),
(
"406-230-2290 4839 Coolidge Street 406-848-3131 Gardiner MT Montana 59030"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 33, "STREET_ADDRESS"),
(34, 46, "TELEPHONE_NUMBER"),
(47, 55, "CITY"),
(56, 58, "STATE"),
(59, 66, "STATE_FULL"),
(67, 72, "ZIPCODE"),
]
}),
(
"Gardiner 406-848-3131 59030 406-230-2290 MT 4839 Coolidge Street Montana"
, {
"entities":[
(0, 8, "CITY"),
(9, 21, "TELEPHONE_NUMBER"),
(22, 27, "ZIPCODE"),
(28, 40, "MOBILE_NUMBER"),
(41, 43, "STATE"),
(44, 64, "STREET_ADDRESS"),
(65, 72, "STATE_FULL"),
]
}),
(
"Gardiner MT 406-230-2290 59030 Montana 406-848-3131 4839 Coolidge Street"
, {
"entities":[
(0, 8, "CITY"),
(9, 11, "STATE"),
(12, 24, "MOBILE_NUMBER"),
(25, 30, "ZIPCODE"),
(31, 38, "STATE_FULL"),
(39, 51, "TELEPHONE_NUMBER"),
(52, 72, "STREET_ADDRESS"),
]
}),
(
"MT Montana 4839 Coolidge Street Gardiner 59030 406-230-2290 406-848-3131"
, {
"entities":[
(0, 2, "STATE"),
(3, 10, "STATE_FULL"),
(11, 31, "STREET_ADDRESS"),
(32, 40, "CITY"),
(41, 46, "ZIPCODE"),
(47, 59, "MOBILE_NUMBER"),
(60, 72, "TELEPHONE_NUMBER"),
]
}),
(
"Gardiner 4839 Coolidge Street 59030 Montana 406-230-2290 MT 406-848-3131"
, {
"entities":[
(0, 8, "CITY"),
(9, 29, "STREET_ADDRESS"),
(30, 35, "ZIPCODE"),
(36, 43, "STATE_FULL"),
(44, 56, "MOBILE_NUMBER"),
(57, 59, "STATE"),
(60, 72, "TELEPHONE_NUMBER"),
]
}),
(
"1744 Golf Course Drive Virginia 703-282-4657 20170 VA Herndon 703-326-5163"
, {
"entities":[
(0, 22, "STREET_ADDRESS"),
(23, 31, "STATE_FULL"),
(32, 44, "MOBILE_NUMBER"),
(45, 50, "ZIPCODE"),
(51, 53, "STATE"),
(54, 61, "CITY"),
(62, 74, "TELEPHONE_NUMBER"),
]
}),
(
"Virginia 703-326-5163 20170 703-282-4657 1744 Golf Course Drive Herndon VA"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 21, "TELEPHONE_NUMBER"),
(22, 27, "ZIPCODE"),
(28, 40, "MOBILE_NUMBER"),
(41, 63, "STREET_ADDRESS"),
(64, 71, "CITY"),
(72, 74, "STATE"),
]
}),
(
"Virginia 20170 1744 Golf Course Drive Herndon 703-282-4657 VA 703-326-5163"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 14, "ZIPCODE"),
(15, 37, "STREET_ADDRESS"),
(38, 45, "CITY"),
(46, 58, "MOBILE_NUMBER"),
(59, 61, "STATE"),
(62, 74, "TELEPHONE_NUMBER"),
]
}),
(
"703-282-4657 Herndon 1744 Golf Course Drive VA 703-326-5163 20170 Virginia"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 20, "CITY"),
(21, 43, "STREET_ADDRESS"),
(44, 46, "STATE"),
(47, 59, "TELEPHONE_NUMBER"),
(60, 65, "ZIPCODE"),
(66, 74, "STATE_FULL"),
]
}),
(
"20170 703-282-4657 703-326-5163 VA 1744 Golf Course Drive Herndon Virginia"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "MOBILE_NUMBER"),
(19, 31, "TELEPHONE_NUMBER"),
(32, 34, "STATE"),
(35, 57, "STREET_ADDRESS"),
(58, 65, "CITY"),
(66, 74, "STATE_FULL"),
]
}),
(
"20170 703-326-5163 Virginia Herndon 1744 Golf Course Drive 703-282-4657 VA"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "TELEPHONE_NUMBER"),
(19, 27, "STATE_FULL"),
(28, 35, "CITY"),
(36, 58, "STREET_ADDRESS"),
(59, 71, "MOBILE_NUMBER"),
(72, 74, "STATE"),
]
}),
(
"703-282-4657 VA 703-326-5163 Herndon 20170 Virginia 1744 Golf Course Drive"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 15, "STATE"),
(16, 28, "TELEPHONE_NUMBER"),
(29, 36, "CITY"),
(37, 42, "ZIPCODE"),
(43, 51, "STATE_FULL"),
(52, 74, "STREET_ADDRESS"),
]
}),
(
"703-326-5163 703-282-4657 20170 Virginia Herndon VA 1744 Golf Course Drive"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 25, "MOBILE_NUMBER"),
(26, 31, "ZIPCODE"),
(32, 40, "STATE_FULL"),
(41, 48, "CITY"),
(49, 51, "STATE"),
(52, 74, "STREET_ADDRESS"),
]
}),
(
"703-326-5163 20170 Herndon VA 703-282-4657 1744 Golf Course Drive Virginia"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 26, "CITY"),
(27, 29, "STATE"),
(30, 42, "MOBILE_NUMBER"),
(43, 65, "STREET_ADDRESS"),
(66, 74, "STATE_FULL"),
]
}),
(
"20170 Herndon Virginia 1744 Golf Course Drive 703-282-4657 VA 703-326-5163"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 13, "CITY"),
(14, 22, "STATE_FULL"),
(23, 45, "STREET_ADDRESS"),
(46, 58, "MOBILE_NUMBER"),
(59, 61, "STATE"),
(62, 74, "TELEPHONE_NUMBER"),
]
}),
(
"33012 FL 561-652-4972 Hialeah Florida 813-361-5698 4138 Powder House Road"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 21, "TELEPHONE_NUMBER"),
(22, 29, "CITY"),
(30, 37, "STATE_FULL"),
(38, 50, "MOBILE_NUMBER"),
(51, 73, "STREET_ADDRESS"),
]
}),
(
"Hialeah Florida 813-361-5698 4138 Powder House Road FL 33012 561-652-4972"
, {
"entities":[
(0, 7, "CITY"),
(8, 15, "STATE_FULL"),
(16, 28, "MOBILE_NUMBER"),
(29, 51, "STREET_ADDRESS"),
(52, 54, "STATE"),
(55, 60, "ZIPCODE"),
(61, 73, "TELEPHONE_NUMBER"),
]
}),
(
"813-361-5698 4138 Powder House Road Florida FL 561-652-4972 Hialeah 33012"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 35, "STREET_ADDRESS"),
(36, 43, "STATE_FULL"),
(44, 46, "STATE"),
(47, 59, "TELEPHONE_NUMBER"),
(60, 67, "CITY"),
(68, 73, "ZIPCODE"),
]
}),
(
"33012 4138 Powder House Road FL Florida Hialeah 813-361-5698 561-652-4972"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 28, "STREET_ADDRESS"),
(29, 31, "STATE"),
(32, 39, "STATE_FULL"),
(40, 47, "CITY"),
(48, 60, "MOBILE_NUMBER"),
(61, 73, "TELEPHONE_NUMBER"),
]
}),
(
"Florida 813-361-5698 33012 Hialeah 561-652-4972 4138 Powder House Road FL"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 20, "MOBILE_NUMBER"),
(21, 26, "ZIPCODE"),
(27, 34, "CITY"),
(35, 47, "TELEPHONE_NUMBER"),
(48, 70, "STREET_ADDRESS"),
(71, 73, "STATE"),
]
}),
(
"FL 33012 4138 Powder House Road Hialeah 561-652-4972 Florida 813-361-5698"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 31, "STREET_ADDRESS"),
(32, 39, "CITY"),
(40, 52, "TELEPHONE_NUMBER"),
(53, 60, "STATE_FULL"),
(61, 73, "MOBILE_NUMBER"),
]
}),
(
"33012 4138 Powder House Road Hialeah 561-652-4972 FL Florida 813-361-5698"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 28, "STREET_ADDRESS"),
(29, 36, "CITY"),
(37, 49, "TELEPHONE_NUMBER"),
(50, 52, "STATE"),
(53, 60, "STATE_FULL"),
(61, 73, "MOBILE_NUMBER"),
]
}),
(
"813-361-5698 FL Hialeah 33012 561-652-4972 4138 Powder House Road Florida"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 15, "STATE"),
(16, 23, "CITY"),
(24, 29, "ZIPCODE"),
(30, 42, "TELEPHONE_NUMBER"),
(43, 65, "STREET_ADDRESS"),
(66, 73, "STATE_FULL"),
]
}),
(
"33012 Florida Hialeah 561-652-4972 813-361-5698 FL 4138 Powder House Road"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 13, "STATE_FULL"),
(14, 21, "CITY"),
(22, 34, "TELEPHONE_NUMBER"),
(35, 47, "MOBILE_NUMBER"),
(48, 50, "STATE"),
(51, 73, "STREET_ADDRESS"),
]
}),
(
"Florida 561-652-4972 FL Hialeah 33012 813-361-5698 4138 Powder House Road"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 20, "TELEPHONE_NUMBER"),
(21, 23, "STATE"),
(24, 31, "CITY"),
(32, 37, "ZIPCODE"),
(38, 50, "MOBILE_NUMBER"),
(51, 73, "STREET_ADDRESS"),
]
}),
(
"Boys Ranch 2703 Charmaine Lane Texas TX 281-473-0781 79092 806-534-0694"
, {
"entities":[
(0, 10, "CITY"),
(11, 30, "STREET_ADDRESS"),
(31, 36, "STATE_FULL"),
(37, 39, "STATE"),
(40, 52, "MOBILE_NUMBER"),
(53, 58, "ZIPCODE"),
(59, 71, "TELEPHONE_NUMBER"),
]
}),
(
"TX Boys Ranch 281-473-0781 Texas 2703 Charmaine Lane 79092 806-534-0694"
, {
"entities":[
(0, 2, "STATE"),
(3, 13, "CITY"),
(14, 26, "MOBILE_NUMBER"),
(27, 32, "STATE_FULL"),
(33, 52, "STREET_ADDRESS"),
(53, 58, "ZIPCODE"),
(59, 71, "TELEPHONE_NUMBER"),
]
}),
(
"TX Boys Ranch 806-534-0694 Texas 281-473-0781 79092 2703 Charmaine Lane"
, {
"entities":[
(0, 2, "STATE"),
(3, 13, "CITY"),
(14, 26, "TELEPHONE_NUMBER"),
(27, 32, "STATE_FULL"),
(33, 45, "MOBILE_NUMBER"),
(46, 51, "ZIPCODE"),
(52, 71, "STREET_ADDRESS"),
]
}),
(
"806-534-0694 TX Texas 281-473-0781 Boys Ranch 79092 2703 Charmaine Lane"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 15, "STATE"),
(16, 21, "STATE_FULL"),
(22, 34, "MOBILE_NUMBER"),
(35, 45, "CITY"),
(46, 51, "ZIPCODE"),
(52, 71, "STREET_ADDRESS"),
]
}),
(
"806-534-0694 2703 Charmaine Lane TX 281-473-0781 Texas Boys Ranch 79092"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 32, "STREET_ADDRESS"),
(33, 35, "STATE"),
(36, 48, "MOBILE_NUMBER"),
(49, 54, "STATE_FULL"),
(55, 65, "CITY"),
(66, 71, "ZIPCODE"),
]
}),
(
"Texas 281-473-0781 806-534-0694 2703 Charmaine Lane 79092 Boys Ranch TX"
, {
"entities":[
(0, 5, "STATE_FULL"),
(6, 18, "MOBILE_NUMBER"),
(19, 31, "TELEPHONE_NUMBER"),
(32, 51, "STREET_ADDRESS"),
(52, 57, "ZIPCODE"),
(58, 68, "CITY"),
(69, 71, "STATE"),
]
}),
(
"281-473-0781 79092 Boys Ranch 2703 Charmaine Lane 806-534-0694 Texas TX"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 29, "CITY"),
(30, 49, "STREET_ADDRESS"),
(50, 62, "TELEPHONE_NUMBER"),
(63, 68, "STATE_FULL"),
(69, 71, "STATE"),
]
}),
(
"2703 Charmaine Lane 806-534-0694 281-473-0781 79092 Texas TX Boys Ranch"
, {
"entities":[
(0, 19, "STREET_ADDRESS"),
(20, 32, "TELEPHONE_NUMBER"),
(33, 45, "MOBILE_NUMBER"),
(46, 51, "ZIPCODE"),
(52, 57, "STATE_FULL"),
(58, 60, "STATE"),
(61, 71, "CITY"),
]
}),
(
"806-534-0694 79092 Texas 281-473-0781 2703 Charmaine Lane Boys Ranch TX"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 24, "STATE_FULL"),
(25, 37, "MOBILE_NUMBER"),
(38, 57, "STREET_ADDRESS"),
(58, 68, "CITY"),
(69, 71, "STATE"),
]
}),
(
"Boys Ranch 281-473-0781 79092 Texas TX 2703 Charmaine Lane 806-534-0694"
, {
"entities":[
(0, 10, "CITY"),
(11, 23, "MOBILE_NUMBER"),
(24, 29, "ZIPCODE"),
(30, 35, "STATE_FULL"),
(36, 38, "STATE"),
(39, 58, "STREET_ADDRESS"),
(59, 71, "TELEPHONE_NUMBER"),
]
}),
(
"San Antonio 78205 Texas 210-215-4526 TX 1814 Todds Lane 210-487-6670"
, {
"entities":[
(0, 11, "CITY"),
(12, 17, "ZIPCODE"),
(18, 23, "STATE_FULL"),
(24, 36, "MOBILE_NUMBER"),
(37, 39, "STATE"),
(40, 55, "STREET_ADDRESS"),
(56, 68, "TELEPHONE_NUMBER"),
]
}),
(
"210-215-4526 Texas San Antonio TX 210-487-6670 1814 Todds Lane 78205"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 18, "STATE_FULL"),
(19, 30, "CITY"),
(31, 33, "STATE"),
(34, 46, "TELEPHONE_NUMBER"),
(47, 62, "STREET_ADDRESS"),
(63, 68, "ZIPCODE"),
]
}),
(
"Texas 210-215-4526 78205 210-487-6670 San Antonio 1814 Todds Lane TX"
, {
"entities":[
(0, 5, "STATE_FULL"),
(6, 18, "MOBILE_NUMBER"),
(19, 24, "ZIPCODE"),
(25, 37, "TELEPHONE_NUMBER"),
(38, 49, "CITY"),
(50, 65, "STREET_ADDRESS"),
(66, 68, "STATE"),
]
}),
(
"78205 210-215-4526 San Antonio 210-487-6670 1814 Todds Lane TX Texas"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "MOBILE_NUMBER"),
(19, 30, "CITY"),
(31, 43, "TELEPHONE_NUMBER"),
(44, 59, "STREET_ADDRESS"),
(60, 62, "STATE"),
(63, 68, "STATE_FULL"),
]
}),
(
"TX Texas 78205 210-215-4526 1814 Todds Lane 210-487-6670 San Antonio"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "STATE_FULL"),
(9, 14, "ZIPCODE"),
(15, 27, "MOBILE_NUMBER"),
(28, 43, "STREET_ADDRESS"),
(44, 56, "TELEPHONE_NUMBER"),
(57, 68, "CITY"),
]
}),
(
"Texas 210-215-4526 78205 1814 Todds Lane 210-487-6670 TX San Antonio"
, {
"entities":[
(0, 5, "STATE_FULL"),
(6, 18, "MOBILE_NUMBER"),
(19, 24, "ZIPCODE"),
(25, 40, "STREET_ADDRESS"),
(41, 53, "TELEPHONE_NUMBER"),
(54, 56, "STATE"),
(57, 68, "CITY"),
]
}),
(
"1814 Todds Lane 210-215-4526 TX San Antonio 210-487-6670 Texas 78205"
, {
"entities":[
(0, 15, "STREET_ADDRESS"),
(16, 28, "MOBILE_NUMBER"),
(29, 31, "STATE"),
(32, 43, "CITY"),
(44, 56, "TELEPHONE_NUMBER"),
(57, 62, "STATE_FULL"),
(63, 68, "ZIPCODE"),
]
}),
(
"San Antonio Texas 1814 Todds Lane 78205 210-215-4526 210-487-6670 TX"
, {
"entities":[
(0, 11, "CITY"),
(12, 17, "STATE_FULL"),
(18, 33, "STREET_ADDRESS"),
(34, 39, "ZIPCODE"),
(40, 52, "MOBILE_NUMBER"),
(53, 65, "TELEPHONE_NUMBER"),
(66, 68, "STATE"),
]
}),
(
"Texas San Antonio TX 210-487-6670 78205 210-215-4526 1814 Todds Lane"
, {
"entities":[
(0, 5, "STATE_FULL"),
(6, 17, "CITY"),
(18, 20, "STATE"),
(21, 33, "TELEPHONE_NUMBER"),
(34, 39, "ZIPCODE"),
(40, 52, "MOBILE_NUMBER"),
(53, 68, "STREET_ADDRESS"),
]
}),
(
"210-487-6670 1814 Todds Lane Texas San Antonio TX 210-215-4526 78205"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 28, "STREET_ADDRESS"),
(29, 34, "STATE_FULL"),
(35, 46, "CITY"),
(47, 49, "STATE"),
(50, 62, "MOBILE_NUMBER"),
(63, 68, "ZIPCODE"),
]
}),
(
"417-809-6346 Missouri Stockton MO 2143 Briarwood Road 65785 417-955-9780"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 21, "STATE_FULL"),
(22, 30, "CITY"),
(31, 33, "STATE"),
(34, 53, "STREET_ADDRESS"),
(54, 59, "ZIPCODE"),
(60, 72, "MOBILE_NUMBER"),
]
}),
(
"Stockton 65785 417-955-9780 2143 Briarwood Road MO 417-809-6346 Missouri"
, {
"entities":[
(0, 8, "CITY"),
(9, 14, "ZIPCODE"),
(15, 27, "MOBILE_NUMBER"),
(28, 47, "STREET_ADDRESS"),
(48, 50, "STATE"),
(51, 63, "TELEPHONE_NUMBER"),
(64, 72, "STATE_FULL"),
]
}),
(
"417-955-9780 2143 Briarwood Road Missouri 65785 Stockton MO 417-809-6346"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 32, "STREET_ADDRESS"),
(33, 41, "STATE_FULL"),
(42, 47, "ZIPCODE"),
(48, 56, "CITY"),
(57, 59, "STATE"),
(60, 72, "TELEPHONE_NUMBER"),
]
}),
(
"Stockton 65785 2143 Briarwood Road 417-809-6346 417-955-9780 Missouri MO"
, {
"entities":[
(0, 8, "CITY"),
(9, 14, "ZIPCODE"),
(15, 34, "STREET_ADDRESS"),
(35, 47, "TELEPHONE_NUMBER"),
(48, 60, "MOBILE_NUMBER"),
(61, 69, "STATE_FULL"),
(70, 72, "STATE"),
]
}),
(
"65785 Stockton 2143 Briarwood Road Missouri MO 417-809-6346 417-955-9780"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 14, "CITY"),
(15, 34, "STREET_ADDRESS"),
(35, 43, "STATE_FULL"),
(44, 46, "STATE"),
(47, 59, "TELEPHONE_NUMBER"),
(60, 72, "MOBILE_NUMBER"),
]
}),
(
"2143 Briarwood Road 417-809-6346 MO Missouri Stockton 65785 417-955-9780"
, {
"entities":[
(0, 19, "STREET_ADDRESS"),
(20, 32, "TELEPHONE_NUMBER"),
(33, 35, "STATE"),
(36, 44, "STATE_FULL"),
(45, 53, "CITY"),
(54, 59, "ZIPCODE"),
(60, 72, "MOBILE_NUMBER"),
]
}),
(
"65785 417-955-9780 Missouri Stockton 2143 Briarwood Road 417-809-6346 MO"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "MOBILE_NUMBER"),
(19, 27, "STATE_FULL"),
(28, 36, "CITY"),
(37, 56, "STREET_ADDRESS"),
(57, 69, "TELEPHONE_NUMBER"),
(70, 72, "STATE"),
]
}),
(
"417-955-9780 2143 Briarwood Road 65785 Missouri Stockton 417-809-6346 MO"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 32, "STREET_ADDRESS"),
(33, 38, "ZIPCODE"),
(39, 47, "STATE_FULL"),
(48, 56, "CITY"),
(57, 69, "TELEPHONE_NUMBER"),
(70, 72, "STATE"),
]
}),
(
"Stockton Missouri 65785 2143 Briarwood Road MO 417-955-9780 417-809-6346"
, {
"entities":[
(0, 8, "CITY"),
(9, 17, "STATE_FULL"),
(18, 23, "ZIPCODE"),
(24, 43, "STREET_ADDRESS"),
(44, 46, "STATE"),
(47, 59, "MOBILE_NUMBER"),
(60, 72, "TELEPHONE_NUMBER"),
]
}),
(
"65785 Missouri MO 417-955-9780 Stockton 2143 Briarwood Road 417-809-6346"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 14, "STATE_FULL"),
(15, 17, "STATE"),
(18, 30, "MOBILE_NUMBER"),
(31, 39, "CITY"),
(40, 59, "STREET_ADDRESS"),
(60, 72, "TELEPHONE_NUMBER"),
]
}),
(
"33037 305-394-1573 Florida 720 Steve Hunt Road Key Largo FL 305-786-3135"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "MOBILE_NUMBER"),
(19, 26, "STATE_FULL"),
(27, 46, "STREET_ADDRESS"),
(47, 56, "CITY"),
(57, 59, "STATE"),
(60, 72, "TELEPHONE_NUMBER"),
]
}),
(
"305-786-3135 33037 FL 305-394-1573 720 Steve Hunt Road Key Largo Florida"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 21, "STATE"),
(22, 34, "MOBILE_NUMBER"),
(35, 54, "STREET_ADDRESS"),
(55, 64, "CITY"),
(65, 72, "STATE_FULL"),
]
}),
(
"720 Steve Hunt Road Florida 305-786-3135 305-394-1573 Key Largo FL 33037"
, {
"entities":[
(0, 19, "STREET_ADDRESS"),
(20, 27, "STATE_FULL"),
(28, 40, "TELEPHONE_NUMBER"),
(41, 53, "MOBILE_NUMBER"),
(54, 63, "CITY"),
(64, 66, "STATE"),
(67, 72, "ZIPCODE"),
]
}),
(
"FL Florida 33037 Key Largo 720 Steve Hunt Road 305-786-3135 305-394-1573"
, {
"entities":[
(0, 2, "STATE"),
(3, 10, "STATE_FULL"),
(11, 16, "ZIPCODE"),
(17, 26, "CITY"),
(27, 46, "STREET_ADDRESS"),
(47, 59, "TELEPHONE_NUMBER"),
(60, 72, "MOBILE_NUMBER"),
]
}),
(
"305-394-1573 Key Largo 720 Steve Hunt Road FL 33037 305-786-3135 Florida"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 22, "CITY"),
(23, 42, "STREET_ADDRESS"),
(43, 45, "STATE"),
(46, 51, "ZIPCODE"),
(52, 64, "TELEPHONE_NUMBER"),
(65, 72, "STATE_FULL"),
]
}),
(
"Key Largo 305-394-1573 33037 720 Steve Hunt Road Florida 305-786-3135 FL"
, {
"entities":[
(0, 9, "CITY"),
(10, 22, "MOBILE_NUMBER"),
(23, 28, "ZIPCODE"),
(29, 48, "STREET_ADDRESS"),
(49, 56, "STATE_FULL"),
(57, 69, "TELEPHONE_NUMBER"),
(70, 72, "STATE"),
]
}),
(
"Florida 720 Steve Hunt Road FL 305-786-3135 33037 305-394-1573 Key Largo"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 27, "STREET_ADDRESS"),
(28, 30, "STATE"),
(31, 43, "TELEPHONE_NUMBER"),
(44, 49, "ZIPCODE"),
(50, 62, "MOBILE_NUMBER"),
(63, 72, "CITY"),
]
}),
(
"305-786-3135 33037 FL Florida 305-394-1573 Key Largo 720 Steve Hunt Road"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 21, "STATE"),
(22, 29, "STATE_FULL"),
(30, 42, "MOBILE_NUMBER"),
(43, 52, "CITY"),
(53, 72, "STREET_ADDRESS"),
]
}),
(
"Florida Key Largo 305-786-3135 FL 720 Steve Hunt Road 305-394-1573 33037"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 17, "CITY"),
(18, 30, "TELEPHONE_NUMBER"),
(31, 33, "STATE"),
(34, 53, "STREET_ADDRESS"),
(54, 66, "MOBILE_NUMBER"),
(67, 72, "ZIPCODE"),
]
}),
(
"720 Steve Hunt Road Key Largo 33037 FL 305-786-3135 305-394-1573 Florida"
, {
"entities":[
(0, 19, "STREET_ADDRESS"),
(20, 29, "CITY"),
(30, 35, "ZIPCODE"),
(36, 38, "STATE"),
(39, 51, "TELEPHONE_NUMBER"),
(52, 64, "MOBILE_NUMBER"),
(65, 72, "STATE_FULL"),
]
}),
(
"Kokomo IN 4750 Sugarfoot Lane 317-608-3568 46901 765-434-7252 Indiana"
, {
"entities":[
(0, 6, "CITY"),
(7, 9, "STATE"),
(10, 29, "STREET_ADDRESS"),
(30, 42, "MOBILE_NUMBER"),
(43, 48, "ZIPCODE"),
(49, 61, "TELEPHONE_NUMBER"),
(62, 69, "STATE_FULL"),
]
}),
(
"4750 Sugarfoot Lane 765-434-7252 Kokomo Indiana IN 317-608-3568 46901"
, {
"entities":[
(0, 19, "STREET_ADDRESS"),
(20, 32, "TELEPHONE_NUMBER"),
(33, 39, "CITY"),
(40, 47, "STATE_FULL"),
(48, 50, "STATE"),
(51, 63, "MOBILE_NUMBER"),
(64, 69, "ZIPCODE"),
]
}),
(
"Indiana 765-434-7252 317-608-3568 4750 Sugarfoot Lane IN 46901 Kokomo"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 20, "TELEPHONE_NUMBER"),
(21, 33, "MOBILE_NUMBER"),
(34, 53, "STREET_ADDRESS"),
(54, 56, "STATE"),
(57, 62, "ZIPCODE"),
(63, 69, "CITY"),
]
}),
(
"46901 317-608-3568 Kokomo 765-434-7252 4750 Sugarfoot Lane IN Indiana"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "MOBILE_NUMBER"),
(19, 25, "CITY"),
(26, 38, "TELEPHONE_NUMBER"),
(39, 58, "STREET_ADDRESS"),
(59, 61, "STATE"),
(62, 69, "STATE_FULL"),
]
}),
(
"317-608-3568 Indiana IN Kokomo 4750 Sugarfoot Lane 46901 765-434-7252"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 20, "STATE_FULL"),
(21, 23, "STATE"),
(24, 30, "CITY"),
(31, 50, "STREET_ADDRESS"),
(51, 56, "ZIPCODE"),
(57, 69, "TELEPHONE_NUMBER"),
]
}),
(
"317-608-3568 4750 Sugarfoot Lane Indiana IN 765-434-7252 46901 Kokomo"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 32, "STREET_ADDRESS"),
(33, 40, "STATE_FULL"),
(41, 43, "STATE"),
(44, 56, "TELEPHONE_NUMBER"),
(57, 62, "ZIPCODE"),
(63, 69, "CITY"),
]
}),
(
"IN Kokomo 317-608-3568 46901 765-434-7252 Indiana 4750 Sugarfoot Lane"
, {
"entities":[
(0, 2, "STATE"),
(3, 9, "CITY"),
(10, 22, "MOBILE_NUMBER"),
(23, 28, "ZIPCODE"),
(29, 41, "TELEPHONE_NUMBER"),
(42, 49, "STATE_FULL"),
(50, 69, "STREET_ADDRESS"),
]
}),
(
"317-608-3568 Indiana 4750 Sugarfoot Lane 46901 Kokomo 765-434-7252 IN"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 20, "STATE_FULL"),
(21, 40, "STREET_ADDRESS"),
(41, 46, "ZIPCODE"),
(47, 53, "CITY"),
(54, 66, "TELEPHONE_NUMBER"),
(67, 69, "STATE"),
]
}),
(
"Indiana Kokomo 317-608-3568 765-434-7252 4750 Sugarfoot Lane 46901 IN"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 14, "CITY"),
(15, 27, "MOBILE_NUMBER"),
(28, 40, "TELEPHONE_NUMBER"),
(41, 60, "STREET_ADDRESS"),
(61, 66, "ZIPCODE"),
(67, 69, "STATE"),
]
}),
(
"Indiana Kokomo 46901 317-608-3568 IN 4750 Sugarfoot Lane 765-434-7252"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 14, "CITY"),
(15, 20, "ZIPCODE"),
(21, 33, "MOBILE_NUMBER"),
(34, 36, "STATE"),
(37, 56, "STREET_ADDRESS"),
(57, 69, "TELEPHONE_NUMBER"),
]
}),
(
"Virginia 571-233-1460 4404 Conference Center Way VA 703-431-0931 Leesburg 22075"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 21, "TELEPHONE_NUMBER"),
(22, 48, "STREET_ADDRESS"),
(49, 51, "STATE"),
(52, 64, "MOBILE_NUMBER"),
(65, 73, "CITY"),
(74, 79, "ZIPCODE"),
]
}),
(
"4404 Conference Center Way 571-233-1460 Virginia 703-431-0931 VA Leesburg 22075"
, {
"entities":[
(0, 26, "STREET_ADDRESS"),
(27, 39, "TELEPHONE_NUMBER"),
(40, 48, "STATE_FULL"),
(49, 61, "MOBILE_NUMBER"),
(62, 64, "STATE"),
(65, 73, "CITY"),
(74, 79, "ZIPCODE"),
]
}),
(
"Virginia 4404 Conference Center Way 703-431-0931 VA 571-233-1460 Leesburg 22075"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 35, "STREET_ADDRESS"),
(36, 48, "MOBILE_NUMBER"),
(49, 51, "STATE"),
(52, 64, "TELEPHONE_NUMBER"),
(65, 73, "CITY"),
(74, 79, "ZIPCODE"),
]
}),
(
"Leesburg 571-233-1460 4404 Conference Center Way Virginia 22075 703-431-0931 VA"
, {
"entities":[
(0, 8, "CITY"),
(9, 21, "TELEPHONE_NUMBER"),
(22, 48, "STREET_ADDRESS"),
(49, 57, "STATE_FULL"),
(58, 63, "ZIPCODE"),
(64, 76, "MOBILE_NUMBER"),
(77, 79, "STATE"),
]
}),
(
"4404 Conference Center Way Virginia VA Leesburg 571-233-1460 22075 703-431-0931"
, {
"entities":[
(0, 26, "STREET_ADDRESS"),
(27, 35, "STATE_FULL"),
(36, 38, "STATE"),
(39, 47, "CITY"),
(48, 60, "TELEPHONE_NUMBER"),
(61, 66, "ZIPCODE"),
(67, 79, "MOBILE_NUMBER"),
]
}),
(
"Virginia VA 571-233-1460 22075 703-431-0931 4404 Conference Center Way Leesburg"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 11, "STATE"),
(12, 24, "TELEPHONE_NUMBER"),
(25, 30, "ZIPCODE"),
(31, 43, "MOBILE_NUMBER"),
(44, 70, "STREET_ADDRESS"),
(71, 79, "CITY"),
]
}),
(
"22075 Virginia VA 4404 Conference Center Way 703-431-0931 571-233-1460 Leesburg"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 14, "STATE_FULL"),
(15, 17, "STATE"),
(18, 44, "STREET_ADDRESS"),
(45, 57, "MOBILE_NUMBER"),
(58, 70, "TELEPHONE_NUMBER"),
(71, 79, "CITY"),
]
}),
(
"571-233-1460 Leesburg 22075 4404 Conference Center Way 703-431-0931 Virginia VA"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 21, "CITY"),
(22, 27, "ZIPCODE"),
(28, 54, "STREET_ADDRESS"),
(55, 67, "MOBILE_NUMBER"),
(68, 76, "STATE_FULL"),
(77, 79, "STATE"),
]
}),
(
"Leesburg 703-431-0931 22075 4404 Conference Center Way VA Virginia 571-233-1460"
, {
"entities":[
(0, 8, "CITY"),
(9, 21, "MOBILE_NUMBER"),
(22, 27, "ZIPCODE"),
(28, 54, "STREET_ADDRESS"),
(55, 57, "STATE"),
(58, 66, "STATE_FULL"),
(67, 79, "TELEPHONE_NUMBER"),
]
}),
(
"22075 Leesburg 4404 Conference Center Way Virginia 703-431-0931 571-233-1460 VA"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 14, "CITY"),
(15, 41, "STREET_ADDRESS"),
(42, 50, "STATE_FULL"),
(51, 63, "MOBILE_NUMBER"),
(64, 76, "TELEPHONE_NUMBER"),
(77, 79, "STATE"),
]
}),
(
"Jacksonville 30 Cherry Tree Drive Florida 904-323-0815 904-351-7672 32202 FL"
, {
"entities":[
(0, 12, "CITY"),
(13, 33, "STREET_ADDRESS"),
(34, 41, "STATE_FULL"),
(42, 54, "MOBILE_NUMBER"),
(55, 67, "TELEPHONE_NUMBER"),
(68, 73, "ZIPCODE"),
(74, 76, "STATE"),
]
}),
(
"FL 30 Cherry Tree Drive 904-351-7672 904-323-0815 Jacksonville Florida 32202"
, {
"entities":[
(0, 2, "STATE"),
(3, 23, "STREET_ADDRESS"),
(24, 36, "TELEPHONE_NUMBER"),
(37, 49, "MOBILE_NUMBER"),
(50, 62, "CITY"),
(63, 70, "STATE_FULL"),
(71, 76, "ZIPCODE"),
]
}),
(
"904-323-0815 Jacksonville 904-351-7672 30 Cherry Tree Drive Florida FL 32202"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 25, "CITY"),
(26, 38, "TELEPHONE_NUMBER"),
(39, 59, "STREET_ADDRESS"),
(60, 67, "STATE_FULL"),
(68, 70, "STATE"),
(71, 76, "ZIPCODE"),
]
}),
(
"30 Cherry Tree Drive 32202 Florida 904-323-0815 904-351-7672 Jacksonville FL"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 26, "ZIPCODE"),
(27, 34, "STATE_FULL"),
(35, 47, "MOBILE_NUMBER"),
(48, 60, "TELEPHONE_NUMBER"),
(61, 73, "CITY"),
(74, 76, "STATE"),
]
}),
(
"904-351-7672 904-323-0815 Florida 32202 30 Cherry Tree Drive FL Jacksonville"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 25, "MOBILE_NUMBER"),
(26, 33, "STATE_FULL"),
(34, 39, "ZIPCODE"),
(40, 60, "STREET_ADDRESS"),
(61, 63, "STATE"),
(64, 76, "CITY"),
]
}),
(
"Florida FL 30 Cherry Tree Drive 904-351-7672 32202 Jacksonville 904-323-0815"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 10, "STATE"),
(11, 31, "STREET_ADDRESS"),
(32, 44, "TELEPHONE_NUMBER"),
(45, 50, "ZIPCODE"),
(51, 63, "CITY"),
(64, 76, "MOBILE_NUMBER"),
]
}),
(
"Florida FL 30 Cherry Tree Drive 904-323-0815 32202 904-351-7672 Jacksonville"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 10, "STATE"),
(11, 31, "STREET_ADDRESS"),
(32, 44, "MOBILE_NUMBER"),
(45, 50, "ZIPCODE"),
(51, 63, "TELEPHONE_NUMBER"),
(64, 76, "CITY"),
]
}),
(
"904-323-0815 Florida Jacksonville 32202 904-351-7672 FL 30 Cherry Tree Drive"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 20, "STATE_FULL"),
(21, 33, "CITY"),
(34, 39, "ZIPCODE"),
(40, 52, "TELEPHONE_NUMBER"),
(53, 55, "STATE"),
(56, 76, "STREET_ADDRESS"),
]
}),
(
"30 Cherry Tree Drive 904-351-7672 Florida 904-323-0815 32202 Jacksonville FL"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 33, "TELEPHONE_NUMBER"),
(34, 41, "STATE_FULL"),
(42, 54, "MOBILE_NUMBER"),
(55, 60, "ZIPCODE"),
(61, 73, "CITY"),
(74, 76, "STATE"),
]
}),
(
"Jacksonville Florida 904-351-7672 FL 30 Cherry Tree Drive 904-323-0815 32202"
, {
"entities":[
(0, 12, "CITY"),
(13, 20, "STATE_FULL"),
(21, 33, "TELEPHONE_NUMBER"),
(34, 36, "STATE"),
(37, 57, "STREET_ADDRESS"),
(58, 70, "MOBILE_NUMBER"),
(71, 76, "ZIPCODE"),
]
}),
(
"620 Elk Rd Little Tucson 520-268-8804 520-267-6140 AZ 85701 Arizona"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 24, "CITY"),
(25, 37, "MOBILE_NUMBER"),
(38, 50, "TELEPHONE_NUMBER"),
(51, 53, "STATE"),
(54, 59, "ZIPCODE"),
(60, 67, "STATE_FULL"),
]
}),
(
"520-268-8804 85701 520-267-6140 Tucson 620 Elk Rd Little Arizona AZ"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 31, "TELEPHONE_NUMBER"),
(32, 38, "CITY"),
(39, 56, "STREET_ADDRESS"),
(57, 64, "STATE_FULL"),
(65, 67, "STATE"),
]
}),
(
"520-268-8804 85701 Tucson Arizona 520-267-6140 AZ 620 Elk Rd Little"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 25, "CITY"),
(26, 33, "STATE_FULL"),
(34, 46, "TELEPHONE_NUMBER"),
(47, 49, "STATE"),
(50, 67, "STREET_ADDRESS"),
]
}),
(
"85701 520-268-8804 Tucson 620 Elk Rd Little 520-267-6140 AZ Arizona"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "MOBILE_NUMBER"),
(19, 25, "CITY"),
(26, 43, "STREET_ADDRESS"),
(44, 56, "TELEPHONE_NUMBER"),
(57, 59, "STATE"),
(60, 67, "STATE_FULL"),
]
}),
(
"520-267-6140 Tucson AZ 620 Elk Rd Little Arizona 85701 520-268-8804"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 19, "CITY"),
(20, 22, "STATE"),
(23, 40, "STREET_ADDRESS"),
(41, 48, "STATE_FULL"),
(49, 54, "ZIPCODE"),
(55, 67, "MOBILE_NUMBER"),
]
}),
(
"520-268-8804 AZ 620 Elk Rd Little Tucson 85701 Arizona 520-267-6140"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 15, "STATE"),
(16, 33, "STREET_ADDRESS"),
(34, 40, "CITY"),
(41, 46, "ZIPCODE"),
(47, 54, "STATE_FULL"),
(55, 67, "TELEPHONE_NUMBER"),
]
}),
(
"620 Elk Rd Little 85701 Tucson Arizona 520-268-8804 520-267-6140 AZ"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 23, "ZIPCODE"),
(24, 30, "CITY"),
(31, 38, "STATE_FULL"),
(39, 51, "MOBILE_NUMBER"),
(52, 64, "TELEPHONE_NUMBER"),
(65, 67, "STATE"),
]
}),
(
"Arizona AZ Tucson 520-267-6140 620 Elk Rd Little 85701 520-268-8804"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 10, "STATE"),
(11, 17, "CITY"),
(18, 30, "TELEPHONE_NUMBER"),
(31, 48, "STREET_ADDRESS"),
(49, 54, "ZIPCODE"),
(55, 67, "MOBILE_NUMBER"),
]
}),
(
"AZ Tucson Arizona 520-267-6140 520-268-8804 620 Elk Rd Little 85701"
, {
"entities":[
(0, 2, "STATE"),
(3, 9, "CITY"),
(10, 17, "STATE_FULL"),
(18, 30, "TELEPHONE_NUMBER"),
(31, 43, "MOBILE_NUMBER"),
(44, 61, "STREET_ADDRESS"),
(62, 67, "ZIPCODE"),
]
}),
(
"Tucson Arizona 520-267-6140 AZ 520-268-8804 620 Elk Rd Little 85701"
, {
"entities":[
(0, 6, "CITY"),
(7, 14, "STATE_FULL"),
(15, 27, "TELEPHONE_NUMBER"),
(28, 30, "STATE"),
(31, 43, "MOBILE_NUMBER"),
(44, 61, "STREET_ADDRESS"),
(62, 67, "ZIPCODE"),
]
}),
(
"734-812-3858 1900 John Avenue MI East Lansing Michigan 48823 517-895-7439"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 29, "STREET_ADDRESS"),
(30, 32, "STATE"),
(33, 45, "CITY"),
(46, 54, "STATE_FULL"),
(55, 60, "ZIPCODE"),
(61, 73, "TELEPHONE_NUMBER"),
]
}),
(
"MI Michigan 517-895-7439 1900 John Avenue East Lansing 48823 734-812-3858"
, {
"entities":[
(0, 2, "STATE"),
(3, 11, "STATE_FULL"),
(12, 24, "TELEPHONE_NUMBER"),
(25, 41, "STREET_ADDRESS"),
(42, 54, "CITY"),
(55, 60, "ZIPCODE"),
(61, 73, "MOBILE_NUMBER"),
]
}),
(
"734-812-3858 Michigan 517-895-7439 MI 48823 1900 John Avenue East Lansing"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 21, "STATE_FULL"),
(22, 34, "TELEPHONE_NUMBER"),
(35, 37, "STATE"),
(38, 43, "ZIPCODE"),
(44, 60, "STREET_ADDRESS"),
(61, 73, "CITY"),
]
}),
(
"517-895-7439 East Lansing MI 1900 John Avenue Michigan 734-812-3858 48823"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 25, "CITY"),
(26, 28, "STATE"),
(29, 45, "STREET_ADDRESS"),
(46, 54, "STATE_FULL"),
(55, 67, "MOBILE_NUMBER"),
(68, 73, "ZIPCODE"),
]
}),
(
"734-812-3858 1900 John Avenue Michigan East Lansing MI 48823 517-895-7439"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 29, "STREET_ADDRESS"),
(30, 38, "STATE_FULL"),
(39, 51, "CITY"),
(52, 54, "STATE"),
(55, 60, "ZIPCODE"),
(61, 73, "TELEPHONE_NUMBER"),
]
}),
(
"48823 East Lansing 517-895-7439 1900 John Avenue 734-812-3858 MI Michigan"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "CITY"),
(19, 31, "TELEPHONE_NUMBER"),
(32, 48, "STREET_ADDRESS"),
(49, 61, "MOBILE_NUMBER"),
(62, 64, "STATE"),
(65, 73, "STATE_FULL"),
]
}),
(
"48823 East Lansing MI 734-812-3858 1900 John Avenue Michigan 517-895-7439"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "CITY"),
(19, 21, "STATE"),
(22, 34, "MOBILE_NUMBER"),
(35, 51, "STREET_ADDRESS"),
(52, 60, "STATE_FULL"),
(61, 73, "TELEPHONE_NUMBER"),
]
}),
(
"734-812-3858 517-895-7439 1900 John Avenue MI 48823 Michigan East Lansing"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 25, "TELEPHONE_NUMBER"),
(26, 42, "STREET_ADDRESS"),
(43, 45, "STATE"),
(46, 51, "ZIPCODE"),
(52, 60, "STATE_FULL"),
(61, 73, "CITY"),
]
}),
(
"48823 734-812-3858 MI Michigan 1900 John Avenue East Lansing 517-895-7439"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "MOBILE_NUMBER"),
(19, 21, "STATE"),
(22, 30, "STATE_FULL"),
(31, 47, "STREET_ADDRESS"),
(48, 60, "CITY"),
(61, 73, "TELEPHONE_NUMBER"),
]
}),
(
"48823 517-895-7439 1900 John Avenue 734-812-3858 East Lansing Michigan MI"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "TELEPHONE_NUMBER"),
(19, 35, "STREET_ADDRESS"),
(36, 48, "MOBILE_NUMBER"),
(49, 61, "CITY"),
(62, 70, "STATE_FULL"),
(71, 73, "STATE"),
]
}),
(
"720-275-0496 CO Colorado 80202 303-389-1411 2698 Sweetwood Drive Denver"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 15, "STATE"),
(16, 24, "STATE_FULL"),
(25, 30, "ZIPCODE"),
(31, 43, "TELEPHONE_NUMBER"),
(44, 64, "STREET_ADDRESS"),
(65, 71, "CITY"),
]
}),
(
"303-389-1411 720-275-0496 80202 CO Colorado Denver 2698 Sweetwood Drive"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 25, "MOBILE_NUMBER"),
(26, 31, "ZIPCODE"),
(32, 34, "STATE"),
(35, 43, "STATE_FULL"),
(44, 50, "CITY"),
(51, 71, "STREET_ADDRESS"),
]
}),
(
"Colorado 303-389-1411 Denver 720-275-0496 2698 Sweetwood Drive 80202 CO"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 21, "TELEPHONE_NUMBER"),
(22, 28, "CITY"),
(29, 41, "MOBILE_NUMBER"),
(42, 62, "STREET_ADDRESS"),
(63, 68, "ZIPCODE"),
(69, 71, "STATE"),
]
}),
(
"Denver 80202 720-275-0496 CO Colorado 303-389-1411 2698 Sweetwood Drive"
, {
"entities":[
(0, 6, "CITY"),
(7, 12, "ZIPCODE"),
(13, 25, "MOBILE_NUMBER"),
(26, 28, "STATE"),
(29, 37, "STATE_FULL"),
(38, 50, "TELEPHONE_NUMBER"),
(51, 71, "STREET_ADDRESS"),
]
}),
(
"720-275-0496 303-389-1411 2698 Sweetwood Drive Denver CO Colorado 80202"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 25, "TELEPHONE_NUMBER"),
(26, 46, "STREET_ADDRESS"),
(47, 53, "CITY"),
(54, 56, "STATE"),
(57, 65, "STATE_FULL"),
(66, 71, "ZIPCODE"),
]
}),
(
"80202 720-275-0496 303-389-1411 Colorado 2698 Sweetwood Drive CO Denver"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "MOBILE_NUMBER"),
(19, 31, "TELEPHONE_NUMBER"),
(32, 40, "STATE_FULL"),
(41, 61, "STREET_ADDRESS"),
(62, 64, "STATE"),
(65, 71, "CITY"),
]
}),
(
"720-275-0496 2698 Sweetwood Drive 80202 303-389-1411 CO Denver Colorado"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 33, "STREET_ADDRESS"),
(34, 39, "ZIPCODE"),
(40, 52, "TELEPHONE_NUMBER"),
(53, 55, "STATE"),
(56, 62, "CITY"),
(63, 71, "STATE_FULL"),
]
}),
(
"720-275-0496 CO Denver 2698 Sweetwood Drive 303-389-1411 80202 Colorado"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 15, "STATE"),
(16, 22, "CITY"),
(23, 43, "STREET_ADDRESS"),
(44, 56, "TELEPHONE_NUMBER"),
(57, 62, "ZIPCODE"),
(63, 71, "STATE_FULL"),
]
}),
(
"2698 Sweetwood Drive CO Colorado 80202 303-389-1411 Denver 720-275-0496"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 23, "STATE"),
(24, 32, "STATE_FULL"),
(33, 38, "ZIPCODE"),
(39, 51, "TELEPHONE_NUMBER"),
(52, 58, "CITY"),
(59, 71, "MOBILE_NUMBER"),
]
}),
(
"303-389-1411 Denver Colorado 720-275-0496 2698 Sweetwood Drive CO 80202"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 19, "CITY"),
(20, 28, "STATE_FULL"),
(29, 41, "MOBILE_NUMBER"),
(42, 62, "STREET_ADDRESS"),
(63, 65, "STATE"),
(66, 71, "ZIPCODE"),
]
}),
(
"76102 620-680-7509 785-659-3965 4947 Dog Hill Lane Fort Worth Kansas KS"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "MOBILE_NUMBER"),
(19, 31, "TELEPHONE_NUMBER"),
(32, 50, "STREET_ADDRESS"),
(51, 61, "CITY"),
(62, 68, "STATE_FULL"),
(69, 71, "STATE"),
]
}),
(
"4947 Dog Hill Lane Fort Worth Kansas 76102 620-680-7509 KS 785-659-3965"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 29, "CITY"),
(30, 36, "STATE_FULL"),
(37, 42, "ZIPCODE"),
(43, 55, "MOBILE_NUMBER"),
(56, 58, "STATE"),
(59, 71, "TELEPHONE_NUMBER"),
]
}),
(
"KS Kansas 620-680-7509 4947 Dog Hill Lane Fort Worth 785-659-3965 76102"
, {
"entities":[
(0, 2, "STATE"),
(3, 9, "STATE_FULL"),
(10, 22, "MOBILE_NUMBER"),
(23, 41, "STREET_ADDRESS"),
(42, 52, "CITY"),
(53, 65, "TELEPHONE_NUMBER"),
(66, 71, "ZIPCODE"),
]
}),
(
"785-659-3965 76102 4947 Dog Hill Lane Fort Worth 620-680-7509 KS Kansas"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 37, "STREET_ADDRESS"),
(38, 48, "CITY"),
(49, 61, "MOBILE_NUMBER"),
(62, 64, "STATE"),
(65, 71, "STATE_FULL"),
]
}),
(
"76102 4947 Dog Hill Lane Fort Worth KS Kansas 785-659-3965 620-680-7509"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 24, "STREET_ADDRESS"),
(25, 35, "CITY"),
(36, 38, "STATE"),
(39, 45, "STATE_FULL"),
(46, 58, "TELEPHONE_NUMBER"),
(59, 71, "MOBILE_NUMBER"),
]
}),
(
"Kansas KS Fort Worth 4947 Dog Hill Lane 785-659-3965 76102 620-680-7509"
, {
"entities":[
(0, 6, "STATE_FULL"),
(7, 9, "STATE"),
(10, 20, "CITY"),
(21, 39, "STREET_ADDRESS"),
(40, 52, "TELEPHONE_NUMBER"),
(53, 58, "ZIPCODE"),
(59, 71, "MOBILE_NUMBER"),
]
}),
(
"620-680-7509 KS 4947 Dog Hill Lane 76102 785-659-3965 Kansas Fort Worth"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 15, "STATE"),
(16, 34, "STREET_ADDRESS"),
(35, 40, "ZIPCODE"),
(41, 53, "TELEPHONE_NUMBER"),
(54, 60, "STATE_FULL"),
(61, 71, "CITY"),
]
}),
(
"Fort Worth KS 76102 785-659-3965 4947 Dog Hill Lane Kansas 620-680-7509"
, {
"entities":[
(0, 10, "CITY"),
(11, 13, "STATE"),
(14, 19, "ZIPCODE"),
(20, 32, "TELEPHONE_NUMBER"),
(33, 51, "STREET_ADDRESS"),
(52, 58, "STATE_FULL"),
(59, 71, "MOBILE_NUMBER"),
]
}),
(
"76102 620-680-7509 4947 Dog Hill Lane Kansas KS Fort Worth 785-659-3965"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "MOBILE_NUMBER"),
(19, 37, "STREET_ADDRESS"),
(38, 44, "STATE_FULL"),
(45, 47, "STATE"),
(48, 58, "CITY"),
(59, 71, "TELEPHONE_NUMBER"),
]
}),
(
"785-659-3965 Fort Worth Kansas 4947 Dog Hill Lane 620-680-7509 KS 76102"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 23, "CITY"),
(24, 30, "STATE_FULL"),
(31, 49, "STREET_ADDRESS"),
(50, 62, "MOBILE_NUMBER"),
(63, 65, "STATE"),
(66, 71, "ZIPCODE"),
]
}),
(
"79602 325-370-1894 Texas TX 1955 Anthony Avenue 325-788-7234 Abilene"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "MOBILE_NUMBER"),
(19, 24, "STATE_FULL"),
(25, 27, "STATE"),
(28, 47, "STREET_ADDRESS"),
(48, 60, "TELEPHONE_NUMBER"),
(61, 68, "CITY"),
]
}),
(
"325-370-1894 1955 Anthony Avenue 79602 Texas TX Abilene 325-788-7234"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 32, "STREET_ADDRESS"),
(33, 38, "ZIPCODE"),
(39, 44, "STATE_FULL"),
(45, 47, "STATE"),
(48, 55, "CITY"),
(56, 68, "TELEPHONE_NUMBER"),
]
}),
(
"Abilene TX 325-788-7234 325-370-1894 1955 Anthony Avenue Texas 79602"
, {
"entities":[
(0, 7, "CITY"),
(8, 10, "STATE"),
(11, 23, "TELEPHONE_NUMBER"),
(24, 36, "MOBILE_NUMBER"),
(37, 56, "STREET_ADDRESS"),
(57, 62, "STATE_FULL"),
(63, 68, "ZIPCODE"),
]
}),
(
"1955 Anthony Avenue 325-370-1894 Abilene TX 79602 Texas 325-788-7234"
, {
"entities":[
(0, 19, "STREET_ADDRESS"),
(20, 32, "MOBILE_NUMBER"),
(33, 40, "CITY"),
(41, 43, "STATE"),
(44, 49, "ZIPCODE"),
(50, 55, "STATE_FULL"),
(56, 68, "TELEPHONE_NUMBER"),
]
}),
(
"Texas 325-788-7234 325-370-1894 Abilene TX 79602 1955 Anthony Avenue"
, {
"entities":[
(0, 5, "STATE_FULL"),
(6, 18, "TELEPHONE_NUMBER"),
(19, 31, "MOBILE_NUMBER"),
(32, 39, "CITY"),
(40, 42, "STATE"),
(43, 48, "ZIPCODE"),
(49, 68, "STREET_ADDRESS"),
]
}),
(
"Texas 325-370-1894 TX Abilene 79602 1955 Anthony Avenue 325-788-7234"
, {
"entities":[
(0, 5, "STATE_FULL"),
(6, 18, "MOBILE_NUMBER"),
(19, 21, "STATE"),
(22, 29, "CITY"),
(30, 35, "ZIPCODE"),
(36, 55, "STREET_ADDRESS"),
(56, 68, "TELEPHONE_NUMBER"),
]
}),
(
"1955 Anthony Avenue 325-370-1894 Abilene TX 325-788-7234 79602 Texas"
, {
"entities":[
(0, 19, "STREET_ADDRESS"),
(20, 32, "MOBILE_NUMBER"),
(33, 40, "CITY"),
(41, 43, "STATE"),
(44, 56, "TELEPHONE_NUMBER"),
(57, 62, "ZIPCODE"),
(63, 68, "STATE_FULL"),
]
}),
(
"Texas TX 325-788-7234 325-370-1894 Abilene 1955 Anthony Avenue 79602"
, {
"entities":[
(0, 5, "STATE_FULL"),
(6, 8, "STATE"),
(9, 21, "TELEPHONE_NUMBER"),
(22, 34, "MOBILE_NUMBER"),
(35, 42, "CITY"),
(43, 62, "STREET_ADDRESS"),
(63, 68, "ZIPCODE"),
]
}),
(
"79602 1955 Anthony Avenue 325-370-1894 TX Texas 325-788-7234 Abilene"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 25, "STREET_ADDRESS"),
(26, 38, "MOBILE_NUMBER"),
(39, 41, "STATE"),
(42, 47, "STATE_FULL"),
(48, 60, "TELEPHONE_NUMBER"),
(61, 68, "CITY"),
]
}),
(
"79602 Abilene 325-370-1894 1955 Anthony Avenue Texas TX 325-788-7234"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 13, "CITY"),
(14, 26, "MOBILE_NUMBER"),
(27, 46, "STREET_ADDRESS"),
(47, 52, "STATE_FULL"),
(53, 55, "STATE"),
(56, 68, "TELEPHONE_NUMBER"),
]
}),
(
"Baton Rouge LA 225-326-7082 2926 Washburn Street Louisiana 70802 225-409-6039"
, {
"entities":[
(0, 11, "CITY"),
(12, 14, "STATE"),
(15, 27, "TELEPHONE_NUMBER"),
(28, 48, "STREET_ADDRESS"),
(49, 58, "STATE_FULL"),
(59, 64, "ZIPCODE"),
(65, 77, "MOBILE_NUMBER"),
]
}),
(
"70802 Baton Rouge 225-409-6039 2926 Washburn Street Louisiana 225-326-7082 LA"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 17, "CITY"),
(18, 30, "MOBILE_NUMBER"),
(31, 51, "STREET_ADDRESS"),
(52, 61, "STATE_FULL"),
(62, 74, "TELEPHONE_NUMBER"),
(75, 77, "STATE"),
]
}),
(
"Louisiana 70802 LA 2926 Washburn Street 225-326-7082 225-409-6039 Baton Rouge"
, {
"entities":[
(0, 9, "STATE_FULL"),
(10, 15, "ZIPCODE"),
(16, 18, "STATE"),
(19, 39, "STREET_ADDRESS"),
(40, 52, "TELEPHONE_NUMBER"),
(53, 65, "MOBILE_NUMBER"),
(66, 77, "CITY"),
]
}),
(
"Baton Rouge 225-409-6039 2926 Washburn Street LA 70802 225-326-7082 Louisiana"
, {
"entities":[
(0, 11, "CITY"),
(12, 24, "MOBILE_NUMBER"),
(25, 45, "STREET_ADDRESS"),
(46, 48, "STATE"),
(49, 54, "ZIPCODE"),
(55, 67, "TELEPHONE_NUMBER"),
(68, 77, "STATE_FULL"),
]
}),
(
"225-409-6039 2926 Washburn Street 70802 Louisiana Baton Rouge 225-326-7082 LA"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 33, "STREET_ADDRESS"),
(34, 39, "ZIPCODE"),
(40, 49, "STATE_FULL"),
(50, 61, "CITY"),
(62, 74, "TELEPHONE_NUMBER"),
(75, 77, "STATE"),
]
}),
(
"225-326-7082 225-409-6039 70802 LA 2926 Washburn Street Louisiana Baton Rouge"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 25, "MOBILE_NUMBER"),
(26, 31, "ZIPCODE"),
(32, 34, "STATE"),
(35, 55, "STREET_ADDRESS"),
(56, 65, "STATE_FULL"),
(66, 77, "CITY"),
]
}),
(
"225-326-7082 225-409-6039 2926 Washburn Street 70802 Louisiana LA Baton Rouge"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 25, "MOBILE_NUMBER"),
(26, 46, "STREET_ADDRESS"),
(47, 52, "ZIPCODE"),
(53, 62, "STATE_FULL"),
(63, 65, "STATE"),
(66, 77, "CITY"),
]
}),
(
"70802 LA 225-409-6039 225-326-7082 Baton Rouge 2926 Washburn Street Louisiana"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 21, "MOBILE_NUMBER"),
(22, 34, "TELEPHONE_NUMBER"),
(35, 46, "CITY"),
(47, 67, "STREET_ADDRESS"),
(68, 77, "STATE_FULL"),
]
}),
(
"225-326-7082 2926 Washburn Street Baton Rouge Louisiana 70802 LA 225-409-6039"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 33, "STREET_ADDRESS"),
(34, 45, "CITY"),
(46, 55, "STATE_FULL"),
(56, 61, "ZIPCODE"),
(62, 64, "STATE"),
(65, 77, "MOBILE_NUMBER"),
]
}),
(
"Louisiana 225-326-7082 LA 2926 Washburn Street Baton Rouge 70802 225-409-6039"
, {
"entities":[
(0, 9, "STATE_FULL"),
(10, 22, "TELEPHONE_NUMBER"),
(23, 25, "STATE"),
(26, 46, "STREET_ADDRESS"),
(47, 58, "CITY"),
(59, 64, "ZIPCODE"),
(65, 77, "MOBILE_NUMBER"),
]
}),
(
"Philadelphia 267-347-1530 PA 19123 1568 Valley Drive Pennsylvania 267-231-8750"
, {
"entities":[
(0, 12, "CITY"),
(13, 25, "TELEPHONE_NUMBER"),
(26, 28, "STATE"),
(29, 34, "ZIPCODE"),
(35, 52, "STREET_ADDRESS"),
(53, 65, "STATE_FULL"),
(66, 78, "MOBILE_NUMBER"),
]
}),
(
"Philadelphia 267-347-1530 1568 Valley Drive 19123 PA Pennsylvania 267-231-8750"
, {
"entities":[
(0, 12, "CITY"),
(13, 25, "TELEPHONE_NUMBER"),
(26, 43, "STREET_ADDRESS"),
(44, 49, "ZIPCODE"),
(50, 52, "STATE"),
(53, 65, "STATE_FULL"),
(66, 78, "MOBILE_NUMBER"),
]
}),
(
"267-231-8750 1568 Valley Drive PA Philadelphia 19123 Pennsylvania 267-347-1530"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 30, "STREET_ADDRESS"),
(31, 33, "STATE"),
(34, 46, "CITY"),
(47, 52, "ZIPCODE"),
(53, 65, "STATE_FULL"),
(66, 78, "TELEPHONE_NUMBER"),
]
}),
(
"267-347-1530 19123 1568 Valley Drive Pennsylvania 267-231-8750 PA Philadelphia"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 36, "STREET_ADDRESS"),
(37, 49, "STATE_FULL"),
(50, 62, "MOBILE_NUMBER"),
(63, 65, "STATE"),
(66, 78, "CITY"),
]
}),
(
"267-347-1530 1568 Valley Drive 267-231-8750 PA 19123 Philadelphia Pennsylvania"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 30, "STREET_ADDRESS"),
(31, 43, "MOBILE_NUMBER"),
(44, 46, "STATE"),
(47, 52, "ZIPCODE"),
(53, 65, "CITY"),
(66, 78, "STATE_FULL"),
]
}),
(
"PA 19123 267-347-1530 1568 Valley Drive 267-231-8750 Philadelphia Pennsylvania"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 21, "TELEPHONE_NUMBER"),
(22, 39, "STREET_ADDRESS"),
(40, 52, "MOBILE_NUMBER"),
(53, 65, "CITY"),
(66, 78, "STATE_FULL"),
]
}),
(
"Philadelphia PA 267-347-1530 267-231-8750 Pennsylvania 1568 Valley Drive 19123"
, {
"entities":[
(0, 12, "CITY"),
(13, 15, "STATE"),
(16, 28, "TELEPHONE_NUMBER"),
(29, 41, "MOBILE_NUMBER"),
(42, 54, "STATE_FULL"),
(55, 72, "STREET_ADDRESS"),
(73, 78, "ZIPCODE"),
]
}),
(
"1568 Valley Drive 19123 Pennsylvania PA Philadelphia 267-231-8750 267-347-1530"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 23, "ZIPCODE"),
(24, 36, "STATE_FULL"),
(37, 39, "STATE"),
(40, 52, "CITY"),
(53, 65, "MOBILE_NUMBER"),
(66, 78, "TELEPHONE_NUMBER"),
]
}),
(
"267-347-1530 19123 PA 267-231-8750 1568 Valley Drive Pennsylvania Philadelphia"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 21, "STATE"),
(22, 34, "MOBILE_NUMBER"),
(35, 52, "STREET_ADDRESS"),
(53, 65, "STATE_FULL"),
(66, 78, "CITY"),
]
}),
(
"19123 267-231-8750 267-347-1530 Philadelphia 1568 Valley Drive PA Pennsylvania"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "MOBILE_NUMBER"),
(19, 31, "TELEPHONE_NUMBER"),
(32, 44, "CITY"),
(45, 62, "STREET_ADDRESS"),
(63, 65, "STATE"),
(66, 78, "STATE_FULL"),
]
}),
(
"Superior Wisconsin 715-862-0701 715-969-9795 1599 Orphan Road WI 54880"
, {
"entities":[
(0, 8, "CITY"),
(9, 18, "STATE_FULL"),
(19, 31, "TELEPHONE_NUMBER"),
(32, 44, "MOBILE_NUMBER"),
(45, 61, "STREET_ADDRESS"),
(62, 64, "STATE"),
(65, 70, "ZIPCODE"),
]
}),
(
"Wisconsin WI 715-862-0701 1599 Orphan Road Superior 54880 715-969-9795"
, {
"entities":[
(0, 9, "STATE_FULL"),
(10, 12, "STATE"),
(13, 25, "TELEPHONE_NUMBER"),
(26, 42, "STREET_ADDRESS"),
(43, 51, "CITY"),
(52, 57, "ZIPCODE"),
(58, 70, "MOBILE_NUMBER"),
]
}),
(
"1599 Orphan Road 715-969-9795 WI Superior Wisconsin 715-862-0701 54880"
, {
"entities":[
(0, 16, "STREET_ADDRESS"),
(17, 29, "MOBILE_NUMBER"),
(30, 32, "STATE"),
(33, 41, "CITY"),
(42, 51, "STATE_FULL"),
(52, 64, "TELEPHONE_NUMBER"),
(65, 70, "ZIPCODE"),
]
}),
(
"1599 Orphan Road WI Wisconsin Superior 715-862-0701 54880 715-969-9795"
, {
"entities":[
(0, 16, "STREET_ADDRESS"),
(17, 19, "STATE"),
(20, 29, "STATE_FULL"),
(30, 38, "CITY"),
(39, 51, "TELEPHONE_NUMBER"),
(52, 57, "ZIPCODE"),
(58, 70, "MOBILE_NUMBER"),
]
}),
(
"Wisconsin 715-862-0701 WI Superior 715-969-9795 54880 1599 Orphan Road"
, {
"entities":[
(0, 9, "STATE_FULL"),
(10, 22, "TELEPHONE_NUMBER"),
(23, 25, "STATE"),
(26, 34, "CITY"),
(35, 47, "MOBILE_NUMBER"),
(48, 53, "ZIPCODE"),
(54, 70, "STREET_ADDRESS"),
]
}),
(
"715-969-9795 1599 Orphan Road Wisconsin WI Superior 54880 715-862-0701"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 29, "STREET_ADDRESS"),
(30, 39, "STATE_FULL"),
(40, 42, "STATE"),
(43, 51, "CITY"),
(52, 57, "ZIPCODE"),
(58, 70, "TELEPHONE_NUMBER"),
]
}),
(
"Superior 54880 1599 Orphan Road 715-862-0701 WI 715-969-9795 Wisconsin"
, {
"entities":[
(0, 8, "CITY"),
(9, 14, "ZIPCODE"),
(15, 31, "STREET_ADDRESS"),
(32, 44, "TELEPHONE_NUMBER"),
(45, 47, "STATE"),
(48, 60, "MOBILE_NUMBER"),
(61, 70, "STATE_FULL"),
]
}),
(
"715-969-9795 715-862-0701 Superior WI 1599 Orphan Road 54880 Wisconsin"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 25, "TELEPHONE_NUMBER"),
(26, 34, "CITY"),
(35, 37, "STATE"),
(38, 54, "STREET_ADDRESS"),
(55, 60, "ZIPCODE"),
(61, 70, "STATE_FULL"),
]
}),
(
"WI Superior 715-862-0701 1599 Orphan Road 54880 Wisconsin 715-969-9795"
, {
"entities":[
(0, 2, "STATE"),
(3, 11, "CITY"),
(12, 24, "TELEPHONE_NUMBER"),
(25, 41, "STREET_ADDRESS"),
(42, 47, "ZIPCODE"),
(48, 57, "STATE_FULL"),
(58, 70, "MOBILE_NUMBER"),
]
}),
(
"715-969-9795 WI 1599 Orphan Road Wisconsin 54880 Superior 715-862-0701"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 15, "STATE"),
(16, 32, "STREET_ADDRESS"),
(33, 42, "STATE_FULL"),
(43, 48, "ZIPCODE"),
(49, 57, "CITY"),
(58, 70, "TELEPHONE_NUMBER"),
]
}),
(
"4216 Small Street NY 10029 New York New York 212-876-0196 917-812-1769"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 20, "STATE"),
(21, 26, "ZIPCODE"),
(27, 35, "CITY"),
(36, 44, "STATE_FULL"),
(45, 57, "TELEPHONE_NUMBER"),
(58, 70, "MOBILE_NUMBER"),
]
}),
(
"New York NY 4216 Small Street 917-812-1769 10029 New York 212-876-0196"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 11, "STATE"),
(12, 29, "STREET_ADDRESS"),
(30, 42, "MOBILE_NUMBER"),
(43, 48, "ZIPCODE"),
(49, 57, "CITY"),
(58, 70, "TELEPHONE_NUMBER"),
]
}),
(
"212-876-0196 New York NY 10029 New York 917-812-1769 4216 Small Street"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 21, "CITY"),
(22, 24, "STATE"),
(25, 30, "ZIPCODE"),
(31, 39, "STATE_FULL"),
(40, 52, "MOBILE_NUMBER"),
(53, 70, "STREET_ADDRESS"),
]
}),
(
"212-876-0196 4216 Small Street 917-812-1769 New York 10029 New York NY"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 30, "STREET_ADDRESS"),
(31, 43, "MOBILE_NUMBER"),
(44, 52, "CITY"),
(53, 58, "ZIPCODE"),
(59, 67, "STATE_FULL"),
(68, 70, "STATE"),
]
}),
(
"New York 212-876-0196 10029 917-812-1769 New York 4216 Small Street NY"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 21, "TELEPHONE_NUMBER"),
(22, 27, "ZIPCODE"),
(28, 40, "MOBILE_NUMBER"),
(41, 49, "CITY"),
(50, 67, "STREET_ADDRESS"),
(68, 70, "STATE"),
]
}),
(
"212-876-0196 10029 4216 Small Street NY New York 917-812-1769 New York"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 36, "STREET_ADDRESS"),
(37, 39, "STATE"),
(40, 48, "CITY"),
(49, 61, "MOBILE_NUMBER"),
(62, 70, "STATE_FULL"),
]
}),
(
"917-812-1769 212-876-0196 NY New York 10029 New York 4216 Small Street"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 25, "TELEPHONE_NUMBER"),
(26, 28, "STATE"),
(29, 37, "CITY"),
(38, 43, "ZIPCODE"),
(44, 52, "STATE_FULL"),
(53, 70, "STREET_ADDRESS"),
]
}),
(
"212-876-0196 4216 Small Street 10029 NY New York 917-812-1769 New York"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 30, "STREET_ADDRESS"),
(31, 36, "ZIPCODE"),
(37, 39, "STATE"),
(40, 48, "CITY"),
(49, 61, "MOBILE_NUMBER"),
(62, 70, "STATE_FULL"),
]
}),
(
"New York 212-876-0196 10029 New York 4216 Small Street NY 917-812-1769"
, {
"entities":[
(0, 8, "CITY"),
(9, 21, "TELEPHONE_NUMBER"),
(22, 27, "ZIPCODE"),
(28, 36, "STATE_FULL"),
(37, 54, "STREET_ADDRESS"),
(55, 57, "STATE"),
(58, 70, "MOBILE_NUMBER"),
]
}),
(
"New York NY 4216 Small Street 917-812-1769 10029 212-876-0196 New York"
, {
"entities":[
(0, 8, "CITY"),
(9, 11, "STATE"),
(12, 29, "STREET_ADDRESS"),
(30, 42, "MOBILE_NUMBER"),
(43, 48, "ZIPCODE"),
(49, 61, "TELEPHONE_NUMBER"),
(62, 70, "STATE_FULL"),
]
}),
(
"503-998-2350 Oregon OR 1171 Brooklyn Street 97205 Portland 541-239-0350"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 19, "STATE_FULL"),
(20, 22, "STATE"),
(23, 43, "STREET_ADDRESS"),
(44, 49, "ZIPCODE"),
(50, 58, "CITY"),
(59, 71, "TELEPHONE_NUMBER"),
]
}),
(
"503-998-2350 Portland 541-239-0350 OR Oregon 97205 1171 Brooklyn Street"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 21, "CITY"),
(22, 34, "TELEPHONE_NUMBER"),
(35, 37, "STATE"),
(38, 44, "STATE_FULL"),
(45, 50, "ZIPCODE"),
(51, 71, "STREET_ADDRESS"),
]
}),
(
"503-998-2350 Portland OR 1171 Brooklyn Street Oregon 97205 541-239-0350"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 21, "CITY"),
(22, 24, "STATE"),
(25, 45, "STREET_ADDRESS"),
(46, 52, "STATE_FULL"),
(53, 58, "ZIPCODE"),
(59, 71, "TELEPHONE_NUMBER"),
]
}),
(
"Portland OR 1171 Brooklyn Street 503-998-2350 541-239-0350 Oregon 97205"
, {
"entities":[
(0, 8, "CITY"),
(9, 11, "STATE"),
(12, 32, "STREET_ADDRESS"),
(33, 45, "MOBILE_NUMBER"),
(46, 58, "TELEPHONE_NUMBER"),
(59, 65, "STATE_FULL"),
(66, 71, "ZIPCODE"),
]
}),
(
"97205 Oregon 503-998-2350 Portland 1171 Brooklyn Street OR 541-239-0350"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 12, "STATE_FULL"),
(13, 25, "MOBILE_NUMBER"),
(26, 34, "CITY"),
(35, 55, "STREET_ADDRESS"),
(56, 58, "STATE"),
(59, 71, "TELEPHONE_NUMBER"),
]
}),
(
"1171 Brooklyn Street 503-998-2350 97205 541-239-0350 Portland Oregon OR"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 33, "MOBILE_NUMBER"),
(34, 39, "ZIPCODE"),
(40, 52, "TELEPHONE_NUMBER"),
(53, 61, "CITY"),
(62, 68, "STATE_FULL"),
(69, 71, "STATE"),
]
}),
(
"OR 97205 1171 Brooklyn Street 541-239-0350 Oregon Portland 503-998-2350"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 29, "STREET_ADDRESS"),
(30, 42, "TELEPHONE_NUMBER"),
(43, 49, "STATE_FULL"),
(50, 58, "CITY"),
(59, 71, "MOBILE_NUMBER"),
]
}),
(
"97205 1171 Brooklyn Street Portland Oregon OR 541-239-0350 503-998-2350"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 26, "STREET_ADDRESS"),
(27, 35, "CITY"),
(36, 42, "STATE_FULL"),
(43, 45, "STATE"),
(46, 58, "TELEPHONE_NUMBER"),
(59, 71, "MOBILE_NUMBER"),
]
}),
(
"Oregon OR Portland 541-239-0350 97205 1171 Brooklyn Street 503-998-2350"
, {
"entities":[
(0, 6, "STATE_FULL"),
(7, 9, "STATE"),
(10, 18, "CITY"),
(19, 31, "TELEPHONE_NUMBER"),
(32, 37, "ZIPCODE"),
(38, 58, "STREET_ADDRESS"),
(59, 71, "MOBILE_NUMBER"),
]
}),
(
"1171 Brooklyn Street Oregon Portland OR 541-239-0350 97205 503-998-2350"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 27, "STATE_FULL"),
(28, 36, "CITY"),
(37, 39, "STATE"),
(40, 52, "TELEPHONE_NUMBER"),
(53, 58, "ZIPCODE"),
(59, 71, "MOBILE_NUMBER"),
]
}),
(
"95827 California 916-362-5515 Sacramento 916-806-8324 3573 Pearl Street CA"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 16, "STATE_FULL"),
(17, 29, "TELEPHONE_NUMBER"),
(30, 40, "CITY"),
(41, 53, "MOBILE_NUMBER"),
(54, 71, "STREET_ADDRESS"),
(72, 74, "STATE"),
]
}),
(
"916-806-8324 California CA Sacramento 95827 916-362-5515 3573 Pearl Street"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 23, "STATE_FULL"),
(24, 26, "STATE"),
(27, 37, "CITY"),
(38, 43, "ZIPCODE"),
(44, 56, "TELEPHONE_NUMBER"),
(57, 74, "STREET_ADDRESS"),
]
}),
(
"916-806-8324 California Sacramento CA 3573 Pearl Street 95827 916-362-5515"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 23, "STATE_FULL"),
(24, 34, "CITY"),
(35, 37, "STATE"),
(38, 55, "STREET_ADDRESS"),
(56, 61, "ZIPCODE"),
(62, 74, "TELEPHONE_NUMBER"),
]
}),
(
"916-806-8324 3573 Pearl Street California Sacramento 95827 916-362-5515 CA"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 30, "STREET_ADDRESS"),
(31, 41, "STATE_FULL"),
(42, 52, "CITY"),
(53, 58, "ZIPCODE"),
(59, 71, "TELEPHONE_NUMBER"),
(72, 74, "STATE"),
]
}),
(
"95827 Sacramento California 916-362-5515 916-806-8324 CA 3573 Pearl Street"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 16, "CITY"),
(17, 27, "STATE_FULL"),
(28, 40, "TELEPHONE_NUMBER"),
(41, 53, "MOBILE_NUMBER"),
(54, 56, "STATE"),
(57, 74, "STREET_ADDRESS"),
]
}),
(
"California 916-806-8324 916-362-5515 3573 Pearl Street 95827 CA Sacramento"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 23, "MOBILE_NUMBER"),
(24, 36, "TELEPHONE_NUMBER"),
(37, 54, "STREET_ADDRESS"),
(55, 60, "ZIPCODE"),
(61, 63, "STATE"),
(64, 74, "CITY"),
]
}),
(
"916-806-8324 CA 95827 916-362-5515 California 3573 Pearl Street Sacramento"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 15, "STATE"),
(16, 21, "ZIPCODE"),
(22, 34, "TELEPHONE_NUMBER"),
(35, 45, "STATE_FULL"),
(46, 63, "STREET_ADDRESS"),
(64, 74, "CITY"),
]
}),
(
"916-362-5515 CA Sacramento 3573 Pearl Street 95827 916-806-8324 California"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 15, "STATE"),
(16, 26, "CITY"),
(27, 44, "STREET_ADDRESS"),
(45, 50, "ZIPCODE"),
(51, 63, "MOBILE_NUMBER"),
(64, 74, "STATE_FULL"),
]
}),
(
"Sacramento 95827 916-806-8324 California 3573 Pearl Street CA 916-362-5515"
, {
"entities":[
(0, 10, "CITY"),
(11, 16, "ZIPCODE"),
(17, 29, "MOBILE_NUMBER"),
(30, 40, "STATE_FULL"),
(41, 58, "STREET_ADDRESS"),
(59, 61, "STATE"),
(62, 74, "TELEPHONE_NUMBER"),
]
}),
(
"California CA 3573 Pearl Street Sacramento 95827 916-362-5515 916-806-8324"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 13, "STATE"),
(14, 31, "STREET_ADDRESS"),
(32, 42, "CITY"),
(43, 48, "ZIPCODE"),
(49, 61, "TELEPHONE_NUMBER"),
(62, 74, "MOBILE_NUMBER"),
]
}),
(
"714-301-2713 CA 714-315-9441 Anaheim California 3859 Maple Street 92805"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 15, "STATE"),
(16, 28, "MOBILE_NUMBER"),
(29, 36, "CITY"),
(37, 47, "STATE_FULL"),
(48, 65, "STREET_ADDRESS"),
(66, 71, "ZIPCODE"),
]
}),
(
"3859 Maple Street CA 714-301-2713 California Anaheim 714-315-9441 92805"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 20, "STATE"),
(21, 33, "TELEPHONE_NUMBER"),
(34, 44, "STATE_FULL"),
(45, 52, "CITY"),
(53, 65, "MOBILE_NUMBER"),
(66, 71, "ZIPCODE"),
]
}),
(
"Anaheim California 714-315-9441 CA 92805 3859 Maple Street 714-301-2713"
, {
"entities":[
(0, 7, "CITY"),
(8, 18, "STATE_FULL"),
(19, 31, "MOBILE_NUMBER"),
(32, 34, "STATE"),
(35, 40, "ZIPCODE"),
(41, 58, "STREET_ADDRESS"),
(59, 71, "TELEPHONE_NUMBER"),
]
}),
(
"CA Anaheim 3859 Maple Street 714-315-9441 92805 California 714-301-2713"
, {
"entities":[
(0, 2, "STATE"),
(3, 10, "CITY"),
(11, 28, "STREET_ADDRESS"),
(29, 41, "MOBILE_NUMBER"),
(42, 47, "ZIPCODE"),
(48, 58, "STATE_FULL"),
(59, 71, "TELEPHONE_NUMBER"),
]
}),
(
"3859 Maple Street California 92805 Anaheim 714-315-9441 714-301-2713 CA"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 28, "STATE_FULL"),
(29, 34, "ZIPCODE"),
(35, 42, "CITY"),
(43, 55, "MOBILE_NUMBER"),
(56, 68, "TELEPHONE_NUMBER"),
(69, 71, "STATE"),
]
}),
(
"714-315-9441 3859 Maple Street Anaheim CA 714-301-2713 92805 California"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 30, "STREET_ADDRESS"),
(31, 38, "CITY"),
(39, 41, "STATE"),
(42, 54, "TELEPHONE_NUMBER"),
(55, 60, "ZIPCODE"),
(61, 71, "STATE_FULL"),
]
}),
(
"714-301-2713 CA 714-315-9441 3859 Maple Street California 92805 Anaheim"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 15, "STATE"),
(16, 28, "MOBILE_NUMBER"),
(29, 46, "STREET_ADDRESS"),
(47, 57, "STATE_FULL"),
(58, 63, "ZIPCODE"),
(64, 71, "CITY"),
]
}),
(
"714-315-9441 3859 Maple Street California 92805 CA 714-301-2713 Anaheim"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 30, "STREET_ADDRESS"),
(31, 41, "STATE_FULL"),
(42, 47, "ZIPCODE"),
(48, 50, "STATE"),
(51, 63, "TELEPHONE_NUMBER"),
(64, 71, "CITY"),
]
}),
(
"92805 California 714-315-9441 3859 Maple Street CA Anaheim 714-301-2713"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 16, "STATE_FULL"),
(17, 29, "MOBILE_NUMBER"),
(30, 47, "STREET_ADDRESS"),
(48, 50, "STATE"),
(51, 58, "CITY"),
(59, 71, "TELEPHONE_NUMBER"),
]
}),
(
"CA California 714-301-2713 3859 Maple Street Anaheim 92805 714-315-9441"
, {
"entities":[
(0, 2, "STATE"),
(3, 13, "STATE_FULL"),
(14, 26, "TELEPHONE_NUMBER"),
(27, 44, "STREET_ADDRESS"),
(45, 52, "CITY"),
(53, 58, "ZIPCODE"),
(59, 71, "MOBILE_NUMBER"),
]
}),
(
"4438 Lochmere Lane 860-370-9877 Connecticut 860-268-4851 CT 06040 Manchester"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 31, "TELEPHONE_NUMBER"),
(32, 43, "STATE_FULL"),
(44, 56, "MOBILE_NUMBER"),
(57, 59, "STATE"),
(60, 65, "ZIPCODE"),
(66, 76, "CITY"),
]
}),
(
"4438 Lochmere Lane Manchester 860-268-4851 860-370-9877 CT Connecticut 06040"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 29, "CITY"),
(30, 42, "MOBILE_NUMBER"),
(43, 55, "TELEPHONE_NUMBER"),
(56, 58, "STATE"),
(59, 70, "STATE_FULL"),
(71, 76, "ZIPCODE"),
]
}),
(
"CT Manchester 860-268-4851 4438 Lochmere Lane 860-370-9877 Connecticut 06040"
, {
"entities":[
(0, 2, "STATE"),
(3, 13, "CITY"),
(14, 26, "MOBILE_NUMBER"),
(27, 45, "STREET_ADDRESS"),
(46, 58, "TELEPHONE_NUMBER"),
(59, 70, "STATE_FULL"),
(71, 76, "ZIPCODE"),
]
}),
(
"4438 Lochmere Lane 860-370-9877 06040 Connecticut CT Manchester 860-268-4851"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 31, "TELEPHONE_NUMBER"),
(32, 37, "ZIPCODE"),
(38, 49, "STATE_FULL"),
(50, 52, "STATE"),
(53, 63, "CITY"),
(64, 76, "MOBILE_NUMBER"),
]
}),
(
"4438 Lochmere Lane 06040 860-370-9877 Manchester Connecticut 860-268-4851 CT"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 24, "ZIPCODE"),
(25, 37, "TELEPHONE_NUMBER"),
(38, 48, "CITY"),
(49, 60, "STATE_FULL"),
(61, 73, "MOBILE_NUMBER"),
(74, 76, "STATE"),
]
}),
(
"860-268-4851 4438 Lochmere Lane Manchester CT Connecticut 06040 860-370-9877"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 31, "STREET_ADDRESS"),
(32, 42, "CITY"),
(43, 45, "STATE"),
(46, 57, "STATE_FULL"),
(58, 63, "ZIPCODE"),
(64, 76, "TELEPHONE_NUMBER"),
]
}),
(
"Connecticut 4438 Lochmere Lane CT 860-268-4851 Manchester 860-370-9877 06040"
, {
"entities":[
(0, 11, "STATE_FULL"),
(12, 30, "STREET_ADDRESS"),
(31, 33, "STATE"),
(34, 46, "MOBILE_NUMBER"),
(47, 57, "CITY"),
(58, 70, "TELEPHONE_NUMBER"),
(71, 76, "ZIPCODE"),
]
}),
(
"860-268-4851 CT Connecticut Manchester 06040 860-370-9877 4438 Lochmere Lane"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 15, "STATE"),
(16, 27, "STATE_FULL"),
(28, 38, "CITY"),
(39, 44, "ZIPCODE"),
(45, 57, "TELEPHONE_NUMBER"),
(58, 76, "STREET_ADDRESS"),
]
}),
(
"860-268-4851 06040 860-370-9877 4438 Lochmere Lane CT Connecticut Manchester"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 31, "TELEPHONE_NUMBER"),
(32, 50, "STREET_ADDRESS"),
(51, 53, "STATE"),
(54, 65, "STATE_FULL"),
(66, 76, "CITY"),
]
}),
(
"860-370-9877 Connecticut 4438 Lochmere Lane Manchester CT 06040 860-268-4851"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 24, "STATE_FULL"),
(25, 43, "STREET_ADDRESS"),
(44, 54, "CITY"),
(55, 57, "STATE"),
(58, 63, "ZIPCODE"),
(64, 76, "MOBILE_NUMBER"),
]
}),
(
"301-780-0752 1801 Bluff Street 20772 Upper Marlboro MD Maryland 443-680-5032"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 30, "STREET_ADDRESS"),
(31, 36, "ZIPCODE"),
(37, 51, "CITY"),
(52, 54, "STATE"),
(55, 63, "STATE_FULL"),
(64, 76, "MOBILE_NUMBER"),
]
}),
(
"301-780-0752 20772 443-680-5032 Upper Marlboro MD Maryland 1801 Bluff Street"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 31, "MOBILE_NUMBER"),
(32, 46, "CITY"),
(47, 49, "STATE"),
(50, 58, "STATE_FULL"),
(59, 76, "STREET_ADDRESS"),
]
}),
(
"443-680-5032 20772 301-780-0752 Maryland 1801 Bluff Street Upper Marlboro MD"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 31, "TELEPHONE_NUMBER"),
(32, 40, "STATE_FULL"),
(41, 58, "STREET_ADDRESS"),
(59, 73, "CITY"),
(74, 76, "STATE"),
]
}),
(
"301-780-0752 20772 MD 443-680-5032 Maryland 1801 Bluff Street Upper Marlboro"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 21, "STATE"),
(22, 34, "MOBILE_NUMBER"),
(35, 43, "STATE_FULL"),
(44, 61, "STREET_ADDRESS"),
(62, 76, "CITY"),
]
}),
(
"Upper Marlboro 301-780-0752 20772 1801 Bluff Street 443-680-5032 MD Maryland"
, {
"entities":[
(0, 14, "CITY"),
(15, 27, "TELEPHONE_NUMBER"),
(28, 33, "ZIPCODE"),
(34, 51, "STREET_ADDRESS"),
(52, 64, "MOBILE_NUMBER"),
(65, 67, "STATE"),
(68, 76, "STATE_FULL"),
]
}),
(
"Upper Marlboro 443-680-5032 20772 MD Maryland 1801 Bluff Street 301-780-0752"
, {
"entities":[
(0, 14, "CITY"),
(15, 27, "MOBILE_NUMBER"),
(28, 33, "ZIPCODE"),
(34, 36, "STATE"),
(37, 45, "STATE_FULL"),
(46, 63, "STREET_ADDRESS"),
(64, 76, "TELEPHONE_NUMBER"),
]
}),
(
"301-780-0752 Upper Marlboro Maryland 443-680-5032 MD 20772 1801 Bluff Street"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 27, "CITY"),
(28, 36, "STATE_FULL"),
(37, 49, "MOBILE_NUMBER"),
(50, 52, "STATE"),
(53, 58, "ZIPCODE"),
(59, 76, "STREET_ADDRESS"),
]
}),
(
"Maryland 1801 Bluff Street 301-780-0752 443-680-5032 Upper Marlboro MD 20772"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 26, "STREET_ADDRESS"),
(27, 39, "TELEPHONE_NUMBER"),
(40, 52, "MOBILE_NUMBER"),
(53, 67, "CITY"),
(68, 70, "STATE"),
(71, 76, "ZIPCODE"),
]
}),
(
"MD Upper Marlboro 20772 1801 Bluff Street 301-780-0752 Maryland 443-680-5032"
, {
"entities":[
(0, 2, "STATE"),
(3, 17, "CITY"),
(18, 23, "ZIPCODE"),
(24, 41, "STREET_ADDRESS"),
(42, 54, "TELEPHONE_NUMBER"),
(55, 63, "STATE_FULL"),
(64, 76, "MOBILE_NUMBER"),
]
}),
(
"MD 20772 Maryland 1801 Bluff Street Upper Marlboro 443-680-5032 301-780-0752"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 17, "STATE_FULL"),
(18, 35, "STREET_ADDRESS"),
(36, 50, "CITY"),
(51, 63, "MOBILE_NUMBER"),
(64, 76, "TELEPHONE_NUMBER"),
]
}),
(
"42301 2756 Glen Street Owensboro 270-313-6201 KY 270-570-4302 Kentucky"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 22, "STREET_ADDRESS"),
(23, 32, "CITY"),
(33, 45, "TELEPHONE_NUMBER"),
(46, 48, "STATE"),
(49, 61, "MOBILE_NUMBER"),
(62, 70, "STATE_FULL"),
]
}),
(
"2756 Glen Street 42301 270-313-6201 KY Owensboro Kentucky 270-570-4302"
, {
"entities":[
(0, 16, "STREET_ADDRESS"),
(17, 22, "ZIPCODE"),
(23, 35, "TELEPHONE_NUMBER"),
(36, 38, "STATE"),
(39, 48, "CITY"),
(49, 57, "STATE_FULL"),
(58, 70, "MOBILE_NUMBER"),
]
}),
(
"2756 Glen Street Kentucky Owensboro 270-570-4302 270-313-6201 42301 KY"
, {
"entities":[
(0, 16, "STREET_ADDRESS"),
(17, 25, "STATE_FULL"),
(26, 35, "CITY"),
(36, 48, "MOBILE_NUMBER"),
(49, 61, "TELEPHONE_NUMBER"),
(62, 67, "ZIPCODE"),
(68, 70, "STATE"),
]
}),
(
"42301 Owensboro 270-570-4302 Kentucky 2756 Glen Street 270-313-6201 KY"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 15, "CITY"),
(16, 28, "MOBILE_NUMBER"),
(29, 37, "STATE_FULL"),
(38, 54, "STREET_ADDRESS"),
(55, 67, "TELEPHONE_NUMBER"),
(68, 70, "STATE"),
]
}),
(
"KY 2756 Glen Street Owensboro 270-313-6201 Kentucky 270-570-4302 42301"
, {
"entities":[
(0, 2, "STATE"),
(3, 19, "STREET_ADDRESS"),
(20, 29, "CITY"),
(30, 42, "TELEPHONE_NUMBER"),
(43, 51, "STATE_FULL"),
(52, 64, "MOBILE_NUMBER"),
(65, 70, "ZIPCODE"),
]
}),
(
"Owensboro Kentucky 42301 KY 2756 Glen Street 270-313-6201 270-570-4302"
, {
"entities":[
(0, 9, "CITY"),
(10, 18, "STATE_FULL"),
(19, 24, "ZIPCODE"),
(25, 27, "STATE"),
(28, 44, "STREET_ADDRESS"),
(45, 57, "TELEPHONE_NUMBER"),
(58, 70, "MOBILE_NUMBER"),
]
}),
(
"270-313-6201 Kentucky Owensboro 270-570-4302 KY 2756 Glen Street 42301"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 21, "STATE_FULL"),
(22, 31, "CITY"),
(32, 44, "MOBILE_NUMBER"),
(45, 47, "STATE"),
(48, 64, "STREET_ADDRESS"),
(65, 70, "ZIPCODE"),
]
}),
(
"Kentucky KY Owensboro 42301 270-570-4302 2756 Glen Street 270-313-6201"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 11, "STATE"),
(12, 21, "CITY"),
(22, 27, "ZIPCODE"),
(28, 40, "MOBILE_NUMBER"),
(41, 57, "STREET_ADDRESS"),
(58, 70, "TELEPHONE_NUMBER"),
]
}),
(
"270-570-4302 42301 2756 Glen Street Kentucky KY 270-313-6201 Owensboro"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 35, "STREET_ADDRESS"),
(36, 44, "STATE_FULL"),
(45, 47, "STATE"),
(48, 60, "TELEPHONE_NUMBER"),
(61, 70, "CITY"),
]
}),
(
"270-313-6201 KY Owensboro 2756 Glen Street 42301 270-570-4302 Kentucky"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 15, "STATE"),
(16, 25, "CITY"),
(26, 42, "STREET_ADDRESS"),
(43, 48, "ZIPCODE"),
(49, 61, "MOBILE_NUMBER"),
(62, 70, "STATE_FULL"),
]
}),
(
"Oregon 541-870-1895 Eugene 541-543-4739 OR 937 Haymond Rocks Road 97408"
, {
"entities":[
(0, 6, "STATE_FULL"),
(7, 19, "MOBILE_NUMBER"),
(20, 26, "CITY"),
(27, 39, "TELEPHONE_NUMBER"),
(40, 42, "STATE"),
(43, 65, "STREET_ADDRESS"),
(66, 71, "ZIPCODE"),
]
}),
(
"937 Haymond Rocks Road OR Eugene 541-870-1895 Oregon 97408 541-543-4739"
, {
"entities":[
(0, 22, "STREET_ADDRESS"),
(23, 25, "STATE"),
(26, 32, "CITY"),
(33, 45, "MOBILE_NUMBER"),
(46, 52, "STATE_FULL"),
(53, 58, "ZIPCODE"),
(59, 71, "TELEPHONE_NUMBER"),
]
}),
(
"Oregon 541-870-1895 Eugene 541-543-4739 OR 937 Haymond Rocks Road 97408"
, {
"entities":[
(0, 6, "STATE_FULL"),
(7, 19, "MOBILE_NUMBER"),
(20, 26, "CITY"),
(27, 39, "TELEPHONE_NUMBER"),
(40, 42, "STATE"),
(43, 65, "STREET_ADDRESS"),
(66, 71, "ZIPCODE"),
]
}),
(
"541-870-1895 Eugene OR Oregon 937 Haymond Rocks Road 97408 541-543-4739"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 19, "CITY"),
(20, 22, "STATE"),
(23, 29, "STATE_FULL"),
(30, 52, "STREET_ADDRESS"),
(53, 58, "ZIPCODE"),
(59, 71, "TELEPHONE_NUMBER"),
]
}),
(
"541-870-1895 541-543-4739 97408 937 Haymond Rocks Road Eugene OR Oregon"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 25, "TELEPHONE_NUMBER"),
(26, 31, "ZIPCODE"),
(32, 54, "STREET_ADDRESS"),
(55, 61, "CITY"),
(62, 64, "STATE"),
(65, 71, "STATE_FULL"),
]
}),
(
"97408 937 Haymond Rocks Road 541-870-1895 OR Oregon 541-543-4739 Eugene"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 28, "STREET_ADDRESS"),
(29, 41, "MOBILE_NUMBER"),
(42, 44, "STATE"),
(45, 51, "STATE_FULL"),
(52, 64, "TELEPHONE_NUMBER"),
(65, 71, "CITY"),
]
}),
(
"541-870-1895 937 Haymond Rocks Road OR Eugene Oregon 541-543-4739 97408"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 35, "STREET_ADDRESS"),
(36, 38, "STATE"),
(39, 45, "CITY"),
(46, 52, "STATE_FULL"),
(53, 65, "TELEPHONE_NUMBER"),
(66, 71, "ZIPCODE"),
]
}),
(
"541-543-4739 Oregon 97408 937 Haymond Rocks Road Eugene 541-870-1895 OR"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 19, "STATE_FULL"),
(20, 25, "ZIPCODE"),
(26, 48, "STREET_ADDRESS"),
(49, 55, "CITY"),
(56, 68, "MOBILE_NUMBER"),
(69, 71, "STATE"),
]
}),
(
"Eugene Oregon 97408 937 Haymond Rocks Road 541-870-1895 OR 541-543-4739"
, {
"entities":[
(0, 6, "CITY"),
(7, 13, "STATE_FULL"),
(14, 19, "ZIPCODE"),
(20, 42, "STREET_ADDRESS"),
(43, 55, "MOBILE_NUMBER"),
(56, 58, "STATE"),
(59, 71, "TELEPHONE_NUMBER"),
]
}),
(
"541-870-1895 541-543-4739 Eugene 937 Haymond Rocks Road 97408 OR Oregon"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 25, "TELEPHONE_NUMBER"),
(26, 32, "CITY"),
(33, 55, "STREET_ADDRESS"),
(56, 61, "ZIPCODE"),
(62, 64, "STATE"),
(65, 71, "STATE_FULL"),
]
}),
(
"27292 NC Lexington North Carolina 336-247-7975 336-239-7470 4659 Bryan Street"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 18, "CITY"),
(19, 33, "STATE_FULL"),
(34, 46, "TELEPHONE_NUMBER"),
(47, 59, "MOBILE_NUMBER"),
(60, 77, "STREET_ADDRESS"),
]
}),
(
"4659 Bryan Street 336-247-7975 336-239-7470 North Carolina 27292 NC Lexington"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 30, "TELEPHONE_NUMBER"),
(31, 43, "MOBILE_NUMBER"),
(44, 58, "STATE_FULL"),
(59, 64, "ZIPCODE"),
(65, 67, "STATE"),
(68, 77, "CITY"),
]
}),
(
"27292 Lexington 336-247-7975 336-239-7470 North Carolina 4659 Bryan Street NC"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 15, "CITY"),
(16, 28, "TELEPHONE_NUMBER"),
(29, 41, "MOBILE_NUMBER"),
(42, 56, "STATE_FULL"),
(57, 74, "STREET_ADDRESS"),
(75, 77, "STATE"),
]
}),
(
"NC Lexington 27292 336-247-7975 336-239-7470 North Carolina 4659 Bryan Street"
, {
"entities":[
(0, 2, "STATE"),
(3, 12, "CITY"),
(13, 18, "ZIPCODE"),
(19, 31, "TELEPHONE_NUMBER"),
(32, 44, "MOBILE_NUMBER"),
(45, 59, "STATE_FULL"),
(60, 77, "STREET_ADDRESS"),
]
}),
(
"Lexington NC 336-247-7975 North Carolina 4659 Bryan Street 336-239-7470 27292"
, {
"entities":[
(0, 9, "CITY"),
(10, 12, "STATE"),
(13, 25, "TELEPHONE_NUMBER"),
(26, 40, "STATE_FULL"),
(41, 58, "STREET_ADDRESS"),
(59, 71, "MOBILE_NUMBER"),
(72, 77, "ZIPCODE"),
]
}),
(
"NC 336-239-7470 North Carolina 27292 4659 Bryan Street Lexington 336-247-7975"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "MOBILE_NUMBER"),
(16, 30, "STATE_FULL"),
(31, 36, "ZIPCODE"),
(37, 54, "STREET_ADDRESS"),
(55, 64, "CITY"),
(65, 77, "TELEPHONE_NUMBER"),
]
}),
(
"336-239-7470 336-247-7975 Lexington 4659 Bryan Street 27292 NC North Carolina"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 25, "TELEPHONE_NUMBER"),
(26, 35, "CITY"),
(36, 53, "STREET_ADDRESS"),
(54, 59, "ZIPCODE"),
(60, 62, "STATE"),
(63, 77, "STATE_FULL"),
]
}),
(
"336-247-7975 27292 4659 Bryan Street Lexington North Carolina 336-239-7470 NC"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 36, "STREET_ADDRESS"),
(37, 46, "CITY"),
(47, 61, "STATE_FULL"),
(62, 74, "MOBILE_NUMBER"),
(75, 77, "STATE"),
]
}),
(
"336-239-7470 Lexington 336-247-7975 4659 Bryan Street North Carolina NC 27292"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 22, "CITY"),
(23, 35, "TELEPHONE_NUMBER"),
(36, 53, "STREET_ADDRESS"),
(54, 68, "STATE_FULL"),
(69, 71, "STATE"),
(72, 77, "ZIPCODE"),
]
}),
(
"336-247-7975 336-239-7470 North Carolina 27292 Lexington 4659 Bryan Street NC"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 25, "MOBILE_NUMBER"),
(26, 40, "STATE_FULL"),
(41, 46, "ZIPCODE"),
(47, 56, "CITY"),
(57, 74, "STREET_ADDRESS"),
(75, 77, "STATE"),
]
}),
(
"Virginia 778 Daffodil Lane 703-657-7023 22070 703-430-5886 VA Herndon"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 26, "STREET_ADDRESS"),
(27, 39, "MOBILE_NUMBER"),
(40, 45, "ZIPCODE"),
(46, 58, "TELEPHONE_NUMBER"),
(59, 61, "STATE"),
(62, 69, "CITY"),
]
}),
(
"703-430-5886 Herndon VA 22070 Virginia 778 Daffodil Lane 703-657-7023"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 20, "CITY"),
(21, 23, "STATE"),
(24, 29, "ZIPCODE"),
(30, 38, "STATE_FULL"),
(39, 56, "STREET_ADDRESS"),
(57, 69, "MOBILE_NUMBER"),
]
}),
(
"778 Daffodil Lane 22070 703-657-7023 Virginia 703-430-5886 VA Herndon"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 23, "ZIPCODE"),
(24, 36, "MOBILE_NUMBER"),
(37, 45, "STATE_FULL"),
(46, 58, "TELEPHONE_NUMBER"),
(59, 61, "STATE"),
(62, 69, "CITY"),
]
}),
(
"Virginia 778 Daffodil Lane VA 703-657-7023 Herndon 22070 703-430-5886"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 26, "STREET_ADDRESS"),
(27, 29, "STATE"),
(30, 42, "MOBILE_NUMBER"),
(43, 50, "CITY"),
(51, 56, "ZIPCODE"),
(57, 69, "TELEPHONE_NUMBER"),
]
}),
(
"Herndon VA 22070 778 Daffodil Lane 703-430-5886 703-657-7023 Virginia"
, {
"entities":[
(0, 7, "CITY"),
(8, 10, "STATE"),
(11, 16, "ZIPCODE"),
(17, 34, "STREET_ADDRESS"),
(35, 47, "TELEPHONE_NUMBER"),
(48, 60, "MOBILE_NUMBER"),
(61, 69, "STATE_FULL"),
]
}),
(
"Herndon 22070 778 Daffodil Lane 703-657-7023 Virginia 703-430-5886 VA"
, {
"entities":[
(0, 7, "CITY"),
(8, 13, "ZIPCODE"),
(14, 31, "STREET_ADDRESS"),
(32, 44, "MOBILE_NUMBER"),
(45, 53, "STATE_FULL"),
(54, 66, "TELEPHONE_NUMBER"),
(67, 69, "STATE"),
]
}),
(
"703-657-7023 22070 703-430-5886 778 Daffodil Lane Herndon VA Virginia"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 31, "TELEPHONE_NUMBER"),
(32, 49, "STREET_ADDRESS"),
(50, 57, "CITY"),
(58, 60, "STATE"),
(61, 69, "STATE_FULL"),
]
}),
(
"Herndon VA Virginia 703-430-5886 703-657-7023 22070 778 Daffodil Lane"
, {
"entities":[
(0, 7, "CITY"),
(8, 10, "STATE"),
(11, 19, "STATE_FULL"),
(20, 32, "TELEPHONE_NUMBER"),
(33, 45, "MOBILE_NUMBER"),
(46, 51, "ZIPCODE"),
(52, 69, "STREET_ADDRESS"),
]
}),
(
"703-657-7023 VA Virginia 778 Daffodil Lane 22070 Herndon 703-430-5886"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 15, "STATE"),
(16, 24, "STATE_FULL"),
(25, 42, "STREET_ADDRESS"),
(43, 48, "ZIPCODE"),
(49, 56, "CITY"),
(57, 69, "TELEPHONE_NUMBER"),
]
}),
(
"22070 Herndon VA Virginia 778 Daffodil Lane 703-430-5886 703-657-7023"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 13, "CITY"),
(14, 16, "STATE"),
(17, 25, "STATE_FULL"),
(26, 43, "STREET_ADDRESS"),
(44, 56, "TELEPHONE_NUMBER"),
(57, 69, "MOBILE_NUMBER"),
]
}),
(
"850-290-3893 Madison 1178 Virgil Street 32340 904-918-7436 Florida FL"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 20, "CITY"),
(21, 39, "STREET_ADDRESS"),
(40, 45, "ZIPCODE"),
(46, 58, "MOBILE_NUMBER"),
(59, 66, "STATE_FULL"),
(67, 69, "STATE"),
]
}),
(
"FL 904-918-7436 Madison 1178 Virgil Street 850-290-3893 32340 Florida"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "MOBILE_NUMBER"),
(16, 23, "CITY"),
(24, 42, "STREET_ADDRESS"),
(43, 55, "TELEPHONE_NUMBER"),
(56, 61, "ZIPCODE"),
(62, 69, "STATE_FULL"),
]
}),
(
"850-290-3893 Florida Madison 32340 904-918-7436 FL 1178 Virgil Street"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 20, "STATE_FULL"),
(21, 28, "CITY"),
(29, 34, "ZIPCODE"),
(35, 47, "MOBILE_NUMBER"),
(48, 50, "STATE"),
(51, 69, "STREET_ADDRESS"),
]
}),
(
"32340 Madison FL Florida 850-290-3893 1178 Virgil Street 904-918-7436"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 13, "CITY"),
(14, 16, "STATE"),
(17, 24, "STATE_FULL"),
(25, 37, "TELEPHONE_NUMBER"),
(38, 56, "STREET_ADDRESS"),
(57, 69, "MOBILE_NUMBER"),
]
}),
(
"32340 FL 1178 Virgil Street Florida 850-290-3893 904-918-7436 Madison"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 27, "STREET_ADDRESS"),
(28, 35, "STATE_FULL"),
(36, 48, "TELEPHONE_NUMBER"),
(49, 61, "MOBILE_NUMBER"),
(62, 69, "CITY"),
]
}),
(
"Florida 1178 Virgil Street 32340 Madison 904-918-7436 850-290-3893 FL"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 26, "STREET_ADDRESS"),
(27, 32, "ZIPCODE"),
(33, 40, "CITY"),
(41, 53, "MOBILE_NUMBER"),
(54, 66, "TELEPHONE_NUMBER"),
(67, 69, "STATE"),
]
}),
(
"850-290-3893 Madison 1178 Virgil Street FL 904-918-7436 32340 Florida"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 20, "CITY"),
(21, 39, "STREET_ADDRESS"),
(40, 42, "STATE"),
(43, 55, "MOBILE_NUMBER"),
(56, 61, "ZIPCODE"),
(62, 69, "STATE_FULL"),
]
}),
(
"850-290-3893 Madison 1178 Virgil Street FL Florida 32340 904-918-7436"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 20, "CITY"),
(21, 39, "STREET_ADDRESS"),
(40, 42, "STATE"),
(43, 50, "STATE_FULL"),
(51, 56, "ZIPCODE"),
(57, 69, "MOBILE_NUMBER"),
]
}),
(
"Florida 32340 Madison 904-918-7436 850-290-3893 FL 1178 Virgil Street"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 13, "ZIPCODE"),
(14, 21, "CITY"),
(22, 34, "MOBILE_NUMBER"),
(35, 47, "TELEPHONE_NUMBER"),
(48, 50, "STATE"),
(51, 69, "STREET_ADDRESS"),
]
}),
(
"FL 850-290-3893 Florida 904-918-7436 1178 Virgil Street Madison 32340"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "TELEPHONE_NUMBER"),
(16, 23, "STATE_FULL"),
(24, 36, "MOBILE_NUMBER"),
(37, 55, "STREET_ADDRESS"),
(56, 63, "CITY"),
(64, 69, "ZIPCODE"),
]
}),
(
"3826 Lyon Avenue Massachusetts 781-367-0128 01801 508-933-9890 Woburn MA"
, {
"entities":[
(0, 16, "STREET_ADDRESS"),
(17, 30, "STATE_FULL"),
(31, 43, "MOBILE_NUMBER"),
(44, 49, "ZIPCODE"),
(50, 62, "TELEPHONE_NUMBER"),
(63, 69, "CITY"),
(70, 72, "STATE"),
]
}),
(
"01801 MA Massachusetts Woburn 781-367-0128 3826 Lyon Avenue 508-933-9890"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 22, "STATE_FULL"),
(23, 29, "CITY"),
(30, 42, "MOBILE_NUMBER"),
(43, 59, "STREET_ADDRESS"),
(60, 72, "TELEPHONE_NUMBER"),
]
}),
(
"Woburn 3826 Lyon Avenue 508-933-9890 01801 MA Massachusetts 781-367-0128"
, {
"entities":[
(0, 6, "CITY"),
(7, 23, "STREET_ADDRESS"),
(24, 36, "TELEPHONE_NUMBER"),
(37, 42, "ZIPCODE"),
(43, 45, "STATE"),
(46, 59, "STATE_FULL"),
(60, 72, "MOBILE_NUMBER"),
]
}),
(
"508-933-9890 3826 Lyon Avenue 781-367-0128 Massachusetts Woburn 01801 MA"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 29, "STREET_ADDRESS"),
(30, 42, "MOBILE_NUMBER"),
(43, 56, "STATE_FULL"),
(57, 63, "CITY"),
(64, 69, "ZIPCODE"),
(70, 72, "STATE"),
]
}),
(
"3826 Lyon Avenue 781-367-0128 Woburn MA 508-933-9890 01801 Massachusetts"
, {
"entities":[
(0, 16, "STREET_ADDRESS"),
(17, 29, "MOBILE_NUMBER"),
(30, 36, "CITY"),
(37, 39, "STATE"),
(40, 52, "TELEPHONE_NUMBER"),
(53, 58, "ZIPCODE"),
(59, 72, "STATE_FULL"),
]
}),
(
"MA Massachusetts 508-933-9890 781-367-0128 Woburn 01801 3826 Lyon Avenue"
, {
"entities":[
(0, 2, "STATE"),
(3, 16, "STATE_FULL"),
(17, 29, "TELEPHONE_NUMBER"),
(30, 42, "MOBILE_NUMBER"),
(43, 49, "CITY"),
(50, 55, "ZIPCODE"),
(56, 72, "STREET_ADDRESS"),
]
}),
(
"781-367-0128 MA Woburn 508-933-9890 3826 Lyon Avenue Massachusetts 01801"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 15, "STATE"),
(16, 22, "CITY"),
(23, 35, "TELEPHONE_NUMBER"),
(36, 52, "STREET_ADDRESS"),
(53, 66, "STATE_FULL"),
(67, 72, "ZIPCODE"),
]
}),
(
"3826 Lyon Avenue 508-933-9890 Woburn 01801 Massachusetts MA 781-367-0128"
, {
"entities":[
(0, 16, "STREET_ADDRESS"),
(17, 29, "TELEPHONE_NUMBER"),
(30, 36, "CITY"),
(37, 42, "ZIPCODE"),
(43, 56, "STATE_FULL"),
(57, 59, "STATE"),
(60, 72, "MOBILE_NUMBER"),
]
}),
(
"MA 781-367-0128 01801 Woburn Massachusetts 508-933-9890 3826 Lyon Avenue"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "MOBILE_NUMBER"),
(16, 21, "ZIPCODE"),
(22, 28, "CITY"),
(29, 42, "STATE_FULL"),
(43, 55, "TELEPHONE_NUMBER"),
(56, 72, "STREET_ADDRESS"),
]
}),
(
"Woburn 508-933-9890 3826 Lyon Avenue Massachusetts 01801 MA 781-367-0128"
, {
"entities":[
(0, 6, "CITY"),
(7, 19, "TELEPHONE_NUMBER"),
(20, 36, "STREET_ADDRESS"),
(37, 50, "STATE_FULL"),
(51, 56, "ZIPCODE"),
(57, 59, "STATE"),
(60, 72, "MOBILE_NUMBER"),
]
}),
(
"New York 917-365-2237 4224 Geraldine Lane 646-359-9220 New York NY 10011"
, {
"entities":[
(0, 8, "CITY"),
(9, 21, "MOBILE_NUMBER"),
(22, 41, "STREET_ADDRESS"),
(42, 54, "TELEPHONE_NUMBER"),
(55, 63, "STATE_FULL"),
(64, 66, "STATE"),
(67, 72, "ZIPCODE"),
]
}),
(
"4224 Geraldine Lane 646-359-9220 10011 917-365-2237 NY New York New York"
, {
"entities":[
(0, 19, "STREET_ADDRESS"),
(20, 32, "TELEPHONE_NUMBER"),
(33, 38, "ZIPCODE"),
(39, 51, "MOBILE_NUMBER"),
(52, 54, "STATE"),
(55, 63, "STATE_FULL"),
(64, 72, "CITY"),
]
}),
(
"New York New York NY 646-359-9220 4224 Geraldine Lane 10011 917-365-2237"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 17, "CITY"),
(18, 20, "STATE"),
(21, 33, "TELEPHONE_NUMBER"),
(34, 53, "STREET_ADDRESS"),
(54, 59, "ZIPCODE"),
(60, 72, "MOBILE_NUMBER"),
]
}),
(
"NY 646-359-9220 New York 917-365-2237 4224 Geraldine Lane 10011 New York"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "TELEPHONE_NUMBER"),
(16, 24, "CITY"),
(25, 37, "MOBILE_NUMBER"),
(38, 57, "STREET_ADDRESS"),
(58, 63, "ZIPCODE"),
(64, 72, "STATE_FULL"),
]
}),
(
"New York 917-365-2237 NY 4224 Geraldine Lane New York 10011 646-359-9220"
, {
"entities":[
(0, 8, "CITY"),
(9, 21, "MOBILE_NUMBER"),
(22, 24, "STATE"),
(25, 44, "STREET_ADDRESS"),
(45, 53, "STATE_FULL"),
(54, 59, "ZIPCODE"),
(60, 72, "TELEPHONE_NUMBER"),
]
}),
(
"10011 646-359-9220 New York 917-365-2237 4224 Geraldine Lane New York NY"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "TELEPHONE_NUMBER"),
(19, 27, "STATE_FULL"),
(28, 40, "MOBILE_NUMBER"),
(41, 60, "STREET_ADDRESS"),
(61, 69, "CITY"),
(70, 72, "STATE"),
]
}),
(
"10011 917-365-2237 New York NY New York 646-359-9220 4224 Geraldine Lane"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "MOBILE_NUMBER"),
(19, 27, "STATE_FULL"),
(28, 30, "STATE"),
(31, 39, "CITY"),
(40, 52, "TELEPHONE_NUMBER"),
(53, 72, "STREET_ADDRESS"),
]
}),
(
"646-359-9220 NY New York 917-365-2237 10011 New York 4224 Geraldine Lane"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 15, "STATE"),
(16, 24, "STATE_FULL"),
(25, 37, "MOBILE_NUMBER"),
(38, 43, "ZIPCODE"),
(44, 52, "CITY"),
(53, 72, "STREET_ADDRESS"),
]
}),
(
"917-365-2237 10011 4224 Geraldine Lane New York 646-359-9220 NY New York"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 38, "STREET_ADDRESS"),
(39, 47, "CITY"),
(48, 60, "TELEPHONE_NUMBER"),
(61, 63, "STATE"),
(64, 72, "STATE_FULL"),
]
}),
(
"NY 10011 646-359-9220 4224 Geraldine Lane 917-365-2237 New York New York"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 21, "TELEPHONE_NUMBER"),
(22, 41, "STREET_ADDRESS"),
(42, 54, "MOBILE_NUMBER"),
(55, 63, "CITY"),
(64, 72, "STATE_FULL"),
]
}),
(
"New York 14202 716-362-3525 45 Cameron Road NY 716-289-6614 Buffalo"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 14, "ZIPCODE"),
(15, 27, "TELEPHONE_NUMBER"),
(28, 43, "STREET_ADDRESS"),
(44, 46, "STATE"),
(47, 59, "MOBILE_NUMBER"),
(60, 67, "CITY"),
]
}),
(
"14202 45 Cameron Road 716-362-3525 NY 716-289-6614 New York Buffalo"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 21, "STREET_ADDRESS"),
(22, 34, "TELEPHONE_NUMBER"),
(35, 37, "STATE"),
(38, 50, "MOBILE_NUMBER"),
(51, 59, "STATE_FULL"),
(60, 67, "CITY"),
]
}),
(
"NY 45 Cameron Road Buffalo New York 716-362-3525 14202 716-289-6614"
, {
"entities":[
(0, 2, "STATE"),
(3, 18, "STREET_ADDRESS"),
(19, 26, "CITY"),
(27, 35, "STATE_FULL"),
(36, 48, "TELEPHONE_NUMBER"),
(49, 54, "ZIPCODE"),
(55, 67, "MOBILE_NUMBER"),
]
}),
(
"Buffalo 14202 NY New York 716-289-6614 45 Cameron Road 716-362-3525"
, {
"entities":[
(0, 7, "CITY"),
(8, 13, "ZIPCODE"),
(14, 16, "STATE"),
(17, 25, "STATE_FULL"),
(26, 38, "MOBILE_NUMBER"),
(39, 54, "STREET_ADDRESS"),
(55, 67, "TELEPHONE_NUMBER"),
]
}),
(
"New York NY 45 Cameron Road Buffalo 716-289-6614 716-362-3525 14202"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 11, "STATE"),
(12, 27, "STREET_ADDRESS"),
(28, 35, "CITY"),
(36, 48, "MOBILE_NUMBER"),
(49, 61, "TELEPHONE_NUMBER"),
(62, 67, "ZIPCODE"),
]
}),
(
"45 Cameron Road 716-289-6614 14202 NY New York Buffalo 716-362-3525"
, {
"entities":[
(0, 15, "STREET_ADDRESS"),
(16, 28, "MOBILE_NUMBER"),
(29, 34, "ZIPCODE"),
(35, 37, "STATE"),
(38, 46, "STATE_FULL"),
(47, 54, "CITY"),
(55, 67, "TELEPHONE_NUMBER"),
]
}),
(
"Buffalo 14202 NY 716-362-3525 45 Cameron Road New York 716-289-6614"
, {
"entities":[
(0, 7, "CITY"),
(8, 13, "ZIPCODE"),
(14, 16, "STATE"),
(17, 29, "TELEPHONE_NUMBER"),
(30, 45, "STREET_ADDRESS"),
(46, 54, "STATE_FULL"),
(55, 67, "MOBILE_NUMBER"),
]
}),
(
"NY 716-289-6614 14202 45 Cameron Road New York Buffalo 716-362-3525"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "MOBILE_NUMBER"),
(16, 21, "ZIPCODE"),
(22, 37, "STREET_ADDRESS"),
(38, 46, "STATE_FULL"),
(47, 54, "CITY"),
(55, 67, "TELEPHONE_NUMBER"),
]
}),
(
"Buffalo 716-289-6614 45 Cameron Road 14202 New York NY 716-362-3525"
, {
"entities":[
(0, 7, "CITY"),
(8, 20, "MOBILE_NUMBER"),
(21, 36, "STREET_ADDRESS"),
(37, 42, "ZIPCODE"),
(43, 51, "STATE_FULL"),
(52, 54, "STATE"),
(55, 67, "TELEPHONE_NUMBER"),
]
}),
(
"716-289-6614 Buffalo New York 716-362-3525 45 Cameron Road 14202 NY"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 20, "CITY"),
(21, 29, "STATE_FULL"),
(30, 42, "TELEPHONE_NUMBER"),
(43, 58, "STREET_ADDRESS"),
(59, 64, "ZIPCODE"),
(65, 67, "STATE"),
]
}),
(
"404-201-0953 678-952-2353 30303 Atlanta 397 Mount Olive Road GA Georgia"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 25, "TELEPHONE_NUMBER"),
(26, 31, "ZIPCODE"),
(32, 39, "CITY"),
(40, 60, "STREET_ADDRESS"),
(61, 63, "STATE"),
(64, 71, "STATE_FULL"),
]
}),
(
"GA Atlanta 30303 Georgia 404-201-0953 397 Mount Olive Road 678-952-2353"
, {
"entities":[
(0, 2, "STATE"),
(3, 10, "CITY"),
(11, 16, "ZIPCODE"),
(17, 24, "STATE_FULL"),
(25, 37, "MOBILE_NUMBER"),
(38, 58, "STREET_ADDRESS"),
(59, 71, "TELEPHONE_NUMBER"),
]
}),
(
"404-201-0953 397 Mount Olive Road Georgia GA 678-952-2353 Atlanta 30303"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 33, "STREET_ADDRESS"),
(34, 41, "STATE_FULL"),
(42, 44, "STATE"),
(45, 57, "TELEPHONE_NUMBER"),
(58, 65, "CITY"),
(66, 71, "ZIPCODE"),
]
}),
(
"678-952-2353 Georgia 397 Mount Olive Road GA 30303 404-201-0953 Atlanta"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 20, "STATE_FULL"),
(21, 41, "STREET_ADDRESS"),
(42, 44, "STATE"),
(45, 50, "ZIPCODE"),
(51, 63, "MOBILE_NUMBER"),
(64, 71, "CITY"),
]
}),
(
"GA 397 Mount Olive Road Georgia 30303 Atlanta 678-952-2353 404-201-0953"
, {
"entities":[
(0, 2, "STATE"),
(3, 23, "STREET_ADDRESS"),
(24, 31, "STATE_FULL"),
(32, 37, "ZIPCODE"),
(38, 45, "CITY"),
(46, 58, "TELEPHONE_NUMBER"),
(59, 71, "MOBILE_NUMBER"),
]
}),
(
"30303 404-201-0953 678-952-2353 Georgia Atlanta 397 Mount Olive Road GA"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "MOBILE_NUMBER"),
(19, 31, "TELEPHONE_NUMBER"),
(32, 39, "STATE_FULL"),
(40, 47, "CITY"),
(48, 68, "STREET_ADDRESS"),
(69, 71, "STATE"),
]
}),
(
"30303 Atlanta Georgia 404-201-0953 GA 678-952-2353 397 Mount Olive Road"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 13, "CITY"),
(14, 21, "STATE_FULL"),
(22, 34, "MOBILE_NUMBER"),
(35, 37, "STATE"),
(38, 50, "TELEPHONE_NUMBER"),
(51, 71, "STREET_ADDRESS"),
]
}),
(
"Georgia 404-201-0953 Atlanta 30303 GA 397 Mount Olive Road 678-952-2353"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 20, "MOBILE_NUMBER"),
(21, 28, "CITY"),
(29, 34, "ZIPCODE"),
(35, 37, "STATE"),
(38, 58, "STREET_ADDRESS"),
(59, 71, "TELEPHONE_NUMBER"),
]
}),
(
"Georgia GA 397 Mount Olive Road Atlanta 404-201-0953 678-952-2353 30303"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 10, "STATE"),
(11, 31, "STREET_ADDRESS"),
(32, 39, "CITY"),
(40, 52, "MOBILE_NUMBER"),
(53, 65, "TELEPHONE_NUMBER"),
(66, 71, "ZIPCODE"),
]
}),
(
"30303 Atlanta Georgia GA 678-952-2353 397 Mount Olive Road 404-201-0953"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 13, "CITY"),
(14, 21, "STATE_FULL"),
(22, 24, "STATE"),
(25, 37, "TELEPHONE_NUMBER"),
(38, 58, "STREET_ADDRESS"),
(59, 71, "MOBILE_NUMBER"),
]
}),
(
"SC 843-270-2458 843-818-8824 Charleston South Carolina 4725 Broadway Street 29405"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "MOBILE_NUMBER"),
(16, 28, "TELEPHONE_NUMBER"),
(29, 39, "CITY"),
(40, 54, "STATE_FULL"),
(55, 75, "STREET_ADDRESS"),
(76, 81, "ZIPCODE"),
]
}),
(
"Charleston South Carolina 29405 843-818-8824 SC 4725 Broadway Street 843-270-2458"
, {
"entities":[
(0, 10, "CITY"),
(11, 25, "STATE_FULL"),
(26, 31, "ZIPCODE"),
(32, 44, "TELEPHONE_NUMBER"),
(45, 47, "STATE"),
(48, 68, "STREET_ADDRESS"),
(69, 81, "MOBILE_NUMBER"),
]
}),
(
"843-270-2458 South Carolina 4725 Broadway Street SC 843-818-8824 Charleston 29405"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 27, "STATE_FULL"),
(28, 48, "STREET_ADDRESS"),
(49, 51, "STATE"),
(52, 64, "TELEPHONE_NUMBER"),
(65, 75, "CITY"),
(76, 81, "ZIPCODE"),
]
}),
(
"SC 843-270-2458 843-818-8824 South Carolina 4725 Broadway Street 29405 Charleston"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "MOBILE_NUMBER"),
(16, 28, "TELEPHONE_NUMBER"),
(29, 43, "STATE_FULL"),
(44, 64, "STREET_ADDRESS"),
(65, 70, "ZIPCODE"),
(71, 81, "CITY"),
]
}),
(
"4725 Broadway Street 843-270-2458 South Carolina Charleston 843-818-8824 29405 SC"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 33, "MOBILE_NUMBER"),
(34, 48, "STATE_FULL"),
(49, 59, "CITY"),
(60, 72, "TELEPHONE_NUMBER"),
(73, 78, "ZIPCODE"),
(79, 81, "STATE"),
]
}),
(
"South Carolina 4725 Broadway Street Charleston SC 843-818-8824 843-270-2458 29405"
, {
"entities":[
(0, 14, "STATE_FULL"),
(15, 35, "STREET_ADDRESS"),
(36, 46, "CITY"),
(47, 49, "STATE"),
(50, 62, "TELEPHONE_NUMBER"),
(63, 75, "MOBILE_NUMBER"),
(76, 81, "ZIPCODE"),
]
}),
(
"4725 Broadway Street 843-270-2458 South Carolina Charleston SC 29405 843-818-8824"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 33, "MOBILE_NUMBER"),
(34, 48, "STATE_FULL"),
(49, 59, "CITY"),
(60, 62, "STATE"),
(63, 68, "ZIPCODE"),
(69, 81, "TELEPHONE_NUMBER"),
]
}),
(
"843-270-2458 4725 Broadway Street 29405 843-818-8824 SC Charleston South Carolina"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 33, "STREET_ADDRESS"),
(34, 39, "ZIPCODE"),
(40, 52, "TELEPHONE_NUMBER"),
(53, 55, "STATE"),
(56, 66, "CITY"),
(67, 81, "STATE_FULL"),
]
}),
(
"SC 843-818-8824 Charleston 29405 4725 Broadway Street 843-270-2458 South Carolina"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "TELEPHONE_NUMBER"),
(16, 26, "CITY"),
(27, 32, "ZIPCODE"),
(33, 53, "STREET_ADDRESS"),
(54, 66, "MOBILE_NUMBER"),
(67, 81, "STATE_FULL"),
]
}),
(
"Charleston South Carolina 843-818-8824 29405 SC 4725 Broadway Street 843-270-2458"
, {
"entities":[
(0, 10, "CITY"),
(11, 25, "STATE_FULL"),
(26, 38, "TELEPHONE_NUMBER"),
(39, 44, "ZIPCODE"),
(45, 47, "STATE"),
(48, 68, "STREET_ADDRESS"),
(69, 81, "MOBILE_NUMBER"),
]
}),
(
"New Mexico 505-436-1857 575-513-2347 248 Waterview Lane NM 88009 Playas"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 23, "TELEPHONE_NUMBER"),
(24, 36, "MOBILE_NUMBER"),
(37, 55, "STREET_ADDRESS"),
(56, 58, "STATE"),
(59, 64, "ZIPCODE"),
(65, 71, "CITY"),
]
}),
(
"505-436-1857 New Mexico Playas 88009 NM 575-513-2347 248 Waterview Lane"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 23, "STATE_FULL"),
(24, 30, "CITY"),
(31, 36, "ZIPCODE"),
(37, 39, "STATE"),
(40, 52, "MOBILE_NUMBER"),
(53, 71, "STREET_ADDRESS"),
]
}),
(
"Playas NM New Mexico 88009 248 Waterview Lane 505-436-1857 575-513-2347"
, {
"entities":[
(0, 6, "CITY"),
(7, 9, "STATE"),
(10, 20, "STATE_FULL"),
(21, 26, "ZIPCODE"),
(27, 45, "STREET_ADDRESS"),
(46, 58, "TELEPHONE_NUMBER"),
(59, 71, "MOBILE_NUMBER"),
]
}),
(
"248 Waterview Lane 88009 New Mexico 575-513-2347 NM 505-436-1857 Playas"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 24, "ZIPCODE"),
(25, 35, "STATE_FULL"),
(36, 48, "MOBILE_NUMBER"),
(49, 51, "STATE"),
(52, 64, "TELEPHONE_NUMBER"),
(65, 71, "CITY"),
]
}),
(
"248 Waterview Lane New Mexico NM 505-436-1857 575-513-2347 88009 Playas"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 29, "STATE_FULL"),
(30, 32, "STATE"),
(33, 45, "TELEPHONE_NUMBER"),
(46, 58, "MOBILE_NUMBER"),
(59, 64, "ZIPCODE"),
(65, 71, "CITY"),
]
}),
(
"88009 575-513-2347 New Mexico NM 248 Waterview Lane Playas 505-436-1857"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "MOBILE_NUMBER"),
(19, 29, "STATE_FULL"),
(30, 32, "STATE"),
(33, 51, "STREET_ADDRESS"),
(52, 58, "CITY"),
(59, 71, "TELEPHONE_NUMBER"),
]
}),
(
"New Mexico NM Playas 575-513-2347 88009 248 Waterview Lane 505-436-1857"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 13, "STATE"),
(14, 20, "CITY"),
(21, 33, "MOBILE_NUMBER"),
(34, 39, "ZIPCODE"),
(40, 58, "STREET_ADDRESS"),
(59, 71, "TELEPHONE_NUMBER"),
]
}),
(
"248 Waterview Lane New Mexico 88009 505-436-1857 Playas NM 575-513-2347"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 29, "STATE_FULL"),
(30, 35, "ZIPCODE"),
(36, 48, "TELEPHONE_NUMBER"),
(49, 55, "CITY"),
(56, 58, "STATE"),
(59, 71, "MOBILE_NUMBER"),
]
}),
(
"NM 505-436-1857 575-513-2347 248 Waterview Lane 88009 New Mexico Playas"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "TELEPHONE_NUMBER"),
(16, 28, "MOBILE_NUMBER"),
(29, 47, "STREET_ADDRESS"),
(48, 53, "ZIPCODE"),
(54, 64, "STATE_FULL"),
(65, 71, "CITY"),
]
}),
(
"Playas 88009 NM 505-436-1857 575-513-2347 New Mexico 248 Waterview Lane"
, {
"entities":[
(0, 6, "CITY"),
(7, 12, "ZIPCODE"),
(13, 15, "STATE"),
(16, 28, "TELEPHONE_NUMBER"),
(29, 41, "MOBILE_NUMBER"),
(42, 52, "STATE_FULL"),
(53, 71, "STREET_ADDRESS"),
]
}),
(
"620-778-6100 67107 Kansas 3279 Ridge Road 620-747-7903 KS Moundridge"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 25, "STATE_FULL"),
(26, 41, "STREET_ADDRESS"),
(42, 54, "MOBILE_NUMBER"),
(55, 57, "STATE"),
(58, 68, "CITY"),
]
}),
(
"67107 620-778-6100 3279 Ridge Road Kansas 620-747-7903 Moundridge KS"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "TELEPHONE_NUMBER"),
(19, 34, "STREET_ADDRESS"),
(35, 41, "STATE_FULL"),
(42, 54, "MOBILE_NUMBER"),
(55, 65, "CITY"),
(66, 68, "STATE"),
]
}),
(
"67107 620-778-6100 Moundridge 620-747-7903 KS Kansas 3279 Ridge Road"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "TELEPHONE_NUMBER"),
(19, 29, "CITY"),
(30, 42, "MOBILE_NUMBER"),
(43, 45, "STATE"),
(46, 52, "STATE_FULL"),
(53, 68, "STREET_ADDRESS"),
]
}),
(
"Moundridge 620-778-6100 Kansas 3279 Ridge Road 620-747-7903 KS 67107"
, {
"entities":[
(0, 10, "CITY"),
(11, 23, "TELEPHONE_NUMBER"),
(24, 30, "STATE_FULL"),
(31, 46, "STREET_ADDRESS"),
(47, 59, "MOBILE_NUMBER"),
(60, 62, "STATE"),
(63, 68, "ZIPCODE"),
]
}),
(
"Moundridge KS 3279 Ridge Road 620-747-7903 Kansas 67107 620-778-6100"
, {
"entities":[
(0, 10, "CITY"),
(11, 13, "STATE"),
(14, 29, "STREET_ADDRESS"),
(30, 42, "MOBILE_NUMBER"),
(43, 49, "STATE_FULL"),
(50, 55, "ZIPCODE"),
(56, 68, "TELEPHONE_NUMBER"),
]
}),
(
"3279 Ridge Road 620-747-7903 620-778-6100 Kansas Moundridge KS 67107"
, {
"entities":[
(0, 15, "STREET_ADDRESS"),
(16, 28, "MOBILE_NUMBER"),
(29, 41, "TELEPHONE_NUMBER"),
(42, 48, "STATE_FULL"),
(49, 59, "CITY"),
(60, 62, "STATE"),
(63, 68, "ZIPCODE"),
]
}),
(
"Kansas 620-778-6100 67107 Moundridge 3279 Ridge Road 620-747-7903 KS"
, {
"entities":[
(0, 6, "STATE_FULL"),
(7, 19, "TELEPHONE_NUMBER"),
(20, 25, "ZIPCODE"),
(26, 36, "CITY"),
(37, 52, "STREET_ADDRESS"),
(53, 65, "MOBILE_NUMBER"),
(66, 68, "STATE"),
]
}),
(
"KS Kansas Moundridge 3279 Ridge Road 67107 620-778-6100 620-747-7903"
, {
"entities":[
(0, 2, "STATE"),
(3, 9, "STATE_FULL"),
(10, 20, "CITY"),
(21, 36, "STREET_ADDRESS"),
(37, 42, "ZIPCODE"),
(43, 55, "TELEPHONE_NUMBER"),
(56, 68, "MOBILE_NUMBER"),
]
}),
(
"67107 KS 620-778-6100 620-747-7903 3279 Ridge Road Kansas Moundridge"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 21, "TELEPHONE_NUMBER"),
(22, 34, "MOBILE_NUMBER"),
(35, 50, "STREET_ADDRESS"),
(51, 57, "STATE_FULL"),
(58, 68, "CITY"),
]
}),
(
"67107 KS Kansas Moundridge 3279 Ridge Road 620-778-6100 620-747-7903"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 15, "STATE_FULL"),
(16, 26, "CITY"),
(27, 42, "STREET_ADDRESS"),
(43, 55, "TELEPHONE_NUMBER"),
(56, 68, "MOBILE_NUMBER"),
]
}),
(
"Massachusetts 01801 MA 3553 Metz Lane Woburn 857-719-7136 781-405-3870"
, {
"entities":[
(0, 13, "STATE_FULL"),
(14, 19, "ZIPCODE"),
(20, 22, "STATE"),
(23, 37, "STREET_ADDRESS"),
(38, 44, "CITY"),
(45, 57, "TELEPHONE_NUMBER"),
(58, 70, "MOBILE_NUMBER"),
]
}),
(
"MA Massachusetts 857-719-7136 Woburn 3553 Metz Lane 781-405-3870 01801"
, {
"entities":[
(0, 2, "STATE"),
(3, 16, "STATE_FULL"),
(17, 29, "TELEPHONE_NUMBER"),
(30, 36, "CITY"),
(37, 51, "STREET_ADDRESS"),
(52, 64, "MOBILE_NUMBER"),
(65, 70, "ZIPCODE"),
]
}),
(
"781-405-3870 MA Woburn 857-719-7136 Massachusetts 01801 3553 Metz Lane"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 15, "STATE"),
(16, 22, "CITY"),
(23, 35, "TELEPHONE_NUMBER"),
(36, 49, "STATE_FULL"),
(50, 55, "ZIPCODE"),
(56, 70, "STREET_ADDRESS"),
]
}),
(
"01801 781-405-3870 857-719-7136 Woburn Massachusetts MA 3553 Metz Lane"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "MOBILE_NUMBER"),
(19, 31, "TELEPHONE_NUMBER"),
(32, 38, "CITY"),
(39, 52, "STATE_FULL"),
(53, 55, "STATE"),
(56, 70, "STREET_ADDRESS"),
]
}),
(
"857-719-7136 781-405-3870 01801 Massachusetts 3553 Metz Lane MA Woburn"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 25, "MOBILE_NUMBER"),
(26, 31, "ZIPCODE"),
(32, 45, "STATE_FULL"),
(46, 60, "STREET_ADDRESS"),
(61, 63, "STATE"),
(64, 70, "CITY"),
]
}),
(
"01801 3553 Metz Lane Massachusetts 857-719-7136 781-405-3870 Woburn MA"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 20, "STREET_ADDRESS"),
(21, 34, "STATE_FULL"),
(35, 47, "TELEPHONE_NUMBER"),
(48, 60, "MOBILE_NUMBER"),
(61, 67, "CITY"),
(68, 70, "STATE"),
]
}),
(
"01801 781-405-3870 MA Massachusetts 857-719-7136 Woburn 3553 Metz Lane"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "MOBILE_NUMBER"),
(19, 21, "STATE"),
(22, 35, "STATE_FULL"),
(36, 48, "TELEPHONE_NUMBER"),
(49, 55, "CITY"),
(56, 70, "STREET_ADDRESS"),
]
}),
(
"MA 01801 781-405-3870 Massachusetts 3553 Metz Lane 857-719-7136 Woburn"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 21, "MOBILE_NUMBER"),
(22, 35, "STATE_FULL"),
(36, 50, "STREET_ADDRESS"),
(51, 63, "TELEPHONE_NUMBER"),
(64, 70, "CITY"),
]
}),
(
"Massachusetts Woburn MA 01801 781-405-3870 3553 Metz Lane 857-719-7136"
, {
"entities":[
(0, 13, "STATE_FULL"),
(14, 20, "CITY"),
(21, 23, "STATE"),
(24, 29, "ZIPCODE"),
(30, 42, "MOBILE_NUMBER"),
(43, 57, "STREET_ADDRESS"),
(58, 70, "TELEPHONE_NUMBER"),
]
}),
(
"Woburn MA Massachusetts 781-405-3870 857-719-7136 3553 Metz Lane 01801"
, {
"entities":[
(0, 6, "CITY"),
(7, 9, "STATE"),
(10, 23, "STATE_FULL"),
(24, 36, "MOBILE_NUMBER"),
(37, 49, "TELEPHONE_NUMBER"),
(50, 64, "STREET_ADDRESS"),
(65, 70, "ZIPCODE"),
]
}),
(
"NY 716-713-8554 11423 718-264-0098 Queens New York 4705 Alfred Drive"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "MOBILE_NUMBER"),
(16, 21, "ZIPCODE"),
(22, 34, "TELEPHONE_NUMBER"),
(35, 41, "CITY"),
(42, 50, "STATE_FULL"),
(51, 68, "STREET_ADDRESS"),
]
}),
(
"716-713-8554 Queens 4705 Alfred Drive 718-264-0098 New York 11423 NY"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 19, "CITY"),
(20, 37, "STREET_ADDRESS"),
(38, 50, "TELEPHONE_NUMBER"),
(51, 59, "STATE_FULL"),
(60, 65, "ZIPCODE"),
(66, 68, "STATE"),
]
}),
(
"NY New York 11423 716-713-8554 718-264-0098 4705 Alfred Drive Queens"
, {
"entities":[
(0, 2, "STATE"),
(3, 11, "STATE_FULL"),
(12, 17, "ZIPCODE"),
(18, 30, "MOBILE_NUMBER"),
(31, 43, "TELEPHONE_NUMBER"),
(44, 61, "STREET_ADDRESS"),
(62, 68, "CITY"),
]
}),
(
"718-264-0098 716-713-8554 11423 NY Queens New York 4705 Alfred Drive"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 25, "MOBILE_NUMBER"),
(26, 31, "ZIPCODE"),
(32, 34, "STATE"),
(35, 41, "CITY"),
(42, 50, "STATE_FULL"),
(51, 68, "STREET_ADDRESS"),
]
}),
(
"4705 Alfred Drive New York 11423 Queens 716-713-8554 NY 718-264-0098"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 26, "STATE_FULL"),
(27, 32, "ZIPCODE"),
(33, 39, "CITY"),
(40, 52, "MOBILE_NUMBER"),
(53, 55, "STATE"),
(56, 68, "TELEPHONE_NUMBER"),
]
}),
(
"11423 Queens 718-264-0098 New York 716-713-8554 NY 4705 Alfred Drive"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 12, "CITY"),
(13, 25, "TELEPHONE_NUMBER"),
(26, 34, "STATE_FULL"),
(35, 47, "MOBILE_NUMBER"),
(48, 50, "STATE"),
(51, 68, "STREET_ADDRESS"),
]
}),
(
"New York 718-264-0098 Queens 11423 NY 4705 Alfred Drive 716-713-8554"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 21, "TELEPHONE_NUMBER"),
(22, 28, "CITY"),
(29, 34, "ZIPCODE"),
(35, 37, "STATE"),
(38, 55, "STREET_ADDRESS"),
(56, 68, "MOBILE_NUMBER"),
]
}),
(
"New York 716-713-8554 4705 Alfred Drive 718-264-0098 11423 Queens NY"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 21, "MOBILE_NUMBER"),
(22, 39, "STREET_ADDRESS"),
(40, 52, "TELEPHONE_NUMBER"),
(53, 58, "ZIPCODE"),
(59, 65, "CITY"),
(66, 68, "STATE"),
]
}),
(
"NY 4705 Alfred Drive 718-264-0098 New York 11423 716-713-8554 Queens"
, {
"entities":[
(0, 2, "STATE"),
(3, 20, "STREET_ADDRESS"),
(21, 33, "TELEPHONE_NUMBER"),
(34, 42, "STATE_FULL"),
(43, 48, "ZIPCODE"),
(49, 61, "MOBILE_NUMBER"),
(62, 68, "CITY"),
]
}),
(
"NY 11423 718-264-0098 716-713-8554 Queens 4705 Alfred Drive New York"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 21, "TELEPHONE_NUMBER"),
(22, 34, "MOBILE_NUMBER"),
(35, 41, "CITY"),
(42, 59, "STREET_ADDRESS"),
(60, 68, "STATE_FULL"),
]
}),
(
"Wisconsin 920-297-9380 4722 Saint Francis Way 53085 262-919-0418 Sheboygan Falls WI"
, {
"entities":[
(0, 9, "STATE_FULL"),
(10, 22, "MOBILE_NUMBER"),
(23, 45, "STREET_ADDRESS"),
(46, 51, "ZIPCODE"),
(52, 64, "TELEPHONE_NUMBER"),
(65, 80, "CITY"),
(81, 83, "STATE"),
]
}),
(
"4722 Saint Francis Way WI Wisconsin 53085 920-297-9380 Sheboygan Falls 262-919-0418"
, {
"entities":[
(0, 22, "STREET_ADDRESS"),
(23, 25, "STATE"),
(26, 35, "STATE_FULL"),
(36, 41, "ZIPCODE"),
(42, 54, "MOBILE_NUMBER"),
(55, 70, "CITY"),
(71, 83, "TELEPHONE_NUMBER"),
]
}),
(
"4722 Saint Francis Way 53085 262-919-0418 920-297-9380 Sheboygan Falls Wisconsin WI"
, {
"entities":[
(0, 22, "STREET_ADDRESS"),
(23, 28, "ZIPCODE"),
(29, 41, "TELEPHONE_NUMBER"),
(42, 54, "MOBILE_NUMBER"),
(55, 70, "CITY"),
(71, 80, "STATE_FULL"),
(81, 83, "STATE"),
]
}),
(
"262-919-0418 Sheboygan Falls 4722 Saint Francis Way Wisconsin WI 920-297-9380 53085"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 28, "CITY"),
(29, 51, "STREET_ADDRESS"),
(52, 61, "STATE_FULL"),
(62, 64, "STATE"),
(65, 77, "MOBILE_NUMBER"),
(78, 83, "ZIPCODE"),
]
}),
(
"53085 WI Wisconsin 262-919-0418 4722 Saint Francis Way Sheboygan Falls 920-297-9380"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 18, "STATE_FULL"),
(19, 31, "TELEPHONE_NUMBER"),
(32, 54, "STREET_ADDRESS"),
(55, 70, "CITY"),
(71, 83, "MOBILE_NUMBER"),
]
}),
(
"53085 4722 Saint Francis Way Sheboygan Falls 262-919-0418 Wisconsin 920-297-9380 WI"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 28, "STREET_ADDRESS"),
(29, 44, "CITY"),
(45, 57, "TELEPHONE_NUMBER"),
(58, 67, "STATE_FULL"),
(68, 80, "MOBILE_NUMBER"),
(81, 83, "STATE"),
]
}),
(
"4722 Saint Francis Way Sheboygan Falls 53085 Wisconsin 262-919-0418 920-297-9380 WI"
, {
"entities":[
(0, 22, "STREET_ADDRESS"),
(23, 38, "CITY"),
(39, 44, "ZIPCODE"),
(45, 54, "STATE_FULL"),
(55, 67, "TELEPHONE_NUMBER"),
(68, 80, "MOBILE_NUMBER"),
(81, 83, "STATE"),
]
}),
(
"262-919-0418 920-297-9380 53085 Wisconsin 4722 Saint Francis Way Sheboygan Falls WI"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 25, "MOBILE_NUMBER"),
(26, 31, "ZIPCODE"),
(32, 41, "STATE_FULL"),
(42, 64, "STREET_ADDRESS"),
(65, 80, "CITY"),
(81, 83, "STATE"),
]
}),
(
"WI 262-919-0418 Sheboygan Falls 53085 4722 Saint Francis Way 920-297-9380 Wisconsin"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "TELEPHONE_NUMBER"),
(16, 31, "CITY"),
(32, 37, "ZIPCODE"),
(38, 60, "STREET_ADDRESS"),
(61, 73, "MOBILE_NUMBER"),
(74, 83, "STATE_FULL"),
]
}),
(
"WI Wisconsin 262-919-0418 920-297-9380 Sheboygan Falls 53085 4722 Saint Francis Way"
, {
"entities":[
(0, 2, "STATE"),
(3, 12, "STATE_FULL"),
(13, 25, "TELEPHONE_NUMBER"),
(26, 38, "MOBILE_NUMBER"),
(39, 54, "CITY"),
(55, 60, "ZIPCODE"),
(61, 83, "STREET_ADDRESS"),
]
}),
(
"3935 Gorby Lane MS Mississippi 601-252-5876 39402 Hattiesburg 601-467-3689"
, {
"entities":[
(0, 15, "STREET_ADDRESS"),
(16, 18, "STATE"),
(19, 30, "STATE_FULL"),
(31, 43, "TELEPHONE_NUMBER"),
(44, 49, "ZIPCODE"),
(50, 61, "CITY"),
(62, 74, "MOBILE_NUMBER"),
]
}),
(
"601-467-3689 3935 Gorby Lane 601-252-5876 Hattiesburg 39402 Mississippi MS"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 28, "STREET_ADDRESS"),
(29, 41, "TELEPHONE_NUMBER"),
(42, 53, "CITY"),
(54, 59, "ZIPCODE"),
(60, 71, "STATE_FULL"),
(72, 74, "STATE"),
]
}),
(
"3935 Gorby Lane 601-252-5876 Mississippi MS 39402 Hattiesburg 601-467-3689"
, {
"entities":[
(0, 15, "STREET_ADDRESS"),
(16, 28, "TELEPHONE_NUMBER"),
(29, 40, "STATE_FULL"),
(41, 43, "STATE"),
(44, 49, "ZIPCODE"),
(50, 61, "CITY"),
(62, 74, "MOBILE_NUMBER"),
]
}),
(
"Hattiesburg 601-252-5876 39402 601-467-3689 Mississippi MS 3935 Gorby Lane"
, {
"entities":[
(0, 11, "CITY"),
(12, 24, "TELEPHONE_NUMBER"),
(25, 30, "ZIPCODE"),
(31, 43, "MOBILE_NUMBER"),
(44, 55, "STATE_FULL"),
(56, 58, "STATE"),
(59, 74, "STREET_ADDRESS"),
]
}),
(
"3935 Gorby Lane Mississippi 39402 601-252-5876 601-467-3689 Hattiesburg MS"
, {
"entities":[
(0, 15, "STREET_ADDRESS"),
(16, 27, "STATE_FULL"),
(28, 33, "ZIPCODE"),
(34, 46, "TELEPHONE_NUMBER"),
(47, 59, "MOBILE_NUMBER"),
(60, 71, "CITY"),
(72, 74, "STATE"),
]
}),
(
"601-252-5876 3935 Gorby Lane Hattiesburg Mississippi MS 601-467-3689 39402"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 28, "STREET_ADDRESS"),
(29, 40, "CITY"),
(41, 52, "STATE_FULL"),
(53, 55, "STATE"),
(56, 68, "MOBILE_NUMBER"),
(69, 74, "ZIPCODE"),
]
}),
(
"3935 Gorby Lane Mississippi MS 39402 601-252-5876 Hattiesburg 601-467-3689"
, {
"entities":[
(0, 15, "STREET_ADDRESS"),
(16, 27, "STATE_FULL"),
(28, 30, "STATE"),
(31, 36, "ZIPCODE"),
(37, 49, "TELEPHONE_NUMBER"),
(50, 61, "CITY"),
(62, 74, "MOBILE_NUMBER"),
]
}),
(
"MS 3935 Gorby Lane 39402 Hattiesburg Mississippi 601-252-5876 601-467-3689"
, {
"entities":[
(0, 2, "STATE"),
(3, 18, "STREET_ADDRESS"),
(19, 24, "ZIPCODE"),
(25, 36, "CITY"),
(37, 48, "STATE_FULL"),
(49, 61, "TELEPHONE_NUMBER"),
(62, 74, "MOBILE_NUMBER"),
]
}),
(
"601-252-5876 MS 601-467-3689 Hattiesburg 3935 Gorby Lane Mississippi 39402"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 15, "STATE"),
(16, 28, "MOBILE_NUMBER"),
(29, 40, "CITY"),
(41, 56, "STREET_ADDRESS"),
(57, 68, "STATE_FULL"),
(69, 74, "ZIPCODE"),
]
}),
(
"39402 3935 Gorby Lane Mississippi 601-467-3689 Hattiesburg 601-252-5876 MS"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 21, "STREET_ADDRESS"),
(22, 33, "STATE_FULL"),
(34, 46, "MOBILE_NUMBER"),
(47, 58, "CITY"),
(59, 71, "TELEPHONE_NUMBER"),
(72, 74, "STATE"),
]
}),
(
"OH 740-202-8837 43609 Ohio 4235 Langtown Road 567-272-8170 Toledo"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "MOBILE_NUMBER"),
(16, 21, "ZIPCODE"),
(22, 26, "STATE_FULL"),
(27, 45, "STREET_ADDRESS"),
(46, 58, "TELEPHONE_NUMBER"),
(59, 65, "CITY"),
]
}),
(
"567-272-8170 740-202-8837 OH 43609 Toledo Ohio 4235 Langtown Road"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 25, "MOBILE_NUMBER"),
(26, 28, "STATE"),
(29, 34, "ZIPCODE"),
(35, 41, "CITY"),
(42, 46, "STATE_FULL"),
(47, 65, "STREET_ADDRESS"),
]
}),
(
"740-202-8837 567-272-8170 4235 Langtown Road Ohio OH Toledo 43609"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 25, "TELEPHONE_NUMBER"),
(26, 44, "STREET_ADDRESS"),
(45, 49, "STATE_FULL"),
(50, 52, "STATE"),
(53, 59, "CITY"),
(60, 65, "ZIPCODE"),
]
}),
(
"Ohio 43609 4235 Langtown Road Toledo 740-202-8837 OH 567-272-8170"
, {
"entities":[
(0, 4, "STATE_FULL"),
(5, 10, "ZIPCODE"),
(11, 29, "STREET_ADDRESS"),
(30, 36, "CITY"),
(37, 49, "MOBILE_NUMBER"),
(50, 52, "STATE"),
(53, 65, "TELEPHONE_NUMBER"),
]
}),
(
"4235 Langtown Road Ohio OH 43609 567-272-8170 740-202-8837 Toledo"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 23, "STATE_FULL"),
(24, 26, "STATE"),
(27, 32, "ZIPCODE"),
(33, 45, "TELEPHONE_NUMBER"),
(46, 58, "MOBILE_NUMBER"),
(59, 65, "CITY"),
]
}),
(
"4235 Langtown Road Toledo 740-202-8837 567-272-8170 OH 43609 Ohio"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 25, "CITY"),
(26, 38, "MOBILE_NUMBER"),
(39, 51, "TELEPHONE_NUMBER"),
(52, 54, "STATE"),
(55, 60, "ZIPCODE"),
(61, 65, "STATE_FULL"),
]
}),
(
"43609 4235 Langtown Road 567-272-8170 740-202-8837 OH Ohio Toledo"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 24, "STREET_ADDRESS"),
(25, 37, "TELEPHONE_NUMBER"),
(38, 50, "MOBILE_NUMBER"),
(51, 53, "STATE"),
(54, 58, "STATE_FULL"),
(59, 65, "CITY"),
]
}),
(
"OH 43609 Toledo 567-272-8170 740-202-8837 Ohio 4235 Langtown Road"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 15, "CITY"),
(16, 28, "TELEPHONE_NUMBER"),
(29, 41, "MOBILE_NUMBER"),
(42, 46, "STATE_FULL"),
(47, 65, "STREET_ADDRESS"),
]
}),
(
"740-202-8837 43609 Ohio OH 567-272-8170 4235 Langtown Road Toledo"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 23, "STATE_FULL"),
(24, 26, "STATE"),
(27, 39, "TELEPHONE_NUMBER"),
(40, 58, "STREET_ADDRESS"),
(59, 65, "CITY"),
]
}),
(
"Toledo OH 4235 Langtown Road 43609 740-202-8837 Ohio 567-272-8170"
, {
"entities":[
(0, 6, "CITY"),
(7, 9, "STATE"),
(10, 28, "STREET_ADDRESS"),
(29, 34, "ZIPCODE"),
(35, 47, "MOBILE_NUMBER"),
(48, 52, "STATE_FULL"),
(53, 65, "TELEPHONE_NUMBER"),
]
}),
(
"301-538-0639 Greenbelt Maryland 20770 778 Doe Meadow Drive 301-488-3720 MD"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 22, "CITY"),
(23, 31, "STATE_FULL"),
(32, 37, "ZIPCODE"),
(38, 58, "STREET_ADDRESS"),
(59, 71, "MOBILE_NUMBER"),
(72, 74, "STATE"),
]
}),
(
"20770 301-488-3720 301-538-0639 Greenbelt 778 Doe Meadow Drive MD Maryland"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "MOBILE_NUMBER"),
(19, 31, "TELEPHONE_NUMBER"),
(32, 41, "CITY"),
(42, 62, "STREET_ADDRESS"),
(63, 65, "STATE"),
(66, 74, "STATE_FULL"),
]
}),
(
"Greenbelt 301-488-3720 Maryland MD 778 Doe Meadow Drive 20770 301-538-0639"
, {
"entities":[
(0, 9, "CITY"),
(10, 22, "MOBILE_NUMBER"),
(23, 31, "STATE_FULL"),
(32, 34, "STATE"),
(35, 55, "STREET_ADDRESS"),
(56, 61, "ZIPCODE"),
(62, 74, "TELEPHONE_NUMBER"),
]
}),
(
"MD 301-538-0639 Greenbelt 20770 778 Doe Meadow Drive Maryland 301-488-3720"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "TELEPHONE_NUMBER"),
(16, 25, "CITY"),
(26, 31, "ZIPCODE"),
(32, 52, "STREET_ADDRESS"),
(53, 61, "STATE_FULL"),
(62, 74, "MOBILE_NUMBER"),
]
}),
(
"301-488-3720 MD Greenbelt 301-538-0639 778 Doe Meadow Drive 20770 Maryland"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 15, "STATE"),
(16, 25, "CITY"),
(26, 38, "TELEPHONE_NUMBER"),
(39, 59, "STREET_ADDRESS"),
(60, 65, "ZIPCODE"),
(66, 74, "STATE_FULL"),
]
}),
(
"778 Doe Meadow Drive MD Greenbelt 301-538-0639 20770 301-488-3720 Maryland"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 23, "STATE"),
(24, 33, "CITY"),
(34, 46, "TELEPHONE_NUMBER"),
(47, 52, "ZIPCODE"),
(53, 65, "MOBILE_NUMBER"),
(66, 74, "STATE_FULL"),
]
}),
(
"Greenbelt 301-538-0639 778 Doe Meadow Drive 20770 MD 301-488-3720 Maryland"
, {
"entities":[
(0, 9, "CITY"),
(10, 22, "TELEPHONE_NUMBER"),
(23, 43, "STREET_ADDRESS"),
(44, 49, "ZIPCODE"),
(50, 52, "STATE"),
(53, 65, "MOBILE_NUMBER"),
(66, 74, "STATE_FULL"),
]
}),
(
"20770 301-488-3720 778 Doe Meadow Drive Greenbelt Maryland MD 301-538-0639"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "MOBILE_NUMBER"),
(19, 39, "STREET_ADDRESS"),
(40, 49, "CITY"),
(50, 58, "STATE_FULL"),
(59, 61, "STATE"),
(62, 74, "TELEPHONE_NUMBER"),
]
}),
(
"MD 301-488-3720 Greenbelt 20770 301-538-0639 778 Doe Meadow Drive Maryland"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "MOBILE_NUMBER"),
(16, 25, "CITY"),
(26, 31, "ZIPCODE"),
(32, 44, "TELEPHONE_NUMBER"),
(45, 65, "STREET_ADDRESS"),
(66, 74, "STATE_FULL"),
]
}),
(
"301-538-0639 20770 778 Doe Meadow Drive MD Greenbelt Maryland 301-488-3720"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 39, "STREET_ADDRESS"),
(40, 42, "STATE"),
(43, 52, "CITY"),
(53, 61, "STATE_FULL"),
(62, 74, "MOBILE_NUMBER"),
]
}),
(
"Massachusetts 774-840-0667 Chatham 508-348-5402 2304 C Street MA 02633"
, {
"entities":[
(0, 13, "STATE_FULL"),
(14, 26, "MOBILE_NUMBER"),
(27, 34, "CITY"),
(35, 47, "TELEPHONE_NUMBER"),
(48, 61, "STREET_ADDRESS"),
(62, 64, "STATE"),
(65, 70, "ZIPCODE"),
]
}),
(
"MA 774-840-0667 508-348-5402 Chatham 02633 Massachusetts 2304 C Street"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "MOBILE_NUMBER"),
(16, 28, "TELEPHONE_NUMBER"),
(29, 36, "CITY"),
(37, 42, "ZIPCODE"),
(43, 56, "STATE_FULL"),
(57, 70, "STREET_ADDRESS"),
]
}),
(
"Massachusetts 774-840-0667 508-348-5402 Chatham 02633 2304 C Street MA"
, {
"entities":[
(0, 13, "STATE_FULL"),
(14, 26, "MOBILE_NUMBER"),
(27, 39, "TELEPHONE_NUMBER"),
(40, 47, "CITY"),
(48, 53, "ZIPCODE"),
(54, 67, "STREET_ADDRESS"),
(68, 70, "STATE"),
]
}),
(
"02633 Chatham Massachusetts 774-840-0667 2304 C Street MA 508-348-5402"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 13, "CITY"),
(14, 27, "STATE_FULL"),
(28, 40, "MOBILE_NUMBER"),
(41, 54, "STREET_ADDRESS"),
(55, 57, "STATE"),
(58, 70, "TELEPHONE_NUMBER"),
]
}),
(
"MA 774-840-0667 Chatham 02633 2304 C Street Massachusetts 508-348-5402"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "MOBILE_NUMBER"),
(16, 23, "CITY"),
(24, 29, "ZIPCODE"),
(30, 43, "STREET_ADDRESS"),
(44, 57, "STATE_FULL"),
(58, 70, "TELEPHONE_NUMBER"),
]
}),
(
"508-348-5402 2304 C Street 774-840-0667 02633 MA Chatham Massachusetts"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 26, "STREET_ADDRESS"),
(27, 39, "MOBILE_NUMBER"),
(40, 45, "ZIPCODE"),
(46, 48, "STATE"),
(49, 56, "CITY"),
(57, 70, "STATE_FULL"),
]
}),
(
"774-840-0667 2304 C Street 02633 Massachusetts Chatham MA 508-348-5402"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 26, "STREET_ADDRESS"),
(27, 32, "ZIPCODE"),
(33, 46, "STATE_FULL"),
(47, 54, "CITY"),
(55, 57, "STATE"),
(58, 70, "TELEPHONE_NUMBER"),
]
}),
(
"Massachusetts 02633 774-840-0667 Chatham MA 508-348-5402 2304 C Street"
, {
"entities":[
(0, 13, "STATE_FULL"),
(14, 19, "ZIPCODE"),
(20, 32, "MOBILE_NUMBER"),
(33, 40, "CITY"),
(41, 43, "STATE"),
(44, 56, "TELEPHONE_NUMBER"),
(57, 70, "STREET_ADDRESS"),
]
}),
(
"2304 C Street Chatham 508-348-5402 MA 774-840-0667 02633 Massachusetts"
, {
"entities":[
(0, 13, "STREET_ADDRESS"),
(14, 21, "CITY"),
(22, 34, "TELEPHONE_NUMBER"),
(35, 37, "STATE"),
(38, 50, "MOBILE_NUMBER"),
(51, 56, "ZIPCODE"),
(57, 70, "STATE_FULL"),
]
}),
(
"508-348-5402 02633 774-840-0667 Chatham 2304 C Street MA Massachusetts"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 31, "MOBILE_NUMBER"),
(32, 39, "CITY"),
(40, 53, "STREET_ADDRESS"),
(54, 56, "STATE"),
(57, 70, "STATE_FULL"),
]
}),
(
"Tennessee 4472 Buffalo Creek Road TN 615-789-1710 Charlotte 865-604-8330 37036"
, {
"entities":[
(0, 9, "STATE_FULL"),
(10, 33, "STREET_ADDRESS"),
(34, 36, "STATE"),
(37, 49, "TELEPHONE_NUMBER"),
(50, 59, "CITY"),
(60, 72, "MOBILE_NUMBER"),
(73, 78, "ZIPCODE"),
]
}),
(
"37036 TN Tennessee Charlotte 4472 Buffalo Creek Road 615-789-1710 865-604-8330"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 18, "STATE_FULL"),
(19, 28, "CITY"),
(29, 52, "STREET_ADDRESS"),
(53, 65, "TELEPHONE_NUMBER"),
(66, 78, "MOBILE_NUMBER"),
]
}),
(
"Charlotte 615-789-1710 37036 4472 Buffalo Creek Road 865-604-8330 TN Tennessee"
, {
"entities":[
(0, 9, "CITY"),
(10, 22, "TELEPHONE_NUMBER"),
(23, 28, "ZIPCODE"),
(29, 52, "STREET_ADDRESS"),
(53, 65, "MOBILE_NUMBER"),
(66, 68, "STATE"),
(69, 78, "STATE_FULL"),
]
}),
(
"Tennessee 4472 Buffalo Creek Road Charlotte 615-789-1710 865-604-8330 37036 TN"
, {
"entities":[
(0, 9, "STATE_FULL"),
(10, 33, "STREET_ADDRESS"),
(34, 43, "CITY"),
(44, 56, "TELEPHONE_NUMBER"),
(57, 69, "MOBILE_NUMBER"),
(70, 75, "ZIPCODE"),
(76, 78, "STATE"),
]
}),
(
"615-789-1710 Tennessee 37036 4472 Buffalo Creek Road TN 865-604-8330 Charlotte"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 22, "STATE_FULL"),
(23, 28, "ZIPCODE"),
(29, 52, "STREET_ADDRESS"),
(53, 55, "STATE"),
(56, 68, "MOBILE_NUMBER"),
(69, 78, "CITY"),
]
}),
(
"4472 Buffalo Creek Road 865-604-8330 TN 615-789-1710 Charlotte Tennessee 37036"
, {
"entities":[
(0, 23, "STREET_ADDRESS"),
(24, 36, "MOBILE_NUMBER"),
(37, 39, "STATE"),
(40, 52, "TELEPHONE_NUMBER"),
(53, 62, "CITY"),
(63, 72, "STATE_FULL"),
(73, 78, "ZIPCODE"),
]
}),
(
"615-789-1710 4472 Buffalo Creek Road TN 37036 865-604-8330 Charlotte Tennessee"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 36, "STREET_ADDRESS"),
(37, 39, "STATE"),
(40, 45, "ZIPCODE"),
(46, 58, "MOBILE_NUMBER"),
(59, 68, "CITY"),
(69, 78, "STATE_FULL"),
]
}),
(
"615-789-1710 4472 Buffalo Creek Road 37036 TN 865-604-8330 Charlotte Tennessee"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 36, "STREET_ADDRESS"),
(37, 42, "ZIPCODE"),
(43, 45, "STATE"),
(46, 58, "MOBILE_NUMBER"),
(59, 68, "CITY"),
(69, 78, "STATE_FULL"),
]
}),
(
"615-789-1710 865-604-8330 Tennessee Charlotte TN 4472 Buffalo Creek Road 37036"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 25, "MOBILE_NUMBER"),
(26, 35, "STATE_FULL"),
(36, 45, "CITY"),
(46, 48, "STATE"),
(49, 72, "STREET_ADDRESS"),
(73, 78, "ZIPCODE"),
]
}),
(
"37036 615-789-1710 Tennessee TN 4472 Buffalo Creek Road Charlotte 865-604-8330"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "TELEPHONE_NUMBER"),
(19, 28, "STATE_FULL"),
(29, 31, "STATE"),
(32, 55, "STREET_ADDRESS"),
(56, 65, "CITY"),
(66, 78, "MOBILE_NUMBER"),
]
}),
(
"Georgia GA Atlanta 404-200-8175 706-661-9662 2590 Radio Park Drive 30303"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 10, "STATE"),
(11, 18, "CITY"),
(19, 31, "MOBILE_NUMBER"),
(32, 44, "TELEPHONE_NUMBER"),
(45, 66, "STREET_ADDRESS"),
(67, 72, "ZIPCODE"),
]
}),
(
"2590 Radio Park Drive 30303 Georgia 706-661-9662 404-200-8175 Atlanta GA"
, {
"entities":[
(0, 21, "STREET_ADDRESS"),
(22, 27, "ZIPCODE"),
(28, 35, "STATE_FULL"),
(36, 48, "TELEPHONE_NUMBER"),
(49, 61, "MOBILE_NUMBER"),
(62, 69, "CITY"),
(70, 72, "STATE"),
]
}),
(
"Georgia Atlanta GA 2590 Radio Park Drive 30303 706-661-9662 404-200-8175"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 15, "CITY"),
(16, 18, "STATE"),
(19, 40, "STREET_ADDRESS"),
(41, 46, "ZIPCODE"),
(47, 59, "TELEPHONE_NUMBER"),
(60, 72, "MOBILE_NUMBER"),
]
}),
(
"30303 2590 Radio Park Drive 706-661-9662 Atlanta 404-200-8175 GA Georgia"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 27, "STREET_ADDRESS"),
(28, 40, "TELEPHONE_NUMBER"),
(41, 48, "CITY"),
(49, 61, "MOBILE_NUMBER"),
(62, 64, "STATE"),
(65, 72, "STATE_FULL"),
]
}),
(
"Georgia GA 2590 Radio Park Drive Atlanta 30303 404-200-8175 706-661-9662"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 10, "STATE"),
(11, 32, "STREET_ADDRESS"),
(33, 40, "CITY"),
(41, 46, "ZIPCODE"),
(47, 59, "MOBILE_NUMBER"),
(60, 72, "TELEPHONE_NUMBER"),
]
}),
(
"Atlanta 706-661-9662 2590 Radio Park Drive 404-200-8175 30303 Georgia GA"
, {
"entities":[
(0, 7, "CITY"),
(8, 20, "TELEPHONE_NUMBER"),
(21, 42, "STREET_ADDRESS"),
(43, 55, "MOBILE_NUMBER"),
(56, 61, "ZIPCODE"),
(62, 69, "STATE_FULL"),
(70, 72, "STATE"),
]
}),
(
"GA 2590 Radio Park Drive Atlanta Georgia 404-200-8175 706-661-9662 30303"
, {
"entities":[
(0, 2, "STATE"),
(3, 24, "STREET_ADDRESS"),
(25, 32, "CITY"),
(33, 40, "STATE_FULL"),
(41, 53, "MOBILE_NUMBER"),
(54, 66, "TELEPHONE_NUMBER"),
(67, 72, "ZIPCODE"),
]
}),
(
"30303 Georgia 706-661-9662 Atlanta GA 2590 Radio Park Drive 404-200-8175"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 13, "STATE_FULL"),
(14, 26, "TELEPHONE_NUMBER"),
(27, 34, "CITY"),
(35, 37, "STATE"),
(38, 59, "STREET_ADDRESS"),
(60, 72, "MOBILE_NUMBER"),
]
}),
(
"706-661-9662 GA Georgia 2590 Radio Park Drive 404-200-8175 Atlanta 30303"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 15, "STATE"),
(16, 23, "STATE_FULL"),
(24, 45, "STREET_ADDRESS"),
(46, 58, "MOBILE_NUMBER"),
(59, 66, "CITY"),
(67, 72, "ZIPCODE"),
]
}),
(
"404-200-8175 Atlanta 706-661-9662 30303 Georgia 2590 Radio Park Drive GA"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 20, "CITY"),
(21, 33, "TELEPHONE_NUMBER"),
(34, 39, "ZIPCODE"),
(40, 47, "STATE_FULL"),
(48, 69, "STREET_ADDRESS"),
(70, 72, "STATE"),
]
}),
(
"808-331-2576 Kona 96740 Hawaii 808-252-0275 HI 1109 Stratford Drive"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 17, "CITY"),
(18, 23, "ZIPCODE"),
(24, 30, "STATE_FULL"),
(31, 43, "MOBILE_NUMBER"),
(44, 46, "STATE"),
(47, 67, "STREET_ADDRESS"),
]
}),
(
"808-252-0275 96740 Hawaii 808-331-2576 Kona 1109 Stratford Drive HI"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 25, "STATE_FULL"),
(26, 38, "TELEPHONE_NUMBER"),
(39, 43, "CITY"),
(44, 64, "STREET_ADDRESS"),
(65, 67, "STATE"),
]
}),
(
"Hawaii Kona HI 808-331-2576 808-252-0275 1109 Stratford Drive 96740"
, {
"entities":[
(0, 6, "STATE_FULL"),
(7, 11, "CITY"),
(12, 14, "STATE"),
(15, 27, "TELEPHONE_NUMBER"),
(28, 40, "MOBILE_NUMBER"),
(41, 61, "STREET_ADDRESS"),
(62, 67, "ZIPCODE"),
]
}),
(
"Kona HI 1109 Stratford Drive 96740 Hawaii 808-331-2576 808-252-0275"
, {
"entities":[
(0, 4, "CITY"),
(5, 7, "STATE"),
(8, 28, "STREET_ADDRESS"),
(29, 34, "ZIPCODE"),
(35, 41, "STATE_FULL"),
(42, 54, "TELEPHONE_NUMBER"),
(55, 67, "MOBILE_NUMBER"),
]
}),
(
"808-331-2576 96740 HI 808-252-0275 Kona 1109 Stratford Drive Hawaii"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 21, "STATE"),
(22, 34, "MOBILE_NUMBER"),
(35, 39, "CITY"),
(40, 60, "STREET_ADDRESS"),
(61, 67, "STATE_FULL"),
]
}),
(
"1109 Stratford Drive 808-331-2576 Hawaii Kona 808-252-0275 96740 HI"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 33, "TELEPHONE_NUMBER"),
(34, 40, "STATE_FULL"),
(41, 45, "CITY"),
(46, 58, "MOBILE_NUMBER"),
(59, 64, "ZIPCODE"),
(65, 67, "STATE"),
]
}),
(
"808-331-2576 Kona HI 808-252-0275 Hawaii 96740 1109 Stratford Drive"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 17, "CITY"),
(18, 20, "STATE"),
(21, 33, "MOBILE_NUMBER"),
(34, 40, "STATE_FULL"),
(41, 46, "ZIPCODE"),
(47, 67, "STREET_ADDRESS"),
]
}),
(
"Hawaii HI 96740 808-252-0275 808-331-2576 Kona 1109 Stratford Drive"
, {
"entities":[
(0, 6, "STATE_FULL"),
(7, 9, "STATE"),
(10, 15, "ZIPCODE"),
(16, 28, "MOBILE_NUMBER"),
(29, 41, "TELEPHONE_NUMBER"),
(42, 46, "CITY"),
(47, 67, "STREET_ADDRESS"),
]
}),
(
"808-331-2576 HI 808-252-0275 Kona 1109 Stratford Drive Hawaii 96740"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 15, "STATE"),
(16, 28, "MOBILE_NUMBER"),
(29, 33, "CITY"),
(34, 54, "STREET_ADDRESS"),
(55, 61, "STATE_FULL"),
(62, 67, "ZIPCODE"),
]
}),
(
"808-252-0275 1109 Stratford Drive HI 96740 Hawaii Kona 808-331-2576"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 33, "STREET_ADDRESS"),
(34, 36, "STATE"),
(37, 42, "ZIPCODE"),
(43, 49, "STATE_FULL"),
(50, 54, "CITY"),
(55, 67, "TELEPHONE_NUMBER"),
]
}),
(
"76259 Texas Slidell 682-201-2492 940-466-1421 TX 402 Alexander Drive"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 11, "STATE_FULL"),
(12, 19, "CITY"),
(20, 32, "MOBILE_NUMBER"),
(33, 45, "TELEPHONE_NUMBER"),
(46, 48, "STATE"),
(49, 68, "STREET_ADDRESS"),
]
}),
(
"682-201-2492 402 Alexander Drive Texas TX 76259 940-466-1421 Slidell"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 32, "STREET_ADDRESS"),
(33, 38, "STATE_FULL"),
(39, 41, "STATE"),
(42, 47, "ZIPCODE"),
(48, 60, "TELEPHONE_NUMBER"),
(61, 68, "CITY"),
]
}),
(
"Slidell TX 682-201-2492 940-466-1421 402 Alexander Drive Texas 76259"
, {
"entities":[
(0, 7, "CITY"),
(8, 10, "STATE"),
(11, 23, "MOBILE_NUMBER"),
(24, 36, "TELEPHONE_NUMBER"),
(37, 56, "STREET_ADDRESS"),
(57, 62, "STATE_FULL"),
(63, 68, "ZIPCODE"),
]
}),
(
"682-201-2492 TX 940-466-1421 76259 Texas 402 Alexander Drive Slidell"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 15, "STATE"),
(16, 28, "TELEPHONE_NUMBER"),
(29, 34, "ZIPCODE"),
(35, 40, "STATE_FULL"),
(41, 60, "STREET_ADDRESS"),
(61, 68, "CITY"),
]
}),
(
"682-201-2492 Slidell 940-466-1421 Texas 402 Alexander Drive 76259 TX"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 20, "CITY"),
(21, 33, "TELEPHONE_NUMBER"),
(34, 39, "STATE_FULL"),
(40, 59, "STREET_ADDRESS"),
(60, 65, "ZIPCODE"),
(66, 68, "STATE"),
]
}),
(
"76259 682-201-2492 Texas Slidell 940-466-1421 402 Alexander Drive TX"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "MOBILE_NUMBER"),
(19, 24, "STATE_FULL"),
(25, 32, "CITY"),
(33, 45, "TELEPHONE_NUMBER"),
(46, 65, "STREET_ADDRESS"),
(66, 68, "STATE"),
]
}),
(
"682-201-2492 940-466-1421 TX 402 Alexander Drive 76259 Texas Slidell"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 25, "TELEPHONE_NUMBER"),
(26, 28, "STATE"),
(29, 48, "STREET_ADDRESS"),
(49, 54, "ZIPCODE"),
(55, 60, "STATE_FULL"),
(61, 68, "CITY"),
]
}),
(
"682-201-2492 402 Alexander Drive 76259 940-466-1421 TX Slidell Texas"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 32, "STREET_ADDRESS"),
(33, 38, "ZIPCODE"),
(39, 51, "TELEPHONE_NUMBER"),
(52, 54, "STATE"),
(55, 62, "CITY"),
(63, 68, "STATE_FULL"),
]
}),
(
"Slidell 76259 682-201-2492 940-466-1421 402 Alexander Drive TX Texas"
, {
"entities":[
(0, 7, "CITY"),
(8, 13, "ZIPCODE"),
(14, 26, "MOBILE_NUMBER"),
(27, 39, "TELEPHONE_NUMBER"),
(40, 59, "STREET_ADDRESS"),
(60, 62, "STATE"),
(63, 68, "STATE_FULL"),
]
}),
(
"76259 940-466-1421 402 Alexander Drive Texas 682-201-2492 Slidell TX"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "TELEPHONE_NUMBER"),
(19, 38, "STREET_ADDRESS"),
(39, 44, "STATE_FULL"),
(45, 57, "MOBILE_NUMBER"),
(58, 65, "CITY"),
(66, 68, "STATE"),
]
}),
(
"NC North Carolina 27560 919-476-7085 919-609-6179 Morrisville 2695 Jennifer Lane"
, {
"entities":[
(0, 2, "STATE"),
(3, 17, "STATE_FULL"),
(18, 23, "ZIPCODE"),
(24, 36, "TELEPHONE_NUMBER"),
(37, 49, "MOBILE_NUMBER"),
(50, 61, "CITY"),
(62, 80, "STREET_ADDRESS"),
]
}),
(
"Morrisville 27560 919-609-6179 NC North Carolina 919-476-7085 2695 Jennifer Lane"
, {
"entities":[
(0, 11, "CITY"),
(12, 17, "ZIPCODE"),
(18, 30, "MOBILE_NUMBER"),
(31, 33, "STATE"),
(34, 48, "STATE_FULL"),
(49, 61, "TELEPHONE_NUMBER"),
(62, 80, "STREET_ADDRESS"),
]
}),
(
"NC 27560 Morrisville North Carolina 919-476-7085 919-609-6179 2695 Jennifer Lane"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 20, "CITY"),
(21, 35, "STATE_FULL"),
(36, 48, "TELEPHONE_NUMBER"),
(49, 61, "MOBILE_NUMBER"),
(62, 80, "STREET_ADDRESS"),
]
}),
(
"Morrisville NC North Carolina 919-609-6179 27560 919-476-7085 2695 Jennifer Lane"
, {
"entities":[
(0, 11, "CITY"),
(12, 14, "STATE"),
(15, 29, "STATE_FULL"),
(30, 42, "MOBILE_NUMBER"),
(43, 48, "ZIPCODE"),
(49, 61, "TELEPHONE_NUMBER"),
(62, 80, "STREET_ADDRESS"),
]
}),
(
"919-476-7085 Morrisville NC 919-609-6179 North Carolina 2695 Jennifer Lane 27560"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 24, "CITY"),
(25, 27, "STATE"),
(28, 40, "MOBILE_NUMBER"),
(41, 55, "STATE_FULL"),
(56, 74, "STREET_ADDRESS"),
(75, 80, "ZIPCODE"),
]
}),
(
"NC 919-476-7085 Morrisville 919-609-6179 27560 2695 Jennifer Lane North Carolina"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "TELEPHONE_NUMBER"),
(16, 27, "CITY"),
(28, 40, "MOBILE_NUMBER"),
(41, 46, "ZIPCODE"),
(47, 65, "STREET_ADDRESS"),
(66, 80, "STATE_FULL"),
]
}),
(
"27560 919-609-6179 2695 Jennifer Lane North Carolina 919-476-7085 NC Morrisville"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "MOBILE_NUMBER"),
(19, 37, "STREET_ADDRESS"),
(38, 52, "STATE_FULL"),
(53, 65, "TELEPHONE_NUMBER"),
(66, 68, "STATE"),
(69, 80, "CITY"),
]
}),
(
"919-476-7085 Morrisville 2695 Jennifer Lane NC 919-609-6179 North Carolina 27560"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 24, "CITY"),
(25, 43, "STREET_ADDRESS"),
(44, 46, "STATE"),
(47, 59, "MOBILE_NUMBER"),
(60, 74, "STATE_FULL"),
(75, 80, "ZIPCODE"),
]
}),
(
"27560 919-476-7085 North Carolina 2695 Jennifer Lane 919-609-6179 Morrisville NC"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "TELEPHONE_NUMBER"),
(19, 33, "STATE_FULL"),
(34, 52, "STREET_ADDRESS"),
(53, 65, "MOBILE_NUMBER"),
(66, 77, "CITY"),
(78, 80, "STATE"),
]
}),
(
"NC Morrisville 919-476-7085 North Carolina 2695 Jennifer Lane 919-609-6179 27560"
, {
"entities":[
(0, 2, "STATE"),
(3, 14, "CITY"),
(15, 27, "TELEPHONE_NUMBER"),
(28, 42, "STATE_FULL"),
(43, 61, "STREET_ADDRESS"),
(62, 74, "MOBILE_NUMBER"),
(75, 80, "ZIPCODE"),
]
}),
(
"347-557-9734 4409 Hoffman Avenue New York 10016 917-919-4628 New York NY"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 32, "STREET_ADDRESS"),
(33, 41, "CITY"),
(42, 47, "ZIPCODE"),
(48, 60, "TELEPHONE_NUMBER"),
(61, 69, "STATE_FULL"),
(70, 72, "STATE"),
]
}),
(
"New York 347-557-9734 NY 10016 917-919-4628 New York 4409 Hoffman Avenue"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 21, "MOBILE_NUMBER"),
(22, 24, "STATE"),
(25, 30, "ZIPCODE"),
(31, 43, "TELEPHONE_NUMBER"),
(44, 52, "CITY"),
(53, 72, "STREET_ADDRESS"),
]
}),
(
"10016 NY New York New York 4409 Hoffman Avenue 917-919-4628 347-557-9734"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 17, "CITY"),
(18, 26, "STATE_FULL"),
(27, 46, "STREET_ADDRESS"),
(47, 59, "TELEPHONE_NUMBER"),
(60, 72, "MOBILE_NUMBER"),
]
}),
(
"917-919-4628 347-557-9734 New York NY 10016 New York 4409 Hoffman Avenue"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 25, "MOBILE_NUMBER"),
(26, 34, "CITY"),
(35, 37, "STATE"),
(38, 43, "ZIPCODE"),
(44, 52, "STATE_FULL"),
(53, 72, "STREET_ADDRESS"),
]
}),
(
"4409 Hoffman Avenue 917-919-4628 10016 New York NY New York 347-557-9734"
, {
"entities":[
(0, 19, "STREET_ADDRESS"),
(20, 32, "TELEPHONE_NUMBER"),
(33, 38, "ZIPCODE"),
(39, 47, "CITY"),
(48, 50, "STATE"),
(51, 59, "STATE_FULL"),
(60, 72, "MOBILE_NUMBER"),
]
}),
(
"New York 917-919-4628 347-557-9734 NY 4409 Hoffman Avenue 10016 New York"
, {
"entities":[
(0, 8, "CITY"),
(9, 21, "TELEPHONE_NUMBER"),
(22, 34, "MOBILE_NUMBER"),
(35, 37, "STATE"),
(38, 57, "STREET_ADDRESS"),
(58, 63, "ZIPCODE"),
(64, 72, "STATE_FULL"),
]
}),
(
"10016 347-557-9734 917-919-4628 New York NY 4409 Hoffman Avenue New York"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "MOBILE_NUMBER"),
(19, 31, "TELEPHONE_NUMBER"),
(32, 40, "STATE_FULL"),
(41, 43, "STATE"),
(44, 63, "STREET_ADDRESS"),
(64, 72, "CITY"),
]
}),
(
"4409 Hoffman Avenue New York 347-557-9734 New York 917-919-4628 10016 NY"
, {
"entities":[
(0, 19, "STREET_ADDRESS"),
(20, 28, "CITY"),
(29, 41, "MOBILE_NUMBER"),
(42, 50, "STATE_FULL"),
(51, 63, "TELEPHONE_NUMBER"),
(64, 69, "ZIPCODE"),
(70, 72, "STATE"),
]
}),
(
"New York 347-557-9734 NY 4409 Hoffman Avenue 10016 New York 917-919-4628"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 21, "MOBILE_NUMBER"),
(22, 24, "STATE"),
(25, 44, "STREET_ADDRESS"),
(45, 50, "ZIPCODE"),
(51, 59, "CITY"),
(60, 72, "TELEPHONE_NUMBER"),
]
}),
(
"10016 4409 Hoffman Avenue 347-557-9734 NY New York 917-919-4628 New York"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 25, "STREET_ADDRESS"),
(26, 38, "MOBILE_NUMBER"),
(39, 41, "STATE"),
(42, 50, "CITY"),
(51, 63, "TELEPHONE_NUMBER"),
(64, 72, "STATE_FULL"),
]
}),
(
"Texas Spring 281-288-5801 TX 77388 832-642-7358 564 Richland Avenue"
, {
"entities":[
(0, 5, "STATE_FULL"),
(6, 12, "CITY"),
(13, 25, "TELEPHONE_NUMBER"),
(26, 28, "STATE"),
(29, 34, "ZIPCODE"),
(35, 47, "MOBILE_NUMBER"),
(48, 67, "STREET_ADDRESS"),
]
}),
(
"Texas 77388 281-288-5801 832-642-7358 TX 564 Richland Avenue Spring"
, {
"entities":[
(0, 5, "STATE_FULL"),
(6, 11, "ZIPCODE"),
(12, 24, "TELEPHONE_NUMBER"),
(25, 37, "MOBILE_NUMBER"),
(38, 40, "STATE"),
(41, 60, "STREET_ADDRESS"),
(61, 67, "CITY"),
]
}),
(
"281-288-5801 77388 TX Texas 832-642-7358 564 Richland Avenue Spring"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 21, "STATE"),
(22, 27, "STATE_FULL"),
(28, 40, "MOBILE_NUMBER"),
(41, 60, "STREET_ADDRESS"),
(61, 67, "CITY"),
]
}),
(
"281-288-5801 564 Richland Avenue TX 832-642-7358 77388 Spring Texas"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 32, "STREET_ADDRESS"),
(33, 35, "STATE"),
(36, 48, "MOBILE_NUMBER"),
(49, 54, "ZIPCODE"),
(55, 61, "CITY"),
(62, 67, "STATE_FULL"),
]
}),
(
"77388 TX 281-288-5801 Spring Texas 832-642-7358 564 Richland Avenue"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 21, "TELEPHONE_NUMBER"),
(22, 28, "CITY"),
(29, 34, "STATE_FULL"),
(35, 47, "MOBILE_NUMBER"),
(48, 67, "STREET_ADDRESS"),
]
}),
(
"281-288-5801 564 Richland Avenue 832-642-7358 Spring Texas 77388 TX"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 32, "STREET_ADDRESS"),
(33, 45, "MOBILE_NUMBER"),
(46, 52, "CITY"),
(53, 58, "STATE_FULL"),
(59, 64, "ZIPCODE"),
(65, 67, "STATE"),
]
}),
(
"77388 TX 832-642-7358 Spring Texas 281-288-5801 564 Richland Avenue"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 21, "MOBILE_NUMBER"),
(22, 28, "CITY"),
(29, 34, "STATE_FULL"),
(35, 47, "TELEPHONE_NUMBER"),
(48, 67, "STREET_ADDRESS"),
]
}),
(
"TX 564 Richland Avenue Texas 832-642-7358 77388 281-288-5801 Spring"
, {
"entities":[
(0, 2, "STATE"),
(3, 22, "STREET_ADDRESS"),
(23, 28, "STATE_FULL"),
(29, 41, "MOBILE_NUMBER"),
(42, 47, "ZIPCODE"),
(48, 60, "TELEPHONE_NUMBER"),
(61, 67, "CITY"),
]
}),
(
"Texas 281-288-5801 77388 564 Richland Avenue TX 832-642-7358 Spring"
, {
"entities":[
(0, 5, "STATE_FULL"),
(6, 18, "TELEPHONE_NUMBER"),
(19, 24, "ZIPCODE"),
(25, 44, "STREET_ADDRESS"),
(45, 47, "STATE"),
(48, 60, "MOBILE_NUMBER"),
(61, 67, "CITY"),
]
}),
(
"77388 281-288-5801 TX Texas 832-642-7358 Spring 564 Richland Avenue"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "TELEPHONE_NUMBER"),
(19, 21, "STATE"),
(22, 27, "STATE_FULL"),
(28, 40, "MOBILE_NUMBER"),
(41, 47, "CITY"),
(48, 67, "STREET_ADDRESS"),
]
}),
(
"815 Davisson Street Indianapolis Indiana IN 765-780-5778 317-714-4171 46225"
, {
"entities":[
(0, 19, "STREET_ADDRESS"),
(20, 32, "CITY"),
(33, 40, "STATE_FULL"),
(41, 43, "STATE"),
(44, 56, "TELEPHONE_NUMBER"),
(57, 69, "MOBILE_NUMBER"),
(70, 75, "ZIPCODE"),
]
}),
(
"46225 815 Davisson Street 765-780-5778 Indiana Indianapolis IN 317-714-4171"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 25, "STREET_ADDRESS"),
(26, 38, "TELEPHONE_NUMBER"),
(39, 46, "STATE_FULL"),
(47, 59, "CITY"),
(60, 62, "STATE"),
(63, 75, "MOBILE_NUMBER"),
]
}),
(
"IN 317-714-4171 Indiana 765-780-5778 815 Davisson Street Indianapolis 46225"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "MOBILE_NUMBER"),
(16, 23, "STATE_FULL"),
(24, 36, "TELEPHONE_NUMBER"),
(37, 56, "STREET_ADDRESS"),
(57, 69, "CITY"),
(70, 75, "ZIPCODE"),
]
}),
(
"Indianapolis 317-714-4171 815 Davisson Street 765-780-5778 IN Indiana 46225"
, {
"entities":[
(0, 12, "CITY"),
(13, 25, "MOBILE_NUMBER"),
(26, 45, "STREET_ADDRESS"),
(46, 58, "TELEPHONE_NUMBER"),
(59, 61, "STATE"),
(62, 69, "STATE_FULL"),
(70, 75, "ZIPCODE"),
]
}),
(
"Indiana IN 765-780-5778 815 Davisson Street 46225 Indianapolis 317-714-4171"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 10, "STATE"),
(11, 23, "TELEPHONE_NUMBER"),
(24, 43, "STREET_ADDRESS"),
(44, 49, "ZIPCODE"),
(50, 62, "CITY"),
(63, 75, "MOBILE_NUMBER"),
]
}),
(
"765-780-5778 317-714-4171 Indiana 46225 Indianapolis 815 Davisson Street IN"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 25, "MOBILE_NUMBER"),
(26, 33, "STATE_FULL"),
(34, 39, "ZIPCODE"),
(40, 52, "CITY"),
(53, 72, "STREET_ADDRESS"),
(73, 75, "STATE"),
]
}),
(
"317-714-4171 765-780-5778 46225 IN 815 Davisson Street Indianapolis Indiana"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 25, "TELEPHONE_NUMBER"),
(26, 31, "ZIPCODE"),
(32, 34, "STATE"),
(35, 54, "STREET_ADDRESS"),
(55, 67, "CITY"),
(68, 75, "STATE_FULL"),
]
}),
(
"Indiana 317-714-4171 815 Davisson Street IN 46225 765-780-5778 Indianapolis"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 20, "MOBILE_NUMBER"),
(21, 40, "STREET_ADDRESS"),
(41, 43, "STATE"),
(44, 49, "ZIPCODE"),
(50, 62, "TELEPHONE_NUMBER"),
(63, 75, "CITY"),
]
}),
(
"765-780-5778 46225 317-714-4171 Indianapolis 815 Davisson Street IN Indiana"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 31, "MOBILE_NUMBER"),
(32, 44, "CITY"),
(45, 64, "STREET_ADDRESS"),
(65, 67, "STATE"),
(68, 75, "STATE_FULL"),
]
}),
(
"Indianapolis 765-780-5778 815 Davisson Street Indiana 317-714-4171 46225 IN"
, {
"entities":[
(0, 12, "CITY"),
(13, 25, "TELEPHONE_NUMBER"),
(26, 45, "STREET_ADDRESS"),
(46, 53, "STATE_FULL"),
(54, 66, "MOBILE_NUMBER"),
(67, 72, "ZIPCODE"),
(73, 75, "STATE"),
]
}),
(
"1185 Ritter Avenue 586-481-9809 Warren MI Michigan 48092 586-753-7026"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 31, "MOBILE_NUMBER"),
(32, 38, "CITY"),
(39, 41, "STATE"),
(42, 50, "STATE_FULL"),
(51, 56, "ZIPCODE"),
(57, 69, "TELEPHONE_NUMBER"),
]
}),
(
"586-753-7026 MI Michigan 1185 Ritter Avenue 586-481-9809 Warren 48092"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 15, "STATE"),
(16, 24, "STATE_FULL"),
(25, 43, "STREET_ADDRESS"),
(44, 56, "MOBILE_NUMBER"),
(57, 63, "CITY"),
(64, 69, "ZIPCODE"),
]
}),
(
"Michigan 586-753-7026 Warren 48092 MI 1185 Ritter Avenue 586-481-9809"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 21, "TELEPHONE_NUMBER"),
(22, 28, "CITY"),
(29, 34, "ZIPCODE"),
(35, 37, "STATE"),
(38, 56, "STREET_ADDRESS"),
(57, 69, "MOBILE_NUMBER"),
]
}),
(
"Warren 1185 Ritter Avenue MI 48092 Michigan 586-481-9809 586-753-7026"
, {
"entities":[
(0, 6, "CITY"),
(7, 25, "STREET_ADDRESS"),
(26, 28, "STATE"),
(29, 34, "ZIPCODE"),
(35, 43, "STATE_FULL"),
(44, 56, "MOBILE_NUMBER"),
(57, 69, "TELEPHONE_NUMBER"),
]
}),
(
"Warren 48092 586-481-9809 Michigan 1185 Ritter Avenue 586-753-7026 MI"
, {
"entities":[
(0, 6, "CITY"),
(7, 12, "ZIPCODE"),
(13, 25, "MOBILE_NUMBER"),
(26, 34, "STATE_FULL"),
(35, 53, "STREET_ADDRESS"),
(54, 66, "TELEPHONE_NUMBER"),
(67, 69, "STATE"),
]
}),
(
"586-481-9809 1185 Ritter Avenue 586-753-7026 Michigan 48092 MI Warren"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 31, "STREET_ADDRESS"),
(32, 44, "TELEPHONE_NUMBER"),
(45, 53, "STATE_FULL"),
(54, 59, "ZIPCODE"),
(60, 62, "STATE"),
(63, 69, "CITY"),
]
}),
(
"Warren 48092 MI 586-481-9809 Michigan 1185 Ritter Avenue 586-753-7026"
, {
"entities":[
(0, 6, "CITY"),
(7, 12, "ZIPCODE"),
(13, 15, "STATE"),
(16, 28, "MOBILE_NUMBER"),
(29, 37, "STATE_FULL"),
(38, 56, "STREET_ADDRESS"),
(57, 69, "TELEPHONE_NUMBER"),
]
}),
(
"48092 586-753-7026 1185 Ritter Avenue Michigan MI 586-481-9809 Warren"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "TELEPHONE_NUMBER"),
(19, 37, "STREET_ADDRESS"),
(38, 46, "STATE_FULL"),
(47, 49, "STATE"),
(50, 62, "MOBILE_NUMBER"),
(63, 69, "CITY"),
]
}),
(
"Michigan MI 1185 Ritter Avenue 48092 586-481-9809 586-753-7026 Warren"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 11, "STATE"),
(12, 30, "STREET_ADDRESS"),
(31, 36, "ZIPCODE"),
(37, 49, "MOBILE_NUMBER"),
(50, 62, "TELEPHONE_NUMBER"),
(63, 69, "CITY"),
]
}),
(
"48092 586-481-9809 586-753-7026 1185 Ritter Avenue Michigan Warren MI"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "MOBILE_NUMBER"),
(19, 31, "TELEPHONE_NUMBER"),
(32, 50, "STREET_ADDRESS"),
(51, 59, "STATE_FULL"),
(60, 66, "CITY"),
(67, 69, "STATE"),
]
}),
(
"KY 259 Coffman Alley 270-752-7632 Madisonville 270-841-7467 42431 Kentucky"
, {
"entities":[
(0, 2, "STATE"),
(3, 20, "STREET_ADDRESS"),
(21, 33, "TELEPHONE_NUMBER"),
(34, 46, "CITY"),
(47, 59, "MOBILE_NUMBER"),
(60, 65, "ZIPCODE"),
(66, 74, "STATE_FULL"),
]
}),
(
"270-841-7467 42431 KY Madisonville Kentucky 259 Coffman Alley 270-752-7632"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 21, "STATE"),
(22, 34, "CITY"),
(35, 43, "STATE_FULL"),
(44, 61, "STREET_ADDRESS"),
(62, 74, "TELEPHONE_NUMBER"),
]
}),
(
"42431 259 Coffman Alley 270-841-7467 270-752-7632 KY Madisonville Kentucky"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 23, "STREET_ADDRESS"),
(24, 36, "MOBILE_NUMBER"),
(37, 49, "TELEPHONE_NUMBER"),
(50, 52, "STATE"),
(53, 65, "CITY"),
(66, 74, "STATE_FULL"),
]
}),
(
"KY 270-841-7467 259 Coffman Alley Madisonville Kentucky 270-752-7632 42431"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "MOBILE_NUMBER"),
(16, 33, "STREET_ADDRESS"),
(34, 46, "CITY"),
(47, 55, "STATE_FULL"),
(56, 68, "TELEPHONE_NUMBER"),
(69, 74, "ZIPCODE"),
]
}),
(
"Madisonville Kentucky 270-752-7632 KY 270-841-7467 42431 259 Coffman Alley"
, {
"entities":[
(0, 12, "CITY"),
(13, 21, "STATE_FULL"),
(22, 34, "TELEPHONE_NUMBER"),
(35, 37, "STATE"),
(38, 50, "MOBILE_NUMBER"),
(51, 56, "ZIPCODE"),
(57, 74, "STREET_ADDRESS"),
]
}),
(
"42431 Kentucky KY 259 Coffman Alley Madisonville 270-841-7467 270-752-7632"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 14, "STATE_FULL"),
(15, 17, "STATE"),
(18, 35, "STREET_ADDRESS"),
(36, 48, "CITY"),
(49, 61, "MOBILE_NUMBER"),
(62, 74, "TELEPHONE_NUMBER"),
]
}),
(
"Kentucky KY 270-752-7632 259 Coffman Alley Madisonville 270-841-7467 42431"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 11, "STATE"),
(12, 24, "TELEPHONE_NUMBER"),
(25, 42, "STREET_ADDRESS"),
(43, 55, "CITY"),
(56, 68, "MOBILE_NUMBER"),
(69, 74, "ZIPCODE"),
]
}),
(
"KY Madisonville 270-752-7632 270-841-7467 42431 259 Coffman Alley Kentucky"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "CITY"),
(16, 28, "TELEPHONE_NUMBER"),
(29, 41, "MOBILE_NUMBER"),
(42, 47, "ZIPCODE"),
(48, 65, "STREET_ADDRESS"),
(66, 74, "STATE_FULL"),
]
}),
(
"Madisonville Kentucky 259 Coffman Alley 270-752-7632 270-841-7467 KY 42431"
, {
"entities":[
(0, 12, "CITY"),
(13, 21, "STATE_FULL"),
(22, 39, "STREET_ADDRESS"),
(40, 52, "TELEPHONE_NUMBER"),
(53, 65, "MOBILE_NUMBER"),
(66, 68, "STATE"),
(69, 74, "ZIPCODE"),
]
}),
(
"42431 Madisonville Kentucky KY 270-752-7632 259 Coffman Alley 270-841-7467"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "CITY"),
(19, 27, "STATE_FULL"),
(28, 30, "STATE"),
(31, 43, "TELEPHONE_NUMBER"),
(44, 61, "STREET_ADDRESS"),
(62, 74, "MOBILE_NUMBER"),
]
}),
(
"4300 Ashwood Drive Imogene 712-386-3172 Iowa IA 51645 641-860-0723"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 26, "CITY"),
(27, 39, "TELEPHONE_NUMBER"),
(40, 44, "STATE_FULL"),
(45, 47, "STATE"),
(48, 53, "ZIPCODE"),
(54, 66, "MOBILE_NUMBER"),
]
}),
(
"641-860-0723 IA 51645 4300 Ashwood Drive Iowa 712-386-3172 Imogene"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 15, "STATE"),
(16, 21, "ZIPCODE"),
(22, 40, "STREET_ADDRESS"),
(41, 45, "STATE_FULL"),
(46, 58, "TELEPHONE_NUMBER"),
(59, 66, "CITY"),
]
}),
(
"4300 Ashwood Drive IA 51645 Imogene 712-386-3172 641-860-0723 Iowa"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 21, "STATE"),
(22, 27, "ZIPCODE"),
(28, 35, "CITY"),
(36, 48, "TELEPHONE_NUMBER"),
(49, 61, "MOBILE_NUMBER"),
(62, 66, "STATE_FULL"),
]
}),
(
"4300 Ashwood Drive 641-860-0723 Imogene Iowa 51645 712-386-3172 IA"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 31, "MOBILE_NUMBER"),
(32, 39, "CITY"),
(40, 44, "STATE_FULL"),
(45, 50, "ZIPCODE"),
(51, 63, "TELEPHONE_NUMBER"),
(64, 66, "STATE"),
]
}),
(
"Imogene 641-860-0723 IA Iowa 51645 4300 Ashwood Drive 712-386-3172"
, {
"entities":[
(0, 7, "CITY"),
(8, 20, "MOBILE_NUMBER"),
(21, 23, "STATE"),
(24, 28, "STATE_FULL"),
(29, 34, "ZIPCODE"),
(35, 53, "STREET_ADDRESS"),
(54, 66, "TELEPHONE_NUMBER"),
]
}),
(
"4300 Ashwood Drive 51645 712-386-3172 Imogene Iowa IA 641-860-0723"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 24, "ZIPCODE"),
(25, 37, "TELEPHONE_NUMBER"),
(38, 45, "CITY"),
(46, 50, "STATE_FULL"),
(51, 53, "STATE"),
(54, 66, "MOBILE_NUMBER"),
]
}),
(
"51645 4300 Ashwood Drive IA 641-860-0723 712-386-3172 Imogene Iowa"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 24, "STREET_ADDRESS"),
(25, 27, "STATE"),
(28, 40, "MOBILE_NUMBER"),
(41, 53, "TELEPHONE_NUMBER"),
(54, 61, "CITY"),
(62, 66, "STATE_FULL"),
]
}),
(
"Imogene 641-860-0723 Iowa 712-386-3172 4300 Ashwood Drive IA 51645"
, {
"entities":[
(0, 7, "CITY"),
(8, 20, "MOBILE_NUMBER"),
(21, 25, "STATE_FULL"),
(26, 38, "TELEPHONE_NUMBER"),
(39, 57, "STREET_ADDRESS"),
(58, 60, "STATE"),
(61, 66, "ZIPCODE"),
]
}),
(
"IA Imogene 51645 641-860-0723 712-386-3172 4300 Ashwood Drive Iowa"
, {
"entities":[
(0, 2, "STATE"),
(3, 10, "CITY"),
(11, 16, "ZIPCODE"),
(17, 29, "MOBILE_NUMBER"),
(30, 42, "TELEPHONE_NUMBER"),
(43, 61, "STREET_ADDRESS"),
(62, 66, "STATE_FULL"),
]
}),
(
"Iowa IA Imogene 641-860-0723 51645 712-386-3172 4300 Ashwood Drive"
, {
"entities":[
(0, 4, "STATE_FULL"),
(5, 7, "STATE"),
(8, 15, "CITY"),
(16, 28, "MOBILE_NUMBER"),
(29, 34, "ZIPCODE"),
(35, 47, "TELEPHONE_NUMBER"),
(48, 66, "STREET_ADDRESS"),
]
}),
(
"1644 Washington Street Corpus Christi TX 361-774-1857 Texas 78401 361-318-0677"
, {
"entities":[
(0, 22, "STREET_ADDRESS"),
(23, 37, "CITY"),
(38, 40, "STATE"),
(41, 53, "MOBILE_NUMBER"),
(54, 59, "STATE_FULL"),
(60, 65, "ZIPCODE"),
(66, 78, "TELEPHONE_NUMBER"),
]
}),
(
"Corpus Christi 1644 Washington Street 361-774-1857 78401 TX 361-318-0677 Texas"
, {
"entities":[
(0, 14, "CITY"),
(15, 37, "STREET_ADDRESS"),
(38, 50, "MOBILE_NUMBER"),
(51, 56, "ZIPCODE"),
(57, 59, "STATE"),
(60, 72, "TELEPHONE_NUMBER"),
(73, 78, "STATE_FULL"),
]
}),
(
"Corpus Christi 78401 TX Texas 1644 Washington Street 361-774-1857 361-318-0677"
, {
"entities":[
(0, 14, "CITY"),
(15, 20, "ZIPCODE"),
(21, 23, "STATE"),
(24, 29, "STATE_FULL"),
(30, 52, "STREET_ADDRESS"),
(53, 65, "MOBILE_NUMBER"),
(66, 78, "TELEPHONE_NUMBER"),
]
}),
(
"78401 Corpus Christi TX 361-774-1857 361-318-0677 1644 Washington Street Texas"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 20, "CITY"),
(21, 23, "STATE"),
(24, 36, "MOBILE_NUMBER"),
(37, 49, "TELEPHONE_NUMBER"),
(50, 72, "STREET_ADDRESS"),
(73, 78, "STATE_FULL"),
]
}),
(
"Texas Corpus Christi 1644 Washington Street TX 361-774-1857 78401 361-318-0677"
, {
"entities":[
(0, 5, "STATE_FULL"),
(6, 20, "CITY"),
(21, 43, "STREET_ADDRESS"),
(44, 46, "STATE"),
(47, 59, "MOBILE_NUMBER"),
(60, 65, "ZIPCODE"),
(66, 78, "TELEPHONE_NUMBER"),
]
}),
(
"1644 Washington Street 361-774-1857 Texas Corpus Christi 78401 TX 361-318-0677"
, {
"entities":[
(0, 22, "STREET_ADDRESS"),
(23, 35, "MOBILE_NUMBER"),
(36, 41, "STATE_FULL"),
(42, 56, "CITY"),
(57, 62, "ZIPCODE"),
(63, 65, "STATE"),
(66, 78, "TELEPHONE_NUMBER"),
]
}),
(
"TX 361-774-1857 1644 Washington Street 361-318-0677 Texas Corpus Christi 78401"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "MOBILE_NUMBER"),
(16, 38, "STREET_ADDRESS"),
(39, 51, "TELEPHONE_NUMBER"),
(52, 57, "STATE_FULL"),
(58, 72, "CITY"),
(73, 78, "ZIPCODE"),
]
}),
(
"Texas 361-774-1857 361-318-0677 TX 78401 Corpus Christi 1644 Washington Street"
, {
"entities":[
(0, 5, "STATE_FULL"),
(6, 18, "MOBILE_NUMBER"),
(19, 31, "TELEPHONE_NUMBER"),
(32, 34, "STATE"),
(35, 40, "ZIPCODE"),
(41, 55, "CITY"),
(56, 78, "STREET_ADDRESS"),
]
}),
(
"Corpus Christi TX 361-774-1857 78401 Texas 361-318-0677 1644 Washington Street"
, {
"entities":[
(0, 14, "CITY"),
(15, 17, "STATE"),
(18, 30, "MOBILE_NUMBER"),
(31, 36, "ZIPCODE"),
(37, 42, "STATE_FULL"),
(43, 55, "TELEPHONE_NUMBER"),
(56, 78, "STREET_ADDRESS"),
]
}),
(
"1644 Washington Street Corpus Christi 78401 361-774-1857 Texas 361-318-0677 TX"
, {
"entities":[
(0, 22, "STREET_ADDRESS"),
(23, 37, "CITY"),
(38, 43, "ZIPCODE"),
(44, 56, "MOBILE_NUMBER"),
(57, 62, "STATE_FULL"),
(63, 75, "TELEPHONE_NUMBER"),
(76, 78, "STATE"),
]
}),
(
"49503 Michigan MI 810-201-8150 1 Cottonwood Lane Grand Rapids 616-270-6236"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 14, "STATE_FULL"),
(15, 17, "STATE"),
(18, 30, "MOBILE_NUMBER"),
(31, 48, "STREET_ADDRESS"),
(49, 61, "CITY"),
(62, 74, "TELEPHONE_NUMBER"),
]
}),
(
"49503 810-201-8150 Grand Rapids MI 616-270-6236 1 Cottonwood Lane Michigan"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "MOBILE_NUMBER"),
(19, 31, "CITY"),
(32, 34, "STATE"),
(35, 47, "TELEPHONE_NUMBER"),
(48, 65, "STREET_ADDRESS"),
(66, 74, "STATE_FULL"),
]
}),
(
"49503 616-270-6236 1 Cottonwood Lane Michigan MI Grand Rapids 810-201-8150"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "TELEPHONE_NUMBER"),
(19, 36, "STREET_ADDRESS"),
(37, 45, "STATE_FULL"),
(46, 48, "STATE"),
(49, 61, "CITY"),
(62, 74, "MOBILE_NUMBER"),
]
}),
(
"616-270-6236 MI 49503 Michigan 810-201-8150 Grand Rapids 1 Cottonwood Lane"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 15, "STATE"),
(16, 21, "ZIPCODE"),
(22, 30, "STATE_FULL"),
(31, 43, "MOBILE_NUMBER"),
(44, 56, "CITY"),
(57, 74, "STREET_ADDRESS"),
]
}),
(
"1 Cottonwood Lane Michigan 810-201-8150 Grand Rapids 49503 MI 616-270-6236"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 26, "STATE_FULL"),
(27, 39, "MOBILE_NUMBER"),
(40, 52, "CITY"),
(53, 58, "ZIPCODE"),
(59, 61, "STATE"),
(62, 74, "TELEPHONE_NUMBER"),
]
}),
(
"MI Michigan 1 Cottonwood Lane 810-201-8150 49503 616-270-6236 Grand Rapids"
, {
"entities":[
(0, 2, "STATE"),
(3, 11, "STATE_FULL"),
(12, 29, "STREET_ADDRESS"),
(30, 42, "MOBILE_NUMBER"),
(43, 48, "ZIPCODE"),
(49, 61, "TELEPHONE_NUMBER"),
(62, 74, "CITY"),
]
}),
(
"MI 49503 810-201-8150 616-270-6236 Michigan Grand Rapids 1 Cottonwood Lane"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 21, "MOBILE_NUMBER"),
(22, 34, "TELEPHONE_NUMBER"),
(35, 43, "STATE_FULL"),
(44, 56, "CITY"),
(57, 74, "STREET_ADDRESS"),
]
}),
(
"Michigan 616-270-6236 810-201-8150 1 Cottonwood Lane MI 49503 Grand Rapids"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 21, "TELEPHONE_NUMBER"),
(22, 34, "MOBILE_NUMBER"),
(35, 52, "STREET_ADDRESS"),
(53, 55, "STATE"),
(56, 61, "ZIPCODE"),
(62, 74, "CITY"),
]
}),
(
"1 Cottonwood Lane 616-270-6236 Grand Rapids MI Michigan 49503 810-201-8150"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 30, "TELEPHONE_NUMBER"),
(31, 43, "CITY"),
(44, 46, "STATE"),
(47, 55, "STATE_FULL"),
(56, 61, "ZIPCODE"),
(62, 74, "MOBILE_NUMBER"),
]
}),
(
"MI Michigan 810-201-8150 49503 Grand Rapids 616-270-6236 1 Cottonwood Lane"
, {
"entities":[
(0, 2, "STATE"),
(3, 11, "STATE_FULL"),
(12, 24, "MOBILE_NUMBER"),
(25, 30, "ZIPCODE"),
(31, 43, "CITY"),
(44, 56, "TELEPHONE_NUMBER"),
(57, 74, "STREET_ADDRESS"),
]
}),
(
"Washington 425-898-0110 425-351-3679 WA Sammamish 4188 Stockert Hollow Road 98053"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 23, "TELEPHONE_NUMBER"),
(24, 36, "MOBILE_NUMBER"),
(37, 39, "STATE"),
(40, 49, "CITY"),
(50, 75, "STREET_ADDRESS"),
(76, 81, "ZIPCODE"),
]
}),
(
"Washington 425-351-3679 WA 4188 Stockert Hollow Road 98053 425-898-0110 Sammamish"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 23, "MOBILE_NUMBER"),
(24, 26, "STATE"),
(27, 52, "STREET_ADDRESS"),
(53, 58, "ZIPCODE"),
(59, 71, "TELEPHONE_NUMBER"),
(72, 81, "CITY"),
]
}),
(
"98053 4188 Stockert Hollow Road Washington Sammamish WA 425-898-0110 425-351-3679"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 31, "STREET_ADDRESS"),
(32, 42, "STATE_FULL"),
(43, 52, "CITY"),
(53, 55, "STATE"),
(56, 68, "TELEPHONE_NUMBER"),
(69, 81, "MOBILE_NUMBER"),
]
}),
(
"425-351-3679 Sammamish 425-898-0110 WA 98053 4188 Stockert Hollow Road Washington"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 22, "CITY"),
(23, 35, "TELEPHONE_NUMBER"),
(36, 38, "STATE"),
(39, 44, "ZIPCODE"),
(45, 70, "STREET_ADDRESS"),
(71, 81, "STATE_FULL"),
]
}),
(
"Washington WA Sammamish 98053 425-898-0110 425-351-3679 4188 Stockert Hollow Road"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 13, "STATE"),
(14, 23, "CITY"),
(24, 29, "ZIPCODE"),
(30, 42, "TELEPHONE_NUMBER"),
(43, 55, "MOBILE_NUMBER"),
(56, 81, "STREET_ADDRESS"),
]
}),
(
"4188 Stockert Hollow Road 425-351-3679 WA 425-898-0110 Sammamish Washington 98053"
, {
"entities":[
(0, 25, "STREET_ADDRESS"),
(26, 38, "MOBILE_NUMBER"),
(39, 41, "STATE"),
(42, 54, "TELEPHONE_NUMBER"),
(55, 64, "CITY"),
(65, 75, "STATE_FULL"),
(76, 81, "ZIPCODE"),
]
}),
(
"4188 Stockert Hollow Road Sammamish 98053 425-351-3679 425-898-0110 WA Washington"
, {
"entities":[
(0, 25, "STREET_ADDRESS"),
(26, 35, "CITY"),
(36, 41, "ZIPCODE"),
(42, 54, "MOBILE_NUMBER"),
(55, 67, "TELEPHONE_NUMBER"),
(68, 70, "STATE"),
(71, 81, "STATE_FULL"),
]
}),
(
"425-898-0110 4188 Stockert Hollow Road WA Washington 425-351-3679 98053 Sammamish"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 38, "STREET_ADDRESS"),
(39, 41, "STATE"),
(42, 52, "STATE_FULL"),
(53, 65, "MOBILE_NUMBER"),
(66, 71, "ZIPCODE"),
(72, 81, "CITY"),
]
}),
(
"4188 Stockert Hollow Road 425-351-3679 WA Washington 98053 425-898-0110 Sammamish"
, {
"entities":[
(0, 25, "STREET_ADDRESS"),
(26, 38, "MOBILE_NUMBER"),
(39, 41, "STATE"),
(42, 52, "STATE_FULL"),
(53, 58, "ZIPCODE"),
(59, 71, "TELEPHONE_NUMBER"),
(72, 81, "CITY"),
]
}),
(
"425-351-3679 425-898-0110 Washington 98053 4188 Stockert Hollow Road Sammamish WA"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 25, "TELEPHONE_NUMBER"),
(26, 36, "STATE_FULL"),
(37, 42, "ZIPCODE"),
(43, 68, "STREET_ADDRESS"),
(69, 78, "CITY"),
(79, 81, "STATE"),
]
}),
(
"New York 3239 Cameron Road 716-400-9625 14202 716-443-9539 Buffalo NY"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 26, "STREET_ADDRESS"),
(27, 39, "TELEPHONE_NUMBER"),
(40, 45, "ZIPCODE"),
(46, 58, "MOBILE_NUMBER"),
(59, 66, "CITY"),
(67, 69, "STATE"),
]
}),
(
"New York NY 3239 Cameron Road 14202 716-400-9625 Buffalo 716-443-9539"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 11, "STATE"),
(12, 29, "STREET_ADDRESS"),
(30, 35, "ZIPCODE"),
(36, 48, "TELEPHONE_NUMBER"),
(49, 56, "CITY"),
(57, 69, "MOBILE_NUMBER"),
]
}),
(
"14202 3239 Cameron Road New York 716-443-9539 Buffalo 716-400-9625 NY"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 23, "STREET_ADDRESS"),
(24, 32, "STATE_FULL"),
(33, 45, "MOBILE_NUMBER"),
(46, 53, "CITY"),
(54, 66, "TELEPHONE_NUMBER"),
(67, 69, "STATE"),
]
}),
(
"3239 Cameron Road 14202 NY New York 716-400-9625 Buffalo 716-443-9539"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 23, "ZIPCODE"),
(24, 26, "STATE"),
(27, 35, "STATE_FULL"),
(36, 48, "TELEPHONE_NUMBER"),
(49, 56, "CITY"),
(57, 69, "MOBILE_NUMBER"),
]
}),
(
"New York 716-443-9539 14202 Buffalo 3239 Cameron Road NY 716-400-9625"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 21, "MOBILE_NUMBER"),
(22, 27, "ZIPCODE"),
(28, 35, "CITY"),
(36, 53, "STREET_ADDRESS"),
(54, 56, "STATE"),
(57, 69, "TELEPHONE_NUMBER"),
]
}),
(
"Buffalo 716-400-9625 New York 716-443-9539 NY 3239 Cameron Road 14202"
, {
"entities":[
(0, 7, "CITY"),
(8, 20, "TELEPHONE_NUMBER"),
(21, 29, "STATE_FULL"),
(30, 42, "MOBILE_NUMBER"),
(43, 45, "STATE"),
(46, 63, "STREET_ADDRESS"),
(64, 69, "ZIPCODE"),
]
}),
(
"Buffalo New York 716-443-9539 716-400-9625 3239 Cameron Road 14202 NY"
, {
"entities":[
(0, 7, "CITY"),
(8, 16, "STATE_FULL"),
(17, 29, "MOBILE_NUMBER"),
(30, 42, "TELEPHONE_NUMBER"),
(43, 60, "STREET_ADDRESS"),
(61, 66, "ZIPCODE"),
(67, 69, "STATE"),
]
}),
(
"14202 New York Buffalo 716-443-9539 716-400-9625 3239 Cameron Road NY"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 14, "STATE_FULL"),
(15, 22, "CITY"),
(23, 35, "MOBILE_NUMBER"),
(36, 48, "TELEPHONE_NUMBER"),
(49, 66, "STREET_ADDRESS"),
(67, 69, "STATE"),
]
}),
(
"NY New York Buffalo 14202 716-400-9625 3239 Cameron Road 716-443-9539"
, {
"entities":[
(0, 2, "STATE"),
(3, 11, "STATE_FULL"),
(12, 19, "CITY"),
(20, 25, "ZIPCODE"),
(26, 38, "TELEPHONE_NUMBER"),
(39, 56, "STREET_ADDRESS"),
(57, 69, "MOBILE_NUMBER"),
]
}),
(
"NY 14202 New York 716-443-9539 3239 Cameron Road 716-400-9625 Buffalo"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 17, "STATE_FULL"),
(18, 30, "MOBILE_NUMBER"),
(31, 48, "STREET_ADDRESS"),
(49, 61, "TELEPHONE_NUMBER"),
(62, 69, "CITY"),
]
}),
(
"12207 New York Albany 518-867-9719 466 West Virginia Avenue 518-422-0365 NY"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 14, "STATE_FULL"),
(15, 21, "CITY"),
(22, 34, "TELEPHONE_NUMBER"),
(35, 59, "STREET_ADDRESS"),
(60, 72, "MOBILE_NUMBER"),
(73, 75, "STATE"),
]
}),
(
"New York 12207 518-422-0365 466 West Virginia Avenue 518-867-9719 Albany NY"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 14, "ZIPCODE"),
(15, 27, "MOBILE_NUMBER"),
(28, 52, "STREET_ADDRESS"),
(53, 65, "TELEPHONE_NUMBER"),
(66, 72, "CITY"),
(73, 75, "STATE"),
]
}),
(
"12207 466 West Virginia Avenue 518-867-9719 518-422-0365 NY Albany New York"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 30, "STREET_ADDRESS"),
(31, 43, "TELEPHONE_NUMBER"),
(44, 56, "MOBILE_NUMBER"),
(57, 59, "STATE"),
(60, 66, "CITY"),
(67, 75, "STATE_FULL"),
]
}),
(
"12207 NY New York Albany 466 West Virginia Avenue 518-422-0365 518-867-9719"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 17, "STATE_FULL"),
(18, 24, "CITY"),
(25, 49, "STREET_ADDRESS"),
(50, 62, "MOBILE_NUMBER"),
(63, 75, "TELEPHONE_NUMBER"),
]
}),
(
"466 West Virginia Avenue New York NY 518-867-9719 Albany 12207 518-422-0365"
, {
"entities":[
(0, 24, "STREET_ADDRESS"),
(25, 33, "STATE_FULL"),
(34, 36, "STATE"),
(37, 49, "TELEPHONE_NUMBER"),
(50, 56, "CITY"),
(57, 62, "ZIPCODE"),
(63, 75, "MOBILE_NUMBER"),
]
}),
(
"466 West Virginia Avenue Albany NY 518-867-9719 518-422-0365 New York 12207"
, {
"entities":[
(0, 24, "STREET_ADDRESS"),
(25, 31, "CITY"),
(32, 34, "STATE"),
(35, 47, "TELEPHONE_NUMBER"),
(48, 60, "MOBILE_NUMBER"),
(61, 69, "STATE_FULL"),
(70, 75, "ZIPCODE"),
]
}),
(
"New York Albany 12207 518-867-9719 518-422-0365 466 West Virginia Avenue NY"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 15, "CITY"),
(16, 21, "ZIPCODE"),
(22, 34, "TELEPHONE_NUMBER"),
(35, 47, "MOBILE_NUMBER"),
(48, 72, "STREET_ADDRESS"),
(73, 75, "STATE"),
]
}),
(
"New York 518-867-9719 Albany 518-422-0365 466 West Virginia Avenue 12207 NY"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 21, "TELEPHONE_NUMBER"),
(22, 28, "CITY"),
(29, 41, "MOBILE_NUMBER"),
(42, 66, "STREET_ADDRESS"),
(67, 72, "ZIPCODE"),
(73, 75, "STATE"),
]
}),
(
"518-867-9719 466 West Virginia Avenue Albany New York NY 12207 518-422-0365"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 37, "STREET_ADDRESS"),
(38, 44, "CITY"),
(45, 53, "STATE_FULL"),
(54, 56, "STATE"),
(57, 62, "ZIPCODE"),
(63, 75, "MOBILE_NUMBER"),
]
}),
(
"466 West Virginia Avenue New York Albany NY 518-867-9719 518-422-0365 12207"
, {
"entities":[
(0, 24, "STREET_ADDRESS"),
(25, 33, "STATE_FULL"),
(34, 40, "CITY"),
(41, 43, "STATE"),
(44, 56, "TELEPHONE_NUMBER"),
(57, 69, "MOBILE_NUMBER"),
(70, 75, "ZIPCODE"),
]
}),
(
"ID Idaho 208-444-8146 Coeur D Alene 83814 208-640-0795 3966 Science Center Drive"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "STATE_FULL"),
(9, 21, "MOBILE_NUMBER"),
(22, 35, "CITY"),
(36, 41, "ZIPCODE"),
(42, 54, "TELEPHONE_NUMBER"),
(55, 80, "STREET_ADDRESS"),
]
}),
(
"Idaho 208-640-0795 83814 3966 Science Center Drive ID 208-444-8146 Coeur D Alene"
, {
"entities":[
(0, 5, "STATE_FULL"),
(6, 18, "TELEPHONE_NUMBER"),
(19, 24, "ZIPCODE"),
(25, 50, "STREET_ADDRESS"),
(51, 53, "STATE"),
(54, 66, "MOBILE_NUMBER"),
(67, 80, "CITY"),
]
}),
(
"Idaho ID 83814 208-640-0795 208-444-8146 Coeur D Alene 3966 Science Center Drive"
, {
"entities":[
(0, 5, "STATE_FULL"),
(6, 8, "STATE"),
(9, 14, "ZIPCODE"),
(15, 27, "TELEPHONE_NUMBER"),
(28, 40, "MOBILE_NUMBER"),
(41, 54, "CITY"),
(55, 80, "STREET_ADDRESS"),
]
}),
(
"208-444-8146 83814 Idaho Coeur D Alene 208-640-0795 3966 Science Center Drive ID"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 24, "STATE_FULL"),
(25, 38, "CITY"),
(39, 51, "TELEPHONE_NUMBER"),
(52, 77, "STREET_ADDRESS"),
(78, 80, "STATE"),
]
}),
(
"83814 Coeur D Alene ID 3966 Science Center Drive 208-640-0795 208-444-8146 Idaho"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 19, "CITY"),
(20, 22, "STATE"),
(23, 48, "STREET_ADDRESS"),
(49, 61, "TELEPHONE_NUMBER"),
(62, 74, "MOBILE_NUMBER"),
(75, 80, "STATE_FULL"),
]
}),
(
"3966 Science Center Drive Idaho ID Coeur D Alene 83814 208-444-8146 208-640-0795"
, {
"entities":[
(0, 25, "STREET_ADDRESS"),
(26, 31, "STATE_FULL"),
(32, 34, "STATE"),
(35, 48, "CITY"),
(49, 54, "ZIPCODE"),
(55, 67, "MOBILE_NUMBER"),
(68, 80, "TELEPHONE_NUMBER"),
]
}),
(
"Idaho 208-444-8146 208-640-0795 83814 ID 3966 Science Center Drive Coeur D Alene"
, {
"entities":[
(0, 5, "STATE_FULL"),
(6, 18, "MOBILE_NUMBER"),
(19, 31, "TELEPHONE_NUMBER"),
(32, 37, "ZIPCODE"),
(38, 40, "STATE"),
(41, 66, "STREET_ADDRESS"),
(67, 80, "CITY"),
]
}),
(
"Coeur D Alene 208-640-0795 208-444-8146 Idaho 83814 ID 3966 Science Center Drive"
, {
"entities":[
(0, 13, "CITY"),
(14, 26, "TELEPHONE_NUMBER"),
(27, 39, "MOBILE_NUMBER"),
(40, 45, "STATE_FULL"),
(46, 51, "ZIPCODE"),
(52, 54, "STATE"),
(55, 80, "STREET_ADDRESS"),
]
}),
(
"83814 208-444-8146 Coeur D Alene 3966 Science Center Drive Idaho 208-640-0795 ID"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "MOBILE_NUMBER"),
(19, 32, "CITY"),
(33, 58, "STREET_ADDRESS"),
(59, 64, "STATE_FULL"),
(65, 77, "TELEPHONE_NUMBER"),
(78, 80, "STATE"),
]
}),
(
"83814 208-640-0795 Coeur D Alene 3966 Science Center Drive Idaho ID 208-444-8146"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "TELEPHONE_NUMBER"),
(19, 32, "CITY"),
(33, 58, "STREET_ADDRESS"),
(59, 64, "STATE_FULL"),
(65, 67, "STATE"),
(68, 80, "MOBILE_NUMBER"),
]
}),
(
"Parkwood 724-726-4609 15701 724-575-9578 PA Pennsylvania 3539 Platinum Drive"
, {
"entities":[
(0, 8, "CITY"),
(9, 21, "TELEPHONE_NUMBER"),
(22, 27, "ZIPCODE"),
(28, 40, "MOBILE_NUMBER"),
(41, 43, "STATE"),
(44, 56, "STATE_FULL"),
(57, 76, "STREET_ADDRESS"),
]
}),
(
"PA Pennsylvania 3539 Platinum Drive Parkwood 724-575-9578 15701 724-726-4609"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "STATE_FULL"),
(16, 35, "STREET_ADDRESS"),
(36, 44, "CITY"),
(45, 57, "MOBILE_NUMBER"),
(58, 63, "ZIPCODE"),
(64, 76, "TELEPHONE_NUMBER"),
]
}),
(
"724-575-9578 PA Pennsylvania 3539 Platinum Drive 15701 Parkwood 724-726-4609"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 15, "STATE"),
(16, 28, "STATE_FULL"),
(29, 48, "STREET_ADDRESS"),
(49, 54, "ZIPCODE"),
(55, 63, "CITY"),
(64, 76, "TELEPHONE_NUMBER"),
]
}),
(
"724-575-9578 724-726-4609 15701 Pennsylvania Parkwood 3539 Platinum Drive PA"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 25, "TELEPHONE_NUMBER"),
(26, 31, "ZIPCODE"),
(32, 44, "STATE_FULL"),
(45, 53, "CITY"),
(54, 73, "STREET_ADDRESS"),
(74, 76, "STATE"),
]
}),
(
"3539 Platinum Drive 724-726-4609 PA 724-575-9578 Parkwood 15701 Pennsylvania"
, {
"entities":[
(0, 19, "STREET_ADDRESS"),
(20, 32, "TELEPHONE_NUMBER"),
(33, 35, "STATE"),
(36, 48, "MOBILE_NUMBER"),
(49, 57, "CITY"),
(58, 63, "ZIPCODE"),
(64, 76, "STATE_FULL"),
]
}),
(
"15701 724-575-9578 Parkwood Pennsylvania 3539 Platinum Drive 724-726-4609 PA"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "MOBILE_NUMBER"),
(19, 27, "CITY"),
(28, 40, "STATE_FULL"),
(41, 60, "STREET_ADDRESS"),
(61, 73, "TELEPHONE_NUMBER"),
(74, 76, "STATE"),
]
}),
(
"3539 Platinum Drive 724-726-4609 Parkwood Pennsylvania PA 15701 724-575-9578"
, {
"entities":[
(0, 19, "STREET_ADDRESS"),
(20, 32, "TELEPHONE_NUMBER"),
(33, 41, "CITY"),
(42, 54, "STATE_FULL"),
(55, 57, "STATE"),
(58, 63, "ZIPCODE"),
(64, 76, "MOBILE_NUMBER"),
]
}),
(
"15701 724-575-9578 Pennsylvania 3539 Platinum Drive 724-726-4609 Parkwood PA"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "MOBILE_NUMBER"),
(19, 31, "STATE_FULL"),
(32, 51, "STREET_ADDRESS"),
(52, 64, "TELEPHONE_NUMBER"),
(65, 73, "CITY"),
(74, 76, "STATE"),
]
}),
(
"3539 Platinum Drive 724-575-9578 Pennsylvania Parkwood 724-726-4609 PA 15701"
, {
"entities":[
(0, 19, "STREET_ADDRESS"),
(20, 32, "MOBILE_NUMBER"),
(33, 45, "STATE_FULL"),
(46, 54, "CITY"),
(55, 67, "TELEPHONE_NUMBER"),
(68, 70, "STATE"),
(71, 76, "ZIPCODE"),
]
}),
(
"3539 Platinum Drive PA 724-726-4609 Parkwood 15701 724-575-9578 Pennsylvania"
, {
"entities":[
(0, 19, "STREET_ADDRESS"),
(20, 22, "STATE"),
(23, 35, "TELEPHONE_NUMBER"),
(36, 44, "CITY"),
(45, 50, "ZIPCODE"),
(51, 63, "MOBILE_NUMBER"),
(64, 76, "STATE_FULL"),
]
}),
(
"2186 Anmoore Road 718-712-7990 Queens New York NY 11413 914-715-0002"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 30, "TELEPHONE_NUMBER"),
(31, 37, "CITY"),
(38, 46, "STATE_FULL"),
(47, 49, "STATE"),
(50, 55, "ZIPCODE"),
(56, 68, "MOBILE_NUMBER"),
]
}),
(
"718-712-7990 NY 11413 914-715-0002 Queens New York 2186 Anmoore Road"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 15, "STATE"),
(16, 21, "ZIPCODE"),
(22, 34, "MOBILE_NUMBER"),
(35, 41, "CITY"),
(42, 50, "STATE_FULL"),
(51, 68, "STREET_ADDRESS"),
]
}),
(
"718-712-7990 11413 914-715-0002 2186 Anmoore Road Queens NY New York"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 31, "MOBILE_NUMBER"),
(32, 49, "STREET_ADDRESS"),
(50, 56, "CITY"),
(57, 59, "STATE"),
(60, 68, "STATE_FULL"),
]
}),
(
"Queens 718-712-7990 11413 New York 2186 Anmoore Road NY 914-715-0002"
, {
"entities":[
(0, 6, "CITY"),
(7, 19, "TELEPHONE_NUMBER"),
(20, 25, "ZIPCODE"),
(26, 34, "STATE_FULL"),
(35, 52, "STREET_ADDRESS"),
(53, 55, "STATE"),
(56, 68, "MOBILE_NUMBER"),
]
}),
(
"New York Queens 2186 Anmoore Road 11413 NY 914-715-0002 718-712-7990"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 15, "CITY"),
(16, 33, "STREET_ADDRESS"),
(34, 39, "ZIPCODE"),
(40, 42, "STATE"),
(43, 55, "MOBILE_NUMBER"),
(56, 68, "TELEPHONE_NUMBER"),
]
}),
(
"Queens 914-715-0002 718-712-7990 11413 NY 2186 Anmoore Road New York"
, {
"entities":[
(0, 6, "CITY"),
(7, 19, "MOBILE_NUMBER"),
(20, 32, "TELEPHONE_NUMBER"),
(33, 38, "ZIPCODE"),
(39, 41, "STATE"),
(42, 59, "STREET_ADDRESS"),
(60, 68, "STATE_FULL"),
]
}),
(
"11413 718-712-7990 Queens New York 2186 Anmoore Road NY 914-715-0002"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "TELEPHONE_NUMBER"),
(19, 25, "CITY"),
(26, 34, "STATE_FULL"),
(35, 52, "STREET_ADDRESS"),
(53, 55, "STATE"),
(56, 68, "MOBILE_NUMBER"),
]
}),
(
"11413 914-715-0002 Queens NY 718-712-7990 New York 2186 Anmoore Road"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "MOBILE_NUMBER"),
(19, 25, "CITY"),
(26, 28, "STATE"),
(29, 41, "TELEPHONE_NUMBER"),
(42, 50, "STATE_FULL"),
(51, 68, "STREET_ADDRESS"),
]
}),
(
"718-712-7990 11413 Queens 914-715-0002 New York NY 2186 Anmoore Road"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 25, "CITY"),
(26, 38, "MOBILE_NUMBER"),
(39, 47, "STATE_FULL"),
(48, 50, "STATE"),
(51, 68, "STREET_ADDRESS"),
]
}),
(
"2186 Anmoore Road New York 914-715-0002 NY 718-712-7990 Queens 11413"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 26, "STATE_FULL"),
(27, 39, "MOBILE_NUMBER"),
(40, 42, "STATE"),
(43, 55, "TELEPHONE_NUMBER"),
(56, 62, "CITY"),
(63, 68, "ZIPCODE"),
]
}),
(
"918-764-2423 2660 Heather Sees Way Tulsa OK 74120 918-206-5982 Oklahoma"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 34, "STREET_ADDRESS"),
(35, 40, "CITY"),
(41, 43, "STATE"),
(44, 49, "ZIPCODE"),
(50, 62, "MOBILE_NUMBER"),
(63, 71, "STATE_FULL"),
]
}),
(
"OK 918-206-5982 Tulsa Oklahoma 2660 Heather Sees Way 918-764-2423 74120"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "MOBILE_NUMBER"),
(16, 21, "CITY"),
(22, 30, "STATE_FULL"),
(31, 52, "STREET_ADDRESS"),
(53, 65, "TELEPHONE_NUMBER"),
(66, 71, "ZIPCODE"),
]
}),
(
"918-206-5982 Tulsa OK 2660 Heather Sees Way 74120 918-764-2423 Oklahoma"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 18, "CITY"),
(19, 21, "STATE"),
(22, 43, "STREET_ADDRESS"),
(44, 49, "ZIPCODE"),
(50, 62, "TELEPHONE_NUMBER"),
(63, 71, "STATE_FULL"),
]
}),
(
"Tulsa 918-206-5982 OK 74120 918-764-2423 2660 Heather Sees Way Oklahoma"
, {
"entities":[
(0, 5, "CITY"),
(6, 18, "MOBILE_NUMBER"),
(19, 21, "STATE"),
(22, 27, "ZIPCODE"),
(28, 40, "TELEPHONE_NUMBER"),
(41, 62, "STREET_ADDRESS"),
(63, 71, "STATE_FULL"),
]
}),
(
"Tulsa Oklahoma 74120 2660 Heather Sees Way OK 918-764-2423 918-206-5982"
, {
"entities":[
(0, 5, "CITY"),
(6, 14, "STATE_FULL"),
(15, 20, "ZIPCODE"),
(21, 42, "STREET_ADDRESS"),
(43, 45, "STATE"),
(46, 58, "TELEPHONE_NUMBER"),
(59, 71, "MOBILE_NUMBER"),
]
}),
(
"Oklahoma 918-764-2423 OK 918-206-5982 74120 2660 Heather Sees Way Tulsa"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 21, "TELEPHONE_NUMBER"),
(22, 24, "STATE"),
(25, 37, "MOBILE_NUMBER"),
(38, 43, "ZIPCODE"),
(44, 65, "STREET_ADDRESS"),
(66, 71, "CITY"),
]
}),
(
"918-206-5982 2660 Heather Sees Way Oklahoma 74120 OK Tulsa 918-764-2423"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 34, "STREET_ADDRESS"),
(35, 43, "STATE_FULL"),
(44, 49, "ZIPCODE"),
(50, 52, "STATE"),
(53, 58, "CITY"),
(59, 71, "TELEPHONE_NUMBER"),
]
}),
(
"918-764-2423 74120 Tulsa 918-206-5982 2660 Heather Sees Way OK Oklahoma"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 18, "ZIPCODE"),
(19, 24, "CITY"),
(25, 37, "MOBILE_NUMBER"),
(38, 59, "STREET_ADDRESS"),
(60, 62, "STATE"),
(63, 71, "STATE_FULL"),
]
}),
(
"OK 74120 918-764-2423 2660 Heather Sees Way Tulsa 918-206-5982 Oklahoma"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 21, "TELEPHONE_NUMBER"),
(22, 43, "STREET_ADDRESS"),
(44, 49, "CITY"),
(50, 62, "MOBILE_NUMBER"),
(63, 71, "STATE_FULL"),
]
}),
(
"2660 Heather Sees Way Oklahoma OK 74120 918-206-5982 Tulsa 918-764-2423"
, {
"entities":[
(0, 21, "STREET_ADDRESS"),
(22, 30, "STATE_FULL"),
(31, 33, "STATE"),
(34, 39, "ZIPCODE"),
(40, 52, "MOBILE_NUMBER"),
(53, 58, "CITY"),
(59, 71, "TELEPHONE_NUMBER"),
]
}),
(
"313-239-4930 Southfield 198 Nash Street 48075 Michigan 248-866-5634 MI"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 23, "CITY"),
(24, 39, "STREET_ADDRESS"),
(40, 45, "ZIPCODE"),
(46, 54, "STATE_FULL"),
(55, 67, "MOBILE_NUMBER"),
(68, 70, "STATE"),
]
}),
(
"198 Nash Street Southfield 313-239-4930 248-866-5634 Michigan MI 48075"
, {
"entities":[
(0, 15, "STREET_ADDRESS"),
(16, 26, "CITY"),
(27, 39, "TELEPHONE_NUMBER"),
(40, 52, "MOBILE_NUMBER"),
(53, 61, "STATE_FULL"),
(62, 64, "STATE"),
(65, 70, "ZIPCODE"),
]
}),
(
"Southfield Michigan 313-239-4930 248-866-5634 48075 MI 198 Nash Street"
, {
"entities":[
(0, 10, "CITY"),
(11, 19, "STATE_FULL"),
(20, 32, "TELEPHONE_NUMBER"),
(33, 45, "MOBILE_NUMBER"),
(46, 51, "ZIPCODE"),
(52, 54, "STATE"),
(55, 70, "STREET_ADDRESS"),
]
}),
(
"MI Michigan 248-866-5634 48075 198 Nash Street Southfield 313-239-4930"
, {
"entities":[
(0, 2, "STATE"),
(3, 11, "STATE_FULL"),
(12, 24, "MOBILE_NUMBER"),
(25, 30, "ZIPCODE"),
(31, 46, "STREET_ADDRESS"),
(47, 57, "CITY"),
(58, 70, "TELEPHONE_NUMBER"),
]
}),
(
"Southfield 313-239-4930 MI Michigan 198 Nash Street 48075 248-866-5634"
, {
"entities":[
(0, 10, "CITY"),
(11, 23, "TELEPHONE_NUMBER"),
(24, 26, "STATE"),
(27, 35, "STATE_FULL"),
(36, 51, "STREET_ADDRESS"),
(52, 57, "ZIPCODE"),
(58, 70, "MOBILE_NUMBER"),
]
}),
(
"Michigan 313-239-4930 Southfield 248-866-5634 MI 48075 198 Nash Street"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 21, "TELEPHONE_NUMBER"),
(22, 32, "CITY"),
(33, 45, "MOBILE_NUMBER"),
(46, 48, "STATE"),
(49, 54, "ZIPCODE"),
(55, 70, "STREET_ADDRESS"),
]
}),
(
"313-239-4930 MI 248-866-5634 198 Nash Street Southfield Michigan 48075"
, {
"entities":[
(0, 12, "TELEPHONE_NUMBER"),
(13, 15, "STATE"),
(16, 28, "MOBILE_NUMBER"),
(29, 44, "STREET_ADDRESS"),
(45, 55, "CITY"),
(56, 64, "STATE_FULL"),
(65, 70, "ZIPCODE"),
]
}),
(
"198 Nash Street 248-866-5634 313-239-4930 48075 Michigan MI Southfield"
, {
"entities":[
(0, 15, "STREET_ADDRESS"),
(16, 28, "MOBILE_NUMBER"),
(29, 41, "TELEPHONE_NUMBER"),
(42, 47, "ZIPCODE"),
(48, 56, "STATE_FULL"),
(57, 59, "STATE"),
(60, 70, "CITY"),
]
}),
(
"248-866-5634 313-239-4930 Southfield 198 Nash Street Michigan 48075 MI"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 25, "TELEPHONE_NUMBER"),
(26, 36, "CITY"),
(37, 52, "STREET_ADDRESS"),
(53, 61, "STATE_FULL"),
(62, 67, "ZIPCODE"),
(68, 70, "STATE"),
]
}),
(
"MI Southfield 248-866-5634 48075 Michigan 198 Nash Street 313-239-4930"
, {
"entities":[
(0, 2, "STATE"),
(3, 13, "CITY"),
(14, 26, "MOBILE_NUMBER"),
(27, 32, "ZIPCODE"),
(33, 41, "STATE_FULL"),
(42, 57, "STREET_ADDRESS"),
(58, 70, "TELEPHONE_NUMBER"),
]
}),
(
"Tennessee 1698 Lords Way TN 38343 731-414-8444 Humboldt 731-784-7953"
, {
"entities":[
(0, 9, "STATE_FULL"),
(10, 24, "STREET_ADDRESS"),
(25, 27, "STATE"),
(28, 33, "ZIPCODE"),
(34, 46, "MOBILE_NUMBER"),
(47, 55, "CITY"),
(56, 68, "TELEPHONE_NUMBER"),
]
}),
(
"Tennessee 731-414-8444 TN 38343 1698 Lords Way 731-784-7953 Humboldt"
, {
"entities":[
(0, 9, "STATE_FULL"),
(10, 22, "MOBILE_NUMBER"),
(23, 25, "STATE"),
(26, 31, "ZIPCODE"),
(32, 46, "STREET_ADDRESS"),
(47, 59, "TELEPHONE_NUMBER"),
(60, 68, "CITY"),
]
}),
(
"TN 38343 731-414-8444 731-784-7953 1698 Lords Way Humboldt Tennessee"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 21, "MOBILE_NUMBER"),
(22, 34, "TELEPHONE_NUMBER"),
(35, 49, "STREET_ADDRESS"),
(50, 58, "CITY"),
(59, 68, "STATE_FULL"),
]
}),
(
"Humboldt 1698 Lords Way 731-414-8444 731-784-7953 Tennessee TN 38343"
, {
"entities":[
(0, 8, "CITY"),
(9, 23, "STREET_ADDRESS"),
(24, 36, "MOBILE_NUMBER"),
(37, 49, "TELEPHONE_NUMBER"),
(50, 59, "STATE_FULL"),
(60, 62, "STATE"),
(63, 68, "ZIPCODE"),
]
}),
(
"Humboldt 731-784-7953 1698 Lords Way 731-414-8444 Tennessee 38343 TN"
, {
"entities":[
(0, 8, "CITY"),
(9, 21, "TELEPHONE_NUMBER"),
(22, 36, "STREET_ADDRESS"),
(37, 49, "MOBILE_NUMBER"),
(50, 59, "STATE_FULL"),
(60, 65, "ZIPCODE"),
(66, 68, "STATE"),
]
}),
(
"1698 Lords Way TN 731-784-7953 731-414-8444 Tennessee 38343 Humboldt"
, {
"entities":[
(0, 14, "STREET_ADDRESS"),
(15, 17, "STATE"),
(18, 30, "TELEPHONE_NUMBER"),
(31, 43, "MOBILE_NUMBER"),
(44, 53, "STATE_FULL"),
(54, 59, "ZIPCODE"),
(60, 68, "CITY"),
]
}),
(
"731-414-8444 1698 Lords Way TN Humboldt Tennessee 38343 731-784-7953"
, {
"entities":[
(0, 12, "MOBILE_NUMBER"),
(13, 27, "STREET_ADDRESS"),
(28, 30, "STATE"),
(31, 39, "CITY"),
(40, 49, "STATE_FULL"),
(50, 55, "ZIPCODE"),
(56, 68, "TELEPHONE_NUMBER"),
]
}),
(
"Tennessee 731-414-8444 Humboldt 38343 731-784-7953 1698 Lords Way TN"
, {
"entities":[
(0, 9, "STATE_FULL"),
(10, 22, "MOBILE_NUMBER"),
(23, 31, "CITY"),
(32, 37, "ZIPCODE"),
(38, 50, "TELEPHONE_NUMBER"),
(51, 65, "STREET_ADDRESS"),
(66, 68, "STATE"),
]
}),
(
"Tennessee 38343 TN 731-414-8444 1698 Lords Way 731-784-7953 Humboldt"
, {
"entities":[
(0, 9, "STATE_FULL"),
(10, 15, "ZIPCODE"),
(16, 18, "STATE"),
(19, 31, "MOBILE_NUMBER"),
(32, 46, "STREET_ADDRESS"),
(47, 59, "TELEPHONE_NUMBER"),
(60, 68, "CITY"),
]
}),
(
"1698 Lords Way TN 731-414-8444 731-784-7953 Tennessee 38343 Humboldt"
, {
"entities":[
(0, 14, "STREET_ADDRESS"),
(15, 17, "STATE"),
(18, 30, "MOBILE_NUMBER"),
(31, 43, "TELEPHONE_NUMBER"),
(44, 53, "STATE_FULL"),
(54, 59, "ZIPCODE"),
(60, 68, "CITY"),
]
}),
]
