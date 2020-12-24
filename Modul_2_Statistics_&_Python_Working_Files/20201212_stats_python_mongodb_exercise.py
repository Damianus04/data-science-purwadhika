# 1) display all documents
db.restaurants.find()

# 2) display the fields restaurant_id, name, borough and cuisine
db.restaurants.find({}, {restaurant_id: 1, name: 1,
                         borough: 1, cuisine: 1}).pretty()

# 3) display the fields restaurant_id, name, borough and cuisine, but exclude the field _id
db.restaurants.find({}, {_id: 0, restaurant_id: 1, name: 1,
                         borough: 1, cuisine: 1}).pretty()

# 4)  display the fields restaurant_id, name, borough and zip code, but exclude the field _id
db.restaurants.find({}, {_id: 0, restaurant_id: 1, name: 1,
                         borough: 1, "address.zipcode": 1}).pretty()

# 5) display all the restaurant which is in the borough Bronx
db.restaurants.find({"borough": "Bronx"}).pretty()

# 6) to display the first 5 restaurant which is in the borough Bronx
db.restaurants.find({"borough": "Bronx"}).limit(5)

# 7) display the next 5 restaurants after skipping first 5 which are in the borough Bronx
db.restaurants.find({'borough': 'Bronx'}).limit(5).skip(5)

db.restaurants.find({}, {_id: 0, name: 1}).limit(5).skip(5)

# 8)  find the restaurants who achieved a score more than 90
db.restaurants.find({grades: {$elemMatch: {"score": {$gt: 90}}}}).pretty()

# 9) find the restaurants that achieved a score, more than 80 but less than 100
db.restaurants.find({$and: [{grades: {$elemMatch: {"score": {$gt: 80}}}}, {grades: {$elemMatch: {'score': {$lt: 100}}}}]}).pretty() - -> need to be checked

# 10) find the restaurants which locate in latitude value less than -95.754168
db.restaurants.find({"address.coord": {$lt: -95.754168}}).pretty()

# 11)  find the restaurants that do not prepare any cuisine of 'American' and their grade score more than 70 and latitude less than -65.754168

- -> space should be added("American ")
db.restaurants.find({$and: [{"cuisine": {$ne: "American"}}, {"grades.score": {$gt: 70}}, {"address.coord": {$lt: -65}}]}).pretty() - -> still need revision

db.restaurants.find(
    {$and:
     [
         {"cuisine": {$ne: "American "}},
         {"grades.score": {$gt: 70}},
         {"address.coord": {$lt: -65.754168}}
     ]
     }
)


# 12. find the restaurants which do not prepare any cuisine of 'American' and achieved a score more than 70 and located in the longitude less than -65.754168. Note : Do this query without using $and operator
db.restaurants.find({"cuisine": {$ne: "American "}, "grades.score": {$gt: 70}, "address.coord": {$lt: -65}}).pretty()
