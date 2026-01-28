import json
from datetime import datetime


def parse_iso_timestamp(iso_ts):
    """
    Convert ISO 8601 timestamp to milliseconds since epoch.
    Example: 2021-03-15T10:15:30Z -> 1615803330000
    """
    dt = datetime.fromisoformat(iso_ts.replace("Z", "+00:00"))
    return int(dt.timestamp() * 1000)


def parse_format_1(data):
    """
    IMPLEMENT: Parse data from data-1.json format
    """
    result = {
        "deviceId": data["device"]["id"],
        "deviceType": data["device"]["type"],
        "timestamp": data["timestamp"],
        "location": {
            "lat": data["location"]["latitude"],
            "lon": data["location"]["longitude"]
        },
        "metrics": data["metrics"]
    }
    return result


def parse_format_2(data):
    """
    IMPLEMENT: Parse data from data-2.json format
    """
    result = {
        "deviceId": data["deviceId"],
        "deviceType": data["deviceType"],
        "timestamp": parse_iso_timestamp(data["time"]),
        "location": {
            "lat": data["lat"],
            "lon": data["lon"]
        },
        "metrics": data["metrics"]
    }
    return result


def main():
    with open("data-1.json") as f1:
        data1 = json.load(f1)

    with open("data-2.json") as f2:
        data2 = json.load(f2)

    parsed1 = parse_format_1(data1)
    parsed2 = parse_format_2(data2)

    # Write one unified result (example uses parsed1)
    with open("data-result.json", "w") as out:
        json.dump(parsed1, out, indent=2)


if __name__ == "__main__":
    main()
