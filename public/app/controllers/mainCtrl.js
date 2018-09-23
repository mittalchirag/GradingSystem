angular.module('mainController', ['authServices'])

  .controller('mainCtrl', function ($interval, $cookies, $location, $window, $timeout, RawData, $rootScope) {
    var app = this;

    app.showG=false;
    app.username = "chirag";
    app.data = new Array;
    app.courses = new Array;
    app.getData = function () {
      RawData.getrawdata().then(function (data) {
        console.log(data);
        app.data = data.data;
        console.log(app.data);
      });

    };
    app.getCourseData = function () {
      RawData.getcoursedata().then(function (data) {
        console.log(data);
        app.courses = data.data;
        console.log(app.data);
      });

    };
    app.getGrading= function(){
      RawData.getGrades().then(function(data){
        console.log(data);
      });

    }
    app.toggle = function(){
      app.showG=!(app.showG);
    };
    app.getData();
    app.getCourseData();

  });
