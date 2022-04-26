from classs.district import District

from utils.utils import get_user_operation, validate_user_operation, get_crud_operation, validate_crud_operation, print_success_message, print_failure_message

from classs.province import Province
from classs.district import District
from classs.municipality import Municipality

Province = Province()
District = District()
Municipality = Municipality()


while True:

    user_operation = get_user_operation()
    is_user_validated = validate_user_operation(user_operation)
    if is_user_validated:
        user_operation = int(user_operation)
        if user_operation == 1:
            while True:
                crud_operation = get_crud_operation("Province")
                is_crud_validated = validate_crud_operation(crud_operation)
                if is_crud_validated:
                    if crud_operation == "a":
                        province_name = Province.take_input()
                        Province.add_province(province_name)
                        print_success_message()
                        break

                    elif crud_operation == "b":
                        provinces_collection = Province.get_all_provinces()
                        print(
                            "\nHere are the Available Provinces\n" + str(provinces_collection))
                        previous_province_name = input(
                            "\nPlease Enter the name of Province to Update: ")

                        if previous_province_name in provinces_collection:
                            latest_province_name = input(
                                "\nEnter Updated Name for Province " + previous_province_name + ": ")
                            Province.update_province(
                                latest_province_name, previous_province_name)
                            print_success_message()
                            break

                        else:
                            print_failure_message()

                    elif crud_operation == "c":
                        provinces_collection = Province.get_all_provinces()
                        print(
                            "Here are the Available Provinces\n" + str(provinces_collection))
                        province_name = input(
                            "\nPlease Enter the name of Province to Delete: ")

                        if province_name in provinces_collection:
                            Province.delete_province(province_name)
                            print_success_message()
                            break

                        else:
                            print_failure_message()
                else:
                    print_failure_message()

        elif user_operation == 2:
            while True:
                provinces_collection = Province.get_all_provinces()
                print('\nTo access districts data, plz choose Province')
                print("\nHere are the Available Provinces.\n" +
                      str(provinces_collection))
                province_name = input(
                    "\nProvince name: ")
                if province_name in provinces_collection:
                    crud_operation = get_crud_operation("District")
                    is_crud_validated = validate_crud_operation(crud_operation)
                    if is_crud_validated:
                        province_id = Province.get_province_id(province_name)
                        if crud_operation == "a":
                            district_name = input("\nEnter District Name: ")
                            District.add_district(district_name, province_id)
                            print_success_message()
                            break

                        if crud_operation == "b":
                            districts_collection = District. get_specific_districts(
                                province_id)
                            print("\nAvailable Districts.\n" +
                                  str(districts_collection))
                            print(
                                "\nEnter the name of District to Update")
                            old_district_name = input("\nEnter: ")
                            if old_district_name in districts_collection:
                                new_district_name = input(
                                    "\nEnter new Name of District " + old_district_name + ": ")
                                District.update_district(
                                    new_district_name, old_district_name)
                                print_success_message()
                                break

                            else:
                                print_failure_message()

                        if crud_operation == "c":
                            districts_collection = District. get_specific_districts(
                                province_id)
                            print("\nAvailable Districts.\n" +
                                  str(districts_collection))
                            print(
                                "\nEnter the name of District to Delete")
                            district_name = input("Enter: ")
                            if district_name in districts_collection:
                                District.delete_district(district_name)
                                print_success_message()
                                break
                            else:
                                print_failure_message()

                    else:
                        print_failure_message()
                else:
                    print_failure_message()
        elif user_operation == 3:
            while True:
                provinces_collection = Province.get_all_provinces()
                print(
                    '\nTo access municipality data, you have to choose Province First.')
                print("\nHere are the Available Provinces.\n" +
                      str(provinces_collection))
                province_name = input(
                    "\nProvince name: ")
                if province_name in provinces_collection:
                    province_id = Province.get_province_id(province_name)
                    districts_collection = District.get_specific_districts(
                        province_id)
                    print(
                        '\nTo access municipality data, you have to choose District First')
                    print("\nHere are the Available Districts.\n" +
                          str(districts_collection))
                    district_name = input(
                        "\nDistrict name: ")

                    if district_name in districts_collection:
                        crud_operation = get_crud_operation("Municipality")
                        is_crud_validated = validate_crud_operation(
                            crud_operation)
                        if is_crud_validated:
                            district_id = District.get_district_id(
                                district_name)
                            if crud_operation == "a":
                                municipality_name = input(
                                    "\nMunicipality Name: ")
                                Municipality.add_municipality(
                                    municipality_name, district_id)
                                print_success_message()
                                break

                            elif crud_operation == "b":
                                municipalities_collection = Municipality.get_specific_municipalities(
                                    district_id)
                                print("Available Municipalities\n " +
                                      str(municipalities_collection))
                                print("Enter name of Municipality to Update:")
                                old_municipality_name = input("\nEnter: ")
                                if old_municipality_name in municipalities_collection:
                                    print(
                                        "Enter the new name of Municipality " + old_municipality_name)
                                    latest_municipality_name = input(
                                        "\nEnter: ")
                                    Municipality.update_municipality(
                                        latest_municipality_name, old_municipality_name)
                                    print_success_message()
                                    break

                                else:
                                    print_failure_message()

                            elif crud_operation == "c":
                                municipalities_collection = Municipality.get_specific_municipalities(
                                    district_id)
                                print("Available Municipalities\n " +
                                      str(municipalities_collection))
                                print("Enter name of Municipality to Delete:")
                                municipality_name = input("\nEnter: ")
                                if municipality_name in municipalities_collection:
                                    Municipality.delete_municipality(
                                        municipality_name)
                                    print_success_message()
                                    break

                                else:
                                    print_failure_message()
                        else:
                            print_failure_message()
                    else:
                        print_failure_message()
                else:
                    print_failure_message()

        elif user_operation == 4:
            provinces_collection = Province.get_all_provinces()
            while True:
                print(
                    '\nTo access Districts data, you have to choose Province First.')
                print("\nHere are the Available Provinces.\n" +
                      str(provinces_collection))
                province_name = input(
                    "\nProvince name: ")
                if province_name in provinces_collection:
                    province_id = Province.get_province_id(province_name)
                    districts_collection = District.get_specific_districts(
                        province_id)
                    print("\nDistricts: " + str(districts_collection))
                    print_success_message()
                    break
                else:
                    print_failure_message()

        elif user_operation == 5:
            districts_collection = District.get_all_districts()
            while True:
                print("\nAll districts:" + str(districts_collection))
                print("\nEnter the name of District to view its Municipalities.")
                district_name = input("\nInput: ")
                if district_name in districts_collection:
                    district_id = District.get_district_id(district_name)
                    municipalities_collection = Municipality.get_specific_municipalities(
                        district_id)
                    print("\n" + "Muncipalities List \n" +
                          str(municipalities_collection))
                    print_success_message()
                    break
                else:
                    print_failure_message()

        print("\nDo you want to continue the program(Y/N)")
        endProgram = input("\nInput: ").lower()
        if(endProgram == "n"):
            print("Program Ended!")
            break
    else:
        print("\nInput Invalid. Try Again!")
