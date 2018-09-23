var raw = require('../text');
var PythonShell = require('python-shell');
module.exports = function (router) {



  data = raw;
  router.get('/data', function (req, res) {
    res.send(data);
  });

  router.get('/getGrades', function(req,res){

      PythonShell.PythonShell.run('./getDataoops.py', null, function (err, data) {
          if(err) res.send(err);
          res.send(data);
      });
  });
  router.get('/rawjson', function (req, res) {
    res.sendFile('/home/chiragm/GradingSystem/app/routes/text.json');
  });
  router.get('/rawCoursesJson', function (req, res) {
    res.sendFile('/home/chiragm/GradingSystem/app/routes/courses.json');
  });


  return router;
};
