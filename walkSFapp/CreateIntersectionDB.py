__author__ = 'bill'
from intersection import *
import sqlite3

def main():
    connection = sqlite3.connect("./intersections.db")
    # connection.
    # connection.execute("create table intersections(cnn int primary key, latitude real not null, longitude real not null, description text not null)")
    intersections = loadIntersections();
    count = 0
    ints = []
    for intersection in generate_intersections(intersections):
        insert_str = "insert into intersections values({}, {}, {}, {});".format(intersection.CNN, intersection.loc.getLat(), intersection.loc.getLong(), intersection.streets[0] + " & " + intersection.streets[1])
        # connection.execute(insert_str)
        int = (intersection.CNN, intersection.loc.getLat(), intersection.loc.getLong(), intersection.streets[0] + " & " + intersection.streets[1])
        ints.append(int)
        # print(int)
        count+=1

    connection.executemany('INSERT INTO intersections VALUES (?,?,?,?)', ints)
    print(count)

    connection.commit()
    connection.close()


if __name__ == '__main__':
    main()