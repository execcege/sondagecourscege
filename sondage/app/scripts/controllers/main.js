'use strict';

angular.module('sondageApp')
  .controller('MainCtrl', ['$scope', 'coursService', function ($scope, coursService) {
    $scope.cours = coursService.getCours();
    $scope.$watch('cours', function() {
        $scope.selectedCourses = $scope.cours.filter(function(x){return x[2]==true})
    }, true);
    $scope.selectedCourses = $scope.cours.filter(function(x){return x[2]==true})

  }]);
