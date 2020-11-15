% Auto-generated: do not edit by hand
\name{timer}

\alias{timer}

\title{Timer component}

\description{
A component that repeatedly increments a counter `n_intervals` with a fixed time delay between each increment. Interval is good for triggering a component on a recurring basis. The time delay is set with the property "interval" in milliseconds.
}

\usage{
timer(id=NULL, interval=NULL, disabled=NULL, n_intervals=NULL,
max_intervals=NULL, timer=NULL, mode=NULL, duration=NULL,
reset=NULL, messages=NULL, timer_format=NULL)
}

\arguments{
\item{id}{Character. The ID of this component, used to identify dash components
in callbacks. The ID needs to be unique across all of the
components in an app.}

\item{interval}{Numeric. This component will increment the counter `n_intervals` every
`interval` milliseconds}

\item{disabled}{Logical. If True, the n_interval counter  and the timer no longer updates.  This pauses the timer.}

\item{n_intervals}{Numeric. Number of times the interval has passed (read-only)}

\item{max_intervals}{Numeric. Number of times the interval will be fired.
If -1, then the interval has no limit (the default)
and if 0 then the interval stops running.}

\item{timer}{Numeric. When in countdown mode, the timer will count down to zero from the starting `duration` and will show the number
 of milliseconds remaining.
 When in stopwatch mode, the timer will count up from zero and show the number of milliseconds elapsed.
 (read-only)}

\item{mode}{A value equal to: 'stopwatch', 'countdown'. The timer will count down to zero in `countdown` mode and count up from zero in `stopwatch` mode}

\item{duration}{Numeric. Sets the number of milliseconds the timer will run.  If -1 the timer will not be limited by the duration. (the default)
and if 0 then the timer stops running but may be reset.}

\item{reset}{Logical. This will start the timer at the beginning with the given prop settings.}

\item{messages}{Named list. Timer messages to be displayed by the component rather than the timer. It is a dictionary in the form of:
 { integer: string} where integer is the time in milliseconds of when the `string` message is to be displayed.
for example, {10000 : "updating in 10 seconds"} will display the message "updating in 10 seconds" once the
timer equals 10000
Note:  `timer_format` will override `messages`.}

\item{timer_format}{Lists containing elements 'display', 'compact', 'verbose', 'colonnotation'.
those elements have the following types:
  - display (logical; optional): if false, then no timer will be displayed.  timer `messages` will be displayed (if any)  default: false
  - compact (logical; optional): shows a compact timer display.  default: false
if true, it will only show the first unit: 1h 10m → 1h.
  - verbose (logical; optional): verbose will display full-length units. default: false
 example - if true: 5h 1m 45s → 5 hours 1 minute 45 seconds
  - colonnotation (logical; optional): display time in a colon notation. default: false
example - if true:  5h 1m 45s → 5:01:45.
will always shows time in at least minutes: 1s → 0:01
useful when you want to display time without the time units, similar to a digital watch.. If a timer is displayed, it will override timer `messages`.  This formats the timer (milliseconds) into human
readable formats.  For example: 1337000000 milliseconds will display as: '15d 11h 23m 20s'.  This may be changed
using the following options:}
}

\value{named list of JSON elements corresponding to React.js properties and their values}
