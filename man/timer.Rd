% Auto-generated: do not edit by hand
\name{timer}

\alias{timer}

\title{Timer component}

\description{
A component that repeatedly increments a counter `n_intervals` with a fixed time delay between each increment. Interval is good for triggering a component on a recurring basis. The time delay is set with the property "interval" in milliseconds.
}

\usage{
timer(id=NULL, interval=NULL, disabled=NULL, n_intervals=NULL,
max_intervals=NULL, remaining_duration=NULL,
countdown_duration=NULL, reset=NULL)
}

\arguments{
\item{id}{Character. The ID of this component, used to identify dash components
in callbacks. The ID needs to be unique across all of the
components in an app.}

\item{interval}{Numeric. This component will increment the counter `n_intervals` every
`interval` milliseconds}

\item{disabled}{Logical. If True, the n_interval counter  and the remaining_duration no longer updates.  This pauses the timer.}

\item{n_intervals}{Numeric. Number of times the interval has passed (read-only)}

\item{max_intervals}{Numeric. Number of times the interval will be fired.
If -1, then the interval has no limit (the default)
and if 0 then the interval stops running.}

\item{remaining_duration}{Numeric. Number of milliseconds remaining on the timer.  (read-only)}

\item{countdown_duration}{Numeric. Sets the number of milliseconds the timer will run.  If -1 the duration has no limit (the default)
and if 0 then the timer stops running.}

\item{reset}{Logical. starts the timer at the beginning with the given prop settings.}
}

\value{named list of JSON elements corresponding to React.js properties and their values}

