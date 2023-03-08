"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_acp.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow

#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.
#


def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
       brevet_dist_km: number, nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An arrow object
    Returns:
       An arrow object indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    if control_dist_km == 0 or control_dist_km > (brevet_dist_km * 1.2):
      hours, minutes = 0, 0 # figure out how
      return brevet_start_time.shift(hours=hours, minutes=minutes)

    if control_dist_km >= brevet_dist_km and control_dist_km <= (brevet_dist_km * 1.2):
      if brevet_dist_km == 200:
        return brevet_start_time.shift(hours=5, minutes=53)

      if brevet_dist_km == 300:
        return brevet_start_time.shift(hours=9)

      if brevet_dist_km == 400:
        return brevet_start_time.shift(hours=12, minutes=8)

      if brevet_dist_km == 600:
        return brevet_start_time.shift(hours=18, minutes=48)

      if brevet_dist_km == 1000:
        return brevet_start_time.shift(hours=33, minutes=5)

    if control_dist_km > 0 and control_dist_km <= 200:
      holder = (control_dist_km / 34)
      fraction = holder - int(holder)
      hour_val = int(holder)
      minute_val = round(fraction * 60)
      hours, minutes = hour_val, minute_val # figure out how
      return brevet_start_time.shift(hours=hours, minutes=minutes)

    if control_dist_km > 200 and control_dist_km <= 400:
      holder = ((control_dist_km - 200) / 32)
      fraction = holder - int(holder)
      hour_val = int(holder)
      minute_val = round((fraction * 60)-.01)
      hours, minutes = hour_val, minute_val # figure out how
      return brevet_start_time.shift(hours=hours + 5, minutes=minutes + 53)

    if control_dist_km > 400 and control_dist_km <= 600:
      holder = ((control_dist_km - 400) / 30)
      fraction = holder - int(holder)
      hour_val = int(holder)
      minute_val = round(fraction * 60)
      hours, minutes = hour_val, minute_val # figure out how
      return brevet_start_time.shift(hours=hours + 12, minutes=minutes + 8)

    if control_dist_km > 600 and control_dist_km <= 1000:
      holder = ((control_dist_km - 600) / 28)
      fraction = holder - int(holder)
      hour_val = int(holder)
      minute_val = round(fraction * 60)
      hours, minutes = hour_val, minute_val # figure out how
      return brevet_start_time.shift(hours=hours + 18, minutes=minutes + 48)

    if control_dist_km > 1000 and control_dist_km <= 1300:
      holder = ((control_dist_km - 1000) / 26)
      fraction = holder - int(holder)
      hour_val = int(holder)
      minute_val = round(fraction * 60)
      hours, minutes = hour_val, minute_val # figure out how
      return brevet_start_time.shift(hours=hours + 33, minutes=minutes + 5)

def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
          brevet_dist_km: number, nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An arrow object
    Returns:
       An arrow object indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    if control_dist_km > (brevet_dist_km * 1.2):
      hours, minutes = 0, 0 # figure out how
      return brevet_start_time.shift(hours=hours, minutes=minutes)

    if control_dist_km == 0:
      hours, minutes = 1, 0 # figure out how
      return brevet_start_time.shift(hours=hours, minutes=minutes)

    if control_dist_km >= brevet_dist_km and control_dist_km <= (brevet_dist_km * 1.2):
      if brevet_dist_km == 200:
        return brevet_start_time.shift(hours=13, minutes=30)

      if brevet_dist_km == 300:
        return brevet_start_time.shift(hours=20)

      if brevet_dist_km == 400:
        return brevet_start_time.shift(hours=27)

      if brevet_dist_km == 600:
        return brevet_start_time.shift(hours=40)

      if brevet_dist_km == 1000:
        return brevet_start_time.shift(hours=75)

    if control_dist_km > 0 and control_dist_km <= 60:
      holder = (control_dist_km / 20)
      fraction = holder - int(holder)
      hour_val = int(holder) + 1
      minute_val = round(fraction * 60)
      hours, minutes = hour_val, minute_val # figure out how
      return brevet_start_time.shift(hours=hours, minutes=minutes)

    if control_dist_km > 60 and control_dist_km <= 200:
      holder = (control_dist_km / 15)
      fraction = holder - int(holder)
      hour_val = int(holder)
      minute_val = round(fraction * 60)
      hours, minutes = hour_val, minute_val # figure out how
      return brevet_start_time.shift(hours=hours, minutes=minutes)

    if control_dist_km > 200 and control_dist_km <= 400:
      holder = ((control_dist_km - 200)/ 15)
      fraction = holder - int(holder)
      hour_val = int(holder)
      minute_val = round(fraction * 60)
      hours, minutes = hour_val, minute_val # figure out how
      return brevet_start_time.shift(hours=hours + 13, minutes=minutes + 20)

    if control_dist_km > 400 and control_dist_km <= 600:
      holder = ((control_dist_km - 400) / 15)
      fraction = holder - int(holder)
      hour_val = int(holder)
      minute_val = round(fraction * 60)
      hours, minutes = hour_val, minute_val # figure out how
      return brevet_start_time.shift(hours=hours + 26, minutes=minutes + 40)

    if control_dist_km > 600 and control_dist_km <= 1000:
      holder = ((control_dist_km - 600) / 11.428)
      fraction = holder - int(holder)
      hour_val = int(holder)
      minute_val = round(fraction * 60)
      hours, minutes = hour_val, minute_val # figure out how
      return brevet_start_time.shift(hours=hours + 40, minutes=minutes)

    if control_dist_km > 1000 and control_dist_km <= 1300:
      holder = ((control_dist_km - 1000) / 13.333)
      fraction = holder - int(holder)
      hour_val = int(holder)
      minute_val = round(fraction * 60)
      hours, minutes = hour_val, minute_val # figure out how
      return brevet_start_time.shift(hours=hours + 75, minutes=minutes)