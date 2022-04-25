from province import get_all_provinces_name, get_province_name
from district import get_all_districts_name, get_district_name
from municipality import get_all_municipalities_name, get_municipality_name


def get_user_operation():
    print('''\nEnter 1 for inserting/updating/deleting a Province
Enter 2 for inserting/updating/deleting a District
Enter 3 for inserting/updating/deleting a Municipality
Enter 4 for listing all Districts of a Province
Enter 5 for listing all Municipalities of a Province\n''')
    user_operation = input("Input: ")
    return user_operation


def validate_user_operation(user_operation):
    is_valid = True
    if user_operation != "1" and user_operation != "2" and user_operation != "3" and user_operation != "4"\
            and user_operation != "5":
        is_valid = False
    return is_valid


def get_crud_operation(type):
    print("\nEnter a for inserting a " + type + "\nEnter b updating a " +
          type + "\nEnter c for deleting a " + type + "\n")
    crud_operation = input("Input: ")
    return crud_operation


def validate_crud_operation(crud_operation):
    is_valid = True
    if crud_operation != "a" and crud_operation != "b" and crud_operation != "c":
        is_valid = False

    return is_valid


def validate_province():
    province_exists = False
    provinces_name_list = get_all_provinces_name()
    province_name = get_province_name(provinces_name_list)
    if province_name in provinces_name_list:
        province_exists = True

    return [province_exists, province_name]


def validate_district(province_id):
    district_exists = False
    districts_name_list = get_all_districts_name(province_id)
    district_name = get_district_name(districts_name_list)
    if district_name in districts_name_list:
        district_exists = True

    return [district_exists, district_name]


def validate_municipality(district_id):
    municipality_exist = False
    municipalities_name_list = get_all_municipalities_name(
        district_id)
    municipality_name = get_municipality_name(municipalities_name_list)
    if municipality_name in municipalities_name_list:
        municipality_exist = True

    return [municipality_exist, municipality_name]
