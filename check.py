"""Fixture checker for Souk's Busy Forest: passes a JSON file whose "answer" is 42."""
import json
import sys

sys.exit(0 if json.load(open(sys.argv[1])).get("answer") == 42 else 1)
