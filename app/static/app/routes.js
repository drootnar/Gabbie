angular.module('app').config(function ($routeProvider) {
    $routeProvider
        .when('/', {
            controller: 'RoomIndexController',
            templateUrl: '/static/app/partials/room_index.html'
        })
        .when('/docs', {
            controller: 'APIReferenceController',
            templateUrl: '/admin/doc.html'
        })
        .otherwise({ redirectTo: '/' });
});