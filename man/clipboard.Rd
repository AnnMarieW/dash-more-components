% Auto-generated: do not edit by hand
\name{clipboard}

\alias{clipboard}

\title{Clipboard component}

\description{
The Clipboard component copies text to the clipboard
}

\usage{
clipboard(id=NULL, target_id=NULL, title=NULL, style=NULL,
className=NULL)
}

\arguments{
\item{id}{Character. The ID used to identify this component.}

\item{target_id}{Character. id of target component containing text to copy to the clipboard.
 The inner text of the `children` prop will be copied to the clipboard.  If none, then the text from the
 `value` prop will be copied.}

\item{title}{Character. The text shown as a tooltip when hovering over the copy icon.}

\item{style}{Named list. The icon's styles}

\item{className}{Character. The class  name of the icon element}
}

\value{named list of JSON elements corresponding to React.js properties and their values}

