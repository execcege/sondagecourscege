'use strict';

angular.module('sondageApp')
  .controller('QuestionsCtrl', ['$scope', '$http', '$location', 'coursService', function ($scope, $http, $location, coursService) {
    $scope.cours = coursService.getCours();
    $scope.selectedCourses = $scope.cours.filter(function(x){return x[2]==true});

    $scope.cour = null;
    $scope.form = null;
    var responses = [];

    $scope.getNext= function(){
        if($scope.cour != null){

            $scope.form['sigle']= $scope.cour[0];
            responses.push($scope.form);
            $scope.form = newForm();

            $scope.cour = $scope.selectedCourses.shift();

        }
        else
        {
            $scope.form = newForm();

            $scope.cour = $scope.selectedCourses.shift();
        }

        if($scope.cour === undefined){
            if(responses.length != 0){
                var matricule = "";
                matricule = prompt("Afin de pouvoir contacter les gens pour plus d'informations, il est nécessaire pour nous de connaître votre matricule. Sâchez toutefois que ce sondage reste confidentiel. Si vous ne souhaitez pas être contacté, laissez ce champ vide.");
                var data = {'matricule':matricule, 'responses': responses};
                $http.post("/api/Answer", data)
            }
            $location.path('/thanks');
        }

    };


    var newForm = function(){
        return {
            'no1' : null,
            'no2' : null,
            'no3' : null,
            'no4' : null,
            'no5' : null,
            'no6' : null,
            'no7' : null,
            'no8' : null,
            'no9' : null,
            'no10' : null,
            'no11' : null,
            'no12' : null,
            'no13' : null,
            'no14' : null,
            'no15' : null,
            'no16' : null,
            'no17' : null,
            'no18' : null,
            'no19' : null,
            'no20' : null,
            'no21' : null,
            'no22' : null,
            'no23' : null,
            'no24' : null,
            'no25' : null,
            'no26' : null,
            'no27' : null,
            'no28' : null,
            'no29' : "",
            'no30' : ""
        }
    };

    $scope.getNext();
  }]);
