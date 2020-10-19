% Auto-generated: do not edit by hand
\name{timepicker}

\alias{timepicker}

\title{Timepicker component}

\description{
TODO:  Remove https://github.com/arqex/react-datetime - it takes a lot of space.              necessary to add className?  if sim test array of strings - classname            how to use{...}  ?            necessary to specify all vars in div in return?
}

\usage{
timepicker(id=NULL, value=NULL, format=NULL, maxDetail=NULL,
maxTime=NULL, minTime=NULL, disabled=NULL,
disableClock=NULL, locale=NULL)
}

\arguments{
\item{id}{Character. The ID used to identify this component in Dash callbacks.}

\item{value}{Character. value is the selected time}

\item{format}{Character. Input format based on Unicode Technical Standard #35. Supported values are: H, HH, h, hh, m, mm, s, ss, a.
     example: h:m:s a}

\item{maxDetail}{A value equal to: 'hour', 'minute', 'second'. (string, one of 'hour', 'minute', 'second, Default: 'minute')
  The level of detail to show on the time picker.}

\item{maxTime}{Character. Maximum time the user can select}

\item{minTime}{Character. Minimum time the user can select}

\item{disabled}{Logical. Whether the time picker should be disables}

\item{disableClock}{Logical. When set to true will remove the clock and the button toggling its visibility}

\item{locale}{Character. Locale that should be used by the time picker and the clock.  Can be any
IEFE language tag. https://en.wikipedia.org/wiki/IETF_language_tag
Default from User's browser settings.}
}

\value{named list of JSON elements corresponding to React.js properties and their values}

