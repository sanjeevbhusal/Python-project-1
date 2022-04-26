from utils.db_connection import db, mycursor


class Province:
    fetch_all_provinces = "SELECT * FROM provinces"
    fetch_certain_provinces = "SELECT * FROM provinces WHERE "
    insert_single_province = "INSERT INTO provinces (province_name) VALUES (%s)"
    update_single_province = "UPDATE provinces SET province_name = (%s) WHERE province_name = (%s )"
    delete_single_province = "DELETE FROM provinces WHERE province_name = (%s)"
    get_single_province_id = "SELECT province_id FROM provinces WHERE province_name = (%s)"

    def _init_(self):
        pass

    def add_province(self, province_name):
        mycursor.execute(self.insert_single_province, (province_name,))
        db.commit()

    def delete_province(self, province_name):
        mycursor.execute(self.delete_single_province, (province_name,))
        db.commit()

    def update_province(self, latest_province_name, previous_province_name):
        mycursor.execute(
            self.update_single_province, (latest_province_name, previous_province_name))
        db.commit()

    def get_province_id(self, province_name):
        mycursor.execute(self.get_single_province_id, (province_name,))
        for i in mycursor:
            province_id, *_ = i
            return province_id

    def get_all_provinces(self):
        provinces_collections = []
        mycursor.execute(self.fetch_all_provinces)
        for _, province_name in mycursor:
            provinces_collections.append(province_name)

        return provinces_collections

    def get_province_name(provincesNameList):
        print("\nPlease select the Province name First. ")
        print("\nAvailable Provinces " + str(provincesNameList))
        province_name = input(
            "\nInput: ")
        return province_name

    def take_input(self):
        print("\nPlease Enter the name of Province to Create")
        province_name = input("Input: ")
        return province_name

    def print_success_message(self):
        print("\nCongratulations!The Operation was Succesfull.")

    def print_failure_message(self):
        print("\nOops!Looks like You did some Mistake. Try Again!!")
