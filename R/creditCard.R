# AUTO GENERATED FILE - DO NOT EDIT

creditCard <- function(id=NULL, cvc=NULL, expiry=NULL, focus=NULL, name=NULL, number=NULL, locale=NULL) {
    
    props <- list(id=id, cvc=cvc, expiry=expiry, focus=focus, name=name, number=number, locale=locale)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'CreditCard',
        namespace = 'dash_more_components',
        propNames = c('id', 'cvc', 'expiry', 'focus', 'name', 'number', 'locale'),
        package = 'dashMoreComponents'
        )

    structure(component, class = c('dash_component', 'list'))
}
