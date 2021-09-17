
def season (num):
    
    if (num == 12 or (num <= 2 and num != 0)):
        return ("зима")
    elif  ((num <= 5 and num > 2)):
        return ("весна")
    elif  ((num <= 8 and num > 5)):
        return ("лето")
    elif  ((num <= 11 and num > 8)):
        return ("осень")
    else:
        return ("такого мес. неть")

var = int(input("введите номер мес: "))
print(season(var))