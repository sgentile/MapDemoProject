'use strict';

angular.module('MapDemoClientApp')
  .controller('MainCtrl', function ($scope, noteFactory) {

    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];

    $scope.awesomeThings = noteFactory.get();

  });
