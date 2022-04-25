from db_connection import db, mycursor
from sql_queries import insert_single_province, get_single_province_id, delete_single_province, update_single_province,\
    fetch_all_provinces, truncate_province_table


def add_single_province(province_name):
    mycursor.execute(insert_single_province, (province_name,))
    db.commit()


def get_province_name(provincesNameList):
    print("\nPlease select the Province name First. ")
    print("\nAvailable Provinces " + str(provincesNameList))
    province_name = input(
        "\nInput: ")
    return province_name


def get_province_id(province_name):
    mycursor.execute(get_single_province_id, (province_name,))
    for i in mycursor:
        province_id, *remaining = i
        return province_id


def delete_province(province_name):
    mycursor.execute(delete_single_province, (province_name,))
    db.commit()


def update_province(latest_province_name, previous_province_name):
    mycursor.execute(
        update_single_province, (latest_province_name, previous_province_name))
    db.commit()


def get_all_provinces_name():
    provincesNameList = []
    mycursor.execute(fetch_all_provinces)
    for province_id, province_name in mycursor:
        provincesNameList.append(province_name)

    return provincesNameList


def truncate_province():
    mycursor.execute(truncate_province_table)
    db.commit()
