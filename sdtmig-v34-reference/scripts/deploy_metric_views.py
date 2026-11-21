#!/usr/bin/env python3
"""Create the SDTM metric views from assets/metric-views/sdtm_metric_views.sql.

Usage (local, Databricks Connect on serverless):
    python deploy_metric_views.py --sdtm main.sdtm --target main.sdtm_metrics --profile <profile>
    python deploy_metric_views.py --sdtm main.sdtm --target main.sdtm_metrics --print   # just render the SQL
In a Databricks notebook omit --profile; the active Spark session is used.
"""
import argparse
import re
from pathlib import Path

TEMPLATE = Path(__file__).resolve().parent.parent / "assets" / "metric-views" / "sdtm_metric_views.sql"


def render(sdtm: str, target: str) -> list[str]:
    for name in (sdtm, target):
        if not re.fullmatch(r"[A-Za-z0-9_`]+\.[A-Za-z0-9_`]+", name):
            raise ValueError(f"expected catalog.schema, got {name!r}")
    sql = TEMPLATE.read_text().replace("{{SDTM_SCHEMA}}", sdtm).replace("{{TARGET_SCHEMA}}", target)
    return [s.strip() for s in re.split(r"(?<=\$\$);\s*\n", sql) if "CREATE" in s]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--sdtm", required=True, help="catalog.schema with the SDTM tables")
    ap.add_argument("--target", required=True, help="catalog.schema for the metric views")
    ap.add_argument("--profile", help="Databricks CLI profile (Databricks Connect, serverless)")
    ap.add_argument("--print", action="store_true", help="print rendered SQL instead of executing")
    a = ap.parse_args(argv)
    stmts = render(a.sdtm, a.target)
    if a.print:
        print(";\n\n".join(s.rstrip(";") for s in stmts) + ";")
        return 0
    if a.profile:
        from databricks.connect import DatabricksSession
        spark = DatabricksSession.builder.profile(a.profile).serverless(True).getOrCreate()
    else:
        from pyspark.sql import SparkSession
        spark = SparkSession.builder.getOrCreate()
    spark.sql(f"CREATE SCHEMA IF NOT EXISTS {a.target} COMMENT 'Metric views over SDTM tables in {a.sdtm}'")
    failed = 0
    for s in stmts:
        name = re.search(r"VIEW\s+(\S+)", s).group(1)
        try:
            spark.sql(s.rstrip(";"))
            print(f"created {name}")
        except Exception as e:  # report every view, then fail
            failed += 1
            print(f"FAILED  {name}: {str(e).splitlines()[0][:400]}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
