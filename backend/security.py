# from Models.user import UserModel

# def authenticate(firstname, password):
#     user = UserModel.find_by_surname(surname)
#     if user and user.password == password:
#         return user

# def identity(payload):
#     user_id = payload['identity']
#     return UserModel.find_by_id(user_id)

# def authenticate_e_mail(e_mail, password):
#     user = UserModel.find_by_email(e_mail) #if no email found, return none
#     if user and user.password == password:
#         return user

# def identity_id(payload):
#     user_id = payload['identity']
#     return UserModel.find_by_email(user_id)




# Simulierung einer Database
#users =[
 #   ('milena.hofmann@uniwuerzburg.de', "ABC124")
    #(1, 'Milena', 'Hofmann', 'milena.hofmann@uniwuerzburg.de', 'Uni-Wuerzburg', 'Funktion', 0, "ABC124"),
    #(2, 'Norman', 'Pytel', 'norman.pytel@uniwuerzburg.de', 'Uni-Wuerzburg', 'Funktion', 0, "ABC123")
#]

#user_email_mapping = {u.user_email: u for u in users} # Abrufen der Email eines Users
#userid_mapping = {u.id: u for u in users}

#user_email_mapping = {'e-mail':   'ID': 1,
 # 'firstname': 'Norman',
  #'surname': 'Pytel', 
  #'e_mail': 'norman.pytel@uniwuerzburg.de', #obligatorisch  UI bitte Email einfügen
  #'orga_name': 'Uni-Wuerzburg',
  #'function': 'Funktion',
  #'del_kz': 0,
  #'pw' = "ABC123"
   # }

#data = Json User ID?
#userid_mapping = { 1 :  { 'ID': 1,
#  'firstname': 'Norman',
#  'surname': 'Pytel', 
#  'e_mail': 'norman.pytel@uniwuerzburg.de', #obligatorisch  UI bitte Email einfügen
#  'orga_name': 'Uni-Wuerzburg',
#  'function': 'Funktion',
#  'del_kz': 0,
#  'pw' = "ABC123"
#    }
#}