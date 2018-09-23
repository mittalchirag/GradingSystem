angular.module('authServices', [])

    .factory('RawData', function ($http) {
        rawData = {};

        //RawData.getLanguages()
        rawData.getrawdata = function () {
            return $http.get('/api/rawjson');
        };
        rawData.getcoursedata =function(){
            return $http.get('api/rawCoursesJson');
        };
        rawData.getGrades= function(){
            return ($http.get('api/getGrades'));
        };
        return rawData;
    });