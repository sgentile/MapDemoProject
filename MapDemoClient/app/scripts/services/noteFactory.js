'use strict';

angular.module('MapDemoClientApp')
  .factory('noteFactory', function ($resource) {
    return $resource('/note/:id',  {id:'@id'}, {

    });
  });
