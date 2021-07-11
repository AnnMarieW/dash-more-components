% Auto-generated: do not edit by hand
\name{timer}

\alias{timer}

\title{Timer component}

\description{
The Timer component has all the functionality of the Interval component plus the following additional features:  Operate in either `countdown` or `stopwatch` (count up) modes. Display custom messages, or start/stop jobs at specified times. Convert milliseconds into human readable times. Update messages clientside to help improve app performance. Specify the elapsed times to fire a callback rather than every interval
}

\usage{
timer(id=NULL, interval=NULL, disabled=NULL, n_intervals=NULL,
max_intervals=NULL, timer=NULL, mode=NULL, duration=NULL,
reset=NULL, fire_times=NULL, at_fire_time=NULL, rerun=NULL,
messages=NULL, timer_format=NULL, style=NULL,
class_name=NULL)
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
and if 0 then the timer stops running.}

\item{reset}{Logical. This will start the timer at the beginning with the given prop settings.}

\item{fire_times}{List of numerics. A list of the time(s) in milliseconds at which to fire a callback. This can be used to start a task at a given
time rather than using the timer. Since the timer is typically set at a small interval like one second, using
fire_times can reduce the number of times a callback is fired and can increase app performance. The time(s) must be a
multiple of the interval.}

\item{at_fire_time}{Numeric. This number is updated when the timer it reaches a time in the  fire_times property. (Read only)}

\item{rerun}{Logical. When True, the timer repeats once the timer has run for the number of milliseconds set in the duration.}

\item{messages}{Named list. Timer messages to be displayed by the component rather than showing the timer. It is a dictionary in the form of:
{integer: string} where integer is the time in milliseconds of when the string message is to be displayed.
Note: timer_format will override messages. For example, {10000 : "updating in 10 seconds"} will display the message
"updating in 10 seconds" once the timer equals 10000.}

\item{timer_format}{A value equal to: 'none', 'display', 'compact', 'verbose', 'colonnotation'. If a timer is displayed, it will override timer `messages`.  This formats the timer (milliseconds) into human
readable formats.  The options are:
 `'none'`: no timer will be displayed;
 `'display'`:  example - 1337000000 milliseconds will display as: '15d 11h 23m 20s';
 `'compact'`: will show only the first unit: 1h 10m → 1h ;
 `'verbose'`: will show full-length units. Example --  5 hours 1 minute 45 seconds
 `'colonNotation'`: Useful when you want to show time without the time units, similar to
                  a digital watch. Will always shows time in at least minutes: 1s → 0:01.
                  Example - 5h 1m 45s → 5:01:45.}

\item{style}{Named list. The messages styles}

\item{class_name}{Character. The class  name of the messages container}
}

\value{named list of JSON elements corresponding to React.js properties and their values}

