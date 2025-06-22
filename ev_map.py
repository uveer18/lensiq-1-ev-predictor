#ev mapping tool of EXIF Predictor module of LensIQ Suite 


def ev_scene(ev, nd_stops=0):
    adjusted_ev = round(ev + nd_stops)
    mapping = {
        -3: "Candlelight (very dim)",
        -2: "Full moonlight",
        -1: "Dim night street",
         0: "Night city w/ lamps",
         1: "Twilight (blue hour)",
         2: "Moody candlelit indoor",
         3: "Bar/restaurant lighting",
         4: "Bright indoor w/ windows",
         5: "Window-lit overcast scene",
         6: "Overcast outdoor",
         7: "Open shade, late evening",
         8: "Cloudy daylight",
         9: "Shade on sunny day",
        10: "Soft daylight",
        11: "Sunny daylight",
        12: "Bright beach or sand",
        13: "Snow in sun",
        14: "Reflective water / mountains",
        15: "Direct noon sun (extreme brightness)"
    }
    return mapping.get(adjusted_ev, f"EV {adjusted_ev} scene not defined")