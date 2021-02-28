# AUTO GENERATED FILE - DO NOT EDIT

clipboard <- function(id=NULL, target_id=NULL, title=NULL, style=NULL, className=NULL) {
    
    props <- list(id=id, target_id=target_id, title=title, style=style, className=className)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Clipboard',
        namespace = 'dash_more_components',
        propNames = c('id', 'target_id', 'title', 'style', 'className'),
        package = 'dashMoreComponents'
        )

    structure(component, class = c('dash_component', 'list'))
}
