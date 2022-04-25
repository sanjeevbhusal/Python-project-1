import mysql.connector
db = mysql.connector.connect(
    host="localhost", user="root", passwd="1234", database="python_intern_1")
mycursor = db.cursor()


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


# createTables()


#############################################  SQL QUERIES  ############################################
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


#############################################  PROVINCES  ############################################
def add_single_province(province_name):
    mycursor.execute(insert_single_province, (province_name,))
    db.commit()


def get_province_name(provincesNameList):
    print("\nTo perform Operations on District, please select the Province name First. ")
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

#############################################  DISTRICTS  ############################################


def add_district(district_name, province_id):
    mycursor.execute(insert_single_district, (district_name, int(province_id)))
    db.commit()


def get_district_name(districtsNameList):
    print("\nAvailable Districts" + str(districtsNameList))
    print("\nTo perform Operations on Municipality please select the District name First: ")
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

#############################################  MUNICIPALITIES  ############################################


def get_all_municipalities_name(district_id):
    municipalitiesList = []
    mycursor.execute(fetch_certain_municipalities, (int(district_id),))
    for municipality_id, municipality_name, municipality_to_province in mycursor:
        municipalitiesList.append(municipality_name)

    return municipalitiesList


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


while True:
    print('''\nEnter 1 for inserting/updating/deleting a Province
Enter 2 for inserting/updating/deleting a District
Enter 3 for inserting/updating/deleting a Municipality
Enter 4 for listing all Districts of a Province
Enter 5 for listing all Municipalities of a Province\n''')
    user_operation = input("Input: ")

    if user_operation != 1 and user_operation != 2 and user_operation != 3 and user_operation != 4 and user_operation != 5:
        print("\nInput Invalid. Try Again!")
    else:
        user_operation = int(user_operation)
        if user_operation == 1:
            while True:
                print('''\nEnter a for inserting a Province
Enter b updating a Province
Enter c for deleting a Province\n
                         ''')
                crud_operation = input("Input: ")

                if crud_operation != "a" and crud_operation != "b" and crud_operation != "c":
                    print("Invalid CRUD Operation. Please Try Again!")

                else:
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

        elif user_operation == 2:
            provincesNameList = get_all_provinces_name()
            while True:
                provinceName = get_province_name(provincesNameList)
                if provinceName in provincesNameList:
                    provinceID = get_province_id(provinceName)
                    print(
                        "\nEnter a for creating, b for updating, c for deleting a District. ")
                    crud_operation = input(
                        "\nInput: ")

                    if crud_operation != "a" and crud_operation != "b" and crud_operation != "c":
                        print("\nCrud Operation not recognized.Try Again")

                    else:
                        if crud_operation == "a":
                            districtName = input("\nEnter District Name: ")
                            add_district(districtName, provinceID)
                            print("\n" + districtName + " added Succesfuly")
                            break

                        if crud_operation == "b":
                            availableDistricts = get_all_districts_name(
                                provinceID)
                            print("\nAvailable Districts: \n" +
                                  str(availableDistricts))
                            previousDistrictName = input(
                                "\nEnter the name of District to Update: ")

                            if previousDistrictName in availableDistricts:
                                latestDistrictName = input(
                                    "\nEnter new Name of District " + previousDistrictName + ": ")
                                update_district(latestDistrictName,
                                                previousDistrictName)
                                print("\n" +
                                      previousDistrictName + " has been succesfully updated as " + latestDistrictName)
                                break

                            else:
                                print("\nDistrict " + previousDistrictName +
                                      " doesnot exist in database. Try Again!")

                        if crud_operation == "c":
                            availableDistricts = get_all_districts_name(
                                provinceID)
                            print("\nAvailable Districts: \n" +
                                  str(availableDistricts))
                            districtName = input(
                                "\nEnter the name of District to Delete: ")

                            if districtName in availableDistricts:
                                delete_district(districtName)
                                print("\n" + districtName +
                                      " has been succesfully deleted.")
                                break

                            else:
                                print("\n" + districtName +
                                      " District Does not Exist. Try Again!")

                else:
                    print("\nProvince " + provinceName + " does not exist.")

        elif user_operation == 3:
            provincesNameList = get_all_provinces_name()
            while True:
                provinceName = get_province_name(provincesNameList)

                if provinceName in provincesNameList:
                    provinceID = get_province_id(provinceName)
                    districtsNameList = get_all_districts_name(provinceID)
                    districtName = get_district_name(districtsNameList)

                    if districtName in districtsNameList:
                        districtID = get_district_id(districtName)
                        print(
                            "\nEnter a for creating, b for updating, c for deleting a Municipality.")
                        crud_operation = input(
                            "\nInput: ")

                        if crud_operation != "a" and crud_operation != "b" and crud_operation != "c":
                            print("\nCrud Operation not recognized. Try Again.")

                        else:
                            municipalitiesNameList = get_all_municipalities_name(
                                districtID)

                            if crud_operation == "a":
                                municipality_name = input(
                                    "\nMunicipality Name: ")
                                add_municipality(municipality_name, districtID)
                                print("\nMunicipality " + municipality_name +
                                      " added Succesfuly.")
                                break

                            elif crud_operation == "b":
                                print("\nMunicipalities List \n" +
                                      str(municipalitiesNameList))
                                previous_municipality_name = input(
                                    "\nEnter previous name : ")
                                if previous_municipality_name in municipalitiesNameList:
                                    latest_municipality_name = input(
                                        "\nEnter latest Name: ")
                                    update_municipality(
                                        latest_municipality_name, previous_municipality_name)
                                    print("\nMunicipality " + previous_municipality_name +
                                          " has been updated to " + latest_municipality_name)
                                    break

                                else:
                                    print("\n" + previous_municipality_name +
                                          " doesnot exist. try Again!")

                            elif crud_operation == "c":
                                print("\nAvailable Municipalities  \n" +
                                      str(municipalitiesNameList))
                                municipality_name = input(
                                    "\nEnter the name of Municipality to delete: ")
                                if municipality_name in municipalitiesNameList:
                                    delete_municipality(municipality_name)
                                    print("\nMunicipality " +
                                          municipality_name + " deleted succesfully.")
                                    break

                                else:
                                    print("\n" + municipality_name +
                                          "doesnot exist. Try Again later!")

                    else:
                        print("\nDistrict " + districtName +
                              " doesnot exist. Try Again!")

                else:
                    print("\nProvince " + provinceName +
                          " doesnot exist. Try Again! ")

        elif user_operation == 4:
            provincesNameList = get_all_provinces_name()
            print("\nHere are the Available Provinces\n " + str(provincesNameList))
            while True:
                print("\nPlease Enter the name of Province to view Districts:")
                province_name = input("\nEnter: ")
                if province_name in provincesNameList:
                    provinceID = get_province_id(province_name)
                    districtsNameList = get_all_districts_name(provinceID)
                    print("\nDistricts: " + str(districtsNameList))
                    break

                else:
                    print("\n" + province_name + "doesnot exist. Try Again!")

        elif user_operation == 5:
            districtsNameList = get_entire_districts()
            while True:
                print("\nHere are the Available Districts\n " +
                      str(districtsNameList))
                print("\nPlease Enter the name of District to view its Municipalities:")
                district_name = input("Input: ")
                if district_name in districtsNameList:
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
