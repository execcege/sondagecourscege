'use strict';

angular
  .module('sondageApp', [
    'ngCookies',
    'ngResource',
    'ngSanitize',
    'ngRoute',
    'mm.foundation'
  ])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl'
      })
        .when('/questions', {
            templateUrl: 'views/questions.html',
            controller: 'QuestionsCtrl'
        })
        .when('/thanks', {
            templateUrl: 'views/thanks.html',
            controller: 'ThanksCtrl'
        })
      .otherwise({
        redirectTo: '/'
      });
  });
