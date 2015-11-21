angular.module('app').controller('RoomIndexController', ['$scope', '$log', 'Room', function($scope, $log, Room) {

    init = function() {
        Room.query({}, function(data) {$scope.fetch_page(data)});
    };

    init();

    $scope.fetch_page = function(data) {
        $scope.rooms = data.results;
    };

    $scope.set_current_room = function(id) {
        $scope.current_id = id;
    };

    $scope.messages = [
        {'author': 'Wojciech', 'text': 'dafsd asdfl asd lkasd fjsadlf jalsdfj lsadjf ;aksdf lkasdjf asd lkfjsd fa'},
        {'author': 'Wojciech', 'text': 'dafsd asdfl asd lkasd fjsadlf jalsdfj lsadjf ;aksdf lkasdjf asd lkfjsd fa'},
        {'author': 'Wojciech', 'text': 'dafsd asdfl asd lkasd fjsadlf jalsdfj lsadjf ;aksdf lkasdjf asd lkfjsd fa'},
        {'author': 'Wojciech', 'text': 'dafsd asdfl asd lkasd fjsadlf jalsdfj lsadjf ;aksdf lkasdjf asd lkfjsd fa'},
        {'author': 'Wojciech', 'text': 'dafsd asdfl asd lkasd fjsadlf jalsdfj lsadjf ;aksdf lkasdjf asd lkfjsd fa'},
        {'author': 'Wojciech', 'text': 'dafsd asdfl asd lkasd fjsadlf jalsdfj lsadjf ;aksdf lkasdjf asd lkfjsd fa'},
        {'author': 'Wojciech', 'text': 'dafsd asdfl asd lkasd fjsadlf jalsdfj lsadjf ;aksdf lkasdjf asd lkfjsd fa'}
    ]

}]);

