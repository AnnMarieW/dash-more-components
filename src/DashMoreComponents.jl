
module DashMoreComponents
using Dash

const resources_path = realpath(joinpath( @__DIR__, "..", "deps"))
const version = "0.0.1"

include("countdowntimer.jl")
include("creditcard.jl")
include("datetimepicker.jl")
include("geolocation.jl")
include("timepicker.jl")
include("timer.jl")

function __init__()
    DashBase.register_package(
        DashBase.ResourcePkg(
            "dash_more_components",
            resources_path,
            version = version,
            [
                DashBase.Resource(
    relative_package_path = "dash_more_components.min.js",
    external_url = nothing,
    dynamic = nothing,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "dash_more_components.min.js.map",
    external_url = nothing,
    dynamic = true,
    async = nothing,
    type = :js
)
            ]
        )

    )
end
end
