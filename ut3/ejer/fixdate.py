american_date = "12/31/20"

splitted_date = american_date.split("/")
month = splitted_date[0]
day = splitted_date[1]
year = splitted_date[2]
year = "20" + year
eu_date = [day, month, year]
spanish_date = "-".join(eu_date)
print(spanish_date)
