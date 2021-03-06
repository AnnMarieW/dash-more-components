# AUTO GENERATED FILE - DO NOT EDIT

datetimePicker <- function(id=NULL, value=NULL, format=NULL, maxDetail=NULL, minDetail=NULL, maxTime=NULL, minTime=NULL, maxDate=NULL, minDate=NULL, disabled=NULL, disableClock=NULL, locale=NULL, returnValue=NULL) {
    
    props <- list(id=id, value=value, format=format, maxDetail=maxDetail, minDetail=minDetail, maxTime=maxTime, minTime=minTime, maxDate=maxDate, minDate=minDate, disabled=disabled, disableClock=disableClock, locale=locale, returnValue=returnValue)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DatetimePicker',
        namespace = 'dash_more_components',
        propNames = c('id', 'value', 'format', 'maxDetail', 'minDetail', 'maxTime', 'minTime', 'maxDate', 'minDate', 'disabled', 'disableClock', 'locale', 'returnValue'),
        package = 'dashMoreComponents'
        )

    structure(component, class = c('dash_component', 'list'))
}
