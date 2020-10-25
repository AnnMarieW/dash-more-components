# AUTO GENERATED FILE - DO NOT EDIT

currentLocation <- function(id=NULL, local_date=NULL, timestamp=NULL, position=NULL, position_error=NULL, watch_position=NULL, update_now=NULL, high_accuracy=NULL) {
    
    props <- list(id=id, local_date=local_date, timestamp=timestamp, position=position, position_error=position_error, watch_position=watch_position, update_now=update_now, high_accuracy=high_accuracy)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'CurrentLocation',
        namespace = 'dash_more_components',
        propNames = c('id', 'local_date', 'timestamp', 'position', 'position_error', 'watch_position', 'update_now', 'high_accuracy'),
        package = 'dashMoreComponents'
        )

    structure(component, class = c('dash_component', 'list'))
}
