angular.module('app').controller('RoomIndexController', ['$scope', '$log', 'Room', function($scope, $log, Room) {

    $scope.messages = [];

    init = function() {
        Room.query({}, function(data) {$scope.fetch_page(data)});
    };

    init();

    $scope.fetch_page = function(data) {
        $scope.rooms = data.results;
    };

    $scope.set_current_room = function(id) {
        $scope.current_id = id;
        Room.messages({'id': $scope.current_id}, function(data) {
            $scope.messages = data.results;
        });
    };

    $scope.send_message = function(id) {
        Room.create({'id': id}, $scope.new_message, function(data) {
            Room.messages({'id': $scope.current_id}, function(data) {
                $scope.messages = data.results;
            });
        });
    }

}]);

