from db_connection import db, mycursor
from sql_queries import fetch_certain_municipalities, insert_single_municipality, update_single_municipality,\
    delete_single_municipality, truncate_municipality_table


def get_all_municipalities_name(district_id):
    municipalitiesList = []
    mycursor.execute(fetch_certain_municipalities, (int(district_id),))
    for municipality_id, municipality_name, municipality_to_province in mycursor:
        municipalitiesList.append(municipality_name)

    return municipalitiesList


def get_municipality_name(municipality_name_list):
    print("\nAvailable Municipalities" + str(municipality_name_list))
    print("\nPlease select the Municipality name: ")
    municipality_name = input(
        "\nInput: ")
    return municipality_name


def add_municipality(municipality_name, district_id):
    mycursor.execute(insert_single_municipality,
                     (municipality_name, int((district_id))))
    db.commit()


def update_municipality(new_municipality, old_municipality):
    mycursor.execute(update_single_municipality,
                     (new_municipality, old_municipality))
    db.commit()


def delete_municipality(municipality_name):
    mycursor.execute(delete_single_municipality, (municipality_name,))
    db.commit()


def truncate_municipality():
    mycursor.execute(truncate_municipality_table)
    db.commit()
