% Auto-generated: do not edit by hand
\name{currentLocation}

\alias{currentLocation}

\title{CurrentLocation component}

\description{
The CurrentLocation component gets geolocation of device from the web browser.  See more info here: https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API
}

\usage{
currentLocation(id=NULL, local_date=NULL, timestamp=NULL, position=NULL,
position_error=NULL, watch_position=NULL, update_now=NULL,
high_accuracy=NULL, maximum_age=NULL, timeout=NULL)
}

\arguments{
\item{id}{Character. The ID used to identify this component in Dash callbacks.}

\item{local_date}{Character. The local date and time when the device position was updated.
Format:  MM/DD/YYYY, hh:mm:ss p   where p is AM or PM}

\item{timestamp}{Numeric. timestamp}

\item{position}{Lists containing elements 'latitude', 'longitude', 'altitude', 'accuracy', 'altitudeaccuracy', 'heading', 'speed'.
those elements have the following types:
  - latitude (numeric; optional)
  - longitude (numeric; optional)
  - altitude (numeric; optional)
  - accuracy (numeric; optional)
  - altitudeaccuracy (numeric; optional)
  - heading (numeric; optional)
  - speed (numeric; optional). The position of the device}

\item{position_error}{Lists containing elements 'code', 'message'.
those elements have the following types:
  - code (numeric; optional)
  - message (character; optional). Position error}

\item{watch_position}{Logical. (boolean; default False).  If false, position is obtained as an asynchronous request.  If true, then  position data
is updated when either the location changes or more accurate information becomes available}

\item{update_now}{Logical. (boolean; default False).  Forces a one-time update to the position data.   If set to True in a callback, the browser
  will update the position data and reset update_now back to False.  This can, for example, to update the position
 with a button click or an interval timer.}

\item{high_accuracy}{Logical. (boolean; default False).   If true and if the device is able to provide a more accurate position,
 it will do so. Note that this can result in slower response times or increased power consumption (with a GPS
 chip on a mobile device for example). If false (the default value), the device can take
 the liberty to save resources by responding more quickly and/or using less power.}

\item{maximum_age}{Numeric. }

\item{timeout}{Numeric. }
}

\value{named list of JSON elements corresponding to React.js properties and their values}

