# extract_log_exceptions.py

import config


def read_log_file(file_path):
    """Read log file and return all lines."""
    with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
        return file.readlines()


def is_start_line(line):
    """Check whether line is the starting line of required exception."""
    return (
        config.START_LINE_KEYWORD in line
        and config.START_LINE_END_KEYWORD in line
    )


def is_required_exception_line(line):
    """Check whether exception line matches all required keywords."""
    return all(keyword in line for keyword in config.EXCEPTION_KEYWORDS)


def is_required_stack_line(line):
    """Check whether stack trace line is useful for output."""
    return any(keyword in line for keyword in config.STACK_TRACE_KEYWORDS)


def extract_exception_blocks(lines):
    """Extract required exception blocks from log lines."""
    extracted_blocks = []

    for index, line in enumerate(lines):
        if not is_start_line(line):
            continue

        start_line = line.rstrip()
        exception_line = None
        stack_lines = []

        next_lines = lines[index + 1:index + 1 + config.LOOKAHEAD_LINES]

        for next_line in next_lines:
            clean_line = next_line.rstrip()

            if is_required_exception_line(clean_line):
                exception_line = clean_line
                continue

            if exception_line and is_required_stack_line(clean_line):
                stack_lines.append(clean_line)

            if exception_line and len(stack_lines) >= len(config.STACK_TRACE_KEYWORDS):
                break

        if exception_line:
            block = {
                "start_line": start_line,
                "exception_line": exception_line,
                "stack_lines": stack_lines
            }
            extracted_blocks.append(block)

        if len(extracted_blocks) >= config.MAX_SAMPLES:
            break

    return extracted_blocks


def write_output_file(blocks, output_file):
    """Write extracted exception blocks to output file."""
    with open(output_file, "w", encoding="utf-8") as file:
        if not blocks:
            file.write("No matching exceptions found.\n")
            return

        file.write(f"Total sample exceptions extracted: {len(blocks)}\n")
        file.write("=" * 100 + "\n\n")

        for number, block in enumerate(blocks, start=1):
            file.write(f"{number}.\n")
            file.write(block["start_line"] + "\n\n")
            file.write(block["exception_line"] + "\n\n")

            for stack_line in block["stack_lines"]:
                file.write(stack_line + "\n")

            file.write("\n" + "=" * 100 + "\n\n")


def main():
    lines = read_log_file(config.INPUT_LOG_FILE)
    blocks = extract_exception_blocks(lines)
    write_output_file(blocks, config.OUTPUT_FILE)

    print(f"Completed. Extracted {len(blocks)} exception sample(s).")
    print(f"Output file created: {config.OUTPUT_FILE}")


if __name__ == "__main__":
    main()