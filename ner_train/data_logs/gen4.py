TRAINING_DATA2 = [
(
"California 92117 CA San Diego 709 Ocello Street"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 16, "ZIPCODE"),
(17, 19, "STATE"),
(20, 29, "CITY"),
(30, 47, "STREET_ADDRESS"),
]
}),
(
"92117 California San Diego 709 Ocello Street CA"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 16, "STATE_FULL"),
(17, 26, "CITY"),
(27, 44, "STREET_ADDRESS"),
(45, 47, "STATE"),
]
}),
(
"CA California 92117 709 Ocello Street San Diego"
, {
"entities":[
(0, 2, "STATE"),
(3, 13, "STATE_FULL"),
(14, 19, "ZIPCODE"),
(20, 37, "STREET_ADDRESS"),
(38, 47, "CITY"),
]
}),
(
"California CA San Diego 709 Ocello Street 92117"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 13, "STATE"),
(14, 23, "CITY"),
(24, 41, "STREET_ADDRESS"),
(42, 47, "ZIPCODE"),
]
}),
(
"92117 San Diego CA California 709 Ocello Street"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 15, "CITY"),
(16, 18, "STATE"),
(19, 29, "STATE_FULL"),
(30, 47, "STREET_ADDRESS"),
]
}),
(
"92117 California CA San Diego 709 Ocello Street"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 16, "STATE_FULL"),
(17, 19, "STATE"),
(20, 29, "CITY"),
(30, 47, "STREET_ADDRESS"),
]
}),
(
"San Diego 709 Ocello Street 92117 California CA"
, {
"entities":[
(0, 9, "CITY"),
(10, 27, "STREET_ADDRESS"),
(28, 33, "ZIPCODE"),
(34, 44, "STATE_FULL"),
(45, 47, "STATE"),
]
}),
(
"CA 709 Ocello Street California San Diego 92117"
, {
"entities":[
(0, 2, "STATE"),
(3, 20, "STREET_ADDRESS"),
(21, 31, "STATE_FULL"),
(32, 41, "CITY"),
(42, 47, "ZIPCODE"),
]
}),
(
"San Diego California 92117 709 Ocello Street CA"
, {
"entities":[
(0, 9, "CITY"),
(10, 20, "STATE_FULL"),
(21, 26, "ZIPCODE"),
(27, 44, "STREET_ADDRESS"),
(45, 47, "STATE"),
]
}),
(
"CA 92117 San Diego California 709 Ocello Street"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 18, "CITY"),
(19, 29, "STATE_FULL"),
(30, 47, "STREET_ADDRESS"),
]
}),
(
"Phone 1613 Kennedy Court Massachusetts Westborough 01581 MA"
, {
"entities":[
(6, 24, "STREET_ADDRESS"),
(25, 38, "STATE_FULL"),
(39, 50, "CITY"),
(51, 56, "ZIPCODE"),
(57, 59, "STATE"),
]
}),
(
"MA Westborough Massachusetts 1613 Kennedy Court 01581 Phone"
, {
"entities":[
(0, 2, "STATE"),
(3, 14, "CITY"),
(15, 28, "STATE_FULL"),
(29, 47, "STREET_ADDRESS"),
(48, 53, "ZIPCODE"),
]
}),
(
"01581 MA 1613 Kennedy Court Westborough Phone Massachusetts"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 27, "STREET_ADDRESS"),
(28, 39, "CITY"),
(46, 59, "STATE_FULL"),
]
}),
(
"Phone 01581 Massachusetts Westborough MA 1613 Kennedy Court"
, {
"entities":[
(6, 11, "ZIPCODE"),
(12, 25, "STATE_FULL"),
(26, 37, "CITY"),
(38, 40, "STATE"),
(41, 59, "STREET_ADDRESS"),
]
}),
(
"01581 MA Phone Massachusetts 1613 Kennedy Court Westborough"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(15, 28, "STATE_FULL"),
(29, 47, "STREET_ADDRESS"),
(48, 59, "CITY"),
]
}),
(
"Phone 01581 Westborough MA Massachusetts 1613 Kennedy Court"
, {
"entities":[
(6, 11, "ZIPCODE"),
(12, 23, "CITY"),
(24, 26, "STATE"),
(27, 40, "STATE_FULL"),
(41, 59, "STREET_ADDRESS"),
]
}),
(
"MA Massachusetts Phone 1613 Kennedy Court Westborough 01581"
, {
"entities":[
(0, 2, "STATE"),
(3, 16, "STATE_FULL"),
(23, 41, "STREET_ADDRESS"),
(42, 53, "CITY"),
(54, 59, "ZIPCODE"),
]
}),
(
"Massachusetts 1613 Kennedy Court Westborough Phone 01581 MA"
, {
"entities":[
(0, 13, "STATE_FULL"),
(14, 32, "STREET_ADDRESS"),
(33, 44, "CITY"),
(51, 56, "ZIPCODE"),
(57, 59, "STATE"),
]
}),
(
"Phone 01581 MA Massachusetts 1613 Kennedy Court Westborough"
, {
"entities":[
(6, 11, "ZIPCODE"),
(12, 14, "STATE"),
(15, 28, "STATE_FULL"),
(29, 47, "STREET_ADDRESS"),
(48, 59, "CITY"),
]
}),
(
"MA Westborough Phone 01581 1613 Kennedy Court Massachusetts"
, {
"entities":[
(0, 2, "STATE"),
(3, 14, "CITY"),
(21, 26, "ZIPCODE"),
(27, 45, "STREET_ADDRESS"),
(46, 59, "STATE_FULL"),
]
}),
(
"97223 OR 1134 Kincheloe Road Tigard Oregon"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 28, "STREET_ADDRESS"),
(29, 35, "CITY"),
(36, 42, "STATE_FULL"),
]
}),
(
"97223 Tigard Oregon 1134 Kincheloe Road OR"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 12, "CITY"),
(13, 19, "STATE_FULL"),
(20, 39, "STREET_ADDRESS"),
(40, 42, "STATE"),
]
}),
(
"97223 Tigard Oregon OR 1134 Kincheloe Road"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 12, "CITY"),
(13, 19, "STATE_FULL"),
(20, 22, "STATE"),
(23, 42, "STREET_ADDRESS"),
]
}),
(
"97223 Tigard OR 1134 Kincheloe Road Oregon"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 12, "CITY"),
(13, 15, "STATE"),
(16, 35, "STREET_ADDRESS"),
(36, 42, "STATE_FULL"),
]
}),
(
"1134 Kincheloe Road Oregon 97223 OR Tigard"
, {
"entities":[
(0, 19, "STREET_ADDRESS"),
(20, 26, "STATE_FULL"),
(27, 32, "ZIPCODE"),
(33, 35, "STATE"),
(36, 42, "CITY"),
]
}),
(
"Oregon OR 97223 Tigard 1134 Kincheloe Road"
, {
"entities":[
(0, 6, "STATE_FULL"),
(7, 9, "STATE"),
(10, 15, "ZIPCODE"),
(16, 22, "CITY"),
(23, 42, "STREET_ADDRESS"),
]
}),
(
"Oregon 97223 Tigard 1134 Kincheloe Road OR"
, {
"entities":[
(0, 6, "STATE_FULL"),
(7, 12, "ZIPCODE"),
(13, 19, "CITY"),
(20, 39, "STREET_ADDRESS"),
(40, 42, "STATE"),
]
}),
(
"OR 97223 1134 Kincheloe Road Tigard Oregon"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 28, "STREET_ADDRESS"),
(29, 35, "CITY"),
(36, 42, "STATE_FULL"),
]
}),
(
"1134 Kincheloe Road OR 97223 Tigard Oregon"
, {
"entities":[
(0, 19, "STREET_ADDRESS"),
(20, 22, "STATE"),
(23, 28, "ZIPCODE"),
(29, 35, "CITY"),
(36, 42, "STATE_FULL"),
]
}),
(
"Tigard OR 97223 1134 Kincheloe Road Oregon"
, {
"entities":[
(0, 6, "CITY"),
(7, 9, "STATE"),
(10, 15, "ZIPCODE"),
(16, 35, "STREET_ADDRESS"),
(36, 42, "STATE_FULL"),
]
}),
(
"Michigan Grand Rapids MI 49503 961 Shingleton Road"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 21, "CITY"),
(22, 24, "STATE"),
(25, 30, "ZIPCODE"),
(31, 50, "STREET_ADDRESS"),
]
}),
(
"MI Grand Rapids Michigan 961 Shingleton Road 49503"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "CITY"),
(16, 24, "STATE_FULL"),
(25, 44, "STREET_ADDRESS"),
(45, 50, "ZIPCODE"),
]
}),
(
"Grand Rapids Michigan 49503 961 Shingleton Road MI"
, {
"entities":[
(0, 12, "CITY"),
(13, 21, "STATE_FULL"),
(22, 27, "ZIPCODE"),
(28, 47, "STREET_ADDRESS"),
(48, 50, "STATE"),
]
}),
(
"Michigan 49503 Grand Rapids MI 961 Shingleton Road"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 14, "ZIPCODE"),
(15, 27, "CITY"),
(28, 30, "STATE"),
(31, 50, "STREET_ADDRESS"),
]
}),
(
"49503 Grand Rapids MI Michigan 961 Shingleton Road"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "CITY"),
(19, 21, "STATE"),
(22, 30, "STATE_FULL"),
(31, 50, "STREET_ADDRESS"),
]
}),
(
"961 Shingleton Road Michigan MI 49503 Grand Rapids"
, {
"entities":[
(0, 19, "STREET_ADDRESS"),
(20, 28, "STATE_FULL"),
(29, 31, "STATE"),
(32, 37, "ZIPCODE"),
(38, 50, "CITY"),
]
}),
(
"Grand Rapids Michigan 49503 961 Shingleton Road MI"
, {
"entities":[
(0, 12, "CITY"),
(13, 21, "STATE_FULL"),
(22, 27, "ZIPCODE"),
(28, 47, "STREET_ADDRESS"),
(48, 50, "STATE"),
]
}),
(
"Michigan Grand Rapids 961 Shingleton Road 49503 MI"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 21, "CITY"),
(22, 41, "STREET_ADDRESS"),
(42, 47, "ZIPCODE"),
(48, 50, "STATE"),
]
}),
(
"Michigan Grand Rapids MI 961 Shingleton Road 49503"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 21, "CITY"),
(22, 24, "STATE"),
(25, 44, "STREET_ADDRESS"),
(45, 50, "ZIPCODE"),
]
}),
(
"961 Shingleton Road MI Michigan Grand Rapids 49503"
, {
"entities":[
(0, 19, "STREET_ADDRESS"),
(20, 22, "STATE"),
(23, 31, "STATE_FULL"),
(32, 44, "CITY"),
(45, 50, "ZIPCODE"),
]
}),
(
"94111 2105 Roosevelt Street California San Francisco CA"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 27, "STREET_ADDRESS"),
(28, 38, "STATE_FULL"),
(39, 52, "CITY"),
(53, 55, "STATE"),
]
}),
(
"CA 2105 Roosevelt Street San Francisco California 94111"
, {
"entities":[
(0, 2, "STATE"),
(3, 24, "STREET_ADDRESS"),
(25, 38, "CITY"),
(39, 49, "STATE_FULL"),
(50, 55, "ZIPCODE"),
]
}),
(
"2105 Roosevelt Street San Francisco CA California 94111"
, {
"entities":[
(0, 21, "STREET_ADDRESS"),
(22, 35, "CITY"),
(36, 38, "STATE"),
(39, 49, "STATE_FULL"),
(50, 55, "ZIPCODE"),
]
}),
(
"San Francisco California 2105 Roosevelt Street CA 94111"
, {
"entities":[
(0, 13, "CITY"),
(14, 24, "STATE_FULL"),
(25, 46, "STREET_ADDRESS"),
(47, 49, "STATE"),
(50, 55, "ZIPCODE"),
]
}),
(
"CA 94111 California San Francisco 2105 Roosevelt Street"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 19, "STATE_FULL"),
(20, 33, "CITY"),
(34, 55, "STREET_ADDRESS"),
]
}),
(
"California 2105 Roosevelt Street 94111 CA San Francisco"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 32, "STREET_ADDRESS"),
(33, 38, "ZIPCODE"),
(39, 41, "STATE"),
(42, 55, "CITY"),
]
}),
(
"CA 94111 California San Francisco 2105 Roosevelt Street"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 19, "STATE_FULL"),
(20, 33, "CITY"),
(34, 55, "STREET_ADDRESS"),
]
}),
(
"California CA 2105 Roosevelt Street San Francisco 94111"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 13, "STATE"),
(14, 35, "STREET_ADDRESS"),
(36, 49, "CITY"),
(50, 55, "ZIPCODE"),
]
}),
(
"94111 2105 Roosevelt Street California CA San Francisco"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 27, "STREET_ADDRESS"),
(28, 38, "STATE_FULL"),
(39, 41, "STATE"),
(42, 55, "CITY"),
]
}),
(
"94111 2105 Roosevelt Street San Francisco California CA"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 27, "STREET_ADDRESS"),
(28, 41, "CITY"),
(42, 52, "STATE_FULL"),
(53, 55, "STATE"),
]
}),
(
"Santa Fe Springs 90670 California 2347 Thompson Street CA"
, {
"entities":[
(0, 16, "CITY"),
(17, 22, "ZIPCODE"),
(23, 33, "STATE_FULL"),
(34, 54, "STREET_ADDRESS"),
(55, 57, "STATE"),
]
}),
(
"90670 CA Santa Fe Springs California 2347 Thompson Street"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 25, "CITY"),
(26, 36, "STATE_FULL"),
(37, 57, "STREET_ADDRESS"),
]
}),
(
"Santa Fe Springs CA 2347 Thompson Street California 90670"
, {
"entities":[
(0, 16, "CITY"),
(17, 19, "STATE"),
(20, 40, "STREET_ADDRESS"),
(41, 51, "STATE_FULL"),
(52, 57, "ZIPCODE"),
]
}),
(
"CA California 2347 Thompson Street Santa Fe Springs 90670"
, {
"entities":[
(0, 2, "STATE"),
(3, 13, "STATE_FULL"),
(14, 34, "STREET_ADDRESS"),
(35, 51, "CITY"),
(52, 57, "ZIPCODE"),
]
}),
(
"CA California 2347 Thompson Street Santa Fe Springs 90670"
, {
"entities":[
(0, 2, "STATE"),
(3, 13, "STATE_FULL"),
(14, 34, "STREET_ADDRESS"),
(35, 51, "CITY"),
(52, 57, "ZIPCODE"),
]
}),
(
"CA California Santa Fe Springs 90670 2347 Thompson Street"
, {
"entities":[
(0, 2, "STATE"),
(3, 13, "STATE_FULL"),
(14, 30, "CITY"),
(31, 36, "ZIPCODE"),
(37, 57, "STREET_ADDRESS"),
]
}),
(
"CA 90670 2347 Thompson Street California Santa Fe Springs"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 29, "STREET_ADDRESS"),
(30, 40, "STATE_FULL"),
(41, 57, "CITY"),
]
}),
(
"Santa Fe Springs 2347 Thompson Street California CA 90670"
, {
"entities":[
(0, 16, "CITY"),
(17, 37, "STREET_ADDRESS"),
(38, 48, "STATE_FULL"),
(49, 51, "STATE"),
(52, 57, "ZIPCODE"),
]
}),
(
"CA Santa Fe Springs 90670 California 2347 Thompson Street"
, {
"entities":[
(0, 2, "STATE"),
(3, 19, "CITY"),
(20, 25, "ZIPCODE"),
(26, 36, "STATE_FULL"),
(37, 57, "STREET_ADDRESS"),
]
}),
(
"Santa Fe Springs California CA 2347 Thompson Street 90670"
, {
"entities":[
(0, 16, "CITY"),
(17, 27, "STATE_FULL"),
(28, 30, "STATE"),
(31, 51, "STREET_ADDRESS"),
(52, 57, "ZIPCODE"),
]
}),
(
"70 Heron Way 97205 OR Portland Oregon"
, {
"entities":[
(0, 12, "STREET_ADDRESS"),
(13, 18, "ZIPCODE"),
(19, 21, "STATE"),
(22, 30, "CITY"),
(31, 37, "STATE_FULL"),
]
}),
(
"Oregon OR 97205 70 Heron Way Portland"
, {
"entities":[
(0, 6, "STATE_FULL"),
(7, 9, "STATE"),
(10, 15, "ZIPCODE"),
(16, 28, "STREET_ADDRESS"),
(29, 37, "CITY"),
]
}),
(
"Oregon 97205 70 Heron Way OR Portland"
, {
"entities":[
(0, 6, "STATE_FULL"),
(7, 12, "ZIPCODE"),
(13, 25, "STREET_ADDRESS"),
(26, 28, "STATE"),
(29, 37, "CITY"),
]
}),
(
"Portland 70 Heron Way 97205 OR Oregon"
, {
"entities":[
(0, 8, "CITY"),
(9, 21, "STREET_ADDRESS"),
(22, 27, "ZIPCODE"),
(28, 30, "STATE"),
(31, 37, "STATE_FULL"),
]
}),
(
"Portland 97205 Oregon OR 70 Heron Way"
, {
"entities":[
(0, 8, "CITY"),
(9, 14, "ZIPCODE"),
(15, 21, "STATE_FULL"),
(22, 24, "STATE"),
(25, 37, "STREET_ADDRESS"),
]
}),
(
"70 Heron Way Portland Oregon OR 97205"
, {
"entities":[
(0, 12, "STREET_ADDRESS"),
(13, 21, "CITY"),
(22, 28, "STATE_FULL"),
(29, 31, "STATE"),
(32, 37, "ZIPCODE"),
]
}),
(
"97205 70 Heron Way Oregon OR Portland"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "STREET_ADDRESS"),
(19, 25, "STATE_FULL"),
(26, 28, "STATE"),
(29, 37, "CITY"),
]
}),
(
"Portland 70 Heron Way OR 97205 Oregon"
, {
"entities":[
(0, 8, "CITY"),
(9, 21, "STREET_ADDRESS"),
(22, 24, "STATE"),
(25, 30, "ZIPCODE"),
(31, 37, "STATE_FULL"),
]
}),
(
"70 Heron Way 97205 Portland OR Oregon"
, {
"entities":[
(0, 12, "STREET_ADDRESS"),
(13, 18, "ZIPCODE"),
(19, 27, "CITY"),
(28, 30, "STATE"),
(31, 37, "STATE_FULL"),
]
}),
(
"70 Heron Way 97205 OR Oregon Portland"
, {
"entities":[
(0, 12, "STREET_ADDRESS"),
(13, 18, "ZIPCODE"),
(19, 21, "STATE"),
(22, 28, "STATE_FULL"),
(29, 37, "CITY"),
]
}),
(
"10013 New York NY 1954 Bicetown Road New York"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 14, "STATE_FULL"),
(15, 17, "STATE"),
(18, 36, "STREET_ADDRESS"),
(37, 45, "CITY"),
]
}),
(
"NY New York New York 1954 Bicetown Road 10013"
, {
"entities":[
(0, 2, "STATE"),
(3, 11, "CITY"),
(12, 20, "STATE_FULL"),
(21, 39, "STREET_ADDRESS"),
(40, 45, "ZIPCODE"),
]
}),
(
"New York NY 1954 Bicetown Road 10013 New York"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 11, "STATE"),
(12, 30, "STREET_ADDRESS"),
(31, 36, "ZIPCODE"),
(37, 45, "CITY"),
]
}),
(
"10013 New York New York 1954 Bicetown Road NY"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 14, "CITY"),
(15, 23, "STATE_FULL"),
(24, 42, "STREET_ADDRESS"),
(43, 45, "STATE"),
]
}),
(
"New York New York 1954 Bicetown Road 10013 NY"
, {
"entities":[
(0, 8, "CITY"),
(9, 17, "STATE_FULL"),
(18, 36, "STREET_ADDRESS"),
(37, 42, "ZIPCODE"),
(43, 45, "STATE"),
]
}),
(
"New York New York 10013 1954 Bicetown Road NY"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 17, "CITY"),
(18, 23, "ZIPCODE"),
(24, 42, "STREET_ADDRESS"),
(43, 45, "STATE"),
]
}),
(
"10013 NY 1954 Bicetown Road New York New York"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 27, "STREET_ADDRESS"),
(28, 36, "STATE_FULL"),
(37, 45, "CITY"),
]
}),
(
"NY 1954 Bicetown Road New York 10013 New York"
, {
"entities":[
(0, 2, "STATE"),
(3, 21, "STREET_ADDRESS"),
(22, 30, "CITY"),
(31, 36, "ZIPCODE"),
(37, 45, "STATE_FULL"),
]
}),
(
"New York 1954 Bicetown Road 10013 NY New York"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 27, "STREET_ADDRESS"),
(28, 33, "ZIPCODE"),
(34, 36, "STATE"),
(37, 45, "CITY"),
]
}),
(
"NY New York 1954 Bicetown Road 10013 New York"
, {
"entities":[
(0, 2, "STATE"),
(3, 11, "CITY"),
(12, 30, "STREET_ADDRESS"),
(31, 36, "ZIPCODE"),
(37, 45, "STATE_FULL"),
]
}),
(
"1395 Broadcast Drive Charlotte North Carolina NC 28202"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 30, "CITY"),
(31, 45, "STATE_FULL"),
(46, 48, "STATE"),
(49, 54, "ZIPCODE"),
]
}),
(
"North Carolina 1395 Broadcast Drive Charlotte NC 28202"
, {
"entities":[
(0, 14, "STATE_FULL"),
(15, 35, "STREET_ADDRESS"),
(36, 45, "CITY"),
(46, 48, "STATE"),
(49, 54, "ZIPCODE"),
]
}),
(
"North Carolina Charlotte 1395 Broadcast Drive 28202 NC"
, {
"entities":[
(0, 14, "STATE_FULL"),
(15, 24, "CITY"),
(25, 45, "STREET_ADDRESS"),
(46, 51, "ZIPCODE"),
(52, 54, "STATE"),
]
}),
(
"Charlotte North Carolina 28202 1395 Broadcast Drive NC"
, {
"entities":[
(0, 9, "CITY"),
(10, 24, "STATE_FULL"),
(25, 30, "ZIPCODE"),
(31, 51, "STREET_ADDRESS"),
(52, 54, "STATE"),
]
}),
(
"1395 Broadcast Drive NC Charlotte North Carolina 28202"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 23, "STATE"),
(24, 33, "CITY"),
(34, 48, "STATE_FULL"),
(49, 54, "ZIPCODE"),
]
}),
(
"NC Charlotte North Carolina 1395 Broadcast Drive 28202"
, {
"entities":[
(0, 2, "STATE"),
(3, 12, "CITY"),
(13, 27, "STATE_FULL"),
(28, 48, "STREET_ADDRESS"),
(49, 54, "ZIPCODE"),
]
}),
(
"North Carolina NC 28202 1395 Broadcast Drive Charlotte"
, {
"entities":[
(0, 14, "STATE_FULL"),
(15, 17, "STATE"),
(18, 23, "ZIPCODE"),
(24, 44, "STREET_ADDRESS"),
(45, 54, "CITY"),
]
}),
(
"1395 Broadcast Drive North Carolina Charlotte 28202 NC"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 35, "STATE_FULL"),
(36, 45, "CITY"),
(46, 51, "ZIPCODE"),
(52, 54, "STATE"),
]
}),
(
"1395 Broadcast Drive NC Charlotte 28202 North Carolina"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 23, "STATE"),
(24, 33, "CITY"),
(34, 39, "ZIPCODE"),
(40, 54, "STATE_FULL"),
]
}),
(
"Charlotte 1395 Broadcast Drive North Carolina 28202 NC"
, {
"entities":[
(0, 9, "CITY"),
(10, 30, "STREET_ADDRESS"),
(31, 45, "STATE_FULL"),
(46, 51, "ZIPCODE"),
(52, 54, "STATE"),
]
}),
(
"92308 Apple Valley California CA 2175 Parkway Street"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "CITY"),
(19, 29, "STATE_FULL"),
(30, 32, "STATE"),
(33, 52, "STREET_ADDRESS"),
]
}),
(
"92308 California 2175 Parkway Street CA Apple Valley"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 16, "STATE_FULL"),
(17, 36, "STREET_ADDRESS"),
(37, 39, "STATE"),
(40, 52, "CITY"),
]
}),
(
"Apple Valley 92308 CA 2175 Parkway Street California"
, {
"entities":[
(0, 12, "CITY"),
(13, 18, "ZIPCODE"),
(19, 21, "STATE"),
(22, 41, "STREET_ADDRESS"),
(42, 52, "STATE_FULL"),
]
}),
(
"CA 2175 Parkway Street 92308 California Apple Valley"
, {
"entities":[
(0, 2, "STATE"),
(3, 22, "STREET_ADDRESS"),
(23, 28, "ZIPCODE"),
(29, 39, "STATE_FULL"),
(40, 52, "CITY"),
]
}),
(
"CA 2175 Parkway Street Apple Valley 92308 California"
, {
"entities":[
(0, 2, "STATE"),
(3, 22, "STREET_ADDRESS"),
(23, 35, "CITY"),
(36, 41, "ZIPCODE"),
(42, 52, "STATE_FULL"),
]
}),
(
"92308 Apple Valley 2175 Parkway Street California CA"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "CITY"),
(19, 38, "STREET_ADDRESS"),
(39, 49, "STATE_FULL"),
(50, 52, "STATE"),
]
}),
(
"92308 California 2175 Parkway Street Apple Valley CA"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 16, "STATE_FULL"),
(17, 36, "STREET_ADDRESS"),
(37, 49, "CITY"),
(50, 52, "STATE"),
]
}),
(
"California Apple Valley 2175 Parkway Street CA 92308"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 23, "CITY"),
(24, 43, "STREET_ADDRESS"),
(44, 46, "STATE"),
(47, 52, "ZIPCODE"),
]
}),
(
"2175 Parkway Street Apple Valley 92308 CA California"
, {
"entities":[
(0, 19, "STREET_ADDRESS"),
(20, 32, "CITY"),
(33, 38, "ZIPCODE"),
(39, 41, "STATE"),
(42, 52, "STATE_FULL"),
]
}),
(
"CA California 2175 Parkway Street Apple Valley 92308"
, {
"entities":[
(0, 2, "STATE"),
(3, 13, "STATE_FULL"),
(14, 33, "STREET_ADDRESS"),
(34, 46, "CITY"),
(47, 52, "ZIPCODE"),
]
}),
(
"19963 1164 Callison Lane DE Milford Delaware"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 24, "STREET_ADDRESS"),
(25, 27, "STATE"),
(28, 35, "CITY"),
(36, 44, "STATE_FULL"),
]
}),
(
"DE 1164 Callison Lane Milford Delaware 19963"
, {
"entities":[
(0, 2, "STATE"),
(3, 21, "STREET_ADDRESS"),
(22, 29, "CITY"),
(30, 38, "STATE_FULL"),
(39, 44, "ZIPCODE"),
]
}),
(
"DE Delaware 19963 1164 Callison Lane Milford"
, {
"entities":[
(0, 2, "STATE"),
(3, 11, "STATE_FULL"),
(12, 17, "ZIPCODE"),
(18, 36, "STREET_ADDRESS"),
(37, 44, "CITY"),
]
}),
(
"DE 1164 Callison Lane 19963 Delaware Milford"
, {
"entities":[
(0, 2, "STATE"),
(3, 21, "STREET_ADDRESS"),
(22, 27, "ZIPCODE"),
(28, 36, "STATE_FULL"),
(37, 44, "CITY"),
]
}),
(
"1164 Callison Lane Milford 19963 Delaware DE"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 26, "CITY"),
(27, 32, "ZIPCODE"),
(33, 41, "STATE_FULL"),
(42, 44, "STATE"),
]
}),
(
"19963 Delaware Milford DE 1164 Callison Lane"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 14, "STATE_FULL"),
(15, 22, "CITY"),
(23, 25, "STATE"),
(26, 44, "STREET_ADDRESS"),
]
}),
(
"Milford Delaware 1164 Callison Lane 19963 DE"
, {
"entities":[
(0, 7, "CITY"),
(8, 16, "STATE_FULL"),
(17, 35, "STREET_ADDRESS"),
(36, 41, "ZIPCODE"),
(42, 44, "STATE"),
]
}),
(
"DE 19963 Milford Delaware 1164 Callison Lane"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 16, "CITY"),
(17, 25, "STATE_FULL"),
(26, 44, "STREET_ADDRESS"),
]
}),
(
"1164 Callison Lane DE Milford 19963 Delaware"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 21, "STATE"),
(22, 29, "CITY"),
(30, 35, "ZIPCODE"),
(36, 44, "STATE_FULL"),
]
}),
(
"19963 Milford 1164 Callison Lane Delaware DE"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 13, "CITY"),
(14, 32, "STREET_ADDRESS"),
(33, 41, "STATE_FULL"),
(42, 44, "STATE"),
]
}),
(
"2957 Sussex Court 76552 Copperas Cove TX Texas"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 23, "ZIPCODE"),
(24, 37, "CITY"),
(38, 40, "STATE"),
(41, 46, "STATE_FULL"),
]
}),
(
"Copperas Cove 2957 Sussex Court 76552 Texas TX"
, {
"entities":[
(0, 13, "CITY"),
(14, 31, "STREET_ADDRESS"),
(32, 37, "ZIPCODE"),
(38, 43, "STATE_FULL"),
(44, 46, "STATE"),
]
}),
(
"2957 Sussex Court TX Texas 76552 Copperas Cove"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 20, "STATE"),
(21, 26, "STATE_FULL"),
(27, 32, "ZIPCODE"),
(33, 46, "CITY"),
]
}),
(
"2957 Sussex Court Copperas Cove Texas 76552 TX"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 31, "CITY"),
(32, 37, "STATE_FULL"),
(38, 43, "ZIPCODE"),
(44, 46, "STATE"),
]
}),
(
"2957 Sussex Court 76552 Copperas Cove TX Texas"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 23, "ZIPCODE"),
(24, 37, "CITY"),
(38, 40, "STATE"),
(41, 46, "STATE_FULL"),
]
}),
(
"76552 TX Copperas Cove Texas 2957 Sussex Court"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 22, "CITY"),
(23, 28, "STATE_FULL"),
(29, 46, "STREET_ADDRESS"),
]
}),
(
"Texas 76552 TX 2957 Sussex Court Copperas Cove"
, {
"entities":[
(0, 5, "STATE_FULL"),
(6, 11, "ZIPCODE"),
(12, 14, "STATE"),
(15, 32, "STREET_ADDRESS"),
(33, 46, "CITY"),
]
}),
(
"2957 Sussex Court 76552 TX Copperas Cove Texas"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 23, "ZIPCODE"),
(24, 26, "STATE"),
(27, 40, "CITY"),
(41, 46, "STATE_FULL"),
]
}),
(
"TX Texas 2957 Sussex Court Copperas Cove 76552"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "STATE_FULL"),
(9, 26, "STREET_ADDRESS"),
(27, 40, "CITY"),
(41, 46, "ZIPCODE"),
]
}),
(
"TX Copperas Cove 2957 Sussex Court 76552 Texas"
, {
"entities":[
(0, 2, "STATE"),
(3, 16, "CITY"),
(17, 34, "STREET_ADDRESS"),
(35, 40, "ZIPCODE"),
(41, 46, "STATE_FULL"),
]
}),
(
"VA 23803 2540 Eden Drive Petersburg Virginia that"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 24, "STREET_ADDRESS"),
(25, 35, "CITY"),
(36, 44, "STATE_FULL"),
]
}),
(
"that Virginia 23803 2540 Eden Drive Petersburg VA"
, {
"entities":[
(5, 13, "STATE_FULL"),
(14, 19, "ZIPCODE"),
(20, 35, "STREET_ADDRESS"),
(36, 46, "CITY"),
(47, 49, "STATE"),
]
}),
(
"VA Petersburg 2540 Eden Drive that Virginia 23803"
, {
"entities":[
(0, 2, "STATE"),
(3, 13, "CITY"),
(14, 29, "STREET_ADDRESS"),
(35, 43, "STATE_FULL"),
(44, 49, "ZIPCODE"),
]
}),
(
"23803 Virginia VA Petersburg that 2540 Eden Drive"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 14, "STATE_FULL"),
(15, 17, "STATE"),
(18, 28, "CITY"),
(34, 49, "STREET_ADDRESS"),
]
}),
(
"2540 Eden Drive Petersburg VA that 23803 Virginia"
, {
"entities":[
(0, 15, "STREET_ADDRESS"),
(16, 26, "CITY"),
(27, 29, "STATE"),
(35, 40, "ZIPCODE"),
(41, 49, "STATE_FULL"),
]
}),
(
"Petersburg 2540 Eden Drive 23803 that Virginia VA"
, {
"entities":[
(0, 10, "CITY"),
(11, 26, "STREET_ADDRESS"),
(27, 32, "ZIPCODE"),
(38, 46, "STATE_FULL"),
(47, 49, "STATE"),
]
}),
(
"VA 2540 Eden Drive Petersburg 23803 Virginia that"
, {
"entities":[
(0, 2, "STATE"),
(3, 18, "STREET_ADDRESS"),
(19, 29, "CITY"),
(30, 35, "ZIPCODE"),
(36, 44, "STATE_FULL"),
]
}),
(
"VA that 23803 Petersburg Virginia 2540 Eden Drive"
, {
"entities":[
(0, 2, "STATE"),
(8, 13, "ZIPCODE"),
(14, 24, "CITY"),
(25, 33, "STATE_FULL"),
(34, 49, "STREET_ADDRESS"),
]
}),
(
"VA that 23803 Petersburg 2540 Eden Drive Virginia"
, {
"entities":[
(0, 2, "STATE"),
(8, 13, "ZIPCODE"),
(14, 24, "CITY"),
(25, 40, "STREET_ADDRESS"),
(41, 49, "STATE_FULL"),
]
}),
(
"Petersburg VA Virginia 23803 that 2540 Eden Drive"
, {
"entities":[
(0, 10, "CITY"),
(11, 13, "STATE"),
(14, 22, "STATE_FULL"),
(23, 28, "ZIPCODE"),
(34, 49, "STREET_ADDRESS"),
]
}),
(
"Kentucky KY 40071 Taylorsville 1605 Cerullo Road"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 11, "STATE"),
(12, 17, "ZIPCODE"),
(18, 30, "CITY"),
(31, 48, "STREET_ADDRESS"),
]
}),
(
"Kentucky 1605 Cerullo Road 40071 Taylorsville KY"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 26, "STREET_ADDRESS"),
(27, 32, "ZIPCODE"),
(33, 45, "CITY"),
(46, 48, "STATE"),
]
}),
(
"Kentucky 1605 Cerullo Road 40071 Taylorsville KY"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 26, "STREET_ADDRESS"),
(27, 32, "ZIPCODE"),
(33, 45, "CITY"),
(46, 48, "STATE"),
]
}),
(
"KY 1605 Cerullo Road Taylorsville Kentucky 40071"
, {
"entities":[
(0, 2, "STATE"),
(3, 20, "STREET_ADDRESS"),
(21, 33, "CITY"),
(34, 42, "STATE_FULL"),
(43, 48, "ZIPCODE"),
]
}),
(
"Taylorsville Kentucky 1605 Cerullo Road KY 40071"
, {
"entities":[
(0, 12, "CITY"),
(13, 21, "STATE_FULL"),
(22, 39, "STREET_ADDRESS"),
(40, 42, "STATE"),
(43, 48, "ZIPCODE"),
]
}),
(
"40071 Taylorsville KY 1605 Cerullo Road Kentucky"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "CITY"),
(19, 21, "STATE"),
(22, 39, "STREET_ADDRESS"),
(40, 48, "STATE_FULL"),
]
}),
(
"Taylorsville 40071 1605 Cerullo Road KY Kentucky"
, {
"entities":[
(0, 12, "CITY"),
(13, 18, "ZIPCODE"),
(19, 36, "STREET_ADDRESS"),
(37, 39, "STATE"),
(40, 48, "STATE_FULL"),
]
}),
(
"1605 Cerullo Road Kentucky 40071 Taylorsville KY"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 26, "STATE_FULL"),
(27, 32, "ZIPCODE"),
(33, 45, "CITY"),
(46, 48, "STATE"),
]
}),
(
"40071 KY Kentucky 1605 Cerullo Road Taylorsville"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 17, "STATE_FULL"),
(18, 35, "STREET_ADDRESS"),
(36, 48, "CITY"),
]
}),
(
"Kentucky 40071 1605 Cerullo Road Taylorsville KY"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 14, "ZIPCODE"),
(15, 32, "STREET_ADDRESS"),
(33, 45, "CITY"),
(46, 48, "STATE"),
]
}),
(
"32207 FL Florida Jacksonville 2674 Brannon Avenue"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 16, "STATE_FULL"),
(17, 29, "CITY"),
(30, 49, "STREET_ADDRESS"),
]
}),
(
"Florida FL Jacksonville 2674 Brannon Avenue 32207"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 10, "STATE"),
(11, 23, "CITY"),
(24, 43, "STREET_ADDRESS"),
(44, 49, "ZIPCODE"),
]
}),
(
"32207 2674 Brannon Avenue Jacksonville FL Florida"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 25, "STREET_ADDRESS"),
(26, 38, "CITY"),
(39, 41, "STATE"),
(42, 49, "STATE_FULL"),
]
}),
(
"2674 Brannon Avenue FL Jacksonville 32207 Florida"
, {
"entities":[
(0, 19, "STREET_ADDRESS"),
(20, 22, "STATE"),
(23, 35, "CITY"),
(36, 41, "ZIPCODE"),
(42, 49, "STATE_FULL"),
]
}),
(
"32207 FL Florida Jacksonville 2674 Brannon Avenue"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 16, "STATE_FULL"),
(17, 29, "CITY"),
(30, 49, "STREET_ADDRESS"),
]
}),
(
"32207 2674 Brannon Avenue FL Jacksonville Florida"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 25, "STREET_ADDRESS"),
(26, 28, "STATE"),
(29, 41, "CITY"),
(42, 49, "STATE_FULL"),
]
}),
(
"FL 32207 2674 Brannon Avenue Florida Jacksonville"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 28, "STREET_ADDRESS"),
(29, 36, "STATE_FULL"),
(37, 49, "CITY"),
]
}),
(
"Florida 2674 Brannon Avenue 32207 Jacksonville FL"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 27, "STREET_ADDRESS"),
(28, 33, "ZIPCODE"),
(34, 46, "CITY"),
(47, 49, "STATE"),
]
}),
(
"2674 Brannon Avenue FL Florida 32207 Jacksonville"
, {
"entities":[
(0, 19, "STREET_ADDRESS"),
(20, 22, "STATE"),
(23, 30, "STATE_FULL"),
(31, 36, "ZIPCODE"),
(37, 49, "CITY"),
]
}),
(
"Jacksonville Florida 2674 Brannon Avenue FL 32207"
, {
"entities":[
(0, 12, "CITY"),
(13, 20, "STATE_FULL"),
(21, 40, "STREET_ADDRESS"),
(41, 43, "STATE"),
(44, 49, "ZIPCODE"),
]
}),
(
"2497 Meadowbrook Mall Road 90017 CA California Los Angeles"
, {
"entities":[
(0, 26, "STREET_ADDRESS"),
(27, 32, "ZIPCODE"),
(33, 35, "STATE"),
(36, 46, "STATE_FULL"),
(47, 58, "CITY"),
]
}),
(
"2497 Meadowbrook Mall Road Los Angeles CA California 90017"
, {
"entities":[
(0, 26, "STREET_ADDRESS"),
(27, 38, "CITY"),
(39, 41, "STATE"),
(42, 52, "STATE_FULL"),
(53, 58, "ZIPCODE"),
]
}),
(
"California 90017 Los Angeles 2497 Meadowbrook Mall Road CA"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 16, "ZIPCODE"),
(17, 28, "CITY"),
(29, 55, "STREET_ADDRESS"),
(56, 58, "STATE"),
]
}),
(
"California CA Los Angeles 2497 Meadowbrook Mall Road 90017"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 13, "STATE"),
(14, 25, "CITY"),
(26, 52, "STREET_ADDRESS"),
(53, 58, "ZIPCODE"),
]
}),
(
"90017 Los Angeles California 2497 Meadowbrook Mall Road CA"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 17, "CITY"),
(18, 28, "STATE_FULL"),
(29, 55, "STREET_ADDRESS"),
(56, 58, "STATE"),
]
}),
(
"90017 CA California Los Angeles 2497 Meadowbrook Mall Road"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 19, "STATE_FULL"),
(20, 31, "CITY"),
(32, 58, "STREET_ADDRESS"),
]
}),
(
"2497 Meadowbrook Mall Road 90017 CA California Los Angeles"
, {
"entities":[
(0, 26, "STREET_ADDRESS"),
(27, 32, "ZIPCODE"),
(33, 35, "STATE"),
(36, 46, "STATE_FULL"),
(47, 58, "CITY"),
]
}),
(
"90017 2497 Meadowbrook Mall Road CA Los Angeles California"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 32, "STREET_ADDRESS"),
(33, 35, "STATE"),
(36, 47, "CITY"),
(48, 58, "STATE_FULL"),
]
}),
(
"California 2497 Meadowbrook Mall Road CA 90017 Los Angeles"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 37, "STREET_ADDRESS"),
(38, 40, "STATE"),
(41, 46, "ZIPCODE"),
(47, 58, "CITY"),
]
}),
(
"90017 California Los Angeles CA 2497 Meadowbrook Mall Road"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 16, "STATE_FULL"),
(17, 28, "CITY"),
(29, 31, "STATE"),
(32, 58, "STREET_ADDRESS"),
]
}),
(
"GA 774 Fowler Avenue Norcross 30071 Georgia"
, {
"entities":[
(0, 2, "STATE"),
(3, 20, "STREET_ADDRESS"),
(21, 29, "CITY"),
(30, 35, "ZIPCODE"),
(36, 43, "STATE_FULL"),
]
}),
(
"30071 Georgia GA Norcross 774 Fowler Avenue"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 13, "STATE_FULL"),
(14, 16, "STATE"),
(17, 25, "CITY"),
(26, 43, "STREET_ADDRESS"),
]
}),
(
"Norcross 30071 774 Fowler Avenue GA Georgia"
, {
"entities":[
(0, 8, "CITY"),
(9, 14, "ZIPCODE"),
(15, 32, "STREET_ADDRESS"),
(33, 35, "STATE"),
(36, 43, "STATE_FULL"),
]
}),
(
"Georgia 30071 Norcross 774 Fowler Avenue GA"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 13, "ZIPCODE"),
(14, 22, "CITY"),
(23, 40, "STREET_ADDRESS"),
(41, 43, "STATE"),
]
}),
(
"Norcross 30071 774 Fowler Avenue Georgia GA"
, {
"entities":[
(0, 8, "CITY"),
(9, 14, "ZIPCODE"),
(15, 32, "STREET_ADDRESS"),
(33, 40, "STATE_FULL"),
(41, 43, "STATE"),
]
}),
(
"Norcross Georgia GA 30071 774 Fowler Avenue"
, {
"entities":[
(0, 8, "CITY"),
(9, 16, "STATE_FULL"),
(17, 19, "STATE"),
(20, 25, "ZIPCODE"),
(26, 43, "STREET_ADDRESS"),
]
}),
(
"30071 774 Fowler Avenue GA Georgia Norcross"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 23, "STREET_ADDRESS"),
(24, 26, "STATE"),
(27, 34, "STATE_FULL"),
(35, 43, "CITY"),
]
}),
(
"GA 774 Fowler Avenue Georgia Norcross 30071"
, {
"entities":[
(0, 2, "STATE"),
(3, 20, "STREET_ADDRESS"),
(21, 28, "STATE_FULL"),
(29, 37, "CITY"),
(38, 43, "ZIPCODE"),
]
}),
(
"774 Fowler Avenue GA 30071 Norcross Georgia"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 20, "STATE"),
(21, 26, "ZIPCODE"),
(27, 35, "CITY"),
(36, 43, "STATE_FULL"),
]
}),
(
"774 Fowler Avenue 30071 Georgia Norcross GA"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 23, "ZIPCODE"),
(24, 31, "STATE_FULL"),
(32, 40, "CITY"),
(41, 43, "STATE"),
]
}),
(
"2602 Russell Street Cambridge MA Massachusetts 02141"
, {
"entities":[
(0, 19, "STREET_ADDRESS"),
(20, 29, "CITY"),
(30, 32, "STATE"),
(33, 46, "STATE_FULL"),
(47, 52, "ZIPCODE"),
]
}),
(
"Cambridge Massachusetts MA 02141 2602 Russell Street"
, {
"entities":[
(0, 9, "CITY"),
(10, 23, "STATE_FULL"),
(24, 26, "STATE"),
(27, 32, "ZIPCODE"),
(33, 52, "STREET_ADDRESS"),
]
}),
(
"MA 2602 Russell Street 02141 Cambridge Massachusetts"
, {
"entities":[
(0, 2, "STATE"),
(3, 22, "STREET_ADDRESS"),
(23, 28, "ZIPCODE"),
(29, 38, "CITY"),
(39, 52, "STATE_FULL"),
]
}),
(
"MA Massachusetts Cambridge 2602 Russell Street 02141"
, {
"entities":[
(0, 2, "STATE"),
(3, 16, "STATE_FULL"),
(17, 26, "CITY"),
(27, 46, "STREET_ADDRESS"),
(47, 52, "ZIPCODE"),
]
}),
(
"Massachusetts MA 02141 2602 Russell Street Cambridge"
, {
"entities":[
(0, 13, "STATE_FULL"),
(14, 16, "STATE"),
(17, 22, "ZIPCODE"),
(23, 42, "STREET_ADDRESS"),
(43, 52, "CITY"),
]
}),
(
"02141 2602 Russell Street Massachusetts Cambridge MA"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 25, "STREET_ADDRESS"),
(26, 39, "STATE_FULL"),
(40, 49, "CITY"),
(50, 52, "STATE"),
]
}),
(
"Massachusetts MA 2602 Russell Street 02141 Cambridge"
, {
"entities":[
(0, 13, "STATE_FULL"),
(14, 16, "STATE"),
(17, 36, "STREET_ADDRESS"),
(37, 42, "ZIPCODE"),
(43, 52, "CITY"),
]
}),
(
"Massachusetts 02141 2602 Russell Street Cambridge MA"
, {
"entities":[
(0, 13, "STATE_FULL"),
(14, 19, "ZIPCODE"),
(20, 39, "STREET_ADDRESS"),
(40, 49, "CITY"),
(50, 52, "STATE"),
]
}),
(
"02141 Massachusetts Cambridge MA 2602 Russell Street"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 19, "STATE_FULL"),
(20, 29, "CITY"),
(30, 32, "STATE"),
(33, 52, "STREET_ADDRESS"),
]
}),
(
"MA Massachusetts 2602 Russell Street Cambridge 02141"
, {
"entities":[
(0, 2, "STATE"),
(3, 16, "STATE_FULL"),
(17, 36, "STREET_ADDRESS"),
(37, 46, "CITY"),
(47, 52, "ZIPCODE"),
]
}),
(
"IL 60610 Illinois Chicago 649 West Drive"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 17, "STATE_FULL"),
(18, 25, "CITY"),
(26, 40, "STREET_ADDRESS"),
]
}),
(
"649 West Drive 60610 IL Chicago Illinois"
, {
"entities":[
(0, 14, "STREET_ADDRESS"),
(15, 20, "ZIPCODE"),
(21, 23, "STATE"),
(24, 31, "CITY"),
(32, 40, "STATE_FULL"),
]
}),
(
"IL Illinois 649 West Drive 60610 Chicago"
, {
"entities":[
(0, 2, "STATE"),
(3, 11, "STATE_FULL"),
(12, 26, "STREET_ADDRESS"),
(27, 32, "ZIPCODE"),
(33, 40, "CITY"),
]
}),
(
"IL 60610 Illinois Chicago 649 West Drive"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 17, "STATE_FULL"),
(18, 25, "CITY"),
(26, 40, "STREET_ADDRESS"),
]
}),
(
"Chicago Illinois IL 60610 649 West Drive"
, {
"entities":[
(0, 7, "CITY"),
(8, 16, "STATE_FULL"),
(17, 19, "STATE"),
(20, 25, "ZIPCODE"),
(26, 40, "STREET_ADDRESS"),
]
}),
(
"649 West Drive IL Chicago Illinois 60610"
, {
"entities":[
(0, 14, "STREET_ADDRESS"),
(15, 17, "STATE"),
(18, 25, "CITY"),
(26, 34, "STATE_FULL"),
(35, 40, "ZIPCODE"),
]
}),
(
"649 West Drive Chicago Illinois IL 60610"
, {
"entities":[
(0, 14, "STREET_ADDRESS"),
(15, 22, "CITY"),
(23, 31, "STATE_FULL"),
(32, 34, "STATE"),
(35, 40, "ZIPCODE"),
]
}),
(
"60610 IL Chicago 649 West Drive Illinois"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 16, "CITY"),
(17, 31, "STREET_ADDRESS"),
(32, 40, "STATE_FULL"),
]
}),
(
"649 West Drive 60610 Illinois IL Chicago"
, {
"entities":[
(0, 14, "STREET_ADDRESS"),
(15, 20, "ZIPCODE"),
(21, 29, "STATE_FULL"),
(30, 32, "STATE"),
(33, 40, "CITY"),
]
}),
(
"IL Illinois Chicago 60610 649 West Drive"
, {
"entities":[
(0, 2, "STATE"),
(3, 11, "STATE_FULL"),
(12, 19, "CITY"),
(20, 25, "ZIPCODE"),
(26, 40, "STREET_ADDRESS"),
]
}),
(
"28105 North Carolina Matthews information NC 3159 Diamond Street"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 20, "STATE_FULL"),
(21, 29, "CITY"),
(42, 44, "STATE"),
(45, 64, "STREET_ADDRESS"),
]
}),
(
"3159 Diamond Street NC Matthews North Carolina 28105 information"
, {
"entities":[
(0, 19, "STREET_ADDRESS"),
(20, 22, "STATE"),
(23, 31, "CITY"),
(32, 46, "STATE_FULL"),
(47, 52, "ZIPCODE"),
]
}),
(
"Matthews North Carolina information NC 28105 3159 Diamond Street"
, {
"entities":[
(0, 8, "CITY"),
(9, 23, "STATE_FULL"),
(36, 38, "STATE"),
(39, 44, "ZIPCODE"),
(45, 64, "STREET_ADDRESS"),
]
}),
(
"North Carolina 3159 Diamond Street Matthews NC information 28105"
, {
"entities":[
(0, 14, "STATE_FULL"),
(15, 34, "STREET_ADDRESS"),
(35, 43, "CITY"),
(44, 46, "STATE"),
(59, 64, "ZIPCODE"),
]
}),
(
"Matthews information NC North Carolina 3159 Diamond Street 28105"
, {
"entities":[
(0, 8, "CITY"),
(21, 23, "STATE"),
(24, 38, "STATE_FULL"),
(39, 58, "STREET_ADDRESS"),
(59, 64, "ZIPCODE"),
]
}),
(
"information North Carolina Matthews 28105 NC 3159 Diamond Street"
, {
"entities":[
(12, 26, "STATE_FULL"),
(27, 35, "CITY"),
(36, 41, "ZIPCODE"),
(42, 44, "STATE"),
(45, 64, "STREET_ADDRESS"),
]
}),
(
"information 3159 Diamond Street North Carolina 28105 Matthews NC"
, {
"entities":[
(12, 31, "STREET_ADDRESS"),
(32, 46, "STATE_FULL"),
(47, 52, "ZIPCODE"),
(53, 61, "CITY"),
(62, 64, "STATE"),
]
}),
(
"Matthews 3159 Diamond Street 28105 NC North Carolina information"
, {
"entities":[
(0, 8, "CITY"),
(9, 28, "STREET_ADDRESS"),
(29, 34, "ZIPCODE"),
(35, 37, "STATE"),
(38, 52, "STATE_FULL"),
]
}),
(
"North Carolina 28105 NC 3159 Diamond Street information Matthews"
, {
"entities":[
(0, 14, "STATE_FULL"),
(15, 20, "ZIPCODE"),
(21, 23, "STATE"),
(24, 43, "STREET_ADDRESS"),
(56, 64, "CITY"),
]
}),
(
"28105 3159 Diamond Street Matthews NC information North Carolina"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 25, "STREET_ADDRESS"),
(26, 34, "CITY"),
(35, 37, "STATE"),
(50, 64, "STATE_FULL"),
]
}),
(
"Texas TX Dallas 75240 1669 Whispering Pines Circle"
, {
"entities":[
(0, 5, "STATE_FULL"),
(6, 8, "STATE"),
(9, 15, "CITY"),
(16, 21, "ZIPCODE"),
(22, 50, "STREET_ADDRESS"),
]
}),
(
"75240 TX Dallas 1669 Whispering Pines Circle Texas"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 15, "CITY"),
(16, 44, "STREET_ADDRESS"),
(45, 50, "STATE_FULL"),
]
}),
(
"Texas Dallas 1669 Whispering Pines Circle TX 75240"
, {
"entities":[
(0, 5, "STATE_FULL"),
(6, 12, "CITY"),
(13, 41, "STREET_ADDRESS"),
(42, 44, "STATE"),
(45, 50, "ZIPCODE"),
]
}),
(
"Dallas 75240 1669 Whispering Pines Circle TX Texas"
, {
"entities":[
(0, 6, "CITY"),
(7, 12, "ZIPCODE"),
(13, 41, "STREET_ADDRESS"),
(42, 44, "STATE"),
(45, 50, "STATE_FULL"),
]
}),
(
"TX 75240 Texas Dallas 1669 Whispering Pines Circle"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 14, "STATE_FULL"),
(15, 21, "CITY"),
(22, 50, "STREET_ADDRESS"),
]
}),
(
"Texas 1669 Whispering Pines Circle 75240 TX Dallas"
, {
"entities":[
(0, 5, "STATE_FULL"),
(6, 34, "STREET_ADDRESS"),
(35, 40, "ZIPCODE"),
(41, 43, "STATE"),
(44, 50, "CITY"),
]
}),
(
"Texas Dallas 1669 Whispering Pines Circle 75240 TX"
, {
"entities":[
(0, 5, "STATE_FULL"),
(6, 12, "CITY"),
(13, 41, "STREET_ADDRESS"),
(42, 47, "ZIPCODE"),
(48, 50, "STATE"),
]
}),
(
"75240 Texas 1669 Whispering Pines Circle Dallas TX"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 11, "STATE_FULL"),
(12, 40, "STREET_ADDRESS"),
(41, 47, "CITY"),
(48, 50, "STATE"),
]
}),
(
"TX Texas 1669 Whispering Pines Circle Dallas 75240"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "STATE_FULL"),
(9, 37, "STREET_ADDRESS"),
(38, 44, "CITY"),
(45, 50, "ZIPCODE"),
]
}),
(
"1669 Whispering Pines Circle 75240 Texas TX Dallas"
, {
"entities":[
(0, 28, "STREET_ADDRESS"),
(29, 34, "ZIPCODE"),
(35, 40, "STATE_FULL"),
(41, 43, "STATE"),
(44, 50, "CITY"),
]
}),
(
"72443 AR Marmaduke 2708 Barrington Court Arkansas"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 18, "CITY"),
(19, 40, "STREET_ADDRESS"),
(41, 49, "STATE_FULL"),
]
}),
(
"Marmaduke 2708 Barrington Court Arkansas AR 72443"
, {
"entities":[
(0, 9, "CITY"),
(10, 31, "STREET_ADDRESS"),
(32, 40, "STATE_FULL"),
(41, 43, "STATE"),
(44, 49, "ZIPCODE"),
]
}),
(
"AR Marmaduke 72443 2708 Barrington Court Arkansas"
, {
"entities":[
(0, 2, "STATE"),
(3, 12, "CITY"),
(13, 18, "ZIPCODE"),
(19, 40, "STREET_ADDRESS"),
(41, 49, "STATE_FULL"),
]
}),
(
"Arkansas 2708 Barrington Court AR Marmaduke 72443"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 30, "STREET_ADDRESS"),
(31, 33, "STATE"),
(34, 43, "CITY"),
(44, 49, "ZIPCODE"),
]
}),
(
"72443 AR 2708 Barrington Court Marmaduke Arkansas"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 30, "STREET_ADDRESS"),
(31, 40, "CITY"),
(41, 49, "STATE_FULL"),
]
}),
(
"72443 2708 Barrington Court AR Marmaduke Arkansas"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 27, "STREET_ADDRESS"),
(28, 30, "STATE"),
(31, 40, "CITY"),
(41, 49, "STATE_FULL"),
]
}),
(
"72443 2708 Barrington Court Arkansas AR Marmaduke"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 27, "STREET_ADDRESS"),
(28, 36, "STATE_FULL"),
(37, 39, "STATE"),
(40, 49, "CITY"),
]
}),
(
"2708 Barrington Court Arkansas Marmaduke 72443 AR"
, {
"entities":[
(0, 21, "STREET_ADDRESS"),
(22, 30, "STATE_FULL"),
(31, 40, "CITY"),
(41, 46, "ZIPCODE"),
(47, 49, "STATE"),
]
}),
(
"AR 72443 Arkansas Marmaduke 2708 Barrington Court"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 17, "STATE_FULL"),
(18, 27, "CITY"),
(28, 49, "STREET_ADDRESS"),
]
}),
(
"72443 Arkansas 2708 Barrington Court AR Marmaduke"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 14, "STATE_FULL"),
(15, 36, "STREET_ADDRESS"),
(37, 39, "STATE"),
(40, 49, "CITY"),
]
}),
(
"3300 Walnut Drive North Dakota Fargo 58102 ND"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 30, "STATE_FULL"),
(31, 36, "CITY"),
(37, 42, "ZIPCODE"),
(43, 45, "STATE"),
]
}),
(
"58102 ND 3300 Walnut Drive North Dakota Fargo"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 26, "STREET_ADDRESS"),
(27, 39, "STATE_FULL"),
(40, 45, "CITY"),
]
}),
(
"58102 Fargo North Dakota 3300 Walnut Drive ND"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 11, "CITY"),
(12, 24, "STATE_FULL"),
(25, 42, "STREET_ADDRESS"),
(43, 45, "STATE"),
]
}),
(
"Fargo ND 58102 3300 Walnut Drive North Dakota"
, {
"entities":[
(0, 5, "CITY"),
(6, 8, "STATE"),
(9, 14, "ZIPCODE"),
(15, 32, "STREET_ADDRESS"),
(33, 45, "STATE_FULL"),
]
}),
(
"Fargo North Dakota 58102 ND 3300 Walnut Drive"
, {
"entities":[
(0, 5, "CITY"),
(6, 18, "STATE_FULL"),
(19, 24, "ZIPCODE"),
(25, 27, "STATE"),
(28, 45, "STREET_ADDRESS"),
]
}),
(
"North Dakota 3300 Walnut Drive Fargo 58102 ND"
, {
"entities":[
(0, 12, "STATE_FULL"),
(13, 30, "STREET_ADDRESS"),
(31, 36, "CITY"),
(37, 42, "ZIPCODE"),
(43, 45, "STATE"),
]
}),
(
"Fargo 3300 Walnut Drive 58102 ND North Dakota"
, {
"entities":[
(0, 5, "CITY"),
(6, 23, "STREET_ADDRESS"),
(24, 29, "ZIPCODE"),
(30, 32, "STATE"),
(33, 45, "STATE_FULL"),
]
}),
(
"ND 3300 Walnut Drive 58102 Fargo North Dakota"
, {
"entities":[
(0, 2, "STATE"),
(3, 20, "STREET_ADDRESS"),
(21, 26, "ZIPCODE"),
(27, 32, "CITY"),
(33, 45, "STATE_FULL"),
]
}),
(
"ND 58102 North Dakota Fargo 3300 Walnut Drive"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 21, "STATE_FULL"),
(22, 27, "CITY"),
(28, 45, "STREET_ADDRESS"),
]
}),
(
"ND Fargo 3300 Walnut Drive 58102 North Dakota"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "CITY"),
(9, 26, "STREET_ADDRESS"),
(27, 32, "ZIPCODE"),
(33, 45, "STATE_FULL"),
]
}),
(
"Boston 02114 Massachusetts MA 3573 Lynn Street"
, {
"entities":[
(0, 6, "CITY"),
(7, 12, "ZIPCODE"),
(13, 26, "STATE_FULL"),
(27, 29, "STATE"),
(30, 46, "STREET_ADDRESS"),
]
}),
(
"Massachusetts MA Boston 3573 Lynn Street 02114"
, {
"entities":[
(0, 13, "STATE_FULL"),
(14, 16, "STATE"),
(17, 23, "CITY"),
(24, 40, "STREET_ADDRESS"),
(41, 46, "ZIPCODE"),
]
}),
(
"Massachusetts 3573 Lynn Street Boston MA 02114"
, {
"entities":[
(0, 13, "STATE_FULL"),
(14, 30, "STREET_ADDRESS"),
(31, 37, "CITY"),
(38, 40, "STATE"),
(41, 46, "ZIPCODE"),
]
}),
(
"Massachusetts 3573 Lynn Street 02114 MA Boston"
, {
"entities":[
(0, 13, "STATE_FULL"),
(14, 30, "STREET_ADDRESS"),
(31, 36, "ZIPCODE"),
(37, 39, "STATE"),
(40, 46, "CITY"),
]
}),
(
"Boston Massachusetts 02114 3573 Lynn Street MA"
, {
"entities":[
(0, 6, "CITY"),
(7, 20, "STATE_FULL"),
(21, 26, "ZIPCODE"),
(27, 43, "STREET_ADDRESS"),
(44, 46, "STATE"),
]
}),
(
"02114 3573 Lynn Street Massachusetts MA Boston"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 22, "STREET_ADDRESS"),
(23, 36, "STATE_FULL"),
(37, 39, "STATE"),
(40, 46, "CITY"),
]
}),
(
"Boston 3573 Lynn Street MA 02114 Massachusetts"
, {
"entities":[
(0, 6, "CITY"),
(7, 23, "STREET_ADDRESS"),
(24, 26, "STATE"),
(27, 32, "ZIPCODE"),
(33, 46, "STATE_FULL"),
]
}),
(
"Massachusetts 3573 Lynn Street Boston MA 02114"
, {
"entities":[
(0, 13, "STATE_FULL"),
(14, 30, "STREET_ADDRESS"),
(31, 37, "CITY"),
(38, 40, "STATE"),
(41, 46, "ZIPCODE"),
]
}),
(
"02114 3573 Lynn Street Massachusetts Boston MA"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 22, "STREET_ADDRESS"),
(23, 36, "STATE_FULL"),
(37, 43, "CITY"),
(44, 46, "STATE"),
]
}),
(
"3573 Lynn Street Boston MA Massachusetts 02114"
, {
"entities":[
(0, 16, "STREET_ADDRESS"),
(17, 23, "CITY"),
(24, 26, "STATE"),
(27, 40, "STATE_FULL"),
(41, 46, "ZIPCODE"),
]
}),
(
"Wisconsin 53151 1610 Joseph Street WI New Berlin"
, {
"entities":[
(0, 9, "STATE_FULL"),
(10, 15, "ZIPCODE"),
(16, 34, "STREET_ADDRESS"),
(35, 37, "STATE"),
(38, 48, "CITY"),
]
}),
(
"WI 1610 Joseph Street New Berlin Wisconsin 53151"
, {
"entities":[
(0, 2, "STATE"),
(3, 21, "STREET_ADDRESS"),
(22, 32, "CITY"),
(33, 42, "STATE_FULL"),
(43, 48, "ZIPCODE"),
]
}),
(
"53151 WI Wisconsin 1610 Joseph Street New Berlin"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 18, "STATE_FULL"),
(19, 37, "STREET_ADDRESS"),
(38, 48, "CITY"),
]
}),
(
"53151 1610 Joseph Street Wisconsin WI New Berlin"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 24, "STREET_ADDRESS"),
(25, 34, "STATE_FULL"),
(35, 37, "STATE"),
(38, 48, "CITY"),
]
}),
(
"Wisconsin WI 53151 1610 Joseph Street New Berlin"
, {
"entities":[
(0, 9, "STATE_FULL"),
(10, 12, "STATE"),
(13, 18, "ZIPCODE"),
(19, 37, "STREET_ADDRESS"),
(38, 48, "CITY"),
]
}),
(
"New Berlin 1610 Joseph Street 53151 Wisconsin WI"
, {
"entities":[
(0, 10, "CITY"),
(11, 29, "STREET_ADDRESS"),
(30, 35, "ZIPCODE"),
(36, 45, "STATE_FULL"),
(46, 48, "STATE"),
]
}),
(
"1610 Joseph Street 53151 Wisconsin WI New Berlin"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 24, "ZIPCODE"),
(25, 34, "STATE_FULL"),
(35, 37, "STATE"),
(38, 48, "CITY"),
]
}),
(
"New Berlin WI 1610 Joseph Street Wisconsin 53151"
, {
"entities":[
(0, 10, "CITY"),
(11, 13, "STATE"),
(14, 32, "STREET_ADDRESS"),
(33, 42, "STATE_FULL"),
(43, 48, "ZIPCODE"),
]
}),
(
"New Berlin Wisconsin WI 1610 Joseph Street 53151"
, {
"entities":[
(0, 10, "CITY"),
(11, 20, "STATE_FULL"),
(21, 23, "STATE"),
(24, 42, "STREET_ADDRESS"),
(43, 48, "ZIPCODE"),
]
}),
(
"1610 Joseph Street Wisconsin WI 53151 New Berlin"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 28, "STATE_FULL"),
(29, 31, "STATE"),
(32, 37, "ZIPCODE"),
(38, 48, "CITY"),
]
}),
(
"94612 Oakland CA 1611 Green Avenue California"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 13, "CITY"),
(14, 16, "STATE"),
(17, 34, "STREET_ADDRESS"),
(35, 45, "STATE_FULL"),
]
}),
(
"1611 Green Avenue CA Oakland California 94612"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 20, "STATE"),
(21, 28, "CITY"),
(29, 39, "STATE_FULL"),
(40, 45, "ZIPCODE"),
]
}),
(
"1611 Green Avenue California 94612 Oakland CA"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 28, "STATE_FULL"),
(29, 34, "ZIPCODE"),
(35, 42, "CITY"),
(43, 45, "STATE"),
]
}),
(
"94612 CA Oakland 1611 Green Avenue California"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 16, "CITY"),
(17, 34, "STREET_ADDRESS"),
(35, 45, "STATE_FULL"),
]
}),
(
"94612 CA 1611 Green Avenue California Oakland"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 26, "STREET_ADDRESS"),
(27, 37, "STATE_FULL"),
(38, 45, "CITY"),
]
}),
(
"Oakland California 94612 1611 Green Avenue CA"
, {
"entities":[
(0, 7, "CITY"),
(8, 18, "STATE_FULL"),
(19, 24, "ZIPCODE"),
(25, 42, "STREET_ADDRESS"),
(43, 45, "STATE"),
]
}),
(
"1611 Green Avenue California 94612 CA Oakland"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 28, "STATE_FULL"),
(29, 34, "ZIPCODE"),
(35, 37, "STATE"),
(38, 45, "CITY"),
]
}),
(
"CA 94612 1611 Green Avenue Oakland California"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 26, "STREET_ADDRESS"),
(27, 34, "CITY"),
(35, 45, "STATE_FULL"),
]
}),
(
"94612 1611 Green Avenue California CA Oakland"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 23, "STREET_ADDRESS"),
(24, 34, "STATE_FULL"),
(35, 37, "STATE"),
(38, 45, "CITY"),
]
}),
(
"California CA 1611 Green Avenue 94612 Oakland"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 13, "STATE"),
(14, 31, "STREET_ADDRESS"),
(32, 37, "ZIPCODE"),
(38, 45, "CITY"),
]
}),
(
"Montana 59401 MT Great Falls 1929 Tibbs Avenue"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 13, "ZIPCODE"),
(14, 16, "STATE"),
(17, 28, "CITY"),
(29, 46, "STREET_ADDRESS"),
]
}),
(
"MT 59401 1929 Tibbs Avenue Great Falls Montana"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 26, "STREET_ADDRESS"),
(27, 38, "CITY"),
(39, 46, "STATE_FULL"),
]
}),
(
"MT 59401 Great Falls 1929 Tibbs Avenue Montana"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 20, "CITY"),
(21, 38, "STREET_ADDRESS"),
(39, 46, "STATE_FULL"),
]
}),
(
"Montana Great Falls 1929 Tibbs Avenue MT 59401"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 19, "CITY"),
(20, 37, "STREET_ADDRESS"),
(38, 40, "STATE"),
(41, 46, "ZIPCODE"),
]
}),
(
"Montana MT 59401 Great Falls 1929 Tibbs Avenue"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 10, "STATE"),
(11, 16, "ZIPCODE"),
(17, 28, "CITY"),
(29, 46, "STREET_ADDRESS"),
]
}),
(
"59401 MT 1929 Tibbs Avenue Great Falls Montana"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 26, "STREET_ADDRESS"),
(27, 38, "CITY"),
(39, 46, "STATE_FULL"),
]
}),
(
"59401 Great Falls MT Montana 1929 Tibbs Avenue"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 17, "CITY"),
(18, 20, "STATE"),
(21, 28, "STATE_FULL"),
(29, 46, "STREET_ADDRESS"),
]
}),
(
"59401 Montana MT Great Falls 1929 Tibbs Avenue"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 13, "STATE_FULL"),
(14, 16, "STATE"),
(17, 28, "CITY"),
(29, 46, "STREET_ADDRESS"),
]
}),
(
"1929 Tibbs Avenue MT Great Falls Montana 59401"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 20, "STATE"),
(21, 32, "CITY"),
(33, 40, "STATE_FULL"),
(41, 46, "ZIPCODE"),
]
}),
(
"MT Montana 59401 1929 Tibbs Avenue Great Falls"
, {
"entities":[
(0, 2, "STATE"),
(3, 10, "STATE_FULL"),
(11, 16, "ZIPCODE"),
(17, 34, "STREET_ADDRESS"),
(35, 46, "CITY"),
]
}),
(
"25301 West Virginia 391 Columbia Mine Road Charleston WV"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 19, "STATE_FULL"),
(20, 42, "STREET_ADDRESS"),
(43, 53, "CITY"),
(54, 56, "STATE"),
]
}),
(
"Charleston 25301 391 Columbia Mine Road WV West Virginia"
, {
"entities":[
(0, 10, "CITY"),
(11, 16, "ZIPCODE"),
(17, 39, "STREET_ADDRESS"),
(40, 42, "STATE"),
(43, 56, "STATE_FULL"),
]
}),
(
"WV West Virginia 391 Columbia Mine Road Charleston 25301"
, {
"entities":[
(0, 2, "STATE"),
(3, 16, "STATE_FULL"),
(17, 39, "STREET_ADDRESS"),
(40, 50, "CITY"),
(51, 56, "ZIPCODE"),
]
}),
(
"WV Charleston 391 Columbia Mine Road West Virginia 25301"
, {
"entities":[
(0, 2, "STATE"),
(3, 13, "CITY"),
(14, 36, "STREET_ADDRESS"),
(37, 50, "STATE_FULL"),
(51, 56, "ZIPCODE"),
]
}),
(
"West Virginia Charleston 25301 391 Columbia Mine Road WV"
, {
"entities":[
(0, 13, "STATE_FULL"),
(14, 24, "CITY"),
(25, 30, "ZIPCODE"),
(31, 53, "STREET_ADDRESS"),
(54, 56, "STATE"),
]
}),
(
"391 Columbia Mine Road West Virginia 25301 WV Charleston"
, {
"entities":[
(0, 22, "STREET_ADDRESS"),
(23, 36, "STATE_FULL"),
(37, 42, "ZIPCODE"),
(43, 45, "STATE"),
(46, 56, "CITY"),
]
}),
(
"West Virginia WV 25301 391 Columbia Mine Road Charleston"
, {
"entities":[
(0, 13, "STATE_FULL"),
(14, 16, "STATE"),
(17, 22, "ZIPCODE"),
(23, 45, "STREET_ADDRESS"),
(46, 56, "CITY"),
]
}),
(
"Charleston 25301 WV 391 Columbia Mine Road West Virginia"
, {
"entities":[
(0, 10, "CITY"),
(11, 16, "ZIPCODE"),
(17, 19, "STATE"),
(20, 42, "STREET_ADDRESS"),
(43, 56, "STATE_FULL"),
]
}),
(
"WV Charleston 391 Columbia Mine Road 25301 West Virginia"
, {
"entities":[
(0, 2, "STATE"),
(3, 13, "CITY"),
(14, 36, "STREET_ADDRESS"),
(37, 42, "ZIPCODE"),
(43, 56, "STATE_FULL"),
]
}),
(
"West Virginia 391 Columbia Mine Road 25301 Charleston WV"
, {
"entities":[
(0, 13, "STATE_FULL"),
(14, 36, "STREET_ADDRESS"),
(37, 42, "ZIPCODE"),
(43, 53, "CITY"),
(54, 56, "STATE"),
]
}),
(
"4970 Jail Drive CA Los Angeles 90045 California"
, {
"entities":[
(0, 15, "STREET_ADDRESS"),
(16, 18, "STATE"),
(19, 30, "CITY"),
(31, 36, "ZIPCODE"),
(37, 47, "STATE_FULL"),
]
}),
(
"4970 Jail Drive California 90045 CA Los Angeles"
, {
"entities":[
(0, 15, "STREET_ADDRESS"),
(16, 26, "STATE_FULL"),
(27, 32, "ZIPCODE"),
(33, 35, "STATE"),
(36, 47, "CITY"),
]
}),
(
"California Los Angeles 90045 CA 4970 Jail Drive"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 22, "CITY"),
(23, 28, "ZIPCODE"),
(29, 31, "STATE"),
(32, 47, "STREET_ADDRESS"),
]
}),
(
"California 90045 CA 4970 Jail Drive Los Angeles"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 16, "ZIPCODE"),
(17, 19, "STATE"),
(20, 35, "STREET_ADDRESS"),
(36, 47, "CITY"),
]
}),
(
"Los Angeles CA California 4970 Jail Drive 90045"
, {
"entities":[
(0, 11, "CITY"),
(12, 14, "STATE"),
(15, 25, "STATE_FULL"),
(26, 41, "STREET_ADDRESS"),
(42, 47, "ZIPCODE"),
]
}),
(
"Los Angeles 4970 Jail Drive CA 90045 California"
, {
"entities":[
(0, 11, "CITY"),
(12, 27, "STREET_ADDRESS"),
(28, 30, "STATE"),
(31, 36, "ZIPCODE"),
(37, 47, "STATE_FULL"),
]
}),
(
"Los Angeles California 90045 4970 Jail Drive CA"
, {
"entities":[
(0, 11, "CITY"),
(12, 22, "STATE_FULL"),
(23, 28, "ZIPCODE"),
(29, 44, "STREET_ADDRESS"),
(45, 47, "STATE"),
]
}),
(
"Los Angeles California 90045 CA 4970 Jail Drive"
, {
"entities":[
(0, 11, "CITY"),
(12, 22, "STATE_FULL"),
(23, 28, "ZIPCODE"),
(29, 31, "STATE"),
(32, 47, "STREET_ADDRESS"),
]
}),
(
"Los Angeles 4970 Jail Drive California CA 90045"
, {
"entities":[
(0, 11, "CITY"),
(12, 27, "STREET_ADDRESS"),
(28, 38, "STATE_FULL"),
(39, 41, "STATE"),
(42, 47, "ZIPCODE"),
]
}),
(
"California 90045 4970 Jail Drive Los Angeles CA"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 16, "ZIPCODE"),
(17, 32, "STREET_ADDRESS"),
(33, 44, "CITY"),
(45, 47, "STATE"),
]
}),
(
"91941 CA 3854 Grim Avenue La Mesa California"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 25, "STREET_ADDRESS"),
(26, 33, "CITY"),
(34, 44, "STATE_FULL"),
]
}),
(
"91941 3854 Grim Avenue La Mesa CA California"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 22, "STREET_ADDRESS"),
(23, 30, "CITY"),
(31, 33, "STATE"),
(34, 44, "STATE_FULL"),
]
}),
(
"91941 California 3854 Grim Avenue La Mesa CA"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 16, "STATE_FULL"),
(17, 33, "STREET_ADDRESS"),
(34, 41, "CITY"),
(42, 44, "STATE"),
]
}),
(
"La Mesa CA California 3854 Grim Avenue 91941"
, {
"entities":[
(0, 7, "CITY"),
(8, 10, "STATE"),
(11, 21, "STATE_FULL"),
(22, 38, "STREET_ADDRESS"),
(39, 44, "ZIPCODE"),
]
}),
(
"La Mesa California 3854 Grim Avenue CA 91941"
, {
"entities":[
(0, 7, "CITY"),
(8, 18, "STATE_FULL"),
(19, 35, "STREET_ADDRESS"),
(36, 38, "STATE"),
(39, 44, "ZIPCODE"),
]
}),
(
"La Mesa 91941 3854 Grim Avenue California CA"
, {
"entities":[
(0, 7, "CITY"),
(8, 13, "ZIPCODE"),
(14, 30, "STREET_ADDRESS"),
(31, 41, "STATE_FULL"),
(42, 44, "STATE"),
]
}),
(
"91941 California 3854 Grim Avenue CA La Mesa"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 16, "STATE_FULL"),
(17, 33, "STREET_ADDRESS"),
(34, 36, "STATE"),
(37, 44, "CITY"),
]
}),
(
"La Mesa 91941 California CA 3854 Grim Avenue"
, {
"entities":[
(0, 7, "CITY"),
(8, 13, "ZIPCODE"),
(14, 24, "STATE_FULL"),
(25, 27, "STATE"),
(28, 44, "STREET_ADDRESS"),
]
}),
(
"91941 La Mesa CA 3854 Grim Avenue California"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 13, "CITY"),
(14, 16, "STATE"),
(17, 33, "STREET_ADDRESS"),
(34, 44, "STATE_FULL"),
]
}),
(
"La Mesa California 91941 CA 3854 Grim Avenue"
, {
"entities":[
(0, 7, "CITY"),
(8, 18, "STATE_FULL"),
(19, 24, "ZIPCODE"),
(25, 27, "STATE"),
(28, 44, "STREET_ADDRESS"),
]
}),
(
"California Burbank 91504 3676 Aviation Way CA"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 18, "CITY"),
(19, 24, "ZIPCODE"),
(25, 42, "STREET_ADDRESS"),
(43, 45, "STATE"),
]
}),
(
"CA California 91504 3676 Aviation Way Burbank"
, {
"entities":[
(0, 2, "STATE"),
(3, 13, "STATE_FULL"),
(14, 19, "ZIPCODE"),
(20, 37, "STREET_ADDRESS"),
(38, 45, "CITY"),
]
}),
(
"3676 Aviation Way CA 91504 California Burbank"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 20, "STATE"),
(21, 26, "ZIPCODE"),
(27, 37, "STATE_FULL"),
(38, 45, "CITY"),
]
}),
(
"91504 3676 Aviation Way Burbank California CA"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 23, "STREET_ADDRESS"),
(24, 31, "CITY"),
(32, 42, "STATE_FULL"),
(43, 45, "STATE"),
]
}),
(
"California CA Burbank 3676 Aviation Way 91504"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 13, "STATE"),
(14, 21, "CITY"),
(22, 39, "STREET_ADDRESS"),
(40, 45, "ZIPCODE"),
]
}),
(
"Burbank 91504 California 3676 Aviation Way CA"
, {
"entities":[
(0, 7, "CITY"),
(8, 13, "ZIPCODE"),
(14, 24, "STATE_FULL"),
(25, 42, "STREET_ADDRESS"),
(43, 45, "STATE"),
]
}),
(
"CA 91504 California Burbank 3676 Aviation Way"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 19, "STATE_FULL"),
(20, 27, "CITY"),
(28, 45, "STREET_ADDRESS"),
]
}),
(
"California Burbank 91504 CA 3676 Aviation Way"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 18, "CITY"),
(19, 24, "ZIPCODE"),
(25, 27, "STATE"),
(28, 45, "STREET_ADDRESS"),
]
}),
(
"California CA Burbank 91504 3676 Aviation Way"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 13, "STATE"),
(14, 21, "CITY"),
(22, 27, "ZIPCODE"),
(28, 45, "STREET_ADDRESS"),
]
}),
(
"California Burbank 3676 Aviation Way 91504 CA"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 18, "CITY"),
(19, 36, "STREET_ADDRESS"),
(37, 42, "ZIPCODE"),
(43, 45, "STATE"),
]
}),
(
"ND 58784 North Dakota 4274 Courtright Street Stanley"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 21, "STATE_FULL"),
(22, 44, "STREET_ADDRESS"),
(45, 52, "CITY"),
]
}),
(
"4274 Courtright Street ND Stanley 58784 North Dakota"
, {
"entities":[
(0, 22, "STREET_ADDRESS"),
(23, 25, "STATE"),
(26, 33, "CITY"),
(34, 39, "ZIPCODE"),
(40, 52, "STATE_FULL"),
]
}),
(
"4274 Courtright Street Stanley ND 58784 North Dakota"
, {
"entities":[
(0, 22, "STREET_ADDRESS"),
(23, 30, "CITY"),
(31, 33, "STATE"),
(34, 39, "ZIPCODE"),
(40, 52, "STATE_FULL"),
]
}),
(
"Stanley North Dakota ND 58784 4274 Courtright Street"
, {
"entities":[
(0, 7, "CITY"),
(8, 20, "STATE_FULL"),
(21, 23, "STATE"),
(24, 29, "ZIPCODE"),
(30, 52, "STREET_ADDRESS"),
]
}),
(
"Stanley North Dakota 4274 Courtright Street ND 58784"
, {
"entities":[
(0, 7, "CITY"),
(8, 20, "STATE_FULL"),
(21, 43, "STREET_ADDRESS"),
(44, 46, "STATE"),
(47, 52, "ZIPCODE"),
]
}),
(
"North Dakota 4274 Courtright Street ND Stanley 58784"
, {
"entities":[
(0, 12, "STATE_FULL"),
(13, 35, "STREET_ADDRESS"),
(36, 38, "STATE"),
(39, 46, "CITY"),
(47, 52, "ZIPCODE"),
]
}),
(
"4274 Courtright Street ND 58784 North Dakota Stanley"
, {
"entities":[
(0, 22, "STREET_ADDRESS"),
(23, 25, "STATE"),
(26, 31, "ZIPCODE"),
(32, 44, "STATE_FULL"),
(45, 52, "CITY"),
]
}),
(
"58784 North Dakota Stanley 4274 Courtright Street ND"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "STATE_FULL"),
(19, 26, "CITY"),
(27, 49, "STREET_ADDRESS"),
(50, 52, "STATE"),
]
}),
(
"North Dakota 4274 Courtright Street 58784 Stanley ND"
, {
"entities":[
(0, 12, "STATE_FULL"),
(13, 35, "STREET_ADDRESS"),
(36, 41, "ZIPCODE"),
(42, 49, "CITY"),
(50, 52, "STATE"),
]
}),
(
"4274 Courtright Street ND Stanley North Dakota 58784"
, {
"entities":[
(0, 22, "STREET_ADDRESS"),
(23, 25, "STATE"),
(26, 33, "CITY"),
(34, 46, "STATE_FULL"),
(47, 52, "ZIPCODE"),
]
}),
(
"MO 2171 Mandan Road Farmington Missouri 63640"
, {
"entities":[
(0, 2, "STATE"),
(3, 19, "STREET_ADDRESS"),
(20, 30, "CITY"),
(31, 39, "STATE_FULL"),
(40, 45, "ZIPCODE"),
]
}),
(
"MO 2171 Mandan Road Missouri 63640 Farmington"
, {
"entities":[
(0, 2, "STATE"),
(3, 19, "STREET_ADDRESS"),
(20, 28, "STATE_FULL"),
(29, 34, "ZIPCODE"),
(35, 45, "CITY"),
]
}),
(
"MO Missouri 2171 Mandan Road 63640 Farmington"
, {
"entities":[
(0, 2, "STATE"),
(3, 11, "STATE_FULL"),
(12, 28, "STREET_ADDRESS"),
(29, 34, "ZIPCODE"),
(35, 45, "CITY"),
]
}),
(
"Missouri 63640 MO 2171 Mandan Road Farmington"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 14, "ZIPCODE"),
(15, 17, "STATE"),
(18, 34, "STREET_ADDRESS"),
(35, 45, "CITY"),
]
}),
(
"63640 2171 Mandan Road Farmington MO Missouri"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 22, "STREET_ADDRESS"),
(23, 33, "CITY"),
(34, 36, "STATE"),
(37, 45, "STATE_FULL"),
]
}),
(
"Missouri 2171 Mandan Road MO Farmington 63640"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 25, "STREET_ADDRESS"),
(26, 28, "STATE"),
(29, 39, "CITY"),
(40, 45, "ZIPCODE"),
]
}),
(
"2171 Mandan Road 63640 MO Farmington Missouri"
, {
"entities":[
(0, 16, "STREET_ADDRESS"),
(17, 22, "ZIPCODE"),
(23, 25, "STATE"),
(26, 36, "CITY"),
(37, 45, "STATE_FULL"),
]
}),
(
"Farmington 2171 Mandan Road 63640 MO Missouri"
, {
"entities":[
(0, 10, "CITY"),
(11, 27, "STREET_ADDRESS"),
(28, 33, "ZIPCODE"),
(34, 36, "STATE"),
(37, 45, "STATE_FULL"),
]
}),
(
"Farmington MO 2171 Mandan Road 63640 Missouri"
, {
"entities":[
(0, 10, "CITY"),
(11, 13, "STATE"),
(14, 30, "STREET_ADDRESS"),
(31, 36, "ZIPCODE"),
(37, 45, "STATE_FULL"),
]
}),
(
"MO 63640 Missouri Farmington 2171 Mandan Road"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 17, "STATE_FULL"),
(18, 28, "CITY"),
(29, 45, "STREET_ADDRESS"),
]
}),
(
"Salinas 57 Emily Renzelli Boulevard 93901 information California CA"
, {
"entities":[
(0, 7, "CITY"),
(8, 35, "STREET_ADDRESS"),
(36, 41, "ZIPCODE"),
(54, 64, "STATE_FULL"),
(65, 67, "STATE"),
]
}),
(
"57 Emily Renzelli Boulevard 93901 information California Salinas CA"
, {
"entities":[
(0, 27, "STREET_ADDRESS"),
(28, 33, "ZIPCODE"),
(46, 56, "STATE_FULL"),
(57, 64, "CITY"),
(65, 67, "STATE"),
]
}),
(
"93901 57 Emily Renzelli Boulevard Salinas CA California information"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 33, "STREET_ADDRESS"),
(34, 41, "CITY"),
(42, 44, "STATE"),
(45, 55, "STATE_FULL"),
]
}),
(
"Salinas CA California 57 Emily Renzelli Boulevard 93901 information"
, {
"entities":[
(0, 7, "CITY"),
(8, 10, "STATE"),
(11, 21, "STATE_FULL"),
(22, 49, "STREET_ADDRESS"),
(50, 55, "ZIPCODE"),
]
}),
(
"93901 CA information 57 Emily Renzelli Boulevard California Salinas"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(21, 48, "STREET_ADDRESS"),
(49, 59, "STATE_FULL"),
(60, 67, "CITY"),
]
}),
(
"California information Salinas 57 Emily Renzelli Boulevard CA 93901"
, {
"entities":[
(0, 10, "STATE_FULL"),
(23, 30, "CITY"),
(31, 58, "STREET_ADDRESS"),
(59, 61, "STATE"),
(62, 67, "ZIPCODE"),
]
}),
(
"Salinas California 57 Emily Renzelli Boulevard 93901 CA information"
, {
"entities":[
(0, 7, "CITY"),
(8, 18, "STATE_FULL"),
(19, 46, "STREET_ADDRESS"),
(47, 52, "ZIPCODE"),
(53, 55, "STATE"),
]
}),
(
"Salinas California 57 Emily Renzelli Boulevard CA 93901 information"
, {
"entities":[
(0, 7, "CITY"),
(8, 18, "STATE_FULL"),
(19, 46, "STREET_ADDRESS"),
(47, 49, "STATE"),
(50, 55, "ZIPCODE"),
]
}),
(
"Salinas CA information California 57 Emily Renzelli Boulevard 93901"
, {
"entities":[
(0, 7, "CITY"),
(8, 10, "STATE"),
(23, 33, "STATE_FULL"),
(34, 61, "STREET_ADDRESS"),
(62, 67, "ZIPCODE"),
]
}),
(
"57 Emily Renzelli Boulevard CA 93901 California information Salinas"
, {
"entities":[
(0, 27, "STREET_ADDRESS"),
(28, 30, "STATE"),
(31, 36, "ZIPCODE"),
(37, 47, "STATE_FULL"),
(60, 67, "CITY"),
]
}),
(
"Connecticut 06002 CT Bloomfield 1501 Hart Street"
, {
"entities":[
(0, 11, "STATE_FULL"),
(12, 17, "ZIPCODE"),
(18, 20, "STATE"),
(21, 31, "CITY"),
(32, 48, "STREET_ADDRESS"),
]
}),
(
"CT 06002 1501 Hart Street Connecticut Bloomfield"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 25, "STREET_ADDRESS"),
(26, 37, "STATE_FULL"),
(38, 48, "CITY"),
]
}),
(
"Connecticut Bloomfield 1501 Hart Street 06002 CT"
, {
"entities":[
(0, 11, "STATE_FULL"),
(12, 22, "CITY"),
(23, 39, "STREET_ADDRESS"),
(40, 45, "ZIPCODE"),
(46, 48, "STATE"),
]
}),
(
"Bloomfield 1501 Hart Street 06002 Connecticut CT"
, {
"entities":[
(0, 10, "CITY"),
(11, 27, "STREET_ADDRESS"),
(28, 33, "ZIPCODE"),
(34, 45, "STATE_FULL"),
(46, 48, "STATE"),
]
}),
(
"1501 Hart Street CT Connecticut Bloomfield 06002"
, {
"entities":[
(0, 16, "STREET_ADDRESS"),
(17, 19, "STATE"),
(20, 31, "STATE_FULL"),
(32, 42, "CITY"),
(43, 48, "ZIPCODE"),
]
}),
(
"CT 06002 Bloomfield 1501 Hart Street Connecticut"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 19, "CITY"),
(20, 36, "STREET_ADDRESS"),
(37, 48, "STATE_FULL"),
]
}),
(
"1501 Hart Street Connecticut 06002 Bloomfield CT"
, {
"entities":[
(0, 16, "STREET_ADDRESS"),
(17, 28, "STATE_FULL"),
(29, 34, "ZIPCODE"),
(35, 45, "CITY"),
(46, 48, "STATE"),
]
}),
(
"Bloomfield 06002 CT 1501 Hart Street Connecticut"
, {
"entities":[
(0, 10, "CITY"),
(11, 16, "ZIPCODE"),
(17, 19, "STATE"),
(20, 36, "STREET_ADDRESS"),
(37, 48, "STATE_FULL"),
]
}),
(
"Connecticut CT Bloomfield 1501 Hart Street 06002"
, {
"entities":[
(0, 11, "STATE_FULL"),
(12, 14, "STATE"),
(15, 25, "CITY"),
(26, 42, "STREET_ADDRESS"),
(43, 48, "ZIPCODE"),
]
}),
(
"Connecticut Bloomfield CT 06002 1501 Hart Street"
, {
"entities":[
(0, 11, "STATE_FULL"),
(12, 22, "CITY"),
(23, 25, "STATE"),
(26, 31, "ZIPCODE"),
(32, 48, "STREET_ADDRESS"),
]
}),
(
"Seymour 1259 Bernardo Street IN 47274 Indiana"
, {
"entities":[
(0, 7, "CITY"),
(8, 28, "STREET_ADDRESS"),
(29, 31, "STATE"),
(32, 37, "ZIPCODE"),
(38, 45, "STATE_FULL"),
]
}),
(
"Seymour IN 47274 Indiana 1259 Bernardo Street"
, {
"entities":[
(0, 7, "CITY"),
(8, 10, "STATE"),
(11, 16, "ZIPCODE"),
(17, 24, "STATE_FULL"),
(25, 45, "STREET_ADDRESS"),
]
}),
(
"IN 47274 Seymour 1259 Bernardo Street Indiana"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 16, "CITY"),
(17, 37, "STREET_ADDRESS"),
(38, 45, "STATE_FULL"),
]
}),
(
"IN 1259 Bernardo Street Seymour Indiana 47274"
, {
"entities":[
(0, 2, "STATE"),
(3, 23, "STREET_ADDRESS"),
(24, 31, "CITY"),
(32, 39, "STATE_FULL"),
(40, 45, "ZIPCODE"),
]
}),
(
"IN Indiana 47274 Seymour 1259 Bernardo Street"
, {
"entities":[
(0, 2, "STATE"),
(3, 10, "STATE_FULL"),
(11, 16, "ZIPCODE"),
(17, 24, "CITY"),
(25, 45, "STREET_ADDRESS"),
]
}),
(
"1259 Bernardo Street Seymour 47274 IN Indiana"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 28, "CITY"),
(29, 34, "ZIPCODE"),
(35, 37, "STATE"),
(38, 45, "STATE_FULL"),
]
}),
(
"IN 47274 1259 Bernardo Street Seymour Indiana"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 29, "STREET_ADDRESS"),
(30, 37, "CITY"),
(38, 45, "STATE_FULL"),
]
}),
(
"1259 Bernardo Street 47274 Indiana IN Seymour"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 26, "ZIPCODE"),
(27, 34, "STATE_FULL"),
(35, 37, "STATE"),
(38, 45, "CITY"),
]
}),
(
"1259 Bernardo Street Indiana Seymour 47274 IN"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 28, "STATE_FULL"),
(29, 36, "CITY"),
(37, 42, "ZIPCODE"),
(43, 45, "STATE"),
]
}),
(
"IN Indiana 1259 Bernardo Street 47274 Seymour"
, {
"entities":[
(0, 2, "STATE"),
(3, 10, "STATE_FULL"),
(11, 31, "STREET_ADDRESS"),
(32, 37, "ZIPCODE"),
(38, 45, "CITY"),
]
}),
(
"15212 PA Pennsylvania 2716 Beechwood Drive Pittsburgh"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 21, "STATE_FULL"),
(22, 42, "STREET_ADDRESS"),
(43, 53, "CITY"),
]
}),
(
"PA Pennsylvania 2716 Beechwood Drive Pittsburgh 15212"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "STATE_FULL"),
(16, 36, "STREET_ADDRESS"),
(37, 47, "CITY"),
(48, 53, "ZIPCODE"),
]
}),
(
"2716 Beechwood Drive 15212 Pennsylvania Pittsburgh PA"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 26, "ZIPCODE"),
(27, 39, "STATE_FULL"),
(40, 50, "CITY"),
(51, 53, "STATE"),
]
}),
(
"2716 Beechwood Drive PA 15212 Pennsylvania Pittsburgh"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 23, "STATE"),
(24, 29, "ZIPCODE"),
(30, 42, "STATE_FULL"),
(43, 53, "CITY"),
]
}),
(
"15212 Pennsylvania 2716 Beechwood Drive PA Pittsburgh"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "STATE_FULL"),
(19, 39, "STREET_ADDRESS"),
(40, 42, "STATE"),
(43, 53, "CITY"),
]
}),
(
"15212 PA 2716 Beechwood Drive Pennsylvania Pittsburgh"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 29, "STREET_ADDRESS"),
(30, 42, "STATE_FULL"),
(43, 53, "CITY"),
]
}),
(
"2716 Beechwood Drive Pennsylvania PA Pittsburgh 15212"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 33, "STATE_FULL"),
(34, 36, "STATE"),
(37, 47, "CITY"),
(48, 53, "ZIPCODE"),
]
}),
(
"2716 Beechwood Drive Pennsylvania 15212 Pittsburgh PA"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 33, "STATE_FULL"),
(34, 39, "ZIPCODE"),
(40, 50, "CITY"),
(51, 53, "STATE"),
]
}),
(
"Pittsburgh PA 15212 2716 Beechwood Drive Pennsylvania"
, {
"entities":[
(0, 10, "CITY"),
(11, 13, "STATE"),
(14, 19, "ZIPCODE"),
(20, 40, "STREET_ADDRESS"),
(41, 53, "STATE_FULL"),
]
}),
(
"Pittsburgh 15212 PA Pennsylvania 2716 Beechwood Drive"
, {
"entities":[
(0, 10, "CITY"),
(11, 16, "ZIPCODE"),
(17, 19, "STATE"),
(20, 32, "STATE_FULL"),
(33, 53, "STREET_ADDRESS"),
]
}),
(
"North Carolina NC 28352 of 620 Ray Court Laurinburg"
, {
"entities":[
(0, 14, "STATE_FULL"),
(15, 17, "STATE"),
(18, 23, "ZIPCODE"),
(27, 40, "STREET_ADDRESS"),
(41, 51, "CITY"),
]
}),
(
"of Laurinburg 620 Ray Court NC North Carolina 28352"
, {
"entities":[
(3, 13, "CITY"),
(14, 27, "STREET_ADDRESS"),
(28, 30, "STATE"),
(31, 45, "STATE_FULL"),
(46, 51, "ZIPCODE"),
]
}),
(
"of Laurinburg NC North Carolina 28352 620 Ray Court"
, {
"entities":[
(3, 13, "CITY"),
(14, 16, "STATE"),
(17, 31, "STATE_FULL"),
(32, 37, "ZIPCODE"),
(38, 51, "STREET_ADDRESS"),
]
}),
(
"620 Ray Court of NC Laurinburg North Carolina 28352"
, {
"entities":[
(0, 13, "STREET_ADDRESS"),
(17, 19, "STATE"),
(20, 30, "CITY"),
(31, 45, "STATE_FULL"),
(46, 51, "ZIPCODE"),
]
}),
(
"North Carolina of Laurinburg 28352 NC 620 Ray Court"
, {
"entities":[
(0, 14, "STATE_FULL"),
(18, 28, "CITY"),
(29, 34, "ZIPCODE"),
(35, 37, "STATE"),
(38, 51, "STREET_ADDRESS"),
]
}),
(
"620 Ray Court Laurinburg NC of North Carolina 28352"
, {
"entities":[
(0, 13, "STREET_ADDRESS"),
(14, 24, "CITY"),
(25, 27, "STATE"),
(31, 45, "STATE_FULL"),
(46, 51, "ZIPCODE"),
]
}),
(
"28352 620 Ray Court of Laurinburg NC North Carolina"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 19, "STREET_ADDRESS"),
(23, 33, "CITY"),
(34, 36, "STATE"),
(37, 51, "STATE_FULL"),
]
}),
(
"620 Ray Court NC North Carolina 28352 Laurinburg of"
, {
"entities":[
(0, 13, "STREET_ADDRESS"),
(14, 16, "STATE"),
(17, 31, "STATE_FULL"),
(32, 37, "ZIPCODE"),
(38, 48, "CITY"),
]
}),
(
"Laurinburg 28352 North Carolina NC 620 Ray Court of"
, {
"entities":[
(0, 10, "CITY"),
(11, 16, "ZIPCODE"),
(17, 31, "STATE_FULL"),
(32, 34, "STATE"),
(35, 48, "STREET_ADDRESS"),
]
}),
(
"of Laurinburg North Carolina NC 620 Ray Court 28352"
, {
"entities":[
(3, 13, "CITY"),
(14, 28, "STATE_FULL"),
(29, 31, "STATE"),
(32, 45, "STREET_ADDRESS"),
(46, 51, "ZIPCODE"),
]
}),
(
"Chicago IL Illinois 60637 366 Farland Street"
, {
"entities":[
(0, 7, "CITY"),
(8, 10, "STATE"),
(11, 19, "STATE_FULL"),
(20, 25, "ZIPCODE"),
(26, 44, "STREET_ADDRESS"),
]
}),
(
"Illinois IL 60637 Chicago 366 Farland Street"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 11, "STATE"),
(12, 17, "ZIPCODE"),
(18, 25, "CITY"),
(26, 44, "STREET_ADDRESS"),
]
}),
(
"Chicago Illinois 60637 IL 366 Farland Street"
, {
"entities":[
(0, 7, "CITY"),
(8, 16, "STATE_FULL"),
(17, 22, "ZIPCODE"),
(23, 25, "STATE"),
(26, 44, "STREET_ADDRESS"),
]
}),
(
"60637 Chicago IL 366 Farland Street Illinois"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 13, "CITY"),
(14, 16, "STATE"),
(17, 35, "STREET_ADDRESS"),
(36, 44, "STATE_FULL"),
]
}),
(
"366 Farland Street IL Chicago 60637 Illinois"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 21, "STATE"),
(22, 29, "CITY"),
(30, 35, "ZIPCODE"),
(36, 44, "STATE_FULL"),
]
}),
(
"366 Farland Street IL 60637 Chicago Illinois"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 21, "STATE"),
(22, 27, "ZIPCODE"),
(28, 35, "CITY"),
(36, 44, "STATE_FULL"),
]
}),
(
"60637 Chicago IL 366 Farland Street Illinois"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 13, "CITY"),
(14, 16, "STATE"),
(17, 35, "STREET_ADDRESS"),
(36, 44, "STATE_FULL"),
]
}),
(
"IL Illinois 60637 366 Farland Street Chicago"
, {
"entities":[
(0, 2, "STATE"),
(3, 11, "STATE_FULL"),
(12, 17, "ZIPCODE"),
(18, 36, "STREET_ADDRESS"),
(37, 44, "CITY"),
]
}),
(
"IL 60637 Chicago Illinois 366 Farland Street"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 16, "CITY"),
(17, 25, "STATE_FULL"),
(26, 44, "STREET_ADDRESS"),
]
}),
(
"Chicago IL 60637 Illinois 366 Farland Street"
, {
"entities":[
(0, 7, "CITY"),
(8, 10, "STATE"),
(11, 16, "ZIPCODE"),
(17, 25, "STATE_FULL"),
(26, 44, "STREET_ADDRESS"),
]
}),
(
"with 4083 Coulter Lane VA Richmond 23219 Virginia"
, {
"entities":[
(5, 22, "STREET_ADDRESS"),
(23, 25, "STATE"),
(26, 34, "CITY"),
(35, 40, "ZIPCODE"),
(41, 49, "STATE_FULL"),
]
}),
(
"Richmond Virginia 23219 VA 4083 Coulter Lane with"
, {
"entities":[
(0, 8, "CITY"),
(9, 17, "STATE_FULL"),
(18, 23, "ZIPCODE"),
(24, 26, "STATE"),
(27, 44, "STREET_ADDRESS"),
]
}),
(
"VA Richmond with 23219 4083 Coulter Lane Virginia"
, {
"entities":[
(0, 2, "STATE"),
(3, 11, "CITY"),
(17, 22, "ZIPCODE"),
(23, 40, "STREET_ADDRESS"),
(41, 49, "STATE_FULL"),
]
}),
(
"Virginia VA 23219 4083 Coulter Lane with Richmond"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 11, "STATE"),
(12, 17, "ZIPCODE"),
(18, 35, "STREET_ADDRESS"),
(41, 49, "CITY"),
]
}),
(
"VA 4083 Coulter Lane with 23219 Richmond Virginia"
, {
"entities":[
(0, 2, "STATE"),
(3, 20, "STREET_ADDRESS"),
(26, 31, "ZIPCODE"),
(32, 40, "CITY"),
(41, 49, "STATE_FULL"),
]
}),
(
"VA Richmond with Virginia 23219 4083 Coulter Lane"
, {
"entities":[
(0, 2, "STATE"),
(3, 11, "CITY"),
(17, 25, "STATE_FULL"),
(26, 31, "ZIPCODE"),
(32, 49, "STREET_ADDRESS"),
]
}),
(
"with Richmond 23219 Virginia 4083 Coulter Lane VA"
, {
"entities":[
(5, 13, "CITY"),
(14, 19, "ZIPCODE"),
(20, 28, "STATE_FULL"),
(29, 46, "STREET_ADDRESS"),
(47, 49, "STATE"),
]
}),
(
"4083 Coulter Lane 23219 with VA Virginia Richmond"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 23, "ZIPCODE"),
(29, 31, "STATE"),
(32, 40, "STATE_FULL"),
(41, 49, "CITY"),
]
}),
(
"with Richmond Virginia VA 4083 Coulter Lane 23219"
, {
"entities":[
(5, 13, "CITY"),
(14, 22, "STATE_FULL"),
(23, 25, "STATE"),
(26, 43, "STREET_ADDRESS"),
(44, 49, "ZIPCODE"),
]
}),
(
"VA with 23219 Virginia 4083 Coulter Lane Richmond"
, {
"entities":[
(0, 2, "STATE"),
(8, 13, "ZIPCODE"),
(14, 22, "STATE_FULL"),
(23, 40, "STREET_ADDRESS"),
(41, 49, "CITY"),
]
}),
(
"63108 MO Saint Louis 1482 Cottrill Lane Missouri"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 20, "CITY"),
(21, 39, "STREET_ADDRESS"),
(40, 48, "STATE_FULL"),
]
}),
(
"Saint Louis MO Missouri 1482 Cottrill Lane 63108"
, {
"entities":[
(0, 11, "CITY"),
(12, 14, "STATE"),
(15, 23, "STATE_FULL"),
(24, 42, "STREET_ADDRESS"),
(43, 48, "ZIPCODE"),
]
}),
(
"Missouri 63108 Saint Louis MO 1482 Cottrill Lane"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 14, "ZIPCODE"),
(15, 26, "CITY"),
(27, 29, "STATE"),
(30, 48, "STREET_ADDRESS"),
]
}),
(
"MO 1482 Cottrill Lane Missouri Saint Louis 63108"
, {
"entities":[
(0, 2, "STATE"),
(3, 21, "STREET_ADDRESS"),
(22, 30, "STATE_FULL"),
(31, 42, "CITY"),
(43, 48, "ZIPCODE"),
]
}),
(
"1482 Cottrill Lane Saint Louis 63108 Missouri MO"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 30, "CITY"),
(31, 36, "ZIPCODE"),
(37, 45, "STATE_FULL"),
(46, 48, "STATE"),
]
}),
(
"Missouri MO 1482 Cottrill Lane Saint Louis 63108"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 11, "STATE"),
(12, 30, "STREET_ADDRESS"),
(31, 42, "CITY"),
(43, 48, "ZIPCODE"),
]
}),
(
"63108 Missouri Saint Louis 1482 Cottrill Lane MO"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 14, "STATE_FULL"),
(15, 26, "CITY"),
(27, 45, "STREET_ADDRESS"),
(46, 48, "STATE"),
]
}),
(
"Saint Louis Missouri 63108 1482 Cottrill Lane MO"
, {
"entities":[
(0, 11, "CITY"),
(12, 20, "STATE_FULL"),
(21, 26, "ZIPCODE"),
(27, 45, "STREET_ADDRESS"),
(46, 48, "STATE"),
]
}),
(
"Saint Louis Missouri 63108 MO 1482 Cottrill Lane"
, {
"entities":[
(0, 11, "CITY"),
(12, 20, "STATE_FULL"),
(21, 26, "ZIPCODE"),
(27, 29, "STATE"),
(30, 48, "STREET_ADDRESS"),
]
}),
(
"MO 63108 Saint Louis Missouri 1482 Cottrill Lane"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 20, "CITY"),
(21, 29, "STATE_FULL"),
(30, 48, "STREET_ADDRESS"),
]
}),
(
"2613 Luke Lane Idabel OK 74745 Oklahoma"
, {
"entities":[
(0, 14, "STREET_ADDRESS"),
(15, 21, "CITY"),
(22, 24, "STATE"),
(25, 30, "ZIPCODE"),
(31, 39, "STATE_FULL"),
]
}),
(
"Oklahoma OK Idabel 2613 Luke Lane 74745"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 11, "STATE"),
(12, 18, "CITY"),
(19, 33, "STREET_ADDRESS"),
(34, 39, "ZIPCODE"),
]
}),
(
"Oklahoma 74745 Idabel OK 2613 Luke Lane"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 14, "ZIPCODE"),
(15, 21, "CITY"),
(22, 24, "STATE"),
(25, 39, "STREET_ADDRESS"),
]
}),
(
"Oklahoma OK Idabel 74745 2613 Luke Lane"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 11, "STATE"),
(12, 18, "CITY"),
(19, 24, "ZIPCODE"),
(25, 39, "STREET_ADDRESS"),
]
}),
(
"74745 Idabel OK Oklahoma 2613 Luke Lane"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 12, "CITY"),
(13, 15, "STATE"),
(16, 24, "STATE_FULL"),
(25, 39, "STREET_ADDRESS"),
]
}),
(
"Oklahoma 74745 2613 Luke Lane Idabel OK"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 14, "ZIPCODE"),
(15, 29, "STREET_ADDRESS"),
(30, 36, "CITY"),
(37, 39, "STATE"),
]
}),
(
"Oklahoma OK Idabel 74745 2613 Luke Lane"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 11, "STATE"),
(12, 18, "CITY"),
(19, 24, "ZIPCODE"),
(25, 39, "STREET_ADDRESS"),
]
}),
(
"OK 74745 Oklahoma Idabel 2613 Luke Lane"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 17, "STATE_FULL"),
(18, 24, "CITY"),
(25, 39, "STREET_ADDRESS"),
]
}),
(
"74745 OK Idabel 2613 Luke Lane Oklahoma"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 15, "CITY"),
(16, 30, "STREET_ADDRESS"),
(31, 39, "STATE_FULL"),
]
}),
(
"74745 OK Idabel Oklahoma 2613 Luke Lane"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 15, "CITY"),
(16, 24, "STATE_FULL"),
(25, 39, "STREET_ADDRESS"),
]
}),
(
"Mississippi 38914 479 School House Road Big Creek MS"
, {
"entities":[
(0, 11, "STATE_FULL"),
(12, 17, "ZIPCODE"),
(18, 39, "STREET_ADDRESS"),
(40, 49, "CITY"),
(50, 52, "STATE"),
]
}),
(
"Mississippi 38914 Big Creek 479 School House Road MS"
, {
"entities":[
(0, 11, "STATE_FULL"),
(12, 17, "ZIPCODE"),
(18, 27, "CITY"),
(28, 49, "STREET_ADDRESS"),
(50, 52, "STATE"),
]
}),
(
"MS 38914 Mississippi 479 School House Road Big Creek"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 20, "STATE_FULL"),
(21, 42, "STREET_ADDRESS"),
(43, 52, "CITY"),
]
}),
(
"MS Big Creek 479 School House Road 38914 Mississippi"
, {
"entities":[
(0, 2, "STATE"),
(3, 12, "CITY"),
(13, 34, "STREET_ADDRESS"),
(35, 40, "ZIPCODE"),
(41, 52, "STATE_FULL"),
]
}),
(
"MS Mississippi Big Creek 479 School House Road 38914"
, {
"entities":[
(0, 2, "STATE"),
(3, 14, "STATE_FULL"),
(15, 24, "CITY"),
(25, 46, "STREET_ADDRESS"),
(47, 52, "ZIPCODE"),
]
}),
(
"MS Big Creek Mississippi 479 School House Road 38914"
, {
"entities":[
(0, 2, "STATE"),
(3, 12, "CITY"),
(13, 24, "STATE_FULL"),
(25, 46, "STREET_ADDRESS"),
(47, 52, "ZIPCODE"),
]
}),
(
"38914 479 School House Road MS Mississippi Big Creek"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 27, "STREET_ADDRESS"),
(28, 30, "STATE"),
(31, 42, "STATE_FULL"),
(43, 52, "CITY"),
]
}),
(
"Mississippi 38914 Big Creek MS 479 School House Road"
, {
"entities":[
(0, 11, "STATE_FULL"),
(12, 17, "ZIPCODE"),
(18, 27, "CITY"),
(28, 30, "STATE"),
(31, 52, "STREET_ADDRESS"),
]
}),
(
"Big Creek 479 School House Road MS 38914 Mississippi"
, {
"entities":[
(0, 9, "CITY"),
(10, 31, "STREET_ADDRESS"),
(32, 34, "STATE"),
(35, 40, "ZIPCODE"),
(41, 52, "STATE_FULL"),
]
}),
(
"479 School House Road Big Creek Mississippi MS 38914"
, {
"entities":[
(0, 21, "STREET_ADDRESS"),
(22, 31, "CITY"),
(32, 43, "STATE_FULL"),
(44, 46, "STATE"),
(47, 52, "ZIPCODE"),
]
}),
(
"Rogersville TN 2425 Nixon Avenue Phone Tennessee 37856"
, {
"entities":[
(0, 11, "CITY"),
(12, 14, "STATE"),
(15, 32, "STREET_ADDRESS"),
(39, 48, "STATE_FULL"),
(49, 54, "ZIPCODE"),
]
}),
(
"TN 37856 Phone Rogersville 2425 Nixon Avenue Tennessee"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(15, 26, "CITY"),
(27, 44, "STREET_ADDRESS"),
(45, 54, "STATE_FULL"),
]
}),
(
"Rogersville Phone 37856 2425 Nixon Avenue Tennessee TN"
, {
"entities":[
(0, 11, "CITY"),
(18, 23, "ZIPCODE"),
(24, 41, "STREET_ADDRESS"),
(42, 51, "STATE_FULL"),
(52, 54, "STATE"),
]
}),
(
"TN Rogersville Phone 2425 Nixon Avenue 37856 Tennessee"
, {
"entities":[
(0, 2, "STATE"),
(3, 14, "CITY"),
(21, 38, "STREET_ADDRESS"),
(39, 44, "ZIPCODE"),
(45, 54, "STATE_FULL"),
]
}),
(
"2425 Nixon Avenue Tennessee TN Phone Rogersville 37856"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 27, "STATE_FULL"),
(28, 30, "STATE"),
(37, 48, "CITY"),
(49, 54, "ZIPCODE"),
]
}),
(
"37856 2425 Nixon Avenue Rogersville TN Tennessee Phone"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 23, "STREET_ADDRESS"),
(24, 35, "CITY"),
(36, 38, "STATE"),
(39, 48, "STATE_FULL"),
]
}),
(
"Tennessee TN 37856 Phone 2425 Nixon Avenue Rogersville"
, {
"entities":[
(0, 9, "STATE_FULL"),
(10, 12, "STATE"),
(13, 18, "ZIPCODE"),
(25, 42, "STREET_ADDRESS"),
(43, 54, "CITY"),
]
}),
(
"Rogersville 37856 TN 2425 Nixon Avenue Tennessee Phone"
, {
"entities":[
(0, 11, "CITY"),
(12, 17, "ZIPCODE"),
(18, 20, "STATE"),
(21, 38, "STREET_ADDRESS"),
(39, 48, "STATE_FULL"),
]
}),
(
"Tennessee Phone TN 2425 Nixon Avenue Rogersville 37856"
, {
"entities":[
(0, 9, "STATE_FULL"),
(16, 18, "STATE"),
(19, 36, "STREET_ADDRESS"),
(37, 48, "CITY"),
(49, 54, "ZIPCODE"),
]
}),
(
"2425 Nixon Avenue Rogersville 37856 Phone TN Tennessee"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 29, "CITY"),
(30, 35, "ZIPCODE"),
(42, 44, "STATE"),
(45, 54, "STATE_FULL"),
]
}),
(
"98204 We WA Everett 1626 Conifer Drive Washington"
, {
"entities":[
(0, 5, "ZIPCODE"),
(9, 11, "STATE"),
(12, 19, "CITY"),
(20, 38, "STREET_ADDRESS"),
(39, 49, "STATE_FULL"),
]
}),
(
"WA 1626 Conifer Drive Washington 98204 We Everett"
, {
"entities":[
(0, 2, "STATE"),
(3, 21, "STREET_ADDRESS"),
(22, 32, "STATE_FULL"),
(33, 38, "ZIPCODE"),
(42, 49, "CITY"),
]
}),
(
"98204 We WA 1626 Conifer Drive Washington Everett"
, {
"entities":[
(0, 5, "ZIPCODE"),
(9, 11, "STATE"),
(12, 30, "STREET_ADDRESS"),
(31, 41, "STATE_FULL"),
(42, 49, "CITY"),
]
}),
(
"1626 Conifer Drive Washington Everett 98204 We WA"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 29, "STATE_FULL"),
(30, 37, "CITY"),
(38, 43, "ZIPCODE"),
(47, 49, "STATE"),
]
}),
(
"Everett WA We 98204 1626 Conifer Drive Washington"
, {
"entities":[
(0, 7, "CITY"),
(8, 10, "STATE"),
(14, 19, "ZIPCODE"),
(20, 38, "STREET_ADDRESS"),
(39, 49, "STATE_FULL"),
]
}),
(
"1626 Conifer Drive We Washington 98204 WA Everett"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(22, 32, "STATE_FULL"),
(33, 38, "ZIPCODE"),
(39, 41, "STATE"),
(42, 49, "CITY"),
]
}),
(
"1626 Conifer Drive We Washington WA 98204 Everett"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(22, 32, "STATE_FULL"),
(33, 35, "STATE"),
(36, 41, "ZIPCODE"),
(42, 49, "CITY"),
]
}),
(
"1626 Conifer Drive Washington Everett WA 98204 We"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 29, "STATE_FULL"),
(30, 37, "CITY"),
(38, 40, "STATE"),
(41, 46, "ZIPCODE"),
]
}),
(
"Everett 1626 Conifer Drive We 98204 WA Washington"
, {
"entities":[
(0, 7, "CITY"),
(8, 26, "STREET_ADDRESS"),
(30, 35, "ZIPCODE"),
(36, 38, "STATE"),
(39, 49, "STATE_FULL"),
]
}),
(
"Washington 1626 Conifer Drive Everett We 98204 WA"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 29, "STREET_ADDRESS"),
(30, 37, "CITY"),
(41, 46, "ZIPCODE"),
(47, 49, "STATE"),
]
}),
(
"95814 CA 3236 Park Avenue California Sacramento"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 25, "STREET_ADDRESS"),
(26, 36, "STATE_FULL"),
(37, 47, "CITY"),
]
}),
(
"Sacramento 3236 Park Avenue 95814 CA California"
, {
"entities":[
(0, 10, "CITY"),
(11, 27, "STREET_ADDRESS"),
(28, 33, "ZIPCODE"),
(34, 36, "STATE"),
(37, 47, "STATE_FULL"),
]
}),
(
"California CA Sacramento 3236 Park Avenue 95814"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 13, "STATE"),
(14, 24, "CITY"),
(25, 41, "STREET_ADDRESS"),
(42, 47, "ZIPCODE"),
]
}),
(
"California Sacramento CA 3236 Park Avenue 95814"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 21, "CITY"),
(22, 24, "STATE"),
(25, 41, "STREET_ADDRESS"),
(42, 47, "ZIPCODE"),
]
}),
(
"CA Sacramento California 95814 3236 Park Avenue"
, {
"entities":[
(0, 2, "STATE"),
(3, 13, "CITY"),
(14, 24, "STATE_FULL"),
(25, 30, "ZIPCODE"),
(31, 47, "STREET_ADDRESS"),
]
}),
(
"Sacramento CA 95814 3236 Park Avenue California"
, {
"entities":[
(0, 10, "CITY"),
(11, 13, "STATE"),
(14, 19, "ZIPCODE"),
(20, 36, "STREET_ADDRESS"),
(37, 47, "STATE_FULL"),
]
}),
(
"CA 95814 Sacramento 3236 Park Avenue California"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 19, "CITY"),
(20, 36, "STREET_ADDRESS"),
(37, 47, "STATE_FULL"),
]
}),
(
"California CA 95814 Sacramento 3236 Park Avenue"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 13, "STATE"),
(14, 19, "ZIPCODE"),
(20, 30, "CITY"),
(31, 47, "STREET_ADDRESS"),
]
}),
(
"Sacramento CA California 95814 3236 Park Avenue"
, {
"entities":[
(0, 10, "CITY"),
(11, 13, "STATE"),
(14, 24, "STATE_FULL"),
(25, 30, "ZIPCODE"),
(31, 47, "STREET_ADDRESS"),
]
}),
(
"95814 Sacramento 3236 Park Avenue CA California"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 16, "CITY"),
(17, 33, "STREET_ADDRESS"),
(34, 36, "STATE"),
(37, 47, "STATE_FULL"),
]
}),
(
"1630 Arlington Avenue Tennessee 37849 Claxton TN on"
, {
"entities":[
(0, 21, "STREET_ADDRESS"),
(22, 31, "STATE_FULL"),
(32, 37, "ZIPCODE"),
(38, 45, "CITY"),
(46, 48, "STATE"),
]
}),
(
"37849 Tennessee 1630 Arlington Avenue TN Claxton on"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 15, "STATE_FULL"),
(16, 37, "STREET_ADDRESS"),
(38, 40, "STATE"),
(41, 48, "CITY"),
]
}),
(
"37849 TN Tennessee Claxton on 1630 Arlington Avenue"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 18, "STATE_FULL"),
(19, 26, "CITY"),
(30, 51, "STREET_ADDRESS"),
]
}),
(
"TN 1630 Arlington Avenue on Tennessee Claxton 37849"
, {
"entities":[
(0, 2, "STATE"),
(3, 24, "STREET_ADDRESS"),
(28, 37, "STATE_FULL"),
(38, 45, "CITY"),
(46, 51, "ZIPCODE"),
]
}),
(
"37849 on 1630 Arlington Avenue TN Tennessee Claxton"
, {
"entities":[
(0, 5, "ZIPCODE"),
(9, 30, "STREET_ADDRESS"),
(31, 33, "STATE"),
(34, 43, "STATE_FULL"),
(44, 51, "CITY"),
]
}),
(
"37849 1630 Arlington Avenue Claxton Tennessee TN on"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 27, "STREET_ADDRESS"),
(28, 35, "CITY"),
(36, 45, "STATE_FULL"),
(46, 48, "STATE"),
]
}),
(
"37849 on Tennessee TN 1630 Arlington Avenue Claxton"
, {
"entities":[
(0, 5, "ZIPCODE"),
(9, 18, "STATE_FULL"),
(19, 21, "STATE"),
(22, 43, "STREET_ADDRESS"),
(44, 51, "CITY"),
]
}),
(
"Claxton 37849 1630 Arlington Avenue Tennessee TN on"
, {
"entities":[
(0, 7, "CITY"),
(8, 13, "ZIPCODE"),
(14, 35, "STREET_ADDRESS"),
(36, 45, "STATE_FULL"),
(46, 48, "STATE"),
]
}),
(
"on TN 1630 Arlington Avenue Claxton 37849 Tennessee"
, {
"entities":[
(3, 5, "STATE"),
(6, 27, "STREET_ADDRESS"),
(28, 35, "CITY"),
(36, 41, "ZIPCODE"),
(42, 51, "STATE_FULL"),
]
}),
(
"37849 Claxton TN on Tennessee 1630 Arlington Avenue"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 13, "CITY"),
(14, 16, "STATE"),
(20, 29, "STATE_FULL"),
(30, 51, "STREET_ADDRESS"),
]
}),
(
"4378 Wilson Street San Diego 92103 California CA estimate"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 28, "CITY"),
(29, 34, "ZIPCODE"),
(35, 45, "STATE_FULL"),
(46, 48, "STATE"),
]
}),
(
"4378 Wilson Street 92103 estimate California San Diego CA"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 24, "ZIPCODE"),
(34, 44, "STATE_FULL"),
(45, 54, "CITY"),
(55, 57, "STATE"),
]
}),
(
"92103 California CA estimate San Diego 4378 Wilson Street"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 16, "STATE_FULL"),
(17, 19, "STATE"),
(29, 38, "CITY"),
(39, 57, "STREET_ADDRESS"),
]
}),
(
"4378 Wilson Street San Diego 92103 CA California estimate"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 28, "CITY"),
(29, 34, "ZIPCODE"),
(35, 37, "STATE"),
(38, 48, "STATE_FULL"),
]
}),
(
"estimate San Diego 4378 Wilson Street 92103 California CA"
, {
"entities":[
(9, 18, "CITY"),
(19, 37, "STREET_ADDRESS"),
(38, 43, "ZIPCODE"),
(44, 54, "STATE_FULL"),
(55, 57, "STATE"),
]
}),
(
"92103 4378 Wilson Street San Diego CA estimate California"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 24, "STREET_ADDRESS"),
(25, 34, "CITY"),
(35, 37, "STATE"),
(47, 57, "STATE_FULL"),
]
}),
(
"San Diego 4378 Wilson Street 92103 CA California estimate"
, {
"entities":[
(0, 9, "CITY"),
(10, 28, "STREET_ADDRESS"),
(29, 34, "ZIPCODE"),
(35, 37, "STATE"),
(38, 48, "STATE_FULL"),
]
}),
(
"estimate CA 4378 Wilson Street California San Diego 92103"
, {
"entities":[
(9, 11, "STATE"),
(12, 30, "STREET_ADDRESS"),
(31, 41, "STATE_FULL"),
(42, 51, "CITY"),
(52, 57, "ZIPCODE"),
]
}),
(
"estimate 4378 Wilson Street San Diego 92103 CA California"
, {
"entities":[
(9, 27, "STREET_ADDRESS"),
(28, 37, "CITY"),
(38, 43, "ZIPCODE"),
(44, 46, "STATE"),
(47, 57, "STATE_FULL"),
]
}),
(
"California 4378 Wilson Street estimate CA San Diego 92103"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 29, "STREET_ADDRESS"),
(39, 41, "STATE"),
(42, 51, "CITY"),
(52, 57, "ZIPCODE"),
]
}),
(
"North Greenbush 12144 New York NY 845 Golden Ridge Road"
, {
"entities":[
(0, 15, "CITY"),
(16, 21, "ZIPCODE"),
(22, 30, "STATE_FULL"),
(31, 33, "STATE"),
(34, 55, "STREET_ADDRESS"),
]
}),
(
"NY New York North Greenbush 12144 845 Golden Ridge Road"
, {
"entities":[
(0, 2, "STATE"),
(3, 11, "STATE_FULL"),
(12, 27, "CITY"),
(28, 33, "ZIPCODE"),
(34, 55, "STREET_ADDRESS"),
]
}),
(
"12144 New York NY 845 Golden Ridge Road North Greenbush"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 14, "STATE_FULL"),
(15, 17, "STATE"),
(18, 39, "STREET_ADDRESS"),
(40, 55, "CITY"),
]
}),
(
"New York 12144 845 Golden Ridge Road North Greenbush NY"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 14, "ZIPCODE"),
(15, 36, "STREET_ADDRESS"),
(37, 52, "CITY"),
(53, 55, "STATE"),
]
}),
(
"12144 845 Golden Ridge Road New York NY North Greenbush"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 27, "STREET_ADDRESS"),
(28, 36, "STATE_FULL"),
(37, 39, "STATE"),
(40, 55, "CITY"),
]
}),
(
"845 Golden Ridge Road NY New York North Greenbush 12144"
, {
"entities":[
(0, 21, "STREET_ADDRESS"),
(22, 24, "STATE"),
(25, 33, "STATE_FULL"),
(34, 49, "CITY"),
(50, 55, "ZIPCODE"),
]
}),
(
"North Greenbush New York 12144 NY 845 Golden Ridge Road"
, {
"entities":[
(0, 15, "CITY"),
(16, 24, "STATE_FULL"),
(25, 30, "ZIPCODE"),
(31, 33, "STATE"),
(34, 55, "STREET_ADDRESS"),
]
}),
(
"New York North Greenbush NY 845 Golden Ridge Road 12144"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 24, "CITY"),
(25, 27, "STATE"),
(28, 49, "STREET_ADDRESS"),
(50, 55, "ZIPCODE"),
]
}),
(
"New York North Greenbush 12144 NY 845 Golden Ridge Road"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 24, "CITY"),
(25, 30, "ZIPCODE"),
(31, 33, "STATE"),
(34, 55, "STREET_ADDRESS"),
]
}),
(
"845 Golden Ridge Road 12144 North Greenbush New York NY"
, {
"entities":[
(0, 21, "STREET_ADDRESS"),
(22, 27, "ZIPCODE"),
(28, 43, "CITY"),
(44, 52, "STATE_FULL"),
(53, 55, "STATE"),
]
}),
(
"Cambridge 02141 1245 Hillcrest Avenue MA Massachusetts"
, {
"entities":[
(0, 9, "CITY"),
(10, 15, "ZIPCODE"),
(16, 37, "STREET_ADDRESS"),
(38, 40, "STATE"),
(41, 54, "STATE_FULL"),
]
}),
(
"Cambridge 02141 1245 Hillcrest Avenue Massachusetts MA"
, {
"entities":[
(0, 9, "CITY"),
(10, 15, "ZIPCODE"),
(16, 37, "STREET_ADDRESS"),
(38, 51, "STATE_FULL"),
(52, 54, "STATE"),
]
}),
(
"02141 Cambridge MA 1245 Hillcrest Avenue Massachusetts"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 15, "CITY"),
(16, 18, "STATE"),
(19, 40, "STREET_ADDRESS"),
(41, 54, "STATE_FULL"),
]
}),
(
"MA Massachusetts Cambridge 02141 1245 Hillcrest Avenue"
, {
"entities":[
(0, 2, "STATE"),
(3, 16, "STATE_FULL"),
(17, 26, "CITY"),
(27, 32, "ZIPCODE"),
(33, 54, "STREET_ADDRESS"),
]
}),
(
"02141 1245 Hillcrest Avenue MA Cambridge Massachusetts"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 27, "STREET_ADDRESS"),
(28, 30, "STATE"),
(31, 40, "CITY"),
(41, 54, "STATE_FULL"),
]
}),
(
"Cambridge MA 1245 Hillcrest Avenue 02141 Massachusetts"
, {
"entities":[
(0, 9, "CITY"),
(10, 12, "STATE"),
(13, 34, "STREET_ADDRESS"),
(35, 40, "ZIPCODE"),
(41, 54, "STATE_FULL"),
]
}),
(
"Massachusetts 1245 Hillcrest Avenue Cambridge MA 02141"
, {
"entities":[
(0, 13, "STATE_FULL"),
(14, 35, "STREET_ADDRESS"),
(36, 45, "CITY"),
(46, 48, "STATE"),
(49, 54, "ZIPCODE"),
]
}),
(
"02141 Cambridge Massachusetts 1245 Hillcrest Avenue MA"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 15, "CITY"),
(16, 29, "STATE_FULL"),
(30, 51, "STREET_ADDRESS"),
(52, 54, "STATE"),
]
}),
(
"02141 Massachusetts 1245 Hillcrest Avenue MA Cambridge"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 19, "STATE_FULL"),
(20, 41, "STREET_ADDRESS"),
(42, 44, "STATE"),
(45, 54, "CITY"),
]
}),
(
"Massachusetts 02141 1245 Hillcrest Avenue MA Cambridge"
, {
"entities":[
(0, 13, "STATE_FULL"),
(14, 19, "ZIPCODE"),
(20, 41, "STREET_ADDRESS"),
(42, 44, "STATE"),
(45, 54, "CITY"),
]
}),
(
"California 94301 Palo Alto 3714 Ella Street CA"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 16, "ZIPCODE"),
(17, 26, "CITY"),
(27, 43, "STREET_ADDRESS"),
(44, 46, "STATE"),
]
}),
(
"California 3714 Ella Street CA Palo Alto 94301"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 27, "STREET_ADDRESS"),
(28, 30, "STATE"),
(31, 40, "CITY"),
(41, 46, "ZIPCODE"),
]
}),
(
"Palo Alto 94301 CA California 3714 Ella Street"
, {
"entities":[
(0, 9, "CITY"),
(10, 15, "ZIPCODE"),
(16, 18, "STATE"),
(19, 29, "STATE_FULL"),
(30, 46, "STREET_ADDRESS"),
]
}),
(
"CA California 94301 Palo Alto 3714 Ella Street"
, {
"entities":[
(0, 2, "STATE"),
(3, 13, "STATE_FULL"),
(14, 19, "ZIPCODE"),
(20, 29, "CITY"),
(30, 46, "STREET_ADDRESS"),
]
}),
(
"94301 California Palo Alto CA 3714 Ella Street"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 16, "STATE_FULL"),
(17, 26, "CITY"),
(27, 29, "STATE"),
(30, 46, "STREET_ADDRESS"),
]
}),
(
"Palo Alto California CA 3714 Ella Street 94301"
, {
"entities":[
(0, 9, "CITY"),
(10, 20, "STATE_FULL"),
(21, 23, "STATE"),
(24, 40, "STREET_ADDRESS"),
(41, 46, "ZIPCODE"),
]
}),
(
"Palo Alto 3714 Ella Street CA California 94301"
, {
"entities":[
(0, 9, "CITY"),
(10, 26, "STREET_ADDRESS"),
(27, 29, "STATE"),
(30, 40, "STATE_FULL"),
(41, 46, "ZIPCODE"),
]
}),
(
"Palo Alto 3714 Ella Street 94301 California CA"
, {
"entities":[
(0, 9, "CITY"),
(10, 26, "STREET_ADDRESS"),
(27, 32, "ZIPCODE"),
(33, 43, "STATE_FULL"),
(44, 46, "STATE"),
]
}),
(
"Palo Alto 3714 Ella Street CA 94301 California"
, {
"entities":[
(0, 9, "CITY"),
(10, 26, "STREET_ADDRESS"),
(27, 29, "STATE"),
(30, 35, "ZIPCODE"),
(36, 46, "STATE_FULL"),
]
}),
(
"CA 94301 3714 Ella Street California Palo Alto"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 25, "STREET_ADDRESS"),
(26, 36, "STATE_FULL"),
(37, 46, "CITY"),
]
}),
(
"45406 OH Ohio Dayton 4574 Pursglove Court"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 13, "STATE_FULL"),
(14, 20, "CITY"),
(21, 41, "STREET_ADDRESS"),
]
}),
(
"4574 Pursglove Court OH Ohio 45406 Dayton"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 23, "STATE"),
(24, 28, "STATE_FULL"),
(29, 34, "ZIPCODE"),
(35, 41, "CITY"),
]
}),
(
"Dayton 4574 Pursglove Court 45406 Ohio OH"
, {
"entities":[
(0, 6, "CITY"),
(7, 27, "STREET_ADDRESS"),
(28, 33, "ZIPCODE"),
(34, 38, "STATE_FULL"),
(39, 41, "STATE"),
]
}),
(
"Ohio Dayton 4574 Pursglove Court OH 45406"
, {
"entities":[
(0, 4, "STATE_FULL"),
(5, 11, "CITY"),
(12, 32, "STREET_ADDRESS"),
(33, 35, "STATE"),
(36, 41, "ZIPCODE"),
]
}),
(
"OH Dayton 4574 Pursglove Court Ohio 45406"
, {
"entities":[
(0, 2, "STATE"),
(3, 9, "CITY"),
(10, 30, "STREET_ADDRESS"),
(31, 35, "STATE_FULL"),
(36, 41, "ZIPCODE"),
]
}),
(
"Ohio OH 45406 Dayton 4574 Pursglove Court"
, {
"entities":[
(0, 4, "STATE_FULL"),
(5, 7, "STATE"),
(8, 13, "ZIPCODE"),
(14, 20, "CITY"),
(21, 41, "STREET_ADDRESS"),
]
}),
(
"45406 4574 Pursglove Court OH Ohio Dayton"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 26, "STREET_ADDRESS"),
(27, 29, "STATE"),
(30, 34, "STATE_FULL"),
(35, 41, "CITY"),
]
}),
(
"OH 4574 Pursglove Court 45406 Dayton Ohio"
, {
"entities":[
(0, 2, "STATE"),
(3, 23, "STREET_ADDRESS"),
(24, 29, "ZIPCODE"),
(30, 36, "CITY"),
(37, 41, "STATE_FULL"),
]
}),
(
"Dayton 4574 Pursglove Court Ohio OH 45406"
, {
"entities":[
(0, 6, "CITY"),
(7, 27, "STREET_ADDRESS"),
(28, 32, "STATE_FULL"),
(33, 35, "STATE"),
(36, 41, "ZIPCODE"),
]
}),
(
"OH Dayton 4574 Pursglove Court 45406 Ohio"
, {
"entities":[
(0, 2, "STATE"),
(3, 9, "CITY"),
(10, 30, "STREET_ADDRESS"),
(31, 36, "ZIPCODE"),
(37, 41, "STATE_FULL"),
]
}),
(
"77002 Texas Houston TX 2500 Chapel Street"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 11, "STATE_FULL"),
(12, 19, "CITY"),
(20, 22, "STATE"),
(23, 41, "STREET_ADDRESS"),
]
}),
(
"TX 2500 Chapel Street 77002 Houston Texas"
, {
"entities":[
(0, 2, "STATE"),
(3, 21, "STREET_ADDRESS"),
(22, 27, "ZIPCODE"),
(28, 35, "CITY"),
(36, 41, "STATE_FULL"),
]
}),
(
"77002 TX Texas 2500 Chapel Street Houston"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 14, "STATE_FULL"),
(15, 33, "STREET_ADDRESS"),
(34, 41, "CITY"),
]
}),
(
"77002 2500 Chapel Street Texas TX Houston"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 24, "STREET_ADDRESS"),
(25, 30, "STATE_FULL"),
(31, 33, "STATE"),
(34, 41, "CITY"),
]
}),
(
"Houston 77002 TX Texas 2500 Chapel Street"
, {
"entities":[
(0, 7, "CITY"),
(8, 13, "ZIPCODE"),
(14, 16, "STATE"),
(17, 22, "STATE_FULL"),
(23, 41, "STREET_ADDRESS"),
]
}),
(
"Texas Houston 2500 Chapel Street TX 77002"
, {
"entities":[
(0, 5, "STATE_FULL"),
(6, 13, "CITY"),
(14, 32, "STREET_ADDRESS"),
(33, 35, "STATE"),
(36, 41, "ZIPCODE"),
]
}),
(
"Houston 77002 2500 Chapel Street Texas TX"
, {
"entities":[
(0, 7, "CITY"),
(8, 13, "ZIPCODE"),
(14, 32, "STREET_ADDRESS"),
(33, 38, "STATE_FULL"),
(39, 41, "STATE"),
]
}),
(
"Texas Houston TX 2500 Chapel Street 77002"
, {
"entities":[
(0, 5, "STATE_FULL"),
(6, 13, "CITY"),
(14, 16, "STATE"),
(17, 35, "STREET_ADDRESS"),
(36, 41, "ZIPCODE"),
]
}),
(
"TX Texas Houston 2500 Chapel Street 77002"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "STATE_FULL"),
(9, 16, "CITY"),
(17, 35, "STREET_ADDRESS"),
(36, 41, "ZIPCODE"),
]
}),
(
"Houston Texas 2500 Chapel Street TX 77002"
, {
"entities":[
(0, 7, "CITY"),
(8, 13, "STATE_FULL"),
(14, 32, "STREET_ADDRESS"),
(33, 35, "STATE"),
(36, 41, "ZIPCODE"),
]
}),
(
"Illinois 2392 Eagle Street IL 63673 St Marys address"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 26, "STREET_ADDRESS"),
(27, 29, "STATE"),
(30, 35, "ZIPCODE"),
(36, 44, "CITY"),
]
}),
(
"St Marys IL address 63673 Illinois 2392 Eagle Street"
, {
"entities":[
(0, 8, "CITY"),
(9, 11, "STATE"),
(20, 25, "ZIPCODE"),
(26, 34, "STATE_FULL"),
(35, 52, "STREET_ADDRESS"),
]
}),
(
"Illinois 2392 Eagle Street address 63673 St Marys IL"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 26, "STREET_ADDRESS"),
(35, 40, "ZIPCODE"),
(41, 49, "CITY"),
(50, 52, "STATE"),
]
}),
(
"IL address Illinois St Marys 2392 Eagle Street 63673"
, {
"entities":[
(0, 2, "STATE"),
(11, 19, "STATE_FULL"),
(20, 28, "CITY"),
(29, 46, "STREET_ADDRESS"),
(47, 52, "ZIPCODE"),
]
}),
(
"IL St Marys 2392 Eagle Street Illinois 63673 address"
, {
"entities":[
(0, 2, "STATE"),
(3, 11, "CITY"),
(12, 29, "STREET_ADDRESS"),
(30, 38, "STATE_FULL"),
(39, 44, "ZIPCODE"),
]
}),
(
"Illinois St Marys 63673 address IL 2392 Eagle Street"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 17, "CITY"),
(18, 23, "ZIPCODE"),
(32, 34, "STATE"),
(35, 52, "STREET_ADDRESS"),
]
}),
(
"Illinois 2392 Eagle Street IL 63673 St Marys address"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 26, "STREET_ADDRESS"),
(27, 29, "STATE"),
(30, 35, "ZIPCODE"),
(36, 44, "CITY"),
]
}),
(
"63673 IL St Marys address 2392 Eagle Street Illinois"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 17, "CITY"),
(26, 43, "STREET_ADDRESS"),
(44, 52, "STATE_FULL"),
]
}),
(
"IL Illinois 63673 2392 Eagle Street address St Marys"
, {
"entities":[
(0, 2, "STATE"),
(3, 11, "STATE_FULL"),
(12, 17, "ZIPCODE"),
(18, 35, "STREET_ADDRESS"),
(44, 52, "CITY"),
]
}),
(
"2392 Eagle Street St Marys address 63673 IL Illinois"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 26, "CITY"),
(35, 40, "ZIPCODE"),
(41, 43, "STATE"),
(44, 52, "STATE_FULL"),
]
}),
(
"Owatonna 2322 Sugar Camp Road Minnesota MN 55060"
, {
"entities":[
(0, 8, "CITY"),
(9, 29, "STREET_ADDRESS"),
(30, 39, "STATE_FULL"),
(40, 42, "STATE"),
(43, 48, "ZIPCODE"),
]
}),
(
"Minnesota 55060 2322 Sugar Camp Road MN Owatonna"
, {
"entities":[
(0, 9, "STATE_FULL"),
(10, 15, "ZIPCODE"),
(16, 36, "STREET_ADDRESS"),
(37, 39, "STATE"),
(40, 48, "CITY"),
]
}),
(
"Minnesota Owatonna MN 55060 2322 Sugar Camp Road"
, {
"entities":[
(0, 9, "STATE_FULL"),
(10, 18, "CITY"),
(19, 21, "STATE"),
(22, 27, "ZIPCODE"),
(28, 48, "STREET_ADDRESS"),
]
}),
(
"Owatonna 55060 2322 Sugar Camp Road MN Minnesota"
, {
"entities":[
(0, 8, "CITY"),
(9, 14, "ZIPCODE"),
(15, 35, "STREET_ADDRESS"),
(36, 38, "STATE"),
(39, 48, "STATE_FULL"),
]
}),
(
"55060 Minnesota Owatonna 2322 Sugar Camp Road MN"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 15, "STATE_FULL"),
(16, 24, "CITY"),
(25, 45, "STREET_ADDRESS"),
(46, 48, "STATE"),
]
}),
(
"55060 Owatonna Minnesota MN 2322 Sugar Camp Road"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 14, "CITY"),
(15, 24, "STATE_FULL"),
(25, 27, "STATE"),
(28, 48, "STREET_ADDRESS"),
]
}),
(
"Minnesota 2322 Sugar Camp Road Owatonna 55060 MN"
, {
"entities":[
(0, 9, "STATE_FULL"),
(10, 30, "STREET_ADDRESS"),
(31, 39, "CITY"),
(40, 45, "ZIPCODE"),
(46, 48, "STATE"),
]
}),
(
"2322 Sugar Camp Road 55060 MN Minnesota Owatonna"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 26, "ZIPCODE"),
(27, 29, "STATE"),
(30, 39, "STATE_FULL"),
(40, 48, "CITY"),
]
}),
(
"55060 Owatonna Minnesota MN 2322 Sugar Camp Road"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 14, "CITY"),
(15, 24, "STATE_FULL"),
(25, 27, "STATE"),
(28, 48, "STREET_ADDRESS"),
]
}),
(
"55060 MN Owatonna 2322 Sugar Camp Road Minnesota"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 17, "CITY"),
(18, 38, "STREET_ADDRESS"),
(39, 48, "STATE_FULL"),
]
}),
(
"Irvine CA 92614 394 Leisure Lane California"
, {
"entities":[
(0, 6, "CITY"),
(7, 9, "STATE"),
(10, 15, "ZIPCODE"),
(16, 32, "STREET_ADDRESS"),
(33, 43, "STATE_FULL"),
]
}),
(
"CA Irvine 92614 394 Leisure Lane California"
, {
"entities":[
(0, 2, "STATE"),
(3, 9, "CITY"),
(10, 15, "ZIPCODE"),
(16, 32, "STREET_ADDRESS"),
(33, 43, "STATE_FULL"),
]
}),
(
"CA 394 Leisure Lane Irvine 92614 California"
, {
"entities":[
(0, 2, "STATE"),
(3, 19, "STREET_ADDRESS"),
(20, 26, "CITY"),
(27, 32, "ZIPCODE"),
(33, 43, "STATE_FULL"),
]
}),
(
"Irvine California 394 Leisure Lane 92614 CA"
, {
"entities":[
(0, 6, "CITY"),
(7, 17, "STATE_FULL"),
(18, 34, "STREET_ADDRESS"),
(35, 40, "ZIPCODE"),
(41, 43, "STATE"),
]
}),
(
"CA Irvine California 394 Leisure Lane 92614"
, {
"entities":[
(0, 2, "STATE"),
(3, 9, "CITY"),
(10, 20, "STATE_FULL"),
(21, 37, "STREET_ADDRESS"),
(38, 43, "ZIPCODE"),
]
}),
(
"92614 Irvine California CA 394 Leisure Lane"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 12, "CITY"),
(13, 23, "STATE_FULL"),
(24, 26, "STATE"),
(27, 43, "STREET_ADDRESS"),
]
}),
(
"394 Leisure Lane CA Irvine California 92614"
, {
"entities":[
(0, 16, "STREET_ADDRESS"),
(17, 19, "STATE"),
(20, 26, "CITY"),
(27, 37, "STATE_FULL"),
(38, 43, "ZIPCODE"),
]
}),
(
"Irvine 394 Leisure Lane CA California 92614"
, {
"entities":[
(0, 6, "CITY"),
(7, 23, "STREET_ADDRESS"),
(24, 26, "STATE"),
(27, 37, "STATE_FULL"),
(38, 43, "ZIPCODE"),
]
}),
(
"Irvine California 92614 394 Leisure Lane CA"
, {
"entities":[
(0, 6, "CITY"),
(7, 17, "STATE_FULL"),
(18, 23, "ZIPCODE"),
(24, 40, "STREET_ADDRESS"),
(41, 43, "STATE"),
]
}),
(
"California Irvine CA 92614 394 Leisure Lane"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 17, "CITY"),
(18, 20, "STATE"),
(21, 26, "ZIPCODE"),
(27, 43, "STREET_ADDRESS"),
]
}),
(
"Fort Worth Texas TX 1577 Romines Mill Road number 76104"
, {
"entities":[
(0, 10, "CITY"),
(11, 16, "STATE_FULL"),
(17, 19, "STATE"),
(20, 42, "STREET_ADDRESS"),
(50, 55, "ZIPCODE"),
]
}),
(
"1577 Romines Mill Road TX number Texas Fort Worth 76104"
, {
"entities":[
(0, 22, "STREET_ADDRESS"),
(23, 25, "STATE"),
(33, 38, "STATE_FULL"),
(39, 49, "CITY"),
(50, 55, "ZIPCODE"),
]
}),
(
"1577 Romines Mill Road Fort Worth TX Texas number 76104"
, {
"entities":[
(0, 22, "STREET_ADDRESS"),
(23, 33, "CITY"),
(34, 36, "STATE"),
(37, 42, "STATE_FULL"),
(50, 55, "ZIPCODE"),
]
}),
(
"1577 Romines Mill Road Texas number 76104 Fort Worth TX"
, {
"entities":[
(0, 22, "STREET_ADDRESS"),
(23, 28, "STATE_FULL"),
(36, 41, "ZIPCODE"),
(42, 52, "CITY"),
(53, 55, "STATE"),
]
}),
(
"Texas 76104 1577 Romines Mill Road Fort Worth TX number"
, {
"entities":[
(0, 5, "STATE_FULL"),
(6, 11, "ZIPCODE"),
(12, 34, "STREET_ADDRESS"),
(35, 45, "CITY"),
(46, 48, "STATE"),
]
}),
(
"76104 Fort Worth TX number 1577 Romines Mill Road Texas"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 16, "CITY"),
(17, 19, "STATE"),
(27, 49, "STREET_ADDRESS"),
(50, 55, "STATE_FULL"),
]
}),
(
"Texas Fort Worth number 1577 Romines Mill Road 76104 TX"
, {
"entities":[
(0, 5, "STATE_FULL"),
(6, 16, "CITY"),
(24, 46, "STREET_ADDRESS"),
(47, 52, "ZIPCODE"),
(53, 55, "STATE"),
]
}),
(
"TX Fort Worth number 1577 Romines Mill Road 76104 Texas"
, {
"entities":[
(0, 2, "STATE"),
(3, 13, "CITY"),
(21, 43, "STREET_ADDRESS"),
(44, 49, "ZIPCODE"),
(50, 55, "STATE_FULL"),
]
}),
(
"76104 number TX 1577 Romines Mill Road Texas Fort Worth"
, {
"entities":[
(0, 5, "ZIPCODE"),
(13, 15, "STATE"),
(16, 38, "STREET_ADDRESS"),
(39, 44, "STATE_FULL"),
(45, 55, "CITY"),
]
}),
(
"76104 Texas TX 1577 Romines Mill Road Fort Worth number"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 11, "STATE_FULL"),
(12, 14, "STATE"),
(15, 37, "STREET_ADDRESS"),
(38, 48, "CITY"),
]
}),
(
"1669 Poplar Street IL Illinois 60477 Tinley Park"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 21, "STATE"),
(22, 30, "STATE_FULL"),
(31, 36, "ZIPCODE"),
(37, 48, "CITY"),
]
}),
(
"IL 60477 Illinois 1669 Poplar Street Tinley Park"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 17, "STATE_FULL"),
(18, 36, "STREET_ADDRESS"),
(37, 48, "CITY"),
]
}),
(
"60477 Illinois IL 1669 Poplar Street Tinley Park"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 14, "STATE_FULL"),
(15, 17, "STATE"),
(18, 36, "STREET_ADDRESS"),
(37, 48, "CITY"),
]
}),
(
"60477 Tinley Park 1669 Poplar Street Illinois IL"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 17, "CITY"),
(18, 36, "STREET_ADDRESS"),
(37, 45, "STATE_FULL"),
(46, 48, "STATE"),
]
}),
(
"Tinley Park 1669 Poplar Street 60477 IL Illinois"
, {
"entities":[
(0, 11, "CITY"),
(12, 30, "STREET_ADDRESS"),
(31, 36, "ZIPCODE"),
(37, 39, "STATE"),
(40, 48, "STATE_FULL"),
]
}),
(
"Illinois IL 1669 Poplar Street Tinley Park 60477"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 11, "STATE"),
(12, 30, "STREET_ADDRESS"),
(31, 42, "CITY"),
(43, 48, "ZIPCODE"),
]
}),
(
"IL Illinois Tinley Park 1669 Poplar Street 60477"
, {
"entities":[
(0, 2, "STATE"),
(3, 11, "STATE_FULL"),
(12, 23, "CITY"),
(24, 42, "STREET_ADDRESS"),
(43, 48, "ZIPCODE"),
]
}),
(
"1669 Poplar Street Illinois IL 60477 Tinley Park"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 27, "STATE_FULL"),
(28, 30, "STATE"),
(31, 36, "ZIPCODE"),
(37, 48, "CITY"),
]
}),
(
"IL Illinois 1669 Poplar Street Tinley Park 60477"
, {
"entities":[
(0, 2, "STATE"),
(3, 11, "STATE_FULL"),
(12, 30, "STREET_ADDRESS"),
(31, 42, "CITY"),
(43, 48, "ZIPCODE"),
]
}),
(
"Tinley Park Illinois IL 60477 1669 Poplar Street"
, {
"entities":[
(0, 11, "CITY"),
(12, 20, "STATE_FULL"),
(21, 23, "STATE"),
(24, 29, "ZIPCODE"),
(30, 48, "STREET_ADDRESS"),
]
}),
(
"45030 1278 Heliport Loop Indiana IN Harrison"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 24, "STREET_ADDRESS"),
(25, 32, "STATE_FULL"),
(33, 35, "STATE"),
(36, 44, "CITY"),
]
}),
(
"Indiana 45030 Harrison 1278 Heliport Loop IN"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 13, "ZIPCODE"),
(14, 22, "CITY"),
(23, 41, "STREET_ADDRESS"),
(42, 44, "STATE"),
]
}),
(
"IN 45030 1278 Heliport Loop Harrison Indiana"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 27, "STREET_ADDRESS"),
(28, 36, "CITY"),
(37, 44, "STATE_FULL"),
]
}),
(
"IN Indiana 1278 Heliport Loop Harrison 45030"
, {
"entities":[
(0, 2, "STATE"),
(3, 10, "STATE_FULL"),
(11, 29, "STREET_ADDRESS"),
(30, 38, "CITY"),
(39, 44, "ZIPCODE"),
]
}),
(
"IN Indiana Harrison 1278 Heliport Loop 45030"
, {
"entities":[
(0, 2, "STATE"),
(3, 10, "STATE_FULL"),
(11, 19, "CITY"),
(20, 38, "STREET_ADDRESS"),
(39, 44, "ZIPCODE"),
]
}),
(
"Indiana Harrison 1278 Heliport Loop 45030 IN"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 16, "CITY"),
(17, 35, "STREET_ADDRESS"),
(36, 41, "ZIPCODE"),
(42, 44, "STATE"),
]
}),
(
"1278 Heliport Loop 45030 Indiana IN Harrison"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 24, "ZIPCODE"),
(25, 32, "STATE_FULL"),
(33, 35, "STATE"),
(36, 44, "CITY"),
]
}),
(
"45030 Harrison IN Indiana 1278 Heliport Loop"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 14, "CITY"),
(15, 17, "STATE"),
(18, 25, "STATE_FULL"),
(26, 44, "STREET_ADDRESS"),
]
}),
(
"45030 Indiana 1278 Heliport Loop Harrison IN"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 13, "STATE_FULL"),
(14, 32, "STREET_ADDRESS"),
(33, 41, "CITY"),
(42, 44, "STATE"),
]
}),
(
"Indiana 45030 1278 Heliport Loop Harrison IN"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 13, "ZIPCODE"),
(14, 32, "STREET_ADDRESS"),
(33, 41, "CITY"),
(42, 44, "STATE"),
]
}),
(
"Virginia Norfolk VA 3207 Allison Avenue 23510"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 16, "CITY"),
(17, 19, "STATE"),
(20, 39, "STREET_ADDRESS"),
(40, 45, "ZIPCODE"),
]
}),
(
"3207 Allison Avenue Norfolk 23510 VA Virginia"
, {
"entities":[
(0, 19, "STREET_ADDRESS"),
(20, 27, "CITY"),
(28, 33, "ZIPCODE"),
(34, 36, "STATE"),
(37, 45, "STATE_FULL"),
]
}),
(
"Norfolk Virginia 3207 Allison Avenue VA 23510"
, {
"entities":[
(0, 7, "CITY"),
(8, 16, "STATE_FULL"),
(17, 36, "STREET_ADDRESS"),
(37, 39, "STATE"),
(40, 45, "ZIPCODE"),
]
}),
(
"Norfolk 3207 Allison Avenue VA Virginia 23510"
, {
"entities":[
(0, 7, "CITY"),
(8, 27, "STREET_ADDRESS"),
(28, 30, "STATE"),
(31, 39, "STATE_FULL"),
(40, 45, "ZIPCODE"),
]
}),
(
"Norfolk 3207 Allison Avenue Virginia 23510 VA"
, {
"entities":[
(0, 7, "CITY"),
(8, 27, "STREET_ADDRESS"),
(28, 36, "STATE_FULL"),
(37, 42, "ZIPCODE"),
(43, 45, "STATE"),
]
}),
(
"VA Virginia 3207 Allison Avenue Norfolk 23510"
, {
"entities":[
(0, 2, "STATE"),
(3, 11, "STATE_FULL"),
(12, 31, "STREET_ADDRESS"),
(32, 39, "CITY"),
(40, 45, "ZIPCODE"),
]
}),
(
"VA Virginia 3207 Allison Avenue 23510 Norfolk"
, {
"entities":[
(0, 2, "STATE"),
(3, 11, "STATE_FULL"),
(12, 31, "STREET_ADDRESS"),
(32, 37, "ZIPCODE"),
(38, 45, "CITY"),
]
}),
(
"VA Norfolk 23510 Virginia 3207 Allison Avenue"
, {
"entities":[
(0, 2, "STATE"),
(3, 10, "CITY"),
(11, 16, "ZIPCODE"),
(17, 25, "STATE_FULL"),
(26, 45, "STREET_ADDRESS"),
]
}),
(
"23510 Norfolk VA 3207 Allison Avenue Virginia"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 13, "CITY"),
(14, 16, "STATE"),
(17, 36, "STREET_ADDRESS"),
(37, 45, "STATE_FULL"),
]
}),
(
"VA 3207 Allison Avenue 23510 Virginia Norfolk"
, {
"entities":[
(0, 2, "STATE"),
(3, 22, "STREET_ADDRESS"),
(23, 28, "ZIPCODE"),
(29, 37, "STATE_FULL"),
(38, 45, "CITY"),
]
}),
(
"66736 4501 Breezewood Court KS Fredonia address Kansas"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 27, "STREET_ADDRESS"),
(28, 30, "STATE"),
(31, 39, "CITY"),
(48, 54, "STATE_FULL"),
]
}),
(
"66736 Fredonia KS 4501 Breezewood Court address Kansas"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 14, "CITY"),
(15, 17, "STATE"),
(18, 39, "STREET_ADDRESS"),
(48, 54, "STATE_FULL"),
]
}),
(
"Fredonia address Kansas KS 4501 Breezewood Court 66736"
, {
"entities":[
(0, 8, "CITY"),
(17, 23, "STATE_FULL"),
(24, 26, "STATE"),
(27, 48, "STREET_ADDRESS"),
(49, 54, "ZIPCODE"),
]
}),
(
"4501 Breezewood Court 66736 address KS Kansas Fredonia"
, {
"entities":[
(0, 21, "STREET_ADDRESS"),
(22, 27, "ZIPCODE"),
(36, 38, "STATE"),
(39, 45, "STATE_FULL"),
(46, 54, "CITY"),
]
}),
(
"66736 address Kansas KS Fredonia 4501 Breezewood Court"
, {
"entities":[
(0, 5, "ZIPCODE"),
(14, 20, "STATE_FULL"),
(21, 23, "STATE"),
(24, 32, "CITY"),
(33, 54, "STREET_ADDRESS"),
]
}),
(
"66736 address 4501 Breezewood Court Fredonia KS Kansas"
, {
"entities":[
(0, 5, "ZIPCODE"),
(14, 35, "STREET_ADDRESS"),
(36, 44, "CITY"),
(45, 47, "STATE"),
(48, 54, "STATE_FULL"),
]
}),
(
"KS Kansas 4501 Breezewood Court address Fredonia 66736"
, {
"entities":[
(0, 2, "STATE"),
(3, 9, "STATE_FULL"),
(10, 31, "STREET_ADDRESS"),
(40, 48, "CITY"),
(49, 54, "ZIPCODE"),
]
}),
(
"KS Fredonia 66736 Kansas 4501 Breezewood Court address"
, {
"entities":[
(0, 2, "STATE"),
(3, 11, "CITY"),
(12, 17, "ZIPCODE"),
(18, 24, "STATE_FULL"),
(25, 46, "STREET_ADDRESS"),
]
}),
(
"4501 Breezewood Court address Fredonia 66736 KS Kansas"
, {
"entities":[
(0, 21, "STREET_ADDRESS"),
(30, 38, "CITY"),
(39, 44, "ZIPCODE"),
(45, 47, "STATE"),
(48, 54, "STATE_FULL"),
]
}),
(
"Kansas address 4501 Breezewood Court 66736 Fredonia KS"
, {
"entities":[
(0, 6, "STATE_FULL"),
(15, 36, "STREET_ADDRESS"),
(37, 42, "ZIPCODE"),
(43, 51, "CITY"),
(52, 54, "STATE"),
]
}),
(
"28328 1474 Ray Court North Carolina Clinton NC"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 20, "STREET_ADDRESS"),
(21, 35, "STATE_FULL"),
(36, 43, "CITY"),
(44, 46, "STATE"),
]
}),
(
"NC 28328 North Carolina Clinton 1474 Ray Court"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 23, "STATE_FULL"),
(24, 31, "CITY"),
(32, 46, "STREET_ADDRESS"),
]
}),
(
"1474 Ray Court NC 28328 Clinton North Carolina"
, {
"entities":[
(0, 14, "STREET_ADDRESS"),
(15, 17, "STATE"),
(18, 23, "ZIPCODE"),
(24, 31, "CITY"),
(32, 46, "STATE_FULL"),
]
}),
(
"NC 1474 Ray Court Clinton 28328 North Carolina"
, {
"entities":[
(0, 2, "STATE"),
(3, 17, "STREET_ADDRESS"),
(18, 25, "CITY"),
(26, 31, "ZIPCODE"),
(32, 46, "STATE_FULL"),
]
}),
(
"28328 North Carolina Clinton NC 1474 Ray Court"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 20, "STATE_FULL"),
(21, 28, "CITY"),
(29, 31, "STATE"),
(32, 46, "STREET_ADDRESS"),
]
}),
(
"Clinton 1474 Ray Court 28328 NC North Carolina"
, {
"entities":[
(0, 7, "CITY"),
(8, 22, "STREET_ADDRESS"),
(23, 28, "ZIPCODE"),
(29, 31, "STATE"),
(32, 46, "STATE_FULL"),
]
}),
(
"28328 1474 Ray Court Clinton North Carolina NC"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 20, "STREET_ADDRESS"),
(21, 28, "CITY"),
(29, 43, "STATE_FULL"),
(44, 46, "STATE"),
]
}),
(
"North Carolina NC Clinton 28328 1474 Ray Court"
, {
"entities":[
(0, 14, "STATE_FULL"),
(15, 17, "STATE"),
(18, 25, "CITY"),
(26, 31, "ZIPCODE"),
(32, 46, "STREET_ADDRESS"),
]
}),
(
"NC 1474 Ray Court North Carolina 28328 Clinton"
, {
"entities":[
(0, 2, "STATE"),
(3, 17, "STREET_ADDRESS"),
(18, 32, "STATE_FULL"),
(33, 38, "ZIPCODE"),
(39, 46, "CITY"),
]
}),
(
"1474 Ray Court Clinton 28328 North Carolina NC"
, {
"entities":[
(0, 14, "STREET_ADDRESS"),
(15, 22, "CITY"),
(23, 28, "ZIPCODE"),
(29, 43, "STATE_FULL"),
(44, 46, "STATE"),
]
}),
(
"from Des Moines 50313 Iowa IA 4270 Nutters Barn Lane"
, {
"entities":[
(5, 15, "CITY"),
(16, 21, "ZIPCODE"),
(22, 26, "STATE_FULL"),
(27, 29, "STATE"),
(30, 52, "STREET_ADDRESS"),
]
}),
(
"IA 4270 Nutters Barn Lane 50313 from Iowa Des Moines"
, {
"entities":[
(0, 2, "STATE"),
(3, 25, "STREET_ADDRESS"),
(26, 31, "ZIPCODE"),
(37, 41, "STATE_FULL"),
(42, 52, "CITY"),
]
}),
(
"Iowa 4270 Nutters Barn Lane 50313 Des Moines IA from"
, {
"entities":[
(0, 4, "STATE_FULL"),
(5, 27, "STREET_ADDRESS"),
(28, 33, "ZIPCODE"),
(34, 44, "CITY"),
(45, 47, "STATE"),
]
}),
(
"50313 from 4270 Nutters Barn Lane Iowa IA Des Moines"
, {
"entities":[
(0, 5, "ZIPCODE"),
(11, 33, "STREET_ADDRESS"),
(34, 38, "STATE_FULL"),
(39, 41, "STATE"),
(42, 52, "CITY"),
]
}),
(
"50313 Iowa IA 4270 Nutters Barn Lane Des Moines from"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 10, "STATE_FULL"),
(11, 13, "STATE"),
(14, 36, "STREET_ADDRESS"),
(37, 47, "CITY"),
]
}),
(
"50313 4270 Nutters Barn Lane IA Iowa Des Moines from"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 28, "STREET_ADDRESS"),
(29, 31, "STATE"),
(32, 36, "STATE_FULL"),
(37, 47, "CITY"),
]
}),
(
"Des Moines IA from Iowa 4270 Nutters Barn Lane 50313"
, {
"entities":[
(0, 10, "CITY"),
(11, 13, "STATE"),
(19, 23, "STATE_FULL"),
(24, 46, "STREET_ADDRESS"),
(47, 52, "ZIPCODE"),
]
}),
(
"50313 4270 Nutters Barn Lane from Iowa IA Des Moines"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 28, "STREET_ADDRESS"),
(34, 38, "STATE_FULL"),
(39, 41, "STATE"),
(42, 52, "CITY"),
]
}),
(
"Iowa Des Moines IA 4270 Nutters Barn Lane from 50313"
, {
"entities":[
(0, 4, "STATE_FULL"),
(5, 15, "CITY"),
(16, 18, "STATE"),
(19, 41, "STREET_ADDRESS"),
(47, 52, "ZIPCODE"),
]
}),
(
"Des Moines 50313 IA 4270 Nutters Barn Lane Iowa from"
, {
"entities":[
(0, 10, "CITY"),
(11, 16, "ZIPCODE"),
(17, 19, "STATE"),
(20, 42, "STREET_ADDRESS"),
(43, 47, "STATE_FULL"),
]
}),
(
"118 Farnum Road NY New York New York 10013"
, {
"entities":[
(0, 15, "STREET_ADDRESS"),
(16, 18, "STATE"),
(19, 27, "STATE_FULL"),
(28, 36, "CITY"),
(37, 42, "ZIPCODE"),
]
}),
(
"New York NY 118 Farnum Road 10013 New York"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 11, "STATE"),
(12, 27, "STREET_ADDRESS"),
(28, 33, "ZIPCODE"),
(34, 42, "CITY"),
]
}),
(
"10013 New York New York 118 Farnum Road NY"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 14, "STATE_FULL"),
(15, 23, "CITY"),
(24, 39, "STREET_ADDRESS"),
(40, 42, "STATE"),
]
}),
(
"New York 118 Farnum Road 10013 New York NY"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 24, "STREET_ADDRESS"),
(25, 30, "ZIPCODE"),
(31, 39, "CITY"),
(40, 42, "STATE"),
]
}),
(
"New York 118 Farnum Road 10013 New York NY"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 24, "STREET_ADDRESS"),
(25, 30, "ZIPCODE"),
(31, 39, "CITY"),
(40, 42, "STATE"),
]
}),
(
"NY New York New York 118 Farnum Road 10013"
, {
"entities":[
(0, 2, "STATE"),
(3, 11, "CITY"),
(12, 20, "STATE_FULL"),
(21, 36, "STREET_ADDRESS"),
(37, 42, "ZIPCODE"),
]
}),
(
"118 Farnum Road 10013 New York New York NY"
, {
"entities":[
(0, 15, "STREET_ADDRESS"),
(16, 21, "ZIPCODE"),
(22, 30, "CITY"),
(31, 39, "STATE_FULL"),
(40, 42, "STATE"),
]
}),
(
"NY 10013 New York 118 Farnum Road New York"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 17, "STATE_FULL"),
(18, 33, "STREET_ADDRESS"),
(34, 42, "CITY"),
]
}),
(
"118 Farnum Road New York New York 10013 NY"
, {
"entities":[
(0, 15, "STREET_ADDRESS"),
(16, 24, "CITY"),
(25, 33, "STATE_FULL"),
(34, 39, "ZIPCODE"),
(40, 42, "STATE"),
]
}),
(
"New York New York NY 10013 118 Farnum Road"
, {
"entities":[
(0, 8, "CITY"),
(9, 17, "STATE_FULL"),
(18, 20, "STATE"),
(21, 26, "ZIPCODE"),
(27, 42, "STREET_ADDRESS"),
]
}),
(
"Dallas Texas 2593 Florence Street TX 75247"
, {
"entities":[
(0, 6, "CITY"),
(7, 12, "STATE_FULL"),
(13, 33, "STREET_ADDRESS"),
(34, 36, "STATE"),
(37, 42, "ZIPCODE"),
]
}),
(
"TX Dallas Texas 2593 Florence Street 75247"
, {
"entities":[
(0, 2, "STATE"),
(3, 9, "CITY"),
(10, 15, "STATE_FULL"),
(16, 36, "STREET_ADDRESS"),
(37, 42, "ZIPCODE"),
]
}),
(
"Texas Dallas 2593 Florence Street 75247 TX"
, {
"entities":[
(0, 5, "STATE_FULL"),
(6, 12, "CITY"),
(13, 33, "STREET_ADDRESS"),
(34, 39, "ZIPCODE"),
(40, 42, "STATE"),
]
}),
(
"2593 Florence Street TX Texas Dallas 75247"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 23, "STATE"),
(24, 29, "STATE_FULL"),
(30, 36, "CITY"),
(37, 42, "ZIPCODE"),
]
}),
(
"75247 2593 Florence Street Dallas TX Texas"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 26, "STREET_ADDRESS"),
(27, 33, "CITY"),
(34, 36, "STATE"),
(37, 42, "STATE_FULL"),
]
}),
(
"2593 Florence Street 75247 Dallas TX Texas"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 26, "ZIPCODE"),
(27, 33, "CITY"),
(34, 36, "STATE"),
(37, 42, "STATE_FULL"),
]
}),
(
"Texas Dallas 75247 2593 Florence Street TX"
, {
"entities":[
(0, 5, "STATE_FULL"),
(6, 12, "CITY"),
(13, 18, "ZIPCODE"),
(19, 39, "STREET_ADDRESS"),
(40, 42, "STATE"),
]
}),
(
"2593 Florence Street Texas 75247 TX Dallas"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 26, "STATE_FULL"),
(27, 32, "ZIPCODE"),
(33, 35, "STATE"),
(36, 42, "CITY"),
]
}),
(
"Texas 75247 TX Dallas 2593 Florence Street"
, {
"entities":[
(0, 5, "STATE_FULL"),
(6, 11, "ZIPCODE"),
(12, 14, "STATE"),
(15, 21, "CITY"),
(22, 42, "STREET_ADDRESS"),
]
}),
(
"2593 Florence Street Dallas 75247 Texas TX"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 27, "CITY"),
(28, 33, "ZIPCODE"),
(34, 39, "STATE_FULL"),
(40, 42, "STATE"),
]
}),
(
"We NY 12956 196 West Virginia Avenue New York Mineville"
, {
"entities":[
(3, 5, "STATE"),
(6, 11, "ZIPCODE"),
(12, 36, "STREET_ADDRESS"),
(37, 45, "STATE_FULL"),
(46, 55, "CITY"),
]
}),
(
"We Mineville 196 West Virginia Avenue New York NY 12956"
, {
"entities":[
(3, 12, "CITY"),
(13, 37, "STREET_ADDRESS"),
(38, 46, "STATE_FULL"),
(47, 49, "STATE"),
(50, 55, "ZIPCODE"),
]
}),
(
"We New York NY Mineville 12956 196 West Virginia Avenue"
, {
"entities":[
(3, 11, "STATE_FULL"),
(12, 14, "STATE"),
(15, 24, "CITY"),
(25, 30, "ZIPCODE"),
(31, 55, "STREET_ADDRESS"),
]
}),
(
"12956 We NY New York 196 West Virginia Avenue Mineville"
, {
"entities":[
(0, 5, "ZIPCODE"),
(9, 11, "STATE"),
(12, 20, "STATE_FULL"),
(21, 45, "STREET_ADDRESS"),
(46, 55, "CITY"),
]
}),
(
"12956 196 West Virginia Avenue Mineville New York NY We"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 30, "STREET_ADDRESS"),
(31, 40, "CITY"),
(41, 49, "STATE_FULL"),
(50, 52, "STATE"),
]
}),
(
"We Mineville NY 196 West Virginia Avenue 12956 New York"
, {
"entities":[
(3, 12, "CITY"),
(13, 15, "STATE"),
(16, 40, "STREET_ADDRESS"),
(41, 46, "ZIPCODE"),
(47, 55, "STATE_FULL"),
]
}),
(
"196 West Virginia Avenue 12956 Mineville NY We New York"
, {
"entities":[
(0, 24, "STREET_ADDRESS"),
(25, 30, "ZIPCODE"),
(31, 40, "CITY"),
(41, 43, "STATE"),
(47, 55, "STATE_FULL"),
]
}),
(
"196 West Virginia Avenue NY New York Mineville We 12956"
, {
"entities":[
(0, 24, "STREET_ADDRESS"),
(25, 27, "STATE"),
(28, 36, "STATE_FULL"),
(37, 46, "CITY"),
(50, 55, "ZIPCODE"),
]
}),
(
"196 West Virginia Avenue Mineville New York We 12956 NY"
, {
"entities":[
(0, 24, "STREET_ADDRESS"),
(25, 34, "CITY"),
(35, 43, "STATE_FULL"),
(47, 52, "ZIPCODE"),
(53, 55, "STATE"),
]
}),
(
"New York NY We Mineville 12956 196 West Virginia Avenue"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 11, "STATE"),
(15, 24, "CITY"),
(25, 30, "ZIPCODE"),
(31, 55, "STREET_ADDRESS"),
]
}),
(
"485 Brookview Drive Beaumont 77701 TX Texas"
, {
"entities":[
(0, 19, "STREET_ADDRESS"),
(20, 28, "CITY"),
(29, 34, "ZIPCODE"),
(35, 37, "STATE"),
(38, 43, "STATE_FULL"),
]
}),
(
"Texas 485 Brookview Drive Beaumont TX 77701"
, {
"entities":[
(0, 5, "STATE_FULL"),
(6, 25, "STREET_ADDRESS"),
(26, 34, "CITY"),
(35, 37, "STATE"),
(38, 43, "ZIPCODE"),
]
}),
(
"Texas Beaumont 485 Brookview Drive TX 77701"
, {
"entities":[
(0, 5, "STATE_FULL"),
(6, 14, "CITY"),
(15, 34, "STREET_ADDRESS"),
(35, 37, "STATE"),
(38, 43, "ZIPCODE"),
]
}),
(
"Texas TX Beaumont 77701 485 Brookview Drive"
, {
"entities":[
(0, 5, "STATE_FULL"),
(6, 8, "STATE"),
(9, 17, "CITY"),
(18, 23, "ZIPCODE"),
(24, 43, "STREET_ADDRESS"),
]
}),
(
"77701 485 Brookview Drive Beaumont Texas TX"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 25, "STREET_ADDRESS"),
(26, 34, "CITY"),
(35, 40, "STATE_FULL"),
(41, 43, "STATE"),
]
}),
(
"Texas TX Beaumont 77701 485 Brookview Drive"
, {
"entities":[
(0, 5, "STATE_FULL"),
(6, 8, "STATE"),
(9, 17, "CITY"),
(18, 23, "ZIPCODE"),
(24, 43, "STREET_ADDRESS"),
]
}),
(
"TX Beaumont Texas 77701 485 Brookview Drive"
, {
"entities":[
(0, 2, "STATE"),
(3, 11, "CITY"),
(12, 17, "STATE_FULL"),
(18, 23, "ZIPCODE"),
(24, 43, "STREET_ADDRESS"),
]
}),
(
"485 Brookview Drive Beaumont TX 77701 Texas"
, {
"entities":[
(0, 19, "STREET_ADDRESS"),
(20, 28, "CITY"),
(29, 31, "STATE"),
(32, 37, "ZIPCODE"),
(38, 43, "STATE_FULL"),
]
}),
(
"485 Brookview Drive TX Texas Beaumont 77701"
, {
"entities":[
(0, 19, "STREET_ADDRESS"),
(20, 22, "STATE"),
(23, 28, "STATE_FULL"),
(29, 37, "CITY"),
(38, 43, "ZIPCODE"),
]
}),
(
"Beaumont 485 Brookview Drive TX 77701 Texas"
, {
"entities":[
(0, 8, "CITY"),
(9, 28, "STREET_ADDRESS"),
(29, 31, "STATE"),
(32, 37, "ZIPCODE"),
(38, 43, "STATE_FULL"),
]
}),
(
"2264 Sunny Glen Lane OH 44115 Cleveland Ohio"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 23, "STATE"),
(24, 29, "ZIPCODE"),
(30, 39, "CITY"),
(40, 44, "STATE_FULL"),
]
}),
(
"2264 Sunny Glen Lane OH Ohio Cleveland 44115"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 23, "STATE"),
(24, 28, "STATE_FULL"),
(29, 38, "CITY"),
(39, 44, "ZIPCODE"),
]
}),
(
"OH Cleveland 2264 Sunny Glen Lane 44115 Ohio"
, {
"entities":[
(0, 2, "STATE"),
(3, 12, "CITY"),
(13, 33, "STREET_ADDRESS"),
(34, 39, "ZIPCODE"),
(40, 44, "STATE_FULL"),
]
}),
(
"44115 Ohio 2264 Sunny Glen Lane Cleveland OH"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 10, "STATE_FULL"),
(11, 31, "STREET_ADDRESS"),
(32, 41, "CITY"),
(42, 44, "STATE"),
]
}),
(
"Ohio Cleveland 44115 OH 2264 Sunny Glen Lane"
, {
"entities":[
(0, 4, "STATE_FULL"),
(5, 14, "CITY"),
(15, 20, "ZIPCODE"),
(21, 23, "STATE"),
(24, 44, "STREET_ADDRESS"),
]
}),
(
"OH 2264 Sunny Glen Lane Ohio Cleveland 44115"
, {
"entities":[
(0, 2, "STATE"),
(3, 23, "STREET_ADDRESS"),
(24, 28, "STATE_FULL"),
(29, 38, "CITY"),
(39, 44, "ZIPCODE"),
]
}),
(
"OH Ohio 2264 Sunny Glen Lane 44115 Cleveland"
, {
"entities":[
(0, 2, "STATE"),
(3, 7, "STATE_FULL"),
(8, 28, "STREET_ADDRESS"),
(29, 34, "ZIPCODE"),
(35, 44, "CITY"),
]
}),
(
"OH Ohio Cleveland 44115 2264 Sunny Glen Lane"
, {
"entities":[
(0, 2, "STATE"),
(3, 7, "STATE_FULL"),
(8, 17, "CITY"),
(18, 23, "ZIPCODE"),
(24, 44, "STREET_ADDRESS"),
]
}),
(
"Ohio 2264 Sunny Glen Lane 44115 Cleveland OH"
, {
"entities":[
(0, 4, "STATE_FULL"),
(5, 25, "STREET_ADDRESS"),
(26, 31, "ZIPCODE"),
(32, 41, "CITY"),
(42, 44, "STATE"),
]
}),
(
"Ohio OH Cleveland 2264 Sunny Glen Lane 44115"
, {
"entities":[
(0, 4, "STATE_FULL"),
(5, 7, "STATE"),
(8, 17, "CITY"),
(18, 38, "STREET_ADDRESS"),
(39, 44, "ZIPCODE"),
]
}),
(
"755 Philadelphia Avenue Contact Information UT 84117 Utah Holladay"
, {
"entities":[
(0, 23, "STREET_ADDRESS"),
(44, 46, "STATE"),
(47, 52, "ZIPCODE"),
(53, 57, "STATE_FULL"),
(58, 66, "CITY"),
]
}),
(
"UT 755 Philadelphia Avenue Contact Information Holladay 84117 Utah"
, {
"entities":[
(0, 2, "STATE"),
(3, 26, "STREET_ADDRESS"),
(47, 55, "CITY"),
(56, 61, "ZIPCODE"),
(62, 66, "STATE_FULL"),
]
}),
(
"Contact Information 84117 UT 755 Philadelphia Avenue Utah Holladay"
, {
"entities":[
(20, 25, "ZIPCODE"),
(26, 28, "STATE"),
(29, 52, "STREET_ADDRESS"),
(53, 57, "STATE_FULL"),
(58, 66, "CITY"),
]
}),
(
"Holladay 84117 Utah Contact Information UT 755 Philadelphia Avenue"
, {
"entities":[
(0, 8, "CITY"),
(9, 14, "ZIPCODE"),
(15, 19, "STATE_FULL"),
(40, 42, "STATE"),
(43, 66, "STREET_ADDRESS"),
]
}),
(
"84117 Utah UT 755 Philadelphia Avenue Contact Information Holladay"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 10, "STATE_FULL"),
(11, 13, "STATE"),
(14, 37, "STREET_ADDRESS"),
(58, 66, "CITY"),
]
}),
(
"Utah 755 Philadelphia Avenue Holladay UT 84117 Contact Information"
, {
"entities":[
(0, 4, "STATE_FULL"),
(5, 28, "STREET_ADDRESS"),
(29, 37, "CITY"),
(38, 40, "STATE"),
(41, 46, "ZIPCODE"),
]
}),
(
"Contact Information 755 Philadelphia Avenue UT 84117 Utah Holladay"
, {
"entities":[
(20, 43, "STREET_ADDRESS"),
(44, 46, "STATE"),
(47, 52, "ZIPCODE"),
(53, 57, "STATE_FULL"),
(58, 66, "CITY"),
]
}),
(
"Contact Information Utah UT 755 Philadelphia Avenue Holladay 84117"
, {
"entities":[
(20, 24, "STATE_FULL"),
(25, 27, "STATE"),
(28, 51, "STREET_ADDRESS"),
(52, 60, "CITY"),
(61, 66, "ZIPCODE"),
]
}),
(
"Holladay Utah Contact Information 755 Philadelphia Avenue 84117 UT"
, {
"entities":[
(0, 8, "CITY"),
(9, 13, "STATE_FULL"),
(34, 57, "STREET_ADDRESS"),
(58, 63, "ZIPCODE"),
(64, 66, "STATE"),
]
}),
(
"Holladay Contact Information UT Utah 84117 755 Philadelphia Avenue"
, {
"entities":[
(0, 8, "CITY"),
(29, 31, "STATE"),
(32, 36, "STATE_FULL"),
(37, 42, "ZIPCODE"),
(43, 66, "STREET_ADDRESS"),
]
}),
(
"NH 03103 New Hampshire 400 Milford Street Manchester"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 22, "STATE_FULL"),
(23, 41, "STREET_ADDRESS"),
(42, 52, "CITY"),
]
}),
(
"NH Manchester 03103 400 Milford Street New Hampshire"
, {
"entities":[
(0, 2, "STATE"),
(3, 13, "CITY"),
(14, 19, "ZIPCODE"),
(20, 38, "STREET_ADDRESS"),
(39, 52, "STATE_FULL"),
]
}),
(
"New Hampshire 03103 NH Manchester 400 Milford Street"
, {
"entities":[
(0, 13, "STATE_FULL"),
(14, 19, "ZIPCODE"),
(20, 22, "STATE"),
(23, 33, "CITY"),
(34, 52, "STREET_ADDRESS"),
]
}),
(
"NH 400 Milford Street Manchester 03103 New Hampshire"
, {
"entities":[
(0, 2, "STATE"),
(3, 21, "STREET_ADDRESS"),
(22, 32, "CITY"),
(33, 38, "ZIPCODE"),
(39, 52, "STATE_FULL"),
]
}),
(
"400 Milford Street 03103 Manchester NH New Hampshire"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 24, "ZIPCODE"),
(25, 35, "CITY"),
(36, 38, "STATE"),
(39, 52, "STATE_FULL"),
]
}),
(
"NH New Hampshire 400 Milford Street Manchester 03103"
, {
"entities":[
(0, 2, "STATE"),
(3, 16, "STATE_FULL"),
(17, 35, "STREET_ADDRESS"),
(36, 46, "CITY"),
(47, 52, "ZIPCODE"),
]
}),
(
"New Hampshire 03103 Manchester 400 Milford Street NH"
, {
"entities":[
(0, 13, "STATE_FULL"),
(14, 19, "ZIPCODE"),
(20, 30, "CITY"),
(31, 49, "STREET_ADDRESS"),
(50, 52, "STATE"),
]
}),
(
"400 Milford Street 03103 NH New Hampshire Manchester"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 24, "ZIPCODE"),
(25, 27, "STATE"),
(28, 41, "STATE_FULL"),
(42, 52, "CITY"),
]
}),
(
"NH Manchester 03103 New Hampshire 400 Milford Street"
, {
"entities":[
(0, 2, "STATE"),
(3, 13, "CITY"),
(14, 19, "ZIPCODE"),
(20, 33, "STATE_FULL"),
(34, 52, "STREET_ADDRESS"),
]
}),
(
"Manchester NH 03103 400 Milford Street New Hampshire"
, {
"entities":[
(0, 10, "CITY"),
(11, 13, "STATE"),
(14, 19, "ZIPCODE"),
(20, 38, "STREET_ADDRESS"),
(39, 52, "STATE_FULL"),
]
}),
(
"MN Cold Spring Minnesota 56320 1114 Red Hawk Road"
, {
"entities":[
(0, 2, "STATE"),
(3, 14, "CITY"),
(15, 24, "STATE_FULL"),
(25, 30, "ZIPCODE"),
(31, 49, "STREET_ADDRESS"),
]
}),
(
"56320 MN 1114 Red Hawk Road Cold Spring Minnesota"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 27, "STREET_ADDRESS"),
(28, 39, "CITY"),
(40, 49, "STATE_FULL"),
]
}),
(
"MN 56320 Minnesota Cold Spring 1114 Red Hawk Road"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 18, "STATE_FULL"),
(19, 30, "CITY"),
(31, 49, "STREET_ADDRESS"),
]
}),
(
"1114 Red Hawk Road Cold Spring Minnesota 56320 MN"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 30, "CITY"),
(31, 40, "STATE_FULL"),
(41, 46, "ZIPCODE"),
(47, 49, "STATE"),
]
}),
(
"Cold Spring MN Minnesota 56320 1114 Red Hawk Road"
, {
"entities":[
(0, 11, "CITY"),
(12, 14, "STATE"),
(15, 24, "STATE_FULL"),
(25, 30, "ZIPCODE"),
(31, 49, "STREET_ADDRESS"),
]
}),
(
"Cold Spring MN 56320 1114 Red Hawk Road Minnesota"
, {
"entities":[
(0, 11, "CITY"),
(12, 14, "STATE"),
(15, 20, "ZIPCODE"),
(21, 39, "STREET_ADDRESS"),
(40, 49, "STATE_FULL"),
]
}),
(
"Minnesota 56320 MN Cold Spring 1114 Red Hawk Road"
, {
"entities":[
(0, 9, "STATE_FULL"),
(10, 15, "ZIPCODE"),
(16, 18, "STATE"),
(19, 30, "CITY"),
(31, 49, "STREET_ADDRESS"),
]
}),
(
"1114 Red Hawk Road Cold Spring 56320 MN Minnesota"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 30, "CITY"),
(31, 36, "ZIPCODE"),
(37, 39, "STATE"),
(40, 49, "STATE_FULL"),
]
}),
(
"1114 Red Hawk Road Cold Spring 56320 Minnesota MN"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 30, "CITY"),
(31, 36, "ZIPCODE"),
(37, 46, "STATE_FULL"),
(47, 49, "STATE"),
]
}),
(
"Cold Spring Minnesota 1114 Red Hawk Road MN 56320"
, {
"entities":[
(0, 11, "CITY"),
(12, 21, "STATE_FULL"),
(22, 40, "STREET_ADDRESS"),
(41, 43, "STATE"),
(44, 49, "ZIPCODE"),
]
}),
(
"75075 TX 1276 Worthington Drive Texas Plano estimate"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 31, "STREET_ADDRESS"),
(32, 37, "STATE_FULL"),
(38, 43, "CITY"),
]
}),
(
"Plano TX Texas 1276 Worthington Drive 75075 estimate"
, {
"entities":[
(0, 5, "CITY"),
(6, 8, "STATE"),
(9, 14, "STATE_FULL"),
(15, 37, "STREET_ADDRESS"),
(38, 43, "ZIPCODE"),
]
}),
(
"estimate 1276 Worthington Drive TX Texas Plano 75075"
, {
"entities":[
(9, 31, "STREET_ADDRESS"),
(32, 34, "STATE"),
(35, 40, "STATE_FULL"),
(41, 46, "CITY"),
(47, 52, "ZIPCODE"),
]
}),
(
"Plano estimate Texas 1276 Worthington Drive 75075 TX"
, {
"entities":[
(0, 5, "CITY"),
(15, 20, "STATE_FULL"),
(21, 43, "STREET_ADDRESS"),
(44, 49, "ZIPCODE"),
(50, 52, "STATE"),
]
}),
(
"75075 Plano Texas 1276 Worthington Drive estimate TX"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 11, "CITY"),
(12, 17, "STATE_FULL"),
(18, 40, "STREET_ADDRESS"),
(50, 52, "STATE"),
]
}),
(
"TX Plano 75075 estimate Texas 1276 Worthington Drive"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "CITY"),
(9, 14, "ZIPCODE"),
(24, 29, "STATE_FULL"),
(30, 52, "STREET_ADDRESS"),
]
}),
(
"Plano TX 75075 estimate 1276 Worthington Drive Texas"
, {
"entities":[
(0, 5, "CITY"),
(6, 8, "STATE"),
(9, 14, "ZIPCODE"),
(24, 46, "STREET_ADDRESS"),
(47, 52, "STATE_FULL"),
]
}),
(
"Texas TX 75075 Plano 1276 Worthington Drive estimate"
, {
"entities":[
(0, 5, "STATE_FULL"),
(6, 8, "STATE"),
(9, 14, "ZIPCODE"),
(15, 20, "CITY"),
(21, 43, "STREET_ADDRESS"),
]
}),
(
"Plano 1276 Worthington Drive 75075 TX estimate Texas"
, {
"entities":[
(0, 5, "CITY"),
(6, 28, "STREET_ADDRESS"),
(29, 34, "ZIPCODE"),
(35, 37, "STATE"),
(47, 52, "STATE_FULL"),
]
}),
(
"Texas 75075 1276 Worthington Drive estimate TX Plano"
, {
"entities":[
(0, 5, "STATE_FULL"),
(6, 11, "ZIPCODE"),
(12, 34, "STREET_ADDRESS"),
(44, 46, "STATE"),
(47, 52, "CITY"),
]
}),
(
"number 97058 OR 4537 Center Street The Dalles Oregon"
, {
"entities":[
(7, 12, "ZIPCODE"),
(13, 15, "STATE"),
(16, 34, "STREET_ADDRESS"),
(35, 45, "CITY"),
(46, 52, "STATE_FULL"),
]
}),
(
"The Dalles OR 4537 Center Street 97058 Oregon number"
, {
"entities":[
(0, 10, "CITY"),
(11, 13, "STATE"),
(14, 32, "STREET_ADDRESS"),
(33, 38, "ZIPCODE"),
(39, 45, "STATE_FULL"),
]
}),
(
"4537 Center Street number 97058 OR Oregon The Dalles"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(26, 31, "ZIPCODE"),
(32, 34, "STATE"),
(35, 41, "STATE_FULL"),
(42, 52, "CITY"),
]
}),
(
"Oregon number 4537 Center Street 97058 OR The Dalles"
, {
"entities":[
(0, 6, "STATE_FULL"),
(14, 32, "STREET_ADDRESS"),
(33, 38, "ZIPCODE"),
(39, 41, "STATE"),
(42, 52, "CITY"),
]
}),
(
"97058 number The Dalles OR 4537 Center Street Oregon"
, {
"entities":[
(0, 5, "ZIPCODE"),
(13, 23, "CITY"),
(24, 26, "STATE"),
(27, 45, "STREET_ADDRESS"),
(46, 52, "STATE_FULL"),
]
}),
(
"OR 97058 4537 Center Street Oregon The Dalles number"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 27, "STREET_ADDRESS"),
(28, 34, "STATE_FULL"),
(35, 45, "CITY"),
]
}),
(
"number OR The Dalles 4537 Center Street 97058 Oregon"
, {
"entities":[
(7, 9, "STATE"),
(10, 20, "CITY"),
(21, 39, "STREET_ADDRESS"),
(40, 45, "ZIPCODE"),
(46, 52, "STATE_FULL"),
]
}),
(
"The Dalles Oregon 4537 Center Street OR number 97058"
, {
"entities":[
(0, 10, "CITY"),
(11, 17, "STATE_FULL"),
(18, 36, "STREET_ADDRESS"),
(37, 39, "STATE"),
(47, 52, "ZIPCODE"),
]
}),
(
"OR Oregon 4537 Center Street number The Dalles 97058"
, {
"entities":[
(0, 2, "STATE"),
(3, 9, "STATE_FULL"),
(10, 28, "STREET_ADDRESS"),
(36, 46, "CITY"),
(47, 52, "ZIPCODE"),
]
}),
(
"number The Dalles Oregon 97058 4537 Center Street OR"
, {
"entities":[
(7, 17, "CITY"),
(18, 24, "STATE_FULL"),
(25, 30, "ZIPCODE"),
(31, 49, "STREET_ADDRESS"),
(50, 52, "STATE"),
]
}),
(
"Fair Oaks 95628 with California CA 110 Frederick Street"
, {
"entities":[
(0, 9, "CITY"),
(10, 15, "ZIPCODE"),
(21, 31, "STATE_FULL"),
(32, 34, "STATE"),
(35, 55, "STREET_ADDRESS"),
]
}),
(
"California CA 110 Frederick Street 95628 Fair Oaks with"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 13, "STATE"),
(14, 34, "STREET_ADDRESS"),
(35, 40, "ZIPCODE"),
(41, 50, "CITY"),
]
}),
(
"with Fair Oaks 95628 California CA 110 Frederick Street"
, {
"entities":[
(5, 14, "CITY"),
(15, 20, "ZIPCODE"),
(21, 31, "STATE_FULL"),
(32, 34, "STATE"),
(35, 55, "STREET_ADDRESS"),
]
}),
(
"CA 95628 110 Frederick Street with Fair Oaks California"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 29, "STREET_ADDRESS"),
(35, 44, "CITY"),
(45, 55, "STATE_FULL"),
]
}),
(
"110 Frederick Street Fair Oaks with CA California 95628"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 30, "CITY"),
(36, 38, "STATE"),
(39, 49, "STATE_FULL"),
(50, 55, "ZIPCODE"),
]
}),
(
"95628 CA 110 Frederick Street with California Fair Oaks"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 29, "STREET_ADDRESS"),
(35, 45, "STATE_FULL"),
(46, 55, "CITY"),
]
}),
(
"California 95628 with Fair Oaks CA 110 Frederick Street"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 16, "ZIPCODE"),
(22, 31, "CITY"),
(32, 34, "STATE"),
(35, 55, "STREET_ADDRESS"),
]
}),
(
"California 95628 110 Frederick Street with CA Fair Oaks"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 16, "ZIPCODE"),
(17, 37, "STREET_ADDRESS"),
(43, 45, "STATE"),
(46, 55, "CITY"),
]
}),
(
"California CA Fair Oaks with 110 Frederick Street 95628"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 13, "STATE"),
(14, 23, "CITY"),
(29, 49, "STREET_ADDRESS"),
(50, 55, "ZIPCODE"),
]
}),
(
"95628 California 110 Frederick Street with CA Fair Oaks"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 16, "STATE_FULL"),
(17, 37, "STREET_ADDRESS"),
(43, 45, "STATE"),
(46, 55, "CITY"),
]
}),
(
"48823 East Lansing 3460 John Avenue Michigan MI"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 18, "CITY"),
(19, 35, "STREET_ADDRESS"),
(36, 44, "STATE_FULL"),
(45, 47, "STATE"),
]
}),
(
"MI 3460 John Avenue East Lansing 48823 Michigan"
, {
"entities":[
(0, 2, "STATE"),
(3, 19, "STREET_ADDRESS"),
(20, 32, "CITY"),
(33, 38, "ZIPCODE"),
(39, 47, "STATE_FULL"),
]
}),
(
"3460 John Avenue MI East Lansing 48823 Michigan"
, {
"entities":[
(0, 16, "STREET_ADDRESS"),
(17, 19, "STATE"),
(20, 32, "CITY"),
(33, 38, "ZIPCODE"),
(39, 47, "STATE_FULL"),
]
}),
(
"East Lansing 48823 Michigan 3460 John Avenue MI"
, {
"entities":[
(0, 12, "CITY"),
(13, 18, "ZIPCODE"),
(19, 27, "STATE_FULL"),
(28, 44, "STREET_ADDRESS"),
(45, 47, "STATE"),
]
}),
(
"Michigan MI 3460 John Avenue East Lansing 48823"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 11, "STATE"),
(12, 28, "STREET_ADDRESS"),
(29, 41, "CITY"),
(42, 47, "ZIPCODE"),
]
}),
(
"48823 3460 John Avenue MI Michigan East Lansing"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 22, "STREET_ADDRESS"),
(23, 25, "STATE"),
(26, 34, "STATE_FULL"),
(35, 47, "CITY"),
]
}),
(
"Michigan East Lansing MI 3460 John Avenue 48823"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 21, "CITY"),
(22, 24, "STATE"),
(25, 41, "STREET_ADDRESS"),
(42, 47, "ZIPCODE"),
]
}),
(
"3460 John Avenue MI Michigan East Lansing 48823"
, {
"entities":[
(0, 16, "STREET_ADDRESS"),
(17, 19, "STATE"),
(20, 28, "STATE_FULL"),
(29, 41, "CITY"),
(42, 47, "ZIPCODE"),
]
}),
(
"48823 MI Michigan East Lansing 3460 John Avenue"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 17, "STATE_FULL"),
(18, 30, "CITY"),
(31, 47, "STREET_ADDRESS"),
]
}),
(
"Michigan East Lansing MI 48823 3460 John Avenue"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 21, "CITY"),
(22, 24, "STATE"),
(25, 30, "ZIPCODE"),
(31, 47, "STREET_ADDRESS"),
]
}),
(
"CA California 4042 Roosevelt Wilson Lane 92376 Rialto Contact"
, {
"entities":[
(0, 2, "STATE"),
(3, 13, "STATE_FULL"),
(14, 40, "STREET_ADDRESS"),
(41, 46, "ZIPCODE"),
(47, 53, "CITY"),
]
}),
(
"4042 Roosevelt Wilson Lane CA 92376 Rialto Contact California"
, {
"entities":[
(0, 26, "STREET_ADDRESS"),
(27, 29, "STATE"),
(30, 35, "ZIPCODE"),
(36, 42, "CITY"),
(51, 61, "STATE_FULL"),
]
}),
(
"California CA Rialto Contact 4042 Roosevelt Wilson Lane 92376"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 13, "STATE"),
(14, 20, "CITY"),
(29, 55, "STREET_ADDRESS"),
(56, 61, "ZIPCODE"),
]
}),
(
"Contact California 92376 CA Rialto 4042 Roosevelt Wilson Lane"
, {
"entities":[
(8, 18, "STATE_FULL"),
(19, 24, "ZIPCODE"),
(25, 27, "STATE"),
(28, 34, "CITY"),
(35, 61, "STREET_ADDRESS"),
]
}),
(
"Contact 92376 CA California Rialto 4042 Roosevelt Wilson Lane"
, {
"entities":[
(8, 13, "ZIPCODE"),
(14, 16, "STATE"),
(17, 27, "STATE_FULL"),
(28, 34, "CITY"),
(35, 61, "STREET_ADDRESS"),
]
}),
(
"CA Rialto California 4042 Roosevelt Wilson Lane Contact 92376"
, {
"entities":[
(0, 2, "STATE"),
(3, 9, "CITY"),
(10, 20, "STATE_FULL"),
(21, 47, "STREET_ADDRESS"),
(56, 61, "ZIPCODE"),
]
}),
(
"California Rialto 4042 Roosevelt Wilson Lane CA 92376 Contact"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 17, "CITY"),
(18, 44, "STREET_ADDRESS"),
(45, 47, "STATE"),
(48, 53, "ZIPCODE"),
]
}),
(
"4042 Roosevelt Wilson Lane Rialto CA Contact California 92376"
, {
"entities":[
(0, 26, "STREET_ADDRESS"),
(27, 33, "CITY"),
(34, 36, "STATE"),
(45, 55, "STATE_FULL"),
(56, 61, "ZIPCODE"),
]
}),
(
"California CA 92376 Rialto Contact 4042 Roosevelt Wilson Lane"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 13, "STATE"),
(14, 19, "ZIPCODE"),
(20, 26, "CITY"),
(35, 61, "STREET_ADDRESS"),
]
}),
(
"Contact 92376 Rialto 4042 Roosevelt Wilson Lane California CA"
, {
"entities":[
(8, 13, "ZIPCODE"),
(14, 20, "CITY"),
(21, 47, "STREET_ADDRESS"),
(48, 58, "STATE_FULL"),
(59, 61, "STATE"),
]
}),
(
"Florida 4781 Woodside Circle FL 32548 Fort Walton Beach"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 28, "STREET_ADDRESS"),
(29, 31, "STATE"),
(32, 37, "ZIPCODE"),
(38, 55, "CITY"),
]
}),
(
"FL 4781 Woodside Circle 32548 Florida Fort Walton Beach"
, {
"entities":[
(0, 2, "STATE"),
(3, 23, "STREET_ADDRESS"),
(24, 29, "ZIPCODE"),
(30, 37, "STATE_FULL"),
(38, 55, "CITY"),
]
}),
(
"Fort Walton Beach 4781 Woodside Circle Florida 32548 FL"
, {
"entities":[
(0, 17, "CITY"),
(18, 38, "STREET_ADDRESS"),
(39, 46, "STATE_FULL"),
(47, 52, "ZIPCODE"),
(53, 55, "STATE"),
]
}),
(
"Florida FL Fort Walton Beach 32548 4781 Woodside Circle"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 10, "STATE"),
(11, 28, "CITY"),
(29, 34, "ZIPCODE"),
(35, 55, "STREET_ADDRESS"),
]
}),
(
"FL 4781 Woodside Circle Fort Walton Beach 32548 Florida"
, {
"entities":[
(0, 2, "STATE"),
(3, 23, "STREET_ADDRESS"),
(24, 41, "CITY"),
(42, 47, "ZIPCODE"),
(48, 55, "STATE_FULL"),
]
}),
(
"4781 Woodside Circle Florida FL 32548 Fort Walton Beach"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 28, "STATE_FULL"),
(29, 31, "STATE"),
(32, 37, "ZIPCODE"),
(38, 55, "CITY"),
]
}),
(
"FL Florida Fort Walton Beach 32548 4781 Woodside Circle"
, {
"entities":[
(0, 2, "STATE"),
(3, 10, "STATE_FULL"),
(11, 28, "CITY"),
(29, 34, "ZIPCODE"),
(35, 55, "STREET_ADDRESS"),
]
}),
(
"Florida 32548 4781 Woodside Circle FL Fort Walton Beach"
, {
"entities":[
(0, 7, "STATE_FULL"),
(8, 13, "ZIPCODE"),
(14, 34, "STREET_ADDRESS"),
(35, 37, "STATE"),
(38, 55, "CITY"),
]
}),
(
"Fort Walton Beach 4781 Woodside Circle Florida FL 32548"
, {
"entities":[
(0, 17, "CITY"),
(18, 38, "STREET_ADDRESS"),
(39, 46, "STATE_FULL"),
(47, 49, "STATE"),
(50, 55, "ZIPCODE"),
]
}),
(
"32548 4781 Woodside Circle FL Florida Fort Walton Beach"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 26, "STREET_ADDRESS"),
(27, 29, "STATE"),
(30, 37, "STATE_FULL"),
(38, 55, "CITY"),
]
}),
(
"14068 NY 3533 Nuzum Court Getzville New York from"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 25, "STREET_ADDRESS"),
(26, 35, "CITY"),
(36, 44, "STATE_FULL"),
]
}),
(
"3533 Nuzum Court NY Getzville 14068 New York from"
, {
"entities":[
(0, 16, "STREET_ADDRESS"),
(17, 19, "STATE"),
(20, 29, "CITY"),
(30, 35, "ZIPCODE"),
(36, 44, "STATE_FULL"),
]
}),
(
"NY 3533 Nuzum Court New York 14068 from Getzville"
, {
"entities":[
(0, 2, "STATE"),
(3, 19, "STREET_ADDRESS"),
(20, 28, "STATE_FULL"),
(29, 34, "ZIPCODE"),
(40, 49, "CITY"),
]
}),
(
"NY from Getzville New York 3533 Nuzum Court 14068"
, {
"entities":[
(0, 2, "STATE"),
(8, 17, "CITY"),
(18, 26, "STATE_FULL"),
(27, 43, "STREET_ADDRESS"),
(44, 49, "ZIPCODE"),
]
}),
(
"3533 Nuzum Court New York from NY Getzville 14068"
, {
"entities":[
(0, 16, "STREET_ADDRESS"),
(17, 25, "STATE_FULL"),
(31, 33, "STATE"),
(34, 43, "CITY"),
(44, 49, "ZIPCODE"),
]
}),
(
"NY New York from 3533 Nuzum Court Getzville 14068"
, {
"entities":[
(0, 2, "STATE"),
(3, 11, "STATE_FULL"),
(17, 33, "STREET_ADDRESS"),
(34, 43, "CITY"),
(44, 49, "ZIPCODE"),
]
}),
(
"3533 Nuzum Court NY from 14068 Getzville New York"
, {
"entities":[
(0, 16, "STREET_ADDRESS"),
(17, 19, "STATE"),
(25, 30, "ZIPCODE"),
(31, 40, "CITY"),
(41, 49, "STATE_FULL"),
]
}),
(
"Getzville NY from New York 14068 3533 Nuzum Court"
, {
"entities":[
(0, 9, "CITY"),
(10, 12, "STATE"),
(18, 26, "STATE_FULL"),
(27, 32, "ZIPCODE"),
(33, 49, "STREET_ADDRESS"),
]
}),
(
"New York 3533 Nuzum Court NY from Getzville 14068"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 25, "STREET_ADDRESS"),
(26, 28, "STATE"),
(34, 43, "CITY"),
(44, 49, "ZIPCODE"),
]
}),
(
"3533 Nuzum Court 14068 Getzville New York NY from"
, {
"entities":[
(0, 16, "STREET_ADDRESS"),
(17, 22, "ZIPCODE"),
(23, 32, "CITY"),
(33, 41, "STATE_FULL"),
(42, 44, "STATE"),
]
}),
(
"Spokane Valley WA 2418 Melrose Street Washington 99206"
, {
"entities":[
(0, 14, "CITY"),
(15, 17, "STATE"),
(18, 37, "STREET_ADDRESS"),
(38, 48, "STATE_FULL"),
(49, 54, "ZIPCODE"),
]
}),
(
"Spokane Valley WA 2418 Melrose Street 99206 Washington"
, {
"entities":[
(0, 14, "CITY"),
(15, 17, "STATE"),
(18, 37, "STREET_ADDRESS"),
(38, 43, "ZIPCODE"),
(44, 54, "STATE_FULL"),
]
}),
(
"WA Spokane Valley 2418 Melrose Street 99206 Washington"
, {
"entities":[
(0, 2, "STATE"),
(3, 17, "CITY"),
(18, 37, "STREET_ADDRESS"),
(38, 43, "ZIPCODE"),
(44, 54, "STATE_FULL"),
]
}),
(
"99206 Washington Spokane Valley WA 2418 Melrose Street"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 16, "STATE_FULL"),
(17, 31, "CITY"),
(32, 34, "STATE"),
(35, 54, "STREET_ADDRESS"),
]
}),
(
"Washington WA 2418 Melrose Street 99206 Spokane Valley"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 13, "STATE"),
(14, 33, "STREET_ADDRESS"),
(34, 39, "ZIPCODE"),
(40, 54, "CITY"),
]
}),
(
"99206 Spokane Valley Washington WA 2418 Melrose Street"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 20, "CITY"),
(21, 31, "STATE_FULL"),
(32, 34, "STATE"),
(35, 54, "STREET_ADDRESS"),
]
}),
(
"2418 Melrose Street WA Spokane Valley Washington 99206"
, {
"entities":[
(0, 19, "STREET_ADDRESS"),
(20, 22, "STATE"),
(23, 37, "CITY"),
(38, 48, "STATE_FULL"),
(49, 54, "ZIPCODE"),
]
}),
(
"WA Spokane Valley Washington 2418 Melrose Street 99206"
, {
"entities":[
(0, 2, "STATE"),
(3, 17, "CITY"),
(18, 28, "STATE_FULL"),
(29, 48, "STREET_ADDRESS"),
(49, 54, "ZIPCODE"),
]
}),
(
"99206 Washington WA Spokane Valley 2418 Melrose Street"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 16, "STATE_FULL"),
(17, 19, "STATE"),
(20, 34, "CITY"),
(35, 54, "STREET_ADDRESS"),
]
}),
(
"2418 Melrose Street Spokane Valley Washington WA 99206"
, {
"entities":[
(0, 19, "STREET_ADDRESS"),
(20, 34, "CITY"),
(35, 45, "STATE_FULL"),
(46, 48, "STATE"),
(49, 54, "ZIPCODE"),
]
}),
(
"976 Worthington Drive Irving TX 75061 Texas"
, {
"entities":[
(0, 21, "STREET_ADDRESS"),
(22, 28, "CITY"),
(29, 31, "STATE"),
(32, 37, "ZIPCODE"),
(38, 43, "STATE_FULL"),
]
}),
(
"75061 TX Texas 976 Worthington Drive Irving"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 14, "STATE_FULL"),
(15, 36, "STREET_ADDRESS"),
(37, 43, "CITY"),
]
}),
(
"Texas 75061 TX 976 Worthington Drive Irving"
, {
"entities":[
(0, 5, "STATE_FULL"),
(6, 11, "ZIPCODE"),
(12, 14, "STATE"),
(15, 36, "STREET_ADDRESS"),
(37, 43, "CITY"),
]
}),
(
"Texas Irving TX 976 Worthington Drive 75061"
, {
"entities":[
(0, 5, "STATE_FULL"),
(6, 12, "CITY"),
(13, 15, "STATE"),
(16, 37, "STREET_ADDRESS"),
(38, 43, "ZIPCODE"),
]
}),
(
"75061 TX Irving 976 Worthington Drive Texas"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 15, "CITY"),
(16, 37, "STREET_ADDRESS"),
(38, 43, "STATE_FULL"),
]
}),
(
"75061 TX Irving Texas 976 Worthington Drive"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 15, "CITY"),
(16, 21, "STATE_FULL"),
(22, 43, "STREET_ADDRESS"),
]
}),
(
"976 Worthington Drive Texas 75061 TX Irving"
, {
"entities":[
(0, 21, "STREET_ADDRESS"),
(22, 27, "STATE_FULL"),
(28, 33, "ZIPCODE"),
(34, 36, "STATE"),
(37, 43, "CITY"),
]
}),
(
"Texas 75061 TX 976 Worthington Drive Irving"
, {
"entities":[
(0, 5, "STATE_FULL"),
(6, 11, "ZIPCODE"),
(12, 14, "STATE"),
(15, 36, "STREET_ADDRESS"),
(37, 43, "CITY"),
]
}),
(
"75061 Texas Irving TX 976 Worthington Drive"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 11, "STATE_FULL"),
(12, 18, "CITY"),
(19, 21, "STATE"),
(22, 43, "STREET_ADDRESS"),
]
}),
(
"75061 976 Worthington Drive TX Texas Irving"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 27, "STREET_ADDRESS"),
(28, 30, "STATE"),
(31, 36, "STATE_FULL"),
(37, 43, "CITY"),
]
}),
(
"27406 NC 3442 Havanna Street North Carolina Greensboro"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 28, "STREET_ADDRESS"),
(29, 43, "STATE_FULL"),
(44, 54, "CITY"),
]
}),
(
"North Carolina 3442 Havanna Street Greensboro 27406 NC"
, {
"entities":[
(0, 14, "STATE_FULL"),
(15, 34, "STREET_ADDRESS"),
(35, 45, "CITY"),
(46, 51, "ZIPCODE"),
(52, 54, "STATE"),
]
}),
(
"North Carolina 27406 NC 3442 Havanna Street Greensboro"
, {
"entities":[
(0, 14, "STATE_FULL"),
(15, 20, "ZIPCODE"),
(21, 23, "STATE"),
(24, 43, "STREET_ADDRESS"),
(44, 54, "CITY"),
]
}),
(
"NC Greensboro 3442 Havanna Street North Carolina 27406"
, {
"entities":[
(0, 2, "STATE"),
(3, 13, "CITY"),
(14, 33, "STREET_ADDRESS"),
(34, 48, "STATE_FULL"),
(49, 54, "ZIPCODE"),
]
}),
(
"3442 Havanna Street 27406 NC North Carolina Greensboro"
, {
"entities":[
(0, 19, "STREET_ADDRESS"),
(20, 25, "ZIPCODE"),
(26, 28, "STATE"),
(29, 43, "STATE_FULL"),
(44, 54, "CITY"),
]
}),
(
"NC Greensboro 3442 Havanna Street North Carolina 27406"
, {
"entities":[
(0, 2, "STATE"),
(3, 13, "CITY"),
(14, 33, "STREET_ADDRESS"),
(34, 48, "STATE_FULL"),
(49, 54, "ZIPCODE"),
]
}),
(
"NC Greensboro 3442 Havanna Street North Carolina 27406"
, {
"entities":[
(0, 2, "STATE"),
(3, 13, "CITY"),
(14, 33, "STREET_ADDRESS"),
(34, 48, "STATE_FULL"),
(49, 54, "ZIPCODE"),
]
}),
(
"Greensboro 27406 3442 Havanna Street NC North Carolina"
, {
"entities":[
(0, 10, "CITY"),
(11, 16, "ZIPCODE"),
(17, 36, "STREET_ADDRESS"),
(37, 39, "STATE"),
(40, 54, "STATE_FULL"),
]
}),
(
"North Carolina 3442 Havanna Street NC 27406 Greensboro"
, {
"entities":[
(0, 14, "STATE_FULL"),
(15, 34, "STREET_ADDRESS"),
(35, 37, "STATE"),
(38, 43, "ZIPCODE"),
(44, 54, "CITY"),
]
}),
(
"NC North Carolina 3442 Havanna Street Greensboro 27406"
, {
"entities":[
(0, 2, "STATE"),
(3, 17, "STATE_FULL"),
(18, 37, "STREET_ADDRESS"),
(38, 48, "CITY"),
(49, 54, "ZIPCODE"),
]
}),
(
"4715 Russell Street MA Cambridge Massachusetts 02141"
, {
"entities":[
(0, 19, "STREET_ADDRESS"),
(20, 22, "STATE"),
(23, 32, "CITY"),
(33, 46, "STATE_FULL"),
(47, 52, "ZIPCODE"),
]
}),
(
"Cambridge Massachusetts 4715 Russell Street 02141 MA"
, {
"entities":[
(0, 9, "CITY"),
(10, 23, "STATE_FULL"),
(24, 43, "STREET_ADDRESS"),
(44, 49, "ZIPCODE"),
(50, 52, "STATE"),
]
}),
(
"Cambridge 02141 MA Massachusetts 4715 Russell Street"
, {
"entities":[
(0, 9, "CITY"),
(10, 15, "ZIPCODE"),
(16, 18, "STATE"),
(19, 32, "STATE_FULL"),
(33, 52, "STREET_ADDRESS"),
]
}),
(
"4715 Russell Street 02141 MA Cambridge Massachusetts"
, {
"entities":[
(0, 19, "STREET_ADDRESS"),
(20, 25, "ZIPCODE"),
(26, 28, "STATE"),
(29, 38, "CITY"),
(39, 52, "STATE_FULL"),
]
}),
(
"Massachusetts Cambridge 02141 4715 Russell Street MA"
, {
"entities":[
(0, 13, "STATE_FULL"),
(14, 23, "CITY"),
(24, 29, "ZIPCODE"),
(30, 49, "STREET_ADDRESS"),
(50, 52, "STATE"),
]
}),
(
"4715 Russell Street MA Cambridge Massachusetts 02141"
, {
"entities":[
(0, 19, "STREET_ADDRESS"),
(20, 22, "STATE"),
(23, 32, "CITY"),
(33, 46, "STATE_FULL"),
(47, 52, "ZIPCODE"),
]
}),
(
"02141 MA 4715 Russell Street Cambridge Massachusetts"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 28, "STREET_ADDRESS"),
(29, 38, "CITY"),
(39, 52, "STATE_FULL"),
]
}),
(
"MA Massachusetts 4715 Russell Street 02141 Cambridge"
, {
"entities":[
(0, 2, "STATE"),
(3, 16, "STATE_FULL"),
(17, 36, "STREET_ADDRESS"),
(37, 42, "ZIPCODE"),
(43, 52, "CITY"),
]
}),
(
"Massachusetts Cambridge 4715 Russell Street 02141 MA"
, {
"entities":[
(0, 13, "STATE_FULL"),
(14, 23, "CITY"),
(24, 43, "STREET_ADDRESS"),
(44, 49, "ZIPCODE"),
(50, 52, "STATE"),
]
}),
(
"Massachusetts 02141 MA 4715 Russell Street Cambridge"
, {
"entities":[
(0, 13, "STATE_FULL"),
(14, 19, "ZIPCODE"),
(20, 22, "STATE"),
(23, 42, "STREET_ADDRESS"),
(43, 52, "CITY"),
]
}),
(
"OH 43602 Toledo Ohio 3225 Olive Street"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 15, "CITY"),
(16, 20, "STATE_FULL"),
(21, 38, "STREET_ADDRESS"),
]
}),
(
"43602 OH Ohio 3225 Olive Street Toledo"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 13, "STATE_FULL"),
(14, 31, "STREET_ADDRESS"),
(32, 38, "CITY"),
]
}),
(
"Toledo 3225 Olive Street Ohio 43602 OH"
, {
"entities":[
(0, 6, "CITY"),
(7, 24, "STREET_ADDRESS"),
(25, 29, "STATE_FULL"),
(30, 35, "ZIPCODE"),
(36, 38, "STATE"),
]
}),
(
"OH Toledo 43602 Ohio 3225 Olive Street"
, {
"entities":[
(0, 2, "STATE"),
(3, 9, "CITY"),
(10, 15, "ZIPCODE"),
(16, 20, "STATE_FULL"),
(21, 38, "STREET_ADDRESS"),
]
}),
(
"43602 3225 Olive Street OH Ohio Toledo"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 23, "STREET_ADDRESS"),
(24, 26, "STATE"),
(27, 31, "STATE_FULL"),
(32, 38, "CITY"),
]
}),
(
"Toledo 43602 OH Ohio 3225 Olive Street"
, {
"entities":[
(0, 6, "CITY"),
(7, 12, "ZIPCODE"),
(13, 15, "STATE"),
(16, 20, "STATE_FULL"),
(21, 38, "STREET_ADDRESS"),
]
}),
(
"Ohio 43602 3225 Olive Street OH Toledo"
, {
"entities":[
(0, 4, "STATE_FULL"),
(5, 10, "ZIPCODE"),
(11, 28, "STREET_ADDRESS"),
(29, 31, "STATE"),
(32, 38, "CITY"),
]
}),
(
"Ohio 43602 OH 3225 Olive Street Toledo"
, {
"entities":[
(0, 4, "STATE_FULL"),
(5, 10, "ZIPCODE"),
(11, 13, "STATE"),
(14, 31, "STREET_ADDRESS"),
(32, 38, "CITY"),
]
}),
(
"3225 Olive Street 43602 OH Toledo Ohio"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 23, "ZIPCODE"),
(24, 26, "STATE"),
(27, 33, "CITY"),
(34, 38, "STATE_FULL"),
]
}),
(
"43602 OH Ohio 3225 Olive Street Toledo"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 13, "STATE_FULL"),
(14, 31, "STREET_ADDRESS"),
(32, 38, "CITY"),
]
}),
(
"1692 Bridge Avenue 70583 LA Louisiana Scott"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 24, "ZIPCODE"),
(25, 27, "STATE"),
(28, 37, "STATE_FULL"),
(38, 43, "CITY"),
]
}),
(
"Louisiana LA 1692 Bridge Avenue 70583 Scott"
, {
"entities":[
(0, 9, "STATE_FULL"),
(10, 12, "STATE"),
(13, 31, "STREET_ADDRESS"),
(32, 37, "ZIPCODE"),
(38, 43, "CITY"),
]
}),
(
"LA 1692 Bridge Avenue Louisiana 70583 Scott"
, {
"entities":[
(0, 2, "STATE"),
(3, 21, "STREET_ADDRESS"),
(22, 31, "STATE_FULL"),
(32, 37, "ZIPCODE"),
(38, 43, "CITY"),
]
}),
(
"70583 Louisiana Scott 1692 Bridge Avenue LA"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 15, "STATE_FULL"),
(16, 21, "CITY"),
(22, 40, "STREET_ADDRESS"),
(41, 43, "STATE"),
]
}),
(
"LA 70583 1692 Bridge Avenue Louisiana Scott"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 27, "STREET_ADDRESS"),
(28, 37, "STATE_FULL"),
(38, 43, "CITY"),
]
}),
(
"70583 Louisiana 1692 Bridge Avenue Scott LA"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 15, "STATE_FULL"),
(16, 34, "STREET_ADDRESS"),
(35, 40, "CITY"),
(41, 43, "STATE"),
]
}),
(
"Scott 70583 Louisiana LA 1692 Bridge Avenue"
, {
"entities":[
(0, 5, "CITY"),
(6, 11, "ZIPCODE"),
(12, 21, "STATE_FULL"),
(22, 24, "STATE"),
(25, 43, "STREET_ADDRESS"),
]
}),
(
"LA 1692 Bridge Avenue Scott Louisiana 70583"
, {
"entities":[
(0, 2, "STATE"),
(3, 21, "STREET_ADDRESS"),
(22, 27, "CITY"),
(28, 37, "STATE_FULL"),
(38, 43, "ZIPCODE"),
]
}),
(
"Louisiana Scott 1692 Bridge Avenue 70583 LA"
, {
"entities":[
(0, 9, "STATE_FULL"),
(10, 15, "CITY"),
(16, 34, "STREET_ADDRESS"),
(35, 40, "ZIPCODE"),
(41, 43, "STATE"),
]
}),
(
"Scott 70583 1692 Bridge Avenue Louisiana LA"
, {
"entities":[
(0, 5, "CITY"),
(6, 11, "ZIPCODE"),
(12, 30, "STREET_ADDRESS"),
(31, 40, "STATE_FULL"),
(41, 43, "STATE"),
]
}),
(
"San Diego 92123 4295 Pike Street CA California"
, {
"entities":[
(0, 9, "CITY"),
(10, 15, "ZIPCODE"),
(16, 32, "STREET_ADDRESS"),
(33, 35, "STATE"),
(36, 46, "STATE_FULL"),
]
}),
(
"92123 San Diego 4295 Pike Street CA California"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 15, "CITY"),
(16, 32, "STREET_ADDRESS"),
(33, 35, "STATE"),
(36, 46, "STATE_FULL"),
]
}),
(
"CA 92123 California San Diego 4295 Pike Street"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 19, "STATE_FULL"),
(20, 29, "CITY"),
(30, 46, "STREET_ADDRESS"),
]
}),
(
"CA 92123 4295 Pike Street California San Diego"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 25, "STREET_ADDRESS"),
(26, 36, "STATE_FULL"),
(37, 46, "CITY"),
]
}),
(
"San Diego 92123 4295 Pike Street California CA"
, {
"entities":[
(0, 9, "CITY"),
(10, 15, "ZIPCODE"),
(16, 32, "STREET_ADDRESS"),
(33, 43, "STATE_FULL"),
(44, 46, "STATE"),
]
}),
(
"San Diego 4295 Pike Street California 92123 CA"
, {
"entities":[
(0, 9, "CITY"),
(10, 26, "STREET_ADDRESS"),
(27, 37, "STATE_FULL"),
(38, 43, "ZIPCODE"),
(44, 46, "STATE"),
]
}),
(
"92123 California CA San Diego 4295 Pike Street"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 16, "STATE_FULL"),
(17, 19, "STATE"),
(20, 29, "CITY"),
(30, 46, "STREET_ADDRESS"),
]
}),
(
"92123 San Diego CA California 4295 Pike Street"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 15, "CITY"),
(16, 18, "STATE"),
(19, 29, "STATE_FULL"),
(30, 46, "STREET_ADDRESS"),
]
}),
(
"CA 92123 4295 Pike Street San Diego California"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 25, "STREET_ADDRESS"),
(26, 35, "CITY"),
(36, 46, "STATE_FULL"),
]
}),
(
"California San Diego 4295 Pike Street CA 92123"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 20, "CITY"),
(21, 37, "STREET_ADDRESS"),
(38, 40, "STATE"),
(41, 46, "ZIPCODE"),
]
}),
(
"for House Springs 4773 Rodney Street 63051 Missouri MO"
, {
"entities":[
(4, 17, "CITY"),
(18, 36, "STREET_ADDRESS"),
(37, 42, "ZIPCODE"),
(43, 51, "STATE_FULL"),
(52, 54, "STATE"),
]
}),
(
"MO for House Springs 63051 Missouri 4773 Rodney Street"
, {
"entities":[
(0, 2, "STATE"),
(7, 20, "CITY"),
(21, 26, "ZIPCODE"),
(27, 35, "STATE_FULL"),
(36, 54, "STREET_ADDRESS"),
]
}),
(
"MO Missouri 4773 Rodney Street for 63051 House Springs"
, {
"entities":[
(0, 2, "STATE"),
(3, 11, "STATE_FULL"),
(12, 30, "STREET_ADDRESS"),
(35, 40, "ZIPCODE"),
(41, 54, "CITY"),
]
}),
(
"4773 Rodney Street for 63051 MO Missouri House Springs"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(23, 28, "ZIPCODE"),
(29, 31, "STATE"),
(32, 40, "STATE_FULL"),
(41, 54, "CITY"),
]
}),
(
"63051 House Springs 4773 Rodney Street for Missouri MO"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 19, "CITY"),
(20, 38, "STREET_ADDRESS"),
(43, 51, "STATE_FULL"),
(52, 54, "STATE"),
]
}),
(
"for 63051 4773 Rodney Street Missouri House Springs MO"
, {
"entities":[
(4, 9, "ZIPCODE"),
(10, 28, "STREET_ADDRESS"),
(29, 37, "STATE_FULL"),
(38, 51, "CITY"),
(52, 54, "STATE"),
]
}),
(
"63051 House Springs 4773 Rodney Street Missouri for MO"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 19, "CITY"),
(20, 38, "STREET_ADDRESS"),
(39, 47, "STATE_FULL"),
(52, 54, "STATE"),
]
}),
(
"for Missouri 63051 House Springs MO 4773 Rodney Street"
, {
"entities":[
(4, 12, "STATE_FULL"),
(13, 18, "ZIPCODE"),
(19, 32, "CITY"),
(33, 35, "STATE"),
(36, 54, "STREET_ADDRESS"),
]
}),
(
"Missouri House Springs 63051 MO 4773 Rodney Street for"
, {
"entities":[
(0, 8, "STATE_FULL"),
(9, 22, "CITY"),
(23, 28, "ZIPCODE"),
(29, 31, "STATE"),
(32, 50, "STREET_ADDRESS"),
]
}),
(
"MO 4773 Rodney Street Missouri for 63051 House Springs"
, {
"entities":[
(0, 2, "STATE"),
(3, 21, "STREET_ADDRESS"),
(22, 30, "STATE_FULL"),
(35, 40, "ZIPCODE"),
(41, 54, "CITY"),
]
}),
(
"1408 Brownton Road Mississippi MS USE Starkville 39759"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 30, "STATE_FULL"),
(31, 33, "STATE"),
(38, 48, "CITY"),
(49, 54, "ZIPCODE"),
]
}),
(
"MS Mississippi 1408 Brownton Road 39759 USE Starkville"
, {
"entities":[
(0, 2, "STATE"),
(3, 14, "STATE_FULL"),
(15, 33, "STREET_ADDRESS"),
(34, 39, "ZIPCODE"),
(44, 54, "CITY"),
]
}),
(
"1408 Brownton Road Starkville MS USE Mississippi 39759"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 29, "CITY"),
(30, 32, "STATE"),
(37, 48, "STATE_FULL"),
(49, 54, "ZIPCODE"),
]
}),
(
"Starkville 39759 MS USE 1408 Brownton Road Mississippi"
, {
"entities":[
(0, 10, "CITY"),
(11, 16, "ZIPCODE"),
(17, 19, "STATE"),
(24, 42, "STREET_ADDRESS"),
(43, 54, "STATE_FULL"),
]
}),
(
"1408 Brownton Road Mississippi 39759 USE Starkville MS"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 30, "STATE_FULL"),
(31, 36, "ZIPCODE"),
(41, 51, "CITY"),
(52, 54, "STATE"),
]
}),
(
"USE MS 1408 Brownton Road Starkville 39759 Mississippi"
, {
"entities":[
(4, 6, "STATE"),
(7, 25, "STREET_ADDRESS"),
(26, 36, "CITY"),
(37, 42, "ZIPCODE"),
(43, 54, "STATE_FULL"),
]
}),
(
"Mississippi MS 39759 Starkville USE 1408 Brownton Road"
, {
"entities":[
(0, 11, "STATE_FULL"),
(12, 14, "STATE"),
(15, 20, "ZIPCODE"),
(21, 31, "CITY"),
(36, 54, "STREET_ADDRESS"),
]
}),
(
"1408 Brownton Road USE MS 39759 Starkville Mississippi"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(23, 25, "STATE"),
(26, 31, "ZIPCODE"),
(32, 42, "CITY"),
(43, 54, "STATE_FULL"),
]
}),
(
"Starkville MS 39759 USE Mississippi 1408 Brownton Road"
, {
"entities":[
(0, 10, "CITY"),
(11, 13, "STATE"),
(14, 19, "ZIPCODE"),
(24, 35, "STATE_FULL"),
(36, 54, "STREET_ADDRESS"),
]
}),
(
"Mississippi USE Starkville 39759 MS 1408 Brownton Road"
, {
"entities":[
(0, 11, "STATE_FULL"),
(16, 26, "CITY"),
(27, 32, "ZIPCODE"),
(33, 35, "STATE"),
(36, 54, "STREET_ADDRESS"),
]
}),
(
"95814 CA Sacramento California 2171 Timber Ridge Road"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 19, "CITY"),
(20, 30, "STATE_FULL"),
(31, 53, "STREET_ADDRESS"),
]
}),
(
"95814 CA 2171 Timber Ridge Road Sacramento California"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 31, "STREET_ADDRESS"),
(32, 42, "CITY"),
(43, 53, "STATE_FULL"),
]
}),
(
"CA 95814 California Sacramento 2171 Timber Ridge Road"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 19, "STATE_FULL"),
(20, 30, "CITY"),
(31, 53, "STREET_ADDRESS"),
]
}),
(
"Sacramento 2171 Timber Ridge Road CA California 95814"
, {
"entities":[
(0, 10, "CITY"),
(11, 33, "STREET_ADDRESS"),
(34, 36, "STATE"),
(37, 47, "STATE_FULL"),
(48, 53, "ZIPCODE"),
]
}),
(
"95814 CA 2171 Timber Ridge Road Sacramento California"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 31, "STREET_ADDRESS"),
(32, 42, "CITY"),
(43, 53, "STATE_FULL"),
]
}),
(
"CA 2171 Timber Ridge Road California 95814 Sacramento"
, {
"entities":[
(0, 2, "STATE"),
(3, 25, "STREET_ADDRESS"),
(26, 36, "STATE_FULL"),
(37, 42, "ZIPCODE"),
(43, 53, "CITY"),
]
}),
(
"Sacramento 95814 California 2171 Timber Ridge Road CA"
, {
"entities":[
(0, 10, "CITY"),
(11, 16, "ZIPCODE"),
(17, 27, "STATE_FULL"),
(28, 50, "STREET_ADDRESS"),
(51, 53, "STATE"),
]
}),
(
"Sacramento 95814 California CA 2171 Timber Ridge Road"
, {
"entities":[
(0, 10, "CITY"),
(11, 16, "ZIPCODE"),
(17, 27, "STATE_FULL"),
(28, 30, "STATE"),
(31, 53, "STREET_ADDRESS"),
]
}),
(
"CA California 95814 2171 Timber Ridge Road Sacramento"
, {
"entities":[
(0, 2, "STATE"),
(3, 13, "STATE_FULL"),
(14, 19, "ZIPCODE"),
(20, 42, "STREET_ADDRESS"),
(43, 53, "CITY"),
]
}),
(
"California Sacramento CA 95814 2171 Timber Ridge Road"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 21, "CITY"),
(22, 24, "STATE"),
(25, 30, "ZIPCODE"),
(31, 53, "STREET_ADDRESS"),
]
}),
(
"4371 Caynor Circle Contact New Jersey NJ Piscataway 08854"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(27, 37, "STATE_FULL"),
(38, 40, "STATE"),
(41, 51, "CITY"),
(52, 57, "ZIPCODE"),
]
}),
(
"08854 4371 Caynor Circle Piscataway NJ Contact New Jersey"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 24, "STREET_ADDRESS"),
(25, 35, "CITY"),
(36, 38, "STATE"),
(47, 57, "STATE_FULL"),
]
}),
(
"New Jersey Piscataway Contact 4371 Caynor Circle 08854 NJ"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 21, "CITY"),
(30, 48, "STREET_ADDRESS"),
(49, 54, "ZIPCODE"),
(55, 57, "STATE"),
]
}),
(
"New Jersey NJ 4371 Caynor Circle 08854 Piscataway Contact"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 13, "STATE"),
(14, 32, "STREET_ADDRESS"),
(33, 38, "ZIPCODE"),
(39, 49, "CITY"),
]
}),
(
"NJ Piscataway Contact New Jersey 08854 4371 Caynor Circle"
, {
"entities":[
(0, 2, "STATE"),
(3, 13, "CITY"),
(22, 32, "STATE_FULL"),
(33, 38, "ZIPCODE"),
(39, 57, "STREET_ADDRESS"),
]
}),
(
"New Jersey Piscataway 08854 4371 Caynor Circle Contact NJ"
, {
"entities":[
(0, 10, "STATE_FULL"),
(11, 21, "CITY"),
(22, 27, "ZIPCODE"),
(28, 46, "STREET_ADDRESS"),
(55, 57, "STATE"),
]
}),
(
"08854 New Jersey NJ Piscataway 4371 Caynor Circle Contact"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 16, "STATE_FULL"),
(17, 19, "STATE"),
(20, 30, "CITY"),
(31, 49, "STREET_ADDRESS"),
]
}),
(
"Contact New Jersey 4371 Caynor Circle Piscataway NJ 08854"
, {
"entities":[
(8, 18, "STATE_FULL"),
(19, 37, "STREET_ADDRESS"),
(38, 48, "CITY"),
(49, 51, "STATE"),
(52, 57, "ZIPCODE"),
]
}),
(
"New Jersey Contact 08854 Piscataway 4371 Caynor Circle NJ"
, {
"entities":[
(0, 10, "STATE_FULL"),
(19, 24, "ZIPCODE"),
(25, 35, "CITY"),
(36, 54, "STREET_ADDRESS"),
(55, 57, "STATE"),
]
}),
(
"NJ 4371 Caynor Circle Piscataway New Jersey Contact 08854"
, {
"entities":[
(0, 2, "STATE"),
(3, 21, "STREET_ADDRESS"),
(22, 32, "CITY"),
(33, 43, "STATE_FULL"),
(52, 57, "ZIPCODE"),
]
}),
(
"3608 Rogers Street OH 45202 Ohio Cincinnati"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 21, "STATE"),
(22, 27, "ZIPCODE"),
(28, 32, "STATE_FULL"),
(33, 43, "CITY"),
]
}),
(
"Cincinnati Ohio OH 45202 3608 Rogers Street"
, {
"entities":[
(0, 10, "CITY"),
(11, 15, "STATE_FULL"),
(16, 18, "STATE"),
(19, 24, "ZIPCODE"),
(25, 43, "STREET_ADDRESS"),
]
}),
(
"OH Cincinnati Ohio 3608 Rogers Street 45202"
, {
"entities":[
(0, 2, "STATE"),
(3, 13, "CITY"),
(14, 18, "STATE_FULL"),
(19, 37, "STREET_ADDRESS"),
(38, 43, "ZIPCODE"),
]
}),
(
"Cincinnati Ohio 3608 Rogers Street OH 45202"
, {
"entities":[
(0, 10, "CITY"),
(11, 15, "STATE_FULL"),
(16, 34, "STREET_ADDRESS"),
(35, 37, "STATE"),
(38, 43, "ZIPCODE"),
]
}),
(
"45202 OH Cincinnati 3608 Rogers Street Ohio"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 19, "CITY"),
(20, 38, "STREET_ADDRESS"),
(39, 43, "STATE_FULL"),
]
}),
(
"3608 Rogers Street Ohio Cincinnati OH 45202"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 23, "STATE_FULL"),
(24, 34, "CITY"),
(35, 37, "STATE"),
(38, 43, "ZIPCODE"),
]
}),
(
"3608 Rogers Street Cincinnati 45202 OH Ohio"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 29, "CITY"),
(30, 35, "ZIPCODE"),
(36, 38, "STATE"),
(39, 43, "STATE_FULL"),
]
}),
(
"Ohio 45202 Cincinnati OH 3608 Rogers Street"
, {
"entities":[
(0, 4, "STATE_FULL"),
(5, 10, "ZIPCODE"),
(11, 21, "CITY"),
(22, 24, "STATE"),
(25, 43, "STREET_ADDRESS"),
]
}),
(
"Cincinnati OH 3608 Rogers Street 45202 Ohio"
, {
"entities":[
(0, 10, "CITY"),
(11, 13, "STATE"),
(14, 32, "STREET_ADDRESS"),
(33, 38, "ZIPCODE"),
(39, 43, "STATE_FULL"),
]
}),
(
"3608 Rogers Street 45202 Cincinnati Ohio OH"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 24, "ZIPCODE"),
(25, 35, "CITY"),
(36, 40, "STATE_FULL"),
(41, 43, "STATE"),
]
}),
(
"88310 1135 Waterview Lane New Mexico NM Alamogordo"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 25, "STREET_ADDRESS"),
(26, 36, "STATE_FULL"),
(37, 39, "STATE"),
(40, 50, "CITY"),
]
}),
(
"88310 New Mexico NM Alamogordo 1135 Waterview Lane"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 16, "STATE_FULL"),
(17, 19, "STATE"),
(20, 30, "CITY"),
(31, 50, "STREET_ADDRESS"),
]
}),
(
"Alamogordo NM 88310 1135 Waterview Lane New Mexico"
, {
"entities":[
(0, 10, "CITY"),
(11, 13, "STATE"),
(14, 19, "ZIPCODE"),
(20, 39, "STREET_ADDRESS"),
(40, 50, "STATE_FULL"),
]
}),
(
"88310 New Mexico 1135 Waterview Lane NM Alamogordo"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 16, "STATE_FULL"),
(17, 36, "STREET_ADDRESS"),
(37, 39, "STATE"),
(40, 50, "CITY"),
]
}),
(
"NM 88310 New Mexico Alamogordo 1135 Waterview Lane"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 19, "STATE_FULL"),
(20, 30, "CITY"),
(31, 50, "STREET_ADDRESS"),
]
}),
(
"NM Alamogordo New Mexico 88310 1135 Waterview Lane"
, {
"entities":[
(0, 2, "STATE"),
(3, 13, "CITY"),
(14, 24, "STATE_FULL"),
(25, 30, "ZIPCODE"),
(31, 50, "STREET_ADDRESS"),
]
}),
(
"Alamogordo 88310 New Mexico 1135 Waterview Lane NM"
, {
"entities":[
(0, 10, "CITY"),
(11, 16, "ZIPCODE"),
(17, 27, "STATE_FULL"),
(28, 47, "STREET_ADDRESS"),
(48, 50, "STATE"),
]
}),
(
"NM New Mexico 88310 Alamogordo 1135 Waterview Lane"
, {
"entities":[
(0, 2, "STATE"),
(3, 13, "STATE_FULL"),
(14, 19, "ZIPCODE"),
(20, 30, "CITY"),
(31, 50, "STREET_ADDRESS"),
]
}),
(
"Alamogordo NM New Mexico 88310 1135 Waterview Lane"
, {
"entities":[
(0, 10, "CITY"),
(11, 13, "STATE"),
(14, 24, "STATE_FULL"),
(25, 30, "ZIPCODE"),
(31, 50, "STREET_ADDRESS"),
]
}),
(
"88310 Alamogordo NM New Mexico 1135 Waterview Lane"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 16, "CITY"),
(17, 19, "STATE"),
(20, 30, "STATE_FULL"),
(31, 50, "STREET_ADDRESS"),
]
}),
(
"LA 71457 Natchitoches Louisiana 195 Roguski Road"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 21, "CITY"),
(22, 31, "STATE_FULL"),
(32, 48, "STREET_ADDRESS"),
]
}),
(
"Louisiana 71457 LA Natchitoches 195 Roguski Road"
, {
"entities":[
(0, 9, "STATE_FULL"),
(10, 15, "ZIPCODE"),
(16, 18, "STATE"),
(19, 31, "CITY"),
(32, 48, "STREET_ADDRESS"),
]
}),
(
"195 Roguski Road LA Natchitoches Louisiana 71457"
, {
"entities":[
(0, 16, "STREET_ADDRESS"),
(17, 19, "STATE"),
(20, 32, "CITY"),
(33, 42, "STATE_FULL"),
(43, 48, "ZIPCODE"),
]
}),
(
"195 Roguski Road LA Louisiana Natchitoches 71457"
, {
"entities":[
(0, 16, "STREET_ADDRESS"),
(17, 19, "STATE"),
(20, 29, "STATE_FULL"),
(30, 42, "CITY"),
(43, 48, "ZIPCODE"),
]
}),
(
"LA Louisiana Natchitoches 71457 195 Roguski Road"
, {
"entities":[
(0, 2, "STATE"),
(3, 12, "STATE_FULL"),
(13, 25, "CITY"),
(26, 31, "ZIPCODE"),
(32, 48, "STREET_ADDRESS"),
]
}),
(
"195 Roguski Road Louisiana LA 71457 Natchitoches"
, {
"entities":[
(0, 16, "STREET_ADDRESS"),
(17, 26, "STATE_FULL"),
(27, 29, "STATE"),
(30, 35, "ZIPCODE"),
(36, 48, "CITY"),
]
}),
(
"71457 Louisiana 195 Roguski Road Natchitoches LA"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 15, "STATE_FULL"),
(16, 32, "STREET_ADDRESS"),
(33, 45, "CITY"),
(46, 48, "STATE"),
]
}),
(
"LA 195 Roguski Road Natchitoches Louisiana 71457"
, {
"entities":[
(0, 2, "STATE"),
(3, 19, "STREET_ADDRESS"),
(20, 32, "CITY"),
(33, 42, "STATE_FULL"),
(43, 48, "ZIPCODE"),
]
}),
(
"Natchitoches 195 Roguski Road 71457 Louisiana LA"
, {
"entities":[
(0, 12, "CITY"),
(13, 29, "STREET_ADDRESS"),
(30, 35, "ZIPCODE"),
(36, 45, "STATE_FULL"),
(46, 48, "STATE"),
]
}),
(
"LA Natchitoches Louisiana 195 Roguski Road 71457"
, {
"entities":[
(0, 2, "STATE"),
(3, 15, "CITY"),
(16, 25, "STATE_FULL"),
(26, 42, "STREET_ADDRESS"),
(43, 48, "ZIPCODE"),
]
}),
(
"75051 TX 3779 Worthington Drive Grand Prairie Texas"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 31, "STREET_ADDRESS"),
(32, 45, "CITY"),
(46, 51, "STATE_FULL"),
]
}),
(
"Grand Prairie Texas TX 75051 3779 Worthington Drive"
, {
"entities":[
(0, 13, "CITY"),
(14, 19, "STATE_FULL"),
(20, 22, "STATE"),
(23, 28, "ZIPCODE"),
(29, 51, "STREET_ADDRESS"),
]
}),
(
"Texas Grand Prairie 75051 3779 Worthington Drive TX"
, {
"entities":[
(0, 5, "STATE_FULL"),
(6, 19, "CITY"),
(20, 25, "ZIPCODE"),
(26, 48, "STREET_ADDRESS"),
(49, 51, "STATE"),
]
}),
(
"3779 Worthington Drive Texas Grand Prairie TX 75051"
, {
"entities":[
(0, 22, "STREET_ADDRESS"),
(23, 28, "STATE_FULL"),
(29, 42, "CITY"),
(43, 45, "STATE"),
(46, 51, "ZIPCODE"),
]
}),
(
"TX 75051 3779 Worthington Drive Grand Prairie Texas"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 31, "STREET_ADDRESS"),
(32, 45, "CITY"),
(46, 51, "STATE_FULL"),
]
}),
(
"3779 Worthington Drive Grand Prairie 75051 Texas TX"
, {
"entities":[
(0, 22, "STREET_ADDRESS"),
(23, 36, "CITY"),
(37, 42, "ZIPCODE"),
(43, 48, "STATE_FULL"),
(49, 51, "STATE"),
]
}),
(
"3779 Worthington Drive Grand Prairie 75051 Texas TX"
, {
"entities":[
(0, 22, "STREET_ADDRESS"),
(23, 36, "CITY"),
(37, 42, "ZIPCODE"),
(43, 48, "STATE_FULL"),
(49, 51, "STATE"),
]
}),
(
"75051 Grand Prairie 3779 Worthington Drive TX Texas"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 19, "CITY"),
(20, 42, "STREET_ADDRESS"),
(43, 45, "STATE"),
(46, 51, "STATE_FULL"),
]
}),
(
"TX 3779 Worthington Drive Texas 75051 Grand Prairie"
, {
"entities":[
(0, 2, "STATE"),
(3, 25, "STREET_ADDRESS"),
(26, 31, "STATE_FULL"),
(32, 37, "ZIPCODE"),
(38, 51, "CITY"),
]
}),
(
"3779 Worthington Drive TX Grand Prairie Texas 75051"
, {
"entities":[
(0, 22, "STREET_ADDRESS"),
(23, 25, "STATE"),
(26, 39, "CITY"),
(40, 45, "STATE_FULL"),
(46, 51, "ZIPCODE"),
]
}),
(
"Minneapolis 55405 MN 1455 Willison Street Minnesota"
, {
"entities":[
(0, 11, "CITY"),
(12, 17, "ZIPCODE"),
(18, 20, "STATE"),
(21, 41, "STREET_ADDRESS"),
(42, 51, "STATE_FULL"),
]
}),
(
"1455 Willison Street Minnesota Minneapolis 55405 MN"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 30, "STATE_FULL"),
(31, 42, "CITY"),
(43, 48, "ZIPCODE"),
(49, 51, "STATE"),
]
}),
(
"55405 Minneapolis 1455 Willison Street Minnesota MN"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 17, "CITY"),
(18, 38, "STREET_ADDRESS"),
(39, 48, "STATE_FULL"),
(49, 51, "STATE"),
]
}),
(
"1455 Willison Street Minnesota MN Minneapolis 55405"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 30, "STATE_FULL"),
(31, 33, "STATE"),
(34, 45, "CITY"),
(46, 51, "ZIPCODE"),
]
}),
(
"MN 55405 Minneapolis Minnesota 1455 Willison Street"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 20, "CITY"),
(21, 30, "STATE_FULL"),
(31, 51, "STREET_ADDRESS"),
]
}),
(
"55405 Minneapolis 1455 Willison Street Minnesota MN"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 17, "CITY"),
(18, 38, "STREET_ADDRESS"),
(39, 48, "STATE_FULL"),
(49, 51, "STATE"),
]
}),
(
"1455 Willison Street Minneapolis Minnesota 55405 MN"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 32, "CITY"),
(33, 42, "STATE_FULL"),
(43, 48, "ZIPCODE"),
(49, 51, "STATE"),
]
}),
(
"55405 Minneapolis 1455 Willison Street MN Minnesota"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 17, "CITY"),
(18, 38, "STREET_ADDRESS"),
(39, 41, "STATE"),
(42, 51, "STATE_FULL"),
]
}),
(
"Minnesota 55405 Minneapolis 1455 Willison Street MN"
, {
"entities":[
(0, 9, "STATE_FULL"),
(10, 15, "ZIPCODE"),
(16, 27, "CITY"),
(28, 48, "STREET_ADDRESS"),
(49, 51, "STATE"),
]
}),
(
"Minnesota MN 55405 Minneapolis 1455 Willison Street"
, {
"entities":[
(0, 9, "STATE_FULL"),
(10, 12, "STATE"),
(13, 18, "ZIPCODE"),
(19, 30, "CITY"),
(31, 51, "STREET_ADDRESS"),
]
}),
(
"66438 KS 4278 Dog Hill Lane Kansas Home"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 27, "STREET_ADDRESS"),
(28, 34, "STATE_FULL"),
(35, 39, "CITY"),
]
}),
(
"KS Kansas 4278 Dog Hill Lane Home 66438"
, {
"entities":[
(0, 2, "STATE"),
(3, 9, "STATE_FULL"),
(10, 28, "STREET_ADDRESS"),
(29, 33, "CITY"),
(34, 39, "ZIPCODE"),
]
}),
(
"KS Kansas 66438 Home 4278 Dog Hill Lane"
, {
"entities":[
(0, 2, "STATE"),
(3, 9, "STATE_FULL"),
(10, 15, "ZIPCODE"),
(16, 20, "CITY"),
(21, 39, "STREET_ADDRESS"),
]
}),
(
"KS 66438 Home Kansas 4278 Dog Hill Lane"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 13, "CITY"),
(14, 20, "STATE_FULL"),
(21, 39, "STREET_ADDRESS"),
]
}),
(
"Kansas 4278 Dog Hill Lane 66438 KS Home"
, {
"entities":[
(0, 6, "STATE_FULL"),
(7, 25, "STREET_ADDRESS"),
(26, 31, "ZIPCODE"),
(32, 34, "STATE"),
(35, 39, "CITY"),
]
}),
(
"66438 4278 Dog Hill Lane Kansas KS Home"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 24, "STREET_ADDRESS"),
(25, 31, "STATE_FULL"),
(32, 34, "STATE"),
(35, 39, "CITY"),
]
}),
(
"Kansas KS 66438 Home 4278 Dog Hill Lane"
, {
"entities":[
(0, 6, "STATE_FULL"),
(7, 9, "STATE"),
(10, 15, "ZIPCODE"),
(16, 20, "CITY"),
(21, 39, "STREET_ADDRESS"),
]
}),
(
"4278 Dog Hill Lane Kansas 66438 Home KS"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 25, "STATE_FULL"),
(26, 31, "ZIPCODE"),
(32, 36, "CITY"),
(37, 39, "STATE"),
]
}),
(
"Home 66438 4278 Dog Hill Lane KS Kansas"
, {
"entities":[
(0, 4, "CITY"),
(5, 10, "ZIPCODE"),
(11, 29, "STREET_ADDRESS"),
(30, 32, "STATE"),
(33, 39, "STATE_FULL"),
]
}),
(
"4278 Dog Hill Lane KS Kansas 66438 Home"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 21, "STATE"),
(22, 28, "STATE_FULL"),
(29, 34, "ZIPCODE"),
(35, 39, "CITY"),
]
}),
(
"KS 67202 2797 Williams Lane Wichita Kansas"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 27, "STREET_ADDRESS"),
(28, 35, "CITY"),
(36, 42, "STATE_FULL"),
]
}),
(
"Wichita 2797 Williams Lane Kansas KS 67202"
, {
"entities":[
(0, 7, "CITY"),
(8, 26, "STREET_ADDRESS"),
(27, 33, "STATE_FULL"),
(34, 36, "STATE"),
(37, 42, "ZIPCODE"),
]
}),
(
"Wichita 67202 KS Kansas 2797 Williams Lane"
, {
"entities":[
(0, 7, "CITY"),
(8, 13, "ZIPCODE"),
(14, 16, "STATE"),
(17, 23, "STATE_FULL"),
(24, 42, "STREET_ADDRESS"),
]
}),
(
"Wichita KS 67202 Kansas 2797 Williams Lane"
, {
"entities":[
(0, 7, "CITY"),
(8, 10, "STATE"),
(11, 16, "ZIPCODE"),
(17, 23, "STATE_FULL"),
(24, 42, "STREET_ADDRESS"),
]
}),
(
"67202 Wichita KS 2797 Williams Lane Kansas"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 13, "CITY"),
(14, 16, "STATE"),
(17, 35, "STREET_ADDRESS"),
(36, 42, "STATE_FULL"),
]
}),
(
"Wichita Kansas 2797 Williams Lane KS 67202"
, {
"entities":[
(0, 7, "CITY"),
(8, 14, "STATE_FULL"),
(15, 33, "STREET_ADDRESS"),
(34, 36, "STATE"),
(37, 42, "ZIPCODE"),
]
}),
(
"Kansas 2797 Williams Lane 67202 Wichita KS"
, {
"entities":[
(0, 6, "STATE_FULL"),
(7, 25, "STREET_ADDRESS"),
(26, 31, "ZIPCODE"),
(32, 39, "CITY"),
(40, 42, "STATE"),
]
}),
(
"67202 KS Kansas Wichita 2797 Williams Lane"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 15, "STATE_FULL"),
(16, 23, "CITY"),
(24, 42, "STREET_ADDRESS"),
]
}),
(
"KS 67202 Kansas 2797 Williams Lane Wichita"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 15, "STATE_FULL"),
(16, 34, "STREET_ADDRESS"),
(35, 42, "CITY"),
]
}),
(
"2797 Williams Lane 67202 KS Wichita Kansas"
, {
"entities":[
(0, 18, "STREET_ADDRESS"),
(19, 24, "ZIPCODE"),
(25, 27, "STATE"),
(28, 35, "CITY"),
(36, 42, "STATE_FULL"),
]
}),
(
"94612 California with Oakland CA 3705 Brown Street"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 16, "STATE_FULL"),
(22, 29, "CITY"),
(30, 32, "STATE"),
(33, 50, "STREET_ADDRESS"),
]
}),
(
"with 3705 Brown Street 94612 Oakland CA California"
, {
"entities":[
(5, 22, "STREET_ADDRESS"),
(23, 28, "ZIPCODE"),
(29, 36, "CITY"),
(37, 39, "STATE"),
(40, 50, "STATE_FULL"),
]
}),
(
"with Oakland CA 3705 Brown Street 94612 California"
, {
"entities":[
(5, 12, "CITY"),
(13, 15, "STATE"),
(16, 33, "STREET_ADDRESS"),
(34, 39, "ZIPCODE"),
(40, 50, "STATE_FULL"),
]
}),
(
"3705 Brown Street CA California with 94612 Oakland"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 20, "STATE"),
(21, 31, "STATE_FULL"),
(37, 42, "ZIPCODE"),
(43, 50, "CITY"),
]
}),
(
"with 3705 Brown Street California Oakland 94612 CA"
, {
"entities":[
(5, 22, "STREET_ADDRESS"),
(23, 33, "STATE_FULL"),
(34, 41, "CITY"),
(42, 47, "ZIPCODE"),
(48, 50, "STATE"),
]
}),
(
"3705 Brown Street 94612 with Oakland California CA"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 23, "ZIPCODE"),
(29, 36, "CITY"),
(37, 47, "STATE_FULL"),
(48, 50, "STATE"),
]
}),
(
"with 3705 Brown Street CA Oakland 94612 California"
, {
"entities":[
(5, 22, "STREET_ADDRESS"),
(23, 25, "STATE"),
(26, 33, "CITY"),
(34, 39, "ZIPCODE"),
(40, 50, "STATE_FULL"),
]
}),
(
"3705 Brown Street Oakland with CA 94612 California"
, {
"entities":[
(0, 17, "STREET_ADDRESS"),
(18, 25, "CITY"),
(31, 33, "STATE"),
(34, 39, "ZIPCODE"),
(40, 50, "STATE_FULL"),
]
}),
(
"CA 94612 3705 Brown Street California Oakland with"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 26, "STREET_ADDRESS"),
(27, 37, "STATE_FULL"),
(38, 45, "CITY"),
]
}),
(
"with Oakland CA California 94612 3705 Brown Street"
, {
"entities":[
(5, 12, "CITY"),
(13, 15, "STATE"),
(16, 26, "STATE_FULL"),
(27, 32, "ZIPCODE"),
(33, 50, "STREET_ADDRESS"),
]
}),
(
"GA 30091 Norcross 511 Neuport Lane Georgia"
, {
"entities":[
(0, 2, "STATE"),
(3, 8, "ZIPCODE"),
(9, 17, "CITY"),
(18, 34, "STREET_ADDRESS"),
(35, 42, "STATE_FULL"),
]
}),
(
"30091 Georgia GA Norcross 511 Neuport Lane"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 13, "STATE_FULL"),
(14, 16, "STATE"),
(17, 25, "CITY"),
(26, 42, "STREET_ADDRESS"),
]
}),
(
"511 Neuport Lane 30091 Norcross GA Georgia"
, {
"entities":[
(0, 16, "STREET_ADDRESS"),
(17, 22, "ZIPCODE"),
(23, 31, "CITY"),
(32, 34, "STATE"),
(35, 42, "STATE_FULL"),
]
}),
(
"511 Neuport Lane GA Norcross 30091 Georgia"
, {
"entities":[
(0, 16, "STREET_ADDRESS"),
(17, 19, "STATE"),
(20, 28, "CITY"),
(29, 34, "ZIPCODE"),
(35, 42, "STATE_FULL"),
]
}),
(
"511 Neuport Lane 30091 Georgia Norcross GA"
, {
"entities":[
(0, 16, "STREET_ADDRESS"),
(17, 22, "ZIPCODE"),
(23, 30, "STATE_FULL"),
(31, 39, "CITY"),
(40, 42, "STATE"),
]
}),
(
"Norcross 30091 GA 511 Neuport Lane Georgia"
, {
"entities":[
(0, 8, "CITY"),
(9, 14, "ZIPCODE"),
(15, 17, "STATE"),
(18, 34, "STREET_ADDRESS"),
(35, 42, "STATE_FULL"),
]
}),
(
"Norcross 30091 Georgia 511 Neuport Lane GA"
, {
"entities":[
(0, 8, "CITY"),
(9, 14, "ZIPCODE"),
(15, 22, "STATE_FULL"),
(23, 39, "STREET_ADDRESS"),
(40, 42, "STATE"),
]
}),
(
"511 Neuport Lane Georgia Norcross 30091 GA"
, {
"entities":[
(0, 16, "STREET_ADDRESS"),
(17, 24, "STATE_FULL"),
(25, 33, "CITY"),
(34, 39, "ZIPCODE"),
(40, 42, "STATE"),
]
}),
(
"Norcross 511 Neuport Lane 30091 Georgia GA"
, {
"entities":[
(0, 8, "CITY"),
(9, 25, "STREET_ADDRESS"),
(26, 31, "ZIPCODE"),
(32, 39, "STATE_FULL"),
(40, 42, "STATE"),
]
}),
(
"511 Neuport Lane 30091 GA Georgia Norcross"
, {
"entities":[
(0, 16, "STREET_ADDRESS"),
(17, 22, "ZIPCODE"),
(23, 25, "STATE"),
(26, 33, "STATE_FULL"),
(34, 42, "CITY"),
]
}),
(
"67545 KS Hudson 832 Breezewood Court Kansas"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 8, "STATE"),
(9, 15, "CITY"),
(16, 36, "STREET_ADDRESS"),
(37, 43, "STATE_FULL"),
]
}),
(
"Hudson Kansas KS 67545 832 Breezewood Court"
, {
"entities":[
(0, 6, "CITY"),
(7, 13, "STATE_FULL"),
(14, 16, "STATE"),
(17, 22, "ZIPCODE"),
(23, 43, "STREET_ADDRESS"),
]
}),
(
"67545 Hudson KS Kansas 832 Breezewood Court"
, {
"entities":[
(0, 5, "ZIPCODE"),
(6, 12, "CITY"),
(13, 15, "STATE"),
(16, 22, "STATE_FULL"),
(23, 43, "STREET_ADDRESS"),
]
}),
(
"Kansas 67545 832 Breezewood Court Hudson KS"
, {
"entities":[
(0, 6, "STATE_FULL"),
(7, 12, "ZIPCODE"),
(13, 33, "STREET_ADDRESS"),
(34, 40, "CITY"),
(41, 43, "STATE"),
]
}),
(
"KS Hudson 67545 832 Breezewood Court Kansas"
, {
"entities":[
(0, 2, "STATE"),
(3, 9, "CITY"),
(10, 15, "ZIPCODE"),
(16, 36, "STREET_ADDRESS"),
(37, 43, "STATE_FULL"),
]
}),
(
"Hudson 67545 KS 832 Breezewood Court Kansas"
, {
"entities":[
(0, 6, "CITY"),
(7, 12, "ZIPCODE"),
(13, 15, "STATE"),
(16, 36, "STREET_ADDRESS"),
(37, 43, "STATE_FULL"),
]
}),
(
"Hudson KS 832 Breezewood Court Kansas 67545"
, {
"entities":[
(0, 6, "CITY"),
(7, 9, "STATE"),
(10, 30, "STREET_ADDRESS"),
(31, 37, "STATE_FULL"),
(38, 43, "ZIPCODE"),
]
}),
(
"832 Breezewood Court Hudson 67545 KS Kansas"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 27, "CITY"),
(28, 33, "ZIPCODE"),
(34, 36, "STATE"),
(37, 43, "STATE_FULL"),
]
}),
(
"832 Breezewood Court Kansas 67545 KS Hudson"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 27, "STATE_FULL"),
(28, 33, "ZIPCODE"),
(34, 36, "STATE"),
(37, 43, "CITY"),
]
}),
(
"832 Breezewood Court KS Hudson 67545 Kansas"
, {
"entities":[
(0, 20, "STREET_ADDRESS"),
(21, 23, "STATE"),
(24, 30, "CITY"),
(31, 36, "ZIPCODE"),
(37, 43, "STATE_FULL"),
]
}),
(
"Maryland Information in Information MD 139 Five Points Baltimore Information 21201 address"
, {
"entities":[
(0, 8, "STATE_FULL"),
(36, 38, "STATE"),
(39, 54, "STREET_ADDRESS"),
(55, 64, "CITY"),
(77, 82, "ZIPCODE"),
]
}),
(
"Baltimore address Information 139 Five Points in MD Maryland Information Information 21201"
, {
"entities":[
(0, 9, "CITY"),
(30, 45, "STREET_ADDRESS"),
(49, 51, "STATE"),
(52, 60, "STATE_FULL"),
(85, 90, "ZIPCODE"),
]
}),
(
"MD Information in Maryland Information 21201 Information 139 Five Points Baltimore address"
, {
"entities":[
(0, 2, "STATE"),
(18, 26, "STATE_FULL"),
(39, 44, "ZIPCODE"),
(57, 72, "STREET_ADDRESS"),
(73, 82, "CITY"),
]
}),
(
"139 Five Points Information address MD Baltimore 21201 Maryland Information in Information"
, {
"entities":[
(0, 15, "STREET_ADDRESS"),
(36, 38, "STATE"),
(39, 48, "CITY"),
(49, 54, "ZIPCODE"),
(55, 63, "STATE_FULL"),
]
}),
(
"Baltimore MD Information 21201 in Maryland address Information Information 139 Five Points"
, {
"entities":[
(0, 9, "CITY"),
(10, 12, "STATE"),
(25, 30, "ZIPCODE"),
(34, 42, "STATE_FULL"),
(75, 90, "STREET_ADDRESS"),
]
}),
(
"Information Information MD Maryland 21201 address in Baltimore Information 139 Five Points"
, {
"entities":[
(24, 26, "STATE"),
(27, 35, "STATE_FULL"),
(36, 41, "ZIPCODE"),
(53, 62, "CITY"),
(75, 90, "STREET_ADDRESS"),
]
}),
(
"Information address Maryland Information Baltimore 139 Five Points MD in 21201 Information"
, {
"entities":[
(20, 28, "STATE_FULL"),
(41, 50, "CITY"),
(51, 66, "STREET_ADDRESS"),
(67, 69, "STATE"),
(73, 78, "ZIPCODE"),
]
}),
(
"139 Five Points Maryland address MD in Information Information Baltimore 21201 Information"
, {
"entities":[
(0, 15, "STREET_ADDRESS"),
(16, 24, "STATE_FULL"),
(33, 35, "STATE"),
(63, 72, "CITY"),
(73, 78, "ZIPCODE"),
]
}),
(
"Information Baltimore in address Information Maryland 139 Five Points Information 21201 MD"
, {
"entities":[
(12, 21, "CITY"),
(45, 53, "STATE_FULL"),
(54, 69, "STREET_ADDRESS"),
(82, 87, "ZIPCODE"),
(88, 90, "STATE"),
]
}),
(
"21201 Information address 139 Five Points Information Maryland MD in Baltimore Information"
, {
"entities":[
(0, 5, "ZIPCODE"),
(26, 41, "STREET_ADDRESS"),
(54, 62, "STATE_FULL"),
(63, 65, "STATE"),
(69, 78, "CITY"),
]
}),
]
