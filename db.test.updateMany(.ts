db.test.updateMany(
    {"isActive":true},
    {$set: {
        "City" : "Madurai"
    }}
);


db.training.find({},{"year":{}})

var pipeline= [
    { $match : {"Country":{$ne:"USA"}}},
    { $sort: {"Country":1}},
    { $limit : 1}   
];

db.training.aggregate(pipeline);

----------------

db.universities.aggregate([
  { $match : { country : 'Spain', city : 'Salamanca' } }
]).pretty()

-----------------

db.universities.aggregate([
  { $group : { _id : '$name', totaldocs : { $sum : 1 } } },
  { $out : 'aggResults' }
])


db.universities.aggregate([
    { $match : { name : 'USAL' } },
    { $unwind : '$students' },
    { $project : { _id : 0, name : 1, 'students.year' :1,'students.number' :1  }},
    { $sort : {'students.number': 1}},
    { $limit : 2}
  ])


  db.universities.aggregate([
    { $match : {"name" : "USAL"} },
    { $unwind : '$students' }
     ])


     db.universities.aggregate([
      { $match : { name : 'USAL' } },
      { $project : { _id : 0, name : 1 } },
      { $lookup : {
        from : 'courses'
      } }
    ]).pretty()



    use <database>;
var collstats = db.customers.stats()
for (var shard_name in collstats["shards"]) {
        print(shard_name + "," + collstats["shards"][shard_name].size + "," + collstats["shards"][shard_name].storageSize);
}