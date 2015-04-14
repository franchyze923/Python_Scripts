def allowed_dating_age(my_age):
    girls_age = my_age/2 +7
    return girls_age

buckys_limit = allowed_dating_age(27)
print('Bucky can date' , buckys_limit)

fran_limit = allowed_dating_age(23)
print('fran can date' , fran_limit)

bob_limit = allowed_dating_age(77)
print('Bob can date' , bob_limit)