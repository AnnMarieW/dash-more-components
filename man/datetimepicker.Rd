% Auto-generated: do not edit by hand
\name{datetimepicker}

\alias{datetimepicker}

\title{Datetimepicker component}

\description{
TODO:  more checking for valid dates.
}

\usage{
datetimepicker(id=NULL, value=NULL, setValue=NULL, format=NULL,
maxDetail=NULL, minDetail=NULL, maxTime=NULL, minTime=NULL,
maxDate=NULL, minDate=NULL, disabled=NULL,
disableClock=NULL, locale=NULL, returnValue=NULL)
}

\arguments{
\item{id}{Character. The ID used to identify this component in Dash callbacks.}

\item{value}{Logical | numeric | character | named list | unnamed list. value is the selected datetime.   type:  datetime objec}

\item{setValue}{Logical | numeric | character | named list | unnamed list. string value of date.  from app. need to convert to datetime object}

\item{format}{Character. Input format based on Unicode Technical Standard #35.  This changes how the date and time is displayed.
Supported values are: y, M, MM, MMM, MMMM, d, dd, H, HH, h, hh, m, mm, s, ss, a
     
     example:  y-MM-dd h:mm:ss a   isodate:y-MM-dd HH:mm:ss}

\item{maxDetail}{A value equal to: 'hour', 'minute', 'second'. (string, one of 'hour', 'minute', 'second, Default: 'minute')
  The level of detail to show on the datetime picker. View defined here also becomes the one on which
  clicking an item in the calendar will select a date.}

\item{minDetail}{A value equal to: "month", "year", "decade", "century". The least detailed calendar view that the user shall see.}

\item{maxTime}{Character. Maximum time the user can select}

\item{minTime}{Character. Minimum time the user can select}

\item{maxDate}{Character. Maximum date that the user can select. Periods partially overlapped by maxDate will also be selectable,
although React-DateTime-Picker will ensure that no later date is selected.}

\item{minDate}{Character. Minimum date that the user can select. Periods partially overlapped by minDate will also be selectable,
although React-DateTime-Picker will ensure that no earlier date is selected.}

\item{disabled}{Logical. Whether the time picker should be disables}

\item{disableClock}{Logical. When set to true will remove the clock and the button toggling its visibility}

\item{locale}{Character. Locale that should be used by the time picker and the clock.  Can be any
IEFE language tag. https://en.wikipedia.org/wiki/IETF_language_tag
Default from User's browser settings.}

\item{returnValue}{A value equal to: "start", "end", "range". Which dates shall be passed by the calendar to the onChange function and onClick{Period} functions.
Can be "start", "end" or "range". The latter will cause an array with start and end values to be passed.}
}

\value{named list of JSON elements corresponding to React.js properties and their values}

