from COURSE.MODULE5.main import app, collection_name

from COURSE.MODULE5 import exo


# print()
# print(dir(main))



valid_keys = ['name', 'phone', 'email', 'address', 'latlng', 'salary', 'age', 'latlon', 'currency', 'conv_to_xof', 'country', 'flag']

@app.get("/all-contacts_")
def get_all_contacts():

    list_contacts = list(collection_name.find())
    return {"new_all_contacts": [ {k:list_contacts[i][k] for k in valid_keys} for i in range(len(list_contacts))] }
