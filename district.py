from db_connection import db, mycursor
from sql_queries import insert_single_district, fetch_all_districts, get_single_district_id, delete_single_district,\
    fetch_certain_districts, update_single_district, truncate_district_table


def add_district(district_name, province_id):
    mycursor.execute(insert_single_district, (district_name, int(province_id)))
    db.commit()


def get_district_name(districtsNameList):
    print("\nAvailable Districts:\n" + str(districtsNameList))
    print("\nPlease select the District name First: ")
    district_name = input(
        "\nInput: ")
    return district_name


def get_entire_districts():
    entireDistricts = []
    mycursor.execute(fetch_all_districts)
    for district_id, district_name, district_to_province in mycursor:
        entireDistricts.append(district_name)
    return entireDistricts


def get_district_id(district_name):
    mycursor.execute(get_single_district_id, (district_name,))
    for i in mycursor:
        district_id, *remaining = i
        return district_id


def delete_district(district_name):
    mycursor.execute(delete_single_district, (district_name,))
    db.commit()


def get_all_districts_name(province_id):
    districtsNameList = []
    mycursor.execute(fetch_certain_districts, (int(province_id),))
    for district_id, district_name, district_to_province in mycursor:
        districtsNameList.append(district_name)

    return districtsNameList


def update_district(latest_district_name, old_district_name):
    mycursor.execute(
        update_single_district, (latest_district_name, old_district_name))
    db.commit()


def truncate_district():
    mycursor.execute(truncate_district_table)
    db.commit()
