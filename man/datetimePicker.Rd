% Auto-generated: do not edit by hand
\name{datetimePicker}

\alias{datetimePicker}

\title{DatetimePicker component}

\description{
TODO:
}

\usage{
datetimePicker(id=NULL, value=NULL, format=NULL, maxDetail=NULL,
minDetail=NULL, maxTime=NULL, minTime=NULL, maxDate=NULL,
minDate=NULL, disabled=NULL, disableClock=NULL, locale=NULL,
returnValue=NULL)
}

\arguments{
\item{id}{Character. The ID used to identify this component in Dash callbacks.}

\item{value}{Character. value is the selected time}

\item{format}{Character. Input format based on Unicode Technical Standard #35. 
Supported values are: y, M, MM, MMM, MMMM, d, dd, H, HH, h, hh, m, mm, s, ss, a
     
     example:  y-MM-dd h:mm:ss a}

\item{maxDetail}{A value equal to: 'hour', 'minute', 'second'. (string, one of 'hour', 'minute', 'second, Default: 'minute')
  The level of detail to show on the datetime picker. View defined here also becomes the one on which
  clicking an item in the calendar will select a date.}

\item{minDetail}{A value equal to: "month", "year", "decade", "century". The least detailed calendar view that the user shall see.}

\item{maxTime}{Character. Maximum time the user can select}

\item{minTime}{Character. Minimum time the user can select}

\item{maxDate}{Character. }

\item{minDate}{Character. }

\item{disabled}{Logical. Whether the time picker should be disables}

\item{disableClock}{Logical. When set to true will remove the clock and the button toggling its visibility}

\item{locale}{Character. Locale that should be used by the time picker and the clock.  Can be any
IEFE language tag. https://en.wikipedia.org/wiki/IETF_language_tag
Default from User's browser settings.}

\item{returnValue}{A value equal to: "start", "end", "range". Which dates shall be passed by the calendar to the onChange function and onClick{Period} functions.
Can be "start", "end" or "range". The latter will cause an array with start and end values to be passed.}
}

\value{named list of JSON elements corresponding to React.js properties and their values}

