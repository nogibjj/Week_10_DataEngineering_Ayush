"""
Query Scripts Using SQLite and Python which can be exceuted via CLI
"""

# Import libraries
import sys
import argparse

sys.path.insert(0, "./mylib")

# Import Custom Libraries functions
from mylib.logs import clear_log, write_log  # noqa: E402
from mylib.data_csv import create_data, delete_data  # noqa: E402
from mylib.lib_spark import create_spark, end_spark, query  # noqa: E402


def handle_arguments(args):
    """To Handle Query Arguments"""
    parser = argparse.ArgumentParser(description="Data Processing Using Spark")
    parser.add_argument(
        "action",
        choices=[
            "create_data",
            "delete_data",
            "clear_log",
            "query",
        ],
    )
    args = parser.parse_args(args[:1])
    print(args.action)
    if args.action == "create_data":
        parser.add_argument(
            "source",
            type=str,
            nargs="?",
            default="https://github.com/Opensourcefordatascience/Data-sets/raw/master/automotive_data.csv",
        )
        parser.add_argument("file_name", type=str, nargs="?", default="Master.csv")
        parser.add_argument("auto", type=str, nargs="?", default="T")
    elif args.action == "delete_data":
        parser.add_argument("file_name", type=str, nargs="?", default="Master.csv")
        parser.add_argument("auto", type=str, nargs="?", default="T")
    elif args.action == "clear_log":
        parser.add_argument("log_file", type=str, nargs="?", default="./query_logs.md")
    elif args.action == "query":
        parser.add_argument(
            "query", type=str, nargs="?", default="SELECT AVG(price) from df"
        )

    # parse again with ever
    return parser.parse_args(sys.argv[1:])


def main():
    """To execute functions in order"""
    args = handle_arguments(sys.argv[1:])

    if args.action == "create_data":
        print("processing...")
        create_data(args.source, args.file_name, args.auto)
        return "processed"
    elif args.action == "delete_data":
        print("processing...")
        delete_data(args.file_name, args.auto)
        return "processed"
    elif args.action == "clear_log":
        print("processing...")
        clear_log(args.log_file)
        return "processed"
    elif args.action == "query":

        # start the spark session
        spark = create_spark("SparkSession")
        write_log("Spark Session Created")

        # read the csv into spark Dataframe
        df = spark.read.csv("./Data/Master.csv", header=True, inferSchema=True)
        write_log("CSV Read into Spark Dataframe")

        # execute the query
        query(spark, df, args.query, "df")
        write_log(f"{args.query} Executed")

        # stop the spark session
        end_spark(spark)
        write_log("Spark Session Stopped")

    else:
        return f"Unknown Input: {args.action}"


if __name__ == "__main__":
    print(main())
