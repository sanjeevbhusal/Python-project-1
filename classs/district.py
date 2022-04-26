from utils.db_connection import db, mycursor


class District:
    age = 50

    def __init__(self):
        self.fetch_all_districts = "SELECT * FROM districts"
        self.fetch_certain_districts = "SELECT * FROM districts WHERE district_to_province = (%s) "
        self.update_single_district = "UPDATE districts SET district_name = (%s) WHERE district_name = (%s )"
        self.delete_single_district = "DELETE FROM districts WHERE district_name = (%s)"
        self.get_single_district_id = "SELECT district_id FROM districts WHERE district_name = (%s)"
        self.insert_single_district = "INSERT INTO districts (district_name, district_to_province) VALUES (%s, %s)"

    def add_district(self, district_name, province_id):
        mycursor.execute(self.insert_single_district,
                         (district_name, int(province_id)))
        db.commit()

    def update_district(self, latest_district_name, old_district_name):
        mycursor.execute(
            self.update_single_district, (latest_district_name, old_district_name))
        db.commit()

    def delete_district(self, district_name):
        mycursor.execute(self.delete_single_district, (district_name,))
        db.commit()

    def get_all_districts(self):
        districts_collection = []
        mycursor.execute(self.fetch_all_districts)
        for district in mycursor:
            districts_collection.append(district[1])

        return districts_collection

    def get_specific_districts(self, province_id):
        districts_collection = []
        mycursor.execute(self.fetch_certain_districts, (int(province_id),))
        for district in mycursor:
            districts_collection.append(district[1])

        return districts_collection

    def get_district_id(self, district_name):
        mycursor.execute(self.get_single_district_id, (district_name,))
        for i in mycursor:
            district_id, *_ = i
            return district_id

    def check_district_exist(self, district_name, districts_collection):
        True if district_name in districts_collection else False

    def get_district_name(districtsNameList):
        print("\nAvailable Districts:\n" + str(districtsNameList))
        print("\nPlease select the District name First: ")
        district_name = input(
            "\nInput: ")
        return district_name

    def print_age(self, num1, num2):
        print(num1 + num2 + self.age)
