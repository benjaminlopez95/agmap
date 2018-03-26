<<<<<<< HEAD
$(window).on('map:init', function (e) {
    var detail = e.originalEvent ?
                 e.originalEvent.detail : e.detail;
    ...
    // Play with Leaflet.Coordinates
    L.marker([50.5, 30.5]).addTo(detail.map);
    ...

    // Optional specific behaviour for particular field
    map.on('map:loadfield', function (ev) {
        ...
        // Customize map for field
        console.log(ev.field, ev.fieldid);
        ...
    });
=======
$(window).on('map:init', function (e) {
    var detail = e.originalEvent ?
                 e.originalEvent.detail : e.detail;
    ...
    // Play with Leaflet.Coordinates
    L.marker([50.5, 30.5]).addTo(detail.map);
    ...

    // Optional specific behaviour for particular field
    map.on('map:loadfield', function (ev) {
        ...
        // Customize map for field
        console.log(ev.field, ev.fieldid);
        ...
    });
>>>>>>> e854a0e1d078f16e921a24a3e201c203befc9c4a
});