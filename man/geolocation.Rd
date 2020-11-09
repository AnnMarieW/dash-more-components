% Auto-generated: do not edit by hand
\name{geolocation}

\alias{geolocation}

\title{Geolocation component}

\description{
The CurrentLocation component gets geolocation of the device from the web browser.  See more info here: https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API
}

\usage{
geolocation(id=NULL, local_date=NULL, timestamp=NULL, position=NULL,
position_error=NULL, show_alert=NULL, watch_position=NULL,
update_now=NULL, high_accuracy=NULL, maximum_age=NULL,
timeout=NULL)
}

\arguments{
\item{id}{Character. The ID used to identify this component in Dash callbacks.}

\item{local_date}{Character. The local date and time when the device position was updated.
Format:  MM/DD/YYYY, hh:mm:ss p   where p is AM or PM}

\item{timestamp}{Numeric. The Unix timestamp in seconds from when the position was updated}

\item{position}{Lists containing elements 'lat', 'lon', 'accuracy', 'alt', 'altaccuracy', 'heading', 'speed'.
those elements have the following types:
  - lat (numeric; optional)
  - lon (numeric; optional)
  - accuracy (numeric; optional)
  - alt (numeric; optional)
  - altaccuracy (numeric; optional)
  - heading (numeric; optional)
  - speed (numeric; optional). (dict)The position of the device.  Lat, lon, and accuracy will always be returned.  The other data will be included
when available, otherwise it will be NaN.
A dictionary with the following keys:
      lat:  latitude in degrees,
      lon: longitude in degrees,
      accuracy: accuracy of the lat/lon in meters,

      When available:
      alt:  altitude above mean sea level in meters,
      altAccuracy:  accuracy of the altitude  in meters,
      heading: compass heading in degrees,
      speed:  speed in meters per sec,}

\item{position_error}{Lists containing elements 'code', 'message'.
those elements have the following types:
  - code (numeric; optional)
  - message (character; optional). Position error}

\item{show_alert}{Logical. If true, error messages will be displayed as an alert}

\item{watch_position}{Logical. (boolean; default False).  If false, position is obtained as an asynchronous request.  If true, then  position data
is updated when either the location changes or more accurate information becomes available}

\item{update_now}{Logical. (boolean; default False).  Forces a one-time update to the position data.   If set to True in a callback, the browser
  will update the position data and reset update_now back to False.  This can, for example, be used to update the
 position with a button or an interval timer.}

\item{high_accuracy}{Logical. (boolean; default False).   If true and if the device is able to provide a more accurate position,
 it will do so. Note that this can result in slower response times or increased power consumption (with a GPS
 chip on a mobile device for example). If false (the default value), the device can save resources by
 responding more quickly and/or using less power.}

\item{maximum_age}{Numeric. The maximum age in milliseconds of a possible cached position that is acceptable to return. If set to 0,
it means that the device cannot use a cached position and must attempt to retrieve the real current position.
If set to Infinity the device must return a cached position regardless of its age. Default: 0.}

\item{timeout}{Numeric. The maximum length of time (in milliseconds) the device is allowed to take in order to return a position.
The default value is Infinity, meaning that data will not be return until the position is available.}
}

\value{named list of JSON elements corresponding to React.js properties and their values}

