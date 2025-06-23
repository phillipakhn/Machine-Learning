import json
import pandas as pd

def location_data(json_path='Dataset/location-history.json'):
    with open(json_path, 'r') as file:
        data = json.load(file)

    records = []

    for entry in data:
        base = {
            "start_time": entry.get("startTime"),
            "end_time": entry.get("endTime")
        }

        if "activity" in entry:
            activity = entry["activity"]
            top = activity.get("topCandidate", {})
            records.append({
                **base,
                "type": "activity",
                "start_location": activity.get("start", "").replace("geo:", ""),
                "end_location": activity.get("end", "").replace("geo:", ""),
                "distance_m": float(activity.get("distanceMeters", "0")),
                "transport_type": top.get("type", "unknown"),
                "transport_prob": top.get("probability", None),
                "location": None,
                "semantic_type": None,
                "place_id": None,
                "visit_prob": None,
                "hierarchy_level": None,
            })

        elif "visit" in entry:
            visit = entry["visit"]
            top = visit.get("topCandidate", {})
            records.append({
                **base,
                "type": "visit",
                "start_location": None,
                "end_location": None,
                "distance_m": None,
                "transport_type": None,
                "transport_prob": None,
                "location": top.get("placeLocation", "").replace("geo:", ""),
                "semantic_type": top.get("semanticType", "unknown"),
                "place_id": top.get("placeID", ""),
                "visit_prob": top.get("probability", None),
                "hierarchy_level": visit.get("hierarchyLevel", None),
            })

    df = pd.DataFrame(records)
    
    # Convert to datetime
    df["start_time"] = pd.to_datetime(df["start_time"], errors='coerce', utc=True)
    df["end_time"] = pd.to_datetime(df["end_time"], errors='coerce', utc=True)

    # Ensure both are datetime64[ns]
    print("start_time dtype:", df["start_time"].dtype)
    print("end_time dtype:", df["end_time"].dtype)

    # Drop rows with invalid or missing times
    df = df.dropna(subset=["start_time", "end_time"])
    df = df[df["end_time"] > df["start_time"]]

    # Compute duration using .dt
    df["duration_min"] = (df["end_time"] - df["start_time"]).dt.total_seconds() / 60

    return df