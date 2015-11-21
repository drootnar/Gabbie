angular.module('app').controller('RoomIndexController', ['$scope', '$log', 'Room', function($scope, $log, Room) {

    init = function() {
        Room.query({}, function(data) {$scope.fetch_page(data)});
    };

    init();

    $scope.fetch_page = function(data) {
            $scope.rooms = data.results;
        };


}]);

