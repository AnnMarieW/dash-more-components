# AUTO GENERATED FILE - DO NOT EDIT

timer <- function(id=NULL, interval=NULL, disabled=NULL, n_intervals=NULL, max_intervals=NULL, timer=NULL, mode=NULL, duration=NULL, reset=NULL, fire=NULL, at_interval=NULL, rerun=NULL, messages=NULL, timer_format=NULL) {
    
    props <- list(id=id, interval=interval, disabled=disabled, n_intervals=n_intervals, max_intervals=max_intervals, timer=timer, mode=mode, duration=duration, reset=reset, fire=fire, at_interval=at_interval, rerun=rerun, messages=messages, timer_format=timer_format)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Timer',
        namespace = 'dash_more_components',
        propNames = c('id', 'interval', 'disabled', 'n_intervals', 'max_intervals', 'timer', 'mode', 'duration', 'reset', 'fire', 'at_interval', 'rerun', 'messages', 'timer_format'),
        package = 'dashMoreComponents'
        )

    structure(component, class = c('dash_component', 'list'))
}
