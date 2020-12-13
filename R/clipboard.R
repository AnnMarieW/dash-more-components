# AUTO GENERATED FILE - DO NOT EDIT

clipboard <- function(id=NULL, target_id=NULL) {
    
    props <- list(id=id, target_id=target_id)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Clipboard',
        namespace = 'dash_more_components',
        propNames = c('id', 'target_id'),
        package = 'dashMoreComponents'
        )

    structure(component, class = c('dash_component', 'list'))
}
