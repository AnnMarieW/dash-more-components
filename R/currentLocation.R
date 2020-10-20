# AUTO GENERATED FILE - DO NOT EDIT

currentLocation <- function(id=NULL, date=NULL, latitude=NULL, longitude=NULL, accuracy=NULL, position=NULL, watch_position=NULL, update_now=NULL, high_accuracy=NULL) {
    
    props <- list(id=id, date=date, latitude=latitude, longitude=longitude, accuracy=accuracy, position=position, watch_position=watch_position, update_now=update_now, high_accuracy=high_accuracy)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'CurrentLocation',
        namespace = 'dash_more_components',
        propNames = c('id', 'date', 'latitude', 'longitude', 'accuracy', 'position', 'watch_position', 'update_now', 'high_accuracy'),
        package = 'dashMoreComponents'
        )

    structure(component, class = c('dash_component', 'list'))
}
