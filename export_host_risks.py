import pickle
from datetime import datetime, date

from censys.asm import Events, HostsAssets
from censys.common.exceptions import CensysHostNotFoundException

IGNORE_LASTRUN = True
# --- functions ---

def load_lastrun():
    try:
        with open ('lastrun', 'rb') as fp:
            return pickle.load(fp)
    except FileNotFoundError:
        return None


def save_lastrun():
    with open('lastrun', 'wb') as fp:
        ct = datetime.now()
        ct_formatted = ct.strftime('%Y-%m-%dT%H:%M:%SZ')
        pickle.dump(ct_formatted, fp)

# --- main thread ---

# it is worth noting that there will be an API endpoint soon at "/api/v2/risks" that will have full filtering capabilities for risks
# until then, we can grab host risks via the logbook and then enrich that using asset info (https://censys-python.readthedocs.io/en/stable/usage-asm.html#assets)
e = Events()
h = HostsAssets()

lastrun = load_lastrun()
if IGNORE_LASTRUN:
    lastrun = None

if lastrun == None:
    print("Getting all added host risks.")
    cursor = e.get_cursor(filters=["HOST_RISK"])
else:
    print("Getting all added host risks since "+lastrun)
    cursor = e.get_cursor(lastrun, filters=["HOST_RISK"])

events = e.get_events(cursor)
save_lastrun()

for event in events:
    # only show logbook events with the 'add' tag
    if event["operation"] == "ADD":
        print(event)

        try:
            # enrich the data of this host_risk with more data from the host itself
            host = h.get_asset_by_id(event["entity"]["ipAddress"])
            print(host)
        except CensysHostNotFoundException:
            pass

        # remove this if you want to loop through all host risks
        # break

#consolidate and export to a csv as you wish