#!/usr/bin/env python3

import sys
import json

from nsl.stac import StacRequest, FloatFilter, GeometryData, ProjectionData
from nsl.stac.client import NSLClient
from epl.protobuf.v1.query_pb2 import GT


AOI = {
    "type": "Polygon",
    "coordinates": [
        [
            [-121.3, 37.9],
            [-120.0, 37.9],
            [-120.0, 37.0],
            [-121.3, 37.0],
            [-121.3, 37.9],
        ]
    ],
}

def main():
    nsl_client = NSLClient()
    request = StacRequest(
            limit=5,
            intersects=GeometryData(
                geojson=json.dumps(AOI),
                proj=ProjectionData(epsg=4326),
            ),
            gsd=FloatFilter(rel_type=GT, value=0.14),
    )

    try:
        response = nsl_client.search(request)
    except Exception as e:
        print(f"An error occurred during search: {e}")
        sys.exit(1)

    for item in response:
        print(item)


if __name__ == "__main__":
    main()
