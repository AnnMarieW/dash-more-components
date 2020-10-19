# AUTO GENERATED FILE - DO NOT EDIT

timepicker <- function(id=NULL, value=NULL, format=NULL, maxDetail=NULL, maxTime=NULL, minTime=NULL, disabled=NULL, disableClock=NULL, locale=NULL) {
    
    props <- list(id=id, value=value, format=format, maxDetail=maxDetail, maxTime=maxTime, minTime=minTime, disabled=disabled, disableClock=disableClock, locale=locale)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Timepicker',
        namespace = 'dash_more_components',
        propNames = c('id', 'value', 'format', 'maxDetail', 'maxTime', 'minTime', 'disabled', 'disableClock', 'locale'),
        package = 'dashMoreComponents'
        )

    structure(component, class = c('dash_component', 'list'))
}
