
TRAIN_DATA_LONG = [
    ('Welcome to Acme Corporation, located at 1234 Elmwood Drive, Suite 567, Toronto, ON, Canada', {
        'entities': [(15, 30, 'ORG'), (44, 61, 'STREET_NAME'), (63, 70, 'CITY'), (72, 74, 'COUNTY'), (76, 81, 'POSTAL_CODE'), (83, 89, 'COUNTRY')]
    }),
    ('We are a leading technology company headquartered in Silicon Valley, California, USA', {
        'entities': [(30, 45, 'LOCATION'), (61, 73, 'STATE'), (75, 82, 'COUNTRY')]
    }),
    ('Our main office is in London, United Kingdom, with branches in Paris, France and Berlin, Germany', {
        'entities': [(19, 25, 'CITY'), (27, 44, 'COUNTRY'), (63, 68, 'CITY'), (70, 76, 'COUNTRY'), (95, 101, 'CITY'), (103, 109, 'COUNTRY')]
    }),
    ('John Smith is our Chief Operating Officer, and Jane Brown is our Vice President of Marketing', {
        'entities': [ (27, 54, 'JOB_TITLE'), (86, 109, 'JOB_TITLE')]
    }),
    ('Our global headquarters is located at 567 Fifth Avenue, New York, NY 10022, USA', {
        'entities': [(26, 43, 'STREET_NAME'), (45, 53, 'CITY'), (55, 57, 'STATE'), (59, 66, 'POSTAL_CODE'), (68, 71, 'COUNTRY')]
    }),
    ('We have offices in major cities such as San Francisco, CA; Austin, TX; and Seattle, WA', {
        'entities': [(24, 38, 'CITY'), (40, 42, 'STATE'), (44, 57, 'CITY'), (59, 61, 'STATE'), (66, 79, 'CITY'), (81, 83, 'STATE')]
    }),
    ('Our company serves clients all over Europe, including London, Paris, Berlin, and Rome', {
        'entities': [(35, 41, 'CITY'), (43, 48, 'CITY'), (50, 55, 'CITY'), (60, 64, 'CITY')]
    }),
    ('Visit our website at www.example.com for more information about our services', {
        'entities': [(17, 31, 'WEBSITE')]
    }),
    ('Acme Corporation, 1234 Elmwood Drive, Suite 567, Toronto, ON, Canada', {
        'entities': [(0, 16, 'ORG'), (18, 35, 'STREET_NAME'), (37, 44, 'STREET_TYPE'), (46, 53, 'CITY'), (55, 57, 'COUNTY'), (59, 64, 'POSTAL_CODE'), (66, 72, 'COUNTRY')]
    }),
    ('We have a dedicated team of experts in New York, Los Angeles, and Chicago', {
        'entities': [(34, 42, 'CITY'), (44, 56, 'CITY'), (61, 68, 'CITY')]
    }),
]

TRAIN_DATA = [
    ('With Us Physical Address​ 503 Maurice Street Monroe NC 28112 Phone Numbers 1-704-283-6342', {
        'entities': [(20, 35, 'STREET_NAME'), (56, 62, 'CITY'), (63, 65, 'COUNTY'), (66, 71, 'POSTAL_CODE'), (36, 55, 'COUNTRY')]
    }),
    ('1234 Elm Street Apt 5B New York NY 10001', {
        'entities': [(0, 18, 'STREET_NAME'), (19, 27, 'CITY'), (28, 30, 'COUNTY'), (31, 36, 'POSTAL_CODE'), (37, 42, 'COUNTRY')]
    }),
    ('Maria Hernandez, 789 Oak Avenue, Los Angeles, CA 90012', {
        'entities': [ (29, 45, 'STREET_NAME'), (46, 58, 'CITY'), (59, 61, 'COUNTY'), (62, 67, 'POSTAL_CODE'), (68, 70, 'COUNTRY')]
    }),
    ('456 Maple Lane Seattle WA 98101', {
        'entities': [(0, 12, 'STREET_NAME'), (13, 20, 'CITY'), (21, 23, 'COUNTY'), (24, 29, 'POSTAL_CODE'), (30, 32, 'COUNTRY')]
    }),
    ('John Smith, 789 Pine Street, Boston, MA 02108', {
        'entities': [ (12, 26, 'STREET_NAME'), (27, 33, 'CITY'), (34, 36, 'COUNTY'), (37, 42, 'POSTAL_CODE'), (43, 45, 'COUNTRY')]
    }),
    ('1001 Oakwood Drive Atlanta GA 30303', {
        'entities': [(0, 17, 'STREET_NAME'), (18, 25, 'CITY'), (26, 28, 'COUNTY'), (29, 34, 'POSTAL_CODE'), (35, 37, 'COUNTRY')]
    }),
    ('Samantha Brown, 567 Cedar Road, San Francisco, CA 94107', {
        'entities': [(17, 27, 'STREET_NAME'), (28, 42, 'CITY'), (43, 45, 'COUNTY'), (46, 51, 'POSTAL_CODE'), (52, 54, 'COUNTRY')]
    }),
    ('123 Main Street Chicago IL 60601', {
        'entities': [(0, 15, 'STREET_NAME'), (16, 23, 'CITY'), (24, 26, 'COUNTY'), (27, 32, 'POSTAL_CODE'), (33, 35, 'COUNTRY')]
    }),
    ('567 Pine Avenue Miami FL 33139', {
        'entities': [(0, 13, 'STREET_NAME'), (14, 19, 'CITY'), (20, 22, 'COUNTY'), (23, 28, 'POSTAL_CODE'), (29, 31, 'COUNTRY')]
    }),
    
    ('1234 Elmwood Drive, Apt 567, Toronto, ON, Canada', {
        'entities': [(0, 17, 'STREET_NAME'), (19, 26, 'STREET_NAME'), (28, 35, 'STREET_TYPE'), (37, 43, 'APARTMENT_NUMBER'), (45, 52, 'CITY'), (54, 56, 'COUNTY'), (58, 63, 'POSTAL_CODE'), (65, 71, 'COUNTRY')]
    }),
    ('4567 Maple Avenue, Suite 890, Los Angeles, CA, USA', {
        'entities': [(0, 17, 'STREET_NAME'),  (33, 40, 'STREET_TYPE'), (42, 53, 'CITY'), (55, 57, 'STATE'), (59, 61, 'COUNTRY')]
    }),
    ('789 Oak Street, London, Greater London, United Kingdom', {
        'entities': [(0, 13, 'STREET_NAME'), (26, 40, 'CITY'), (42, 56, 'COUNTY'), (58, 75, 'COUNTRY')]
    }),
    ('5678 Willow Lane, Sydney, New South Wales, Australia', {
        'entities': [(0, 14, 'STREET_NAME'), (29, 45, 'CITY'), (47, 63, 'COUNTY'), (65, 73, 'COUNTRY')]
    }),
    ('9876 Cedar Road, Paris, Île-de-France, France', {
        'entities': [(0, 13, 'STREET_NAME'),  (28, 42, 'CITY'), (44, 55, 'COUNTY'), (57, 63, 'COUNTRY')]
    }),
    ('345 Pine Street, Berlin, Germany', {
        'entities': [(0, 13, 'STREET_NAME'),  (28, 34, 'CITY'), (36, 43, 'COUNTRY')]
    }),
    ('4567 Maple Avenue, Suite 890, Los Angeles, CA, USA', {
        'entities': [(0, 17, 'STREET_NAME'),  (33, 40, 'STREET_TYPE'), (42, 53, 'CITY'), (55, 57, 'STATE'), (59, 61, 'COUNTRY')]
    }),
    ('789 Oak Street, London, Greater London, United Kingdom', {
        'entities': [(0, 13, 'STREET_NAME'), (26, 40, 'CITY'), (42, 56, 'COUNTY'), (58, 75, 'COUNTRY')]
    }),
    ('5678 Willow Lane, Sydney, New South Wales, Australia', {
        'entities': [(0, 14, 'STREET_NAME'),  (29, 45, 'CITY'), (47, 63, 'COUNTY'), (65, 73, 'COUNTRY')]
    }),
]


TRAIN_DATA_SHORT = [
    ('1234 Elmwood Drive, Suite 567, Toronto, ON, Canada', {
        'entities': [(0, 17, 'STREET_NAME'), (19, 26, 'STREET_TYPE'), (28, 35, 'CITY'), (37, 39, 'COUNTY'), (41, 46, 'POSTAL_CODE'), (48, 54, 'COUNTRY')]
    }),
    ('Silicon Valley, California, USA', {
        'entities': [(0, 14, 'LOCATION'), (16, 28, 'STATE'), (30, 37, 'COUNTRY')]
    }),
    ('London, United Kingdom', {
        'entities': [(0, 6, 'CITY'), (8, 25, 'COUNTRY')]
    }),
    ('Paris, France', {
        'entities': [(0, 5, 'CITY'), (7, 13, 'COUNTRY')]
    }),
    ('Berlin, Germany', {
        'entities': [(0, 6, 'CITY'), (8, 15, 'COUNTRY')]
    }),
    ('John Smith, Chief Operating Officer', {
        'entities': [(12, 36, 'JOB_TITLE')]
    }),
    ('Jane Brown, Vice President of Marketing', {
        'entities': [(12, 35, 'JOB_TITLE')]
    }),
    ('567 Fifth Avenue, New York, NY 10022, USA', {
        'entities': [(0, 17, 'STREET_NAME'), (19, 27, 'CITY'), (29, 31, 'STATE'), (33, 40, 'POSTAL_CODE'), (42, 45, 'COUNTRY')]
    }),
    ('San Francisco, CA', {
        'entities': [(0, 13, 'CITY'), (15, 17, 'STATE')]
    }),
    ('Austin, TX', {
        'entities': [(0, 6, 'CITY'), (8, 10, 'STATE')]
    }),
    ('Seattle, WA', {
        'entities': [(0, 8, 'CITY'), (10, 12, 'STATE')]
    }),
    ('London, Paris, Berlin, Rome', {
        'entities': [(0, 6, 'CITY'), (8, 13, 'CITY'), (15, 20, 'CITY'), (22, 26, 'CITY')]
    }),
    ('www.example.com', {
        'entities': [(0, 15, 'WEBSITE')]
    }),
    ('1234 Elmwood Drive, Suite 567, Toronto, ON, Canada', {
        'entities': [(0, 17, 'STREET_NAME'), (19, 26, 'STREET_TYPE'), (28, 35, 'CITY'), (37, 39, 'COUNTY'), (41, 46, 'POSTAL_CODE'), (48, 54, 'COUNTRY')]
    }),
    ('New York, Los Angeles, Chicago', {
        'entities': [(0, 8, 'CITY'), (10, 22, 'CITY'), (24, 30, 'CITY')]
    }),
]

ALL_TRAINING_DATA = TRAIN_DATA + TRAIN_DATA_LONG + TRAIN_DATA_SHORT