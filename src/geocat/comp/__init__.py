# move functions into geocat.comp namespace
from .climatologies import anomaly, climatology, month_to_season, calendar_average, climatology_average
from .crop import (actual_saturation_vapor_pressure, max_daylight,
                   psychrometric_constant, saturation_vapor_pressure,
                   saturation_vapor_pressure_slope)
from .eofunc import eofunc, eofunc_eofs, eofunc_pcs, eofunc_ts
from .errors import (AttributeError, ChunkError, CoordinateError,
                     DimensionError, Error, MetaError)
from .fourier_filters import (fourier_band_block, fourier_band_pass,
                              fourier_filter, fourier_high_pass,
                              fourier_low_pass)
from .gradient import gradient, arc_lon_wgs84, arc_lat_wgs84, rad_lat_wgs84
from .interpolation import interp_hybrid_to_pressure, interp_sigma_to_hybrid, interp_multidim
from .polynomial import detrend, ndpolyfit, ndpolyval
from .meteorology import dewtemp, heat_index, relhum, relhum_ice, relhum_water
from .skewt_params import get_skewt_vars, showalter_index
from .spherical import decomposition, recomposition, scale_voronoi
from .stats import pearson_r

# bring all functions from geocat.f2py into the geocat.comp namespace
try:
    from geocat.f2py import *
except ImportError:
    pass
