# AUTO GENERATED FILE - DO NOT EDIT

countdownTimer <- function(id=NULL, starting_duration=NULL, pause=NULL, remaining_duration=NULL) {
    
    props <- list(id=id, starting_duration=starting_duration, pause=pause, remaining_duration=remaining_duration)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'CountdownTimer',
        namespace = 'dash_more_components',
        propNames = c('id', 'starting_duration', 'pause', 'remaining_duration'),
        package = 'dashMoreComponents'
        )

    structure(component, class = c('dash_component', 'list'))
}
