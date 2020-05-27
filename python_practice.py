
counties= ["Arapahoe", "Denver", "Jefferson"]
if "El Paso" in counties and "Arapahoe" in counties:
    print("El Paso and Arapahoe are in the counties list")
else:
    print("El Paso or Arapahoe is not in the counties list")

counties_dict={"Arapahoe":422829,"Denver":463353,"Jefferson":432438}
for county in counties_dict:
    print(county)
for county in counties_dict.keys():
    print(county)
for voters in counties_dict.values():
    print(voters)
for county in counties_dict:
    print(counties_dict[county])
for key, value in counties_dict.items():
    print(key, value)
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    print(county_dict)


