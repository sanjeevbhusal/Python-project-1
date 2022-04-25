from db_connection import db, mycursor
from province import add_single_province, delete_province, get_province_name, get_province_id, delete_province, update_province,\
    get_all_provinces_name, truncate_province
from district import add_district, delete_district, get_district_name, get_entire_districts, get_district_id, delete_district, \
    get_all_districts_name, update_district, truncate_district
from municipality import delete_municipality, get_all_municipalities_name, add_municipality, update_municipality, delete_municipality,\
    truncate_municipality
from utils import get_user_operation, validate_user_operation, get_crud_operation, validate_crud_operation, validate_province, validate_district, validate_municipality

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
                        print("\nPlease Enter the name of Province to Create")
                        province_name = input("Input: ")
                        add_single_province(province_name)
                        print("\nThe Operation was Succesfull. " + province_name +
                              " got added Succesfully in Province List")
                        break

                    elif crud_operation == "b":
                        provincesNameList = get_all_provinces_name()
                        print(
                            "\nHere are the Available Provinces\n" + str(provincesNameList))
                        previous_province_name = input(
                            "\nPlease Enter the name of Province to Update: ")

                        if previous_province_name in provincesNameList:
                            latest_province_name = input(
                                "\nEnter Updated Name for Province " + previous_province_name + ": ")
                            update_province(latest_province_name,
                                            previous_province_name)
                            print(
                                "\n" + previous_province_name + " has been succesfully updated to " + latest_province_name)
                            break

                        else:
                            print("\n" + previous_province_name +
                                  "Does not Exist. Please Try Again!")

                    elif crud_operation == "c":
                        provincesNameList = get_all_provinces_name()
                        print(
                            "Here are the Available Provinces\n " + str(provincesNameList))
                        province_name = input(
                            "\nPlease Enter the name of Province to Delete: ")

                        if province_name in provincesNameList:
                            delete_province(province_name)
                            print("\n" + province_name +
                                  " has been succesfully deleted.")
                            break

                        else:
                            print("\n" + province_name +
                                  " does not Exist. Please Try Again!")
                else:
                    print("\nInvalid CRUD Operation. Please Try Again!")

        elif user_operation == 2:
            while True:
                province_exist, province_name = validate_province()
                if province_exist:
                    province_id = get_province_id(province_name)
                    crud_operation = get_crud_operation("District")
                    is_crud_validated = validate_crud_operation(crud_operation)
                    if is_crud_validated:
                        if crud_operation == "a":
                            district_name = input("\nEnter District Name: ")
                            add_district(district_name, province_id)
                            print("\n" + district_name + " added Succesfuly")
                            break

                        if crud_operation == "b":
                            district_exist, district_name = validate_district(
                                province_id)
                            if district_exist:
                                new_district_name = input(
                                    "\nEnter new Name of District " + district_name + ": ")
                                update_district(new_district_name,
                                                district_name)
                                print("\n" +
                                      district_name + " has been succesfully updated as " + new_district_name)
                                break

                            else:
                                print("\nDistrict " + district_name +
                                      " doesnot exist in database. Try Again!")

                        if crud_operation == "c":
                            district_exist, district_name = validate_district(
                                province_id)
                            if district_exist:
                                delete_district(district_name)
                                print("\n" + district_name +
                                      " has been succesfully deleted.")
                                break

                            else:
                                print("\n" + district_name +
                                      " District Does not Exist. Try Again!")

                    else:
                        print("Invalid CRUD Operation. Please Try Again!")
                else:
                    print("\nProvince " + province_name + " does not exist.")

        elif user_operation == 3:
            while True:
                province_exist, province_name = validate_province()
                if province_exist:
                    province_id = get_province_id(province_name)
                    district_exist, district_name = validate_district(
                        province_id)
                    if district_exist:
                        district_id = get_district_id(district_name)
                        crud_operation = get_crud_operation("Municipality")
                        is_crud_validated = validate_crud_operation(
                            crud_operation)
                        if is_crud_validated:
                            if crud_operation == "a":
                                municipality_name = input(
                                    "\nMunicipality Name: ")
                                add_municipality(
                                    municipality_name, district_id)
                                print("\nMunicipality " + municipality_name +
                                      " added Succesfuly.")
                                break

                            elif crud_operation == "b":
                                municipality_exist, municialipality_name = validate_municipality(
                                    district_id)
                                if municipality_exist:
                                    print("\nEnter latest municipality name. ")
                                    latest_municipality_name = input(
                                        "\nEnter :")
                                    update_municipality(
                                        latest_municipality_name, municialipality_name)
                                    print("\nMunicipality " + municialipality_name +
                                          " has been updated to " + municialipality_name)
                                    break

                                else:
                                    print("\n" + municialipality_name +
                                          " doesnot exist. try Again!")

                            elif crud_operation == "c":
                                municipality_exist, municialipality_name = validate_municipality(
                                    district_id)
                                if municipality_exist:
                                    delete_municipality(municipality_name)
                                    print("\nMunicipality " +
                                          municipality_name + " deleted succesfully.")
                                    break

                                else:
                                    print("\n" + municipality_name +
                                          "doesnot exist. Try Again later!")
                        else:
                            print("\nCrud Operation not recognized. Try Again.")
                    else:
                        print("\nDistrict " + district_name +
                              " doesnot exist. Try Again!")
                else:
                    print("\nProvince " + province_name +
                          " doesnot exist. Try Again! ")

        elif user_operation == 4:
            province_exist, province_name = validate_province()
            while True:
                if province_exist:
                    provinceID = get_province_id(province_name)
                    districtsNameList = get_all_districts_name(provinceID)
                    print("\nDistricts: " + str(districtsNameList))
                    break
                else:
                    print("\n" + province_name + "doesnot exist. Try Again!")

        elif user_operation == 5:
            districtsList = get_entire_districts()
            while True:
                print("All districts :" + str(districtsList))
                print("\nEnter the name of District to view its Municipalities.")
                district_name = input("\n Input: ")
                if district_name in districtsList:
                    districtID = get_district_id(district_name)
                    municipalitiesNameList = get_all_municipalities_name(
                        districtID)
                    print("\n" + str(municipalitiesNameList))
                    break
                else:
                    print("\nDistrict " + district_name +
                          "doesnot exist.Try Again!")

        print("\nDo you want to continue the program(Y/N)")
        endProgram = input("Input: ").lower()
        if(endProgram == "n"):
            print("Program Ended!")
            break
    else:
        print("\nInput Invalid. Try Again!")
