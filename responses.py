originalResponse = [
    {
        "phil_id": "f8932c72-791b-467f-9c12-687ca95a3d9c",
        "name": "aristotle",
        "age": 62,
        "city": "Euboea",
        "date_of_birth": "2015-01-22",
        "date_modified": "2015-01-22",
    },
    {
        "phil_id": "92185855-a949-43d7-9f19-41fcbfd04e72",
        "name": "plato",
        "age": 80,
        "city": "Athens",
        "date_of_birth": "2016-02-23",
        "date_modified": "2016-02-23",
    },
    {
        "phil_id": "7a0babfc-a9cc-4fa7-affe-226b5dd5a2d7",
        "name": "socrates",
        "age": 71,
        "city": "Athens",
        "date_of_birth": "2017-03-24",
        "date_modified": "2017-03-24",
    },
    {
        "phil_id": "2d2cc93d-1c12-4e2b-b4ee-427e44c35e63",
        "name": "diogenes",
        "age": 89,
        "city": "Corinth",
        "date_of_birth": "2018-04-25",
        "date_modified": "2018-04-25",
    },
]


modifiedDateColumnResponse = [
    {
        "phil_id": "f8932c72-791b-467f-9c12-687ca95a3d9c",
        "name": "aristotle",
        "age": 62,
        "city": "Euboea",
        "date_born": "2015-01-22",
        "date_modified": "2015-01-22",
    },
    {
        "phil_id": "92185855-a949-43d7-9f19-41fcbfd04e72",
        "name": "plato",
        "age": 80,
        "city": "Athens",
        "date_born": "2016-02-23",
        "date_modified": "2016-02-23",
    },
    {
        "phil_id": "7a0babfc-a9cc-4fa7-affe-226b5dd5a2d7",
        "name": "socrates",
        "age": 71,
        "city": "Athens",
        "date_born": "2017-03-24",
        "date_modified": "2017-03-24",
    },
    {
        "phil_id": "2d2cc93d-1c12-4e2b-b4ee-427e44c35e63",
        "name": "diogenes",
        "age": 89,
        "city": "Corinth",
        "date_born": "2018-04-25",
        "date_modified": "2018-04-25",
    },
]


invalidDateColumnResponse = [
    {
        "phil_id": "f8932c72-791b-467f-9c12-687ca95a3d9c",
        "name": "aristotle",
        "age": 62,
        "city": "Euboea",
        "date_born": "idk",
        "date_modified": "2015-01-22",
    },
    {
        "phil_id": "92185855-a949-43d7-9f19-41fcbfd04e72",
        "name": "plato",
        "age": 80,
        "city": "Athens",
        "date_born": 1208,
        "date_modified": "2016-02-23",
    },
    {
        "phil_id": "7a0babfc-a9cc-4fa7-affe-226b5dd5a2d7",
        "name": "socrates",
        "age": 71,
        "city": "Athens",
        "date_born": "long ago",
        "date_modified": "2017-03-24",
    },
    {
        "phil_id": "2d2cc93d-1c12-4e2b-b4ee-427e44c35e63",
        "name": "diogenes",
        "age": 89,
        "city": "Corinth",
        "date_born": "2018-04-25",
        "date_modified": "2018-04-25",
    },
]
