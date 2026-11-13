name_dict = {"name": "Himadhar", "age": 26}
print(name_dict["name"])

book_dict = {"Book Name": "Learn Python", "Page Count": 20}
book_dict["Page Count"] = 30
print(book_dict)

city_dict = {"name": "Himadhar"}
city_dict["city"] = "Nellore"
print(city_dict)

score_list = {"Python":20,
              ".Net":40}
print(score_list)
for key, value in score_list.items():
    print(key, value)

details_list = {"name": "Hima", "age": 25}
email = details_list.get("Email")
print(email)