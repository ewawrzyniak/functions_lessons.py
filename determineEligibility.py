
#define function 
def determinElegibilityGraduate(name, credits, gpa, satScore,):
    if credits >= 120 and gpa >= 2.0 and satScore >= 800:
        print (f"{name} is eligable to graduate")
    else:
        print (f'{name} is not eligable to graduate')

def listOfMovies(name, genre, price):
    print(f'{name} is a {genre} of movie and costs ${price}')
    if genre == 'comedy':
        print('you will laugh a lot')
    elif genre == 'horror':
        print('You will be scared')
    else:
        print('you will be entertained')
