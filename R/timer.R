# AUTO GENERATED FILE - DO NOT EDIT

timer <- function(id=NULL, interval=NULL, disabled=NULL, n_intervals=NULL, max_intervals=NULL, timer=NULL, mode=NULL, duration=NULL, reset=NULL, fire_times=NULL, at_fire_time=NULL, rerun=NULL, messages=NULL, timer_format=NULL, style=NULL, class_name=NULL) {
    
    props <- list(id=id, interval=interval, disabled=disabled, n_intervals=n_intervals, max_intervals=max_intervals, timer=timer, mode=mode, duration=duration, reset=reset, fire_times=fire_times, at_fire_time=at_fire_time, rerun=rerun, messages=messages, timer_format=timer_format, style=style, class_name=class_name)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Timer',
        namespace = 'dash_more_components',
        propNames = c('id', 'interval', 'disabled', 'n_intervals', 'max_intervals', 'timer', 'mode', 'duration', 'reset', 'fire_times', 'at_fire_time', 'rerun', 'messages', 'timer_format', 'style', 'class_name'),
        package = 'dashMoreComponents'
        )

    structure(component, class = c('dash_component', 'list'))
}
