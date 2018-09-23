var app = angular.module('appRoutes', ['ngRoute', 'ui.router']);

app.config(function ($routeProvider, $locationProvider, $stateProvider, $urlRouterProvider) {
    $stateProvider
        .state('home', {
            url: '/',
            templateUrl: 'app/views/pages/home.html'
        })
        .state('about', {
            url: '/about',
            templateUrl: 'app/views/pages/about.html'
        })
        .state('login', {
            url: '/login',
            templateUrl: 'app/views/pages/users/login.html',
            authenticated: false
        })
        .state('student', {
            url: '/student',
            templateUrl: 'app/views/pages/student.html',
            authenticated: true
        })
        .state('register', {
            url: '/register',
            templateUrl: 'app/views/pages/users/register.html',
            authenticated: false
        });

    $locationProvider.html5Mode({
        enabled: true,
        requireBase: false
    });
});
