# AUTO GENERATED FILE - DO NOT EDIT

timer <- function(id=NULL, interval=NULL, disabled=NULL, n_intervals=NULL, max_intervals=NULL, remaining_duration=NULL, countdown_duration=NULL, reset=NULL) {
    
    props <- list(id=id, interval=interval, disabled=disabled, n_intervals=n_intervals, max_intervals=max_intervals, remaining_duration=remaining_duration, countdown_duration=countdown_duration, reset=reset)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Timer',
        namespace = 'dash_more_components',
        propNames = c('id', 'interval', 'disabled', 'n_intervals', 'max_intervals', 'remaining_duration', 'countdown_duration', 'reset'),
        package = 'dashMoreComponents'
        )

    structure(component, class = c('dash_component', 'list'))
}
