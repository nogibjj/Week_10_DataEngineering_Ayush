"""
Test Script for Main Code and Lib Files.
The main file calls the libs files hence no separate test file for libs.
"""

import subprocess
import os


def test_main():

    # check deletion of Data file
    result = subprocess.run(
        [
            "python",
            "main.py",
            "delete_data",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert "processed" in result.stdout
    assert not os.path.exists("./Data/Master.csv")

    # check creation of Data file
    result = subprocess.run(
        [
            "python",
            "main.py",
            "create_data",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert "processed" in result.stdout
    assert os.path.exists("./Data/Master.csv")

    # check spark query
    result = subprocess.run(
        [
            "python",
            "main.py",
            "query",
        ],
        capture_output=True,
        text=True,
        check=True,
    )

    assert "13207" in result.stdout


if __name__ == "__main__":
    test_main()
    pass
