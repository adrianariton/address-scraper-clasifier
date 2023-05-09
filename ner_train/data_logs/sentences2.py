TRAINING_DATA2 = [
    ("Visit us at 1234 Elm Street, Suite 567, in Miami, FL 33133 for a free consultation.", {
        'entities': [(11, 22, 'STREET_NAME'), (24, 35, 'SUITE'), (37, 42, 'CITY'), (44, 46, 'STATE'), (47, 52, 'ZIP')]
    }),
    ("Our office is located at 567 Oakwood Avenue, Apt 890, in Seattle, WA 98101.", {
        'entities': [(18, 35, 'STREET_NAME'), (37, 46, 'SUITE'), (48, 55, 'CITY'), (57, 59, 'STATE'), (60, 65, 'ZIP')]
    }),
    ("Join us at 987 Market Street, Suite 1234, in Austin, TX 78701 for a special event.", {
        'entities': [(6, 20, 'STREET_NAME'), (22, 33, 'SUITE'), (35, 47, 'CITY'), (49, 51, 'STATE'), (52, 57, 'ZIP')]
    }),
    ("Come see us at 456 Birch Lane, Building 789, in Los Angeles, CA 90001 for a product demo.", {
        'entities': [(13, 25, 'STREET_NAME'), (27, 39, 'BUILDING'), (41, 54, 'CITY'), (56, 58, 'STATE'), (59, 64, 'ZIP')]
    }),
    ("Our store is located at 678 Maple Road, Suite 456, in New York, NY 10001.", {
        'entities': [(20, 33, 'STREET_NAME'), (35, 46, 'SUITE'), (48, 56, 'CITY'), (58, 60, 'STATE'), (61, 66, 'ZIP')]
    }),
    ("Join us at 789 Pine Street, Apt 123, in San Francisco, CA 94102 for a networking event.", {
        'entities': [(8, 21, 'STREET_NAME'), (23, 31, 'SUITE'), (33, 47, 'CITY'), (49, 51, 'STATE'), (52, 57, 'ZIP')]
    }),
    ("Our headquarters is located at 890 Cedar Avenue, Suite 2345, in Chicago, IL 60601.", {
        'entities': [(21, 35, 'STREET_NAME'), (37, 48, 'SUITE'), (50, 57, 'CITY'), (59, 61, 'STATE'), (62, 67, 'ZIP')]
    }),
    ("Come visit us at 1235 Pine Street, Building 567, in Philadelphia, PA 19103 for a grand opening.", {
        'entities': [(12, 25, 'STREET_NAME'), (27, 39, 'BUILDING'), (41, 54, 'CITY'), (56, 58, 'STATE'), (59, 64, 'ZIP')]
    }),
    ("Our showroom is located at 567 Birch Lane, Suite C, in Atlanta, GA 30303.", {
        'entities': [(20, 31, 'STREET_NAME'), (33, 38, 'SUITE'), (40, 47, 'CITY'), (49, 51, 'STATE'), (52,58,'ZIP')]
    }),
    ("Come see us at 456 Oakwood Avenue, Building 789, in Miami, FL 33133 for a product demo.", {
    'entities': [(13, 31, 'STREET_NAME'), (33, 45, 'BUILDING'), (47, 60, 'CITY'), (62, 64, 'STATE'), (65, 70, 'ZIP')]
    }),
    ("Our office is located at 678 Elm Street, Suite 1234, in San Francisco, CA 94102.", {
    'entities': [(18, 30, 'STREET_NAME'), (32, 43, 'SUITE'), (45, 58, 'CITY'), (60, 62, 'STATE'), (63, 68, 'ZIP')]
    }),
    ("Join us at 789 Pine Street, Apt 567, in New York, NY 10001 for a grand opening.", {
    'entities': [(8, 21, 'STREET_NAME'), (23, 31, 'SUITE'), (33, 46, 'CITY'), (48, 50, 'STATE'), (51, 56, 'ZIP')]
    }),
    ("Come visit us at 890 Cedar Avenue, Suite 2345, in Chicago, IL 60601 for a free consultation.", {
    'entities': [(12, 26, 'STREET_NAME'), (28, 39, 'SUITE'), (41, 48, 'CITY'), (50, 52, 'STATE'), (53, 58, 'ZIP')]
    }),
    ("Our store is located at 1234 Pine Street, Building 567, in Atlanta, GA 30303.", {
    'entities': [(20, 32, 'STREET_NAME'), (34, 46, 'BUILDING'), (48, 61, 'CITY'), (63, 65, 'STATE'), (66, 71, 'ZIP')]
    }),
    ("Join us at 456 Birch Lane, Suite C, in Dallas, TX 75201 for a networking event.", {
    'entities': [(8, 20, 'STREET_NAME'), (22, 27, 'SUITE'), (29, 34, 'CITY'), (36, 38, 'STATE'), (39, 44, 'ZIP')]
    }),
    ("Come see us at 678 Oakwood Avenue, Building 789, in Philadelphia, PA 19103 for a product demo.", {
    'entities': [(13, 31, 'STREET_NAME'), (33, 45, 'BUILDING'), (47, 60, 'CITY'), (62, 64, 'STATE'), (65, 70, 'ZIP')]
    }),
    ("Our headquarters is located at 789 Maple Road, Apt 567, in Miami, FL 33133.", {
    'entities': [(21, 33, 'STREET_NAME'), (35, 43, 'SUITE'), (45, 58, 'CITY'), (60, 62, 'STATE'), (63, 68, 'ZIP')]
    }),
    ("Come visit us at 890 Pine Street, Suite 1234, in San Francisco, CA94102 for a product launch.", {
    'entities': [(12, 24, 'STREET_NAME'), (26, 37, 'SUITE'), (39, 52, 'CITY'), (54, 56, 'STATE'), (57, 62, 'ZIP')]
    }),
    ("Join us at 1234 Cedar Avenue, Suite 5678, in New York, NY 10001 for a special event.", {
    'entities': [(8, 22, 'STREET_NAME'), (24, 35, 'SUITE'), (37, 50, 'CITY'), (52, 54, 'STATE'), (55, 60, 'ZIP')]
    }),
    ("Come see us at 456 Elm Street, Building 789, in Chicago, IL 60601 for a workshop.", {
    'entities': [(13, 25, 'STREET_NAME'), (27, 39, 'BUILDING'), (41, 54, 'CITY'), (56, 58, 'STATE'), (59, 64, 'ZIP')]
    }),
    ("Our office is located at 678 Birch Lane, Suite 2345, in Dallas, TX 75201.", {
    'entities': [(18, 30, 'STREET_NAME'), (32, 43, 'SUITE'), (45, 58, 'CITY'), (60, 62, 'STATE'), (63, 68, 'ZIP')]
    }),
    ("Join us at 789 Oakwood Avenue, Apt 567, in San Francisco, CA 94102 for a seminar.", {
    'entities': [(8, 26, 'STREET_NAME'), (28, 36, 'SUITE'), (38, 51, 'CITY'), (53, 55, 'STATE'), (56, 61, 'ZIP')]
    }),
    ("Come visit us at 890 Pine Street, Suite 1234, in Philadelphia, PA 19103 for a consultation.", {
    'entities': [(12, 24, 'STREET_NAME'), (26, 37, 'SUITE'), (39, 52, 'CITY'), (54, 56, 'STATE'), (57, 62, 'ZIP')]
    }),
    ("Our store is located at 1234 Maple Road, Building 567, in Atlanta, GA 30303.", {
    'entities': [(20, 32, 'STREET_NAME'), (34, 46, 'BUILDING'), (48, 61, 'CITY'), (63, 65, 'STATE'), (66, 71, 'ZIP')]
    }),
    ("Join us at 456 Cedar Avenue, Suite C, in Miami, FL 33133 for a networking event.", {
    'entities': [(8, 20, 'STREET_NAME'), (22, 27, 'SUITE'), (29, 42, 'CITY'), (44, 46, 'STATE'), (47, 52, 'ZIP')]
    }),
    ("Come see us at 678 Oakwood Avenue, Building 789, in Dallas, TX 75201 for a product demo.", {
    'entities': [(13, 31, 'STREET_NAME'), (33, 45, 'BUILDING'), (47, 60, 'CITY'), (62, 64, 'STATE'), (65, 70, 'ZIP')]
    }),
    ("Our headquarters is located at 789 Pine Street, Apt 567, in New York, NY 10001.", {
    'entities': [(21, 33, 'STREET_NAME'), (35,46, 'SUITE'), (48, 61, 'CITY'), (63, 65, 'STATE'), (66, 71, 'ZIP')]
    }),
    ("Join us at 890 Birch Lane, Suite 1234, in Chicago, IL 60601 for a workshop.", {
    'entities': [(8, 20, 'STREET_NAME'), (22, 33, 'SUITE'), (35, 48, 'CITY'), (50, 52, 'STATE'), (53, 58, 'ZIP')]
    }),
    ("Come visit us at 1234 Cedar Avenue, Suite 5678, in San Francisco, CA 94102 for a consultation.", {
    'entities': [(12, 26, 'STREET_NAME'), (28, 39, 'SUITE'), (41, 54, 'CITY'), (56, 58, 'STATE'), (59, 64, 'ZIP')]
    }),
    ("Our office is located at 456 Elm Street, Building 789, in Atlanta, GA 30303.", {
    'entities': [(18, 30, 'STREET_NAME'), (32, 44, 'BUILDING'), (46, 59, 'CITY'), (61, 63, 'STATE'), (64, 69, 'ZIP')]
    }),
    ("Join us at 678 Birch Lane, Suite 2345, in Dallas, TX 75201 for a special event.", {
    'entities': [(8, 20, 'STREET_NAME'), (22, 33, 'SUITE'), (35, 48, 'CITY'), (50, 52, 'STATE'), (53, 58, 'ZIP')]
    }),
    ("Come see us at 789 Oakwood Avenue, Apt 567, in Philadelphia, PA 19103 for a seminar.", {
    'entities': [(8, 26, 'STREET_NAME'), (28, 36, 'SUITE'), (38, 51, 'CITY'), (53, 55, 'STATE'), (56, 61, 'ZIP')]
    }),
    ("Our store is located at 890 Pine Street, Suite 1234, in Miami, FL 33133.", {
    'entities': [(20, 32, 'STREET_NAME'), (34, 45, 'SUITE'), (47, 60, 'CITY'), (62, 64, 'STATE'), (65, 70, 'ZIP')]
    }),
    ("Join us at 1234 Maple Road, Building 567, in New York, NY 10001 for a networking event.", {
    'entities': [(8, 20, 'STREET_NAME'), (22, 34, 'BUILDING'), (36, 49, 'CITY'), (51, 53, 'STATE'), (54, 59, 'ZIP')]
    }),
    ("Come visit us at 456 Cedar Avenue, Suite C, in Dallas, TX 75201 for a product demo.", {
    'entities': [(12, 24, 'STREET_NAME'), (26, 31, 'SUITE'), (33, 46, 'CITY'), (48, 50, 'STATE'), (51, 56, 'ZIP')]
    }),
    ]