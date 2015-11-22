app = angular.module('app', ['ngRoute', 'ngResource', 'ui.bootstrap'])

app.factory("Room", function ($resource) {
    return $resource(
        "/api/v1/rooms/:id",
        {id: '@id'},
        {
            'query': {method:'GET', url: '/api/v1/rooms', isArray:false},
            'messages': {method:'GET', url: '/api/v1/rooms/:id/messages', isArray:false},
            'create': {method:'POST', url: '/api/v1/rooms/:id/messages_web'}
        }
    );
});
