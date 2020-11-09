# AUTO GENERATED FILE - DO NOT EDIT

geolocation <- function(id=NULL, local_date=NULL, timestamp=NULL, position=NULL, position_error=NULL, show_alert=NULL, watch_position=NULL, update_now=NULL, high_accuracy=NULL, maximum_age=NULL, timeout=NULL) {
    
    props <- list(id=id, local_date=local_date, timestamp=timestamp, position=position, position_error=position_error, show_alert=show_alert, watch_position=watch_position, update_now=update_now, high_accuracy=high_accuracy, maximum_age=maximum_age, timeout=timeout)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Geolocation',
        namespace = 'dash_more_components',
        propNames = c('id', 'local_date', 'timestamp', 'position', 'position_error', 'show_alert', 'watch_position', 'update_now', 'high_accuracy', 'maximum_age', 'timeout'),
        package = 'dashMoreComponents'
        )

    structure(component, class = c('dash_component', 'list'))
}
