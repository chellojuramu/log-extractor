# Log Extractor

A reusable Python utility to extract specific exception details from application log files.

This tool is designed to avoid manual log checking when repeated exception details need to be collected and shared.  
The main script is generic and reusable. All changeable values such as input file name, output file name, search keywords, and sample count are maintained in a separate configuration file.

## Purpose

This project helps to extract matching exception blocks from large log files based on configurable search criteria.

Example use cases:

- Extract HubSpot API 409 Conflict errors
- Extract duplicate contact creation exceptions
- Extract selected stack trace lines for reporting
- Generate a clean output file with sample exception details
- Reuse the same script for different clients or applications by only changing config values

## Project Structure

```text
log-extractor/
  config.py
  extract_log_exceptions.py
  README.md
  sample.log
