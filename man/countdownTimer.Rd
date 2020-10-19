% Auto-generated: do not edit by hand
\name{countdownTimer}

\alias{countdownTimer}

\title{CountdownTimer component}

\description{
This component is a countdown timer.  All times (starting duration,      remaining duration and countdown interval) are in seconds
}

\usage{
countdownTimer(id=NULL, starting_duration=NULL, pause=NULL, n_seconds=NULL,
remaining_duration=NULL)
}

\arguments{
\item{id}{Character. The ID of this component, used to identify dash components
in callbacks. The ID needs to be unique across all of the
components in an app.}

\item{starting_duration}{Numeric. The amount of time to count down in seconds}

\item{pause}{Logical. If True, the counter will no longer update. If False, the timer will resume.}

\item{n_seconds}{Numeric. Number of seconds elapsed}

\item{remaining_duration}{Numeric. remaining time left on countdown timer in seconds}
}

\value{named list of JSON elements corresponding to React.js properties and their values}

