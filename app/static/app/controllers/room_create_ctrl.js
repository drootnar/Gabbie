angular.module('app').controller('RoomCreateController', ['$scope', '$log', 'Room', function($scope, $log, Room) {

    $scope.create = function() {
        room = $scope.new_room;
        room.start_date = $scope.start_date + 'T' + $scope.start_time + ':00';
        room.end_date = $scope.end_date + 'T' + $scope.end_time + ':00';
        Room.create_room({}, room, function(data) {

        });
    };

}]);

