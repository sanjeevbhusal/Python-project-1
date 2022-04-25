from db_connection import mycursor
fetch_all_provinces = "SELECT * FROM provinces"
fetch_all_districts = "SELECT * FROM districts"
fetch_all_municipalities = "SELECT * FROM municipalities"

fetch_certain_provinces = "SELECT * FROM provinces WHERE "
fetch_certain_districts = "SELECT * FROM districts WHERE district_to_province = (%s) "
fetch_certain_municipalities = "SELECT * FROM municipalities WHERE municipality_to_district = (%s)"

insert_single_province = "INSERT INTO provinces (province_name) VALUES (%s)"
insert_single_district = "INSERT INTO districts (district_name, district_to_province) VALUES (%s, %s)"
insert_single_municipality = "INSERT INTO municipalities (municipality_name, municipality_to_district) VALUES (%s, %s)"

update_single_province = "UPDATE provinces SET province_name = (%s) WHERE province_name = (%s )"
update_single_district = "UPDATE districts SET district_name = (%s) WHERE district_name = (%s )"
update_single_municipality = "UPDATE municipalities SET municipality_name = (%s) WHERE municipality_name = (%s )"

delete_single_province = "DELETE FROM provinces WHERE province_name = (%s)"
delete_single_district = "DELETE FROM districts WHERE district_name = (%s)"
delete_single_municipality = "DELETE FROM municipalities WHERE municipality_name = (%s)"

truncate_province_table = "TRUNCATE TABLE provinces"
truncate_district_table = "TRUNCATE TABLE districts"
truncate_municipality_table = "TRUNCATE TABLE municipalities"

get_single_province_id = "SELECT province_id FROM provinces WHERE province_name = (%s)"
get_single_district_id = "SELECT district_id FROM districts WHERE district_name = (%s)"


def createTables():
    Q1 = '''CREATE TABLE Provinces (
            province_id int PRIMARY KEY AUTO_INCREMENT,
            province_name VARCHAR(25) NOT NULL
            )
        '''

    Q2 = '''CREATE TABLE Districts (
            district_id int PRIMARY KEY AUTO_INCREMENT,
            district_name VARCHAR(25),
            district_to_province int,
            FOREIGN KEY(district_to_province) REFERENCES Provinces(province_id)
            )
        '''

    Q3 = '''CREATE TABLE Municipalities (
            municipality_id int PRIMARY KEY AUTO_INCREMENT,
            municipality_name VARCHAR(25),
            municipality_to_district int,
            FOREIGN KEY(municipality_to_district) REFERENCES Districts(district_id)
            );
        '''

    mycursor.execute(Q1)

    mycursor.execute(Q2)

    mycursor.execute(Q3)
