#!/usr/bin/env python3

import argparse
import glob
import os
import json
import datetime

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def day_from_filename(path):
    base = os.path.basename(path)
    date_part = base.split(".zip")[0].replace("geoTwitter", "")
    return datetime.datetime.strptime(date_part, "%y-%m-%d").date()


parser = argparse.ArgumentParser()
parser.add_argument("hashtags", nargs="+")
parser.add_argument("--glob", default="outputs/*.lang")
parser.add_argument("--out", default="plots/hashtag_timeseries.png")
args = parser.parse_args()

paths = sorted(glob.glob(args.glob))
if not paths:
    raise SystemExit("No daily files found")

dates = [day_from_filename(p) for p in paths]
series = {h: [] for h in args.hashtags}

for p in paths:
    with open(p) as f:
        counts = json.load(f)

    for h in args.hashtags:
        d = counts.get(h, {})
        if isinstance(d, dict):
            series[h].append(sum(d.values()) + 1)
        else:
            series[h].append(0)

os.makedirs(os.path.dirname(args.out), exist_ok=True)

plt.figure(figsize=(10,6))
for h in args.hashtags:
    plt.plot(dates, series[h], label=h)

plt.xlabel("Day of year (2020)")
plt.ylabel("Tweet count (log scale, +1)")
plt.yscale("log")

plt.legend()
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(args.out, dpi=200)

print("saved", args.out)
