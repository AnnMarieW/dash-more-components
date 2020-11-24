# AUTO GENERATED FILE - DO NOT EDIT

datetimepicker <- function(id=NULL, value=NULL, setValue=NULL, format=NULL, maxDetail=NULL, minDetail=NULL, maxTime=NULL, minTime=NULL, maxDate=NULL, minDate=NULL, disabled=NULL, disableClock=NULL, locale=NULL, returnValue=NULL, required=NULL, yearPlaceholder=NULL, monthPlaceholder=NULL, dayPlaceholder=NULL, hourPlaceholder=NULL, minutePlaceholder=NULL, secondPlaceholder=NULL, closeWidgets=NULL) {
    
    props <- list(id=id, value=value, setValue=setValue, format=format, maxDetail=maxDetail, minDetail=minDetail, maxTime=maxTime, minTime=minTime, maxDate=maxDate, minDate=minDate, disabled=disabled, disableClock=disableClock, locale=locale, returnValue=returnValue, required=required, yearPlaceholder=yearPlaceholder, monthPlaceholder=monthPlaceholder, dayPlaceholder=dayPlaceholder, hourPlaceholder=hourPlaceholder, minutePlaceholder=minutePlaceholder, secondPlaceholder=secondPlaceholder, closeWidgets=closeWidgets)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Datetimepicker',
        namespace = 'dash_more_components',
        propNames = c('id', 'value', 'setValue', 'format', 'maxDetail', 'minDetail', 'maxTime', 'minTime', 'maxDate', 'minDate', 'disabled', 'disableClock', 'locale', 'returnValue', 'required', 'yearPlaceholder', 'monthPlaceholder', 'dayPlaceholder', 'hourPlaceholder', 'minutePlaceholder', 'secondPlaceholder', 'closeWidgets'),
        package = 'dashMoreComponents'
        )

    structure(component, class = c('dash_component', 'list'))
}
