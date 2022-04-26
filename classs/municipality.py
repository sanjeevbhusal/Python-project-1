from utils.db_connection import db, mycursor


class Municipality:
    fetch_all_municipalities = "SELECT * FROM municipalities"
    fetch_certain_municipalities = "SELECT * FROM municipalities WHERE municipality_to_district = (%s)"
    insert_single_municipality = "INSERT INTO municipalities (municipality_name, municipality_to_district) VALUES (%s, %s)"
    update_single_municipality = "UPDATE municipalities SET municipality_name = (%s) WHERE municipality_name = (%s )"
    delete_single_municipality = "DELETE FROM municipalities WHERE municipality_name = (%s)"

    def __init__(self):
        pass

    def add_municipality(self, municipality_name, district_id):
        mycursor.execute(self.insert_single_municipality,
                         (municipality_name, int((district_id))))
        db.commit()

    def update_municipality(self, new_municipality, old_municipality):
        mycursor.execute(self.update_single_municipality,
                         (new_municipality, old_municipality))
        db.commit()

    def delete_municipality(self, municipality_name):
        mycursor.execute(self.delete_single_municipality, (municipality_name,))
        db.commit()

    def get_all_municipalities(self):
        municipalities_collection = []
        mycursor.execute(self.fetch_all_municipalities)
        for _, municipality_name, _ in mycursor:
            municipalities_collection.append(municipality_name)

        return municipalities_collection

    def get_specific_municipalities(self, district_id):
        municipalities_collection = []
        mycursor.execute(self.fetch_certain_municipalities,
                         (int(district_id),))
        for _, municipality_name, _ in mycursor:
            municipalities_collection.append(municipality_name)

        return municipalities_collection
