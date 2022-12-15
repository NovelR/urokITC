# authorization
#______________________
# baza = {
#     'Admin':{
#         'name': 'marselle',
#         'phone': '7711320882',
#         'balance': 100000,
#         'password': '12312321'
#     },
#     'endless':{
#         'name': 'roman',
#         'phone': "7017132683",
#         'balanc':100000,
#         }
# }
# key = None

# while  True:
#         table = int(input("""
#       1 >>> Зарегистрироваться
#       2 >>> Авторизоваться
#       3 >>> Перевод баланса
#       4 >>> Список пользователей
#       5 >>> Информация
#       6 >>> Номер телефона   
#       7 >>> Выйти
#       >>> """))
#         if table == 1:
#             if key in None:
#                 login = input('Введите логин: ')
#                 if login.isalpha():
#                     name = input('Введите имя:')
#                     if name.isalpha():
#                         phone = input('Введите номер телефона +7')
#                         if phone.isdigit():
#                             password = input('Введите пароль: ')
#                             password2 = input('Введите пароль повторно: ')
#                             while password != password2:
#                                 password = input('Введите пароль: ')
#                                 password2 = input('Введите пароль повторно: ')
#                             else:
#                                 baza.update({
#                                 login: {
#                                     'name': name,
#                                     'phone': phone,
#                                     'balance': 100,
#                                     'password': password2,
#                                 }
#                             })
#                                 key = login
#                         else:
#                             print('Номер должен состоят только из цифр')
#                     else:
#                         print('Имя должен быть только из букв')
#                 else:
#                     print('Логин должен быть только из букв')
#             else:
#                 print('Вы уже зарегистрированы')
#         elif table == 2:
#             if key is None:
#                 login = input('Введите логин: ')
#                 if login in baza.keys():
#                     password = input('Введите пароль: ')
#                     if password == baza[login]['password']:
#                         print('Вы авторизовались')
#                         key = login
#                     else:
#                         print('У Вас пароль не правильный')    
#                 else:
#                     print('В базе нет такого пользователя')
#             else:
#                 print('Вы уже авторизованы')   
#         elif table == 3:
#             if key is not None:
#                 login_komu = input('Введите логин получателя: ')
#                 if login_komu.isalpha() and login_komu in baza.keys():
#                     summa = int(input('Введите сумму перевода: '))
#                     if summa <= baza[login]['balance']:
#                         baza[login]['balance'] -= summa
#                         baza[login_komu] += summa
#                         print('Отправлено')
#                     else:
#                         ('У Вас не хватает денег для перевода')
#                 else:
#                     ('Не верно указали логин или нет такого пользователя')        
#             else:
#                 print('Сначала авторизуйся')
#         elif table == 4:
#             if key is not None:
#                 print(baza)
#             else:
#                 print('Вы ещё не авторизованы')
#         elif table == 5:
#             if key is not None:
#                 print(f'''
#             Ващи данные
#             login:{key}
#             name: {baza[login]['name']}
#             balance: {baza[login]['balance']}
#             password: {baza[login]['']}
#             ''')
#             else:
#                 print('Сначало авторизуйся')
#         elif table == 6:
#             if key is not None:
#                 print(f'phone number +7{baza[login]["phone"]}')
#             else:
#                 print('Сначала авторизуйся')
#         elif table == 7:
#             key = None
#             print('Вы выщли из аккаунта')

   