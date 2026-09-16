# Reference logger

Status: specification only. The code is written in week 4.

## Purpose

The logger exists to show that the logging, lineage and tamper evidence requirements in the standard are cheap to meet. It is a proof of cost, not a product. It uses only the Python standard library and stays under 300 lines across all files.

## Files

| File | What it does |
|---|---|
| `logger.py` | Three commands. `append` takes a sensor id and a JSON payload and writes one reading record to an append only JSONL file. `alert` writes an alert record that lists the seq numbers of the readings it was derived from. `export` writes the whole log as CSV for the farmer. |
| `verify.py` | Walks the chain, recomputes every hash, reports the first broken link if there is one, and checks that every alert references readings that exist and come before it. |
| `demo.py` | Writes 1,000 readings and 10 alerts, verifies the log, edits one reading in place, and shows the verifier catching the edit. |

## Record format

| Field | Meaning |
|---|---|
| `seq` | Position in the log, starting at 0, with no gaps |
| `ts_utc` | Time of writing, ISO 8601 in UTC |
| `sensor_id` | The sensor or device the reading came from |
| `payload` | The reading or the alert body as JSON |
| `model_version` | Version of the model or rule set that produced the record |
| `prev_hash` | The hash of the previous record, or a fixed genesis value for the first |
| `hash` | SHA 256 over the concatenation of seq, ts_utc, sensor_id, payload, model_version and prev_hash, in that order |

The exact serialisation is fixed when the code is written in week 4: a field separator, and JSON with sorted keys and no spaces for the payload. Without both, two different records could hash the same.

## Requirement to feature mapping

Filled in when the code exists, with the line count.

| Dimension | Feature that satisfies it |
|---|---|
| Indicator validity | |
| Validation evidence | |
| Logging | |
| Data lineage | |
| Access and ownership | |
| Tamper evidence | |
| Disclosure | |
